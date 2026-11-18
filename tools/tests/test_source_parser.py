"""The apparatus parser preserves quoted witness evidence."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib import corpus
from lib.flat_yaml import inline_map


class SourceParserTests(unittest.TestCase):
    def test_readings_lost_at_the_review_checkpoint(self):
        fixture = Path(__file__).parent / "fixtures" / "variant-quoted-commas.json"
        records = json.loads(fixture.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "variants.yaml"
            path.write_text("\n".join(
                f"- chapter: {record['chapter']}\n  line: example\n  base: example\n"
                f"  witnesses: {record['raw']}\n  meaning_bearing: false\n"
                "  our_call: base\n  note: >\n    First line\n    second line\n"
                "  logged: false\n" for record in records), encoding="utf-8")
            with patch.object(corpus, "VARIANTS", path):
                parsed = corpus.load_variants()
        self.assertEqual([v.witnesses for v in parsed], [r["readings"] for r in records])
        self.assertTrue(all(v.note == "First line second line" for v in parsed))

    def test_embedded_punctuation(self):
        self.assertEqual(inline_map(
            r'''{title: "The editor's note: \"a, b\"", locator: 'part 2, p. 4'}''',
            "test:1"), {"title": 'The editor\'s note: "a, b"', "locator": "part 2, p. 4"})

    def test_ambiguous_or_lossy_input_fails(self):
        for raw in ('{a: "x, b: "y"}', '{a: "x", a: "y"}', '{a: [x]}',
                    '{a: "x"} # comment', '{a: "x" garbage}', '{a: "x",}',
                    '{a: "x", missing-colon}'):
            with self.subTest(raw=raw), self.assertRaisesRegex(ValueError, r"test:1:"):
                inline_map(raw, "test:1")
