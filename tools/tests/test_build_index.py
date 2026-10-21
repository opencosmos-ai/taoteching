#!/usr/bin/env python3
"""
Tests for build_index.py's `binds:` column — the one field another book reads.

    python3 -m unittest discover tools/tests

The I Ching vendors glossary/terms.yaml as its own lock table and enforces
every lock in it. `binds:` is how an entry stays in this book, so a generator
that drops it silently hands that book a lock it has ruled against: 咎 (jiù)
as *fault*, forbidding the *blame* its verdict formula 无咎 reads ninety-two
times. These tests read the real entries and the real generated file, so they
fail when terms.yaml is stale as well as when the generator is wrong.
"""

import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.corpus import GLOSSARY, parse_frontmatter  # noqa: E402


def entry_binds():
    """{term: binds list or None}, from each entry's own frontmatter."""
    out = {}
    for path in sorted(GLOSSARY.glob("*.md")):
        if path.name in ("INDEX.md", "TRIAGE.md"):
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8")) or {}
        out[fm.get("term", "")] = fm.get("binds") or None
    return out


def yaml_binds():
    """{term: binds list or None}, from the generated terms.yaml."""
    out = {}
    text = (GLOSSARY / "terms.yaml").read_text(encoding="utf-8")
    for blk in text.split("\n- term:")[1:]:
        term = re.match(r'\s*"([^"]*)"', blk).group(1)
        m = re.search(r"^  binds: \[([^\]]*)\]$", blk, re.M)
        out[term] = [b.strip() for b in m.group(1).split(",")] if m else None
    return out


class BindsTest(unittest.TestCase):
    def test_terms_yaml_carries_every_entrys_binds(self):
        want, got = entry_binds(), yaml_binds()
        for term, binds in want.items():
            with self.subTest(term=term):
                self.assertEqual(got.get(term), binds,
                                 "terms.yaml disagrees with the entry — run tools/build_index.py")

    def test_the_first_two_stay_in_this_book(self):
        got = yaml_binds()
        self.assertEqual(got.get("咎"), ["taoteching"])
        self.assertEqual(got.get("尤"), ["taoteching"])


if __name__ == "__main__":
    unittest.main()
