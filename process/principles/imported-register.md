---
id: imported-register
title: "Register is a claim — a line that would sit in a sermon has made one"
status: active
since: 2026-09-10
trigger: "a rendering would sit comfortably in a sermon, a hymn, or a 1971 paperback on consciousness"
applies: [drafting, glossary]
evidence: ["notes/translation.md#register-no-modern-spiritual-idiom", "notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english", "notes/translation.md#ch-74-a-register-correction-and-what-caused-it"]
check: none
supersedes: []
---

# Register is a claim — a line that would sit in a sermon has made one

**The rule.** Register asserts things vocabulary does not. A rendering can translate every character correctly and still tell the reader **what kind of book this is** — scripture, or self-help, or a manual of ordered nature. Two registers are foreclosed here: **devotional** (the missionary inheritance) and **modern spiritual idiom** (the counterculture inheritance). A third, **mechanistic**, is this edition's own besetting temptation.

**When it fires.** When a line sounds finished. Elevation reads as authority, and authority reads as correctness, so the sermonic line is the one least likely to be questioned.

---

## Why this holds

**The English Tao Te Ching was largely built by missionaries, and the vocabulary carries their theology as sediment.** Legge translated for the London Missionary Society. In the Chinese Union Bible, **John 1:1 reads 太初有道** — 道 (*dào*) for *Logos*, 神 (*shén*) for *God*. The standard renderings are not neutral words that happen to sound religious; they are **a theological programme that succeeded**, and using them re-runs it.

**The counterculture inheritance is newer and equally specific.** *"Here, now"* is not a neutral English phrase — it is *Be Here Now*, 1971, and it installs a whole apparatus of assumptions about what the book is for. Ch 21's 此 (*cǐ* — this) had taken exactly that phrasing, lifted out of 河上公 (*Héshàng Gōng*)'s gloss 此，今也 and landed in a register the commentator does not occupy.

**And the mechanistic one is ours.** *Operating system*, *source code*, *generate*, *system*. It feels like the opposite of an overlay — deflationary, modern, unmystical — and it is the same act: a vocabulary from elsewhere, deciding in advance what kind of thing the Tao is. Ch 29's 神器 (*shén qì* — sacred vessel) read *"sacred system,"* and the chapter's argument went with it: **you can grasp at a vessel and break it; you cannot grasp a system.**

**The reason this needs to be a rule rather than taste is that register survives character-level correctness.** Every gate here keys on a word. A line can pass every lock, render every character, and still be a hymn.

---

## The three tests

| | |
|---|---|
| **The hymn test** | would this line sit comfortably in a sermon? Then check the character. |
| **The pointing test** | could Laozi have pointed at it? His vocabulary is water, valley, wood, dust, an infant. |
| **The 1968 test** | could this have been printed in a paperback on consciousness? Then it is the other overlay. |

**Flag on sight**, per `process/overlay-audit.md`: 聖 ("holy" — it means *acute hearing*) · 神 ("God" — *numinous potency*) · 鬼 ("demons" — *ghosts, the dead*) · 罪 ("sin" — *crime*) · 義 ("righteousness" — *duty*) · 仁 ("benevolence" — *humaneness*) · 精/魄 ("soul" — *vital essence* / the *corporeal* soul) · 一 ("the One" — Neoplatonism) · 福 ("blessing" — *good fortune*) · 善 ("good" — often *skilled*) · 道法自然 (never "the Tao follows Nature" — that inverts the chapter).

**And watch the grammar, not only the words.** KJV cadence, devotional capitalisation, and abstraction drift each carry the register with no forbidden word present. The definite article alone did it once: *"the one"* turns a tally mark into a title.

---

## Why this principle exists

**§1's register rule** was written after *"here, now"* and the *Be Here Now* family were caught in the verse. → [Register](../../notes/translation.md#register-no-modern-spiritual-idiom)

**以此 across ch 21, 54 and 57** — the phrase had three Englishes, one of which was a commentator's gloss in a 1971 register. Now *"By this."* in all three. → [以此](../../notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english)

**Ch 74's register correction**, where the cause was identified as well as the symptom. → [ch 74](../../notes/translation.md#ch-74-a-register-correction-and-what-caused-it)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 4** | the overlay watchlist, the hymn test and the pointing test |
| **`glossary-entry` §2** | the same two tests, applied to every sentence of an entry |
| **`check_locks.py`** · `forbidden-rendering` · `devotional-capitalization` · `mechanistic-register` | catch the known overlay words and the capitals that turn a word into a doctrine |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Partly enforced.** The known words are gated; a new overlay has no entry on any list until someone recognises it.

---

## Where it does not fire

**Not everything churchy-sounding is an import, and the danger runs both ways.** The book *is* sometimes solemn, and flattening it to avoid a suspicion is its own distortion. 玄 (*xuán*) is genuinely dark and strange; rendering it plainly because *mysterious* sounds devotional loses the character.

**Some characters are religious.** 祭祀 (*jì sì* — sacrificial offering) at ch 54 is a rite. Render it as one.

**Deflation can be an overlay too.** *"Just"*, *"merely"*, *"simply"* impose a modern anti-metaphysical stance as surely as a capital letter imposes a doctrine.

**And 道 keeps its capital** — because *Tao* is transliterated, not translated. It is a proper name, and it is the one exception; nothing else takes one.

---

## What it obliges

1. **Run all three tests on any line that sounds finished**, and on any line you are pleased with.
2. **When a test flags something, go to the character** — the test is a detector, not a verdict. Roughly a third of flags are false.
3. **Record the overlay you declined, and name it.** *"Brilliance is 明's forbidden word and 光 is 明's counter-term"* is auditable; *"too religious"* is not.
4. **Watch the commentary hardest.** 天誅 (*tiān zhū*) is *nature's reckoning*, not *Heaven's judgment* — and the pull toward the second is strongest in the glosses, where no checker is looking.
