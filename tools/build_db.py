#!/usr/bin/env python3
"""build_db.py — assemble the manuscript into a queryable corpus.

    python3 tools/build_db.py            # build data/taoteching.sqlite
    python3 tools/build_db.py --report   # build, then print the coverage report
    python3 tools/build_db.py --verify   # build, then assert the regression baseline

**This is a generated artifact and is never authoritative.** `chapters/*.md` is
the manuscript, exactly as it is for `glossary/INDEX.md` and `glossary/terms.yaml`.
Anything that disagrees with a chapter file is this tool's bug.

Two design commitments are load-bearing.

**The addressable unit is a coordinate, not a text.** Every character in the book
has an address `(chapter, line_seq, char_pos)`. Witnesses attach to those
addresses — as full text where their edition is admissible, and as typed variant
facts where it is not. `sources/PROVENANCE.md` excludes transcriptions of the
excavated manuscripts outright and says a `shaloms-call` cannot reach it, so this
is not a preference the schema can be talked out of later.

**No row carries a Chinese character without pinyin and English beside it.**
`CLAUDE.md` standing rule 0, made mechanical. A `characters.csv` that opens as a
column of glyphs is that rule broken 798 times in one file, and the rule records
its own repeated failure as prose. Here it is a check that fails the build.

Stdlib only — a fresh clone runs it with nothing installed.
"""

import argparse
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.corpus import (  # noqa: E402
    CHAPTERS, GLOSSARY, ROOT, load_chapters, load_guodian, load_terms,
    load_variants, parse_frontmatter,
)

DB_PATH = ROOT / "data" / "taoteching.sqlite"
COMMENTARIES = ROOT / "sources" / "commentaries"

# The CJK range check_locks.py and concordance.py already use. Kept identical on
# purpose: three tools disagreeing about what counts as a character would be a
# silent, unfindable class of bug.
HAN = r"[㐀-鿿]"
HAN_RE = re.compile(HAN)

# The base text lives inside the BMP, so HAN_RE is right for tokenising it and
# matches what check_locks.py and concordance.py already use. **說文's component
# graphs do not.** 道 is 从辵从𩠐 — a road one walks, plus a head — and 𩠐 is
# U+29840, outside the BMP. Parsing components with the narrow range deletes it
# silently and leaves 道 looking like it has one part. Use this for anything
# coming out of sources/shuowen/.
WIDE_HAN_RE = re.compile(r"[㐀-鿿豈-﫿\U00020000-\U0002ebef]")

# Punctuation in the source is editorial, not authorial — source/chinese.md says
# so in its own header. Splitting on it is an editorial act, and the repo already
# makes it: this is the unit --formulas and the repeated-formula rule index on.
SEGMENT_SPLIT = re.compile(r"[，。；、！？：]")

_TONE = str.maketrans(
    "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü",
    "aaaaeeeeiiiioooouuuuuuuuu",
)

# Grammatical particles, negatives and pronouns. An editorial call, kept
# deliberately narrow: only graphs that do no lexical work of their own in this
# text. It exists because centrality without it just ranks the particles — 之
# (zhī — the possessive particle) reaches almost every chapter and keeps company
# with almost every character, which says nothing about the book's thought.
# Anything arguable is left OUT of this list and therefore stays visible: 為
# (wéi — do / handle) and 無 (wú — absence) are locked terms, not grammar.
FUNCTION_WORDS = set(
    "之而其以於也者矣乎焉則所夫且與故亦乃兮哉耳斯于曰"
    "不非未弗勿毋何孰安豈"
    "吾我汝爾彼此是"
)

COMMENTATORS = [
    ("wangbi", "王弼", "Wáng Bì", "Wang Bi (d. 249 CE)"),
    ("heshanggong", "河上公", "Héshàng Gōng", "Heshang Gong (Han)"),
    ("hanfeizi", "韓非", "Hán Fēi", "Han Fei (d. 233 BCE)"),
]


# ----------------------------------------------------------------- the schema

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE chapter (
    n                INTEGER PRIMARY KEY,
    hsg_title_zh     TEXT,
    hsg_title_pinyin TEXT,
    hsg_title_en     TEXT,
    guodian_attested INTEGER NOT NULL DEFAULT 0,
    guodian_extent   TEXT,
    guodian_bundles  TEXT,
    status           TEXT,
    han_chars        INTEGER,
    english_words    INTEGER
);

CREATE TABLE line (
    id           INTEGER PRIMARY KEY,
    chapter      INTEGER NOT NULL REFERENCES chapter(n),
    seq          INTEGER NOT NULL,
    chinese      TEXT NOT NULL,
    pinyin       TEXT,
    literal      TEXT,
    block        INTEGER,
    src_line_no  INTEGER,
    UNIQUE (chapter, seq)
);

CREATE TABLE segment (
    id       INTEGER PRIMARY KEY,
    line_id  INTEGER NOT NULL REFERENCES line(id),
    chapter  INTEGER NOT NULL,
    line_seq INTEGER NOT NULL,
    seq      INTEGER NOT NULL,
    chinese  TEXT NOT NULL,
    pinyin   TEXT
);

CREATE TABLE token (
    id         INTEGER PRIMARY KEY,
    chapter    INTEGER NOT NULL,
    line_seq   INTEGER NOT NULL,
    char_pos   INTEGER NOT NULL,
    char       TEXT NOT NULL,
    pinyin     TEXT,
    segment_id INTEGER REFERENCES segment(id),
    global_pos INTEGER NOT NULL,
    UNIQUE (chapter, line_seq, char_pos)
);

CREATE TABLE character (
    char           TEXT PRIMARY KEY,
    pinyin         TEXT,
    gloss          TEXT,
    gloss_source   TEXT NOT NULL DEFAULT 'none',
    -- for the apparatus tier: how many of this character's glossed occurrences
    -- agreed on the winning English, out of how many. Low agreement is a signal
    -- the gloss is contextual, not a definition.
    gloss_agreement TEXT,
    our_render     TEXT,
    lock_status    TEXT,
    glossary_entry TEXT,
    forbidden      TEXT,
    is_function_word INTEGER NOT NULL DEFAULT 0,
    radical        TEXT,      -- from 說文, for grouping; see the shuowen table
    -- Editorial, from glossary/TRIAGE.md. `centrality` sits beside it as a
    -- computed proposal and never as a replacement: TRIAGE's own warning is that
    -- "frequency is not importance — 全 has three occurrences and sat below every
    -- triage threshold for the life of this project." A disagreement between the
    -- two columns is the interesting case, so both are kept visible.
    tier           TEXT,
    centrality     REAL,
    total          INTEGER NOT NULL DEFAULT 0,
    chapter_count  INTEGER NOT NULL DEFAULT 0,
    chapters       TEXT,
    first_chapter  INTEGER,
    last_chapter   INTEGER
);

-- Multi-character locked terms (萬物, 無為, 天地, 自然, 知足) are units the
-- character table cannot express. They get their own table rather than being
-- silently decomposed into characters that mean something else apart.
CREATE TABLE compound (
    term           TEXT PRIMARY KEY,
    pinyin         TEXT,
    render         TEXT,
    forbidden      TEXT,
    glossary_entry TEXT,
    total          INTEGER NOT NULL DEFAULT 0,
    chapters       TEXT
);

-- 說文解字 (c. 100 CE) on the characters of this book. The definition stays in
-- Chinese: ~700 classical definitions machine-rendered would be invented
-- scholarship. The *components* are what carry across, and they are glossed.
CREATE TABLE shuowen (
    char          TEXT PRIMARY KEY,
    headword      TEXT,      -- the graph 說文 files it under: 明 is entered as 朙
    matched_by    TEXT,      -- exact | old-form | orthographic
    radical       TEXT,      -- the 說文 部 (section), NOT the Kangxi radical
    kind          TEXT,      -- pictograph | compound | phonetic-compound | …
    fanqie        TEXT,      -- 反切 — Middle Chinese, free by age
    definition_zh TEXT,
    definition_en TEXT,      -- null by design; filled by hand as entries earn it
    section_head  INTEGER NOT NULL DEFAULT 0
);

-- One row per (character, part). `role` is the distinction a radical table
-- cannot make: semantic parts carry meaning, phonetic parts are there for sound.
CREATE TABLE component (
    id        INTEGER PRIMARY KEY,
    char      TEXT NOT NULL,
    component TEXT NOT NULL,
    role      TEXT NOT NULL,   -- semantic | phonetic
    seq       INTEGER NOT NULL
);

-- Every graph the corpus can show a reader, whether or not it occurs in the
-- Laozi: the book's own characters plus the components they are built from.
-- Standing rule 0 needs this — a component with no English makes the whole
-- decomposition layer unreadable, which is the layer it exists for.
CREATE TABLE glyph (
    char   TEXT PRIMARY KEY,
    pinyin TEXT,
    gloss  TEXT,
    source TEXT NOT NULL      -- corpus | component-gloss
);

CREATE TABLE witness (
    id           TEXT PRIMARY KEY,
    name_zh      TEXT,
    name_pinyin  TEXT,
    name_en      TEXT NOT NULL,
    kind         TEXT NOT NULL,
    date_low     INTEGER,
    date_high    INTEGER,
    edition      TEXT,
    rights       TEXT,
    is_full_text INTEGER NOT NULL DEFAULT 0,
    coverage_note TEXT
);

CREATE TABLE variant (
    id              INTEGER PRIMARY KEY,
    variant_group   INTEGER NOT NULL,   -- one per entry in sources/variants.yaml
    chapter         INTEGER NOT NULL,
    line            TEXT,
    base_reading    TEXT,
    witness_id      TEXT,
    witness_reading TEXT,
    meaning_bearing INTEGER NOT NULL DEFAULT 0,
    our_call        TEXT,
    followed        TEXT,
    note            TEXT,
    logged          TEXT
);

CREATE TABLE verse_line (
    id       INTEGER PRIMARY KEY,
    chapter  INTEGER NOT NULL REFERENCES chapter(n),
    seq      INTEGER NOT NULL,
    stanza   INTEGER NOT NULL,
    english  TEXT NOT NULL,
    UNIQUE (chapter, seq)
);

CREATE TABLE alignment (
    verse_line_id INTEGER NOT NULL REFERENCES verse_line(id),
    line_id       INTEGER NOT NULL REFERENCES line(id),
    confidence    REAL NOT NULL,
    method        TEXT NOT NULL
);

-- The reverse concordance lives on this table: a locked character, the coordinate
-- it sits at, and the English our verse uses there.
CREATE TABLE render (
    id         INTEGER PRIMARY KEY,
    chapter    INTEGER NOT NULL,
    line_seq   INTEGER NOT NULL,
    char       TEXT NOT NULL,
    pinyin     TEXT,
    english    TEXT,
    lock_term  TEXT,
    expected   TEXT,
    honored    INTEGER,
    confidence REAL NOT NULL,
    method     TEXT NOT NULL
);

CREATE TABLE commentary (
    id            INTEGER PRIMARY KEY,
    commentator   TEXT NOT NULL,
    commentator_en TEXT NOT NULL,
    chapter       INTEGER NOT NULL,
    seq           INTEGER NOT NULL,
    lemma_zh      TEXT,
    lemma_en      TEXT,
    comment_zh    TEXT,
    comment_en    TEXT,
    lemma_matched INTEGER NOT NULL DEFAULT 0,
    line_seq      INTEGER
);

CREATE INDEX idx_token_char    ON token(char);
CREATE INDEX idx_token_chapter ON token(chapter, line_seq);
CREATE INDEX idx_render_char   ON render(char);
CREATE INDEX idx_variant_ch    ON variant(chapter);
CREATE INDEX idx_comm_ch       ON commentary(chapter, commentator);
"""


# ------------------------------------------------------------------- helpers

def han_chars(text):
    return HAN_RE.findall(text or "")


def strip_tone(s):
    return s.translate(_TONE).lower()


def syllables(pinyin):
    """Pinyin syllables, in order. Apostrophes are internal (Xi'an), so kept."""
    return re.findall(r"[A-Za-zÀ-ÿāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü']+", pinyin or "")


def align_pinyin(chinese, pinyin):
    """Map each Han character to its pinyin syllable, positionally.

    Chinese is one syllable per character, so a source row's Pinyin column is
    already a per-character transcription — nobody had used it that way. Across
    all 798 rows this aligns exactly, which is why it can be trusted; the one
    row that did not align turned out to be a defect in the manuscript (ch 74
    carried a raw 敢 where its transcription belonged) and was fixed, not
    papered over.

    Returns (pairs, ok). On a count mismatch the pairs come back with None
    syllables rather than a guess — a wrong pinyin is worse than a missing one,
    because it reads as authoritative.
    """
    chars = han_chars(chinese)
    syls = syllables(pinyin)
    if len(chars) == len(syls):
        return list(zip(chars, syls)), True
    return [(c, None) for c in chars], False


def parse_translation(path):
    """Verse lines with stanza numbers.

    Chapter.verse drops blank lines, which is where the stanza breaks live, so
    the section is re-read here. The two trailing spaces on each line are
    CommonMark hard breaks and are load-bearing — see fix-linebreaks.py.
    """
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Translation\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return []
    out, stanza, seq, blank = [], 1, 0, False
    for raw in m.group(1).split("\n"):
        line = raw.strip()
        if not line:
            blank = True
            continue
        if blank and out:
            stanza += 1
        blank = False
        seq += 1
        out.append((seq, stanza, line))
    return out


# Words the sentence owns, not the character. The bracket regex captures
# everything between one \[pin\] and the next, so a conjunction or article
# carried over from the English sentence lands inside the gloss: 義 (yì — duty)
# came out as "and righteousness" where the same character reads "righteousness"
# one chapter later, and the two then failed to agree. Stripped only from the
# front, and never down to nothing — 而 (ér) really is glossed "and".
_CARRIER = ("and ", "or ", "the ", "a ", "an ", "to ", "of ", "is ", "are ", "be ",
            "then ", "there ", "its ", "their ", "his ", "her ")


def _trim_carrier(english):
    low = english.lower()
    for w in _CARRIER:
        if low.startswith(w) and english[len(w):].strip():
            return english[len(w):].strip()
    return english


def apparatus_glosses(pairs, literal):
    """Per-character English from the `\\[pinyin\\]` apparatus in some Literal cells.

    Aligned **positionally inside one line**, never by a global pinyin lookup.
    That distinction is the whole correctness argument: pinyin is not a key.
    Matching glosses to characters by sound across the book collides homophones
    and near-homophones wholesale — an early build of this function rendered
    其 (qí — its) as "tools" by way of 器 (qì — vessel), and 下 (xià — below) as
    "flaws" by way of 瑕 (xiá — flaw). Both were confidently wrong and would have
    shipped in a column headed "gloss".

    Within a single line the character sequence is known, so the brackets can be
    walked in reading order against it: `Tiptoeing \\[qi\\] those \\[zhe\\]` over
    企者 assigns qi→企 and zhe→者 by position. A bracket that does not match the
    next available character is skipped rather than guessed.

    Only single-syllable brackets are used. A multi-syllable bracket glosses a
    phrase, and splitting a phrase across its characters invents readings nobody
    wrote.

    Returns {char_index: english}.
    """
    if not literal or not pairs:
        return {}
    brackets = []
    for m in re.finditer(r"([A-Za-z][A-Za-z' /-]*?)\s*\\\[([^\]\\]+)\\\]", literal):
        english, pin = m.group(1).strip(), m.group(2).strip()
        english = _trim_carrier(english)
        if len(pin.split()) == 1 and english:
            brackets.append((english, strip_tone(pin)))

    out, i = {}, 0
    for english, pin in brackets:
        for j in range(i, len(pairs)):
            syl = pairs[j][1]
            if syl and strip_tone(syl) == pin:
                out[j] = english
                i = j + 1
                break
    return out


def load_title_glosses():
    """(chapter, pinyin, english) for Heshang Gong's chapter titles.

    Hand-rolled like every other YAML reader here — see lib/corpus.py. The files
    are kept to flat scalars precisely so that stdlib-only parsing stays honest.
    """
    path = ROOT / "sources" / "heshanggong-titles.yaml"
    if not path.exists():
        return []
    out, cur = [], {}
    for line in path.read_text(encoding="utf-8").split("\n"):
        s = line.strip()
        if s.startswith("#") or not s:
            continue
        if s.startswith("- chapter:"):
            if cur.get("chapter"):
                out.append((cur["chapter"], cur.get("pinyin"), cur.get("english")))
            cur = {"chapter": int(s.split(":", 1)[1])}
        elif ":" in s:
            k, v = s.split(":", 1)
            cur[k.strip()] = v.strip().strip('"')
    if cur.get("chapter"):
        out.append((cur["chapter"], cur.get("pinyin"), cur.get("english")))
    return out


def load_shuowen():
    """Rows from sources/shuowen/entries.md — see tools/import_shuowen.py."""
    path = ROOT / "sources" / "shuowen" / "entries.md"
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        if not line.startswith("| ") or line.startswith("| :---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 9 or cells[0] == "char":
            continue
        out.append(dict(zip(
            ("char", "headword", "matched_by", "radical", "kind",
             "semantic", "phonetic", "fanqie", "definition"), cells)))
    return out


def load_component_glosses():
    """(char, pinyin, gloss) from sources/component-glosses.yaml."""
    path = ROOT / "sources" / "component-glosses.yaml"
    if not path.exists():
        return []
    out, cur = [], {}
    for line in path.read_text(encoding="utf-8").split("\n"):
        s = line.strip()
        if s.startswith("#") or not s:
            continue
        if s.startswith("- char:"):
            if cur.get("char"):
                out.append((cur["char"], cur.get("pinyin"), cur.get("gloss")))
            cur = {"char": s.split(":", 1)[1].strip().strip('"')}
        elif ":" in s:
            k, v = s.split(":", 1)
            cur[k.strip()] = v.strip().strip('"')
    if cur.get("char"):
        out.append((cur["char"], cur.get("pinyin"), cur.get("gloss")))
    return out


def load_tiers():
    """{char: 'Tier N'} from glossary/TRIAGE.md.

    The triage list is the editorial judgement of what matters, kept by hand and
    argued in prose. It is read, never written: nothing here decides a tier.
    """
    path = GLOSSARY / "TRIAGE.md"
    if not path.exists():
        return {}
    tiers, current = {}, None
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^##\s*Tier\s*(\d)", line)
        if m:
            current = f"Tier {m.group(1)}"
            continue
        if current and line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 2 or cells[0] in ("#", "---"):
                continue
            for c in HAN_RE.findall(cells[1]):
                tiers.setdefault(c, current)
    return tiers


def split_render(term_chars, render):
    """Positional split of a pairing's render: 無 & 有 → absence / presence."""
    parts = [p.strip() for p in render.split(" / ")]
    if len(term_chars) > 1 and len(parts) == len(term_chars):
        return dict(zip(term_chars, parts))
    return {c: render for c in term_chars}


# ------------------------------------------------------------------- the build

def build(conn, report=False):
    cur = conn.cursor()
    cur.executescript(SCHEMA)

    chapters = load_chapters()
    guodian = load_guodian()
    terms = load_terms()
    stats = {"pinyin_ok": 0, "pinyin_fail": 0, "unaligned": []}

    # ---- chapters, lines, segments, tokens ---------------------------------
    global_pos = 0
    line_id = seg_id = 0
    han_by_chapter = {}
    for n in sorted(chapters):
        ch = chapters[n]
        g = guodian.get(n)
        cur.execute(
            "INSERT INTO chapter (n, guodian_attested, guodian_extent, guodian_bundles,"
            " status) VALUES (?,?,?,?,?)",
            (n, 1 if g else 0, g.extent if g else None,
             ", ".join(g.bundles) if g else None, ch.status),
        )
        chapter_han = []
        for seq, row in enumerate(ch.source_rows, 1):
            line_id += 1
            cur.execute(
                "INSERT INTO line (id, chapter, seq, chinese, pinyin, literal, block,"
                " src_line_no) VALUES (?,?,?,?,?,?,?,?)",
                (line_id, n, seq, row.chinese, row.pinyin, row.literal,
                 row.block, row.line_no),
            )
            pairs, ok = align_pinyin(row.chinese, row.pinyin)
            stats["pinyin_ok" if ok else "pinyin_fail"] += 1
            if not ok:
                stats["unaligned"].append((n, seq, row.chinese))

            # segments, and which token belongs to which
            seg_of_char, s_seq = {}, 0
            idx = 0
            for chunk in SEGMENT_SPLIT.split(row.chinese):
                chunk_chars = han_chars(chunk)
                if not chunk_chars:
                    continue
                s_seq += 1
                seg_id += 1
                syl = [p[1] for p in pairs[idx:idx + len(chunk_chars)]]
                cur.execute(
                    "INSERT INTO segment (id, line_id, chapter, line_seq, seq, chinese,"
                    " pinyin) VALUES (?,?,?,?,?,?,?)",
                    (seg_id, line_id, n, seq, s_seq, "".join(chunk_chars),
                     " ".join(s for s in syl if s) or None),
                )
                for k in range(len(chunk_chars)):
                    seg_of_char[idx + k] = seg_id
                idx += len(chunk_chars)

            for pos, (c, syl) in enumerate(pairs, 1):
                global_pos += 1
                cur.execute(
                    "INSERT INTO token (chapter, line_seq, char_pos, char, pinyin,"
                    " segment_id, global_pos) VALUES (?,?,?,?,?,?,?)",
                    (n, seq, pos, c, syl, seg_of_char.get(pos - 1), global_pos),
                )
                chapter_han.append(c)
        han_by_chapter[n] = chapter_han

    # ---- Heshang Gong's own chapter titles ---------------------------------
    # His Chinese comes from the vendored commentary frontmatter; the pinyin and
    # English come from sources/heshanggong-titles.yaml, which is our own work and
    # is marked there as working renderings pending review. They arrive glossed
    # or not at all — a bare title would breach standing rule 0, and export.py
    # would refuse to emit it.
    hsg = COMMENTARIES / "heshanggong"
    if hsg.is_dir():
        for path in sorted(hsg.glob("*.md")):
            fm = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
            title, n = fm.get("chapter_title"), fm.get("chapter")
            if title and n:
                cur.execute("UPDATE chapter SET hsg_title_zh=? WHERE n=?",
                            (title, int(n)))
    for n, pin, en in load_title_glosses():
        cur.execute("UPDATE chapter SET hsg_title_pinyin=?, hsg_title_en=? WHERE n=?",
                    (pin, en, n))

    # ---- the translation, stanza-aware -------------------------------------
    verse_id = 0
    verse_by_chapter = {}
    for n in sorted(chapters):
        rows = parse_translation(CHAPTERS / f"{n:03d}.md")
        verse_by_chapter[n] = []
        for seq, stanza, english in rows:
            verse_id += 1
            cur.execute(
                "INSERT INTO verse_line (id, chapter, seq, stanza, english)"
                " VALUES (?,?,?,?,?)",
                (verse_id, n, seq, stanza, english),
            )
            verse_by_chapter[n].append((verse_id, english))

    # ---- line alignment ----------------------------------------------------
    # Where the counts agree the mapping is 1:1 and certain. Where they do not,
    # a proportional guess is recorded at low confidence and flagged, never
    # presented as settled: check_locks' repeated-formula rule already learned
    # this lesson the hard way (three attempts at inference, all failed).
    align_stats = {"exact": 0, "proportional": 0}
    for n in sorted(chapters):
        srcs = list(chapters[n].source_rows)
        verses = verse_by_chapter.get(n, [])
        if not srcs or not verses:
            continue
        base = cur.execute("SELECT id, seq FROM line WHERE chapter=? ORDER BY seq",
                           (n,)).fetchall()
        if len(verses) == len(srcs):
            align_stats["exact"] += 1
            for (vid, _), (lid, _) in zip(verses, base):
                cur.execute("INSERT INTO alignment VALUES (?,?,?,?)",
                            (vid, lid, 1.0, "exact-count"))
        else:
            align_stats["proportional"] += 1
            covered = set()
            for i, (vid, _) in enumerate(verses):
                j = min(int(i * len(base) / len(verses)), len(base) - 1)
                cur.execute("INSERT INTO alignment VALUES (?,?,?,?)",
                            (vid, base[j][0], 0.3, "proportional"))
                covered.add(j)
            # Map in the other direction too. Mapping only verses onto lines
            # leaves the surplus lines with nothing attached whenever a chapter
            # has fewer verse lines than source lines — which silently cost 60
            # commentary lemmas their English, since a lemma inherits the English
            # of the lines it covers. The pass is total in both directions now.
            for j in range(len(base)):
                if j in covered:
                    continue
                i = min(int(j * len(verses) / len(base)), len(verses) - 1)
                cur.execute("INSERT INTO alignment VALUES (?,?,?,?)",
                            (verses[i][0], base[j][0], 0.2, "proportional-fill"))

    # ---- characters --------------------------------------------------------
    counts, chapters_of = {}, {}
    for n, chars in han_by_chapter.items():
        for c in chars:
            counts[c] = counts.get(c, 0) + 1
            chapters_of.setdefault(c, set()).add(n)

    gloss = {}          # char -> (english, tier)
    render_of = {}      # char -> our_render
    lock_of = {}        # char -> (term, entry, forbidden)
    flex_of = {}        # char -> [(english, {chapters})] — chapter-scoped flexions
    for t in terms:
        if len(t.characters) == 1 and len(t.characters[0]) > 1:
            cur.execute(
                "INSERT OR REPLACE INTO compound (term, pinyin, render, forbidden,"
                " glossary_entry) VALUES (?,?,?,?,?)",
                (t.characters[0], t.pinyin, t.render, "; ".join(t.forbidden), t.entry),
            )
            continue
        for c, part in split_render(t.characters, t.render).items():
            gloss.setdefault(c, (part, "locked"))
            render_of.setdefault(c, part)
            lock_of.setdefault(c, (t.term, t.entry, "; ".join(t.forbidden)))
            if t.flexions:
                flex_of.setdefault(c, [(f["english"], set(f["chapters"]))
                                       for f in t.flexions])

    # `covers:` — a secondary character an entry absorbs (力 inside 強, 腹 inside
    # 心). The repo already treats these as glossed; so does this.
    for path in sorted(GLOSSARY.glob("*.md")):
        if path.name in ("INDEX.md", "TRIAGE.md"):
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
        for c, render in fm.get("covers") or []:
            if len(c) == 1:
                gloss.setdefault(c, (render, "covers"))
                render_of.setdefault(c, render)
                lock_of.setdefault(c, (fm.get("term", ""),
                                       f"glossary/{path.name}", ""))

    # The apparatus tier, harvested per line and aggregated per character. The
    # winning English is the most common one across that character's glossed
    # occurrences; the agreement ratio is kept, because a character glossed six
    # different ways in six places has a context, not a definition.
    appar = {}
    for ch in chapters.values():
        for row in ch.source_rows:
            pairs, _ = align_pinyin(row.chinese, row.pinyin)
            for idx, english in apparatus_glosses(pairs, row.literal).items():
                appar.setdefault(pairs[idx][0], Counter())[english] += 1

    agreement = {}
    for c, counter in appar.items():
        if c in gloss:
            continue
        english, n = counter.most_common(1)[0]
        total = sum(counter.values())
        agreement[c] = f"{n}/{total}"
        # A plurality is not a definition. Counter.most_common breaks a tie by
        # insertion order, so on 1-1 it publishes whichever chapter came first —
        # which is how 義 (yì — duty) shipped glossed "and", from a single
        # misplaced bracket in ch 18 beating a correct one in ch 19. The comment
        # above already states the principle ("a character glossed six different
        # ways in six places has a context, not a definition"); this enforces it.
        # The ratio is recorded either way, so the evidence survives the refusal.
        if n * 2 > total:
            gloss[c] = (english, "apparatus")
        else:
            gloss[c] = ("", "apparatus-split")

    pin_of = dict(cur.execute(
        "SELECT char, pinyin FROM token WHERE pinyin IS NOT NULL GROUP BY char"
    ).fetchall())

    for c in sorted(counts):
        chs = sorted(chapters_of[c])
        g, tier = gloss.get(c, (None, "none"))
        term, entry, forbidden = lock_of.get(c, (None, None, None))
        cur.execute(
            "INSERT INTO character (char, pinyin, gloss, gloss_source, gloss_agreement,"
            " our_render, lock_status, glossary_entry, forbidden, total, chapter_count,"
            " chapters, first_chapter, last_chapter)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (c, pin_of.get(c), g, tier, agreement.get(c), render_of.get(c),
             "locked" if term else None, entry, forbidden or None,
             counts[c], len(chs), ",".join(str(x) for x in chs), chs[0], chs[-1]),
        )
        if c in FUNCTION_WORDS:
            cur.execute("UPDATE character SET is_function_word=1 WHERE char=?", (c,))

    # ---- 說文, components, and the glyph table -----------------------------
    sw = load_shuowen()
    for e in sw:
        cur.execute(
            "INSERT OR REPLACE INTO shuowen (char, headword, matched_by, radical,"
            " kind, fanqie, definition_zh, section_head)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (e["char"], e["headword"], e["matched_by"], e["radical"] or None,
             e["kind"], e["fanqie"] or None, e["definition"],
             1 if "凡" in e["definition"] and "之屬皆从" in e["definition"] else 0),
        )
        for role, field in (("semantic", "semantic"), ("phonetic", "phonetic")):
            for i, part in enumerate(WIDE_HAN_RE.findall(e[field]) or [], 1):
                cur.execute(
                    "INSERT INTO component (char, component, role, seq)"
                    " VALUES (?,?,?,?)", (e["char"], part, role, i))
        if e["radical"]:
            cur.execute("UPDATE character SET radical=? WHERE char=?",
                        (e["radical"], e["char"]))

    for c in sorted(counts):
        g, tier = gloss.get(c, (None, "none"))
        cur.execute("INSERT OR REPLACE INTO glyph VALUES (?,?,?,?)",
                    (c, pin_of.get(c), g, "corpus"))
    for c, pin, g in load_component_glosses():
        cur.execute("INSERT OR IGNORE INTO glyph VALUES (?,?,?,?)",
                    (c, pin, g, "component-gloss"))

    # ---- tier (editorial) and centrality (computed, and only a proposal) ---
    for c, tier in load_tiers().items():
        cur.execute("UPDATE character SET tier=? WHERE char=?", (tier, c))
    cur.execute("UPDATE character SET tier='locked' WHERE tier IS NULL"
                " AND lock_status='locked'")

    # Centrality deliberately does NOT reduce to frequency. Three signals,
    # normalised and averaged: how much of the book a character reaches
    # (chapter spread), how often it occurs (rate), and how many distinct
    # characters it keeps company with inside a segment (collocational degree).
    # Spread and degree are what separate a load-bearing term from a common one:
    # a particle is frequent but keeps company with everything, and a term like
    # 全 is rare but sits at a hinge.
    degree = {}
    for (seg_id,) in cur.execute("SELECT id FROM segment").fetchall():
        chars = [r[0] for r in cur.execute(
            "SELECT DISTINCT char FROM token WHERE segment_id=?", (seg_id,))]
        for a in chars:
            degree.setdefault(a, set()).update(x for x in chars if x != a)
    max_total = max(counts.values())
    max_deg = max((len(v) for v in degree.values()), default=1)
    for c in counts:
        spread = len(chapters_of[c]) / 81.0
        rate = counts[c] / max_total
        deg = len(degree.get(c, ())) / max_deg
        cur.execute("UPDATE character SET centrality=? WHERE char=?",
                    (round((spread + rate + deg) / 3.0, 4), c))

    for row in cur.execute("SELECT term FROM compound").fetchall():
        term = row[0]
        hits = [n for n in sorted(han_by_chapter)
                if term in "".join(han_by_chapter[n])]
        total = sum("".join(han_by_chapter[n]).count(term) for n in hits)
        cur.execute("UPDATE compound SET total=?, chapters=? WHERE term=?",
                    (total, ",".join(str(x) for x in hits), term))

    # ---- chapter ratios (WORKLIST T5-1, the rule that finds absence) --------
    for n in sorted(chapters):
        words = sum(len(re.findall(r"[A-Za-z']+", e))
                    for _, e in verse_by_chapter.get(n, []))
        cur.execute("UPDATE chapter SET han_chars=?, english_words=? WHERE n=?",
                    (len(han_by_chapter[n]), words, n))

    # ---- the render table: locked characters against our English -----------
    for n in sorted(chapters):
        rows = cur.execute(
            "SELECT l.id, l.seq FROM line l WHERE l.chapter=? ORDER BY l.seq", (n,)
        ).fetchall()
        for lid, seq in rows:
            eng = cur.execute(
                "SELECT v.english, a.confidence, a.method FROM alignment a"
                " JOIN verse_line v ON v.id=a.verse_line_id WHERE a.line_id=?", (lid,)
            ).fetchall()
            if not eng:
                continue
            joined = " ".join(e for e, _, _ in eng)
            conf = min(c for _, c, _ in eng)
            method = eng[0][2]
            chars = cur.execute(
                "SELECT char, pinyin FROM token WHERE chapter=? AND line_seq=?"
                " ORDER BY char_pos", (n, seq)
            ).fetchall()
            for c, pin in chars:
                if c not in lock_of:
                    continue
                term, _, _ = lock_of[c]
                expected = render_of.get(c) or ""
                honored = None
                cands = [w.strip().lower() for w in re.split(r"[/·]", expected)
                         if w.strip()]
                # A flexion is the lock's English too, in the chapters it names.
                # Without this the atlas prints NOT FOUND on exactly the lines a
                # flexion exists to license — ch 9's 保 and 守 were both wrong.
                cands += [e.lower() for e, chs in flex_of.get(c, []) if n in chs]
                if cands:
                    low = joined.lower()
                    honored = 1 if any(w in low for w in cands) else 0
                cur.execute(
                    "INSERT INTO render (chapter, line_seq, char, pinyin, english,"
                    " lock_term, expected, honored, confidence, method)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (n, seq, c, pin, joined, term, expected, honored, conf, method),
                )

    # ---- witnesses ---------------------------------------------------------
    for w in [
        ("wangbi", "王弼", "Wáng Bì", "Wang Bi received recension", "received",
         226, 249, "欽定四庫全書, 1782", "public domain by age", 0,
         "base text of this edition; commentary covers 71 of 81 chapters"),
        ("heshanggong", "河上公", "Héshàng Gōng", "Heshang Gong", "received",
         -206, 220, "四部叢刊 0532, Song woodblock", "public domain by age", 0,
         "commentary complete at 81 of 81, with his own chapter titles"),
        ("hanfeizi", "韓非", "Hán Fēi", "Han Feizi, 解老 / 喻老", "quotation",
         -280, -233, "韓非子, ch. 20–21", "public domain by age", 0,
         "the oldest commentary; 53 quotations across the 17 chapters he discusses"),
        ("fuyi", "傅奕", "Fù Yì", "Fu Yi ancient text", "received",
         555, 639, "not yet vendored", "public domain by age; edition unverified", 0,
         "PROVENANCE names it admissible and owed; Phase 4"),
        ("guodian", "郭店", "Guōdiàn", "Guodian bamboo slips", "excavated",
         -320, -300, "excavated 1993", "FACTS ONLY — no transcription admissible", 0,
         "31 of 81 chapters attested; recorded as variant facts, never as text"),
        ("mawangdui-a", "馬王堆甲", "Mǎwángduī jiǎ", "Mawangdui silk A", "excavated",
         -206, -195, "excavated 1973", "FACTS ONLY — no transcription admissible", 0,
         "德 before 道; recorded as variant facts, never as text"),
        ("mawangdui-b", "馬王堆乙", "Mǎwángduī yǐ", "Mawangdui silk B", "excavated",
         -206, -168, "excavated 1973", "FACTS ONLY — no transcription admissible", 0,
         "德 before 道; recorded as variant facts, never as text"),
        ("beida", "北大", "Běidà", "Peking University Han bamboo", "excavated",
         -206, -100, "published 2012", "FACTS ONLY — no transcription admissible", 0,
         "recorded as variant facts, never as text"),
        ("fanyingyuan", "范應元", "Fàn Yìngyuán", "Fan Yingyuan", "received",
         1200, 1275, "not vendored", "public domain by age", 0, "cited in variants"),
    ]:
        cur.execute(
            "INSERT INTO witness (id, name_zh, name_pinyin, name_en, kind, date_low,"
            " date_high, edition, rights, is_full_text, coverage_note)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?)", w)

    # ---- the variant apparatus --------------------------------------------
    # One row per (entry, witness). Entries with no witness reading at all — a
    # punctuation fork at ch 32, an editorial one at ch 61 — still get a row with
    # a null witness. Dropping them would lose two real decisions, and it is the
    # kind of loss nothing downstream would ever notice.
    for group, v in enumerate(load_variants(), 1):
        readings = list((v.witnesses or {}).items()) or [(None, None)]
        for wid, reading in readings:
            cur.execute(
                "INSERT INTO variant (variant_group, chapter, line, base_reading,"
                " witness_id, witness_reading, meaning_bearing, our_call, followed,"
                " note, logged) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (group, v.chapter, v.line, v.base, wid, reading,
                 1 if v.meaning_bearing else 0, v.our_call,
                 "witness" if v.followed_a_witness else "base", v.note, v.logged),
            )

    # ---- commentary --------------------------------------------------------
    # A lemma is a slice of the base text, so our own English for the lines it
    # covers is already written and free to attach. Matching it is not a plain
    # equality test, for three reasons the data shows plainly:
    #
    #   1. a lemma often spans several of our lines, run together without
    #      punctuation — Wang Bi's first is 道可道非常道名可名非常名, which is two;
    #   2. the Siku and Song woodblocks use different glyph forms — 衆 for 眾,
    #      㣲 for 微, 𤣥 for 玄 (the last outside the BMP entirely);
    #   3. the Siku compilers' own 〔…〕 collation notes ride along inside it.
    #
    # So the chapter is concatenated into one folded string with an index back to
    # line numbers, and the folded lemma is located inside it. import_commentary's
    # `fold` already handles (2) and (3), and its CJK range is wider than this
    # module's on purpose: a narrower one silently deletes 𤣥.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from import_commentary import fold  # noqa: E402

    chapter_text, chapter_map, line_en = {}, {}, {}
    for n in sorted(chapters):
        rows_ = cur.execute(
            "SELECT l.id, l.seq, l.chinese FROM line l WHERE l.chapter=? ORDER BY l.seq",
            (n,)).fetchall()
        buf, index = [], []
        for lid, seq, chinese in rows_:
            folded = fold(chinese)
            buf.append(folded)
            index.extend([seq] * len(folded))
            eng = cur.execute(
                "SELECT group_concat(v.english, ' ') FROM alignment a"
                " JOIN verse_line v ON v.id=a.verse_line_id WHERE a.line_id=?",
                (lid,)).fetchone()[0]
            line_en[(n, seq)] = eng
        chapter_text[n] = "".join(buf)
        chapter_map[n] = index

    matched = unmatched = 0
    for slug, zh, pin, en in COMMENTATORS:
        d = COMMENTARIES / slug
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            fm = parse_frontmatter(raw) or {}
            n = fm.get("chapter")
            if not n:
                continue
            n = int(n)
            body = raw.split("---", 2)[-1]
            seq = 0
            for m in re.finditer(r"^\*\*(.+?)\*\*\s*\n+((?:^>.*\n?)*)", body, re.M):
                seq += 1
                lemma = m.group(1).strip()
                comment = "\n".join(
                    ln.lstrip("> ").rstrip()
                    for ln in m.group(2).split("\n") if ln.startswith(">")
                ).strip()

                hit, seqs = None, []
                needle = fold(lemma)
                hay = chapter_text.get(n, "")
                if needle and hay:
                    at = hay.find(needle)
                    if at >= 0:
                        seqs = sorted(set(chapter_map[n][at:at + len(needle)]))
                    else:
                        # A lemma the commentator quotes loosely: fall back to the
                        # longest of our lines that sits inside it.
                        best = None
                        for s2 in sorted({x for x in chapter_map[n]}):
                            f = fold(cur.execute(
                                "SELECT chinese FROM line WHERE chapter=? AND seq=?",
                                (n, s2)).fetchone()[0])
                            if f and f in needle and (best is None or len(f) > best[1]):
                                best = (s2, len(f))
                        if best:
                            seqs = [best[0]]
                if seqs:
                    parts = [line_en.get((n, s2)) for s2 in seqs]
                    hit = " ".join(p for p in parts if p) or None
                matched += 1 if hit else 0
                unmatched += 0 if hit else 1

                cur.execute(
                    "INSERT INTO commentary (commentator, commentator_en, chapter,"
                    " seq, lemma_zh, lemma_en, comment_zh, comment_en, lemma_matched,"
                    " line_seq) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (zh, en, n, seq, lemma, hit, comment or None, None,
                     1 if hit else 0, seqs[0] if seqs else None),
                )
    stats["lemma_matched"] = matched
    stats["lemma_unmatched"] = unmatched

    conn.commit()
    if report:
        print_report(cur, stats, align_stats)
    return stats, align_stats


# ------------------------------------------------------------------ reporting

def print_report(cur, stats, align_stats):
    q = lambda s: cur.execute(s).fetchone()[0]  # noqa: E731
    print("\n  corpus")
    print(f"    chapters          {q('SELECT count(*) FROM chapter')}")
    print(f"    lines             {q('SELECT count(*) FROM line')}")
    print(f"    segments          {q('SELECT count(*) FROM segment')}")
    print(f"    tokens            {q('SELECT count(*) FROM token')}")
    print(f"    unique characters {q('SELECT count(*) FROM character')}")
    print(f"    verse lines       {q('SELECT count(*) FROM verse_line')}")
    print(f"    compounds         {q('SELECT count(*) FROM compound')}")
    print(f"    variants          {q('SELECT count(*) FROM variant')}")
    print(f"    commentary        {q('SELECT count(*) FROM commentary')}")

    print("\n  pinyin")
    tot = stats["pinyin_ok"] + stats["pinyin_fail"]
    pct = 100.0 * stats["pinyin_ok"] / tot if tot else 0
    print(f"    lines aligned     {stats['pinyin_ok']}/{tot}  ({pct:.1f}%)")
    for n, seq, text in stats["unaligned"]:
        print(f"      ! ch {n} line {seq}: {text}")

    print("\n  line alignment")
    print(f"    exact-count       {align_stats['exact']} chapters")
    print(f"    proportional      {align_stats['proportional']} chapters  "
          f"(low confidence, flagged)")

    print("\n  gloss coverage — standing rule 0, measured")
    rows = cur.execute(
        "SELECT gloss_source, count(*), sum(total) FROM character"
        " GROUP BY gloss_source ORDER BY sum(total) DESC").fetchall()
    for tier, chars, occ in rows:
        print(f"    {tier:10} {chars:4} characters  {occ:5} occurrences")
    covered = q("SELECT sum(total) FROM character WHERE gloss_source!='none'")
    total = q("SELECT sum(total) FROM character")
    print(f"    → {100.0 * covered / total:.1f}% of running text carries a gloss")


# The regression baseline: what the corpus measured last time somebody looked.
#
# Each entry is (count, note), and **the note is required** — it says what the
# number counts and why it last moved. That is deliberate, and it is the same
# doctrine as `lock-ok` and `shaloms-call`: a suppression has to exist and has
# to cost something. A bare number invites the one response that destroys the
# check, which is to bump it until the build goes green. Writing down what
# moved and when makes the bump an argument instead of a reflex, and makes a
# reviewer able to tell a real corpus change from a test bent to pass.
#
# If a count moves and you did not mean it to, something changed the corpus
# without meaning to — that is the finding, not the failure.
BASELINE = {
    "chapter":    (81, "one file in chapters/, 1-81"),
    "line":       (798, "source-table rows across all chapters"),
    "token":      (5296, "Han characters in the base text"),
    "character":  (798, "rows in the character table"),
    "variant":    (84, "distinct variant_group rows, from sources/variants.yaml. "
                       "75→82 the 韓非 harvest, 2026-09-10 (R1) · "
                       "82→83 ch 9 功遂 / 功成名遂, 2026-09-20 · "
                       "83→84 ch 20 昏昏 / 若昏, 2026-09-20"),
    "verse_line": (855, "English verse lines across chapters/*.md. "
                        "854→855 ch 26's 奈何萬乘之主，而以身輕天下 set as its "
                        "two comma-segments, 2026-09-20"),
}


def baseline_count(cur, table):
    """One place that knows how each baselined table is counted."""
    if table == "variant":
        return cur.execute(
            "SELECT count(DISTINCT variant_group) FROM variant").fetchone()[0]
    return cur.execute(f"SELECT count(*) FROM {table}").fetchone()[0]



def verify(cur):
    ok = True
    print("\n  verification")
    for table, (expected, note) in BASELINE.items():
        got = baseline_count(cur, table)
        flag = "ok " if got == expected else "FAIL"
        ok &= got == expected
        print(f"    {flag} {table:12} {got:5}  expected {expected}")
        if got != expected:
            print(f"         counts: {note}")
            print(f"         if this move is intended, update BASELINE and extend "
                  f"its note with the date and the cause.")

    bad = cur.execute(
        "SELECT count(*) FROM token t JOIN line l"
        " ON l.chapter=t.chapter AND l.seq=t.line_seq"
        " WHERE instr(l.chinese, t.char)=0").fetchone()[0]
    print(f"    {'ok ' if bad == 0 else 'FAIL'} round trip   "
          f"{bad} tokens not found in their own line")
    ok &= bad == 0

    missing = cur.execute(
        "SELECT count(*) FROM token WHERE pinyin IS NULL").fetchone()[0]
    print(f"    {'ok ' if missing == 0 else 'FAIL'} rule 0       "
          f"{missing} tokens with no pinyin")
    ok &= missing == 0
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--report", action="store_true", help="print the coverage report")
    ap.add_argument("--verify", action="store_true", help="assert the baseline")
    ap.add_argument("-o", "--out", default=str(DB_PATH))
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()

    conn = sqlite3.connect(out)
    stats, align_stats = build(conn, report=args.report or args.verify)
    rc = 0
    if args.verify and not verify(conn.cursor()):
        rc = 1
    conn.close()
    print(f"\n  → {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
