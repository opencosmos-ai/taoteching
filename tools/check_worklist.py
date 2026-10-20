#!/usr/bin/env python3
"""
check_worklist.py — WORKLIST.md against itself.

Four hand-kept lists in this repository went stale in three days, and a person
found every one of them by reading. The pattern was always the same: a fact
written down twice, one copy updated. This checks the copies that remain inside
`WORKLIST.md` against the table that is their source.

    python3 tools/check_worklist.py
    python3 tools/check_worklist.py --json

Exits non-zero when a rule fires. Every rule here enforces something the file
already says about itself; none of them has an opinion about the translation.

What it checks:

  pass-chapters    a pass row's Ch column is the union of the Ch values on the
                   item rows carrying that pass letter
  chapter-row      a per-chapter row (D16) is not marked done while a finding
                   row on that chapter is still open
  chapter-cover    every chapter a finding row names has a per-chapter row
  closed-pass      no pass is marked done while a row tagged to it is open
  tally            the "N item rows: ..." line matches the table
  chapter-tally    the Progress line's three restatements of the per-chapter
                   rows — a figure, a list, and a spelled-out repeat — match
                   those rows
  pass-exists      every pass letter used by an item row has a pass row
  duplicate-id     no row id appears twice

And `WORKLIST-CLOSED.md` against it, since the file says a row that closes
leaves it:

  closed-row       no row in WORKLIST.md is marked done
  archived-id      no id stands in both files, so a reopened row moves back
                   rather than being copied, and a new row cannot take an id
                   that a chapter note already cites for something closed
  open-archived    every row in WORKLIST-CLOSED.md is marked done

It does not check the prose sections. They carry reasoning, which cannot be
diffed against a table, and duplicating a *decision* is not the failure mode —
duplicating a *list* is.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKLIST = ROOT / "WORKLIST.md"
CLOSED = ROOT / "WORKLIST-CLOSED.md"

DONE, PART, OPEN, DEFERRED = "✅", "🔶", "⬜", "⏸"
STATUSES = {DONE, PART, OPEN, DEFERRED}

PASS_ID = re.compile(r"^P[A-G0]$")
ITEM_ID = re.compile(r"^(T\d+-\d+|R\d+|G\d+|D\d+)$")

# A per-chapter work-unit row: D16 is "the ch 16 rewrite", as against T1-6,
# which is "the 守 finding, which happens to be at ch 16". Two granularities,
# deliberately: findings are what gets argued, chapters are what gets done.
CHAPTER_ID = re.compile(r"^D(\d+)$")

# The Progress line spells its chapter count out a second time in words, so the
# checker has to read words. Only the range this file can reach is covered; an
# unknown word is left alone rather than guessed at, since a wrong reading here
# would report drift that is not there.
NUMBER_WORDS = {
    w: i for i, w in enumerate(
        "zero one two three four five six seven eight nine ten eleven twelve "
        "thirteen fourteen fifteen sixteen seventeen eighteen nineteen "
        "twenty".split())
}
NUMBER_WORDS.update({"thirty": 30, "forty": 40, "fifty": 50,
                     "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90})


def word_to_int(word):
    """'twenty-two' -> 22. None when any part is outside the table above."""
    total = 0
    for part in word.lower().split("-"):
        if part not in NUMBER_WORDS:
            return None
        total += NUMBER_WORDS[part]
    return total


@dataclass
class Finding:
    rule: str
    detail: str
    fix: str = ""


@dataclass
class Row:
    id: str
    status: str
    item: str
    chapters: frozenset
    pass_: str
    line_no: int


def _cells(line):
    """A markdown table row's cells, stripped. Leading/trailing pipes dropped."""
    parts = line.split("|")
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [c.strip() for c in parts]


ROW_REF = re.compile(r"\b(?:T\d+|R\d+|G\d+)\b")


def _chapters(cell):
    """
    Chapter numbers from a Ch cell.

    Returns nothing for a cell that does not list chapters at all: prose
    ("book-wide"), a dash, or a *pointer* at other rows ("T3-1 · T2-9→15").
    A pointer cell is not a stale list — it is a row declining to keep one,
    which is the behaviour this tool exists to encourage — so it is never
    checked against the union. Only a cell that actually enumerates chapters
    makes a claim that can be wrong.
    """
    if not cell or cell in {"—", "-"} or ROW_REF.search(cell):
        return frozenset()
    cell = re.sub(r"\+\s*\d+\s*more", " ", cell)   # "5 16 17 18 25 + 26 more"
    return frozenset(int(n) for n in re.findall(r"\b(\d{1,2})\b", cell)
                     if 1 <= int(n) <= 81)


def parse(text):
    """Every id'd row of the main table, in file order."""
    rows = []
    for i, line in enumerate(text.split("\n"), 1):
        if not line.startswith("|"):
            continue
        c = _cells(line)
        if len(c) < 5:
            continue
        rid, status = c[0], c[1]
        if not (PASS_ID.match(rid) or ITEM_ID.match(rid)):
            continue
        if status not in STATUSES:
            continue
        rows.append(Row(rid, status, c[2], _chapters(c[3]), c[4], i))
    return rows


def check(text):
    rows = parse(text)
    passes = {r.id: r for r in rows if PASS_ID.match(r.id)}
    items = [r for r in rows if not PASS_ID.match(r.id)]
    out = []

    seen = {}
    for r in rows:
        if r.id in seen:
            out.append(Finding("duplicate-id",
                               f"{r.id} appears on lines {seen[r.id]} and {r.line_no}",
                               "one row per id"))
        seen[r.id] = r.line_no

    by_pass = defaultdict(list)
    for r in items:
        by_pass[r.pass_].append(r)

    letters = {p.pass_ for p in passes.values()}
    for letter in sorted(by_pass):
        if letter not in letters and letter != "ongoing":
            out.append(Finding("pass-exists",
                               f"item rows are tagged pass {letter!r}, "
                               f"but no pass row carries it",
                               "add the pass row, or retag the items"))

    for pid, prow in sorted(passes.items()):
        mine = by_pass.get(prow.pass_, [])
        if not mine:
            continue

        union = frozenset().union(*(r.chapters for r in mine))
        # A pass row may legitimately say "book-wide" or point at rows instead
        # of listing chapters; only a row that *lists* chapters is checked.
        if prow.chapters and prow.chapters != union:
            missing = sorted(union - prow.chapters)
            extra = sorted(prow.chapters - union)
            bits = []
            if missing:
                bits.append("missing " + " ".join(map(str, missing)))
            if extra:
                bits.append("lists " + " ".join(map(str, extra))
                            + " which no row claims")
            out.append(Finding(
                "pass-chapters",
                f"{pid} (line {prow.line_no}): " + "; ".join(bits),
                "Ch is the union of the rows tagged to this pass — recompute it: "
                + " ".join(map(str, sorted(union)))))

        stragglers = [r for r in mine if r.status in {OPEN, PART}]
        if prow.status == DONE and stragglers:
            names = ", ".join(f"{r.id} ({r.status})" for r in stragglers[:6])
            out.append(Finding(
                "closed-pass",
                f"{pid} is marked done, but {len(stragglers)} row(s) tagged "
                f"pass {prow.pass_} are not: {names}",
                "close the rows, retag them to another pass, or reopen the pass"))

    # ---- per-chapter rows ------------------------------------------------
    # A D<n> row is a work-unit; the findings that fill it are the other rows
    # tagged to the SAME pass whose Ch names n. Its status is therefore not an
    # independent fact, and it is the copy that would otherwise go stale.
    #
    # The pass filter is load-bearing. Ch 13 carries T1-10 and T3-7 in pass D
    # and 身 (T2-1) in pass E; only the first two are the ch 13 rewrite, and a
    # rule that counted both could never let D13 close.
    chapter_rows = {}
    for r in items:
        m = CHAPTER_ID.match(r.id)
        if m:
            chapter_rows[int(m.group(1))] = r

    chaptered_passes = {r.pass_ for r in chapter_rows.values()}

    findings_by_ch = defaultdict(list)
    for r in items:
        if CHAPTER_ID.match(r.id) or r.pass_ not in chaptered_passes:
            continue
        for n in r.chapters:
            findings_by_ch[n].append(r)

    for n, crow in sorted(chapter_rows.items()):
        mine = [r for r in findings_by_ch.get(n, []) if r.pass_ == crow.pass_]
        unfinished = [r for r in mine if r.status in {OPEN, PART}]
        if crow.status == DONE and unfinished:
            names = ", ".join(f"{r.id} ({r.status})" for r in unfinished[:6])
            out.append(Finding(
                "chapter-row",
                f"{crow.id} is marked done, but {len(unfinished)} finding "
                f"row(s) on ch {n} in pass {crow.pass_} are not: {names}",
                "close the findings, or reopen the chapter row"))

    for n, rs in sorted(findings_by_ch.items()):
        if n in chapter_rows:
            continue
        ids = " ".join(sorted(r.id for r in rs))
        out.append(Finding(
            "chapter-cover",
            f"ch {n} is named by {ids} in pass "
            f"{sorted({r.pass_ for r in rs})[0]}, but has no per-chapter row",
            f"add a D{n} row, or retag those findings"))

    counts = defaultdict(int)
    for r in items:
        counts[r.status] += 1
    m = re.search(
        r"\*\*(\d+) item rows: (\d+) open · (\d+) done · (\d+) part done · "
        r"(\d+) deferred\.\*\*", text)
    if m:
        claimed = tuple(int(g) for g in m.groups())
        actual = (len(items), counts[OPEN], counts[DONE], counts[PART],
                  counts[DEFERRED])
        if claimed != actual:
            out.append(Finding(
                "tally",
                f"header says {claimed}, table has {actual} "
                f"(total, open, done, part, deferred)",
                f"**{actual[0]} item rows: {actual[1]} open · {actual[2]} done "
                f"· {actual[3]} part done · {actual[4]} deferred.**"))

    # ---- the Progress line's prose counts ---------------------------------
    # `tally` gates the item-row header. The sentence above it restates the
    # per-chapter rows three more times — "11 of 19 chapters", a list of the
    # done chapter numbers, and "eleven of the nineteen" — and every one of
    # them is a copy. The chapter count in this file drifted four times before
    # this rule existed, twice inside a single session, so each copy is checked
    # against chapter_rows rather than against the others.
    #
    # A copy that is simply absent is not a finding: removing a hand-kept count
    # is a legitimate fix, and was the fix used before this rule was written.
    prog = next((ln for ln in text.splitlines()
                 if ln.startswith("**Progress:")), None)
    if prog and chapter_rows:
        done_ch = sorted(n for n, r in chapter_rows.items()
                         if r.status == DONE)
        total_ch = len(chapter_rows)

        m = re.search(r"(\d+) of (\d+) chapters", prog)
        if m and (int(m.group(1)), int(m.group(2))) != (len(done_ch), total_ch):
            out.append(Finding(
                "chapter-tally",
                f"the Progress line says {m.group(1)} of {m.group(2)} "
                f"chapters, but the per-chapter rows are "
                f"{len(done_ch)} of {total_ch}",
                f"{len(done_ch)} of {total_ch} chapters"))

        m = re.search(r"Done: \*\*([^*]+)\*\*", prog)
        if m:
            listed = [int(x) for x in re.findall(r"\d+", m.group(1))]
            if listed != done_ch:
                out.append(Finding(
                    "chapter-tally",
                    "the Progress line's Done list is "
                    f"{listed or '(empty)'}, but the chapter rows marked done "
                    f"are {done_ch or '(none)'}",
                    "Done: **" + " · ".join(str(n) for n in done_ch) + "**"))

        # "eleven of the nineteen" sits mid-sentence, so there is no anchor
        # to hang it on. The number table is the filter instead: every "X of
        # the Y" in the line is considered, and only the ones where BOTH sides
        # are number words are checked. Ordinary prose cannot reach the test.
        for m in re.finditer(r"\b([a-z]+(?:-[a-z]+)?) of the "
                             r"([a-z]+(?:-[a-z]+)?)\b", prog):
            spelled = (word_to_int(m.group(1)), word_to_int(m.group(2)))
            if None in spelled or spelled == (len(done_ch), total_ch):
                continue
            out.append(Finding(
                "chapter-tally",
                f"the Progress line spells out \"{m.group(1)} of the "
                f"{m.group(2)}\", but the chapter rows are "
                f"{len(done_ch)} of {total_ch}",
                "spell the figure above it, or drop the repeat"))
    return out, rows


def check_split(text, closed_text):
    """
    The forward file against the closed one.

    The worklist said for two months that a closed row leaves it, and 96
    closed rows were still in it when it was split on 2026-10-20, four of them
    restating findings their own detail sections had marked open. A policy
    written in prose did not hold, so it is held here.
    """
    live, closed = parse(text), parse(closed_text)
    out = []
    for r in live:
        if r.status == DONE:
            out.append(Finding(
                "closed-row",
                f"{r.id} (line {r.line_no}) is marked done but is still in "
                f"WORKLIST.md",
                "move the row, word for word, to WORKLIST-CLOSED.md → "
                "*Closed rows*, with any prose that described it"))
    archived = {r.id: r for r in closed}
    for r in live:
        if r.id in archived:
            out.append(Finding(
                "archived-id",
                f"{r.id} is in WORKLIST.md (line {r.line_no}) and in "
                f"WORKLIST-CLOSED.md (line {archived[r.id].line_no})",
                "a reopened row moves back and leaves the closed file; a new "
                "row takes an unused id"))
    for r in closed:
        if r.status != DONE:
            out.append(Finding(
                "open-archived",
                f"{r.id} (WORKLIST-CLOSED.md line {r.line_no}) is marked "
                f"{r.status}, not done",
                "an open row belongs in WORKLIST.md"))
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    text = WORKLIST.read_text(encoding="utf-8")
    findings, rows = check(text)
    if CLOSED.exists():
        findings += check_split(text, CLOSED.read_text(encoding="utf-8"))

    if args.json:
        print(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
        return 1 if findings else 0

    items = [r for r in rows if not PASS_ID.match(r.id)]
    print(f"\n\033[1mWORKLIST.md\033[0m — {len(items)} item rows, "
          f"{len(rows) - len(items)} passes")
    for f in findings:
        print(f"\n  \033[31m✗\033[0m  {f.rule}")
        print(f"       {f.detail}")
        if f.fix:
            print(f"       \033[2m→ {f.fix}\033[0m")
    print("\n" + "─" * 72)
    print(f"{len(findings)} inconsistenc{'y' if len(findings) == 1 else 'ies'}"
          if findings else "consistent with itself")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
