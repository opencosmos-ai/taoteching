---
id: renders-no-character
title: "Every English word in the verse renders a character"
status: active
since: 2026-09-10
trigger: "you are about to put a word in the verse that renders nothing in the Chinese"
applies: [drafting]
evidence: ["notes/translation.md#ch-10-five-englishes-attached-to-characters-that-are-not-in-the-chapter", "notes/translation.md#ch-23-同-is-the-same-not-a-merging-2026-09-03", "notes/translation.md#ch-41-the-建言-catalogue-rebuilt-and-建-licensed-to-flex"]
check: none
supersedes: []
---

# Every English word in the verse renders a character

**The rule.** A word in the translation earns its place by rendering something in the Chinese. A word that renders nothing is an addition, whatever its merits — and this edition does not make additions silently. **Where a word is genuinely supplied, the note says so and says why.**

**When it fires.** When you reach for a word because the line needs it, rather than because the Chinese has it. Intensifiers first (*deeply*, *truly*, *utterly*), then connectives the Chinese does not print, then the abstraction that makes a concrete line sound finished.

---

## Why this holds

**This is the most common failure in the corpus, by a wide margin.** The sweeps have turned up **88 instances** of a word rendering nothing, against 47 of the next most common fault. It is not carelessness and it does not look like error while you are doing it: every added word is added *because the line reads better with it*.

**The mechanism is that English abhors the classical Chinese sentence.** Classical Chinese omits subjects, drops connectives, and stacks four characters where English wants nine. Every one of those gaps is a place where a translator supplies something, and the supply is usually **invisible to the translator and permanent in the text.** The line reads well; nobody can see the seam; and a claim the Chinese never made is now in a public-domain edition under someone's name.

**No check can catch this, and none ever will.** Every gate in this repository fires on a forbidden *word being present*. An addition is an absence in the Chinese, not a presence in the English — there is nothing to key on. `check_locks.py` passes a chapter that renders none of its own characters, because every rule keys off a character to judge an English. **The only instrument is a reader with the source table open.**

**The cost is not evenness of tone. It is evidence.** This translation's whole claim is that it was built from the characters. A word that renders no character is the one thing that, found by a careful reader, makes the claim unverifiable everywhere else.

---

## Why this principle exists

**Ch 10** carried *five* Englishes attached to characters not in the chapter — 全 (*quán* — whole), 萬物 (*wàn wù* — the countless things) and 鑑 (*jiàn* — mirror) among them. `status: drafted`, `retrofit: []`, and it had passed every check and a hand sweep. → [Ch 10](../../notes/translation.md#ch-10-five-englishes-attached-to-characters-that-are-not-in-the-chapter)

**Ch 23** had *intensity* and *sustain* rendering nothing at all — and *intensity* was worse than invented: it was 王弼 (*Wáng Bì*)'s gloss 暴疾 (*bào jí* — violent and rapid) lifted out of the commentary into the verse. The chapter also read 人 (*rén* — a person) as ***we***. → [Ch 23](../../notes/translation.md#ch-23-同-is-the-same-not-a-merging-2026-09-03)

**Ch 41** read *the countless things* on a chapter with no 萬物 in it, and packed twelve proverbs of the 建言 (*jiàn yán* — "established sayings") catalogue onto five lines, which required connective tissue the Chinese does not print. → [Ch 41](../../notes/translation.md#ch-41-the-建言-catalogue-rebuilt-and-建-licensed-to-flex)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *point every English word at a character* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |

**Deliberately not enforced.** A thin-translation rule was prototyped and declined at ~90% false positives (`WORKLIST.md` T5-1): inflection, inserted articles and licensed flexions make the check unanswerable by a tool.

---

## Where it does not fire

**English grammar is not an addition.** Articles, tense, number and the verb *to be* have no characters and are not optional; supplying them is what translating into English *is*. The rule governs **content**, not function words.

**A supplied verb is scaffolding and is allowed, when it is named.** 善下之 (*shàn xià zhī*) is *"masterful at staying below them"* — 下 (*xià* — below) is a position and English will not leave the slot empty. That supply is legitimate, recorded, and consistent across chapters 8, 61 and 66. What is not legitimate is supplying a verb that smuggles in a claim.

**And a rendering may be *interpretive* without being an addition.** Ch 14's *the invisible* for 夷 (*yí* — level) renders the character by its meaning in that line; it is a reading, not an insertion, and it is governed by [[legibility-debt]] instead.

**The dividing question: could you point at the character it comes from?** If yes, argue about the reading. If no, it is an addition and needs a note or removal.

---

## What it obliges

1. **Read the line against the source table, character by character, before you consider it done.** Not the gloss column — the Chinese.
2. **Where you supply, say so in the chapter note** and say what the supply is doing. *"Rare renders no character and that cost is recorded"* is the form.
3. **Never supply from the commentary.** A commentator's gloss is evidence for a reading, never a word for the verse — see the standing rule in `notes/translation.md`.
4. **Treat a line that reads beautifully as a place to look**, not as a place to stop. Every one of the 88 read well.
