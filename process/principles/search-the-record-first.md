---
id: search-the-record-first
title: "Before researching a character, start from what this repository has already decided"
status: active
since: 2026-09-23
trigger: "you are about to research a character, a fork or a rendering from 說文, the commentaries, or the web"
applies: [drafting, glossary, notes]
evidence: ["notes/translation.md#亂-luàn-disorder-a-tangle-with-hands-in-it-not-a-void", "notes/translation.md#明-míng-the-frontmatter-catches-up-with-the-entry-and-道-stops-being-a-path", "notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word"]
check: concordance --record
supersedes: []
---

# Before researching a character, start from what this repository has already decided

**The rule.** Before you open 說文解字, a commentary or a search engine on a character, a textual fork or a candidate rendering, **ask this repository what it has already decided**, and cite what you find.

```bash
python3 tools/concordance.py --record 亂
```

**When it fires.** At the start of any research on a character — before the four corners of `process/method.md` §3, not instead of them.

---

## What the record is, and why it comes first

**This repository holds its own prior reasoning**: fifty glossary entries, three notes layers, `WORKLIST.md`, `DISCOVERIES.md`, and the notes of eighty-one chapters. Much of it was written by someone with the evidence open, and it is dated and argued.

**That record is not indexed by the thing you are looking for.** A finding lives where it was found. `notes/` is indexed by chapter, `glossary/` by term, `WORKLIST.md` by debt, and a finding about one character often sits in the notes of a chapter about something else. You cannot browse to it; you have to search for it.

**Searching first is the cheapest step and it prevents the costliest outcome.** Rebuilding an argument costs the research again. Worse, it risks reaching a *different* answer from the one already recorded, which leaves the repository holding two rulings with nothing to say which is live.

**The record is reasoning, not evidence.** It is a first stop and never the last. It can be wrong, and where a note disagrees with the verse, the disagreement is itself a finding.

---

## Why this principle exists

`process/method.md` §3 named every source outside this repository — the graph, the witnesses, the commentaries, the locks — and none inside it. In the week of 2026-09-20 the gap cost three rediscoveries. The 亂 entry rebuilt from 說文 an argument that `chapters/003.md` had held since August. 明's own entry already listed the forms its frontmatter was missing. `WORKLIST.md` had diagnosed the 保 fault at ch 9 two weeks before it surfaced. → [亂](../../notes/translation.md#亂-luàn-disorder-a-tangle-with-hands-in-it-not-a-void) · [明](../../notes/translation.md#明-míng-the-frontmatter-catches-up-with-the-entry-and-道-stops-being-a-path) · [保](../../notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`tools/concordance.py --record`** | prints every place the repository has written about a character, grouped by layer: `glossary/`, `notes/`, `WORKLIST.md`, `DISCOVERIES.md`, and chapter notes. Chapter **source tables are excluded**, because they print the character on every line it occurs in. The term's **own entry collapses to a pointer**, because that is the one place nobody forgets to look |
| **`process/method.md` §3** | step zero, before the four corners. It is framed as a prior step and not a fifth corner, because the corners are evidence about the Chinese and the record is our own reasoning |
| **`chapter-review` skill, step 0** | in the opening command block, beside `--witnesses`, `--commentary` and `--formulas` |
| **`glossary-entry` skill, §1** | the first command in the evidence block |
| **`tools/tests/test_concordance.py`** | `TheRecord` asserts the command still finds a finding held in another chapter's notes, and still excludes source tables and generated files |

---

## Where it does not fire

**It never replaces the primary sources.** [[commentary-is-not-a-rendering]] and [[verify-the-flag]] still hold. The record tells you what was decided and why; the corners tell you whether that was right.

**A character with no history here** returns nothing. That result is an answer, and it cost one command.

**A note does not outrank a line.** A note records what was true when written. Where it and the verse disagree, treat it as a finding.

---

## What it obliges

1. **Run `--record` before you research.**
2. **Cite what you find**, so the new record points at the old one instead of competing with it.
3. **If the record is superseded, say so where the old reasoning sits** — with a supersession block in place, not only a new note elsewhere. An old ruling with no mark on it will be found again and believed.
4. **If the record was right and you rediscovered it anyway, note that too.** It is evidence about whether the method is working.
