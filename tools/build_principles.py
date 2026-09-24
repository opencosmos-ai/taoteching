#!/usr/bin/env python3
"""
build_principles.py — regenerate process/principles/INDEX.md and principles.yaml
from the YAML frontmatter of every process/principles/*.md entry.

The frontmatter in each entry is the single source of truth. This derives two
things from it, exactly as build_index.py does for the glossary:

  process/principles/INDEX.md    a human table: trigger -> rule -> entry
  process/principles.yaml        the machine-readable list, loaded by the skills

Run after adding or changing a principle:

    python3 tools/build_principles.py

It also VERIFIES every `evidence:` anchor, because a principle whose evidence
link has rotted is worse than one with no link at all: it looks checked.
An unresolvable anchor is an error and exits non-zero.

And it verifies STRUCTURE, because a principle that is well argued and
reached by nobody does not govern anything. Every entry must carry the
standard sections in order (see README, *The shape of an entry*); must say
in *How it is implemented* where the rule runs, naming its `check:` tool if
it has one; and must apply to at least one kind of work that a skill or
CLAUDE.md actually loads with `--applies`. An entry that fails any of these
is an error.

    python3 tools/build_principles.py --check            verify only, write nothing
    python3 tools/build_principles.py --applies drafting  what fires on this work
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import parse_frontmatter  # noqa: E402  — the one frontmatter reader

ROOT = Path(__file__).resolve().parent.parent
PRINCIPLES = ROOT / "process" / "principles"

STATUSES = ("provisional", "active", "superseded")
SCOPES = ("drafting", "glossary", "notes", "tooling", "process")
REQUIRED = ("id", "title", "status", "since", "trigger", "applies")

BADGE = {"active": "✅", "provisional": "🔶", "superseded": "⊘"}

# The standard sections, in order. Other sections may sit between them
# (imported-register's "The three tests"), but these five are required.
SECTIONS = (
    "Why this holds",
    "Why this principle exists",
    "How it is implemented",
    "Where it does not fire",
    "What it obliges",
)

# The files that load principles into work, via `build_principles.py --applies`.
# A scope nobody loads is a principle nobody meets.
LOADERS = ("CLAUDE.md", "process/method.md", "process/skills")


def slug(heading):
    """GitHub's heading-anchor slug: lowercase, drop punctuation, spaces to hyphens.

    CJK characters survive, which is why the anchors in this repo are legible
    at all. Kept deliberately close to GitHub's own rule rather than tidied,
    because the anchors have to resolve on GitHub, not here.
    """
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def headings_in(path):
    """Every heading anchor a markdown file offers."""
    if not path.exists():
        return None
    out = set()
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        if m:
            out.add(slug(m.group(1)))
    return out


def load():
    entries, problems = [], []
    for path in sorted(PRINCIPLES.glob("*.md")):
        if path.name in ("README.md", "INDEX.md"):
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            problems.append(f"{path.name}: no frontmatter")
            continue
        fm["file"] = path.name
        for field in REQUIRED:
            if not fm.get(field):
                problems.append(f"{path.name}: missing required field `{field}`")
        if fm.get("status") and fm["status"] not in STATUSES:
            problems.append(f"{path.name}: status `{fm['status']}` is not one of {'/'.join(STATUSES)}")
        for scope in fm.get("applies", []):
            if scope not in SCOPES:
                problems.append(f"{path.name}: applies `{scope}` is not one of {'/'.join(SCOPES)}")
        if fm.get("id") and fm["id"] != path.stem:
            problems.append(f"{path.name}: id `{fm['id']}` does not match the filename")
        # The threshold: one case is an observation, two is a principle.
        if fm.get("status") == "active" and len(fm.get("evidence", [])) < 2:
            problems.append(
                f"{path.name}: status is `active` with "
                f"{len(fm.get('evidence', []))} case(s) in `evidence:` — "
                f"needs two, or mark it `provisional` (see README, *The threshold*)"
            )
        entries.append(fm)
    return entries, problems


def verify_anchors(entries):
    """Every evidence link must resolve to a real heading in a real file."""
    problems, cache = [], {}
    for e in entries:
        for ref in e.get("evidence", []):
            if "#" not in ref:
                problems.append(f"{e['file']}: evidence `{ref}` has no #anchor")
                continue
            rel, anchor = ref.split("#", 1)
            if rel not in cache:
                cache[rel] = headings_in(ROOT / rel)
            if cache[rel] is None:
                problems.append(f"{e['file']}: evidence file `{rel}` does not exist")
            elif anchor not in cache[rel]:
                problems.append(f"{e['file']}: anchor `#{anchor}` not found in {rel}")
    return problems


def loaded_scopes():
    """Every `--applies <scope>` that some operational file actually runs."""
    found = set()
    for spec in LOADERS:
        path = ROOT / spec
        files = sorted(path.rglob("*.md")) if path.is_dir() else [path]
        for f in files:
            if not f.exists() or "principle-entry" in f.parts:
                continue   # principle-entry lists scopes as documentation, not work
            for line in f.read_text(encoding="utf-8").splitlines():
                code = line.split("#", 1)[0] if line.lstrip().startswith("python3") else line
                found.update(re.findall(r"--applies\s+([a-z]+)", code))
    return found


def verify_structure(entries):
    """The shape a principle needs in order to be read, and in order to run."""
    problems = []
    loaded = loaded_scopes()
    for e in entries:
        if e.get("status") == "superseded":
            continue
        text = (PRINCIPLES / e["file"]).read_text(encoding="utf-8")
        body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
        for lead in ("**The rule.**", "**When it fires.**"):
            if lead not in body:
                problems.append(f"{e['file']}: no `{lead}` paragraph at the top")
        heads = [h.strip() for h in re.findall(r"^## (.+)$", body, re.M)]
        pos = []
        for want in SECTIONS:
            hit = next((i for i, h in enumerate(heads) if h.lower().startswith(want.lower())), None)
            if hit is None:
                problems.append(f"{e['file']}: missing section `## {want}`")
            else:
                pos.append(hit)
        if pos and pos != sorted(pos):
            problems.append(f"{e['file']}: sections out of order — expected "
                            f"{' → '.join(SECTIONS)}")
        m = re.search(r"^## How it is implemented\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
        impl = m.group(1) if m else ""
        tool = (e.get("check") or "none").strip()
        if m and len(impl.split()) < 12:
            problems.append(f"{e['file']}: `How it is implemented` is too thin to say where the rule runs")
        if tool != "none" and m and tool.split()[0] not in impl:
            problems.append(f"{e['file']}: `check: {tool}` is not named in `How it is implemented`")
        if not set(e.get("applies", [])) & loaded:
            problems.append(f"{e['file']}: applies {e.get('applies')} — no skill or CLAUDE.md "
                            f"loads any of these with `--applies`, so nobody meets this rule "
                            f"(loaded: {', '.join(sorted(loaded))})")
    return problems


def write_index(entries):
    live = [e for e in entries if e.get("status") != "superseded"]
    gone = [e for e in entries if e.get("status") == "superseded"]

    out = [
        "# Principles — index",
        "",
        "*Generated by `tools/build_principles.py` from the frontmatter of each entry.*",
        "**Never edit this file by hand.** Edit the entry, then rebuild.",
        "",
        f"**{len(live)} in force** — "
        f"{sum(1 for e in live if e.get('status') == 'active')} active, "
        f"{sum(1 for e in live if e.get('status') == 'provisional')} provisional"
        + (f" · {len(gone)} superseded." if gone else "."),
        "",
        "*A principle fires on its **trigger**. Read that column first.*",
        "",
        "| | When it fires | The rule | Applies to | Enforced by |",
        "|---|---|---|---|---|",
    ]
    for e in sorted(live, key=lambda x: (x.get("status") != "active", x.get("id", ""))):
        check = e.get("check", "none")
        out.append(
            f"| {BADGE.get(e.get('status'), '')} | {e.get('trigger','')} "
            f"| **[{e.get('title','')}]({e['file']})** "
            f"| {' · '.join(e.get('applies', []))} "
            f"| {'—' if check in ('none', '') else '`' + check + '`'} |"
        )
    if gone:
        out += ["", "## Superseded", "",
                "*Kept, never deleted — a reader who finds one of these quoted in an old note "
                "needs to be able to follow it here and see that it fell.*", "",
                "| | The rule | Replaced by |", "|---|---|---|"]
        for e in gone:
            out.append(f"| ⊘ | [{e.get('title','')}]({e['file']}) | "
                       f"{', '.join(e.get('supersededby', [])) or '—'} |")
    out.append("")
    (PRINCIPLES / "INDEX.md").write_text("\n".join(out), encoding="utf-8")


def write_yaml(entries):
    y = ["# principles.yaml — generated by tools/build_principles.py. Do not edit.",
         "# Source of truth: the frontmatter of each process/principles/*.md entry.",
         "# Loaded by the skills, which select on `applies`.",
         ""]
    for e in sorted(entries, key=lambda x: x.get("id", "")):
        y.append(f'- id: {e.get("id","")}')
        y.append(f'  title: "{e.get("title","")}"')
        y.append(f'  trigger: "{e.get("trigger","")}"')
        y.append(f'  status: {e.get("status","provisional")}')
        y.append(f'  since: {e.get("since","")}')
        y.append(f'  applies: [{", ".join(e.get("applies", []))}]')
        y.append(f'  check: {e.get("check","none")}')
        y.append(f'  entry: process/principles/{e["file"]}')
        y.append("")
    (ROOT / "process" / "principles.yaml").write_text("\n".join(y), encoding="utf-8")


def show_applies(entries, scope):
    """What fires on this kind of work. Called by the skills, at the moment it matters."""
    hits = [e for e in entries
            if scope in e.get("applies", []) and e.get("status") != "superseded"]
    if not hits:
        print(f"no principles apply to `{scope}`")
        return 0
    print(f"\nprinciples that fire on `{scope}` — {len(hits)}\n")
    for e in sorted(hits, key=lambda x: (x.get("status") != "active", x.get("id", ""))):
        mark = BADGE.get(e.get("status"), "")
        print(f"  {mark} {e.get('title','')}")
        print(f"     fires when: {e.get('trigger','')}")
        print(f"     {'provisional — one case so far. ' if e.get('status') == 'provisional' else ''}"
              f"process/principles/{e['file']}\n")
    return 0


def main():
    check_only = "--check" in sys.argv
    if "--applies" in sys.argv:
        i = sys.argv.index("--applies")
        scope = sys.argv[i + 1] if len(sys.argv) > i + 1 else ""
        if scope not in SCOPES:
            print(f"--applies takes one of: {', '.join(SCOPES)}")
            return 1
        entries, problems = load()
        if problems:
            print("process/principles — problems:\n")
            for pr in problems:
                print(f"  ✗ {pr}")
            return 1
        return show_applies(entries, scope)
    entries, problems = load()
    problems += verify_anchors(entries)
    problems += verify_structure(entries)

    if problems:
        print("process/principles — problems:\n")
        for p in problems:
            print(f"  ✗ {p}")
        print(f"\n{len(problems)} problem(s). Nothing written.")
        return 1

    if check_only:
        print(f"process/principles — {len(entries)} entr(y/ies), all anchors resolve, all structured.")
        return 0

    write_index(entries)
    write_yaml(entries)
    live = [e for e in entries if e.get("status") != "superseded"]
    print(f"wrote process/principles/INDEX.md and process/principles.yaml "
          f"({len(entries)} entries, {len(live)} in force)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
