---
id: one-question-at-a-time
title: "One question at a time — bring the deepest one, with a recommendation"
status: active
since: 2026-08-28
trigger: "you are about to put more than one open decision to Shalom in a single message"
applies: [process]
evidence: ["CLAUDE.md#how-shalom-works", "process/method.md#1-prime-directive-for-the-ai-collaborator-take-a-stand"]
check: none
supersedes: []
---

# One question at a time

**The rule.** Do not stack decisions. **Bring the deepest one, with a clear recommendation and the evidence and the cost; take the answer; then bring the next.** A menu is not a recommendation, and four questions in one message is not four times as useful as one.

**When it fires.** At the end of any piece of work that surfaced more than one open decision — which is most of them.

---

## Why this holds

**Shalom decides; the AI argues.** That division only works if each decision arrives with enough argument attached to be decidable. **Four questions in one message means four thin arguments**, and the deepest one — the one that would have changed the others — gets the same weight as the smallest.

**And decisions are usually not independent.** Settling the deepest question frequently dissolves two of the others or changes what they are. Asking them together forces answers to questions that should not have been asked yet.

**The rule was stated plainly on 2026-08-28** — *"You're asking too many questions at once"* — and it was a correction, which is the strongest evidence a rule is real here.

**It has an important corollary that is easy to miss: it does not license withholding work.** The requirement is one *question*, not one finding. Everything that does not depend on the answer gets done and reported; only the decisions queue. A message that reports five findings and asks one question is the shape.

**And it is downstream of the prime directive.** *"I'd do X, because ___"* — give alternatives, commit to a lean, defend it. **A question without a recommendation is work handed back.**

---

## Why this principle exists

**How Shalom works** — the rule, the correction that produced it, and the catches that show why a thin argument is worse than none. → [CLAUDE.md](../../CLAUDE.md#how-shalom-works)

**The prime directive** — take a stand, argue for the deepest reading, push back honestly. The one-question rule is what makes that possible per message. → [method](../../process/method.md#1-prime-directive-for-the-ai-collaborator-take-a-stand)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`CLAUDE.md` → *How Shalom works*** | stated as a working rule, starred, and loaded every session |
| **`CLAUDE.md` → *Start here*** | `--applies process` lists it at the start of every session |

**Not enforced.** It governs the conversation, not the text.

---

## Where it does not fire

**A set of related choices with one recommendation is one question.** *"Here are five term swaps, all following from the 執 ruling — apply them?"* is a single decision wearing five hats.

**Reporting is not asking.** Findings, applied changes and flagged riders can all travel together; the constraint is on **open decisions**.

**And a genuinely blocking ambiguity is asked immediately**, not queued behind a deeper question — if proceeding under any assumption would make the work useless, ask.

---

## What it obliges

1. **Rank the open decisions and lead with the deepest.** Never bury the important one under small notes.
2. **Attach a recommendation and the cost.** *"I lean X, and here is what X loses."*
3. **Do everything that does not depend on the answer, first**, and report it.
4. **After the answer, execute without relitigating** — and if a call is already in effect, say so once and proceed.
