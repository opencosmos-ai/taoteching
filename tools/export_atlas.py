#!/usr/bin/env python3
"""export_atlas.py — this text's contribution to the Character Atlas.

    python3 tools/export_atlas.py      # writes data/atlas-export.json

The Open Classical Chinese Character Atlas (opencosmos-ai/chinese-atlas) serves
every OpenCosmos Chinese translation from one site. It never reads this
repository's internals. It reads this one file, which is the contract between
them: every character with its 說文 analysis and this translation's rendering,
every line it stands in, and every glossary entry in full.

**Nothing here is authored.** The characters come from the database, which
comes from the manuscript; the entries are `glossary/*.md`, frontmatter and
body, verbatim. Edit an entry, rebuild, and the atlas changes. CI gates the
file like the rest of `data/`, so a stale export cannot be merged.
"""

import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_explorer import DB_PATH, payload  # noqa: E402
from lib.corpus import GLOSSARY, ROOT, parse_frontmatter  # noqa: E402

OUT = ROOT / "data" / "atlas-export.json"

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


def main():
    if not DB_PATH.exists():
        print("  no database — run: python3 tools/build_db.py")
        return 2
    conn = sqlite3.connect(DB_PATH)
    data = payload(conn)
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

    out = {"contract": CONTRACT, "text": TEXT, **data, "entries": ents}
    # Indented, so a glossary edit shows up as a readable diff here too.
    OUT.write_text(json.dumps(out, ensure_ascii=False, sort_keys=True,
                              indent=1) + "\n", encoding="utf-8")
    print(f"  {len(data['chars'])} characters · {len(ents)} entries"
          f" · {OUT.stat().st_size / 1024:.0f} KB\n  → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
