#!/usr/bin/env python3
"""export_atlas.py — this text's contribution to the Character Atlas.

    python3 tools/export_atlas.py      # writes data/atlas-export.json

The Open Classical Chinese Character Atlas (opencosmos-ai/chinese-atlas) serves
every OpenCosmos Chinese translation from one site. It never reads this
repository's internals. It reads this one file, which is the contract between
them: every character with its 說文 analysis and this translation's rendering,
every line it stands in, and every glossary entry in full.

**It is also what the Library's reader reads** (opencosmos.ai, one page per
chapter — opencosmos ADR 0020), so it carries four keys the atlas ignores:

    verse    {chapter: [[line, …], …]}   the English, stanza by stanza, as authored
    notes    {chapter: markdown}         the chapter's `## Notes`, "" when it has none;
                                         `<!-- lock-ok -->` waivers are for the checker
                                         and are left out; relative links are made
                                         absolute, since no reader of the export has
                                         this repository beside it
    literal  {"ch.line": markdown}       the source table's Literal cell, as authored —
                                         pre-lock English, a starting point, not a reading
    align    {"ch.line": [[verse, confidence, method], …]}
                                         which English lines render this Chinese line:
                                         `verse` is 1-based across the chapter's stanzas,
                                         as in the `verse` key. `method` is exact-count
                                         (1.0, the counts agree, so the pairing is certain),
                                         proportional (0.3) or proportional-fill (0.2):
                                         a guess, never to be shown as a pairing

Additions only, so `contract` stays 1: the atlas refuses any other number, and
reads none of these keys.

**Nothing here is authored.** The characters come from the database, which
comes from the manuscript; the entries are `glossary/*.md`, frontmatter and
body, verbatim. Edit an entry, rebuild, and the atlas changes. CI gates the
file like the rest of `data/`, so a stale export cannot be merged.
"""

import json
import posixpath
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_explorer import DB_PATH, payload  # noqa: E402
from lib.corpus import GLOSSARY, ROOT, load_chapters, parse_frontmatter  # noqa: E402

OUT = ROOT / "data" / "atlas-export.json"
BLOB = "https://github.com/opencosmos-ai/taoteching/blob/main/"

# Bumped when the shape changes in a way a reader must know about.
CONTRACT = 1

TEXT = {
    "id": "tao-te-ching",
    "title": "Tao Te Ching",
    "title_zh": "道德經",
    "repo": "opencosmos-ai/taoteching",
    "unit": "chapter",
    "abbr": "CH",
    "units": 81,
    "cols": 9,
    # The oldest witness, for the map's second view. chapters[n][3] says
    # whether it carries chapter n, and main() counts `carries` from those same
    # rows — it was a typed 31 once, true but kept by hand beside the data
    # that says so.
    "witness": {"name": "Guodian", "date": "c. 300 BCE"},
}


def entries():
    out = []
    for path in sorted(GLOSSARY.glob("*.md")):
        if path.name in ("INDEX.md", "TRIAGE.md"):
            continue
        raw = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(raw) or {}
        body = raw.split("\n---\n", 1)[1] if raw.startswith("---\n") else raw
        term = fm.get("term", "")
        out.append({
            "slug": path.stem,
            "path": f"glossary/{path.name}",
            "term": term,
            # A pairing writes its term "我 & 吾"; the atlas wants the characters.
            "chars": [c for c in term if "㐀" <= c <= "鿿"],
            "pinyin": fm.get("pinyin", ""),
            "render": fm.get("render", ""),
            "status": fm.get("status", ""),
            "forbidden": fm.get("forbidden") or [],
            "flexions": fm.get("flexions") or [],
            "covers": [c for c, _ in fm.get("covers") or []],
            "shuowen": fm.get("shuowen", ""),
            "body": body.lstrip("\n"),
        })
    return out


def absolute_links(markdown, base="chapters"):
    """`](../process/x.md)` → `](https://github.com/…/blob/main/process/x.md)`.

    Notes link to the repository's own files relative to `chapters/`. Read
    anywhere else — the Library, Cosmo's corpus copy — those links point at
    nothing. URLs, anchors and mail links are left as they are.
    """
    def fix(m):
        target = m.group(1)
        if re.match(r"[a-z]+:|#|/", target):
            return m.group(0)
        path, _, frag = target.partition("#")
        full = posixpath.normpath(posixpath.join(base, path))
        if full.startswith(".."):
            return m.group(0)
        return f"]({BLOB}{full}{'#' + frag if frag else ''})"
    return re.sub(r"\]\(([^)\s]+)\)", fix, markdown)


def reader(conn, chapters=None):
    """What a reader of the text needs beyond the atlas: verse, notes, literal
    glosses, and how sure each line's pairing with its English is.

    The verse and the alignment come from the database, so they are the same
    lines check_locks and the concordance see. The notes are the one thing the
    database does not hold, and come straight from the chapter files.
    """
    q = conn.execute
    verse = {}
    for n, stanza, english in q(
            "SELECT chapter, stanza, english FROM verse_line ORDER BY chapter, seq"):
        stanzas = verse.setdefault(str(n), [])
        if len(stanzas) < stanza:
            stanzas.append([])
        stanzas[-1].append(english)

    literal = {f"{n}.{seq}": lit or "" for n, seq, lit in q(
        "SELECT chapter, seq, literal FROM line ORDER BY chapter, seq")}

    align = {}
    for n, seq, vseq, conf, method in q("""
            SELECT l.chapter, l.seq, v.seq, a.confidence, a.method
              FROM alignment a
              JOIN line l ON l.id = a.line_id
              JOIN verse_line v ON v.id = a.verse_line_id
          ORDER BY l.chapter, l.seq, v.seq"""):
        align.setdefault(f"{n}.{seq}", []).append([vseq, conf, method])

    chapters = chapters if chapters is not None else load_chapters()
    notes = {str(n): absolute_links(re.sub(r"\n{3,}", "\n\n",
                            re.sub(r"<!--.*?-->", "", ch.notes, flags=re.S))).strip()
             for n, ch in sorted(chapters.items())}

    return {"verse": verse, "notes": notes, "literal": literal, "align": align}


def main():
    if not DB_PATH.exists():
        print("  no database — run: python3 tools/build_db.py")
        return 2
    conn = sqlite3.connect(DB_PATH)
    data = payload(conn)
    read = reader(conn)
    conn.close()

    ents = entries()
    # Every entry a character belongs to: its own, a compound it stands in, and
    # any entry that covers it as a secondary character.
    member = {}
    for e in ents:
        for c in set(e["chars"]) | set(e["covers"]):
            member.setdefault(c, []).append(e["slug"])
    for c in data["chars"]:
        c["entries"] = sorted(member.get(c["c"], []))
    TEXT["witness"]["carries"] = sum(1 for ch in data["chapters"].values() if ch[3])

    out = {"contract": CONTRACT, "text": TEXT, **data, **read, "entries": ents}
    # Indented, so a glossary edit shows up as a readable diff here too.
    OUT.write_text(json.dumps(out, ensure_ascii=False, sort_keys=True,
                              indent=1) + "\n", encoding="utf-8")
    print(f"  {len(data['chars'])} characters · {len(ents)} entries"
          f" · {OUT.stat().st_size / 1024:.0f} KB\n  → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
