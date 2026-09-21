#!/usr/bin/env python3
"""export.py — the corpus as spreadsheets.

    python3 tools/export.py            # write data/*.csv
    python3 tools/export.py --check    # fail if the committed CSVs are stale

**Why CSV and not just the database.** The `.sqlite` is a binary blob: git cannot
diff it, a reviewer cannot read it, and a spreadsheet is what a person actually
opens. So the database is gitignored and these exports are committed. The
property that buys is worth the duplication — **every future change to the
manuscript shows up as a diff in the data**, the same way `glossary/INDEX.md`
already makes a lock change visible.

**Standing rule 0 is enforced here, not merely intended.** `--check` fails if any
row carries a Han character without pinyin and English beside it. `CLAUDE.md`
records that rule being broken repeatedly despite being written down; a column of
bare glyphs in a file headed "characters" is that failure at scale. Columns are
ordered identity-first for the same reason: character, pinyin, gloss, and only
then the counts.
"""

import argparse
import csv
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.corpus import ROOT  # noqa: E402

DB_PATH = ROOT / "data" / "taoteching.sqlite"
OUT = ROOT / "data"

HAN_RE = re.compile(r"[㐀-鿿]")

# name -> (sql, [columns])
EXPORTS = {
    "characters": """
        SELECT char            AS character,
               pinyin,
               gloss,
               gloss_source,
               gloss_agreement,
               our_render,
               ifnull(lock_status,'')      AS lock_status,
               ifnull(forbidden,'')        AS never_render_as,
               total           AS occurrences,
               chapter_count,
               chapters,
               first_chapter,
               last_chapter,
               round(total * 1000.0 /
                     (SELECT sum(total) FROM character), 2) AS per_1000,
               ifnull(glossary_entry,'')   AS glossary_entry
        FROM character ORDER BY total DESC, character
    """,
    "character-anatomy": """
        SELECT s.char        AS character,
               ch.pinyin,
               ifnull(ch.gloss,'')      AS gloss,
               ifnull(ch.our_render,'') AS our_render,
               s.headword    AS shuowen_headword,
               s.matched_by,
               s.radical     AS shuowen_section,
               s.kind        AS construction,
               ifnull(s.fanqie,'') AS fanqie_middle_chinese,
               (SELECT group_concat(c.component || ' (' || ifnull(g.pinyin,'?')
                       || ' = ' || ifnull(g.gloss,'not yet glossed') || ')', ' + ')
                  FROM component c LEFT JOIN glyph g ON g.char = c.component
                 WHERE c.char = s.char AND c.role = 'semantic')
                                        AS semantic_parts,
               (SELECT group_concat(c.component || ' (' || ifnull(g.pinyin,'?')
                       || ' = ' || ifnull(g.gloss,'not yet glossed') || ')', ' + ')
                  FROM component c LEFT JOIN glyph g ON g.char = c.component
                 WHERE c.char = s.char AND c.role = 'phonetic')
                                        AS phonetic_parts,
               ch.total      AS occurrences,
               ifnull(ch.tier,'')       AS tier,
               ch.centrality,
               s.definition_zh AS shuowen_definition_chinese,
               ifnull(s.definition_en,'') AS shuowen_definition_english
        FROM shuowen s JOIN character ch ON ch.char = s.char
        ORDER BY ch.centrality DESC
    """,
    "components": """
        SELECT c.component,
               ifnull(g.pinyin,'')  AS pinyin,
               ifnull(g.gloss,'')   AS gloss,
               c.role,
               CASE
                 -- A character whose apparatus glosses did not converge carries
                 -- an empty gloss on purpose (gloss_source 'apparatus-split').
                 -- Reporting that as 'glossed' would hand a reader a blank cell
                 -- labelled as filled.
                 WHEN g.gloss IS NOT NULL AND trim(g.gloss) <> '' THEN 'glossed'
                 WHEN g.gloss IS NOT NULL AND trim(g.gloss) = ''
                   THEN 'the apparatus glosses this character several ways and none won a majority'
                 WHEN c.role = 'phonetic'
                   THEN 'no gloss needed: present for sound, not meaning'
                 ELSE 'not yet glossed — see sources/component-glosses.yaml'
               END AS gloss_status,
               count(DISTINCT c.char) AS builds_characters,
               group_concat(DISTINCT c.char) AS characters
        FROM component c LEFT JOIN glyph g ON g.char = c.component
        GROUP BY c.component, c.role
        ORDER BY builds_characters DESC, c.component
    """,
    "compounds": """
        SELECT term, pinyin, render, forbidden AS never_render_as,
               total AS occurrences, chapters, glossary_entry
        FROM compound ORDER BY total DESC
    """,
    "lines": """
        SELECT l.chapter, l.seq AS line, l.block,
               l.chinese, l.pinyin, l.literal AS literal_gloss,
               (SELECT group_concat(v.english, ' / ')
                  FROM alignment a JOIN verse_line v ON v.id = a.verse_line_id
                 WHERE a.line_id = l.id)      AS our_english,
               (SELECT max(a.method) FROM alignment a WHERE a.line_id = l.id)
                                              AS alignment_method
        FROM line l ORDER BY l.chapter, l.seq
    """,
    "translation": """
        SELECT chapter, seq AS line, stanza, english
        FROM verse_line ORDER BY chapter, seq
    """,
    "chapters": """
        SELECT c.n AS chapter,
               ifnull(c.hsg_title_zh,'')      AS heshanggong_title,
               ifnull(c.hsg_title_pinyin,'')  AS heshanggong_title_pinyin,
               ifnull(c.hsg_title_en,'')      AS heshanggong_title_english,
               c.status,
               c.han_chars, c.english_words,
               round(CAST(c.english_words AS REAL) / c.han_chars, 3)
                                          AS words_per_character,
               CASE c.guodian_attested WHEN 1 THEN 'yes' ELSE 'no' END
                                          AS guodian_attested,
               ifnull(c.guodian_extent,'')  AS guodian_extent,
               ifnull(c.guodian_bundles,'') AS guodian_bundles,
               (SELECT count(*) FROM line  WHERE chapter = c.n) AS source_lines,
               (SELECT count(*) FROM verse_line WHERE chapter = c.n) AS verse_lines,
               (SELECT count(DISTINCT variant_group) FROM variant WHERE chapter = c.n)
                                          AS variants
        FROM chapter c ORDER BY c.n
    """,
    "variants": """
        SELECT v.chapter, v.line AS base_line, v.base_reading,
               ifnull(v.witness_id,'—')      AS witness,
               ifnull(w.name_en,'editorial') AS witness_name,
               ifnull(w.kind,'')             AS witness_kind,
               ifnull(v.witness_reading,'')  AS witness_reading,
               CASE v.meaning_bearing WHEN 1 THEN 'yes' ELSE 'no' END
                                             AS meaning_bearing,
               v.our_call, v.followed, ifnull(v.note,'') AS note,
               ifnull(v.logged,'') AS logged
        FROM variant v LEFT JOIN witness w ON w.id = v.witness_id
        ORDER BY v.chapter, v.variant_group
    """,
    "witnesses": """
        SELECT id, name_zh, name_pinyin, name_en, kind, date_low, date_high,
               edition, rights,
               CASE is_full_text WHEN 1 THEN 'yes' ELSE 'no' END AS full_text,
               coverage_note
        FROM witness ORDER BY date_low
    """,
    "locked-renderings": """
        SELECT r.chapter, r.line_seq AS line, r.char AS character, r.pinyin,
               r.lock_term AS locked_term, r.expected AS expected_rendering,
               CASE r.honored WHEN 1 THEN 'yes' WHEN 0 THEN 'NOT FOUND' ELSE '' END
                                     AS rendering_present,
               r.confidence AS alignment_confidence, r.method AS alignment_method,
               r.english AS our_english_for_this_line
        FROM render r ORDER BY r.chapter, r.line_seq, r.char
    """,
    "commentary": """
        SELECT chapter, commentator, commentator_en, seq,
               lemma_zh, ifnull(lemma_en,'') AS lemma_our_english,
               CASE
                 WHEN lemma_matched = 1 THEN 'aligned to our base text'
                 WHEN line_seq IS NULL
                   THEN 'this commentator quotes a text that differs from ours'
                 ELSE 'located, but no English aligned to that line'
               END AS lemma_status,
               ifnull(comment_zh,'') AS comment_chinese,
               ifnull(comment_en,'') AS comment_english
        FROM commentary ORDER BY chapter, commentator, seq
    """,
}

# Which columns satisfy standing rule 0 for each export: the pinyin and English
# that must sit beside any Chinese on the same row. Named explicitly rather than
# sniffed from column names, so that adding a Chinese column to an export without
# also giving it a gloss is a build failure and not an oversight.
GLOSS_COLUMNS = {
    "characters":        {"pinyin", "gloss", "our_render"},
    "character-anatomy": {"pinyin", "gloss", "our_render"},
    "components":        {"pinyin", "gloss", "gloss_status"},
    "compounds":         {"pinyin", "render"},
    "lines":             {"pinyin", "literal_gloss", "our_english"},
    "chapters":          {"heshanggong_title_pinyin", "heshanggong_title_english"},
    "variants":          {"note", "witness_name"},
    "witnesses":         {"name_pinyin", "name_en"},
    "locked-renderings": {"pinyin", "expected_rendering"},
    "commentary":        {"lemma_our_english", "lemma_status"},
}


# Columns holding Chinese this repository has deliberately not translated. They
# are exempt from the rule-0 gate and **counted in the report instead**, because
# the alternative to a marked gap is an invented one. Wang Bi and Heshang Gong
# are quoted, glossed and cited where a decision turns on them — that is
# PROVENANCE's rule and process/method.md §3's — and machine-rendering 1,133
# commentary blocks would manufacture scholarship nobody did.
UNTRANSLATED = {
    "commentary": {"comment_chinese"},
    # 說文's own definitions, ~700 of them in classical Chinese. Machine-rendering
    # them would put invented etymology under real characters. They are glossed by
    # hand as characters earn glossary entries; the components beside them carry
    # the reading in the meantime.
    "character-anatomy": {"shuowen_definition_chinese"},
}


def rows(conn, sql):
    cur = conn.execute(sql)
    return [d[0] for d in cur.description], cur.fetchall()


def rule_zero_violations(name, cols, data):
    """Rows carrying a Han character with nothing on the row that reads it.

    CLAUDE.md standing rule 0, as a check rather than a hope. A row is in breach
    when it contains a Chinese character and every one of its designated gloss
    columns is empty.
    """
    gloss_cols = GLOSS_COLUMNS.get(name, set())
    exempt = UNTRANSLATED.get(name, set())
    idx = {c: i for i, c in enumerate(cols)}
    bad, untranslated = [], 0
    for row in data:
        han_cols = [c for c in cols
                    if c not in exempt
                    and isinstance(row[idx[c]], str) and HAN_RE.search(row[idx[c]])]
        if any(c in exempt and isinstance(row[idx[c]], str)
               and HAN_RE.search(row[idx[c]]) for c in cols):
            untranslated += 1
        if not han_cols:
            continue
        if not any(str(row[idx[c]] or "").strip()
                   for c in gloss_cols if c in idx):
            bad.append((han_cols, row))
    return bad, untranslated


def write(conn, check=False):
    OUT.mkdir(parents=True, exist_ok=True)
    stale, violations, untranslated = [], [], 0
    for name, sql in EXPORTS.items():
        cols, data = rows(conn, sql)
        bad, n_untranslated = rule_zero_violations(name, cols, data)
        violations += [(name, v) for v in bad]
        untranslated += n_untranslated

        buf = []
        buf.append(cols)
        buf.extend(list(r) for r in data)
        path = OUT / f"{name}.csv"

        import io
        sio = io.StringIO()
        w = csv.writer(sio, lineterminator="\n")
        w.writerows(buf)
        text = sio.getvalue()

        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8")
            print(f"    {path.name:24} {len(data):5} rows")
    return stale, violations, untranslated


README = """# `data/` — the corpus as data

**Generated. Do not edit by hand.** Rebuild with:

```bash
python3 tools/build_db.py      # writes data/taoteching.sqlite (gitignored)
python3 tools/export.py        # writes the .csv files in this directory
```

The manuscript is `chapters/001–081.md`. Everything here is derived from it, the
way `glossary/INDEX.md` and `glossary/terms.yaml` are derived from the glossary
entries. Anything here that disagrees with a chapter file is a bug in the tools.

## Reading these files without reading Chinese

Every row that carries a Chinese character carries its pinyin and an English
rendering beside it. That is `CLAUDE.md` standing rule 0, and `tools/export.py
--check` fails the build if any row breaks it.

**The `gloss_source` column tells you how much to trust a gloss.**

| value | where it came from | trust |
|---|---|---|
| `locked` | a settled rendering in `glossary/terms.yaml` | high — this is the edition's own decision |
| `covers` | a secondary character absorbed by a glossary entry | high |
| `apparatus` | the `[pinyin]` notes in the Literal column of the source tables | **working approximation** |
| `none` | nothing in this repo glosses this character yet | — |

`apparatus` glosses are harvested from the source tables' literal column, which
`CLAUDE.md` warns speaks pre-lock English. They are a starting point, never a
ruling, and they never override a lock. The `gloss_agreement` column shows how
many of a character's glossed occurrences agreed on the winning English: `17/31`
means the character was glossed 31 times and the chosen English won 17 of them.
**A low ratio means the character is contextual, not that the gloss is wrong** —
之 (*zhī*) is a particle and will never have one English.

`none` is not hidden. Roughly 389 of the 798 distinct characters have no per-
character English in this repository yet. That gap is the glossary's worklist.

## The files

| file | one row per | good for |
|---|---|---|
| `characters.csv` | distinct character | frequency, coverage, what is glossed |
| `compounds.csv` | multi-character locked term | 萬物, 無為, 天地, 自然, 知足 |
| `lines.csv` | source line | Chinese, pinyin, literal gloss and our English side by side |
| `translation.csv` | verse line | the whole book in English, stanzas intact |
| `chapters.csv` | chapter | ratios, Guodian attestation, Heshang Gong's titles |
| `variants.csv` | witness reading at a fork | where the manuscripts disagree |
| `witnesses.csv` | witness | who they are, when, and on what rights basis |
| `locked-renderings.csv` | locked character occurrence | whether the lock is honored at that line |
| `commentary.csv` | commentary lemma | 王弼, 河上公, 韓非, with our English for the lemma |

## Two cautions that matter

**`alignment_method` is not decoration.** Our English verse lines and the Chinese
source lines are 1:1 in only 30 of 81 chapters (835 verse lines against 798
source lines). Where the counts match, `alignment_method` is `exact-count` and
the pairing is certain. Where they do not, it is `proportional` — a positional
guess at confidence 0.3, recorded so it can be improved, and **not evidence of
anything**. `rendering_present = NOT FOUND` on a `proportional` row usually means
the alignment is wrong, not the translation.

**`expected_rendering` is the lock's primary English, and `rendering_present`
also consults its flexions.** A flexion is a secondary English scoped to named
chapters — 保 (*bǎo*) reads *keep safe* generally and bare *keep* at chapter 9,
執 (*zhí*) reads *grasp* and *seize* at chapter 74 — declared as data in the
entry's frontmatter. The column counts a line honored if it carries the primary
render **or** a flexion licensed in that chapter. Before 2026-09-20 the flexions
were prose inside `render:` and this column printed `NOT FOUND` on 36 lines that
were correct, all of them on flexed locks. `expected_rendering` still shows only
the primary render, so a flexed line reads as `keep safe · yes`; the licence is
in `glossary/terms.yaml`.

**The excavated manuscripts are facts here, never text.** 郭店 (*Guōdiàn*),
馬王堆 (*Mǎwángduī*) and 北大 (*Běidà*) appear only in `variants.csv`, as recorded
disagreements with citations. `sources/PROVENANCE.md` explains why: reconstructing
damaged graphs is living scholarship, and this repository is CC0 with no
exceptions. `witnesses.csv` marks them `FACTS ONLY` in the rights column.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if committed CSVs are stale; write nothing")
    ap.add_argument("--db", default=str(DB_PATH))
    args = ap.parse_args()

    db = Path(args.db)
    if not db.exists():
        print(f"  no database at {db} — run: python3 tools/build_db.py")
        return 2

    conn = sqlite3.connect(db)
    stale, violations, untranslated = write(conn, check=args.check)
    conn.close()

    if not args.check:
        (OUT / "README.md").write_text(README, encoding="utf-8")
        print(f"    {'README.md':24}")

    rc = 0
    if violations:
        print(f"\n  ✗ standing rule 0: {len(violations)} row(s) carry Chinese "
              f"with no pinyin and no English")
        for name, (cols, row) in violations[:5]:
            print(f"      {name}.csv · columns {cols} · {str(row)[:90]}")
        rc = 1
    else:
        print("\n  ✓ standing rule 0: every row with Chinese carries pinyin "
              "or English")
    if untranslated:
        print(f"  · {untranslated} row(s) carry deliberately untranslated Chinese "
              f"(commentary text) — marked, not machine-rendered")

    if args.check and stale:
        print(f"  ✗ stale: {', '.join(stale)} — run python3 tools/export.py")
        rc = 1
    elif args.check:
        print("  ✓ committed CSVs are current")
    return rc


if __name__ == "__main__":
    sys.exit(main())
