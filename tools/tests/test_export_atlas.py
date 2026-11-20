"""Tests for the atlas export's reader keys.

The export is a contract with two readers: the Character Atlas, which refuses
any contract but 1, and the Library on opencosmos.ai, which builds a page per
chapter from `verse`, `notes`, `literal` and `align`. The case worth guarding
is the one the Library's ADR 0020 was written around: a guess must never look
like a pairing. In chapter 6, 玄牝之門 (*xuán pìn zhī mén* — "the gate of the
dark female") was guessed onto "This is the dark female.", when its English is
the next line. Since 2026-10-24 there is no guess: every pairing is certain.
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

    def test_an_authored_chapter_pairs_as_written(self):
        """Ch 25's first English line renders two Chinese lines, which is why
        its counts differ and why the pairing has to be written by hand."""
        self.assertEqual(self.r["align"]["25.1"], [[1, 1.0, "authored"]])
        self.assertEqual(self.r["align"]["25.2"], [[1, 1.0, "authored"]])
        # 17 since 2026-11-19, when 獨立而不改 took its own English line
        self.assertEqual(self.r["align"]["25.19"], [[17, 1.0, "authored"]])

    def test_chapter_six_pairs_its_gate_correctly(self):
        """The guess paired the gate of the dark female with "This is the dark
        female." Its English is the next line. Since 2026-10-24 each Chinese
        line has an English line of its own, so the counts agree and say so."""
        self.assertEqual(self.r["align"]["6.3"], [[3, 1.0, "exact-count"]])
        self.assertEqual(self.r["align"]["6.4"], [[4, 1.0, "exact-count"]])

    def test_every_pairing_is_certain(self):
        """No chapter falls back to a guess (WORKLIST T5-23)."""
        for key, rows in self.r["align"].items():
            for _, conf, method in rows:
                self.assertIn(method, ("exact-count", "authored"), key)
                self.assertEqual(conf, 1.0, key)

    def test_stanzas_are_kept(self):
        """Chapter 1 is written in more than one stanza; the blank lines between
        them are the only place the stanza breaks live."""
        self.assertGreater(len(self.r["verse"]["1"]), 1)
        flat = [l for s in self.r["verse"]["1"] for l in s]
        self.assertTrue(all(l == l.strip() for l in flat))

    def test_empty_notes_are_empty_not_missing(self):
        self.assertTrue(self.r["notes"]["1"])
        # A chapter with no notes yet. This was ch 7 until its first note
        # (2026-11-19); pick another empty one if ch 40 gains notes.
        self.assertEqual(self.r["notes"]["40"], "")
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

    def test_shuowen_pronunciation_belongs_to_its_dictionary_sense(self):
        from build_explorer import payload

        cards = payload(self.conn)["chars"]
        # 埏 (shān — knead clay in chapter 11, yán — the far reaches in Shuowen).
        card = next(card for card in cards if card["c"] == "\u57cf")
        self.assertEqual(card["p"].lower(), "shān")
        self.assertEqual(export_atlas.shuowen_readings(cards)[card["c"]],
                         {"pinyin": "yán", "english": "The far reaches of the earth."})

    def test_shuowen_reuses_english_without_shipping_raw_prose_for_display(self):
        from build_explorer import payload
        from lib.source_registry import han

        cards = payload(self.conn)["chars"]
        readings = export_atlas.shuowen_readings(cards)
        # 和 (hé — harmony); its hand-translated definition includes graph analysis.
        self.assertEqual(readings["\u548c"], {"english": "To answer one another."})
        self.assertTrue(all(not han(reading["english"]) for reading in readings.values()))
        # 一 (yī — one) has a stored definition awaiting an authored English gloss.
        self.assertNotIn("\u4e00", readings)


if __name__ == "__main__":
    unittest.main()


class CardEnglish(unittest.TestCase):
    """A character's English as a reader sees it: senses separated by " · ",
    no chapter numbers, compounds and grammar notes kept."""

    def test_senses_take_the_middot(self):
        self.assertEqual(export_atlas.card_english("few / sparse / the inaudible (14)"),
                         "few · sparse · the inaudible")

    def test_chapter_numbers_go_and_the_rest_of_a_note_stays(self):
        c = export_atlas.card_english
        self.assertEqual(c("would (29, 36)"), "would")
        self.assertEqual(c("sagehood (聖 alone, ch 19)"), "sagehood (聖 alone)")
        self.assertEqual(c("preside over (司殺者, 74)"), "preside over (司殺者)")
        self.assertEqual(c("can be (可 + verb) / cannot (不可)"), "can be (可 + verb) · cannot (不可)")
        self.assertEqual(c("(closes a question) / (an exclamation)"),
                         "(closes a question) · (an exclamation)")

    def test_slashes_without_spaces_and_capitals_from_the_tables(self):
        c = export_atlas.card_english
        self.assertEqual(c("System/Administrator"), "system · administrator")
        self.assertEqual(c("the Tao / way"), "the Tao · way")


class EntryCard(unittest.TestCase):
    def test_a_card_field_is_shown_as_written(self):
        e = {"card": "the people", "render": "the people", "flexions": [{"english": "people"}]}
        self.assertEqual(export_atlas.entry_card(e), "the people")

    def test_without_one_the_ruling_is_followed_by_its_flexions(self):
        e = {"card": "", "render": "strain", "flexions": [{"english": "labor"}]}
        self.assertEqual(export_atlas.entry_card(e), "strain · labor")


class SideForms(unittest.TestCase):
    """`forms` tells the atlas how a part is written, and in which characters.
    沖's card said "built from 水" and a reader could not find water in 沖; then
    it said "written 氵 at the left, 氺 at the bottom", and 沖 has no 氺
    (2026-11-15). A row is shown only on the cards of its own characters."""

    @classmethod
    def setUpClass(cls):
        conn = sqlite3.connect(":memory:")
        build_db.build(conn)
        from build_explorer import payload
        data = payload(conn)
        conn.close()
        cls.built = {}
        for c in data["chars"]:
            for p in c["sem"] + c["pho"]:
                cls.built.setdefault(p, set()).add(c["c"])
        cls.f = export_atlas.forms(cls.built)

    def rows_for(self, part, char):
        return [r[:2] for r in self.f.get(part, []) if char in r[2]]

    def test_chong_is_water_at_the_left_and_nothing_else(self):
        self.assertEqual(self.rows_for("水", "沖"), [["氵", "at the left"]])

    def test_tai_is_water_at_the_bottom(self):
        self.assertEqual(self.rows_for("水", "泰"), [["氺", "at the bottom"]])

    def test_a_character_writing_the_part_otherwise_gets_no_line(self):
        self.assertEqual(self.rows_for("水", "益"), [])
        self.assertEqual(self.rows_for("心", "志"), [])

    def test_every_listed_character_is_built_from_its_part(self):
        for part, rows in self.f.items():
            for _, _, chars in rows:
                self.assertTrue(set(chars) <= self.built[part], (part, chars))

    def test_a_stray_character_fails(self):
        built = {k: set(v) for k, v in self.built.items()}
        built["水"].discard("沖")
        with self.assertRaises(SystemExit):
            export_atlas.forms(built)

    def test_every_form_is_in_a_block_the_atlas_typesets(self):
        """The common fonts set the main CJK block; the atlas's rare-glyph font
        carries the Radicals Supplement (⺮, ⻊) since 2026-11-15. A form from
        any other block could show as an empty box, so it has to wait for
        that font (chinese-atlas: atlas/fonts.py)."""
        for rows in self.f.values():
            for form, _, _ in rows:
                o = ord(form)
                self.assertTrue(0x4E00 <= o <= 0x9FFF or 0x2E80 <= o <= 0x2EFF, form)

    def test_bamboo_and_foot(self):
        self.assertEqual(self.rows_for("竹", "策"), [["⺮", "on top"]])
        self.assertEqual(self.rows_for("足", "跨"), [["⻊", "at the left"]])
