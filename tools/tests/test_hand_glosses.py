"""Tests for the two hand-kept gloss lists: sources/grammar-glosses.yaml and
sources/word-glosses.yaml.

Neither list is enforced against the verse, so the only thing that can keep them
honest is a check on their own shape. Each case below is a way a hand list goes
quietly wrong: a gloss for a character the book does not contain, a character
listed twice with two Englishes, a gloss that a glossary entry has since
replaced and that nobody notices is dead, or an overlay word the edition refuses
everywhere else, published on the atlas under the edition's name.
"""

import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import build_db  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]

# The overlay watchlist (CLAUDE.md), as whole words. A gloss is published as
# the edition's English, so it gets the same refusals the verse does. As in a
# `forbidden:` list, a capital is part of the violation: "the One" is the
# Neoplatonic overlay, "the one who" is English, and lowercase "god" is the
# edition's own word for 帝 (dì).
OVERLAY = ["heaven", "God", "holy", "sacred", "divine", "soul", "sin",
           "righteousness", "benevolence", "virtue", "blessing", "eternal",
           "the Way", "the One", "the masses"]


def book_characters():
    text = (ROOT / "source" / "chinese.md").read_text(encoding="utf-8")
    return set(build_db.han_chars(text))


def entry_characters():
    """Single characters an entry governs, as its term or through `covers:`."""
    out = set()
    terms = (ROOT / "glossary" / "terms.yaml").read_text(encoding="utf-8")
    for m in re.finditer(r'^- term: "([^"]+)"', terms, re.M):
        term = m.group(1)
        if len(term) == 1:
            out.add(term)
        elif "&" in term:
            out.update(t.strip() for t in term.split("&"))
    for m in re.finditer(r"^\s*# covers (.) ->", terms, re.M):
        out.add(m.group(1))
    return out


class HandGlosses(unittest.TestCase):
    lists = {
        "grammar-glosses.yaml": build_db.load_grammar_glosses(),
        "word-glosses.yaml": build_db.load_word_glosses(),
    }

    def test_every_character_is_in_the_book(self):
        book = book_characters()
        for name, rows in self.lists.items():
            stray = [c for c, _, _ in rows if c not in book]
            self.assertEqual(stray, [], f"{name} glosses characters the book lacks")

    def test_no_character_listed_twice(self):
        seen = {}
        for name, rows in self.lists.items():
            for c, _, _ in rows:
                self.assertNotIn(c, seen, f"{c} is in both {seen.get(c)} and {name}")
                seen[c] = name

    def test_no_gloss_shadows_an_entry(self):
        """An entry outranks the list, so a listed character with an entry is a
        dead gloss — kept by hand, published nowhere, and drifting."""
        governed = entry_characters()
        for name, rows in self.lists.items():
            dead = [c for c, _, _ in rows if c in governed]
            self.assertEqual(dead, [], f"{name}: these now have an entry — remove them")

    def test_gloss_is_present_and_short(self):
        for name, rows in self.lists.items():
            for c, pinyin, g in rows:
                self.assertTrue(g and g.strip(), f"{name}: {c} has no gloss")
                self.assertTrue(pinyin, f"{name}: {c} has no pinyin")
                self.assertLessEqual(len(g), 60, f"{name}: {c}'s gloss is an essay")

    def test_no_overlay_words(self):
        for name, rows in self.lists.items():
            for c, _, g in rows:
                for word in OVERLAY:
                    flags = 0 if word != word.lower() else re.I
                    self.assertIsNone(
                        re.search(rf"\b{re.escape(word)}\b", g, flags),
                        f"{name}: {c} → {g!r} uses the overlay word {word!r}")


if __name__ == "__main__":
    unittest.main()
