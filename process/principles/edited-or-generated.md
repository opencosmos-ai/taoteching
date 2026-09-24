---
id: edited-or-generated
title: "Every file is edited or generated, never both"
status: active
since: 2026-08-11
trigger: "you are about to hand-edit a file a tool writes, or hand-maintain a list a tool could derive"
applies: [tooling, notes]
evidence: ["ARCHITECTURE.md#the-one-rule-that-explains-most-of-the-design", "ARCHITECTURE.md#what-is-generated-and-from-what"]
check: none
supersedes: []
---

# Every file is edited or generated, never both

**The rule.** A file is **hand-written and authoritative**, or it is **built and disposable**. Never both. A hand-edit to a generated file is erased on the next build; a hand-kept copy of derived data goes stale on a schedule nobody sets.

**When it fires.** When you reach into a generated file to fix one line, and when you are tempted to keep a convenient summary of something a tool already knows.

---

## Why this holds

**A hand-kept copy of a derivable fact is a second authority, and two authorities drift.** Nothing makes the copy wrong on the day it is written; it goes wrong on the day the source changes and nobody remembers the copy exists. A generated file cannot drift, because it has no author to forget.

**The rule is what makes the architecture legible.** Three directories are edited by hand and are the truth — `chapters/`, `glossary/`, parts of `sources/`. Everything else is a build product with a named generator, and you can always answer *"where does this come from?"* in one step. A file that is partly hand-edited destroys that answer for the whole tree, because you can no longer trust any generated file to be a function of its source.

**And it is why a decision becomes an enforced rule with no code change.** A lock written in an entry's frontmatter is picked up by `build_index.py` into `terms.yaml`, which `check_locks.py` reads. **One authority, one path, no copies.**

---

## Why this principle exists

Both failure modes happened here. A hand-kept table of the locks in `CLAUDE.md` went stale twice in one week — 仁 (*rén* — humaneness) and 慈 (*cí* — tenderness) were locked and never reached it, while the generated index had them right throughout — and it was deleted. And `data/constellation-chars.json` published glosses that `data/characters.csv` had already withdrawn, for seven months, because nothing rebuilt it (see [[deterministic-before-gated]]).

**The one rule that explains most of the design**, with the two places it deliberately bends. → [ARCHITECTURE](../../ARCHITECTURE.md#the-one-rule-that-explains-most-of-the-design)

**The generated-file table** — what is built, by what, from what, and whether CI fails when it is stale. → [ARCHITECTURE](../../ARCHITECTURE.md#what-is-generated-and-from-what)

---

## How it is implemented

| Where | What it does |
|---|---|
| **The generated files' headers** | `glossary/INDEX.md`, `glossary/terms.yaml`, `process/principles/INDEX.md`, `data/README.md` each say what built them and not to edit by hand |
| **CI**, three *generated … files are current* steps | rebuild the glossary, the principles and the atlas, and fail on any diff — a hand edit to a build product cannot survive a push |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Enforced by CI** for every generated file. A hand edit is also overwritten by the next build, silently — which is how `data/README.md` lost one on 2026-09-23.

---

## Where it does not fire

**Two places bend deliberately**, and they are named in the architecture rather than hidden.

**`sources/` is the one mixed directory** — `variants.yaml`, `guodian-inventory.yaml` and the gloss files are hand-kept; `commentaries/` and `shuowen/` are machine-written. The directory is mixed; **no single file is.**

**And `source/chinese.md` is derived but built by hand**, which is a debt rather than an exception.

---

## What it obliges

1. **Put the header on every generated file**: built by what, from what, never edit by hand.
2. **When you want a summary of derived data, generate it** — `INDEX.md`, `terms.yaml`, `principles.yaml` all exist because the hand-kept version failed.
3. **Rebuild and commit in the same commit**, and gate it in CI.
4. **If you catch yourself editing a build product, fix the generator.**
