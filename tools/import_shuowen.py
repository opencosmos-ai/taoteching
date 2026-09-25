#!/usr/bin/env python3
"""import_shuowen.py — vendor the 說文解字 analysis of every character in the Laozi.

    python3 tools/import_shuowen.py --fetch    # download, cache, parse, write
    python3 tools/import_shuowen.py            # parse from cache and write

**What this is for.** This project reads by decomposing characters to their parts
— it is the method, not a flourish: `glossary/qiang-強.md` turns on 強 being
蚚也，从虫弘聲 ("the grain weevil; from 虫 insect, with 弘 as phonetic"), and
`glossary/ruo-弱.md` on 弱 being two bows. Until now every one of those readings
was looked up by hand, one character at a time, and none of it was indexed.

**Why 說文解字 and not a modern character database.** Two reasons, and the second
matters more.

*Rights.* 說文解字 (*Shuōwén Jiězì*, Xu Shen 許慎, ~100 CE) is public domain by age
and the Wikisource transcription names its edition — 四部叢刊初編, the same series
the Heshang Gong text came from. It clears `sources/PROVENANCE.md`'s four
admission rules by an already-trodden route. A modern character database would
raise a licensing question this repository does not need to answer.

*Fitness.* A 康熙 (Kangxi) radical is an **index** — the bucket a character is
filed under so you can find it — and it flattens the one distinction that carries
meaning. 說文 states its analysis in its own text and keeps that distinction
explicit: 从X marks a **semantic** component, X聲 marks a **phonetic** one, present
for sound alone. Told that 強 is "from 虫 (insect)", a reader learns something
true; told its radical is 弓 (bow), they learn how a Qing editor filed it. Both
are worth having and they are not the same fact, so they are stored in different
columns.

**What is vendored.** Only the entries for characters that occur in the Laozi —
the corpus lexicon, not the whole dictionary. That is a selection of public-domain
text, marked as one. The raw volumes are cached under `sources/.cache/`
(gitignored) so the vendoring is reproducible, exactly as import_commentary.py
does it.

**What is NOT here: English.** 說文's definitions are classical Chinese and are
vendored untranslated. Rendering ~800 of them by machine would manufacture
scholarship nobody did, which `sources/PROVENANCE.md` forbids in spirit and
`process/method.md` §3 forbids in terms. The *components* are glossed, because
that is where the explorable value is: seeing 天 (tiān — sky) as 一 (one) over
大 (big) needs no translation of 顛也. Definitions are glossed by hand as
characters earn entries.
"""

import argparse
import html
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.corpus import ROOT, load_chapters  # noqa: E402

CACHE = ROOT / "sources" / ".cache" / "shuowen"
OUT = ROOT / "sources" / "shuowen" / "entries.md"
VOLUMES = [f"{i:02d}" for i in range(1, 15)]   # 卷一 … 卷十四; /15 is the preface

# 說文 uses 从 throughout; the wider CJK range matters because seal-script era
# component graphs stray outside the BMP, and a narrow range deletes them
# silently — the same trap import_commentary.py documents for 𤣥.
CJK = r"[㐀-鿿豈-﫿\U00020000-\U0002ebef]"

UA = {"User-Agent":
      "taoteching-research/1.0 (CC0 public-domain translation project)"}


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    for vol in VOLUMES:
        path = CACHE / f"{vol}.wikitext"
        if path.exists():
            continue
        url = ("https://zh.wikisource.org/w/index.php?title="
               + urllib.parse.quote(f"說文解字/{vol}") + "&action=raw")
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            path.write_bytes(r.read())
        print(f"    fetched 卷{vol}  {path.stat().st_size:>7} bytes")
        time.sleep(0.4)          # be a good citizen, as import_commentary is


# 說文 files its entries under the graph current c. 100 CE, which for some
# characters is not the graph our recension uses. Every mapping below was
# verified against the vendored text — the old form exists as an entry and its
# definition is coherent for the modern character — never asserted from memory.
# Anything unverified stays in the reported gap, where it can be worked on.
#
#   朙  照也。从月从囧          "to shine; from 月 moon and 囧 window"
#   譱  吉也。从誩从羊          "auspicious; from 誩 and 羊"
#   眞  僊人變形而登天也        "an immortal transformed, ascending"
#   処  止也。得几而止          "to halt; to find a stool and stop"
#   灋  刑也。平之如水，从水     "law; level as water, from 水"
#
# 朙 is worth pausing on: CLAUDE.md's 明 lock argues it is *moonlight through a
# window, not the sun*. 說文's own analysis — 从月从囧, moon plus window — says
# exactly that, from c. 100 CE. The lock was argued from the graph; here is the
# oldest witness to the graph agreeing.
SHUOWEN_VARIANTS = {
    "明": "朙", "善": "譱", "真": "眞", "處": "処", "法": "灋",
    # 2026-09-24 (WORKLIST T5-10). The gap list had become the worklist its own
    # footer says it is, and nobody had worked it: 87 of 798 characters, most of
    # them filed under a Han graph. Each pair below was checked the same way as
    # the five above — the old form is an entry in the vendored text, and its
    # definition is this character's word. Four were confirmed by the
    # transcription itself, which names the seal image after the modern graph:
    # 㠯（[[File:以-seal.svg]]）, 𠧞 兆, 宐 宜, 秊 年.
    #
    # Graph variants of one word — the definition reads straight across:
    "並": "竝",   # 併也
    "乘": "椉",   # 覆也
    "享": "亯",   # 獻也
    "以": "㠯",   # 用也
    "侯": "矦",   # 春饗所䠶矦也
    "偽": "僞",   # 詐也
    "兆": "𠧞",   # 灼龜坼也 — the crack in a heated shell
    "全": "仝",   # 完也
    "劍": "劒",   # 人所帶兵也
    "塵": "𪋻",   # 鹿行揚土也 — dust raised by running deer
    "宜": "宐",   # 所安也
    "年": "秊",   # 穀孰也 — the harvest ripening
    "弊": "獘",   # 頓仆也
    "彌": "镾",   # 久長也
    "既": "旣",   # 小食也
    "春": "萅",   # 推也
    "智": "𥏼",   # 識詞也
    "槁": "槀",   # 木枯也
    "窮": "竆",   # 極也
    "累": "纍",   # 綴得理也
    "耀": "燿",   # 照也
    "脆": "膬",   # 耎易破也
    "舉": "擧",   # 對舉也
    "蓋": "葢",   # 苫也
    "衛": "衞",   # 宿衞也
    "躁": "趮",   # 疾也
    "鎮": "鎭",   # 博壓也
    "間": "閒",   # 隟也
    "隳": "隓",   # 敗城𨸏曰隓
    "飲": "㱃",   # 歠也
    "似": "佀",   # 象也
    "孰": "𦏧",   # 食飪也 — cooked through, the sense behind "ripe"
    "戎": "𢦦",   # 兵也
    "肆": "𨽸",   # 極、陳也
    "兕": "𤉡",   # 如野牛而青
    "傫": "儽",   # 垂皃。一曰嬾解 — drooping; slack (ch 20's 傫傫)
    "鄉": "𨞰",   # 國離邑，民所封鄉也 — the definition uses 鄉 itself
    # The modern graph is the entry's 或體 / 篆文 / later form, filed under it:
    "抱": "捊",   # 引取也 — 抱 is 捊's variant with 包
    "網": "网",   # 庖犧所結繩以漁
    "跡": "迹",   # 步處也
    "隣": "鄰",   # 五家爲鄰
    "域": "或",   # 邦也 — 或 is the older graph; 域 adds 土, the soil
    "學": "斆",   # 覺悟也
    "尊": "𢍜",   # 酒器也 — and the definition writes the vessel 尊
    "抑": "𢑏",   # 按也
    "糞": "𡊄",   # 埽除也。讀若糞
    "偷": "媮",   # 巧黠也
    "靈": "𩆜",   # 𩆜巫，以玉事神
    "佐": "左",   # 手相左助也 — 左 is the hand that helps; 佐 adds 人
    "孩": "咳",   # 小兒笑也 — ch 20's 如嬰兒之未孩, the infant's first laugh
    "恍": "怳",   # 狂之皃
    "惚": "忽",   # 忘也
    #
    # Deliberately NOT mapped, though 說文 files each graph under another
    # entry: 其 (箕), 云 (雲), 於 (烏), 求 (裘). The modern character is a
    # borrowed graph there — 其 is "its", 箕 is a winnowing basket — so the
    # entry's definition is another word's, and attaching it would put a wrong
    # etymology under a right character. 太 stays out as well: 泰 is its likely
    # source but the vendored text does not say so.
}


def parse_analysis(text):
    """Split a 說文 entry into gloss, semantic parts, phonetic parts, and kind.

    The grammar is remarkably regular for a first-century text:

        天  顛也。至高無上。从一大。          → 从X Y : two semantic components
        丕  大也。从一，不聲。                → 从X，Y聲 : semantic + phonetic
        吏  治人者也。从一，从史，史亦聲。      → 亦聲 : X is both at once
        一  …凡一之屬皆从一。                 → a section head (a 說文 radical)

    `凡X之屬皆从X` ("all of the X class follow X") is stripped before the split,
    because its 从 is a statement about the class and not about this character —
    leaving it in makes every radical look like a compound of itself.
    """
    head = bool(re.search(r"凡.{1,2}之屬皆从", text))
    body = re.sub(r"凡.{1,2}之屬皆从.{1,2}。?", "", text)

    m = re.search(r"(从|從|象|闕)", body)
    gloss = (body[:m.start()] if m else body).strip()
    analysis = body[m.start():] if m else ""

    # Walk clause by clause. A single regex over the whole analysis cannot do
    # this: 聲 ("phonetic") and 省 ("abbreviated") are grammar, not parts, and a
    # greedy match swallows them — an earlier version reported 聲 as the most
    # common component in the book, 348 times, which is the analytical vocabulary
    # masquerading as the analysis.
    #
    #   从一大        both semantic
    #   从小丿聲      从 + last char before 聲 is the phonetic; the rest semantic
    #   从示，申聲    a bare X聲 clause is phonetic alone
    #   从水，𢊁省聲   省 marks an abbreviated graph; drop the marker, keep the part
    #   史亦聲        亦 = "also": already semantic, and phonetic too
    semantic, phonetic = [], []

    def add(target, ch):
        # Guard on the CJK range as well as the grammar words. Rare graphs arrive
        # as numeric character references (&#135591;) and any that survive
        # un-decoded would otherwise enter the component list one ASCII digit at
        # a time — an early run had "3" as the single most common component in
        # the book, 49 times.
        if (ch and ch not in target and ch not in "省聲亦从從"
                and re.fullmatch(CJK, ch)):
            target.append(ch)

    for clause in re.split(r"[，。；、：]", analysis):
        clause = clause.strip()
        if not clause:
            continue
        m2 = re.fullmatch(rf"({CJK})省?亦?聲", clause)
        if m2:
            add(phonetic, m2.group(1))
            continue
        m3 = re.fullmatch(rf"[从從]((?:{CJK})+)", clause)
        if not m3:
            continue
        chars = m3.group(1)
        if chars.endswith("聲"):
            core = chars[:-1].rstrip("亦").rstrip("省")
            if core:
                add(phonetic, core[-1])
                for c in core[:-1]:
                    add(semantic, c)
        else:
            for c in chars.rstrip("省"):
                add(semantic, c)

    kind = ("phonetic-compound" if phonetic and semantic else
            "phonetic-only" if phonetic else
            "compound" if semantic else
            "pictograph" if "象" in analysis else "unanalysed")
    return gloss, semantic, phonetic, kind, head


def parse_volume(wikitext):
    """Yield (char, radical, definition, annotation) from one volume page.

    Wikisource carries 說文 in **two different transcriptions**, and this was not
    obvious until the first run returned 23 of 798 characters. 卷一 is a wikitable
    with `{{+|'''天'''}}` headwords, `{{yw|…}}` text and `{{*|…}}` annotations
    carrying the 反切. 卷二 through 卷十四 are plain lines — `少：不多也。从小丿聲。`
    — with no annotation layer at all, and rare graphs written as numeric
    character references. Both are parsed; neither is normalised into the other.
    """
    wikitext = html.unescape(wikitext)
    section = None
    # NB `(?==={2}…)` would be a lookahead for THREE equals — the `{2}` binds to
    # the second `=`, not to the pair. It silently matched nothing, leaving every
    # character in 卷二–卷十四 with no 部. Write the lookahead so it cannot be
    # misread: two equals followed by something that is not an equals.
    for chunk in re.split(r"\n(?===[^=])", wikitext):
        m = re.match(r"==\s*(.+?)部\s*==", chunk)
        if m:
            section = m.group(1).strip()

        # 卷一 — the wikitable transcription
        for row in chunk.split("\n|-"):
            head = re.search(rf"\{{\{{\+\|'''({CJK})'''\}}\}}", row)
            yw = re.search(r"\{\{yw\|(.+?)\}\}", row, re.S)
            if not (head and yw):
                continue
            cells = re.findall(rf"\{{\{{\+\|({CJK})\}}\}}", row)
            ann = re.search(r"\{\{\*\|(.+?)\}\}", row, re.S)
            yield head.group(1), (cells[-1] if cells else section), \
                yw.group(1).strip(), (ann.group(1).strip() if ann else "")

        # 卷二 … 卷十四 — the plain transcription
        for raw in chunk.split("\n"):
            line = html.unescape(raw).strip()
            m2 = re.match(rf"^({CJK})(?:（[^）]*）)?[：:](.+)$", line)
            if m2:
                yield m2.group(1), section, m2.group(2).strip(), ""


def fanqie(annotation):
    """The 反切 spelling, e.g. 他前切 — Middle Chinese, and free by age."""
    m = re.search(rf"(({CJK}){{2}}切)", annotation or "")
    return m.group(1) if m else ""


def build(corpus_chars):
    entries = {}
    for vol in VOLUMES:
        path = CACHE / f"{vol}.wikitext"
        if not path.exists():
            print(f"    ! missing cache for 卷{vol} — run with --fetch")
            continue
        text = path.read_text(encoding="utf-8")
        for char, radical, definition, annotation in parse_volume(text):
            if char in entries:
                continue
            entries[char] = {
                "char": char, "radical": radical, "definition": definition,
                "fanqie": fanqie(annotation), "volume": vol,
            }

    # Three routes from a corpus character to its 說文 entry, narrowest first:
    # the graph itself; the curated orthographic fold the commentary importer
    # already uses; and the verified old-form map above. `headword` records which
    # graph the entry was actually filed under, so a reader is never told that
    # 明 has a definition it does not have.
    from import_commentary import fold

    folded = {}
    for c, e in entries.items():
        f = fold(c) or c
        folded.setdefault(f, (c, e))

    hits = {}
    for c in corpus_chars:
        if c in entries:
            hits[c] = dict(entries[c], headword=c, matched_by="exact")
        elif c in SHUOWEN_VARIANTS and SHUOWEN_VARIANTS[c] in entries:
            old = SHUOWEN_VARIANTS[c]
            hits[c] = dict(entries[old], headword=old, matched_by="old-form")
        elif c in folded:
            head, e = folded[c]
            hits[c] = dict(e, headword=head, matched_by="orthographic")

    for e in hits.values():
        g, sem, phon, kind, head = parse_analysis(e["definition"])
        e.update(gloss=g, semantic=sem, phonetic=phon, kind=kind,
                 section_head=head)
    return entries, hits


HEADER = """---
work: "說文解字"
work_english: "Shuowen Jiezi — Explaining Graphs and Analysing Characters"
author: "許慎"
author_english: "Xu Shen"
author_dates: "c. 58 – c. 148 CE"
edition: "四部叢刊初編 (Sibu Congkan, first series), facsimile"
transcription: "Chinese Wikisource, mainspace, tagged public domain worldwide"
obtained: "https://zh.wikisource.org/wiki/說文解字"
punctuation: "modern editorial, present in the transcription and retained"
rights: "public domain by age (author d. c. 148 CE)"
scope: "SELECTION — only characters occurring in the Laozi, not the whole dictionary"
imported_by: "tools/import_shuowen.py"
---

# 說文解字 — the characters of the Laozi

*The earliest systematic analysis of Chinese characters, c. 100 CE. Vendored as a
**selection**: only the characters that occur in this text, which is the corpus
lexicon rather than the dictionary. The Chinese is Xu Shen's and is public domain
by age; the parse into semantic and phonetic components is mechanical, from his
own 从X / X聲 formulas, and is recorded here rather than inferred at read time.*

**The definitions are untranslated, deliberately.** Machine-rendering ~800
classical Chinese definitions would manufacture scholarship nobody did. Component
characters are glossed elsewhere (the corpus lexicon), which is where the
explorable value sits: 天 as 一 over 大 is legible without translating 顛也.

**Columns.** `char` (as our recension writes it) · `headword` (the graph 說文 files
it under — 明 is entered as 朙) · `matched_by` · `radical` (the 說文 section, which
is not always the Kangxi one) · `kind` · `semantic` (从X — components carrying
meaning) · `phonetic` (X聲 — components present for sound alone) · `fanqie` (the
Middle Chinese spelling, where the transcription carries one) · `definition`
(Xu Shen, verbatim).

| char | headword | matched_by | radical | kind | semantic | phonetic | fanqie | definition |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""


def write(hits, missing):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [HEADER]
    for c in sorted(hits):
        e = hits[c]
        lines.append(
            f"| {c} | {e['headword']} | {e['matched_by']} | {e['radical']} | "
            f"{e['kind']} | {''.join(e['semantic'])} | {''.join(e['phonetic'])} | "
            f"{e['fanqie']} | {e['definition']} |"
        )
    if missing:
        lines.append(
            "\n## Not matched to a 說文 entry\n\n"
            f"*{len(missing)} of the corpus's characters. Most are later graphs, "
            "or are filed under an older form this importer has not verified. "
            "**A mapping is added only when the old form is confirmed present in "
            "the vendored text and its definition is coherent for the modern "
            "character** — see `SHUOWEN_VARIANTS` in `tools/import_shuowen.py`. "
            "Guessing here would put a wrong etymology under a right character, "
            "which is worse than a gap. This list is the worklist.*\n\n"
            f"{' '.join(missing)}\n"
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--fetch", action="store_true",
                    help="download the volumes to sources/.cache/ first")
    args = ap.parse_args()

    if args.fetch:
        fetch()

    corpus = set()
    for ch in load_chapters().values():
        corpus.update(re.findall(CJK, ch.chinese))

    entries, hits = build(corpus)
    if not entries:
        return 2
    missing = sorted(corpus - set(hits))
    write(hits, missing)

    kinds = {}
    for e in hits.values():
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1

    print(f"\n  說文 entries parsed        {len(entries)}")
    print(f"  characters in the Laozi    {len(corpus)}")
    print(f"  covered by 說文            {len(hits)}  "
          f"({100.0 * len(hits) / len(corpus):.1f}%)")
    for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
        print(f"    {k:20} {v}")
    print(f"  section heads (radicals)   "
          f"{sum(1 for e in hits.values() if e['section_head'])}")
    if missing:
        print(f"  not in 說文                {len(missing)}: {''.join(missing)}")
    print(f"\n  → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
