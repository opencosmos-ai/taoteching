"""The glossary entry template's four fixed headings, held.

process/skills/glossary-entry/template.md fixes four headings, word for word
and in this order, so a reader always knows where to find the picture, the
refusals, the grammar and the open question. Every other heading is free.

Entries written before the template are listed in NOT_YET. The list may only
shrink: an entry brought to the template leaves it, and the second test fails
until it does, so nobody has to remember.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GLOSSARY = ROOT / "glossary"

FIXED = ["The graph", "What is set aside", "Working register", "Left open"]

# Written before the template (2026-10-26). Remove an entry when it is brought
# to the template; never add one.
NOT_YET = {
    "baixing-百姓", "bao-保", "chang-常", "chi-持", "ci-慈", "da-大", "dao-道", "de-德",
    "di-帝", "fuming-復命", "gan-敢", "gong-公", "hun-混", "huo-貨", "ji-極", "jing-精",
    "jiu-咎", "ke-可", "luan-亂", "min-民", "ming-命", "ming-明", "mu-母", "po-魄",
    "pu-樸", "qi-器", "qiang-強", "qing-清", "quan-全", "ren-仁", "rou-柔", "ruo-弱",
    "shan-善", "shen-身", "sheng-生", "sheng-聖", "shi-事", "shi-士", "shi-恃",
    "shou-守", "tian-天", "tiandi-天地", "wang-王", "wanwu-萬物", "wei-唯", "wei-為",
    "wo-wu-我吾", "wu-you-無有", "wuwei-無為", "xin-信", "xin-心", "xing-行", "xu-虛",
    "xuan-miao-玄妙", "yi-一", "you-尤", "zheng-爭", "zhi-執", "zhi-治", "zhizu-知足",
    "zhong-眾", "ziran-自然",
}


def entries():
    return sorted(p for p in GLOSSARY.glob("*.md") if p.stem not in ("INDEX", "TRIAGE"))


def missing(path):
    """The fixed headings this entry lacks or has out of order, as a list."""
    heads = re.findall(r"^### (.+)$", path.read_text(encoding="utf-8"), re.M)
    at = []
    for name in FIXED:
        hit = next((k for k, h in enumerate(heads) if h.startswith(name)), None)
        if hit is None:
            return [f"no '### {name}'"]
        at.append(hit)
    return [] if at == sorted(at) else ["fixed headings out of order"]


class EntryShape(unittest.TestCase):
    def test_every_entry_follows_the_template(self):
        bad = {p.stem: missing(p) for p in entries()
               if p.stem not in NOT_YET and missing(p)}
        self.assertEqual(bad, {}, "see process/skills/glossary-entry/template.md")

    def test_the_list_of_entries_not_yet_on_the_template_only_shrinks(self):
        stems = {p.stem for p in entries()}
        self.assertEqual(sorted(NOT_YET - stems), [],
                         "NOT_YET names an entry that no longer exists")
        done = sorted(s for s in NOT_YET if s in stems and not missing(GLOSSARY / f"{s}.md"))
        self.assertEqual(done, [], "these now follow the template: take them off NOT_YET")


if __name__ == "__main__":
    unittest.main()
