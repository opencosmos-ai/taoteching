#!/usr/bin/env python3
"""
The formula finder, against the blind spot it was written for.

Chapter 11 repeats 當其無 (dang qi wu — "right where its absence is") verbatim
three times and 有X之用 three times, and our English rendered every one of them
differently. Neither check_locks.py's `repeated-formula` rule nor
concordance.py --formulas could see it: both indexed segments into a SET of
chapter numbers, so three occurrences in one chapter collapsed to one entry and
were then filtered out as "not shared". Found by a human on 2026-09-05.
"""

import contextlib
import io
import sys
import unittest
from types import SimpleNamespace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import concordance as co  # noqa: E402
from lib import corpus  # noqa: E402


def chapters(**by_number):
    """chapters(c11=["三十輻共一轂，當其無，有車之用。", ...]) -> fake Chapters.

    Keyword names are "c" plus the chapter number, so the numbers stay ints —
    a str key here silently made the first draft of these tests pass against
    the wrong thing.
    """
    return {int(k.lstrip("c")): SimpleNamespace(
        number=int(k.lstrip("c")),
        drafted=True,
        verse=[],
        source_rows=[SimpleNamespace(chinese=line) for line in lines])
        for k, lines in by_number.items()}


class Segments(unittest.TestCase):
    def test_a_segment_repeating_inside_one_chapter_is_counted(self):
        """The 2026-09-05 blind spot, in miniature."""
        idx = co._segments(chapters(c11=[
            "三十輻共一轂，當其無，有車之用。",
            "埏埴以為器，當其無，有器之用。",
            "鑿戶牖以為室，當其無，有室之用。"]), 3)
        self.assertEqual(len(idx["當其無"]), 3)
        self.assertEqual({c for c, _ in idx["當其無"]}, {11})

    def test_occurrences_are_a_list_not_a_set_of_chapters(self):
        idx = co._segments(chapters(c7=["天長地久，天長地久。"]), 3)
        self.assertEqual(len(idx["天長地久"]), 2)

    def test_short_segments_are_below_the_floor(self):
        idx = co._segments(chapters(c1=["玄之，玄之。"]), 3)
        self.assertNotIn("玄之", idx)

    def test_punctuation_and_latin_are_stripped(self):
        idx = co._segments(chapters(c1=["道可道？非常道！"]), 3)
        self.assertIn("道可道", idx)
        self.assertIn("非常道", idx)


class Templates(unittest.TestCase):
    def frames(self, *lines, min_len=3):
        idx = co._segments(chapters(c1=list(lines)), min_len)
        return {co._render(n, f) for (n, f) in co._templates(idx, min_len)}

    def test_a_frame_with_one_slot_is_found(self):
        self.assertIn("有▢之用",
                      self.frames("有車之用。有器之用。有室之用。"))

    def test_two_slots_are_allowed(self):
        self.assertIn("▢得一以▢",
                      self.frames("天得一以清。地得一以寧。神得一以靈。"))

    def test_the_ch36_pair_is_found_as_two_frames(self):
        got = self.frames("將欲歙之，必固張之。將欲弱之，必固強之。")
        self.assertIn("將欲▢之", got)
        self.assertIn("必固▢之", got)

    def test_one_anchor_is_not_a_frame(self):
        """MIN_FIXED = 2. One fixed character is a character, not a frame —
        不▢▢ would otherwise collect half the book."""
        self.assertNotIn("居▢▢", self.frames("居善地。居惡淵。"))

    def test_less_than_half_fixed_is_not_a_frame(self):
        """是謂▢▢ is 2 of 4 and survives; a 2-of-6 frame does not."""
        got = self.frames("天下之至柔馳。天下之至堅騁。")
        self.assertTrue(all(f.count(co.SLOT) * 2 <= len(f) for f in got))

    def test_identical_segments_do_not_make_a_frame(self):
        self.assertEqual(self.frames("當其無。當其無。"), set())


class Embedded(unittest.TestCase):
    """T5-13: a repeat that does not start at a punctuation mark.

    為天下貞 sits inside 侯王得一以為天下貞, so the whole-segment index never
    saw it, ch 39 was missing from the 為天下▢ group, and a settled formula got
    a fourth rendering that way.
    """

    def index(self, **by_number):
        return co._formula_index(chapters(**by_number), 3)

    def test_an_exact_repeat_inside_a_longer_segment_is_counted(self):
        idx, _ = self.index(c22=["為天下式。"], c39=["侯王得一以為天下式。"])
        self.assertEqual(sorted(c for c, _ in idx["為天下式"]), [22, 39])

    def test_a_frame_member_inside_a_longer_segment_joins_the_frame(self):
        idx, templates = self.index(
            c28=["為天下谿。為天下谷。"], c39=["侯王得一以為天下貞。"])
        frames = {co._render(n, f): m for (n, f), m in templates.items()}
        self.assertIn("為天下貞", frames["為天下▢"])
        self.assertIn(39, {c for c, _ in idx["為天下貞"]})

    def test_three_characters_are_below_the_embed_floor(self):
        """天下之 is inside everything; EMBED_MIN keeps it from being found there."""
        idx, _ = self.index(c1=["天下之。"], c2=["天下之至柔。"])
        self.assertEqual(len(idx["天下之"]), 1)


class LiveCorpus(unittest.TestCase):
    """The finder against the real book, on the rows it exists to surface."""

    @classmethod
    def setUpClass(cls):
        cls.chapters = corpus.load_chapters()
        cls.index = co._segments(cls.chapters, 3)
        cls.frames = {co._render(n, f): sorted({c for m in members
                                                for c, _ in cls.index[m]})
                      for (n, f), members in co._templates(cls.index, 3).items()}

    def test_ch11_dang_qi_wu_repeats_three_times(self):
        self.assertEqual(len(self.index["當其無"]), 3)

    def test_ch36_and_ch39_open_worklist_rows_surface(self):
        self.assertEqual(self.frames.get("必固▢之"), [36])       # T3-4
        self.assertEqual(self.frames.get("▢得一以▢"), [39])      # T3-6

    def test_ch39_joins_the_wei_tianxia_frame(self):
        """T5-13 against the real book: 為天下貞 is inside 侯王得一以為天下貞."""
        index, templates = co._formula_index(self.chapters, 3)
        frames = {co._render(n, f): m for (n, f), m in templates.items()}
        self.assertIn("為天下貞", frames["為天下▢"])
        self.assertEqual(sorted({c for c, _ in index["為而不恃"]}), [10, 51, 77])

    def test_grammar_spans_many_chapters_and_is_demoted(self):
        self.assertGreater(len(self.frames.get("是謂▢▢", [])), 3)


class TheRecord(unittest.TestCase):
    """`--record` — the repository's own prior reasoning, before the dictionary.

    Built after 亂's entry rediscovered, from 說文, a finding that had been
    sitting in chapters/003.md's notes since 2026-08-31. The command exists so
    that is one keystroke instead of luck. See
    process/principles/search-the-record-first.md.
    """

    def record(self, term):
        """show_record prints; a test suite should not."""
        with contextlib.redirect_stdout(io.StringIO()):
            return co.show_record(term, quiet=True)

    def test_it_finds_a_finding_buried_in_another_chapters_notes(self):
        """The motivating case, asserted directly: 亂's argument lives in ch 3."""
        hits = self.record("亂")
        chapters = {h[1].name for h in hits if h[0] == "chapters"}
        self.assertIn("003.md", chapters,
                      "ch 3's notes hold 說文's 亂，治也 and the tangled-silk graph")

    def test_chapter_source_tables_are_not_searched(self):
        """Only the `## Notes` of a chapter — its source table prints the
        character on every line it occurs in, which would bury the findings
        under the evidence."""
        hits = self.record("道")
        for layer, path, n, line in hits:
            if layer == "chapters":
                text = path.read_text(encoding="utf-8")
                self.assertGreater(n, text[:text.find("## Notes")].count("\n"),
                                   f"{path.name}:{n} is above ## Notes")

    def test_generated_files_are_skipped(self):
        """INDEX.md and terms.yaml are build products; a hit there is a hit on
        the entry that generated it, counted twice."""
        hits = self.record("德")
        self.assertEqual([h for h in hits if h[1].name in ("INDEX.md", "terms.yaml")], [])

    def test_a_character_with_no_record_returns_nothing_and_does_not_fail(self):
        """A blank result is an answer, not an error — recall tools never fail."""
        self.assertEqual(self.record("鱷"), [])


def term(char, render, forbidden=(), flexions=()):
    return corpus.Term(term=char, pinyin="", render=render, forbidden=list(forbidden),
                       chapters=[], status="locked", entry=f"glossary/{char}.md",
                       flexions=list(flexions))


class EnglishAttribution(unittest.TestCase):
    """Which entry --english reports for an English word (WORKLIST T5-19).

    It used to take the first entry whose whole render string contained the
    word, prose included. 善's "good (only where the text names the category)"
    therefore claimed "only", and 唯, which renders it, could never be named.
    """

    def test_a_reason_in_parentheses_never_claims_a_word(self):
        terms = [term("善", "masterful · good (only where the text names the category)"),
                 term("唯", "only")]
        lock, rivals = co.lock_for_english("only", terms)
        self.assertEqual(lock.term, "唯")
        self.assertEqual(rivals, [])

    def test_a_word_only_a_parenthesis_holds_is_tied_to_nothing(self):
        lock, _ = co.lock_for_english("alone", [term("聖", "the sage · sagehood (聖 alone, ch 19)")])
        self.assertIsNone(lock)

    def test_an_exact_render_beats_an_earlier_substring(self):
        terms = [term("守", "hold to / guard"), term("持", "hold")]
        self.assertEqual(co.lock_for_english("hold", terms)[0].term, "持")

    def test_a_substring_still_finds_its_entry(self):
        lock, _ = co.lock_for_english("clear", [term("明", "clear-seeing / clarity")])
        self.assertEqual(lock.term, "明")

    def test_prose_outside_parentheses_does_not_outrank_an_earlier_entry(self):
        """強's render states a grammatical condition as prose, which is allowed."""
        terms = [term("萬物", "the countless things"),
                 term("強", "strong · forcing where it strains against a thing's nature")]
        lock, rivals = co.lock_for_english("thing", terms)
        self.assertEqual(lock.term, "萬物")
        self.assertEqual(rivals, [])

    def test_a_padded_forbidden_word_still_matches(self):
        """' king' is padded so the gate does not fire on 'making'."""
        terms = [term("事", "affairs · making"), term("王", "the king", forbidden=[" king"])]
        self.assertEqual(co.lock_for_english(" king", terms)[0].term, "王")

    def test_a_declared_flexion_is_found(self):
        t = term("唯", "only", flexions=[{"english": "yes", "chapters": [20], "why": ""}])
        self.assertEqual(co.lock_for_english("yes", [t])[0].term, "唯")

    def test_two_entries_holding_one_word_exactly_are_both_reported(self):
        terms = [term("身", "body", forbidden=["soul"]), term("魄", "aliveness", forbidden=["soul"])]
        lock, rivals = co.lock_for_english("soul", terms)
        self.assertEqual((lock.term, [r.term for r in rivals]), ("身", ["魄"]))
