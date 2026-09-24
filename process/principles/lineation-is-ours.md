---
id: lineation-is-ours
title: "The marks are ours; the music is the source's"
status: active
since: 2026-08-11
trigger: "you are deciding line breaks, stanza breaks or punctuation anywhere in the verse"
applies: [drafting, notes]
evidence: ["notes/translation.md#ch-4-56-挫其銳解其紛和其光同其塵-the-nouns-unified-the-subject-deferred", "notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english", "notes/translation.md#ch-41-the-建言-catalogue-rebuilt-and-建-licensed-to-flex"]
check: fix-linebreaks
supersedes: []
---

# The marks are ours; the music is the source's

**The rule.** The ancient text carries **no punctuation and no line breaks** — unbroken columns of characters. Every comma, period and break in every modern edition is a later editor's. So on the page, punctuation and lineation are **ours**, to use freely and deliberately. **But the source is not formless.** Classical Chinese moves in regular character-beats and parallel pairs and triads, and that pulse is audible without a single mark. Lay the English out freely; let the layout **track** the original's rhythm rather than cut across it.

**When it fires.** Every time you break a line — and especially when an instinct says *join these two*. That instinct is usually right and almost always incomplete.

---

## Why this holds

**Two freedoms are being distinguished, and collapsing them is the error.** The marks are genuinely ours: there is nothing to be faithful *to*, because there is nothing there. The **music** is not ours at all. A six-phrase series in even three-character beats is a fact about the source, and a layout that gives four of those phrases their own lines while fusing the last two has **quietly overridden a symmetry the text is holding** — without changing a single word, and without anything in the line looking wrong.

**This is the layout half of a rule the project already holds about words.** *Where the Chinese repeats itself, repeat yourself.* Lineation is the same claim one level up: where the Chinese weighs phrases equally, weigh them equally. Chapter 11 taught it with words; chapter 56 taught it with breaks.

**The consistency requirement is what makes the freedom safe.** Freedom in the marks plus discipline in the music means: when you feel the pull to bind two phrases — as 和光同塵 (*hé guāng tóng chén* — "dim the light, merge with the dust") is one bound gesture — **trust it, then extend it**, so the whole series is treated alike. An unextended instinct is how a symmetry gets broken by good taste.

**And it is load-bearing outside the poetry.** `sources/PROVENANCE.md` records that modern editions' punctuation is editorial and forms no part of the source — the one element of a printed Chinese text that could carry a thin copyright claim. **Because our lineation is demonstrably our own, the CC0 dedication is clean.** The aesthetic rule and the licensing position are the same fact.

---

## Why this principle exists

**Ch 56's six phrases are three couplets**, and ch 4 carries four of the same six. Following the established lineation rather than making a fresh choice is what kept the two chapters answering each other. → [ch 4, 56](../../notes/translation.md#ch-4-56-挫其銳解其紛和其光同其塵-the-nouns-unified-the-subject-deferred)

**Ch 57 keeps its colon** where chapters 21 and 54 take a full stop — because the colon is punctuation, not a word, and ch 57's 以此 (*yǐ cǐ* — "by this") is the only one of the three that points **forward**, opening the list that follows. The marks do work the Chinese leaves to position. → [以此](../../notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english)

**Ch 41's 建言 (*jiàn yán* — "established sayings") catalogue had twelve proverbs packed onto five lines.** Rebuilt one saying per line, the catalogue reads as a catalogue — which is what it is. → [ch 41](../../notes/translation.md#ch-41-the-建言-catalogue-rebuilt-and-建-licensed-to-flex)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`tools/fix-linebreaks.py`** | restores the two trailing spaces a verse line needs; `chapter-review` step 7 |
| **CI**, *verse line breaks* | runs `fix-linebreaks.py --check` and fails on a collapsed stanza |
| **`.editorconfig`** | keeps editors from trimming the trailing whitespace the line breaks are made of |
| **`chapter-review` step 6** | *let the layout track the original's rhythm* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Enforced** for the hard breaks. Whether the lineation tracks the source's beats is judgment.

---

## Where it does not fire

**This is not licence to lineate by feel.** The freedom is in the marks *given* the music; a layout that ignores the beat is not exercising the freedom, it is declining the discipline.

**It does not govern the em-dash.** That is standing rule 5 in `CLAUDE.md`, and its reason is grammatical rather than musical — a dash **strands subjects**, which classical Chinese may omit and English may not.

**It does not govern capitalisation**, which is standing rule 5's other half and is enforced by `check_locks.py`.

**And a mark is not a word.** A colon may carry direction, as at ch 57; it may not carry a character. Where punctuation starts doing a character's work, the problem is the rendering.

---

## What it obliges

1. **Count the beats before you break the lines.** Where the Chinese is a series of even phrases, the English lineation says how many there are.
2. **Extend every joining instinct across the whole series**, or take it back.
3. **Run `python3 tools/fix-linebreaks.py` after editing any verse.** A line break here is a CommonMark hard break — two trailing spaces — and markdown silently collapses a stanza without them. Never trim trailing whitespace in `.md`.
4. **When a chapter shares phrases with another, follow the lineation already settled** rather than deciding again.
