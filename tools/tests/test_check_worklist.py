#!/usr/bin/env python3
"""
The worklist checker, against the drift it was written for.

Every fixture below is a real failure this repository shipped. A checker that
only ever passes is worth nothing, so each rule is proved against the state
that got past a human reader, and then against the corrected state.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_worklist as cw  # noqa: E402


HEAD = "| # | | Item | Ch | Pass |\n|---|---|---|---|---|\n"


def table(*rows):
    return HEAD + "".join(rows)


def row(rid, status, ch, pass_, item="x"):
    return f"| {rid} | {status} | {item} | {ch} | {pass_} |\n"


def rules(text):
    findings, _ = cw.check(text)
    return sorted(f.rule for f in findings)


class PassChapters(unittest.TestCase):
    """The failure of 2026-08-31: two hand-kept Pass D lists, both wrong."""

    def test_the_real_drift_is_caught(self):
        # PD listed 15, 26 and 30 — no D-tagged row named any of them — and
        # omitted 38, which T1-4 does name.
        t = table(
            row("PD", "⬜", "3 4 15 26 30", "D"),
            row("T1-2", "⬜", "4", "D"),
            row("T1-3", "⬜", "3", "D"),
            row("T1-4", "⬜", "38", "D"),
        )
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["pass-chapters"])
        detail = findings[0].detail
        self.assertIn("missing 38", detail)
        self.assertIn("15 26 30", detail)
        self.assertIn("3 4 38", findings[0].fix)

    def test_the_corrected_list_passes(self):
        t = table(
            row("PD", "⬜", "3 4 38", "D"),
            row("T1-3", "⬜", "3", "D"),
            row("T1-2", "⬜", "4", "D"),
            row("T1-4", "⬜", "38", "D"),
        )
        self.assertEqual(rules(t), [])

    def test_a_pointer_cell_is_not_a_list_and_is_never_checked(self):
        """PC says 'T3-1 · T2-9→15'. Declining to keep a list is the goal."""
        t = table(
            row("PC", "🔶", "T3-1 · T2-9→15", "C"),
            row("T2-9", "⬜", "45", "C"),
        )
        self.assertEqual(rules(t), [])

    def test_book_wide_and_dashes_are_not_lists(self):
        t = table(
            row("PE", "⬜", "book-wide", "E"),
            row("PG", "⬜", "—", "G"),
            row("T2-1", "⬜", "7 9 13", "E"),
            row("T5-7", "⬜", "—", "G"),
        )
        self.assertEqual(rules(t), [])

    def test_plus_n_more_does_not_leak_a_chapter_number(self):
        """'5 16 17 18 25 + 26 more' must not read 26 as a chapter."""
        self.assertEqual(cw._chapters("5 16 17 18 25 + 26 more"),
                         frozenset({5, 16, 17, 18, 25}))


class ClosedPass(unittest.TestCase):
    """The failure of 2026-08-31: PC marked done over three open C rows."""

    def test_a_pass_cannot_be_done_over_open_rows(self):
        t = table(
            row("PC", "✅", "T3-1", "C"),
            row("T2-9", "⬜", "45", "C"),
            row("T2-10", "⬜", "27 52", "C"),
            row("T2-11", "⬜", "16 32 44 52", "C"),
        )
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["closed-pass"])
        self.assertIn("3 row(s)", findings[0].detail)
        self.assertIn("T2-9", findings[0].detail)

    def test_part_done_rows_also_block_a_closed_pass(self):
        t = table(row("PC", "✅", "T3-1", "C"), row("T2-15", "🔶", "10 22", "C"))
        self.assertEqual(rules(t), ["closed-pass"])

    def test_deferred_rows_do_not_block(self):
        """⏸ is Shalom's call, not outstanding work."""
        t = table(row("PF", "✅", "—", "F"), row("T4-1", "⏸", "13", "F"))
        self.assertEqual(rules(t), [])

    def test_a_genuinely_finished_pass_passes(self):
        t = table(
            row("PB", "✅", "5 18", "B"),
            row("T1-9", "✅", "5", "B"),
            row("T2-2", "✅", "18", "B"),
        )
        self.assertEqual(rules(t), [])


class Tally(unittest.TestCase):
    def test_a_wrong_header_count_is_caught_and_the_fix_is_printed(self):
        t = ("**2 item rows: 2 open · 0 done · 0 part done · 0 deferred.**\n\n"
             + table(row("PD", "⬜", "—", "D"),
                     row("T1-1", "⬜", "10", "D"), row("T1-2", "✅", "4", "D")))
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["tally"])
        self.assertIn("1 open · 1 done", findings[0].fix)

    def test_a_right_header_count_passes(self):
        t = ("**2 item rows: 1 open · 1 done · 0 part done · 0 deferred.**\n\n"
             + table(row("PD", "⬜", "—", "D"),
                     row("T1-1", "⬜", "10", "D"), row("T1-2", "✅", "4", "D")))
        self.assertEqual(rules(t), [])


class ChapterTally(unittest.TestCase):
    """The drift of 2026-09-05: ch 35 closed, and the Progress line did not.

    Three copies of the same fact live in that one sentence — a figure, a list
    of chapter numbers, and a spelled-out repeat. Before this rule they were
    kept by hand, and the count in this file drifted four times.
    """

    PROG = ("**Progress: Pass D \U0001f536 \u2014 {n} of 2 chapters.** "
            "Done: **{lst}** \u2014 {word} of the two.\n\n")
    TBL = table(row("PD", "\U0001f536", "\u2014", "D"),
                row("D3", "\u2705", "3", "D"),
                row("D11", "\u2b1c", "11", "D"))

    def build(self, n="1", lst="3", word="one"):
        return self.PROG.format(n=n, lst=lst, word=word) + self.TBL

    def test_the_truth_passes(self):
        self.assertEqual(rules(self.build()), [])

    def test_a_stale_figure_is_caught(self):
        findings, _ = cw.check(self.build(n="2"))
        self.assertEqual([f.rule for f in findings], ["chapter-tally"])
        self.assertIn("1 of 2 chapters", findings[0].fix)

    def test_a_stale_done_list_is_caught_and_the_fix_is_printed(self):
        findings, _ = cw.check(self.build(lst="3 \u00b7 11"))
        self.assertEqual([f.rule for f in findings], ["chapter-tally"])
        self.assertIn("Done: **3**", findings[0].fix)

    def test_a_stale_spelled_repeat_is_caught(self):
        findings, _ = cw.check(self.build(word="two"))
        self.assertEqual([f.rule for f in findings], ["chapter-tally"])
        self.assertIn("two of the two", findings[0].detail)

    def test_all_three_drift_independently(self):
        findings, _ = cw.check(self.build(n="2", lst="3 \u00b7 11", word="two"))
        self.assertEqual([f.rule for f in findings],
                         ["chapter-tally"] * 3)

    def test_ordinary_prose_cannot_reach_the_spelled_test(self):
        """"none of the passes" is not two number words, so it is not a count."""
        t = (self.PROG.format(n="1", lst="3", word="one").rstrip("\n")
             + " None of the passes is free. Some of the work is done.\n\n"
             + self.TBL)
        self.assertEqual(rules(t), [])

    def test_a_removed_count_is_not_a_finding(self):
        """Deleting a hand-kept copy is a legitimate fix, and was the one used
        before this rule existed."""
        t = "**Progress: Pass D \U0001f536.**\n\n" + self.TBL
        self.assertEqual(rules(t), [])

    def test_no_progress_line_at_all_is_not_a_finding(self):
        self.assertEqual(rules(self.TBL), [])

    def test_word_to_int_reads_hyphenated_numbers_and_refuses_the_rest(self):
        self.assertEqual(cw.word_to_int("twenty-two"), 22)
        self.assertEqual(cw.word_to_int("nineteen"), 19)
        self.assertIsNone(cw.word_to_int("passes"))
        self.assertIsNone(cw.word_to_int("twenty-odd"))


class Structure(unittest.TestCase):
    def test_duplicate_ids(self):
        t = table(row("PD", "⬜", "—", "D"),
                  row("T1-1", "⬜", "10", "D"), row("T1-1", "⬜", "11", "D"))
        self.assertEqual(rules(t), ["duplicate-id"])

    def test_a_pass_letter_with_no_pass_row(self):
        t = table(row("T9-1", "⬜", "10", "Z"))
        self.assertEqual(rules(t), ["pass-exists"])

    def test_ongoing_is_a_licensed_non_pass(self):
        """T5-4 is tagged 'ongoing' deliberately — it never closes."""
        t = table(row("T5-4", "⬜", "—", "ongoing"))
        self.assertEqual(rules(t), [])

    def test_ledger_and_prose_tables_are_ignored(self):
        """Only rows whose first cell is a row id and second a status count."""
        t = table(row("PD", "⬜", "—", "D"), row("T1-1", "⬜", "10", "D")) + (
            "| 2026-08-30 | **T2-12** — 以此 | `notes/translation.md` |\n"
            "| **56–81** | 26 | **20** (77%) | 6 | 0 |\n")
        _, rows = cw.check(t)
        self.assertEqual([r.id for r in rows], ["PD", "T1-1"])


class ChapterRows(unittest.TestCase):
    """
    Pass D got one row per chapter on 2026-09-02, so chapters could be checked
    off one at a time. That put each chapter's status in two places — the
    finding rows and the chapter row — which is the exact shape of every drift
    this file already tests. These two rules make the chapter row derived.
    """

    def test_a_chapter_cannot_be_done_over_an_open_finding(self):
        t = table(
            row("PD", "🔶", "D3 → D16", "D"),
            row("T1-6", "⬜", "16", "D"),
            row("D16", "✅", "16", "D"),
        )
        self.assertIn("chapter-row", rules(t))

    def test_a_chapter_closes_when_its_findings_do(self):
        t = table(
            row("PD", "🔶", "D3 → D16", "D"),
            row("T1-6", "✅", "16", "D"),
            row("D16", "✅", "16", "D"),
        )
        self.assertNotIn("chapter-row", rules(t))

    def test_part_done_findings_also_block(self):
        t = table(
            row("PD", "🔶", "D29", "D"),
            row("T2-15", "🔶", "29", "D"),
            row("D29", "✅", "29", "D"),
        )
        self.assertIn("chapter-row", rules(t))

    def test_another_pass_does_not_block_a_chapter_row(self):
        # Ch 13 carries T1-10 in pass D and 身 (T2-1) in pass E. Only the
        # first is the ch 13 rewrite; a rule counting both could never close.
        t = table(
            row("PD", "🔶", "D13", "D"),
            row("PE", "⬜", "book-wide", "E"),
            row("T1-10", "✅", "13", "D"),
            row("T2-1", "⬜", "7 9 13 44 54", "E"),
            row("D13", "✅", "13", "D"),
        )
        self.assertEqual(rules(t), [])

    def test_a_chapter_with_no_findings_left_may_close(self):
        # Ch 64 is in Pass D only as the settled side of a formula pair.
        t = table(
            row("PD", "🔶", "D64", "D"),
            row("D64", "✅", "64", "D"),
        )
        self.assertEqual(rules(t), [])

    def test_a_finding_on_a_chapter_with_no_row_is_caught(self):
        t = table(
            row("PD", "🔶", "D36", "D"),
            row("T3-4", "⬜", "36 45", "D"),
            row("D36", "⬜", "36", "D"),
        )
        self.assertIn("chapter-cover", rules(t))

    def test_coverage_is_scoped_to_passes_that_have_chapter_rows(self):
        # Pass E has no chapter rows, so its chapters demand none.
        t = table(
            row("PD", "🔶", "D16", "D"),
            row("PE", "⬜", "book-wide", "E"),
            row("T1-6", "⬜", "16", "D"),
            row("T2-1", "⬜", "7 9 44 54", "E"),
            row("D16", "⬜", "16", "D"),
        )
        self.assertEqual(rules(t), [])


class SplitFiles(unittest.TestCase):
    """The failure of 2026-10-20: a file that said closed rows leave it, and
    96 of them had not."""

    def split(self, live, closed):
        return sorted(f.rule for f in cw.check_split(live, closed))

    def test_a_closed_row_left_in_the_worklist_is_caught(self):
        live = table(row("T2-19", "✅", "9 14 15", "E"),
                     row("T2-21", "⬜", "38 44", "E"))
        self.assertEqual(self.split(live, table()), ["closed-row"])

    def test_an_id_in_both_files_is_caught(self):
        # Not yet shipped: the one way the split itself can drift, a
        # reopened row copied back instead of moved.
        live = table(row("T2-14", "🔶", "12", "E"))
        closed = table(row("T2-14", "✅", "3 12 64", "C"))
        self.assertEqual(self.split(live, closed), ["archived-id"])

    def test_an_open_row_in_the_closed_file_is_caught(self):
        closed = table(row("T1-18", "⬜", "30", "E"))
        self.assertEqual(self.split(table(), closed), ["open-archived"])

    def test_the_split_done_right_passes(self):
        live = table(row("T2-21", "⬜", "38 44", "E"),
                     row("T4-2", "⏸", "37 45", "F"))
        closed = table(row("T2-19", "✅", "9 14 15", "E"))
        self.assertEqual(self.split(live, closed), [])


class LiveFile(unittest.TestCase):
    def test_the_real_worklist_is_consistent(self):
        findings, rows = cw.check(cw.WORKLIST.read_text(encoding="utf-8"))
        self.assertEqual(
            findings, [],
            "WORKLIST.md drifted: " + "; ".join(f.detail for f in findings))
        self.assertGreater(len(rows), 40, "the table failed to parse")

    def test_the_real_files_are_split(self):
        findings = cw.check_split(
            cw.WORKLIST.read_text(encoding="utf-8"),
            cw.CLOSED.read_text(encoding="utf-8"))
        self.assertEqual(
            findings, [],
            "WORKLIST.md and WORKLIST-CLOSED.md disagree: "
            + "; ".join(f.detail for f in findings))


if __name__ == "__main__":
    unittest.main()
