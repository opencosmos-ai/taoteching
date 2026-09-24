---
id: distribution-locates
title: "A distributional argument is a reason to look, not a reason to conclude"
status: active
since: 2026-09-05
trigger: "your case for a rendering is that the character is used this way in its other chapters"
applies: [drafting, glossary]
evidence: ["notes/translation.md#ch-4-the-chapter-rebuilt-and-帝-restored-pass-ds-first", "notes/translation.md#ch-28-the-pointing-test-failed-on-nearly-every-line", "notes/translation.md#ch-8-善s-showcase-and-the-grammar-that-decides-it-2026-09-02"]
check: none
supersedes: []
---

# A distributional argument is a reason to look, not a reason to conclude

**The rule.** *"The character is a noun in its four other chapters, so it is a noun here"* is a strong reason to **examine** a line and a weak reason to **settle** it. Distribution locates the question. **Grammar, the graph, the witnesses and the commentators answer it.**

**When it fires.** Whenever the concordance produces a clean pattern and the pattern is doing the arguing. A count is persuasive out of proportion to its weight, because it looks like evidence and feels like proof.

---

## Why this holds

**A book is not a corpus with uniform behaviour, and this one least of all.** The Tao Te Ching repeatedly uses a word against its own usual sense — 強 (*qiáng* — strong) is the disease at ch 76 and the cure at ch 52. **A rule derived from the majority will misread exactly the lines the book cares most about**, because those are the ones where it breaks its own habit deliberately.

**And distribution is blind to grammar, which usually decides.** 象 (*xiàng*) is *image* at four places, so *image* looked settled at ch 4's 象帝之先. **The grammar defeated it**: wherever 象 is unambiguously a noun it is **marked** as one — by 之, by 有, or by 大 — and here it stands bare before a noun phrase, which is the shape of verb plus object. The count was four to one and the count was wrong.

**Position in the book matters too.** Ch 4 is 象's first appearance, so an English *image* would land where no reader could yet hear the thread. Distribution has no way to know that.

**The rule has a real boundary, and finding it is what makes it usable** — see below. Distribution about the **Chinese** cannot conclude. Distribution about the **English** often can.

---

## Why this principle exists

**Ch 4's 象 — distribution defeated.** Four noun uses against one, and the grammar overruled the count. Both commentaries agreed with the grammar. → [ch 4](../../notes/translation.md#ch-4-the-chapter-rebuilt-and-帝-restored-pass-ds-first)

**Ch 28's 雄/雌 — distribution concluding, legitimately.** *Rooster* and *hen* were **forced** because 牝/牡 already hold *male* and *female*. The note says so outright: the forcing argument is **distributional, not etymological**. This is a claim about which English words are already spoken for, not about what 雄 means. → [ch 28](../../notes/translation.md#ch-28-the-pointing-test-failed-on-nearly-every-line)

**Ch 8's 善 — distribution concluding, on grammar.** The shape was decided **by counting, not by taste**: 善 governs a **verb** in all eighteen of its other instances, so X善Y is *masterful at Y*. What made the count decisive is that it was a count of a **grammatical pattern** and the alternative parse collapsed on its own terms — *masterful ground*, *masterful trust*. → [ch 8](../../notes/translation.md#ch-8-善s-showcase-and-the-grammar-that-decides-it-2026-09-02)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py`** | gives recall and counts and judges nothing, deliberately. `chapter-review` step 3 and `glossary-entry` §1 |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Not enforced.** The rule governs what a count may be used to conclude, which is judgment.

---

## Where it does not fire — the boundary

**Distribution about the English concludes; distribution about the Chinese does not.** [[already-spoken-for]] is entirely distributional and entirely decisive: if *male* is worn by 牡 somewhere in the book, *male* is not available, and no amount of contextual argument makes it available again. That is a fact about this edition's vocabulary, which we control.

**Distribution of a grammatical pattern is stronger than distribution of a sense**, because grammar is more stable across a text than meaning — and stronger still when the competing parse fails independently, as at ch 8.

**And a count is decisive when it is exhaustive and the term is rare.** 彼 (*bǐ* — yonder) occurs exactly three times and all three are one tag; there is no competing context to lose.

---

## What it obliges

1. **State the count, then go and check the line.** `concordance.py` gives recall; it judges nothing, deliberately.
2. **Check the grammar of the specific line before accepting a pattern.** Marking — 之, 有, 大 — decides more often than frequency.
3. **Check whether the line is the character's first appearance.** A thread a reader cannot yet hear is not a thread.
4. **Say which kind of distributional argument you are making** — about the Chinese, or about which English words are taken. Only the second can close a question by itself.
