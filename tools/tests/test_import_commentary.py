#!/usr/bin/env python3
"""
The Wang Bi chapter splitter, against the lines that defeated it.

Ten chapter headings in the Siku transcription are not on a line of their own:
they run onto the end of the previous chapter's last comment. The importer
matched only line-initial headings, merged each of those chapters into its
neighbour, and the ten were recorded as "unproofread" for two years
(WORKLIST T5-6). Every fixture below is a real line from the transcription.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import import_commentary as ic  # noqa: E402


CH18_END = ("　　甚美之名生於大惡所謂美惡同門六親父子兄弟夫婦也若六親自和國家自治"
            "則孝慈忠臣不知其所在矣魚相忘於江湖之道則相濡之徳生也十九章"
            "{{SK notes|案河上公注本此作還淳章永樂大典此章與上章合為一章}}")


class GluedHeading(unittest.TestCase):

    def test_two_digit_heading_on_a_comment_line(self):
        head, n = ic._glued_heading(CH18_END, 18)
        self.assertEqual(n, 19)
        self.assertTrue(head.endswith("則相濡之徳生也"))

    def test_one_digit_heading(self):
        line = "　　無私者無為於身也身先身存故曰能成其私也八章{{SK notes|案河上公注本此為易性章}}"
        head, n = ic._glued_heading(line, 7)
        self.assertEqual(n, 8)
        self.assertTrue(head.endswith("故曰能成其私也"))

    def test_three_character_numeral(self):
        line = "　　抗舉也加當也哀者必相惜而不趣利避害故必勝七十章{{SK notes|案河上公注本此為知難章}}"
        self.assertEqual(ic._glued_heading(line, 69)[1], 70)

    def test_only_the_next_chapter_counts(self):
        # The same line read as if we were in the wrong chapter must not split.
        self.assertIsNone(ic._glued_heading(CH18_END, 17))
        self.assertIsNone(ic._glued_heading(CH18_END, 19))

    def test_mid_line_chapter_references_are_not_headings(self):
        # 下章 ("the next chapter") inside a comment, from ch 35 and ch 57.
        line = "　　聽之不聞名曰希下章言道之出言淡兮其無味也"
        self.assertIsNone(ic._glued_heading(line, 35))
        line = "　　此三者言常反終後乃徳全其所處也下章云反者道之動也功不可取常處其母也"
        self.assertIsNone(ic._glued_heading(line, 39))

    def test_before_the_first_heading(self):
        self.assertIsNone(ic._glued_heading(CH18_END, None))


class WholeTranscription(unittest.TestCase):
    """If the fetched wikitext is cached, all 81 chapters must come out of it."""

    def test_all_81_chapters(self):
        cache = ic.SCRATCH / ic.SOURCES["wangbi"]["cache"]
        if not cache.exists():
            self.skipTest("wikitext not fetched; run import_commentary.py --fetch")
        parsed, _ = ic.parse(ic.SOURCES["wangbi"], cache)
        self.assertEqual(sorted(parsed), list(range(1, 82)))


if __name__ == "__main__":
    unittest.main()
