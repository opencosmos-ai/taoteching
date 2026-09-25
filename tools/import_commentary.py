#!/usr/bin/env python3
"""
import_commentary.py — vendor a classical commentary into sources/, verifiably.

    python3 tools/import_commentary.py --fetch          # download the wikitext
    python3 tools/import_commentary.py --report         # parse and report, write nothing
    python3 tools/import_commentary.py --write          # write sources/commentaries/wangbi/

Why this exists as a tool rather than a one-off paste: **provenance means
reproducible.** Anyone can re-run this and get byte-identical files, and the
fidelity check below is what lets the result be trusted at all.

WHY IT IS SAFE TO VENDOR THIS TEXT. Three independent grounds, each sufficient:

  1. Wang Bi died in 249 CE. The work is public domain by age everywhere.
  2. The transcription is of the 欽定四庫全書 (Siku Quanshu, imperially
     commissioned 1773-1782) — a printing older than any copyright term.
  3. Chinese Wikisource, the transcription's host, states in its own copyright
     policy that "the transcription of a work on Wikisource does not create a
     new copyright, so if the original work has entered the public domain the
     transcription here is also public domain," and that the site-wide CC BY-SA
     default "never comes into play for mainspace content." The page also
     carries {{PD-old}}.

And the one layer that COULD carry a claim is absent by that page's own
editorial policy. Its wikitext opens:

    請根據四庫全書掃描版校對本頁 … 加標點請另外建立頁面
    "Proofread this page against the Siku Quanshu scan … to add punctuation,
     create a separate page."

So the transcription is unpunctuated — the authorial layer only. See
sources/PROVENANCE.md.

THE FIDELITY CHECK, which is the point. The source interleaves Laozi lemmas
with Wang Bi's comment on each. Every lemma line is matched against our own
source/chinese.md for that chapter. If a line matches, the transcription is
faithful there, which is direct evidence that the commentary lines around it
were carried across intact too. Lines that do not match are reported, never
silently normalized: some are Siku glyph forms (handled below) and the rest are
genuine textual variants worth logging in sources/variants.yaml.
"""

import argparse
import difflib
import re
import sys
import urllib.parse
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import (ROOT, load_chapters,  # noqa: E402
                        CJK, ORTHOGRAPHIC, cjk, fold)

SCRATCH = ROOT / "sources" / ".cache"
COMMENTARIES = ROOT / "sources" / "commentaries"

SOURCES = {
    "wangbi": {
        "slug": "wangbi",
        "work": "老子道徳經注",
        "author": "王弼",
        "author_dates": "226–249 CE",
        "edition": "欽定四庫全書 (Siku Quanshu), 子部十四 · 道家類",
        "edition_dates": "commissioned 1773, completed 1782",
        "host": "Chinese Wikisource, mainspace, tagged {{PD-old}}",
        "url": "https://zh.wikisource.org/zh-hant/老子道徳經_(四庫全書本)",
        "punctuation": "none — the page's editorial policy excludes it",
        "rights": "public domain by age (author d. 249 CE); printing 1782",
        # one wikitext page; chapters marked 　　N章
        "pages": None,
        "cache": "wangbi-sikuquanshu.wikitext",
    },
    "heshanggong": {
        "slug": "heshanggong",
        "work": "老子道德經 河上公章句",
        "author": "河上公",
        "author_dates": "Han dynasty, dates unknown",
        "edition": "四部叢刊 0532 · 景常熟瞿氏鐵琴銅劍樓藏宋刊本 (photo-reproduction of the Song printed edition held in the Qu family's Iron-Qin-Copper-Sword Tower, Changshu)",
        "edition_dates": "Song woodblock; Sibu congkan reproduction from 1919",
        "host": "Chinese Wikisource, Page: namespace, transcribed from the djvu scan",
        "url": "https://zh.wikisource.org/wiki/老子道德經_(四部叢刊本)",
        "punctuation": "none in the source",
        "rights": "public domain by age (Han commentary); Song printing, reproduced 1919",
        # assembled from scan pages 16-92 of one djvu index
        "pages": (16, 92, "Sibu Congkan0532-河上公-老子道德經-1-1.djvu"),
        "cache": "heshanggong",
    },
    "hanfeizi": {
        "slug": "hanfeizi",
        "work": "韓非子 · 解老 / 喻老",
        "author": "韓非",
        "author_dates": "c. 280–233 BCE",
        "edition": "韓非子, chapters 20 (解老, \"Explaining Laozi\") and 21 (喻老, \"Illustrating Laozi\")",
        "edition_dates": "pre-Qin; the oldest surviving commentary on the Laozi",
        "host": "Chinese Wikisource, mainspace",
        "url": "https://zh.wikisource.org/wiki/韓非子/解老",
        "punctuation": "modern editorial, PRESENT and retained — these are prose essays, not lemma lists, and are unreadable without it",
        "rights": "public domain by age (author d. 233 BCE)",
        # essays that QUOTE the Laozi in 「」 rather than gloss it lemma by lemma
        "essays": ["韓非子/解老", "韓非子/喻老"],
        "pages": None,
        "cache": "hanfeizi",
    },
}


_NUM = {c: i for i, c in enumerate("〇一二三四五六七八九")}


def cn2int(s):
    if "十" not in s:
        return sum(_NUM[c] for c in s)
    a, _, b = s.partition("十")
    return (_NUM[a] if a else 1) * 10 + (sum(_NUM[c] for c in b) if b else 0)


def strip_markup(line):
    """Drop wiki markup, keeping the Siku editors' own collation notes visible.

    {{SK notes|案…}} are the 18th-century compilers' notes ("originally X, now
    corrected per the Yongle Encyclopedia"). They are part of the Siku edition
    and public domain by age, so they are preserved, marked with 〔〕.
    {{SKchar|N}} stands for a glyph the transcribers could not encode; it
    becomes □ so that a gap is never mistaken for text.
    """
    line = re.sub(r"{{SK notes\|([^}]*)}}", r"〔\1〕", line)
    line = re.sub(r"{{SKchar\|\d+}}", "□", line)
    line = re.sub(r"{{[^}]*}}", "", line)
    line = re.sub(r"<[^>]*>", "", line)
    line = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", line)
    line = re.sub(r"\[\[([^\]]*)\]\]", r"\1", line)
    return line.replace("　", "").strip()


def fetch(src):
    """Download the wikitext. One page, a scan-page range, or a set of essays."""
    if src.get("essays"):
        out = SCRATCH / src["cache"]
        out.mkdir(parents=True, exist_ok=True)
        for title in src["essays"]:
            f = out / (title.split("/")[-1] + ".wikitext")
            if f.exists() and f.stat().st_size:
                continue
            url = ("https://zh.wikisource.org/w/index.php?title="
                   + urllib.parse.quote(title) + "&action=raw")
            f.write_bytes(_get(url))
            time.sleep(0.4)
        print(f"essays: {len(src['essays'])} → {out.relative_to(ROOT)}")
        return out

    if src["pages"] is None:
        SCRATCH.mkdir(parents=True, exist_ok=True)
        dest = SCRATCH / src["cache"]
        url = ("https://zh.wikisource.org/w/index.php?title="
               + urllib.parse.quote("老子道徳經 (四庫全書本)") + "&action=raw")
        dest.write_bytes(_get(url))
        print(f"fetched {dest.stat().st_size:,} bytes → {dest.relative_to(ROOT)}")
        return dest

    lo, hi, index = src["pages"]
    out = SCRATCH / src["cache"]
    out.mkdir(parents=True, exist_ok=True)
    got = cached = 0
    for n in range(lo, hi + 1):
        f = out / f"{n:03d}.wikitext"
        if f.exists() and f.stat().st_size:
            cached += 1
            continue
        url = ("https://zh.wikisource.org/w/index.php?title="
               + urllib.parse.quote(f"Page:{index}/{n}") + "&action=raw")
        f.write_bytes(_get(url))
        got += 1
        time.sleep(0.4)          # be a good citizen with someone else's server
    print(f"scan pages: {got} fetched, {cached} already cached → {out.relative_to(ROOT)}")
    return out


def _get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "taoteching-research/1.0 (CC0 public-domain translation project)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def _load_raw(src, path):
    """One string of wikitext, with page wrappers removed.

    For Heshang Gong the text runs ACROSS scan-page boundaries — a lemma or a
    commentary column can be cut in half by the end of a page — so the pages are
    concatenated in order before anything is parsed.
    """
    if src["pages"] is None:
        return path.read_text(encoding="utf-8")
    files = sorted(path.glob("*.wikitext"), key=lambda p: int(p.stem))
    raw = "\n".join(f.read_text(encoding="utf-8") for f in files)
    # <noinclude> holds pagequality banners and running footers. Strip it FIRST:
    # seven of the eight chapter headings that fall at a page break carry a
    # footer on the same line, and matching before stripping missed all seven.
    return re.sub(r"<noinclude>.*?</noinclude>", "", raw, flags=re.S)


def parse(src, path):
    """Split into chapters, then classify each run as lemma or commentary."""
    if src.get("essays"):
        return _parse_essays(src, path)
    raw = _load_raw(src, path)
    blocks = {}

    if src["pages"] is None:
        cur, num = [], None
        for line in raw.split("\n"):
            m = re.match(r"^　　([一二三四五六七八九十]+)章", line)
            if m:
                if num:
                    blocks[num] = "\n".join(cur)
                num, cur = cn2int(m.group(1)), []
                continue
            # Ten headings are not on a line of their own: the transcription
            # runs them onto the end of the previous chapter's last comment —
            # …相濡之徳生也十九章{{SK notes|…}}. Matching only line-initial
            # headings merged each of those chapters into the one before, and
            # the ten were reported as "unproofread" for two years.
            glued = _glued_heading(line, num)
            if glued:
                cur.append(glued[0])
                blocks[num] = "\n".join(cur)
                num, cur = glued[1], []
                continue
            if num and line.startswith("　　"):
                cur.append(line)
        if num:
            blocks[num] = "\n".join(cur)
    else:
        # Heshang Gong titles each chapter himself: 體道第一, 養身第二 …
        # 河上公章句第一 is the volume heading, not a chapter, so titles are
        # capped at four characters.
        marks = list(re.finditer(r"^　+([㐀-鿿]{2,4})第([一二三四五六七八九十]+)$", raw, re.M))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
            # Drop newlines inside the chapter. They are woodblock line-ends and
            # carry no meaning for us, and templates split across one otherwise
            # survive stripping — {{SKchar|3205}} broken over two lines leaked
            # into the output as text on the first run.
            blocks[cn2int(m.group(2))] = raw[m.end():end].replace("\n", "")
            TITLES[cn2int(m.group(2))] = m.group(1)

    chapters = load_chapters()
    parsed, residual = {}, []
    for n, body in sorted(blocks.items()):
        base = fold(chapters[n].chinese)
        rows = _rows(src, body)
        lemma_ok = lemma_var = 0
        out_rows = []
        for kind, text in rows:
            if kind == "comment":
                out_rows.append((kind, text))
                continue
            probe = fold(text)
            if not probe:
                continue
            if probe in base:
                out_rows.append(("lemma", text)); lemma_ok += 1
                continue
            best = (0.0, "")
            for i in range(max(1, len(base) - len(probe) + 1)):
                w = base[i:i + len(probe)]
                r = difflib.SequenceMatcher(None, probe, w).ratio()
                if r > best[0]:
                    best = (r, w)
            if best[0] > 0.80 and len(probe) < 60:
                out_rows.append(("lemma*", text)); lemma_var += 1
                residual.append((n, probe, best[1]))
            else:
                out_rows.append(("comment", text))
        parsed[n] = {"rows": out_rows, "lemma_ok": lemma_ok, "lemma_var": lemma_var}
    return parsed, residual


TITLES = {}


def _glued_heading(line, num):
    """(text before the heading, chapter number) if `line` ends in chapter num+1's heading.

    Only the NEXT chapter's number is accepted. The comments themselves say 下章
    ("the next chapter") and 上章 mid-line, and a trailing run of numerals can
    belong to the comment — so the number is read right-to-left, one to three
    characters, and must be exactly num + 1 to count.
    """
    if num is None or not line.startswith("　　"):
        return None
    m = re.search(r"章(?:{{SK notes\|[^}]*}})?\s*$", line)
    if not m:
        return None
    head = line[:m.start()]
    for k in (1, 2, 3):
        digits = head[-k:]
        if len(digits) < k or not all(c in "一二三四五六七八九十" for c in digits):
            break
        if cn2int(digits) == num + 1:
            return head[:-k], num + 1
    return None


def _parse_essays(src, path):
    """Han Feizi does not gloss the Laozi line by line; he argues, and quotes.

    The quotations sit in 「」, usually after 故曰 ("therefore it is said"). So
    the chapter a passage belongs to is discovered by matching each quotation
    against our own base text — the same fidelity check the other importers use,
    doing double duty here as the only way to index the essays at all.
    """
    chapters = load_chapters()
    # An index of every 5-gram in the book, so a quotation can be placed.
    index = {}
    for n, ch in chapters.items():
        folded = fold(ch.chinese)
        for i in range(len(folded) - 4):
            index.setdefault(folded[i:i + 5], set()).add(n)

    parsed, residual = {}, []
    for f in sorted(path.glob("*.wikitext")):
        essay = f.stem
        raw = f.read_text(encoding="utf-8")
        raw = re.sub(r"{{[^}]*}}", "", raw)
        raw = re.sub(r"<[^>]*>", "", raw)
        raw = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", raw)
        raw = re.sub(r"\[\[([^\]]*)\]\]", r"\1", raw)
        for para in (p.strip() for p in raw.split("\n") if p.strip()):
            quotes = re.findall(r"「([^」]+)」", para)
            hits = {}
            for q in quotes:
                fq = fold(q)
                if len(fq) < 5:
                    continue
                votes = {}
                for i in range(len(fq) - 4):
                    for n in index.get(fq[i:i + 5], ()):
                        votes[n] = votes.get(n, 0) + 1
                if votes:
                    best = max(votes, key=votes.get)
                    hits.setdefault(best, []).append(q)
            for n, qs in hits.items():
                d = parsed.setdefault(n, {"rows": [], "lemma_ok": 0, "lemma_var": 0})
                base = fold(chapters[n].chinese)
                for q in qs:
                    # The same fidelity check the interleaved importers apply. It
                    # was missing here, so every Han Feizi quotation was written
                    # as an exact lemma and the header's `*` convention silently
                    # asserted agreement it had never tested. 韓非 died in 233 BCE
                    # and is the oldest witness to this text there is, so his
                    # divergences are evidence, not noise.
                    if fold(q) in base:
                        d["rows"].append(("lemma", q)); d["lemma_ok"] += 1
                    else:
                        d["rows"].append(("lemma*", q)); d["lemma_var"] += 1
                        residual.append((n, fold(q), ""))
                d["rows"].append(("comment", f"〔{essay}〕 " + para))
    return parsed, residual


def _rows(src, body):
    """Split a chapter body into alternating lemma / commentary runs."""
    if src["pages"] is None:
        return [("lemma?", strip_markup(l)) for l in body.split("\n") if strip_markup(l)]

    # Heshang Gong's notes are printed as two columns of small type inline with
    # the text, marked {{雙行註文|right|left}}. The | is the column break, so the
    # parts join in reading order. Consecutive templates continue one note.
    rows, buf_lemma, buf_note = [], "", ""

    def flush_lemma():
        nonlocal buf_lemma
        if buf_lemma.strip():
            rows.append(("lemma?", buf_lemma.strip()))
        buf_lemma = ""

    def flush_note():
        nonlocal buf_note
        if buf_note.strip():
            rows.append(("comment", buf_note.strip()))
        buf_note = ""

    # One level of nesting is real: {{SKchar|N}} appears INSIDE annotation
    # templates. A [^}]* body stops at the nested }} and truncates the note,
    # which silently dropped commentary text on the first run.
    NOTE = r"({{雙行註文\|(?:[^{}]|{{[^{}]*}})*}})"
    for token in re.split(NOTE, body):
        if token and token.startswith("{{雙行註文"):
            flush_lemma()
            inner = token[len("{{雙行註文|"):-2]
            # Resolve nested templates BEFORE splitting on the column-break |,
            # or {{SKchar|3932}} loses its pipe and leaks through as text.
            inner = re.sub(r"{{SKchar\|\d+}}", "□", inner)
            inner = re.sub(r"{{[^{}]*}}", "", inner)
            buf_note += "".join(inner.split("|"))
        else:
            plain = strip_markup(token)
            if plain:
                flush_note()
                buf_lemma += plain
    flush_lemma(); flush_note()
    return rows


def write(src, parsed):
    out = COMMENTARIES / src["slug"]
    out.mkdir(parents=True, exist_ok=True)
    for n, d in sorted(parsed.items()):
        title = TITLES.get(n, "")
        head = f'{src["work"]} — {src["author"]} — 第{n}章'
        if title:
            head += f"  〈{title}〉"
        body = [
            "---",
            f'work: "{src["work"]}"',
            f'author: "{src["author"]}"',
            f'author_dates: "{src["author_dates"]}"',
            f"chapter: {n}",
        ]
        if title:
            body.append(f'chapter_title: "{title}"')
        body += [
            f'edition: "{src["edition"]}"',
            f'edition_dates: "{src["edition_dates"]}"',
            f'transcription: "{src["host"]}"',
            f'obtained: "{src["url"]}"',
            f'punctuation: "{src["punctuation"]}"',
            f'rights: "{src["rights"]}"',
            'imported_by: "tools/import_commentary.py"',
            "---",
            "",
            f"# {head}",
            "",
            "*Commentary interleaved. Each **lemma** is the Laozi text being commented on; the "
            "line under it is the comment. Lemmas marked `*` differ from our base text — see "
            "`sources/variants.yaml`. 〔…〕 are the edition's own collation notes. □ is a glyph "
            "the transcribers could not encode.*",
            "",
        ]
        for kind, text in d["rows"]:
            if kind == "lemma":
                body += [f"**{text}**", ""]
            elif kind == "lemma*":
                body += [f"**{text}** `*`", ""]
            else:
                body += [f"> {text}", ""]
        (out / f"{n:03d}.md").write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {len(parsed)} files → {out.relative_to(ROOT)}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", choices=sorted(SOURCES), default="wangbi")
    p.add_argument("--fetch", action="store_true")
    p.add_argument("--report", action="store_true")
    p.add_argument("--write", action="store_true")
    args = p.parse_args()

    src = SOURCES[args.source]
    cached = SCRATCH / src["cache"]
    path = fetch(src) if (args.fetch or not cached.exists()) else cached

    parsed, residual = parse(src, path)
    missing = [n for n in range(1, 82) if n not in parsed]
    ok = sum(d["lemma_ok"] for d in parsed.values())
    var = sum(d["lemma_var"] for d in parsed.values())
    com = sum(1 for d in parsed.values() for k, _ in d["rows"] if k == "comment")

    if src.get("essays"):
        # Han Feizi never set out to cover the book; he argues and quotes. So
        # "missing" is the wrong frame — report what he discusses.
        print(f"\n{args.source}: discusses {len(parsed)} chapters — "
              f"{', '.join(str(n) for n in sorted(parsed))}")
        print("   (coverage is found by matching his 「」 quotations against our base "
              "text, so a passage he paraphrases without quoting will not appear)")
    else:
        print(f"\n{args.source}: {len(parsed)}/81 chapters"
              + (f", missing {missing}" if missing else " — complete"))
    print(f"lemma lines: {ok} matched our base text exactly, {var} with variants"
          + (f" ({ok / (ok + var):.0%} exact)" if ok + var else ""))
    print(f"commentary blocks: {com}")

    if residual:
        seen = set()
        print(f"\ncandidate textual variants ({len(residual)}):")
        for n, mine, theirs in residual:
            diff = [(a, b) for op, i1, i2, j1, j2 in
                    difflib.SequenceMatcher(None, mine, theirs).get_opcodes()
                    if op == "replace" and i2 - i1 == j2 - j1
                    for a, b in zip(mine[i1:i2], theirs[j1:j2])]
            pairs = " ".join(f"{a}/{b}" for a, b in diff if a != b)
            if pairs and (n, pairs) not in seen:
                seen.add((n, pairs))
                print(f"   ch{n:>2}  {pairs}")
        print("\n   Review by hand; real forks go in sources/variants.yaml, glyph-only "
              "pairs in ORTHOGRAPHIC above.")

    if args.write:
        print()
        write(src, parsed)
    elif not args.report:
        print("\n(nothing written — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
