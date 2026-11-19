"""Source evidence travels through the database without losing its context."""

from dataclasses import replace
from pathlib import Path
import re
import sqlite3
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from build_db import build
from build_explorer import payload
from build_sources import render
from check_source_links import source_urls
from lib.corpus import load_chapters, load_variants, parse_frontmatter
from lib.source_registry import han, pairing, resolve
from lib.source_tables import published_chapters, published_citations, published_sources


class PublishedRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with sqlite3.connect(":memory:") as db:
            build(db)
            legacy = payload(db)
            cls.cards = {c["c"] for c in legacy["chars"]}
            cls.chapters = published_chapters(db, cls.cards, legacy["chapters"])
            cls.sources = published_sources(db)
            cls.citations = published_citations(db)
            cls.witness_ids = {ident for (ident,) in db.execute("SELECT id FROM witness")}
        cls.records = {r["id"]: r for r in cls.sources["records"]}

    def test_guodian_coverage_describes_which_passages_survive(self):
        self.assertEqual(list(self.chapters), list(range(1, 82)))
        self.assertEqual(self.chapters[5]["attestation"]["extent"], "middle")
        self.assertEqual(self.chapters[16]["attestation"]["extent"], "opening")
        self.assertEqual(self.chapters[64]["attestation"]["extent"], "split")
        self.assertEqual(self.chapters[1]["attestation"], {
            "source": "guodian", "present": False, "extent": None, "bundles": [], "units": [],
        })

    def test_print_status_belongs_to_the_reading(self):
        fork = next(f for f in self.chapters[3]["forks"]
                    if {r["source"] for r in f["readings"]} == {"heshanggong", "mawangdui-b"})
        readings = {r["source"]: r for r in fork["readings"]}
        self.assertEqual(readings["heshanggong"]["verification"], "unassessed")
        self.assertNotIn("confirm", readings["heshanggong"])
        self.assertEqual(readings["mawangdui-b"]["verification"], "pending-print")
        self.assertEqual(readings["mawangdui-b"]["confirm"], "T2-74")

    def test_wang_bi_identity_and_indirect_evidence(self):
        self.assertNotIn("siku-wangbi", self.records)
        self.assertEqual(self.records["yongle-dadian"]["chain"], ["wangbi"])
        self.assertTrue(any(f["our_call"] == "wangbi" for f in self.chapters[73]["forks"]))
        reading = next(r for f in self.chapters[62]["forks"] for r in f["readings"]
                       if r["source"] == "wangbi")
        self.assertIn("not the transmitted text", reading["annotation"])

    def test_dunhuang_reading_cites_its_collation(self):
        reading = next(r for f in self.chapters[62]["forks"] for r in f["readings"]
                       if r["source"] == "dunhuang")
        self.assertEqual(reading["chain"], ["zhu-qianzhi"])
        self.assertIn("Dunhuang Xin manuscript", reading["locator"])
        self.assertIn("url", reading)

    def test_chapter_11_dictionaries_reach_catalogue_and_link_check(self):
        fork = next(f for f in self.chapters[11]["forks"] if f["id"] == 74)
        ids = {"guangyun", "moe-character-variants", "moe-revised-mandarin"}
        self.assertEqual({ref["source"] for ref in fork["refs"]}, ids)
        guangyun = next(ref for ref in fork["refs"] if ref["source"] == "guangyun")
        self.assertEqual(guangyun["chain"], ["moe-character-variants"])
        self.assertTrue(ids.isdisjoint(self.witness_ids))
        page = render(resolve())
        for ident in ids:
            self.assertEqual(self.records[ident]["forks"], [74])
            self.assertEqual(self.records[ident]["chapters"], [11])
            section = page.split(f'<a name="{ident}"></a>', 1)[1].split('<a name="', 1)[0]
            self.assertIn("Chapter 11 evidence", section)
        urls = source_urls({"sources": self.sources, "chapter_sources": self.chapters, "entries": []})
        for ref in fork["refs"]:
            self.assertIn(ref["url"], urls)
        for ident in ids:
            self.assertIn(self.records[ident]["url"], urls)

    def test_base_editions_are_chronological_in_markdown_and_export(self):
        self.assertEqual([edition["year"] for edition in self.records["base"]["editions"]],
                         [1445, 1782, 1875, 1919])
        page = render(resolve())
        base = page.split('<a name="base"></a>', 1)[1].split('<a name="', 1)[0]
        self.assertEqual(re.findall(r" · (\d{4})\b", base), ["1445", "1782", "1875", "1919"])

    def test_inserting_and_moving_forks_preserves_ids_and_display_order(self):
        variants = load_variants()
        first, second = variants[:2]
        inserted = replace(first, id=max(v.id for v in variants) + 1)
        updated = [inserted, second, first, *variants[2:]]
        with patch("lib.source_registry.load_variants", return_value=updated), sqlite3.connect(":memory:") as db:
            build(db)
            chapter_data = published_chapters(db, self.cards, payload(db)["chapters"])
            self.assertEqual([fork["id"] for fork in chapter_data[first.chapter]["forks"][:3]],
                             [inserted.id, second.id, first.id])
            sources = published_sources(db)
            witness = next(r for r in sources["records"] if r["id"] in first.witnesses)
            self.assertTrue({first.id, inserted.id} <= set(witness["forks"]))

    def test_card_links_resolve_and_missing_cards_keep_their_pairing(self):
        missing = []
        for chapter in self.chapters.values():
            for fork in chapter["forks"]:
                for reading in fork["readings"]:
                    self.assertTrue(set(reading["cards"]) <= self.cards)
                    if any(han(c) and c not in self.cards for c in reading["text"]):
                        missing.append(reading)
        self.assertTrue(missing)
        self.assertTrue(all(r["pinyin"] and r["english"] for r in missing))

    def test_incomplete_glossary_keeps_passage_citations(self):
        self.assertEqual(len(self.citations), self.sources["totals"]["entries"])
        self.assertEqual(self.citations["ruo-\u5f31"]["refs_status"], "incomplete")
        refs = {r["source"]: r for r in self.citations["ruo-\u5f31"]["refs"]}
        self.assertTrue(all("locator" in r or "url" in r for r in refs.values()))
        self.assertEqual(refs["schuessler"]["chain"], ["wiktionary"])

    def test_generated_catalogue_spells_out_conditional_admission(self):
        page = render(resolve())
        self.assertIn("A qualifying transcription can be admitted", page)
        self.assertIn('name="guodian"', page)
        self.assertNotIn("siku-wangbi", page)


class RegistryValidation(unittest.TestCase):
    def test_supplementary_character_needs_its_own_gloss(self):
        # U+29840 is an old head graph, pronounced shǒu.
        with self.assertRaisesRegex(ValueError, "tone-marked pinyin"):
            pairing("\U00029840", "", "head", "fixture")
        self.assertEqual(pairing("\U00029840", "shǒu", "head", "fixture")["english"], "head")

    def test_source_table_literal_cannot_supply_a_missing_pairing(self):
        variants = load_variants()
        chapters = load_chapters()
        fork = variants[0]
        source_row = chapters[fork.chapter].source_rows[0]
        variants[0] = replace(fork, base=source_row.chinese, base_pinyin="", base_english="")
        with patch("lib.source_registry.load_variants", return_value=variants):
            with self.assertRaisesRegex(ValueError, "readable Roman-alphabet display text"):
                resolve(chapters=chapters)

    def test_pending_check_cannot_lose_its_worklist_reference(self):
        variants = load_variants()
        fork = next(v for v in variants if any(r.verification == "pending-print" for r in v.readings))
        fork.readings = [replace(r, confirm="") if r.verification == "pending-print" else r
                         for r in fork.readings]
        with patch("lib.source_registry.load_variants", return_value=variants):
            with self.assertRaisesRegex(ValueError, "relevant open row"):
                resolve()

    def test_confirmation_requires_actual_print_evidence(self):
        variants = load_variants()
        fork = variants[0]
        fork.readings = [replace(r, verification="confirmed-print") for r in fork.readings]
        with patch("lib.source_registry.load_variants", return_value=variants):
            with self.assertRaisesRegex(ValueError, "needs edition, locator, ISO date, and outcome"):
                resolve()

    def test_glossary_citation_shape_cannot_silently_drop_fields(self):
        for content in (
            'refs: []\n  - { source: guodian }',
            'refs:\n  - { source: guodian, source: wangbi }',
            'refs:\n  - { source: guodian, place: chapter }',
        ):
            with self.subTest(content=content), self.assertRaisesRegex(ValueError, "entry.md:3:"):
                parse_frontmatter(f"---\n{content}\n---\n", "entry.md")
