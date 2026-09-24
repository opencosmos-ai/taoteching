---
id: witnesses-before-drafting
title: "Check the witnesses before drafting, not after"
status: active
since: 2026-08-20
trigger: "you are about to read a chapter's base text closely, or about to change a settled line"
applies: [drafting, notes]
evidence: ["notes/manuscript.md#ch-25-王亦大-人亦大-king-or-human-among-the-four-greats", "notes/manuscript.md#ch-21-道之為物-道之物-the-silks-drop-the-copula"]
check: none
supersedes: []
---

# Check the witnesses before drafting, not after

**The rule.** Run `concordance.py --witnesses N` **before** reading the base text closely. Whether the oldest witnesses carry the chapter at all, and where they disagree with it, changes what you are translating — and it cannot be discovered by reading the received text more carefully.

**When it fires.** At the start of every chapter, and again before changing any line that is already settled.

---

## Why this holds

**A base text is one witness, not the text.** Ours is 王弼 (*Wáng Bì*), third century CE, and the chapters reach us through transmitters who emended. Reading it closely tells you what **that** text says; it cannot tell you the line was added, reversed, or is absent from everything older.

**Attestation changes how much weight the base can bear.** Guodian (~300 BCE) carries **31 of 81 chapters**. *Not attested* means the chapter rests on the silks and later — a fact about confidence that should be visible while drafting, not discovered afterwards. It decided ch 4 against ch 56: ch 56 held the ground because it is attested **complete** at Guodian; ch 4 is not attested at all.

**And a blank result is not an answer.** `sources/variants.yaml` is built by hand, chapter by chapter. **A blank means nobody has checked that chapter yet**, not that there are no forks — and the tool says so.

---

## Why this principle exists

Two chapters were drafted before anyone read the witnesses, and neither was carelessness — nobody had looked. Ch 21 was drafted over a chronology both Mawangdui silks reverse, 道之為物 against 道之物. Ch 25 was drafted with a king among the four greats that the oldest witnesses do not have, 王亦大 against 人亦大. → [ch 25](../../notes/manuscript.md#ch-25-王亦大-人亦大-king-or-human-among-the-four-greats) · [ch 21](../../notes/manuscript.md#ch-21-道之為物-道之物-the-silks-drop-the-copula)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py --witnesses N`** | the forks for a chapter, opening with whether Guodian carries it at all. `chapter-review` step 0, run first |
| **`check_locks.py`** · `unlogged-variant` | fails a meaning-bearing fork with no logged decision |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Partly enforced.** A recorded fork must be logged; whether anyone looked at the witnesses before drafting is not checkable.

---

## Where it does not fire

**It does not license following a witness by default.** The base text is the base; departing from it is a decision that gets argued and recorded, as at ch 39's 故致數譽無譽 and ch 29's 挫 → 載.

**And a claim about a manuscript is not evidence unless it is in `sources/variants.yaml`.** A transcription found elsewhere may have been emended — see [[record-the-fact]].

---

## What it obliges

1. **Run `--witnesses N` first, before the close reading.** The tool opens with whether Guodian carries the chapter at all.
2. **Read a blank result as "nobody has looked."** Then look, and record what you find.
3. **Record new forks as facts, never transcriptions.** See [[record-the-fact]] — that is a licensing rule, not a preference.
4. **Log meaning-bearing forks in `notes/manuscript.md`** as well as the apparatus.
