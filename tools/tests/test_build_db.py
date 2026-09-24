"""Tests for the corpus builder.

Every case here is a bug that was actually shipped and caught during the build,
kept so it stays caught. The alignment and decomposition passes are the ones
worth guarding: both produced confidently wrong output that looked right.
"""

import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import build_db  # noqa: E402
import import_shuowen as sw  # noqa: E402


class PinyinAlignment(unittest.TestCase):
    def test_one_syllable_per_character(self):
        pairs, ok = build_db.align_pinyin("道可道，非常道；",
                                          "Dào kě dào, fēi cháng dào;")
        self.assertTrue(ok)
        self.assertEqual([c for c, _ in pairs], list("道可道非常道"))
        self.assertEqual([p for _, p in pairs],
                         ["Dào", "kě", "dào", "fēi", "cháng", "dào"])

    def test_mismatch_yields_no_guess(self):
        """A wrong syllable is worse than a missing one: it reads as settled."""
        pairs, ok = build_db.align_pinyin("道可道", "Dào kě")
        self.assertFalse(ok)
        self.assertTrue(all(p is None for _, p in pairs))

    def test_punctuation_is_not_a_character(self):
        pairs, _ = build_db.align_pinyin("大，小。", "dà, xiǎo.")
        self.assertEqual([c for c, _ in pairs], ["大", "小"])


class ApparatusGlosses(unittest.TestCase):
    """Glosses align inside their own line, never by a global pinyin lookup.

    Pinyin is not a key. An early build matched glosses to characters by sound
    across the whole book and rendered 其 (qí — its) as "tools" by way of 器
    (qì — vessel), and 下 (xià — below) as "flaws" by way of 瑕 (xiá — flaw).
    """

    def test_positional_within_the_line(self):
        pairs, _ = build_db.align_pinyin("企者不立", "Qǐ zhě bù lì")
        got = build_db.apparatus_glosses(
            pairs, r"Tiptoeing \[qi\] those \[zhe\] do not \[bu\] stand \[li\];")
        self.assertEqual(got[0], "Tiptoeing")
        self.assertEqual(got[1], "those")
        self.assertEqual(got[3], "stand")

    def test_a_bracket_matching_nothing_in_the_line_is_dropped(self):
        """Never guess. The gloss is only ever attached to a syllable the line
        actually has."""
        pairs, _ = build_db.align_pinyin("其", "qí")
        self.assertEqual(build_db.apparatus_glosses(pairs, r"vessel \[qì4\]"), {})

    def test_homophones_in_one_line_are_told_apart_by_position(self):
        """Tone-insensitive matching is safe only because brackets are consumed
        in reading order. 其 (qí — its) and 器 (qì — vessel) share a syllable once
        tones are stripped; order is what keeps them straight."""
        pairs, _ = build_db.align_pinyin("其器", "qí qì")
        got = build_db.apparatus_glosses(pairs, r"its \[qi\] vessel \[qi\]")
        self.assertEqual(got, {0: "its", 1: "vessel"})

    def test_multi_syllable_bracket_is_skipped(self):
        pairs, _ = build_db.align_pinyin("有道者", "yǒu dào zhě")
        got = build_db.apparatus_glosses(
            pairs, r"those possessing the Tao \[you dao zhe\]")
        self.assertEqual(got, {})


class ShuowenAnalysis(unittest.TestCase):
    """从X is a semantic part; X聲 is there for sound. Keeping them apart is the
    entire reason to prefer 說文 over a radical table."""

    def test_semantic_and_phonetic_are_separated(self):
        gloss, sem, phon, kind, head = sw.parse_analysis("蚚也。从虫弘聲。")
        self.assertEqual(gloss, "蚚也。")
        self.assertEqual(sem, ["虫"])
        self.assertEqual(phon, ["弘"])
        self.assertEqual(kind, "phonetic-compound")
        self.assertFalse(head)

    def test_two_semantic_parts_without_a_comma(self):
        _, sem, phon, _, _ = sw.parse_analysis("顛也。至高無上。从一大。")
        self.assertEqual(sem, ["一", "大"])
        self.assertEqual(phon, [])

    def test_grammar_words_are_not_components(self):
        """聲 ("phonetic") and 从 ("from") are the vocabulary of the analysis.
        A greedy match once made 聲 the most common component in the book."""
        _, sem, phon, _, _ = sw.parse_analysis("不多也。从小丿聲。")
        self.assertEqual(sem, ["小"])
        self.assertEqual(phon, ["丿"])
        self.assertNotIn("聲", sem + phon)

    def test_section_head_clause_is_not_a_component(self):
        """凡X之屬皆从X describes the class, not this character."""
        _, sem, _, _, head = sw.parse_analysis(
            "人心，土藏，在身之中。象形。凡心之屬皆从心。")
        self.assertTrue(head)
        self.assertEqual(sem, [])

    def test_abbreviated_component_marker_is_dropped(self):
        _, sem, phon, _, _ = sw.parse_analysis("刑也。从水，𢊁省聲。")
        self.assertIn("水", sem)
        self.assertNotIn("省", sem + phon)

    def test_moonlight_through_a_window(self):
        """CLAUDE.md's 明 lock argues the graph is moon plus window, not sun.
        說文 files it under 朙 and says exactly that."""
        _, sem, _, _, _ = sw.parse_analysis("照也。从月从囧。凡朙之屬皆从朙。")
        self.assertEqual(sem, ["月", "囧"])


class SectionSplitting(unittest.TestCase):
    def test_two_equals_header_is_matched(self):
        """`(?==={2}…)` is a lookahead for THREE equals — the quantifier binds to
        the second `=`. It silently left 卷二–卷十四 with no 部 at all."""
        text = "intro\n==小部==\n少：不多也。从小丿聲。\n"
        got = list(sw.parse_volume(text))
        self.assertEqual(len(got), 1)
        char, radical, definition, _ = got[0]
        self.assertEqual(char, "少")
        self.assertEqual(radical, "小")
        self.assertEqual(definition, "不多也。从小丿聲。")

    def test_table_transcription_is_also_parsed(self):
        """卷一 uses a different transcription from the rest of the work."""
        row = ("==一部==\n|-\n| {{+|'''天'''}} || {{yw|顛也。从一大。}}"
               "{{*|他前切。}} || {{+|一}}\n")
        got = list(sw.parse_volume(row))
        self.assertEqual(got[0][0], "天")
        self.assertEqual(sw.fanqie(got[0][3]), "他前切")


class Baseline(unittest.TestCase):
    """The corpus, end to end, against measured counts."""

    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(":memory:")
        cls.stats, cls.align = build_db.build(cls.conn)

    def q(self, sql):
        return self.conn.execute(sql).fetchone()[0]

    def test_counts(self):
        for table, (expected, note) in build_db.BASELINE.items():
            got = build_db.baseline_count(self.conn, table)
            self.assertEqual(got, expected, (
                f"\n\n  {table} moved: {expected} -> {got}\n"
                f"  what it counts: {note}\n"
                f"  If you meant this, update BASELINE in tools/build_db.py and\n"
                f"  extend that entry's note with the date and the cause. If you\n"
                f"  did not, something changed the corpus without meaning to —\n"
                f"  that is the finding, not the failure.\n"))

    def test_every_baseline_entry_states_what_it_counts(self):
        """The note is the cost of bumping a number, so it cannot be empty.

        A bare baseline invites the one response that destroys the check:
        raise it until the build is green. Same doctrine as `lock-ok`'s
        required reason and `shaloms-call`'s required `until:`.
        """
        for table, entry in build_db.BASELINE.items():
            self.assertIsInstance(entry, tuple, f"{table}: baseline must be (count, note)")
            count, note = entry
            self.assertIsInstance(count, int, f"{table}: count must be an int")
            self.assertGreater(len(note.strip()), 20,
                               f"{table}: the note must say what the number counts")

    def test_every_token_reassembles_into_its_line(self):
        self.assertEqual(self.q(
            "SELECT count(*) FROM token t JOIN line l"
            " ON l.chapter=t.chapter AND l.seq=t.line_seq"
            " WHERE instr(l.chinese, t.char)=0"), 0)

    def test_a_flexion_counts_as_honored_in_the_chapters_it_licenses(self):
        """The atlas must not print NOT FOUND on a line a flexion licenses.

        Ch 9 is the case: 保 reads bare *keep* there and 守 reads *guard*, both
        declared flexions, and both were reported as breaches while `render:`
        carried its flexions as prose no tool could read. 36 rows of the export
        were wrong this way.
        """
        for char in ("保", "守"):
            got = self.conn.execute(
                "SELECT honored FROM render WHERE chapter=9 AND char=?",
                (char,)).fetchone()[0]
            self.assertEqual(got, 1, f"{char} at ch 9 should be honored by its flexion")

    def test_a_flexion_does_not_leak_into_chapters_it_does_not_name(self):
        """執 → *seize* is licensed at ch 74 only. Ch 29 and 64 read *grasp*,
        the primary render, and must be judged against that."""
        self.assertEqual(
            self.q("SELECT count(*) FROM render WHERE char='執'"
                   " AND chapter IN (29, 64) AND expected LIKE '%seize%'"), 0)

    def test_rule_zero_every_token_has_pinyin(self):
        self.assertEqual(self.q("SELECT count(*) FROM token WHERE pinyin IS NULL"), 0)
        self.assertEqual(self.stats["pinyin_fail"], 0)

    def test_every_source_line_has_english_attached(self):
        """Alignment is total in both directions. Mapping verses onto lines alone
        left surplus lines bare, which cost 60 commentary lemmas their English."""
        self.assertEqual(self.q(
            "SELECT count(*) FROM line l WHERE NOT EXISTS"
            " (SELECT 1 FROM alignment a WHERE a.line_id = l.id)"), 0)

    def test_locked_characters_carry_their_render(self):
        self.assertEqual(self.q(
            "SELECT count(*) FROM character"
            " WHERE lock_status='locked' AND our_render IS NULL"), 0)

    def test_components_exclude_the_analysis_vocabulary(self):
        self.assertEqual(self.q(
            "SELECT count(*) FROM component WHERE component IN ('聲','从','省','亦')"), 0)

    def test_qiang_decomposes_as_the_glossary_argues(self):
        rows = dict(self.conn.execute(
            "SELECT role, component FROM component WHERE char='強'").fetchall())
        self.assertEqual(rows.get("semantic"), "虫")
        self.assertEqual(rows.get("phonetic"), "弘")


if __name__ == "__main__":
    unittest.main()
