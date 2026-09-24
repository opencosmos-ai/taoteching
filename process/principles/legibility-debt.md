---
id: legibility-debt
title: "A rendering chosen for one chapter's legibility owes the connection it forgoes to the notes"
status: provisional
since: 2026-09-10
trigger: "you are about to render a character by what it means in this line rather than by the word it carries elsewhere in the book"
applies: [drafting, notes]
evidence: ["notes/translation.md#ch-14s-opening-triad-夷-希-微-the-names-and-why-the-verse-gives-their-meanings"]
check: none
supersedes: []
---

# A rendering chosen for legibility owes the connection it forgoes to the notes

**The rule.** Where a character is rendered by **what it means in this line** rather than by **the word it carries across the book**, the reading gained here is paid for by a thread lost everywhere else. That is a legitimate trade and this edition sometimes takes it. **What is not legitimate is taking it silently.** The connection the verse gives up becomes an obligation on the notes: an anchor note where the choice was made, and a pointer in every chapter the lost thread runs through.

**When it fires.** Any time the honest argument for a rendering is *"but the other word is opaque right here."* That sentence is the signal. It is a real argument — it is not a symptom of laziness — and it should win sometimes. It just never settles the matter on its own.

---

## Why this holds, beyond the case that produced it

**A translation of a book has two readers and they want opposite things.** The reader moving through one chapter wants that chapter to land. The reader who has read all eighty-one — and the reader who will read this against the Chinese, and the reader building on the work — wants the book's own vocabulary to be visible, because **the repetitions are the argument.** This edition already treats that as settled in the other direction: *where the Chinese repeats itself, repeat yourself.* Chapter 11 says one sentence three times over a cart, a pot and a room, and varying the English was a fault even though no single line was wrong.

**Those two readers cannot always be served by the same sentence, and pretending otherwise is how both get cheated.** A rendering forced to carry the book-wide thread at all costs produces lines nobody can read. A rendering optimised line by line produces eighty-one clear chapters and no book. The trade is real.

**What makes it survivable is that the loss is recoverable somewhere else.** A connection dropped from the verse can be restored in a note at no cost to the poetry — that is what the notes layer is *for*. A connection dropped from the verse **and not written down anywhere** is not a trade. It is a deletion, and it is invisible: no check can find it, because every affected line is individually correct.

**That invisibility is the whole reason this needs to be a rule.** Every gate in this repository keys off a forbidden word appearing where it should not. A character quietly rendered two ways in two chapters, both defensible, trips nothing. `check_locks.py` cannot see it, `--formulas` cannot see it, and the reverse check with `--english` only finds it if someone thinks to run it on the right word. **The obligation has to be discharged at the moment of the decision, because nothing downstream will remind you.**

---

## Why this principle exists

Chapter 14 names three characters — 夷 (*yí*), 希 (*xī*) and 微 (*wēi*) — in a definition passage, 名曰X three times. Each is rendered by its meaning here (*the invisible · the inaudible · the intangible*) rather than by the word it carries elsewhere (*level* at 41 and 53; *barely heard* at 41 and *sparse* at 23, 43, 70, 74; *faint* at 15 and 64). 王弼 (*Wáng Bì*) argues against that choice directly, defining 希 at chapter 41 by quoting chapter 14 outright — 聽之不聞名曰希, *"listen but you cannot hear it, its name is called 希"* — which makes 大音希聲 and 名曰希 one word by his own hand.

**The choice went to legibility**, because chapter 14 is early and three bare adjectives give a reader nothing to hang them on. The debt was then paid: an anchor note at chapter 14 carrying all three graphs and their recurrences, and a thread note in chapters 15, 23, 36, 41, 43, 53, 64, 70 and 74 pointing back — with chapter 41 carrying 王弼's counter-argument as well as the pointer, since that is where he makes it.

Full argument: [`notes/translation.md` → Ch 14's opening triad](../../notes/translation.md#ch-14s-opening-triad-夷-希-微-the-names-and-why-the-verse-gives-their-meanings).

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 7** | the anchor note where the choice was made, and the thread notes in every chapter the forgone reading runs through |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Not enforced.** The thread notes are the part that gets skipped, and nothing checks that they were written.

---

## Where it does not fire

**This is not a licence to render freely and write a note about it.** The note is the price of a trade, not a way of buying one. Three conditions have to hold before the trade is even available:

- **The book-wide word must actually be opaque *here*, not merely plainer than you would like.** *"Its name is the level"* is opaque. A word being less lovely is not opacity.
- **The two readings must be the same character doing one thing**, visible once pointed out. 夷 as *level* and as *the invisible* are one property — what is perfectly level has no feature to catch the eye. Where the two readings are genuinely different senses, this is a licensed flexion and belongs in the glossary entry, not here.
- **The chapter must be the one that loses.** Where the split is between two chapters that are equally clear, there is no legibility to buy and the book-wide word simply wins.

**And it does not apply to a locked term.** A lock is a claim in both directions and is settled in `glossary/`; setting one aside for legibility is a different act with a different home — `process/shaloms-call.md`, or a `lock-ok` waiver with its reason.

---

## What it obliges

1. **Say in the chapter note that the trade was made, and what was given up.** Not *"we render X as Y"* but *"X reads Y here and Z elsewhere, and here is why."*
2. **Write the anchor note where the choice was made** — the graph, the reading taken, the reading declined, and the full list of chapters the other reading runs through.
3. **Write a thread note in every one of those chapters**, pointing back. This is the part that gets skipped, and skipping it converts the trade into the deletion.
4. **Carry the counter-argument where it is strongest**, not only where it was overruled. A reader who reaches the chapter that makes the best case against the choice should find it acknowledged there.
5. **Open a `WORKLIST.md` row if the recurrences still disagree among themselves.** Settling the chapter that lost does not settle the ones that won.
