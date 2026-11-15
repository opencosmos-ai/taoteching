#!/usr/bin/env python3
"""
Tests for term_where() — the one rule for where a glossary term stands.

    python3 -m unittest discover -s tools/tests

glossary/INDEX.md, terms.yaml and the `where` of every entry in
data/atlas-export.json all come from it, and the Library on opencosmos.ai reads
that `where` for its Key Terms instead of counting. Two rules disagreed once:
INDEX counted only the first half of a pairing, so 我 & 吾 stood in 7 chapters
there and 19 in the Library (2026-11-15). These tests pin the rule, and check
that every place it reaches agrees with it, so a stale file fails here too.
"""

import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.corpus import (  # noqa: E402
    GLOSSARY, ROOT, load_chapters, term_chapters, term_parts, term_where,
)


def per_chapter(where):
    out = {}
    for k, n in where:
        c = int(k.split(".")[0])
        out[c] = out.get(c, 0) + n
    return out


class TermWhere(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ch = load_chapters()

    def test_parts(self):
        self.assertEqual(term_parts("無 & 有"), ["無", "有"])
        self.assertEqual(term_parts("歸 & 復 & 反"), ["歸", "復", "反"])
        self.assertEqual(term_parts("天地"), ["天地"])

    def test_chang_four_times_in_chapter_one(self):
        """非常道, 非常名, 常無欲, 常有欲."""
        self.assertEqual(per_chapter(term_where("常", self.ch)).get(1), 4)

    def test_every_half_of_a_pairing_counts(self):
        """Chapter 4 has 吾 and no 我: the pairing still stands there."""
        self.assertIn("吾", self.ch[4].chinese)
        self.assertNotIn("我", self.ch[4].chinese)
        self.assertIn(4, term_chapters(term_where("我 & 吾", self.ch)))
        self.assertEqual(per_chapter(term_where("玄 & 妙", self.ch)).get(1), 5)

    def test_a_part_inside_a_compound_counts_on_its_own(self):
        """Chapter 1's only 天 is the one in 天地."""
        self.assertEqual(per_chapter(term_where("天", self.ch)).get(1), 1)
        self.assertEqual(per_chapter(term_where("天地", self.ch)).get(1), 1)

    def test_lines_are_the_exports_lines(self):
        """A "ch.line" key names the source row the export's `lines` names."""
        for k, _ in term_where("道", self.ch)[:20]:
            n, i = map(int, k.split("."))
            self.assertIn("道", self.ch[n].source_rows[i - 1].chinese)


class EveryReaderAgrees(unittest.TestCase):
    """The generated files carry the rule's answer, or they are stale."""

    @classmethod
    def setUpClass(cls):
        ch = load_chapters()
        cls.want = {}
        text = (GLOSSARY / "terms.yaml").read_text(encoding="utf-8")
        for blk in text.split("\n- term:")[1:]:
            term = re.match(r'\s*"([^"]*)"', blk).group(1)
            cls.want[term] = term_where(term, ch)
        cls.yaml = {}
        for blk in text.split("\n- term:")[1:]:
            term = re.match(r'\s*"([^"]*)"', blk).group(1)
            m = re.search(r"^  chapters: \[([^\]]*)\]$", blk, re.M)
            cls.yaml[term] = [int(x) for x in re.findall(r"\d+", m.group(1))] if m else []
        export = json.loads((ROOT / "data" / "atlas-export.json").read_text(encoding="utf-8"))
        cls.export = {e["term"]: e.get("where") for e in export["entries"]}

    def test_terms_yaml_chapters(self):
        for term, where in self.want.items():
            with self.subTest(term=term):
                self.assertEqual(self.yaml[term], term_chapters(where),
                                 "terms.yaml is stale — run tools/build_index.py")

    def test_export_where(self):
        self.assertEqual(set(self.export), set(self.want))
        for term, where in self.want.items():
            with self.subTest(term=term):
                self.assertEqual(self.export[term], where,
                                 "the export is stale — run tools/export_atlas.py")


if __name__ == "__main__":
    unittest.main()
