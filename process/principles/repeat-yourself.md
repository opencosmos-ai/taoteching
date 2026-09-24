---
id: repeat-yourself
title: "Where the Chinese repeats itself, repeat yourself"
status: active
since: 2026-09-05
trigger: "the same Chinese segment or frame appears twice and you are about to render it two ways"
applies: [drafting]
evidence: ["DISCOVERIES.md#6-the-repetition-is-the-argument-and-our-tools-could-not-see-it", "PLAN.md#what-chapter-11-taught-the-tools-2026-09-05"]
check: concordance --formulas
supersedes: []
---

# Where the Chinese repeats itself, repeat yourself

**The rule.** A varied English is not a better rendering of a repeated Chinese; **it is a rendering of a text that was never written.** Where a segment or a frame recurs — within a chapter or across the book — the English recurs with it, word for word.

**When it fires.** When a line feels like something you have already translated. It usually is.

---

## Why this holds

**The repetition *is* the argument.** Chapter 11 says one sentence three times, over a cart, a pot and a room — 當其無 (*dāng qí wú* — "right where it is not there") — and the point is precisely that **the same thing is true of all three**. Three different Englishes deliver three observations about three objects. The generalisation, which is the chapter, disappears.

**And the fault is invisible line by line.** Each variant reads well; each is defensible; nothing in any single line is wrong. Only the set is wrong, and nobody reads the set — which is why this survived every human pass and every tool until 2026-09-05.

**The instinct that causes it is a good instinct misapplied.** English prose style penalises repetition, and a translator trained on English prose will vary by reflex. Classical Chinese does not share the penalty; it uses repetition structurally, as scaffolding a reader is meant to notice.

**The tools had the blind spot built in.** Both indexed segments into a *set* of chapter numbers, so a segment repeating three times **inside one chapter** collapsed to a single entry and was then dropped as "not shared." The within-chapter half is where the damage is, and it was the half the machinery could not see.

---

## Why this principle exists

**Ch 11** — three identical 當其無 frames rendered three ways, and 利 (*lì* — advantage) and 用 (*yòng* — use) both lost into an abstraction. Now one frame, three times, eleven lines for eleven. → [DISCOVERIES §6](../../DISCOVERIES.md#6-the-repetition-is-the-argument-and-our-tools-could-not-see-it)

**What it taught the tools** — `--formulas` now covers *within* a chapter as well as across, and finds **frames** as well as segments: 將欲▢之, ▢得一以▢, 有▢之用. → [PLAN](../../PLAN.md#what-chapter-11-taught-the-tools-2026-09-05)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py --formulas N`** | every segment and frame the chapter repeats, within itself and across the book, with the English underneath. `chapter-review` step 0, marked not optional |
| **`check_locks.py`** · `repeated-formula` | compares shared segments **across** chapters, at `warn` |
| **`tools/tests/test_concordance.py`** | pins the within-chapter case that was invisible until 2026-09-05 |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |

**Partly enforced.** Across chapters it warns; within a chapter it is found only by running `--formulas`.

---

## Where it does not fire

**Two different characters are not a repetition**, however alike they look. 襲 (*xí*) and 習 (*xí*) at chapters 27 and 52 produced two Englishes that looked like this fault and were a **manuscript fork**.

**Grammar may force a variation.** Where a repeated phrase governs a noun in one place and a clause in another, the English fits the grammar — 是謂 (*shì wèi*) reads *"This is called"* eight times and *"This is what is meant:"* where it governs a whole clause. **Same verb, fitted; not a different word.**

**And lineation is a separate question.** Two instances may sit on one line in one chapter and two in another without breaking the rule, provided the words match. See [[lineation-is-ours]].

---

## What it obliges

1. **Run `concordance.py --formulas N` before drafting. It is not optional.** It prints every segment and frame the chapter repeats, with the English underneath.
2. **When two chapters share a formula, change both or neither.**
3. **Where you must vary, say in the note what forced it** — grammar, or a fork, or a character that is not the same character.
