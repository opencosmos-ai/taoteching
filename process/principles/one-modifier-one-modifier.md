---
id: one-modifier-one-modifier
title: "One Chinese modifier, one English modifier — and where it will not fit, lose part and say so"
status: provisional
since: 2026-08-30
trigger: "you are about to render one character with two English words because neither alone covers it"
applies: [drafting]
evidence: ["notes/translation.md#ch-3-12-44-64-難得之貨-rare-goods-and-貨-locked-to-goods", "notes/translation.md#ch-63"]
check: none
supersedes: []
---

# One Chinese modifier, one English modifier

**The rule.** Where the Chinese has one modifier, the English has one. **Do not pair two near-synonyms to cover a character neither word quite fits.** Where a character's sense genuinely will not go into one English word, **lose part of it and record the loss** — do not paper the gap with a second word.

**When it fires.** When you have two candidate words, each nearly right, and the obvious move is to use both.

---

## Why this holds

**A doublet reads as emphasis, not as two facts.** *"Rare and scarce"* does not deliver two properties to an English reader; it delivers one property, said twice, with rhetorical weight added. So the pairing both **fails to cover the gap** it was reaching for and **adds a stress the Chinese does not have**.

**And the habit is a period tell.** The near-synonym pair is the signature cadence of the King James Bible — *"assemble and meet together," "acknowledge and confess our manifold sins"* — a translation strategy from a specific century, catalogued in `process/overlay-audit.md`. Using it here imports the register the whole edition exists to keep out, by a route no forbidden-word list can see. See [[imported-register]].

**The honest alternative is subtraction, not addition.** English frequently has no single word for a Chinese sense, and that is a fact about English rather than a problem to be solved. **A recorded partial loss is a translation. A doublet is a translation plus a claim.** The note is what makes the first one honest: *"rare renders no character, and that cost is recorded."*

---

## Why this principle exists

**難得之貨 (*nán dé zhī huò* — "goods hard to come by").** *"Rare and scarce"* was considered and refused. The settled reading is **rare goods**, with the cost stated plainly: *rare* renders no character, because **"hard" is 堅's** and 難's own *difficult* will not go attributive. English has **no one-word adjective for "difficult to obtain" that is not also a value word** — which is why three chapters drifted the same way independently. → [難得之貨](../../notes/translation.md#ch-3-12-44-64-難得之貨-rare-goods-and-貨-locked-to-goods)

**Ch 63's 味無味** reads *"taste the flavorless"* — two English words for one character — and **the loss is recorded rather than hidden**: the second word buys the parallel that 無味 needs, and the note says so. That is the rule's second half working. → [ch 63](../../notes/translation.md#ch-63)

---

## Why this is still `provisional`

**The doublet-refusal half rests on one case.** 難得之貨 is a clean instance; ch 63 exemplifies the *record-the-loss* half rather than the refusal. One case is an observation. A second genuine doublet refused — or a doublet found and repaired — promotes this.

**Two adjacent cases were examined and are not instances.** Ch 21's 恍 and 惚 take *vague* and *elusive*: **two characters, two words**, which is the rule being obeyed, not bent. Ch 24's 跨 rendered *stride* left a near-synonym of 行's *walk* — that is a collision between characters, governed by [[already-spoken-for]].

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *where you used two English words for one Chinese modifier, name the single word you avoided* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |

**Not enforced.** Provisional, on one case.

---

## Where it does not fire

**Two characters take two words.** The rule counts modifiers in the Chinese, not syllables in the English.

**An article, a preposition or a copula is not a second modifier.** *The flavorless* is one modifier with English grammar attached.

**And a compound is one unit.** 難得 is a bound phrase; what it takes in English is judged whole.

---

## What it obliges

1. **When reaching for a second word, stop and ask which single word you are avoiding, and why.** The answer is usually that no single word is right, which is the finding.
2. **Take the loss and name it in the note** — which part of the sense went, and which character's English was unavailable.
3. **Check the doublet against the KJV cadence before accepting it.** If it scans like scripture, it is doing more than covering a gap.
