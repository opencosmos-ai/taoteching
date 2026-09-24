---
id: verify-the-flag
title: "Verify a flagged line against the Chinese in its own chapter before changing it"
status: active
since: 2026-08-10
trigger: "a check, a sweep or a search has flagged a line and you are about to act on the flag"
applies: [drafting, tooling]
evidence: ["PLAN.md#what-the-2026-08-10-sweep-taught-the-checker", "PLAN.md#the-2026-08-10-hand-sweep-the-record"]
check: none
supersedes: []
---

# Verify a flagged line against the Chinese in its own chapter before changing it

**The rule.** A flag is a **reason to look**, never a verdict. Open the chapter, find the character, and confirm the finding against the Chinese on that page before touching the English.

**When it fires.** Every time a tool produces a list — and hardest when the list is long and the fixes look mechanical, because that is when acting without looking is most tempting.

---

## Why this holds

**Roughly a third of the first automated sweep's flags were false positives**, and the failures were not random. They clustered in ways worth knowing:

- **Homographs.** 常 (*cháng* — constant, the ever-present) against 長 (*cháng* — long). Same sound, different characters, and an English search cannot tell them apart.
- **Ordinary English words.** *"The one"* as a pronoun is not 一 (*yī*).
- **Two senses of one English word.** *"Block the openings"* renders 塞 (*sài*); *"uncarved block"* renders 樸 (*pǔ*). The checker sees the string.

**Acting on an unverified flag is worse than missing the finding**, because it introduces an error into a line that was right, in the name of a rule. And it does it with the authority of a tool, so nobody looks again.

**This is why the checker optimises precision and gates on evidence.** `check_locks.py` never cries wolf: no rule fires on English alone, and a finding without its character present drops to `info`. See [[evidence-gate]]. But the evidence gate protects against the *absent* character, not against the *wrong* one — 常 and 長 are both present, and both are 常's evidence as far as a string search can tell.

**And a search tool makes no claim at all.** `concordance.py` optimises recall and judges nothing, deliberately.

---

## Why this principle exists

**The 2026-08-10 sweep** — the first automated pass, and the record of what it taught. The error list went to **9 findings with zero false positives** only after the evidence gate was built; before it, a third of the flags were wrong. → [what the sweep taught the checker](../../PLAN.md#what-the-2026-08-10-sweep-taught-the-checker)

**The hand sweep it replaced** missed `chapters/053.md` rendering 大道 (*dà dào* — the great Tao) as *"the great Way"* — the one rendering `CLAUDE.md` forbids most emphatically — **one line below rendering the same compound correctly**. A careful human sweep missed it; a checker finds it in under a second. **Both halves of that story are the point.** → [the record](../../PLAN.md#the-2026-08-10-hand-sweep-the-record)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`check_locks.py`** | a match without its character is reported as *verify before changing*, not as an error |
| **`lock-ok`** waivers | record a false positive where the tool will see it; an unused waiver is an error, so the files self-clean |
| **`CLAUDE.md` → *How Shalom works*** | *always verify a flagged line against the Chinese in its own chapter* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |

**Not enforced.** It governs what a person does with a flag.

---

## Where it does not fire

**A build failure is not a flag.** A stale generated file, an unresolvable anchor or a broken hard break is a fact, not a judgment; fix it.

**And verification is not permission to dismiss.** Confirming the character is present makes the finding real; it does not make the current English right. The verification step decides *whether there is a question*, not *what the answer is*.

---

## What it obliges

1. **Open the chapter file and read the source table.** Not the gloss column — the Chinese.
2. **Check which character the English is actually rendering**, not which one the rule named.
3. **When a flag is a false positive, say so where the tool can learn it** — a `lock-ok` waiver with a reason, or a narrowed rule. **An unused waiver is itself an error, so the files self-clean.**
4. **Never delete a rule to silence a false positive.** See [[never-silence-a-rule]].
