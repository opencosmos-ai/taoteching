#!/usr/bin/env python3
"""
Tests for check_locks.py, built from the traps the 2026-08-10 sweep actually hit.

    python3 -m unittest discover tools/tests        # or: python3 -m pytest tools/tests

The point of this file is not coverage. It is that roughly a third of that
sweep's 93 flags were false positives, and a checker that cries wolf gets
switched off. So every case below is either a real error that must fire, or a
real false friend that must not — taken from WORKLIST.md's own record.

The false-friend cases are the important half. If one of them starts failing,
the checker has become noise.
"""

import pathlib
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import check_locks as C                                  # noqa: E402
from lib.corpus import Call, Chapter, SourceRow, Term, Waiver  # noqa: E402


def chapter(number, verse, chinese, status="drafted", notes=""):
    """A chapter with one source row, enough to exercise the evidence gate."""
    lines = verse if isinstance(verse, list) else [verse]
    return Chapter(
        number=number,
        path=Path(f"chapters/{number:03d}.md"),
        status=status,
        retrofit=[],
        verse=[(i + 10, t) for i, t in enumerate(lines)],
        source_rows=[SourceRow(chinese, "pinyin", "literal gloss", 1, 20)],
        notes=notes,
        waivers=[],
    )


def term(t, pinyin, render, forbidden):
    return Term(term=t, pinyin=pinyin, render=render, forbidden=forbidden,
                chapters=[], status="locked", entry=f"glossary/{pinyin}-{t}.md")


CHANG = term("常", "chang", "the ever-present", ["eternal", "everlasting"])
DE = term("德", "de", "integrity", ["virtue", "power"])
DAO = term("道", "dao", "the Tao", ["the Way", "the Path"])
WU_YOU = term("無 & 有", "wu-you", "absence / presence",
              ["Being", "Non-Being", "nothingness"])
PU = term("樸", "pu", "uncarved wood", ["uncarved block", "simplicity"])


def rendering_errors(chapters, terms):
    return [f for f in C.rule_forbidden_rendering(chapters=chapters, terms=terms)
            if f.severity == C.ERROR]


class ForbiddenRenderings(unittest.TestCase):
    """The locks, and the false friends that look like them."""

    def test_stem_match_catches_the_adverb(self):
        # WORKLIST.md lesson 1: \beternal\b misses "eternally", which is exactly
        # how two chapters hid from the sweep.
        found = rendering_errors([chapter(1, "The Tao is eternally so.", "常道")], [CHANG])
        self.assertEqual(len(found), 1)
        self.assertIn("eternal", found[0].message)

    def test_cháng_the_homophone_is_not_blamed(self):
        # 長 (cháng — long) is not 常 (cháng — constant). Ch 22's "therefore
        # endures" and Ch 7's 天長地久 were both wrongly flagged in the sweep.
        self.assertEqual(
            rendering_errors([chapter(22, "Therefore it endures.", "故長久")], [CHANG]), [])

    def test_evidence_gate_demotes_without_the_character(self):
        # "power" is forbidden for 德, but ch 33's "willpower" has no 德 in it.
        ch = chapter(33, "One who perseveres has willpower.", "強行者有志")
        all_found = C.rule_forbidden_rendering(chapters=[ch], terms=[DE])
        self.assertTrue(all_found)
        self.assertTrue(all(f.severity == C.INFO for f in all_found))
        self.assertIn("not in this chapter", all_found[0].message)

    def test_evidence_gate_promotes_with_the_character(self):
        found = rendering_errors([chapter(38, "The highest virtue is still.", "上德不德")], [DE])
        self.assertEqual(len(found), 1)

    def test_capitalized_forbidden_string_is_case_sensitive(self):
        # "the Way" is the violation; "the way of nature" is ordinary English.
        # A case-insensitive scan flagged both in ch 9 and ch 47.
        self.assertEqual(
            rendering_errors([chapter(9, "This is the way of nature.", "天之道")], [DAO]), [])
        self.assertEqual(
            len(rendering_errors([chapter(1, "Walking the Way of nature.", "道可道")], [DAO])), 1)

    def test_sentence_initial_capital_is_allowed(self):
        # "Being embodied and embracing the one" (ch 10) opens a line: the
        # capital is English orthography, not metaphysics.
        self.assertEqual(
            rendering_errors([chapter(10, "Being embodied, can you remain whole?", "有無")],
                             [WU_YOU]), [])

    def test_the_participle_is_not_the_noun(self):
        # "being still", "their being", "insists on being right" — six false
        # positives in the corpus, all cleared by case sensitivity.
        for line in ("Relinquishing desire, being still.",
                     "One who insists on being right is not prominent.",
                     "How could a ruler become ungrounded in their being?"):
            self.assertEqual(rendering_errors([chapter(2, line, "有無")], [WU_YOU]), [],
                             msg=line)

    def test_capital_noun_mid_sentence_still_fires(self):
        found = rendering_errors(
            [chapter(2, "It arises from Being and returns.", "有無相生")], [WU_YOU])
        self.assertEqual(len(found), 1)

    def test_blocking_the_openings_is_not_the_uncarved_block(self):
        # 塞其兌 ("block the openings", ch 52/56) vs 樸 ("uncarved wood").
        self.assertEqual(
            rendering_errors([chapter(52, "Block the openings, close the gate.", "塞其兌")],
                             [PU]), [])

    def test_nothingness_is_caught_where_wu_is_present(self):
        found = rendering_errors([chapter(14, "And returns to nothingness.", "無物")], [WU_YOU])
        self.assertEqual(len(found), 1)


class SagePronoun(unittest.TestCase):
    """Standing rule 1. Zero tolerance, no evidence gate."""

    def test_he_fires(self):
        found = C.rule_sage_pronoun(chapters=[chapter(2, "The sage does his work.", "聖人")])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)

    def test_they_is_clean(self):
        self.assertEqual(
            C.rule_sage_pronoun(chapters=[chapter(2, "The sage does their work.", "聖人")]), [])

    def test_the_word_is_not_a_substring(self):
        # "the" contains "he"; word boundaries matter for this rule even though
        # they must not be used for the forbidden-rendering stems.
        self.assertEqual(
            C.rule_sage_pronoun(chapters=[chapter(2, "The sage shelters them.", "聖人")]), [])


class DevotionalCapitalization(unittest.TestCase):
    """Standing rule 5: capitals confer status, and turn a word into a doctrine."""

    def test_the_great_way_in_chapter_53(self):
        # The live error this harness was built on. Note the phrase rule cannot
        # catch it — "the Way" is broken by the inserted "great" — which is why
        # this rule watches the bare word.
        found = [f for f in C.rule_devotional_capitalization(
            chapters=[chapter(53, "The great Way is very level.", "大道甚夷")])
            if f.severity == C.ERROR]
        self.assertEqual(len(found), 1)
        self.assertIn("Way", found[0].message)

    def test_lowercase_is_clean(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(53, "The great way is very level.", "大道甚夷")]), [])

    def test_line_initial_capital_is_allowed(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(25, "Nature follows the Tao.", "道法自然")]), [])

    def test_capital_after_a_full_stop_is_allowed(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(25, "It is so. Nature follows the Tao.", "道法自然")]), [])


class MechanisticRegister(unittest.TestCase):
    """CLAUDE.md's overlay watchlist: our own besetting temptation."""

    def test_source_code_fires(self):
        found = C.rule_mechanistic_register(
            chapters=[chapter(21, "The unerasable source code of all creation.", "眾甫")])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)


class StatusCoherence(unittest.TestCase):
    def test_drafted_but_empty(self):
        ch = chapter(61, C.UNTRANSLATED_MARKER, "大國者下流", status="drafted")
        found = [f for f in C.rule_status_coherence(chapters=[ch])
                 if "empty" in f.message]
        self.assertEqual(len(found), 1)

    def test_untranslated_but_written(self):
        ch = chapter(61, "The great state flows downward.", "大國者下流",
                     status="untranslated")
        found = [f for f in C.rule_status_coherence(chapters=[ch])
                 if "has verse" in f.message]
        self.assertEqual(len(found), 1)

    def test_drafted_and_written_is_clean(self):
        ch = chapter(61, "The great state flows downward.", "大國者下流")
        self.assertEqual(C.rule_status_coherence(chapters=[ch]), [])


class Waivers(unittest.TestCase):
    """Suppression is allowed, must carry a reason, and must not outlive its finding."""

    def test_waiver_marks_the_finding_waived(self):
        ch = chapter(22, "The sage does his work.", "聖人")
        ch.waivers = [Waiver("sage-pronoun", "quoting a critic · notes/translation.md", 40)]
        findings, _, _ = self._run(ch)
        pronoun = [f for f in findings if f.rule == "sage-pronoun"]
        self.assertEqual(len(pronoun), 1)
        self.assertIsNotNone(pronoun[0].waived_by)

    def test_unused_waiver_is_itself_an_error(self):
        ch = chapter(22, "The sage does their work.", "聖人")
        ch.waivers = [Waiver("sage-pronoun", "no longer needed", 40)]
        findings, _, _ = self._run(ch)
        stale = [f for f in findings if f.rule == "unused-waiver"]
        self.assertEqual(len(stale), 1)
        self.assertEqual(stale[0].severity, C.ERROR)

    def test_a_filtered_run_never_calls_a_waiver_dead(self):
        # A partial run cannot know: --rule leaves the consuming rule unrun, and
        # --chapter drops cross-chapter findings filed under another number.
        # Reporting a live waiver as dead would teach you to delete good waivers.
        ch = chapter(22, "The sage does their work.", "聖人")
        ch.waivers = [Waiver("repeated-formula", "deliberate, see notes", 40)]
        findings, _, _ = self._run(ch, rule_filter={"unused-waiver"})
        self.assertEqual([f for f in findings if f.rule == "unused-waiver"], [])

    def _run(self, ch, calls=(), rule_filter=None):
        """Exercise run()'s waiver and suppression logic against one chapter."""
        original_chapters, original_terms, original_calls = (
            C.load_chapters, C.load_terms, C.load_calls)
        C.load_chapters = lambda only=None: {ch.number: ch}
        C.load_terms = lambda: []
        C.load_calls = lambda: list(calls)
        try:
            return C.run(rule_filter=rule_filter)
        finally:
            C.load_chapters, C.load_terms, C.load_calls = (
                original_chapters, original_terms, original_calls)


class WaiverNames(unittest.TestCase):
    """A waiver may name a term three ways, because bare pinyin collides."""

    def test_three_names_per_term(self):
        self.assertEqual(C._waiver_names("glossary/chang-常.md", "常"),
                         {"chang", "chang-常", "常"})

    def test_the_xin_collision_is_disambiguable(self):
        # 心 (xīn, heart) and 信 (xìn, trust) both slug to "xin". The bare pinyin
        # is therefore ambiguous for this pair; the stem and character are not.
        heart = C._waiver_names("glossary/xin-心.md", "心")
        trust = C._waiver_names("glossary/xin-信.md", "信")
        self.assertEqual(heart & trust, {"xin"})
        self.assertIn("xin-心", heart)
        self.assertIn("xin-信", trust)
        self.assertNotIn("xin-信", heart)


class ShalomsCall(unittest.TestCase):
    """The override of record: suppresses by rule name, and never silently."""

    def test_repo_scope_suppresses(self):
        ch = chapter(22, "The sage does his work.", "聖人")
        call = Call("sage-pronoun", "CLAUDE.md", "repo", "standing", "testing", "2026-08-11")
        findings, suppressed, _ = Waivers._run(self, ch, calls=[call])
        self.assertEqual([f for f in findings if f.rule == "sage-pronoun"], [])
        self.assertIn("sage-pronoun", suppressed)

    def test_chapter_scope_is_narrow(self):
        call = Call("em-dash", "CLAUDE.md", "chapter: 44", "standing", "ch 44's are good",
                    "2026-08-11")
        self.assertTrue(call.covers(44))
        self.assertFalse(call.covers(14))

    def test_repo_scope_covers_everything(self):
        call = Call("em-dash", "CLAUDE.md", "repo", "standing", "why", "2026-08-11")
        self.assertTrue(call.covers(14))

    def test_retired_call_suppresses_nothing(self):
        call = Call("em-dash", "CLAUDE.md", "repo", "standing", "why", "2026-08-11",
                    retired=True)
        self.assertFalse(call.covers(14))

    def test_a_qualified_heading_still_parses(self):
        # "## DATE · rule (label)" and "## DATE · rule — retired" are both
        # legitimate; a regex that required the line to end at the rule id once
        # made a three-call ledger parse as one, silently.
        from lib.corpus import load_calls
        calls = load_calls()
        text = (pathlib.Path(__file__).resolve().parent.parent.parent
                / "process" / "shaloms-call.md").read_text()
        headings = re.findall(r"^## \d{4}-\d{2}-\d{2}\s*·", text, re.M)
        self.assertEqual(len(calls), len(headings),
                         "every dated heading in the ledger must parse to a call")

    def test_unparsed_headings_are_an_error(self):
        # The guard must fire when the counts disagree.
        found = C.rule_shaloms_call_unparsed(calls=[])
        self.assertTrue(found, "guard should fire when no calls parse")
        self.assertEqual(found[0].severity, C.ERROR)

    def test_expired_call_is_an_error(self):
        call = Call("no-new-tooling", "PLAN.md", "repo", "2020-01-01", "why", "2019-12-01")
        found = C.rule_stale_shaloms_call(calls=[call])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)

    def test_standing_call_never_expires(self):
        call = Call("shaloms-call", "here", "repo", "standing", "why", "2026-08-11")
        self.assertEqual(C.rule_stale_shaloms_call(calls=[call]), [])

    def test_future_expiry_is_fine(self):
        call = Call("no-new-tooling", "PLAN.md", "repo", "2099-01-01", "why", "2026-08-11")
        self.assertEqual(C.rule_stale_shaloms_call(calls=[call]), [])


class RepeatedFormula(unittest.TestCase):
    """Verbatim Chinese must produce verbatim English."""

    def _pair(self, en_a, en_b):
        rows = [SourceRow("物壯則老，", "wù zhuàng zé lǎo,",
                          "When things peak in strength, they decay,", 1, 20)]
        chs = []
        for n, en in ((30, en_a), (55, en_b)):
            c = chapter(n, en, "物壯則老，")
            c.source_rows = rows
            chs.append(c)
        return C.rule_repeated_formula(chapters=chs)

    def test_identical_renderings_do_not_warn(self):
        # The state ch 30 and ch 55 were left in after the 2026-08-10 fix.
        found = self._pair("When things reach their peak strength, they decay.",
                           "When things reach their peak strength, they decay.")
        self.assertTrue(all(f.severity == C.INFO for f in found))

    def test_divergent_renderings_warn(self):
        # The state they were in before it.
        found = self._pair("When things reach their peak strength, they decay.",
                           "Whatever grows strong will wither away.")
        self.assertTrue(any(f.severity == C.WARN for f in found))

    def test_grammar_is_not_a_formula(self):
        # 是以聖人 ("therefore the sage") opens 17 chapters. It is syntax, not a
        # formula, and reporting it would bury the four real findings.
        chs = []
        for n in range(1, 6):
            c = chapter(n, "Therefore the sage acts.", "是以聖人")
            c.source_rows = [SourceRow("是以聖人，", "shì yǐ shèng rén,",
                                       "Therefore the sage,", 1, 20)]
            chs.append(c)
        self.assertEqual(C.rule_repeated_formula(chapters=chs), [])


class SourceDrift(unittest.TestCase):
    def test_chapter_matching_base_text_is_clean(self):
        ch = chapter(1, "The Tao that can be spoken is not the Tao.", "道可道，非常道。")
        original = C.load_base_text
        C.load_base_text = lambda: {1: "道可道，非常道。\n"}
        try:
            self.assertEqual(C.rule_source_drift(chapters=[ch]), [])
        finally:
            C.load_base_text = original

    def test_drift_is_an_error(self):
        ch = chapter(1, "The Tao that can be spoken is not the Tao.", "道可道，非常道。")
        original = C.load_base_text
        C.load_base_text = lambda: {1: "道可道，非恆道。\n"}
        try:
            found = C.rule_source_drift(chapters=[ch])
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0].severity, C.ERROR)
        finally:
            C.load_base_text = original


class Variants(unittest.TestCase):
    """The apparatus, and the rule that keeps it honest."""

    def test_the_apparatus_parses(self):
        from lib.corpus import load_variants
        vs = load_variants()
        self.assertTrue(vs, "sources/variants.yaml parsed to nothing")
        for v in vs:
            self.assertTrue(v.chapter, "a variant has no chapter")
            self.assertTrue(v.base, f"ch {v.chapter} variant has no base reading")
            self.assertIn(v.our_call,
                          {"base", "punctuation", "undecided"} | set(v.witnesses),
                          f"ch {v.chapter}: our_call must be 'base', 'punctuation', "
                          f"'undecided', or one of its own witnesses")

    def test_chapter_filter(self):
        from lib.corpus import load_variants
        self.assertTrue(all(v.chapter == 25 for v in load_variants(25)))

    def test_every_meaning_bearing_fork_is_logged(self):
        # The whole point of the apparatus: a fork translated over without a
        # recorded decision is a build failure, not an accident.
        errors = [f for f in C.rule_unlogged_variant() if f.severity == C.ERROR]
        self.assertEqual(errors, [])

    def test_an_unlogged_fork_would_fire(self):
        from lib.corpus import Variant
        original = C.load_variants
        C.load_variants = lambda chapter=None: [Variant(
            chapter=63, line="夫輕諾必寡信", base="諾", witnesses={"mawangdui-a": "許"},
            meaning_bearing=True, our_call="base", note="", logged="")]
        try:
            found = C.rule_unlogged_variant()
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0].severity, C.ERROR)
        finally:
            C.load_variants = original


class CommentaryImport(unittest.TestCase):
    """The vendored commentary, and the fidelity of the import."""

    def setUp(self):
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
        import import_commentary
        self.imp = import_commentary
        root = pathlib.Path(__file__).resolve().parent.parent.parent
        self.dir = root / "sources" / "commentaries" / "wangbi"
        self.dirs = [root / "sources" / "commentaries" / s
                     for s in ("wangbi", "heshanggong")]

    def test_files_exist_with_provenance(self):
        files = sorted(self.dir.glob("*.md"))
        self.assertGreaterEqual(len(files), 71)
        from lib.corpus import parse_frontmatter
        for f in files:
            fm = parse_frontmatter(f.read_text(encoding="utf-8"))
            self.assertIsNotNone(fm, f"{f.name} has no frontmatter")
            for key in ("work", "author", "edition", "obtained", "rights"):
                self.assertIn(key, fm, f"{f.name} is missing {key}")

    def test_heshanggong_is_complete_with_his_own_titles(self):
        d = self.dirs[1]
        self.assertEqual(len(sorted(d.glob("*.md"))), 81, "Heshang Gong should be 81/81")
        from lib.corpus import parse_frontmatter
        fm = parse_frontmatter((d / "001.md").read_text(encoding="utf-8"))
        self.assertEqual(fm.get("chapter_title"), "體道")

    def test_every_divergent_lemma_carries_its_mark(self):
        """The header's `*` promise, enforced.

        The Han Feizi importer wrote every quotation as an exact lemma because
        _parse_essays never ran the fidelity check the other two importers run.
        35 divergences went unmarked, in the oldest witness to the text there is.
        """
        findings = C.rule_unmarked_lemma()
        errors = [f for f in findings if f.severity == C.ERROR]
        self.assertEqual(errors, [], "\n".join(f.message for f in errors))

    def test_unmarked_lemma_rule_actually_fires(self):
        """A rule that cannot fail is not a check.

        Folds the lemma through the same map the importer uses, so a printing
        variant never counts as a textual one.
        """
        from lib.corpus import fold, load_base_text
        base = {n: fold(t) for n, t in load_base_text().items()}
        hf = pathlib.Path(__file__).resolve().parents[2] / "sources/commentaries/hanfeizi"
        marked = [ln for p in sorted(hf.glob("[0-9]*.md"))
                  for ln in p.read_text(encoding="utf-8").split("\n")
                  if ln.startswith("**") and ln.rstrip().endswith("`*`")]
        self.assertTrue(marked, "no marked lemmas to test against")
        import re as _re
        for ln in marked:
            m = _re.match(r"^\*\*(.+?)\*\*\s*`\*`\s*$", ln)
            self.assertIsNotNone(m)
            probe = fold(m.group(1))
            self.assertFalse(any(probe in b for b in base.values()),
                             f"marked lemma actually agrees with the base text: {ln}")

    def test_no_wiki_markup_leaked(self):
        # {{SKchar|N}} nested inside a {{雙行註文|…}} annotation broke the outer
        # regex and leaked into the text as "{{SKchar3932".
        for d in self.dirs:
            for f in sorted(d.glob("*.md")):
                # Body only: {{PD-old}} legitimately appears in a frontmatter value.
                body = f.read_text(encoding="utf-8").split("---", 2)[-1]
                self.assertNotIn("{{", body, f"{d.name}/{f.name} has leaked markup")

    def test_no_punctuation_crept_in(self):
        # The whole rights position rests on this text being the authorial layer.
        for d in self.dirs:
          for f in sorted(d.glob("*.md")):
            body = f.read_text(encoding="utf-8").split("---", 2)[-1]
            body = re.sub(r"[*`>#\[\]()/.,:;'\"-]", "", body)
            for mark in "，。；、":
                self.assertNotIn(mark, body, f"{f.name} contains editorial punctuation")

    def test_orthographic_map_is_one_to_one_chars(self):
        for a, b in self.imp.ORTHOGRAPHIC.items():
            self.assertEqual(len(a), 1, f"{a!r} is not a single character")
            self.assertEqual(len(b), 1, f"{b!r} is not a single character")
            self.assertNotEqual(a, b)

    def test_extension_b_is_matched(self):
        # 𤣥 (U+24465), the Siku form of 玄, is outside the BMP. Omitting it from
        # the CJK class silently deleted it, turning 玄德 into 徳.
        self.assertEqual(self.imp.fold("𤣥德"), "玄德")

    def test_collation_notes_excluded_from_matching(self):
        # Folding a 〔...〕 note into the probe made the lemma it annotates fail
        # to match, misclassifying real variants as commentary.
        self.assertEqual(self.imp.fold("揣而梲之〔案某本作銳〕"), "揣而梲之")


class TheCorpusItself(unittest.TestCase):
    """Guards on the live manuscript, not on synthetic fixtures."""

    def test_no_male_pronouns_anywhere(self):
        # This lock has held from the first chapter. Keep it that way.
        chapters = [c for c in C.load_chapters().values() if c.drafted]
        self.assertEqual(C.rule_sage_pronoun(chapters=chapters), [])

    def test_no_virtue_anywhere(self):
        # 德 → integrity has also held from the beginning.
        chapters = [c for c in C.load_chapters().values() if c.drafted]
        de = [t for t in C.load_terms() if t.term == "德"]
        self.assertTrue(de, "the 德 lock is missing from terms.yaml")
        self.assertEqual(rendering_errors(chapters, de), [])

    def test_every_chapter_parses(self):
        chapters = C.load_chapters()
        self.assertEqual(len(chapters), 81)
        for n, c in chapters.items():
            self.assertTrue(c.source_rows, f"chapter {n} has no source rows")
            self.assertEqual(c.number, n)

    def test_base_text_has_not_drifted(self):
        chapters = list(C.load_chapters().values())
        self.assertEqual(C.rule_source_drift(chapters=chapters), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)


class FlexionChapter(unittest.TestCase):
    """A flexion is a lock saying "this other English, but only here."

    The "only here" is the whole reason flexions are data rather than a
    sentence inside `render:`, so it has to be checkable. These are the three
    ways it can be wrong, and the one way it must not be checked.
    """

    def _term(self, flexions, chapters=(9,), forbidden=()):
        return Term(term="保", pinyin="bao", render="keep safe",
                    forbidden=list(forbidden), chapters=list(chapters),
                    status="locked", entry="glossary/bao-保.md",
                    flexions=flexions)

    def run_rule(self, t, chapter_numbers=(9, 44)):
        chs = [chapter(n, "a line", "保") for n in chapter_numbers]
        return C.rule_flexion_chapter(chapters=chs, terms=[t])

    def test_licensed_chapter_the_character_is_in_is_clean(self):
        t = self._term([{"english": "keep", "chapters": [9], "why": "x"}])
        self.assertEqual(self.run_rule(t), [])

    def test_licensed_chapter_the_character_is_absent_from_fires(self):
        """The ch 9 flexion pointed at ch 44, where 保 does not stand."""
        t = self._term([{"english": "keep", "chapters": [44], "why": "x"}])
        found = self.run_rule(t)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].chapter, 44)
        self.assertIn("not in that chapter", found[0].message)

    def test_flexion_with_no_chapters_fires(self):
        """A flexion scoped to nowhere is just a second render, unpoliced."""
        t = self._term([{"english": "keep", "chapters": [], "why": "x"}])
        self.assertEqual(len(self.run_rule(t)), 1)

    def test_flexion_that_is_also_forbidden_fires(self):
        """The build and the entry must not contradict each other."""
        t = self._term([{"english": "keep", "chapters": [9], "why": "x"}],
                       forbidden=["keep"])
        found = self.run_rule(t)
        self.assertEqual(len(found), 1)
        self.assertIn("contradicts itself", found[0].message)

    def test_a_chapter_outside_the_corpus_is_not_judged(self):
        """The rule compares against chapters that were actually loaded, so a
        --staged run over one file cannot invent findings about the rest."""
        t = self._term([{"english": "keep", "chapters": [62], "why": "x"}])
        self.assertEqual(self.run_rule(t, chapter_numbers=(9,)), [])

    def test_the_english_outside_its_chapters_is_deliberately_not_checked(self):
        """The trap this rule refuses to walk into.

        保's own *keep safe* reads "keep the Tao safe" (15) and "keeps safe
        those who are not" (62), so scanning for the bare flexion string finds
        legitimate lines everywhere. T5-1 was declined at ~90% false positives
        for exactly this; check_locks.py must never cry wolf.
        """
        t = self._term([{"english": "keep", "chapters": [9], "why": "x"}])
        chs = [chapter(9, "it will not keep for long", "保"),
               chapter(15, "Those who keep the Tao safe", "保")]
        self.assertEqual(C.rule_flexion_chapter(chapters=chs, terms=[t]), [])


class FlexionsAreData(unittest.TestCase):
    """The parser and the Term model, which the rule and --english both rest on."""

    def test_licenses_is_true_for_the_primary_render_everywhere(self):
        t = Term(term="保", pinyin="bao", render="keep safe", forbidden=[],
                 chapters=[9, 15], status="locked", entry="e",
                 flexions=[{"english": "keep", "chapters": [9], "why": ""}])
        self.assertTrue(t.licenses("keep safe", 15))
        self.assertTrue(t.licenses("anything unrelated", 62))

    def test_licenses_is_false_for_a_flexion_outside_its_chapters(self):
        t = Term(term="保", pinyin="bao", render="keep safe", forbidden=[],
                 chapters=[9, 15], status="locked", entry="e",
                 flexions=[{"english": "keep", "chapters": [9], "why": ""}])
        self.assertTrue(t.licenses("keep", 9))
        self.assertFalse(t.licenses("keep", 15))

    def test_frontmatter_reads_flexions_and_covers_side_by_side(self):
        from lib.corpus import parse_frontmatter
        fm = parse_frontmatter(
            '---\n'
            'term: "保"\n'
            'render: "keep safe"\n'
            'flexions:\n'
            '  - { english: "keep", chapters: [9], why: "not cherished" }\n'
            'covers:\n'
            '  - { char: "寶", render: "treasure" }\n'
            'status: locked\n'
            '---\n'
        )
        self.assertEqual(fm["flexions"],
                         [{"english": "keep", "chapters": [9], "why": "not cherished"}])
        self.assertEqual(fm["covers"], [("寶", "treasure")])
        self.assertEqual(fm["status"], "locked")

    def test_an_entry_with_no_flexions_gets_an_empty_list(self):
        from lib.corpus import parse_frontmatter
        fm = parse_frontmatter('---\nterm: "德"\nrender: "integrity"\n---\n')
        self.assertEqual(fm["flexions"], [])
