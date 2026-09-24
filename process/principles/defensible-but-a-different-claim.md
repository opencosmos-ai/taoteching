---
id: defensible-but-a-different-claim
title: "A construal defensible in the Chinese that lands as a different claim in English has not been translated"
status: active
since: 2026-09-07
trigger: "you are keeping a reading because the Chinese permits it, and the English is saying something the Chinese does not"
applies: [drafting, notes]
evidence: ["notes/translation.md#ch-13-one-word-per-character-and-the-chapters-argument-appears", "notes/translation.md#ch-39-what-得一-means-and-the-mirror-that-was-inverted"]
check: none
supersedes: []
---

# A construal defensible in the Chinese that lands as a different claim in English has not been translated

**The rule.** *Supply what a character means, not what a passage points at* governs what may be **added**. This is the test on what may be **kept**: a parse the Chinese permits is not thereby a translation. **If the English that results makes a different claim than the Chinese does, the construal has failed** — however well it can be defended grammatically.

**When it fires.** When your defence of a line is *"the Chinese allows this reading."* That is an argument about the source; it is not yet an argument about the sentence you have written.

---

## Why this holds

**Permission is not equivalence.** Classical Chinese underdetermines subject, number, definiteness and the direction of many relations, so a line will often permit two or three parses. Each is defensible. **But English cannot be underdetermined the same way** — it must commit — and the committed English may land somewhere the Chinese never stood, while still being traceable to it word by word.

**Which makes grammatical defensibility the most dangerous kind of correctness here**, because it survives every check. A defensible parse passes the locks, passes the concordance, passes a character-by-character reading, and passes a reviewer asking *"is this warranted?"* — because it is. The only question that catches it is a different one: ***what does this English sentence claim, and does the Chinese claim that?***

**The test is about the reader, not the translator.** It asks what an English reader will take away, not what a translator can justify. Those diverge precisely where the construal is clever.

**And it pairs with [[collocation-carries-a-verdict]].** There, the words are right and the **idiom** adds a claim. Here, the words and the grammar are both defensible and the **construal** adds one. Both are faults invisible at the level of the character, which is why both had to be stated.

---

## Why this principle exists

**Ch 13's closing couplet was reversed.** 以A為B is *take A as B*, and the English had inverted it — converting **a judgment of persons** into **a theory of value**. Both readings can be argued from the characters; only one is the chapter's claim. Two of that chapter's decisions turned on this test. → [ch 13](../../notes/translation.md#ch-13-one-word-per-character-and-the-chapters-argument-appears)

**Ch 39's opening line.** The same test decided it: a construal the Chinese permits was set aside because the English it produced asserted something the chapter does not. → [ch 39](../../notes/translation.md#ch-39-what-得一-means-and-the-mirror-that-was-inverted)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *read the English alone, without the Chinese, and say what it claims* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Not enforced.** The two-pass reading is the whole method, and it is a reading.

---

## Where it does not fire

**It is not a licence to prefer the reading you like.** The test asks whether the English *claims* something the Chinese does not — not whether it says something you would rather it did not. A hard claim the Chinese genuinely makes stays.

**It does not settle a genuine ambiguity.** Where the Chinese really is double and the commentators divide, the answer is an English that holds both, not a construal picked by this test. See [[divergence-stays-open]].

**And a difference in emphasis is not a different claim.** Every translation redistributes stress; the threshold is a claim the reader would have to withdraw on seeing the Chinese.

---

## What it obliges

1. **After settling a line, read the English alone — without the Chinese beside it — and say what it claims.** Then check that against the source. The two-pass separation is the whole method.
2. **When a parse is defended on grammar alone, treat that as a warning rather than a conclusion.**
3. **Record the construal you declined and what it would have claimed**, so the argument is available to whoever revisits the line.
