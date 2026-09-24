---
id: perform-dont-label
title: "Correct an overlay by performing it, not by labelling it more accurately"
status: active
since: 2026-09-06
trigger: "you have caught an imported overlay and are reaching for a more accurate abstraction to replace it"
applies: [drafting, glossary]
evidence: ["notes/translation.md#ch-10-five-englishes-attached-to-characters-that-are-not-in-the-chapter", "notes/translation.md#ch-28-the-pointing-test-failed-on-nearly-every-line"]
check: none
supersedes: []
---

# Correct an overlay by performing it, not by labelling it more accurately

**The rule.** When the watchlist catches an imported word, the repair is **not a better label**. A more accurate abstraction is still an abstraction, and it usually reads as jargon — the overlay replaced by a technical term for the overlay. **Render what the character shows, and let the English do the work the label was describing.**

**When it fires.** The moment after a catch, when you know what the word *means* and are looking for an English noun-phrase that says so.

---

## Why this holds

**The overlay and the corrective label are the same kind of move.** Both name the thing from outside it. `CLAUDE.md` flags 精/魄 (*jīng* / *pò*) → *soul*, and the corrective for 魄 is that it is the **corporeal** one. Saying so with a possessive — ***"the body's soul"*** — states the correction accurately and produces a phrase no reader can hear. **The scholarship is right and the line is dead.**

**Laozi's vocabulary is things, and that is the pointing test.** Water, valley, wood, dust, an infant, a bellows, a cart's hub. A label stops the reader to explain; the thing keeps them moving. When the repair reaches for an abstraction, it has swapped one register for another rather than returning to the text's.

**And a verb can carry what a noun-phrase can only assert.** ***Housing*** performs 營 (*yíng*) — and renders the character's own graph while doing it — where *"the body's soul"* merely declares the corporeal reading. The verb does the work and gets out of the way.

**The rule generalises past the watchlist.** Any time a rendering is caught as too abstract, the reflex is to reach for a more precise abstraction. The move that actually works is to reach **down**, for the thing the character draws.

---

## Why this principle exists

**Ch 10's 營魄.** *Soul* was the overlay; *"the body's soul"* was the accurate label; ***housing*** was the repair. **Four Englishes were blocked on the way, and which ones is the useful record**: *spirit* is 神's (6, 39, 60); *flesh* is Pauline — the flesh against the spirit, Romans 8 — which is the hymn test; *quarters* was taken four lines below by the chapter's own 四達; and ***body* is 身's**, avoided rather than borrowed even though 身 does not occur here. → [ch 10](../../notes/translation.md#ch-10-five-englishes-attached-to-characters-that-are-not-in-the-chapter)

**Ch 28's 雄/雌.** The line read *"assertive/yielding energy"* — a label, and a New Age one. The repair is **rooster and hen**, two birds, forced by 牝/牡 already holding *male* and *female*. The chapter failed the pointing test on nearly every line, and every repair was of this shape. → [ch 28](../../notes/translation.md#ch-28-the-pointing-test-failed-on-nearly-every-line)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`glossary-entry` §2** | *read the character as a picture changing over time* — go to the graph before the meaning |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Not enforced.** It governs how an overlay is corrected, which is judgment.

---

## Where it does not fire

**Some characters are abstract and must stay so.** 道 (*dào*), 德 (*dé* — integrity), 常 (*cháng* — the ever-present) are not concealed objects, and concretising them invents an image the Chinese has none of.

**A gloss in the notes should label freely.** The reader-facing note is exactly where *"the corporeal soul"* belongs. **The rule governs the verse.**

**And performing is not paraphrasing.** *Housing* renders 營's graph; it is not a description of what 營魄 is about. If the performing word renders no character, [[renders-no-character]] fires instead.

---

## What it obliges

1. **After a catch, go back to the graph** and ask what it draws before asking what it means.
2. **Try a verb before a noun-phrase.** Verbs perform; noun-phrases assert.
3. **Record which Englishes were blocked and why** — the list is more useful to the next drafter than the word finally chosen.
4. **Put the accurate label in the note**, where it does no harm and real good.
