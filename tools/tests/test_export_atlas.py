"""Tests for the atlas export's reader keys.

The export is a contract with two readers: the Character Atlas, which refuses
any contract but 1, and the Library on opencosmos.ai, which builds a page per
chapter from `verse`, `notes`, `literal` and `align`. The case worth guarding
is the one the Library's ADR 0020 was written around: a proportional guess
must never look like a pairing. In chapter 6, 玄牝之門 (*xuán pìn zhī mén* —
"the gate of the dark female") is guessed onto "This is the dark female.",
when its English is the next line.
"""

import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import build_db  # noqa: E402
import export_atlas  # noqa: E402


class ReaderKeys(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(":memory:")
        build_db.build(cls.conn)
        cls.r = export_atlas.reader(cls.conn)

    def exact(self, n):
        """A chapter is exact when every one of its lines pairs at exact-count."""
        rows = [v for k, v in self.r["align"].items() if k.split(".")[0] == str(n)]
        return all(m == "exact-count" for row in rows for _, _, m in row)

    def test_contract_is_still_one(self):
        """The atlas exits on any other number; these keys are additions."""
        self.assertEqual(export_atlas.CONTRACT, 1)

    def test_every_chapter_has_verse_and_notes(self):
        self.assertEqual(sorted(map(int, self.r["verse"])), list(range(1, 82)))
        self.assertEqual(sorted(map(int, self.r["notes"])), list(range(1, 82)))

    def test_every_line_has_a_literal_and_an_alignment(self):
        self.assertEqual(len(self.r["literal"]), 798)
        self.assertEqual(set(self.r["align"]), set(self.r["literal"]))

    def test_alignment_points_inside_the_verse(self):
        for key, rows in self.r["align"].items():
            n = key.split(".")[0]
            count = sum(len(s) for s in self.r["verse"][n])
            for v, _, _ in rows:
                self.assertTrue(1 <= v <= count, key)

    def test_exact_means_the_counts_agree(self):
        """Exact where, and only where, English and Chinese have as many lines.

        Checked against the counts rather than a number: ADR 0020 was written
        saying 61 chapters were even, when the database had said 32 all along.
        """
        lines = {}
        for key in self.r["literal"]:
            n = key.split(".")[0]
            lines[n] = lines.get(n, 0) + 1
        for n in range(1, 82):
            verse = sum(len(s) for s in self.r["verse"][str(n)])
            self.assertEqual(self.exact(n), verse == lines[str(n)], f"ch {n}")

    def test_an_exact_chapter_pairs_line_for_line(self):
        self.assertTrue(self.exact(1))
        for key, rows in self.r["align"].items():
            ch, seq = key.split(".")
            if ch == "1":
                self.assertEqual(rows, [[int(seq), 1.0, "exact-count"]])

    def test_chapter_six_is_a_guess_and_says_so(self):
        self.assertFalse(self.exact(6))
        for v, conf, method in self.r["align"]["6.3"]:
            self.assertNotEqual(method, "exact-count")
            self.assertLess(conf, 1.0)

    def test_stanzas_are_kept(self):
        """Chapter 1 is written in more than one stanza; the blank lines between
        them are the only place the stanza breaks live."""
        self.assertGreater(len(self.r["verse"]["1"]), 1)
        flat = [l for s in self.r["verse"]["1"] for l in s]
        self.assertTrue(all(l == l.strip() for l in flat))

    def test_empty_notes_are_empty_not_missing(self):
        self.assertTrue(self.r["notes"]["1"])
        self.assertEqual(self.r["notes"]["6"], "")
        self.assertFalse(self.r["notes"]["1"].startswith("## "))

    def test_a_waiver_is_not_a_note(self):
        """A `lock-ok` comment excuses one finding for check_locks; a reader
        of the notes should never see it."""
        from lib.corpus import Chapter
        ch = Chapter(1, Path("001.md"), "drafted", [], [], [],
                     "Prose.\n\n<!-- lock-ok: forbidden · a reason -->\n\nMore.\n")
        conn = sqlite3.connect(":memory:")
        build_db.build(conn)
        self.assertEqual(export_atlas.reader(conn, {1: ch})["notes"]["1"],
                         "Prose.\n\nMore.")

    def test_relative_links_become_absolute(self):
        """Notes link to process/principles/ relative to chapters/; nothing that
        reads the export has the repository beside it."""
        md = ("See [imported-register](../process/principles/imported-register.md), "
              "[a note](../notes/translation.md#ch-1), [web](https://example.org) "
              "and [here](#top).")
        self.assertEqual(export_atlas.absolute_links(md), (
            "See [imported-register](https://github.com/opencosmos-ai/taoteching/blob/main/"
            "process/principles/imported-register.md), [a note](https://github.com/"
            "opencosmos-ai/taoteching/blob/main/notes/translation.md#ch-1), "
            "[web](https://example.org) and [here](#top)."))

    def test_no_note_links_back_into_the_repository(self):
        import re
        for n, md in self.r["notes"].items():
            for target in re.findall(r"\]\(([^)]+)\)", md):
                self.assertRegex(target, r"^(https?:|#)", f"ch {n}: {target}")


if __name__ == "__main__":
    unittest.main()
