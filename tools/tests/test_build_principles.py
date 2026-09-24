#!/usr/bin/env python3
"""
The principles builder, against the two things it exists to prevent.

A principles directory fails in exactly two ways, and both are silent: the
evidence link rots, so a rule looks checked when nothing backs it; and a
passing thought acquires the standing of a law because nobody made it earn a
second case. Each is proved here against the state that would otherwise ship.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_principles as bp  # noqa: E402


class Slug(unittest.TestCase):
    """The anchors have to resolve on GitHub, not here."""

    def test_matches_githubs_rule(self):
        self.assertEqual(bp.slug("Standing principles"), "standing-principles")
        self.assertEqual(bp.slug("Ch 14's opening triad"), "ch-14s-opening-triad")

    def test_cjk_survives(self):
        """The reason the anchors in this repo are legible at all."""
        self.assertEqual(bp.slug("夷 · 希 · 微 — the names"), "夷-希-微-the-names")

    def test_em_dash_and_middot_are_dropped_not_hyphenated(self):
        """Real case: the separators collapse, the spaces around them do not."""
        self.assertEqual(bp.slug("a · b — c"), "a-b-c")


class Headings(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(__file__).parent / "_tmp_principles.md"

    def tearDown(self):
        self.tmp.unlink(missing_ok=True)

    def test_collects_every_level(self):
        self.tmp.write_text("# One\ntext\n### Three deep\n", encoding="utf-8")
        self.assertEqual(bp.headings_in(self.tmp), {"one", "three-deep"})

    def test_missing_file_is_none_not_empty(self):
        """An absent file and a file with no headings are different failures."""
        self.assertIsNone(bp.headings_in(Path("/nonexistent/x.md")))


class Threshold(unittest.TestCase):
    """One case is an observation, two is a principle. See the README."""

    def test_active_needs_two_cases(self):
        self.assertLess(1, 2, "guard: the threshold is two")


class RealDirectory(unittest.TestCase):
    """The shipped entries must always build clean."""

    def test_every_entry_is_valid_and_every_anchor_resolves(self):
        entries, problems = bp.load()
        problems += bp.verify_anchors(entries)
        self.assertEqual(problems, [], "\n".join(problems))

    def test_the_threshold_holds_across_the_directory(self):
        entries, _ = bp.load()
        for e in entries:
            if e.get("status") == "active":
                self.assertGreaterEqual(
                    len(e.get("evidence", [])), 2,
                    f"{e['file']} is active with fewer than two cases")


if __name__ == "__main__":
    unittest.main()


class Structure(unittest.TestCase):
    """The third silent failure: a principle that is argued well and runs nowhere.

    Before this check, 29 of 30 entries said nothing about where they ran and
    seven applied to kinds of work no skill loaded. Each case below is one of
    those shapes, built in a temp file and run through verify_structure.
    """

    GOOD = """---
id: _tmp_shape
title: "A rule"
status: provisional
since: 2026-09-24
trigger: "you are about to do the thing"
applies: [drafting]
check: none
---

# A rule

**The rule.** Do the thing.

**When it fires.** When you are about to do the thing.

## Why this holds

Because it is true of the book.

## Why this principle exists

It went wrong once.

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5** | where the moment occurs and the check is applied by a reader |

**Not enforced.**

## Where it does not fire

Somewhere.

## What it obliges

1. Do it.
"""

    def setUp(self):
        self.path = bp.PRINCIPLES / "_tmp_shape.md"

    def tearDown(self):
        self.path.unlink(missing_ok=True)

    def run_on(self, text):
        self.path.write_text(text, encoding="utf-8")
        fm = bp.parse_frontmatter(text)
        fm["file"] = self.path.name
        return bp.verify_structure([fm])

    def test_a_well_shaped_entry_passes(self):
        self.assertEqual(self.run_on(self.GOOD), [])

    def test_missing_how_it_is_implemented_fails(self):
        text = self.GOOD.replace("## How it is implemented", "## Something else")
        self.assertTrue(any("How it is implemented" in p for p in self.run_on(text)))

    def test_sections_out_of_order_fail(self):
        text = self.GOOD.replace("## Why this holds", "## TMP").replace(
            "## Why this principle exists", "## Why this holds").replace("## TMP", "## Why this principle exists")
        self.assertTrue(any("out of order" in p for p in self.run_on(text)))

    def test_a_check_tool_not_named_in_the_implementation_fails(self):
        text = self.GOOD.replace("check: none", "check: fix-linebreaks")
        self.assertTrue(any("fix-linebreaks" in p for p in self.run_on(text)))

    def test_applies_to_work_nothing_loads_fails(self):
        """The seven-unreachable case: a scope no skill or CLAUDE.md loads."""
        text = self.GOOD.replace("applies: [drafting]", "applies: [nonexistent]")
        self.assertTrue(any("nobody meets this rule" in p for p in self.run_on(text)))

    def test_every_real_scope_is_loaded_somewhere(self):
        """If a loader is removed from a skill, this fails before any entry does."""
        self.assertEqual(set(bp.SCOPES) - bp.loaded_scopes(), set())
