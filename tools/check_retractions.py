#!/usr/bin/env python3
"""
check_retractions.py — no copy of a withdrawn claim survives.

A correction is made in one place, and the claim it corrects has usually been
copied into several. On 2026-08-20 the Ch 25 apparatus was corrected: every
excavated witness reads 王 (*wáng* — king), and 人 (*rén* — human) is a
transmitted reading. Two months later the withdrawn claim still stood as fact
in eleven files, among them `CLAUDE.md`, the `chapter-review` skill and a
principle: the three things an AI session loads first. Nothing looked for the
copies, so only reading found them.

So a correction has two halves: fix the place you found, and add the withdrawn
claim to `process/retractions.yaml`. This then fails the build on every copy,
in every file, today and later. It is a glossary entry's `forbidden:` list
applied to facts instead of renderings.

    python3 tools/check_retractions.py            # every copy, every file
    python3 tools/check_retractions.py --list     # the register
    python3 tools/check_retractions.py --json

What is not a copy, and is never flagged:
- `CHANGELOG.md`, which is dated history;
- a line that announces its own correction: *Corrected*, *withdrawn*,
  *superseded*, *retracted*, *once said*, *formerly*, *(was*, `~~`, or ⚠;
- a Markdown section that carries a ⚠ banner, from its heading down to the next
  heading of the same level or higher (`DISCOVERIES.md` §1 and §4);
- the paths an entry names in `allow:`.

Exits non-zero when a copy survives, or when the register itself is malformed:
an entry missing a field, a duplicate id, a date that is not a date, or a `see:`
that points at a file or heading that does not exist.

It is a separate tool rather than a `check_locks.py` rule for the reason
`check_counts.py` is: it judges no rendering, so it has no evidence gate to pass
and no waiver to honour.
"""

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "process" / "retractions.yaml"

# Vendored or generated: a copy there is fixed upstream, in the file the build
# read, and is reported there.
SKIP_DIRS = {".git", ".cache", "node_modules", "data", "commentaries", "shuowen"}
SUFFIXES = {".md", ".yaml", ".yml", ".cff"}
HISTORY = {"CHANGELOG.md"}

# A line that says it is a correction is the correction, not a copy.
SELF_CORRECTING = re.compile(
    r"correct(ed|ion)|withdrawn|superseded|retracted|once said|once cited|formerly"
    r"|\(was\b|~~|⚠", re.I)
HEADING = re.compile(r"^(#{1,6})\s")
REQUIRED = ("id", "retracted", "claim", "match", "correction", "see")


@dataclass
class Retraction:
    id: str
    retracted: str
    claim: str
    match: list
    correction: str
    see: str
    allow: list = field(default_factory=list)

    def allows(self, rel):
        return any(fnmatch.fnmatch(rel, pat) for pat in self.allow)


@dataclass
class Copy:
    path: str
    line: int
    id: str
    phrase: str
    text: str
    correction: str
    see: str


# ---------------------------------------------------------------- the register

def _inline_list(val, where):
    val = val.strip()
    if not (val.startswith("[") and val.endswith("]")):
        raise ValueError(f"{where}: expected an inline list, got {val!r}")
    body = val[1:-1].strip()
    return [s for s in re.findall(r'"((?:[^"\\]|\\.)*)"', body)] if body else []


def parse(text, where="process/retractions.yaml"):
    """The register, read by a strict hand parser. A shape it cannot read is an
    error, never an empty list: `parse_frontmatter` once dropped a lock on the
    floor for seven weeks by reading an unexpected shape as nothing."""
    entries, cur, key = [], None, None
    for n, raw in enumerate(text.split("\n"), 1):
        if raw.lstrip().startswith("#") or not raw.strip():
            continue
        if raw.startswith("- "):
            if cur is not None:
                entries.append(cur)
            cur, raw = {}, "  " + raw[2:]
        if cur is None:
            raise ValueError(f"{where}:{n}: content before the first entry")
        m = re.match(r"^  (\w+):\s*(.*)$", raw)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key in cur:
                raise ValueError(f"{where}:{n}: `{key}` given twice")
            if key in ("match", "allow"):
                cur[key] = _inline_list(val, f"{where}:{n}")
            elif val == ">":
                cur[key] = ""
            else:
                cur[key] = val.strip('"')
        elif key and raw.startswith("    "):
            cur[key] = (cur.get(key, "") + " " + raw.strip()).strip()
        else:
            raise ValueError(f"{where}:{n}: cannot read {raw.strip()!r}")
    if cur is not None:
        entries.append(cur)

    out, seen = [], set()
    for e in entries:
        missing = [k for k in REQUIRED if not e.get(k)]
        if missing:
            raise ValueError(f"{where}: {e.get('id', '<no id>')} is missing {', '.join(missing)}")
        if e["id"] in seen:
            raise ValueError(f"{where}: id {e['id']!r} is used twice")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", e["retracted"]):
            raise ValueError(f"{where}: {e['id']}: retracted must be YYYY-MM-DD")
        seen.add(e["id"])
        out.append(Retraction(**{k: e.get(k, []) if k == "allow" else e[k]
                                 for k in REQUIRED + ("allow",)}))
    return out


def load(path=REGISTER):
    return parse(path.read_text(encoding="utf-8"), str(path.relative_to(ROOT)))


def broken_see(entries, root=ROOT):
    """Every `see:` must point at a file that exists, and at a heading in it."""
    from build_principles import headings_in
    out = []
    for e in entries:
        path, _, anchor = e.see.partition("#")
        target = root / path
        if not target.exists():
            out.append(f"{e.id}: see {e.see!r} — no such file")
        elif anchor and anchor not in headings_in(target):
            out.append(f"{e.id}: see {e.see!r} — no such heading in {path}")
    return out


# ---------------------------------------------------------------- the search

def files(root=ROOT):
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if (path.is_file() and path.suffix in SUFFIXES
                and not any(part in SKIP_DIRS for part in rel.parts[:-1])
                and path != REGISTER and rel.as_posix() not in HISTORY):
            yield path


def banner_lines(lines):
    """Line numbers inside a Markdown section that carries a ⚠ banner.

    The banner has to be the section's own: in its opening text, before its
    first subheading. It then covers the section and its subsections. A ⚠ deep
    inside one subsection says nothing about the others, and counting it would
    exempt hundreds of lines of notes/translation.md that it never mentions.
    """
    exempt, n = set(), len(lines)
    for i, line in enumerate(lines):
        h = HEADING.match(line)
        if not h:
            continue
        level, lead_end, end = len(h.group(1)), n, n
        for j in range(i + 1, n):
            h2 = HEADING.match(lines[j])
            if h2 and lead_end == n:
                lead_end = j
            if h2 and len(h2.group(1)) <= level:
                end = j
                break
        if any("⚠" in lines[k] for k in range(i, lead_end)):
            exempt.update(range(i, end))
    return exempt


def copies_in(text, rel, entries):
    lines = text.split("\n")
    exempt = banner_lines(lines) if rel.endswith(".md") else set()
    found = []
    for e in entries:
        if e.allows(rel):
            continue
        for i, line in enumerate(lines):
            if i in exempt or SELF_CORRECTING.search(line):
                continue
            low = line.lower()
            for phrase in e.match:
                if phrase.lower() in low:
                    found.append(Copy(rel, i + 1, e.id, phrase, line.strip(),
                                      " ".join(e.correction.split()), e.see))
                    break
    return found


def check(entries, root=ROOT):
    out = []
    for path in files(root):
        rel = path.relative_to(root).as_posix()
        out += copies_in(path.read_text(encoding="utf-8", errors="replace"), rel, entries)
    return out


# ---------------------------------------------------------------- report

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--list", action="store_true", help="print the register")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    try:
        entries = load()
    except ValueError as err:
        print(f"process/retractions.yaml cannot be read: {err}")
        return 1

    if args.list:
        for e in entries:
            print(f"{e.id}  (retracted {e.retracted})\n  claim:      {' '.join(e.claim.split())}"
                  f"\n  correction: {' '.join(e.correction.split())}\n  see:        {e.see}\n")
        return 0

    broken, found = broken_see(entries), check(entries)
    if args.json:
        print(json.dumps({"broken_see": broken, "copies": [asdict(c) for c in found]},
                         ensure_ascii=False, indent=2))
        return 1 if broken or found else 0

    print(f"withdrawn claims — {len(entries)} in the register")
    for b in broken:
        print(f"  ✗  {b}")
    for c in found:
        print(f"\n  ✗  {c.path}:{c.line}  [{c.id}]  matches {c.phrase!r}\n"
              f"       {c.text[:160]}\n       true: {c.correction}\n       see:  {c.see}")
    print("─" * 72)
    if broken or found:
        print(f"{len(found)} surviving cop{'y' if len(found) == 1 else 'ies'}"
              f"{f', {len(broken)} broken see' if broken else ''}")
        return 1
    print("no withdrawn claim survives")
    return 0


if __name__ == "__main__":
    sys.exit(main())
