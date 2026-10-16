#!/usr/bin/env python3
"""
check_counts.py — the counts the documentation claims, against their sources.

A count written into prose is a hand-kept copy of a fact a tool already knows,
and it goes stale on the day the source moves. On 2026-10-15 an audit of the
docs found README.md saying the glossary had 35 entries when it had 55,
CONTRIBUTING.md putting 87 characters outside 說文 (*Shuōwén* — the Han
dictionary) when 35 were, and 32 chapters "still carrying em-dashes" when 8 did.
Every one was true once. Nothing compared them.

The decision (Shalom's, that day) was **trim, then gate**: a count that is
incidental is deleted and the sentence links to the generated index that prints
it (`glossary/INDEX.md`, `process/principles/INDEX.md`). A count worth keeping
stays in the prose, hand-written, and is **marked** — and this checks every
marked count against the real source and prints the true value.

    python3 tools/check_counts.py            # every marked count, every .md file
    python3 tools/check_counts.py --list     # the counts that can be marked, and their values
    python3 tools/check_counts.py --json

**The mark** is an HTML comment directly before the number. It renders as
nothing, so a reader of the Markdown never sees it:

    the analysis of <!-- count: shuowen -->763 of the book's <!-- count: characters -->798 characters

Emphasis between the two is allowed (`<!-- count: x -->**55**`); a number in
words is not — write a gated count in digits. A marked count inside a fenced
code block or an inline code span is not read, because there the comment would
render as text: a count in a code block is a count to trim.

Exits non-zero when a marked count is wrong, names nothing this tool knows, or
marks no number. **A count with no mark is not checked**: marking is opt-in, and
trimming is the default. The docs stay hand-edited, which is what
`edited-or-generated` asks; this only makes their drift unmergeable.

Every value is computed from the authority itself — the database built in
memory exactly as `build_db.py` builds it, the vendored commentaries, and
`check_locks.py`'s own em-dash rule — never from a generated file that could
itself be stale.
"""

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent

# The number may sit inside emphasis; "1,054" reads as 1054.
MARK = re.compile(
    r"<!--\s*count:\s*(?P<name>[^\s>]*)\s*-->"
    r"(?P<lead>[*_]{0,3})(?P<num>\d[\d,]*)?")
FENCE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN = re.compile(r"(`+).*?\1")

# Never read: build products whose prose a generator owns, vendored text, and
# the chapters, which hold verse and not documentation.
# .claude/ is skipped because its skills are symlinks to process/skills/, which
# would read every skill twice.
SKIP_DIRS = {".git", ".claude", ".cache", "chapters", "commentaries", "shuowen",
             "node_modules"}


@dataclass
class Mark:
    path: str
    line: int
    name: str
    claimed: object   # int, or None when the mark is followed by no number


@dataclass
class Finding:
    rule: str
    where: str
    detail: str
    fix: str = ""


# ---- reading the marks -----------------------------------------------------

def marks_in(text, path="<text>"):
    """Every count mark in a Markdown text, skipping code."""
    out, fenced = [], False
    for i, line in enumerate(text.split("\n"), 1):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if fenced:
            continue
        line = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), line)
        for m in MARK.finditer(line):
            num = m.group("num")
            out.append(Mark(path, i, m.group("name"),
                            int(num.replace(",", "")) if num else None))
    return out


def markdown_files(root=ROOT):
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        yield path


# ---- the sources -----------------------------------------------------------

class Sources:
    """What each count is computed from. Built lazily: a file with no marks
    needing the database never builds one."""

    def __init__(self, root=ROOT):
        self.root = root
        self._db = None

    @property
    def db(self):
        if self._db is None:
            import build_db
            self._db = sqlite3.connect(":memory:")
            build_db.build(self._db)
        return self._db

    def one(self, sql, *args):
        return self.db.execute(sql, args).fetchone()[0]

    def lemmas(self, source):
        """(exact, marked) lemma counts in sources/commentaries/<source>/.

        Read the way check_locks.py's unmarked-lemma rule reads them, which is
        what keeps a `*` honest: a lemma is marked exactly when it differs from
        our base text, so counting marks is counting divergences.
        """
        d = self.root / "sources" / "commentaries" / source
        if not d.is_dir():
            raise KeyError(source)
        exact = marked = 0
        for path in sorted(d.glob("[0-9]*.md")):
            for line in path.read_text(encoding="utf-8").split("\n"):
                m = re.match(r"^\*\*(.+?)\*\*(\s*`\*`)?\s*$", line)
                if m:
                    if m.group(2):
                        marked += 1
                    else:
                        exact += 1
        return exact, marked

    def comment_blocks(self, source):
        d = self.root / "sources" / "commentaries" / source
        if not d.is_dir():
            raise KeyError(source)
        return sum(1 for path in d.glob("[0-9]*.md")
                   for line in path.read_text(encoding="utf-8").split("\n")
                   if line.startswith("> "))

    def dash_chapters(self):
        """Chapters with a dash in the verse — by check_locks.py's own rule, so
        the count and the inventory it summarises cannot disagree."""
        import check_locks
        from lib.corpus import load_chapters
        return len({f.chapter for f in check_locks.rule_em_dash(
            list(load_chapters().values()))})


# name -> (what it counts, how). A name may take one argument after a colon:
# `gloss:word`, `lemmas-exact:wangbi`.
COUNTS = {
    "characters": (
        "distinct characters in the book",
        lambda s, _: s.one("SELECT count(*) FROM character")),
    "shuowen": (
        "characters with a 說文 (Shuōwén) entry matched to them",
        lambda s, _: s.one("SELECT count(DISTINCT char) FROM shuowen")),
    "shuowen-missing": (
        "characters with no 說文 (Shuōwén) entry",
        lambda s, _: s.one("SELECT count(*) FROM character WHERE char NOT IN "
                           "(SELECT char FROM shuowen)")),
    "variants": (
        "forks in the witness apparatus (distinct variant groups in sources/variants.yaml)",
        lambda s, _: s.one("SELECT count(DISTINCT variant_group) FROM variant")),
    "variants-meaning": (
        "forks in the apparatus marked meaning-bearing",
        lambda s, _: s.one("SELECT count(DISTINCT variant_group) FROM variant "
                           "WHERE meaning_bearing")),
    "guodian-chapters": (
        "chapters the Guodian slips carry (sources/guodian-inventory.yaml)",
        lambda s, _: s.one("SELECT count(*) FROM chapter WHERE guodian_attested")),
    "gloss": (
        "characters whose gloss_source is <arg> (word, apparatus, grammar, …)",
        lambda s, a: s.one("SELECT count(*) FROM character WHERE gloss_source = ?", a)),
    "gloss-3plus": (
        "characters whose gloss_source is <arg> and that occur three or more times",
        lambda s, a: s.one("SELECT count(*) FROM character "
                           "WHERE gloss_source = ? AND total >= 3", a)),
    "dash-chapters": (
        "chapters with a dash in the verse (check_locks.py --rule em-dash)",
        lambda s, _: s.dash_chapters()),
    "lemmas": (
        "lemma lines vendored from commentary <arg>",
        lambda s, a: sum(s.lemmas(a))),
    "lemmas-exact": (
        "lemmas from commentary <arg> that match our base text",
        lambda s, a: s.lemmas(a)[0]),
    "lemmas-variant": (
        "lemmas from commentary <arg> marked `*`, differing from our base text",
        lambda s, a: s.lemmas(a)[1]),
    "comment-blocks": (
        "commentary blocks vendored from commentary <arg>",
        lambda s, a: s.comment_blocks(a)),
}

TAKES_ARG = {"gloss", "gloss-3plus", "lemmas", "lemmas-exact", "lemmas-variant",
             "comment-blocks"}


def value(sources, name):
    """The true value for a mark's name, or None when the name means nothing."""
    base, _, arg = name.partition(":")
    if base not in COUNTS or bool(arg) != (base in TAKES_ARG):
        return None
    try:
        return COUNTS[base][1](sources, arg or None)
    except KeyError:
        return None


# ---- the check -------------------------------------------------------------

def check(marks, sources):
    out, cache = [], {}
    for m in marks:
        where = f"{m.path}:{m.line}"
        if m.name not in cache:
            cache[m.name] = value(sources, m.name)
        actual = cache[m.name]
        if actual is None:
            out.append(Finding(
                "unknown-count", where,
                f'the mark names "{m.name}", which this tool cannot compute',
                "use a name from: python3 tools/check_counts.py --list"))
        elif m.claimed is None:
            out.append(Finding(
                "no-number", where,
                f'the "{m.name}" mark is not followed by a number in digits',
                f"put the number straight after the mark: "
                f"<!-- count: {m.name} -->{actual}"))
        elif m.claimed != actual:
            out.append(Finding(
                "stale-count", where,
                f'says {m.claimed}; {m.name} is {actual}',
                f"write {actual} — or, if the count is incidental, delete it "
                f"and point at the index that prints it"))
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--list", action="store_true",
                   help="print every count that can be marked, with its value")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    sources = Sources()

    if args.list:
        args_for = {
            "gloss": [r[0] for r in sources.db.execute(
                "SELECT DISTINCT gloss_source FROM character ORDER BY 1")],
            "commentary": sorted(d.name for d in
                                 (ROOT / "sources" / "commentaries").iterdir()
                                 if d.is_dir()),
        }
        for name, (what, _) in COUNTS.items():
            if name not in TAKES_ARG:
                print(f"  {name:28} {value(sources, name):>5}  {what}")
                continue
            print(f"  {name + ':<arg>':28}        {what}")
            for a in args_for["gloss" if name.startswith("gloss") else "commentary"]:
                print(f"    {name + ':' + a:26} {value(sources, name + ':' + a):>5}")
        return 0

    marks = []
    for path in markdown_files():
        rel = str(path.relative_to(ROOT))
        marks += marks_in(path.read_text(encoding="utf-8"), rel)
    findings = check(marks, sources)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], ensure_ascii=False, indent=2))
        return 1 if findings else 0

    files = len({m.path for m in marks})
    print(f"\n\033[1mcounts in the docs\033[0m — {len(marks)} marked, in {files} files")
    for f in findings:
        print(f"\n  \033[31m✗\033[0m  {f.where}  {f.rule}")
        print(f"       {f.detail}")
        if f.fix:
            print(f"       \033[2m→ {f.fix}\033[0m")
    print("\n" + "─" * 72)
    print(f"{len(findings)} wrong" if findings else "every marked count is true")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
