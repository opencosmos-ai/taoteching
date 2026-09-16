#!/usr/bin/env python3
"""build_graph.py — the corpus as a knowledge graph, for the OpenCosmos constellation.

    python3 tools/build_graph.py                 # both graphs
    python3 tools/build_graph.py --graph text    # chapters only, existing schema
    python3 tools/build_graph.py --graph chars   # the character graph

Writes `data/constellation-*.json` in the node/link shape
`scripts/knowledge/generate-constellation-graph.ts` already emits, so the
OpenCosmos generator can merge these payloads instead of parsing this repo.

**Why the payload and not the renderer.** This repository is stdlib-only Python
and its CI has no dependency-install step, deliberately — a fresh clone runs the
checks with nothing else present. `@opencosmos/constellation` is a React/WebGL
package. Putting it here would trade that property away for a picture. So the
boundary is drawn at the data: **this repo emits, OpenCosmos renders.** Neither
side acquires the other's dependency tree.

**Why this is licence-safe, which is not an accident.** OpenCosmos decision 0009
rejected `@cosmograph/cosmograph` because it is CC BY-NC-4.0, and non-commercial
"constrains what OpenCosmos can ever become." That is the same argument
`sources/PROVENANCE.md` makes about texts, applied to code — and it is why these
two repositories can meet at all. This repo is CC0 with no exceptions and the
companion volume is intended to be sold; a CC BY-NC dependency anywhere in the
chain would poison both. `@cosmos.gl/graph` is MIT. The compatibility was won by
a decision someone already made carefully, on the other side.

Two graphs, because they answer different questions.

**text** — the shape OpenCosmos already speaks: one `work` node, 81 `section`
nodes, edges of type `contains`. This is the translation taking its place in the
corpus beside the other traditions.

**chars** — the shape this corpus alone can offer: every character, every part it
is built from, and every chapter, wired together. A force-directed layout over
shared components does something a list cannot — it puts the water characters
near each other without being told to, because they share 水. The semantic
families lay themselves out.
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.corpus import ROOT  # noqa: E402

DB_PATH = ROOT / "data" / "taoteching.sqlite"
OUT_DIR = ROOT / "data"

WORK_ID = "work:tao-te-ching-ormsby"

# Enough co-occurrence to mean something. Two characters sharing one segment
# somewhere in 5,296 tokens is noise; the graph is unreadable if every
# coincidence becomes an edge, and force layout is especially punished by it.
MIN_COOCCURRENCE = 4


def text_graph(conn):
    """One work, 81 sections — the existing constellation schema, exactly."""
    nodes = [{
        "id": WORK_ID, "tier": "work",
        "label": "Tao Te Ching — a translation from the source",
        "tradition": "taoism", "domain": "wisdom",
        "author": "Laozi 老子 (Lǎozǐ), translated by Shalom Ormsby",
        "provenanceStatus": "CC0 — public domain dedication, no rights reserved",
        "degree": 0, "x": 0.0, "y": 0.0,
    }]
    links = []
    for r in conn.execute(
        "SELECT n, hsg_title_zh, hsg_title_pinyin, hsg_title_en,"
        " guodian_attested, han_chars, english_words FROM chapter ORDER BY n"
    ):
        n, zh, pin, en, guodian, han, words = r
        # Every label carries English. A constellation node reading 體道 tells an
        # English reader nothing, and standing rule 0 does not stop at the repo
        # boundary — it is about the reader, and the reader is the same person.
        label = f"{n}. {en}" if en else f"Chapter {n}"
        nodes.append({
            "id": f"section:ttc-{n:03d}", "tier": "section", "label": label,
            "parent": WORK_ID, "tradition": "taoism", "domain": "wisdom",
            "category": "chapter",
            "heshanggongTitle": zh, "heshanggongPinyin": pin,
            "heshanggongEnglish": en,
            "guodianAttested": bool(guodian),
            "hanChars": han, "englishWords": words,
            "degree": 0, "x": 0.0, "y": 0.0,
        })
        links.append({"source": WORK_ID, "target": f"section:ttc-{n:03d}",
                      "type": "contains"})
    return nodes, links


def char_graph(conn):
    """Characters, the parts they are built from, and the chapters they live in."""
    nodes, links = [], []
    # Every query below is ordered, and the co-occurrence map is emitted sorted.
    # Not for tidiness: this file is committed, and CI rebuilds it and diffs it
    # against the commit. Unordered SQLite results are stable for one machine
    # and one planner version, which is exactly the kind of stability that
    # breaks when the gate moves to another machine. Ordering makes the output
    # a function of the data alone.
    seen = set()

    def add(node):
        if node["id"] not in seen:
            seen.add(node["id"])
            nodes.append(node)

    for r in conn.execute("""
        SELECT c.char, c.pinyin, c.gloss, c.our_render, c.lock_status, c.tier,
               c.centrality, c.total, c.is_function_word, s.kind, s.radical
          FROM character c LEFT JOIN shuowen s ON s.char = c.char
         WHERE c.is_function_word = 0
         ORDER BY c.char"""):
        char, pin, gloss, render, lock, tier, cent, total, _fw, kind, rad = r
        label = f"{char} {pin}" + (f" · {gloss}" if gloss else "")
        add({
            "id": f"char:{char}", "tier": "quote" if lock else "section",
            "label": label, "parent": WORK_ID,
            "tradition": "taoism", "domain": "wisdom",
            "category": "character",
            "han": char, "pinyin": pin, "gloss": gloss, "ourRender": render,
            "locked": bool(lock), "triageTier": tier, "centrality": cent,
            "occurrences": total, "construction": kind, "shuowenSection": rad,
            "degree": 0, "x": 0.0, "y": 0.0,
        })

    for r in conn.execute("""
        SELECT DISTINCT c.component, c.role, g.pinyin, g.gloss
          FROM component c LEFT JOIN glyph g ON g.char = c.component
         ORDER BY c.component, c.role"""):
        comp, role, pin, gloss = r
        meaning = gloss or ("sound only — carries no meaning"
                            if role == "phonetic" else "not yet glossed")
        add({
            "id": f"part:{comp}", "tier": "synthesis",
            "label": f"{comp} {pin or ''} · {meaning}".strip(),
            "tradition": "taoism", "domain": "wisdom", "category": "component",
            "han": comp, "pinyin": pin, "gloss": gloss,
            "glossed": gloss is not None,
            "degree": 0, "x": 0.0, "y": 0.0,
        })

    # A part builds a character. The edge type carries the one distinction a
    # radical index throws away, so the renderer can colour by it.
    for r in conn.execute("SELECT DISTINCT char, component, role FROM component"
                          " ORDER BY char, component, role"):
        char, comp, role = r
        if f"char:{char}" in seen:
            links.append({"source": f"part:{comp}", "target": f"char:{char}",
                          "type": "builds_semantic" if role == "semantic"
                                  else "builds_phonetic"})

    for r in conn.execute(
        "SELECT n, hsg_title_en, guodian_attested FROM chapter ORDER BY n"
    ):
        n, en, guodian = r
        add({
            "id": f"ch:{n}", "tier": "tradition",
            "label": f"Chapter {n}" + (f" — {en}" if en else ""),
            "tradition": "taoism", "domain": "wisdom", "category": "chapter",
            "guodianAttested": bool(guodian),
            "degree": 0, "x": 0.0, "y": 0.0,
        })

    for r in conn.execute("""
        SELECT DISTINCT t.char, t.chapter FROM token t
          JOIN character c ON c.char = t.char
         WHERE c.is_function_word = 0
         ORDER BY t.char, t.chapter"""):
        char, n = r
        if f"char:{char}" in seen:
            links.append({"source": f"char:{char}", "target": f"ch:{n}",
                          "type": "occurs_in"})

    # Characters that keep company inside a segment. This is the edge that makes
    # the layout say something: the force solver pulls co-occurring terms
    # together, so the book's own conceptual neighbourhoods emerge rather than
    # being asserted.
    pairs = {}
    for (seg_id,) in conn.execute("SELECT id FROM segment ORDER BY id").fetchall():
        chars = sorted({r[0] for r in conn.execute(
            "SELECT t.char FROM token t JOIN character c ON c.char = t.char"
            " WHERE t.segment_id = ? AND c.is_function_word = 0", (seg_id,))})
        for i, a in enumerate(chars):
            for b in chars[i + 1:]:
                pairs[(a, b)] = pairs.get((a, b), 0) + 1
    for (a, b), n in sorted(pairs.items()):
        if n >= MIN_COOCCURRENCE and f"char:{a}" in seen and f"char:{b}" in seen:
            links.append({"source": f"char:{a}", "target": f"char:{b}",
                          "type": "semantic", "weight": n})

    degree = {}
    for e in links:
        degree[e["source"]] = degree.get(e["source"], 0) + 1
        degree[e["target"]] = degree.get(e["target"], 0) + 1
    for node in nodes:
        node["degree"] = degree.get(node["id"], 0)

    return nodes, links


META = {
    "source": "https://github.com/opencosmos-ai/taoteching",
    "rights": "CC0 1.0 Universal — public domain dedication, no rights reserved",
    "generator": "tools/build_graph.py",
    "note": ("Chinese is public domain by age. English glosses, renderings and "
             "translation are by Shalom Ormsby, dedicated CC0. The excavated "
             "manuscripts appear nowhere as text — only as recorded variant "
             "facts; see sources/PROVENANCE.md."),
}


def write(name, nodes, links):
    path = OUT_DIR / f"constellation-{name}.json"
    payload = {"meta": dict(META, graph=name),
               "nodes": nodes, "links": links}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1),
                    encoding="utf-8")
    kinds = {}
    for e in links:
        kinds[e["type"]] = kinds.get(e["type"], 0) + 1
    print(f"\n  {name}: {len(nodes)} nodes · {len(links)} edges "
          f"· {path.stat().st_size / 1024:.0f} KB")
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print(f"      {k:18} {v}")
    print(f"      → {path.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--graph", choices=("text", "chars", "both"), default="both")
    ap.add_argument("--db", default=str(DB_PATH))
    args = ap.parse_args()

    db = Path(args.db)
    if not db.exists():
        print(f"  no database at {db} — run: python3 tools/build_db.py")
        return 2

    conn = sqlite3.connect(db)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.graph in ("text", "both"):
        write("text", *text_graph(conn))
    if args.graph in ("chars", "both"):
        write("chars", *char_graph(conn))
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
