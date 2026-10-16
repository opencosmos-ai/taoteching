#!/usr/bin/env python3
"""
The counts checker, against the drift it was written for.

The fixtures are the real sentences the 2026-10-15 audit found wrong, marked as
they would have been. A checker that only ever passes is worth nothing, so each
is proved against the stale figure and then against the true one.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_counts as cc  # noqa: E402


def check(text, **values):
    """Findings for a text, every count answered from `values` instead of the
    real sources — so a fixture never needs the database."""
    real = cc.value
    cc.value = lambda _sources, name: values.get(name)
    try:
        return cc.check(cc.marks_in(text), sources=None)
    finally:
        cc.value = real


class Marks(unittest.TestCase):

    def test_the_mark_and_its_number(self):
        m = cc.marks_in("the analysis of <!-- count: shuowen -->763 of the book's "
                        "<!-- count: characters -->798 characters")
        self.assertEqual([(x.name, x.claimed) for x in m],
                         [("shuowen", 763), ("characters", 798)])

    def test_emphasis_between_mark_and_number(self):
        m = cc.marks_in("<!-- count: gloss:word -->**462** characters")
        self.assertEqual((m[0].name, m[0].claimed), ("gloss:word", 462))

    def test_a_thousands_separator_is_read(self):
        m = cc.marks_in("<!-- count: comment-blocks:heshanggong -->1,052 blocks")
        self.assertEqual(m[0].claimed, 1052)

    def test_line_numbers_are_the_files(self):
        m = cc.marks_in("one\ntwo\nthree <!-- count: variants -->92", "README.md")
        self.assertEqual((m[0].path, m[0].line), ("README.md", 3))

    def test_a_fenced_example_is_not_a_claim(self):
        """ARCHITECTURE.md shows the syntax in a code block; that is not a count."""
        text = ("```markdown\n<!-- count: shuowen -->1\n```\n"
                "<!-- count: shuowen -->763\n")
        self.assertEqual([x.claimed for x in cc.marks_in(text)], [763])

    def test_an_inline_code_example_is_not_a_claim(self):
        text = "marked like `<!-- count: shuowen -->1`, which renders as nothing"
        self.assertEqual(cc.marks_in(text), [])

    def test_an_unmarked_number_is_never_read(self):
        """Marking is opt-in. A dated figure in a changelog is not a claim."""
        self.assertEqual(cc.marks_in("On 2026-08-26, 81 of 81 chapters."), [])


class TheRealDrift(unittest.TestCase):
    """README.md, CONTRIBUTING.md and ARCHITECTURE.md as the audit found them."""

    def test_the_stale_figure_fails_and_names_the_true_one(self):
        f = check("**<!-- count: shuowen-missing -->87 characters have no 說文 entry**",
                  **{"shuowen-missing": 35})
        self.assertEqual([x.rule for x in f], ["stale-count"])
        self.assertIn("says 87", f[0].detail)
        self.assertIn("35", f[0].fix)

    def test_the_true_figure_passes(self):
        self.assertEqual(
            check("**<!-- count: shuowen-missing -->35 characters have no 說文 entry**",
                  **{"shuowen-missing": 35}), [])

    def test_every_mark_on_a_line_is_checked(self):
        f = check("<!-- count: gloss:apparatus -->218 of the book's "
                  "<!-- count: characters -->798 characters",
                  **{"gloss:apparatus": 216, "characters": 798})
        self.assertEqual([(x.rule, x.detail) for x in f],
                         [("stale-count", "says 218; gloss:apparatus is 216")])


class BrokenMarks(unittest.TestCase):

    def test_a_name_nothing_computes_is_a_finding(self):
        """A typo in a name must not pass silently as 'nothing to check'."""
        f = check("<!-- count: shuowne -->763")
        self.assertEqual([x.rule for x in f], ["unknown-count"])

    def test_a_mark_with_no_number_is_a_finding(self):
        """'thirteen rules' was the third copy that disagreed. Digits only."""
        f = check("<!-- count: characters -->seven hundred", characters=798)
        self.assertEqual([x.rule for x in f], ["no-number"])
        self.assertIn("-->798", f[0].fix)


class Names(unittest.TestCase):
    """The names resolve, and the arguments are checked, without the database."""

    def test_an_argument_where_none_is_taken_is_unknown(self):
        self.assertIsNone(cc.value(cc.Sources(), "characters:extra"))

    def test_a_missing_argument_is_unknown(self):
        self.assertIsNone(cc.value(cc.Sources(), "lemmas"))

    def test_an_unknown_commentary_is_unknown(self):
        self.assertIsNone(cc.value(cc.Sources(), "lemmas:fuyi"))

    def test_lemmas_split_into_exact_and_marked(self):
        s = cc.Sources()
        exact, marked = s.lemmas("hanfeizi")
        self.assertEqual(cc.value(s, "lemmas:hanfeizi"), exact + marked)
        self.assertEqual(cc.value(s, "lemmas-variant:hanfeizi"), marked)


class AgainstTheRepository(unittest.TestCase):
    """The real sources, built once: the counts agree with each other and with
    the tools that own the facts they summarise."""

    @classmethod
    def setUpClass(cls):
        cls.s = cc.Sources()

    def test_shuowen_coverage_adds_up(self):
        v = lambda n: cc.value(self.s, n)  # noqa: E731
        self.assertEqual(v("shuowen") + v("shuowen-missing"), v("characters"))

    def test_variants_match_the_build_baseline(self):
        """BASELINE in build_db.py counts the same thing; they cannot differ."""
        import build_db
        self.assertEqual(cc.value(self.s, "variants"), build_db.BASELINE["variant"][0])

    def test_dash_chapters_is_the_em_dash_inventory(self):
        import check_locks
        from lib.corpus import load_chapters
        found = check_locks.rule_em_dash(list(load_chapters().values()))
        self.assertEqual(cc.value(self.s, "dash-chapters"),
                         len({f.chapter for f in found}))

    def test_every_count_computes(self):
        for name in cc.COUNTS:
            if name in cc.TAKES_ARG:
                continue
            self.assertIsInstance(cc.value(self.s, name), int, name)


if __name__ == "__main__":
    unittest.main()
