#!/usr/bin/env python3
"""
concordance.py — a character in, the evidence out.

The counterpart to check_locks.py, and the opposite kind of tool. The checker
optimizes precision: it must not cry wolf, and it exits non-zero. This optimizes
recall: it shows everything remotely relevant, judges nothing, and never fails.
Do not merge them — a tool that gates and searches at once ends up too noisy to
gate and too quiet to search.

    python3 tools/concordance.py 明                 # every chapter, line, rendering
    python3 tools/concordance.py --english "mystery"   # the reverse direction
    python3 tools/concordance.py --pairs 我 吾        # two terms side by side
    python3 tools/concordance.py --formulas          # repeated segments and frames
    python3 tools/concordance.py 常 --json           # for pulling into a session

This replaces the ad-hoc greps the method has been running by hand. The 天地
entry was built that way, and the finding that 陰 appears exactly once in the
whole book came out of exactly this kind of sweep.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import (ROOT, load_chapters, load_guodian, load_terms,  # noqa: E402
                        load_variants)

BOLD, DIM, OFF = "\033[1m", "\033[2m", "\033[0m"


def _plain(text):
    """Strip the literal gloss's bracketed pinyin apparatus."""
    return re.sub(r"\s+", " ", re.sub(r"\\?\[[^\]]*\\?\]", "", text)).strip()


def lock_for(term, terms):
    for t in terms:
        if term in t.characters or term == t.term:
            return t
    return None


# ------------------------------------------------------------------ occurrences

def occurrences(term, chapters):
    """Every chapter containing the term, with its lines and the chapter's verse."""
    out = []
    for n in sorted(chapters):
        ch = chapters[n]
        rows = [r for r in ch.source_rows if term in r.chinese]
        if rows:
            out.append((ch, rows))
    return out


def show_term(term, chapters, terms, quiet=False):
    hits = occurrences(term, chapters)
    lock = lock_for(term, terms)

    print(f"\n{BOLD}{term}{OFF}", end="")
    if lock:
        print(f"  ({lock.pinyin}) → {lock.render}", end="")
        if lock.forbidden:
            print(f"   never: {', '.join(lock.forbidden)}", end="")
        print(f"\n{DIM}{lock.entry}{OFF}")
    else:
        print(f"   {DIM}no glossary entry yet — see glossary/TRIAGE.md{OFF}")

    total = sum(len(rows) for _, rows in hits)
    drafted = [ch for ch, _ in hits if ch.drafted]
    print(f"{len(hits)} chapters, {total} lines "
          f"({len(drafted)} drafted, {len(hits) - len(drafted)} not yet)\n")

    for ch, rows in hits:
        flag = "" if ch.drafted else f"  {DIM}[{ch.status}]{OFF}"
        print(f"  {BOLD}ch {ch.number}{OFF}{flag}")
        for r in rows:
            print(f"    {r.chinese}")
            if not quiet:
                print(f"      {DIM}{_plain(r.literal)}{OFF}")
        if ch.drafted and not quiet:
            for _, line in ch.verse:
                print(f"      │ {line.strip()}")
        print()
    return hits


# ------------------------------------------------------- the reverse direction

def show_english(phrase, chapters, terms, quiet=False):
    """Which chapters use this English, and is each use backed by its character?

    The higher-value direction, and the half the Chinese cannot answer. A lock
    is a two-way claim — every 明 renders as clear-seeing, AND every
    clear-seeing renders 明 — and only this direction catches the second half:
    a rendering applied where the character licensing it is absent.
    """
    lock = None
    for t in terms:
        if (phrase.lower() in t.render.lower()
                or t.flexion_for(phrase)
                or any(phrase.lower() == f.lower() for f in t.forbidden)):
            lock = t
            break
    flexion = lock.flexion_for(phrase) if lock else None

    print(f'\n{BOLD}"{phrase}"{OFF}', end="")
    if lock:
        if any(phrase.lower() == f.lower() for f in lock.forbidden):
            kind, scope = "forbidden for", ""
        elif flexion:
            chs = ", ".join(str(c) for c in flexion["chapters"])
            kind = "a declared flexion of"
            scope = f" — licensed at ch {chs} only"
        else:
            kind, scope = "the rendering of", ""
        print(f"  — {kind} {lock.term} ({lock.pinyin}){scope}\n{DIM}{lock.entry}{OFF}")
        if flexion and flexion.get("why"):
            print(f'{DIM}  why: {flexion["why"]}{OFF}')
    else:
        print(f"   {DIM}not tied to any locked term{OFF}")

    backed, unbacked = [], []
    for n in sorted(chapters):
        ch = chapters[n]
        if not ch.drafted:
            continue
        for ln, line in ch.verse:
            if phrase.lower() in line.lower():
                has = (lock and any(ch.has(c) for c in lock.characters)
                       and lock.licenses(phrase, ch.number))
                (backed if has else unbacked).append((ch, ln, line.strip()))

    print(f"{len(backed) + len(unbacked)} lines"
          + (f" — {len(backed)} backed by {lock.term}, {len(unbacked)} not" if lock else "")
          + "\n")

    for label, group in (("backed", backed), ("not backed", unbacked)):
        if not group or (not lock and label == "backed"):
            continue
        if lock:
            print(f"  {BOLD}{label}{OFF}")
        for ch, ln, line in group:
            print(f"    ch {ch.number}:{ln}  {line}")
            if lock and label == "not backed" and not quiet:
                if flexion and any(ch.has(c) for c in lock.characters):
                    print(f"      {DIM}{'/'.join(lock.characters)} is here, but this "
                          f"flexion is licensed only at ch "
                          f"{', '.join(str(c) for c in flexion['chapters'])}{OFF}")
                else:
                    print(f"      {DIM}no {'/'.join(lock.characters)} in this chapter{OFF}")
        print()

    if lock and unbacked:
        print(f'  {DIM}"{phrase}" without {lock.term} is either an ordinary English word '
              f"or a rendering that outran its character. Check each.{OFF}\n")
    return backed, unbacked


# ------------------------------------------------- what we have already decided

# Where a decision can have been written down. Ordered as a reader should take
# them: the ruling first, then the thin record, then the debt, then the essays.
_RECORD = [
    ("glossary", "the ruling and its argument"),
    ("notes", "the decision, thin"),
    ("WORKLIST.md", "what is still owed"),
    ("DISCOVERIES.md", "findings worth an essay"),
    ("chapters", "the chapter notes — where findings are born and stay"),
]


def _record_hits(term):
    """Every place this repository has already written about a character.

    Chapters are searched in their `## Notes` only. Their source tables print
    the character on every line it occurs in, which would bury the findings
    under the evidence — and the findings are the point.
    """
    out = []
    for name, _ in _RECORD:
        if name.endswith(".md"):
            paths = [ROOT / name]
        else:
            paths = sorted((ROOT / name).glob("*.md"))
        for path in paths:
            if not path.exists() or path.name in ("INDEX.md", "terms.yaml"):
                continue
            text = path.read_text(encoding="utf-8")
            if name == "chapters":
                i = text.find("## Notes")
                if i < 0:
                    continue
                offset = text[:i].count("\n")
                text = text[i:]
            else:
                offset = 0
            for n, line in enumerate(text.split("\n"), 1):
                if term in line:
                    out.append((name, path, n + offset, line.strip()))
    return out


def show_record(term, quiet=False):
    """`--record 亂` — the repo's own prior reasoning, before the dictionary.

    The method sends you to the graph, the witnesses, the commentaries and the
    locks: every source outside this repository and none inside it. So the
    record we have built is the one source nobody consults, and it is the
    cheapest. See process/principles/search-the-record-first.md.
    """
    hits = _record_hits(term)
    print(f"\n{BOLD}{term}{OFF} — what this repository has already written\n")
    if not hits:
        print(f"  {DIM}nothing yet. That is an answer, and it took one command.{OFF}\n")
        return hits

    blurb = dict(_RECORD)
    for name, _ in _RECORD:
        group = [h for h in hits if h[0] == name]
        if not group:
            continue
        print(f"  {BOLD}{name}{OFF}  {DIM}{blurb[name]} — {len(group)}{OFF}")
        # The term's own entry is the one place nobody forgets to look, and it
        # is long enough to bury everything else. Collapse it to a pointer.
        own = [h for h in group if name == "glossary" and term in h[1].stem]
        if own:
            print(f"    {DIM}{own[0][1].relative_to(ROOT)}{OFF}  "
                  f"{DIM}— its own entry, {len(own)} lines{OFF}")
            group = [h for h in group if h not in own]
        for _, path, n, line in group:
            rel = path.relative_to(ROOT)
            if quiet:
                print(f"    {rel}:{n}")
            else:
                text = line if len(line) <= 150 else line[:147] + "…"
                print(f"    {DIM}{rel}:{n}{OFF}  {text}")
        print()

    print(f"  {DIM}This is our own prior reasoning, not evidence — a first stop, "
          f"never the last.{OFF}\n")
    return hits


# ----------------------------------------------------------------------- pairs

def show_pairs(a, b, chapters, terms, quiet=False):
    """Two terms across the book — the 我/吾, 玄/妙, 正/奇 work."""
    ha = {ch.number: rows for ch, rows in occurrences(a, chapters)}
    hb = {ch.number: rows for ch, rows in occurrences(b, chapters)}
    both = sorted(set(ha) & set(hb))
    only_a = sorted(set(ha) - set(hb))
    only_b = sorted(set(hb) - set(ha))

    print(f"\n{BOLD}{a}{OFF} and {BOLD}{b}{OFF}\n")
    print(f"  together in {len(both)}: {', '.join(map(str, both)) or '—'}")
    print(f"  {a} alone in {len(only_a)}: {', '.join(map(str, only_a)) or '—'}")
    print(f"  {b} alone in {len(only_b)}: {', '.join(map(str, only_b)) or '—'}\n")

    for n in both:
        ch = chapters[n]
        print(f"  {BOLD}ch {ch.number}{OFF}" + ("" if ch.drafted else f"  {DIM}[{ch.status}]{OFF}"))
        for label, rows in ((a, ha[n]), (b, hb[n])):
            for r in rows:
                print(f"    {label}  {r.chinese}")
                if not quiet:
                    print(f"        {DIM}{_plain(r.literal)}{OFF}")
        print()
    return both, only_a, only_b


# -------------------------------------------------------------------- formulas

def _segments(chapters, min_len):
    """Every Chinese comma-segment in the book, with every place it occurs.

    An occurrence is (chapter, row index), NOT a set of chapters — which is the
    whole point. The previous version indexed into a set, so a segment repeating
    three times inside one chapter collapsed to one entry and was then filtered
    out as "not shared". Chapter 11's 當其無, repeated verbatim three times and
    rendered three different ways, was invisible to this tool and to
    check_locks.py alike until 2026-09-05.
    """
    index = defaultdict(list)
    for ch in chapters.values():
        for i, row in enumerate(ch.source_rows):
            for seg in re.split(r"[，。；、？！]", row.chinese):
                seg = "".join(re.findall(r"[㐀-鿿]+", seg))
                if len(seg) >= min_len:
                    index[seg].append((ch.number, i))
    return index


# A template is a repeated frame with slots: 將欲▢之, 有▢之用, ▢得一以▢. Two
# same-length segments belong to one when they agree everywhere but a few
# positions. Two fixed characters is the floor — one is not a frame, it is a
# character, and 不▢▢ would collect half the book. That floor is why ch 8's
# X善Y (one anchor, seven members) is not found here; 善's own concordance is.
SLOT = "▢"
MAX_VARIABLE = 2
MIN_FIXED = 2


def _templates(index, min_len):
    """Cluster same-length segments that share a fixed frame."""
    by_len = defaultdict(list)
    for seg in index:
        if min_len <= len(seg) <= 12:
            by_len[len(seg)].append(seg)

    masks = defaultdict(set)
    for n, segs in by_len.items():
        for i, a in enumerate(segs):
            for b in segs[i + 1:]:
                fixed = tuple((k, a[k]) for k in range(n) if a[k] == b[k])
                if len(fixed) < MIN_FIXED or n - len(fixed) > MAX_VARIABLE:
                    continue
                # Half the frame must be fixed, or it is not a frame. 是謂▢▢
                # would otherwise arrive as a finding in fifteen chapters.
                if len(fixed) * 2 < n:
                    continue
                masks[(n, fixed)].update((a, b))

    # A longer frame subsumes a shorter one over the same members; keep the
    # most specific, so ▢得一以▢ is not also reported as ▢得一▢▢.
    out = {}
    for (n, fixed), members in masks.items():
        key = frozenset(members)
        if key not in out or len(fixed) > len(out[key][1]):
            out[key] = (n, fixed)
    return {v: sorted(k) for k, v in out.items()}


def _render(n, fixed):
    chars = [SLOT] * n
    for k, c in fixed:
        chars[k] = c
    return "".join(chars)


def show_formulas(chapters, min_len=3, only=None):
    """Every repeated Chinese segment and frame in the book — within a chapter
    and across chapters both.

    check_locks.py keeps its own, narrower index and is deliberately not fed
    from here: that one gates and must never cry wolf, this one searches and
    judges nothing. See CLAUDE.md on why the two are not merged.
    """
    index = _segments(chapters, min_len)
    templates = _templates(index, min_len)

    def spread(occ):
        """(within, across) — repeats inside one chapter, and chapters spanned."""
        chs = defaultdict(int)
        for n, _ in occ:
            chs[n] += 1
        return chs

    rows = []
    for seg, occ in index.items():
        if len(occ) > 1:
            rows.append((seg, spread(occ), "exact", []))
    for (n, fixed), members in templates.items():
        occ = [o for m in members for o in index[m]]
        if len(occ) < 2:
            continue
        rows.append((_render(n, fixed), spread(occ), "frame", members))

    # The finding is CONCENTRATION, not frequency. A frame four times in ch 36
    # and once in ch 65 is that chapter's formula; one appearing once each in
    # fifteen chapters is grammar. So a repeat inside a chapter is only reported
    # when the segment is not also spread all over the book.
    def peak(r):
        return max(r[1].values())

    within = [r for r in rows if peak(r) > 1 and len(r[1]) <= 3]
    grammar = [r for r in rows if peak(r) > 1 and len(r[1]) > 3]
    across = [r for r in rows if peak(r) == 1 and len(r[1]) > 1]
    common = [r for r in across if len(r[1]) > 3] + grammar
    across = [r for r in across if len(r[1]) <= 3]

    def line(seg, chs, kind, members):
        where = ", ".join(f"{n}{f' ×{c}' if c > 1 else ''}"
                          for n, c in sorted(chs.items()))
        tail = ""
        if kind == "frame":
            slots = sorted({m[k] for m in members
                            for k in range(len(m)) if seg[k] == SLOT})
            tail = f"   {DIM}{' · '.join(slots)}{OFF}" if slots else ""
        print(f"  {seg:<14} {DIM}ch{OFF} {where}{tail}")

    def block(title, rs, note=""):
        if not rs:
            return
        print(f"\n  {BOLD}{title}{OFF}  {DIM}({len(rs)}){OFF}"
              + (f"  {DIM}{note}{OFF}" if note else ""))
        for seg, chs, kind, members in sorted(
                rs, key=lambda r: (-max(r[1].values()), r[2] != "exact",
                                   -len(r[0]))):
            line(seg, chs, kind, members)

    if only is not None:
        within = [r for r in within if only in r[1]]
        across = [r for r in across if only in r[1]]
        common = [r for r in common if only in r[1]]

    scope = f"chapter {only}" if only is not None else "the whole text"
    print(f"\n{BOLD}repeated Chinese — {scope}{OFF}")
    print(f"  {DIM}segments of {min_len}+ characters, and the frames they "
          f"share. Nothing here is a verdict.{OFF}")

    block("repeats INSIDE a chapter", within,
          "the parallelism the English most often flattens")
    block("repeats ACROSS 2-3 chapters", across,
          "verbatim Chinese, so the English should match")
    if common:
        print(f"\n  {DIM}in 4+ chapters — grammar, not formula:{OFF}")
        for seg, chs, _, _ in sorted(common, key=lambda r: -len(r[1]))[:16]:
            print(f"    {DIM}{seg:<14} {len(chs)} chapters{OFF}")
    if only is not None and only in chapters:
        print(f"\n  {BOLD}ch {only} — the English, to read against them{OFF}")
        for _, line in chapters[only].verse:
            print(f"    {DIM}│{OFF} {line}")
        print()
    else:
        print(f"\n  {DIM}--formulas N narrows this to one chapter and prints "
              f"its English beside them.{OFF}\n")
    return index


# ------------------------------------------------------------------ commentary

COMMENTATORS = [
    ("wangbi", "王弼 (Wang Bi, d. 249 CE)", "Siku Quanshu, 1782"),
    ("heshanggong", "河上公 (Heshang Gong, Han)", "Song woodblock via Sibu congkan, 1919"),
]


def show_commentary(number, quiet=False):
    """The classical commentators on one chapter, from sources/commentaries/."""
    shown = 0
    for slug, who, ed in COMMENTATORS:
        path = ROOT / "sources" / "commentaries" / slug / f"{number:03d}.md"
        if not path.exists():
            print(f"\n{BOLD}chapter {number}{OFF} — {who}: {DIM}not vendored{OFF}")
            if slug == "wangbi":
                print(f"  {DIM}The Siku transcription is unproofread for 10 chapters "
                      f"(8, 14, 15, 19, 30, 54, 62, 70, 71, 78).{OFF}")
            continue
        text = path.read_text(encoding="utf-8")
        title = ""
        for line in text.split("\n"):
            if line.startswith("chapter_title:"):
                title = line.split('"')[1]
        print(f"\n{BOLD}chapter {number}{OFF} — {who}   {DIM}{ed}{OFF}"
              + (f"   〈{title}〉" if title else ""))
        print()
        for line in text.split("---", 2)[-1].split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("*Commentary"):
                continue
            if line.startswith("**"):
                print(f"  {BOLD}{line.strip('*` ')}{OFF}")
            elif line.startswith(">"):
                print(f"    {line.lstrip('> ')}")
        shown += 1
    print()
    return shown


# ------------------------------------------------------------------- witnesses

def _show_guodian(number):
    """Whether the oldest witness carries this chapter at all.

    An inventory, never a text — see sources/guodian-inventory.yaml for why the
    slips are recorded as facts and never transcribed. Printed above the forks
    because "the oldest witness does not have this chapter" changes how much
    weight the later ones carry, and that is worth knowing before drafting.
    """
    g = load_guodian(number)
    if not g:
        print(f"  {DIM}guodian (~300 BCE): not attested — this chapter rests on "
              f"the silks and later witnesses.{OFF}")
        return
    where = " + ".join(f"bundle {b}" for b in g.bundles)
    extent = "" if g.extent == "complete" else f", {g.extent} only"
    print(f"  {BOLD}guodian (~300 BCE){OFF}: attested — {where}{extent}"
          f"  {DIM}[{', '.join(g.units)}]{OFF}")
    if g.note:
        print(f"      {DIM}{g.note}{OFF}")


def show_witnesses(number, chapters, quiet=False):
    """Where the older witnesses disagree with our base text, for one chapter.

    Run this BEFORE drafting. Ch 21 needed four witnesses fetched from the open
    web to settle one line; Ch 25's throne turned out to be absent from both
    silks. Neither would have been found by reading the base text alone.
    """
    variants = load_variants(number)
    ch = chapters.get(number)

    print(f"\n{BOLD}chapter {number}{OFF} — witnesses", end="")
    if ch and not ch.drafted:
        print(f"  {DIM}[{ch.status}]{OFF}", end="")
    print()

    _show_guodian(number)

    if not variants:
        print(f"  {DIM}no forks recorded. That may mean none exist, or that no "
              f"one has looked yet — sources/variants.yaml is built by hand.{OFF}\n")
        return []

    bearing = [v for v in variants if v.meaning_bearing]
    print(f"  {len(variants)} recorded, {len(bearing)} meaning-bearing\n")

    for v in variants:
        mark = "!" if v.meaning_bearing else "·"
        print(f"  {mark} {BOLD}{v.base}{OFF}   {DIM}in{OFF} {v.line}")
        for w, reading in sorted(v.witnesses.items()):
            arrow = "→" if v.our_call == w else " "
            print(f"      {arrow} {w:<14} {reading}")
        if not v.witnesses:
            print(f"        {DIM}(editorial, not a witness fork){OFF}")
        called = {"base": "we keep the base text", "punctuation": "a punctuation fork",
                  "undecided": "UNDECIDED"}.get(v.our_call, f"we follow {v.our_call}")
        print(f"      {DIM}{called}{OFF}")
        if not quiet and v.note:
            print(f"      {DIM}{v.note}{OFF}")
        if not quiet and v.logged and v.logged != "false":
            print(f"      {DIM}see {v.logged}{OFF}")
        print()
    return variants


# -------------------------------------------------------------------------- cli

def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("term", nargs="?", help="a character or compound, e.g. 明 or 天地")
    p.add_argument("--english", metavar="PHRASE",
                   help="reverse lookup: which chapters use this English, and is it backed")
    p.add_argument("--pairs", nargs=2, metavar=("A", "B"),
                   help="two terms across the book")
    p.add_argument("--formulas", nargs="?", const=0, type=int, metavar="N",
                   help="every repeated Chinese segment and frame, in the whole "
                        "book or (with N) the ones touching chapter N")
    p.add_argument("--witnesses", type=int, metavar="N",
                   help="where the older witnesses disagree with our base text, for chapter N")
    p.add_argument("--record", metavar="TERM",
                   help="what this repo has already decided about a character")
    p.add_argument("--commentary", type=int, metavar="N",
                   help="Wang Bi's commentary on chapter N")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="lines only — omit glosses and surrounding verse")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    chapters = load_chapters()
    terms = load_terms()

    if args.json:
        payload = {}
        if args.term:
            payload["term"] = args.term
            payload["chapters"] = [
                {"chapter": ch.number, "status": ch.status,
                 "lines": [{"chinese": r.chinese, "literal": _plain(r.literal)} for r in rows],
                 "verse": [t.strip() for _, t in ch.verse]}
                for ch, rows in occurrences(args.term, chapters)]
        if args.english:
            backed, unbacked = [], []
            lock = next((t for t in terms if args.english.lower() in t.render.lower()), None)
            for n in sorted(chapters):
                ch = chapters[n]
                if not ch.drafted:
                    continue
                for ln, line in ch.verse:
                    if args.english.lower() in line.lower():
                        has = lock and any(ch.has(c) for c in lock.characters)
                        (backed if has else unbacked).append(
                            {"chapter": ch.number, "line": ln, "text": line.strip()})
            payload["english"] = {"phrase": args.english, "backed": backed,
                                  "unbacked": unbacked}
        if args.witnesses:
            payload["witnesses"] = [
                {"chapter": v.chapter, "line": v.line, "base": v.base,
                 "witnesses": v.witnesses, "meaning_bearing": v.meaning_bearing,
                 "our_call": v.our_call, "note": v.note, "logged": v.logged}
                for v in load_variants(args.witnesses)]
            g = load_guodian(args.witnesses)
            payload["guodian"] = None if not g else {
                "attested": True, "bundles": g.bundles, "extent": g.extent,
                "units": g.units, "note": g.note}
        if args.formulas is not None:
            # One index, not a second copy of it. This path used to rebuild the
            # segment index by hand and had already drifted from the printed
            # one: min_len 4 against 3, and a set of chapters, which cannot
            # express a segment repeating inside a chapter at all.
            index = _segments(chapters, 3)
            payload["formulas"] = {
                s: [{"chapter": n, "row": i} for n, i in occ]
                for s, occ in index.items() if len(occ) > 1}
            payload["frames"] = {
                _render(n, fixed): {"members": members,
                                    "chapters": sorted({c for m in members
                                                        for c, _ in index[m]})}
                for (n, fixed), members in _templates(index, 3).items()}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    did = False
    if args.commentary:
        show_commentary(args.commentary, args.quiet)
        did = True
    if args.witnesses:
        show_witnesses(args.witnesses, chapters, args.quiet)
        did = True
    if args.formulas is not None:
        show_formulas(chapters, only=args.formulas or None)
        did = True
    if args.pairs:
        show_pairs(args.pairs[0], args.pairs[1], chapters, terms, args.quiet)
        did = True
    if args.record:
        show_record(args.record, args.quiet)
        did = True
    if args.english:
        show_english(args.english, chapters, terms, args.quiet)
        did = True
    if args.term:
        show_term(args.term, chapters, terms, args.quiet)
        did = True

    if not did:
        p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
