#!/usr/bin/env python3
"""
The retractions checker, against the copies it was written to find.

The fixtures are the real sentences that kept the Ch 25 claim alive for two
months after it was corrected. Each is proved found as it stood, then left
alone once it announces its own correction, so the checker is shown to catch a
copy and to spare a correction, not only to pass.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_retractions as cr  # noqa: E402

CH25 = cr.Retraction(
    id="ch25", retracted="2026-08-20", claim="the silks read 人",
    match=["silks read 人", "oldest witnesses proved"],
    correction="every excavated witness reads 王", see="sources/variants.yaml")


def found(text, rel="notes/x.md", entries=(CH25,)):
    return cr.copies_in(text, rel, list(entries))


class Copies(unittest.TestCase):

    def test_the_claim_as_it_stood_in_claude_md(self):
        line = ("Ch 25's *king* was caught exactly this way, and the oldest "
                "witnesses proved him right (`DISCOVERIES.md` §1).")
        self.assertEqual([c.phrase for c in found(line)], ["oldest witnesses proved"])

    def test_matching_ignores_case(self):
        self.assertEqual(len(found("**Both Mawangdui Silks Read 人** (rén)")), 1)

    def test_one_finding_per_line_per_entry(self):
        self.assertEqual(len(found("silks read 人, and the oldest witnesses proved it")), 1)

    def test_a_line_that_announces_its_correction_is_spared(self):
        for line in (
            "*(This note once said both Mawangdui silks read 人. They do not.)*",
            "CORRECTED 2026-08-20. This entry previously recorded \"both silks read 人\"",
            "**⚠ It is not true that the silks read 人.**",
            "(was: both silks read 人)",
            "~~both silks read 人~~",
            "This sentence formerly contrasted Ch 25, on the claim that the silks read 人.",
        ):
            self.assertEqual(found(line), [], line)


class Banners(unittest.TestCase):

    DOC = "\n".join([
        "## 4 · The throne was installed four times",
        "",
        "> **⚠ ONE OF THE FOUR IS WITHDRAWN.**",
        "",
        "### The installations",
        "Both Mawangdui silks read 人, and Han scribes put the king in.",
        "",
        "## 5 · Another finding",
        "Both Mawangdui silks read 人, and nothing here says otherwise.",
    ])

    def test_a_banner_covers_its_section_and_subsections(self):
        self.assertEqual([c.line for c in found(self.DOC)], [9])

    def test_a_banner_deep_in_one_subsection_covers_only_that_one(self):
        doc = "\n".join([
            "## Rendering decisions",
            "### Ch 25",
            "⚠ the silks do not read 人 after all.",
            "### 天子",
            "the same move §1 catches in Ch 25, where both Mawangdui silks read 人.",
        ])
        self.assertEqual([c.line for c in found(doc)], [5])

    def test_banners_are_a_markdown_idea(self):
        doc = "## x\n⚠\nsilks read 人"
        self.assertEqual([c.line for c in found(doc, rel="sources/variants.yaml")], [3])
        self.assertEqual(found(doc, rel="notes/x.md"), [])


class Scope(unittest.TestCase):

    def test_allow_and_history_are_not_copies(self):
        e = cr.Retraction(id="line1", retracted="2026-10-16", claim="c",
                          match=["Tao that can be spoken is not the ever-present Tao"],
                          correction="made a way", see="chapters/001.md",
                          allow=["source/archive-*.md"])
        line = "The Tao that can be spoken is not the ever-present Tao."
        self.assertEqual(found(line, "source/archive-google-doc-final-export-2026-08-09.md", [e]), [])
        self.assertEqual(len(found(line, "README.md", [e])), 1)

    def test_changelog_and_the_register_are_never_read(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "CHANGELOG.md").write_text("both silks read 人", encoding="utf-8")
            (root / "data").mkdir()
            (root / "data" / "README.md").write_text("both silks read 人", encoding="utf-8")
            (root / "NOTES.md").write_text("both silks read 人", encoding="utf-8")
            self.assertEqual([c.path for c in cr.check([CH25], root)], ["NOTES.md"])


class Register(unittest.TestCase):

    def test_the_real_register_parses_and_every_see_resolves(self):
        entries = cr.load()
        self.assertTrue(entries)
        self.assertEqual(cr.broken_see(entries), [])

    def test_the_repository_carries_no_surviving_copy(self):
        self.assertEqual(cr.check(cr.load()), [])

    def test_a_shape_the_parser_cannot_read_is_an_error_not_an_empty_list(self):
        for bad in (
            '- id: x\n  retracted: 2026-08-20\n  claim: c\n  match: "not a list"\n'
            '  correction: c\n  see: s\n',
            '- id: x\n  retracted: yesterday\n  claim: c\n  match: ["a"]\n  correction: c\n  see: s\n',
            '- id: x\n  claim: c\n  match: ["a"]\n  correction: c\n  see: s\n',
            '- id: x\n  retracted: 2026-08-20\n  claim: c\n  match: ["a"]\n  correction: c\n'
            '  see: s\n- id: x\n  retracted: 2026-08-20\n  claim: c\n  match: ["a"]\n'
            '  correction: c\n  see: s\n',
        ):
            with self.assertRaises(ValueError):
                cr.parse(bad)

    def test_a_folded_claim_reads_as_one_sentence(self):
        e = cr.parse('- id: x\n  retracted: 2026-08-20\n  claim: >\n    first half\n'
                     '    second half\n  match: ["a", "b"]\n  correction: c\n  see: s\n')[0]
        self.assertEqual((e.claim, e.match), ("first half second half", ["a", "b"]))


if __name__ == "__main__":
    unittest.main()
