---
id: collocation-carries-a-verdict
title: "A collocation carries a verdict its component words do not"
status: active
since: 2026-08-31
trigger: "every word in your line is a defensible gloss and the phrase still says something the Chinese does not"
applies: [drafting]
evidence: ["notes/translation.md#ch-3-the-closing-movement-restored-and-a-sinister-register-that-was-ours", "notes/translation.md#ch-4-the-chapter-rebuilt-and-帝-restored-pass-ds-first", "notes/translation.md#ch-13-one-word-per-character-and-the-chapters-argument-appears"]
check: none
supersedes: []
---

# A collocation carries a verdict its component words do not

**The rule.** English phrases mean more than the sum of their words. A line in which **every word is a defensible gloss of its character** can still assert something the Chinese never says — because the *combination* is a fixed idiom with a meaning of its own. Check the phrase, not only the words.

**When it fires.** When you have checked every character, everything is right, and something is still off. That feeling is the detector; this is one of the three things it is usually detecting.

---

## Why this holds

**This is the third way a rendering smuggles a claim, and it is the hardest to see.** The first two are on record and both are visible in a single word. **A capital letter** confers status and turns a word into a doctrine. **A definite article** asserts a hierarchy — *"the high god"* for 帝 (*dì* — god). This third one is invisible at the word level **by definition**: no single word in the line is wrong, so no word-based check and no character-by-character reading will find it.

**English idiom is dense with buried judgments about power.** *"Without X knowing"* means **behind someone's back**. *"Weaken someone's will"* belongs to interrogation. *"Keep X from Y"* is restraint imposed from outside. None of those meanings lives in any component word; all three arrive with the phrase, fully formed, carrying a stance toward the person in the sentence.

**Which is exactly where this book is most vulnerable**, because so much of it is about a ruler and the ruled. A chapter of instructions can be turned into a manual of manipulation without a single mistranslated character — and the result reads fluently, because fixed idioms always do.

**The test that catches it: does the book use this English of the sage?** Every state chapter 3 names — 無知 (*wú zhī* — without knowing), 無欲 (*wú yù* — without wanting) — is asked of the reader elsewhere as a **good** thing. If a rendering makes the same state sound like something done *to* the people, the collocation has supplied a verdict the character does not carry.

---

## Why this principle exists

**Ch 3's closing movement** was drafted as *"keeping the people without knowing," "weakening their will," "keeping those who know from pushing to act."* Every word defensible; all three phrases wrong. 王弼 (*Wáng Bì*) on the first: 骨無知以幹 — *"the bones have no knowing, and so they are the frame."* **Bones are not being deceived.** And 河上公 (*Héshàng Gōng*) reads the third as what the knowers **become**: 思慮深，不輕言. → [ch 3](../../notes/translation.md#ch-3-the-closing-movement-restored-and-a-sinister-register-that-was-ours)

**Ch 4's 帝** — *"the high god"*, where the definite article does the work. The article is the single-word cousin of this fault, and the two were named together. → [ch 4](../../notes/translation.md#ch-4-the-chapter-rebuilt-and-帝-restored-pass-ds-first)

**Ch 13's closing couplet was reversed** by a construction rather than by a word: 以A為B is *take A as B*, and an English that inverted it turned a judgment of persons into a theory of value. → [ch 13](../../notes/translation.md#ch-13-one-word-per-character-and-the-chapters-argument-appears)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *ask what the line implies about the people in it* — the sage test |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |

**Not enforced, and cannot be.** A collocation is innocent word by word, so no rule keyed to a word can see it. It is held by the read-back and by judgment.

---

## Where it does not fire

**Not every idiom is a verdict.** English has to be idiomatic to be readable, and a fixed phrase that carries no stance is just English. The question is never *"is this an idiom?"* but *"what does this idiom think about the people in the sentence?"*

**It is distinct from [[no-verdict-the-chinese-lacks]], and the difference is where the verdict lives.** There, a **single word** is loaded and a plainer synonym fixes it. Here, no word is loaded and **the phrase must be recast**. A synonym swap will not help, which is why this one so often survives a careful pass.

**And it is not a licence to write stiffly.** Avoiding idiom altogether produces translationese, which carries its own claim — that the text is foreign and remote.

---

## What it obliges

1. **Read the finished line aloud and ask what it implies about the people in it**, not what it says about the characters.
2. **Apply the sage test**: does this book use this English of the sage, elsewhere? If a state is good when the sage has it and sinister when the people have it, the English is doing that, not the Chinese.
3. **Recast rather than substitute.** A collocation cannot be repaired one word at a time.
4. **Name the idiom in the note.** *"'Without X knowing' is a fixed English idiom meaning behind someone's back"* — so the next drafter meets the trap rather than the phrase.
