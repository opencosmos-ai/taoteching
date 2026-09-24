---
id: evidence-gate
title: "No rule fires on English alone — a gate that cries wolf is not a gate"
status: active
since: 2026-08-11
trigger: "you are writing a check, or widening one, so that it can fire without seeing the character"
applies: [tooling]
evidence: ["ARCHITECTURE.md#the-evidence-gate", "ARCHITECTURE.md#the-thirteen-rules"]
check: check_locks
supersedes: []
---

# No rule fires on English alone

**The rule.** A finding requires **evidence in the Chinese**. *"Virtue"* is an error only when 德 (*dé*) stands in **that chapter's own** source table; otherwise it drops to `info`, in a separate false-friends list that fails nothing.

**When it fires.** Whenever a check is written or widened, and whenever a missed finding tempts you to loosen one.

---

## Why this holds

**A gate that is sometimes wrong stops being read.** `check_locks.py` exits non-zero, gates the pre-commit hook and CI, and therefore **must never cry wolf** — because the cost of a false positive is not one wasted minute, it is that the next real finding is skimmed past. Precision is not a nicety here; it is the whole basis on which the tool is allowed to block a commit.

**The evidence gate is what made it usable.** It took the first run's error list to **nine findings with zero false positives.** Before it, roughly a third of flags were wrong.

**And precision has a price that must be paid elsewhere, not wished away.** The gate keys off the character being present, so it can only ever test **one direction** of a lock — every 強 renders *strong*, never every *strong* renders 強. The reverse direction is a reader's job with `--english`, and it caught 固 and 壯 both wearing 強's English **inside chapters that contain 強**. See [[already-spoken-for]].

**Which is why the two tools have opposite contracts and must not be merged.** `check_locks.py` optimises precision and judges. `concordance.py` optimises recall and judges nothing. **A tool that gated and searched at once would be too noisy to gate and too quiet to search.**

---

## The cases

**The evidence gate** has a section of its own in the architecture, because it is the design decision the rest of the checker rests on. → [ARCHITECTURE](../../ARCHITECTURE.md#the-evidence-gate)

**The thirteen rules** each carry a severity, and which findings are allowed to fail a build is the same decision made thirteen times. → [ARCHITECTURE](../../ARCHITECTURE.md#the-thirteen-rules)

---

## Where it does not fire

**Structural checks need no evidence gate.** A stale generated file, an unresolved anchor, a missing hard break, an expired `shaloms-call` — these are facts about the repository, not judgments about a rendering, and they fail immediately.

**Warnings are not gated the same way.** Repeated-formula findings are a reading for Shalom, not a verdict; they print and never fail.

**And an `info` finding is not a non-finding.** The false-friends list is where the reverse-direction work starts.

---

## What it obliges

1. **Key every rendering rule on the character being present in that chapter.**
2. **When a real finding is missed because of the gate, add the direction elsewhere** — a reverse `--english` pass, a new narrow rule — rather than loosening the gate.
3. **Keep severity honest**: `error` blocks, `warning` informs, `info` accumulates. Promoting a noisy rule to `error` costs the whole gate its authority.
4. **Do not merge the search tool into the gate.**
