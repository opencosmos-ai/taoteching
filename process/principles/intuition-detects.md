---
id: intuition-detects
title: "Intuition is last as an arbiter and first as a detector — discomfort is a research assignment"
status: active
since: 2026-08-20
trigger: "a rendering feels wrong and you cannot yet say why"
applies: [drafting, process]
evidence: ["process/method.md#intuition-is-last-as-an-arbiter-and-often-first-as-a-detector", "DISCOVERIES.md#how-it-was-found-and-it-started-with-a-feeling"]
check: none
supersedes: []
---

# Intuition is last as an arbiter and first as a detector

**The rule.** In the tie-breaking order, poetic intuition comes **last** — exercised after the deepest reading is on the table. In the order of *discovery* it comes **first**. When a word feels off, that is **a research assignment, not a preference to accommodate.** Do not offer a synonym that feels better. Go and find what the discomfort is detecting.

**When it fires.** The moment anyone says a line feels wrong and cannot say why. Especially then.

---

## Why this holds

**The feeling is data about the text, and it usually precedes the evidence.** A reader with decades in the book has a model of it that is not fully articulable, and that model registers a wrong note before the argument for it exists. **Treating the note as taste throws away the finding.**

**The catastrophic version of the mistake is the synonym.** A word feels off; a better-feeling word is offered; the feeling subsides; **the fault is still there, now harder to see, because the alarm has been silenced.** The discomfort was pointing at something structural, and it got answered at the level of diction.

**And the direction of the rule matters.** Intuition detects; it does not adjudicate. A feeling that survives investigation is a finding; a feeling that the evidence contradicts is a feeling. The order — characters, witnesses, commentaries, internal consistency, ethos, then intuition — is the adjudication order, and it is not what this rule is about.

---

## Why this principle exists

The largest finding in this repository began as a feeling. Shalom said ch 25's *king* did not sit right before anyone could say why; the hunt that followed reached the oldest witnesses, which have 人 (*rén* — a person) where the received text has 王 (*wáng* — king). A throne had been installed in the text, and the detector was a feeling.

**The method states it directly**, as a section of its own. → [method](../../process/method.md#intuition-is-last-as-an-arbiter-and-often-first-as-a-detector)

**Ch 25 — "it started with a feeling."** Shalom noticed that *king* did not feel right; the manuscripts proved him right. → [DISCOVERIES §1](../../DISCOVERIES.md#how-it-was-found-and-it-started-with-a-feeling)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`CLAUDE.md` → *How Shalom works*** | stated as a working rule, starred |
| **`concordance.py`**, `--commentary`, `--witnesses` | the instruments for answering the alarm rather than muting it with a synonym |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`CLAUDE.md` → *Start here*** | `--applies process` lists it at the start of every session |

**Not enforced.** It governs how a challenge is received.

---

## Where it does not fire

**It does not make the feeling right.** DISCOVERIES §1's *heaven* half stands and its *king* half was **backwards** — the finding was real, part of the conclusion was not. The assignment is to investigate, not to vindicate.

**It does not override the tie-breaking order.** Where the characters and the witnesses answer, they answer.

**And it is not a licence to hold out.** A discomfort that survives the evidence gets recorded as an open question, not defended as a veto.

---

## What it obliges

1. **Treat "this feels off" as a task.** Run the concordance, the commentary, the witnesses on that line.
2. **Never answer a feeling with a synonym.** If the replacement is not backed by a finding, the alarm has been muted rather than answered.
3. **Report what the discomfort was detecting**, even when the original rendering survives. The investigation is the value.
4. **Treat a challenge as a finding, not a complaint.**
