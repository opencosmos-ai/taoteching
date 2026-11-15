---
id: part-role-is-not-the-reading
title: "A part's role in a character and what a witness's bare part means in a line are two facts: the card holds the first, the notes the second"
status: provisional
since: 2026-11-15
trigger: "a witness writes a character's sound part alone, as a word, and you are about to decide what that part does inside the character, or what the line means"
applies: [drafting, glossary, tooling]
evidence: ["glossary/chong-沖.md#the-graph-water-and-a-sound", "glossary/chong-沖.md#chapter-42-the-breath-within"]
check: none
supersedes: []
---

# A part's role in a character and what a witness's bare part means in a line are two facts: the card holds the first, the notes the second

**The rule.** Record what a part does inside its character, sound or meaning, from the character's own meaning and the dictionary's formulas, and put that on the character's card. Record what a witness means when it writes that part alone in a line, and argue whether it is a word or a short spelling, in the variant apparatus and the notes. Never let either fact rewrite the other.

**When it fires.** A witness writes a character's sound part alone, as a word, where the received text writes the whole character, and you are about to decide what that part does inside the character, or what the line means.

---

## Why this holds

**A sound part is chosen for how it sounds, and it is also a word in its own right.** 中 (*zhōng* — middle) is the sound part of 沖 (*chōng* — surging), 盅 (*zhōng* — an empty vessel) and 忠 (*zhōng* — loyal), and none of those three means *middle*. Written alone, 中 means *middle*. Both facts are true at once, and they are about different things: one is how a character is built, the other is which word a scribe set down.

**The sound link is how the two words came to share a spelling.** Classical scribes often wrote by sound, so a character and its sound part could stand for each other. When an older copy writes the bare part, it may be spelling the whole character short, or it may be writing the other word. The link explains how the fork arose. It does not settle which word the line holds.

**So moving the part on the card would get the character wrong, and letting the card decide would get the line wrong.** Marking 中 as *meaning* in 沖 because chapter 42 reads *within* tells every reader of every 沖 that surging water has a middle in it. Reading chapter 42 as surging because 中 is only sound in 沖 decides a witness question by a dictionary analysis. Each fact has its own evidence, and the evidence for one says nothing about the other.

### The word-or-spelling test

Whether a bare part is a word or a short spelling is a question about the witness, and these three tests answer it:

- **Does the same copy write the whole character elsewhere?** If its scribe had the full graph and used it at another place, the bare part at this one is a choice rather than a habit.
- **Do independent copies write the bare part at the same place?** Two copies agreeing is a reading. One copy alone may be a scribe's shorthand.
- **Does an early commentator read the whole character as the bare part's word?** A reader close to the text heard the word that way.

---

## Why this principle exists

On 2026-11-15, chapter 42 was settled on silk A's 中 read as *within*, and the same change marked 中 as the sound part of 沖 on the atlas card. Shalom asked why a part would be marked *sound* when the line was drawing its meaning from it. The answer was that the two calls concern different things: the card describes how 沖 is built, and the note describes which word silk A wrote. The entry for 沖 puts them in separate sections for that reason (`glossary/chong-沖.md` → *The graph: water, and a sound* and *Chapter 42: the breath within*).

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 1** | the decomposition step says to keep a part's role and a bare-part variant's word apart |
| **`tools/import_shuowen.py` → `SOUND_PART_READINGS`** | the card's parse moves a part to *sound* only on the dictionary's own evidence, and lists every move as our reading in `sources/shuowen/entries.md` |
| **`sources/variants.yaml`** | holds the witness's word, with the word-or-spelling argument in the note |
| **`chapter-review` step 0** | `--applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |

**Not enforced, and cannot be.** Whether a bare part is a word or a spelling is a judgment about the witnesses, and whether a part carries meaning is a judgment about the character. No check can see either.

---

## Where it does not fire

**A part the dictionary marks 亦聲 (*yì shēng* — "also for sound")** carries both sound and meaning by Xu Shen's own analysis. The card records both, and a bare-part variant may then share the character's sense.

**A variant that writes a different whole character** (學 (*xué* — learning) for 教 (*jiào* — teaching) at ch 42) is an ordinary fork between words. No part is involved, and `witnesses-before-drafting` governs it.

**A character whose part is plainly there for meaning** does not raise the question: the card and the line agree.

---

## What it obliges

1. **On the card, record the part's role from the character's meaning and the dictionary's formulas.** Move a part between *sound* and *meaning* only with that evidence, and list the move as ours in `SOUND_PART_READINGS`.
2. **In the apparatus, record the word the witness writes**, and argue word or spelling with the three tests above, in the note.
3. **In a glossary entry, give the two facts separate sections**, and say that the sound link is how the readings came to share a spelling.
