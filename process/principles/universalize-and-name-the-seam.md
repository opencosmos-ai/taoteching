---
id: universalize-and-name-the-seam
title: "Universalize over the text's incidental male-default — and name the seam, never erase it"
status: active
since: 2026-08-11
trigger: "the Chinese assumes a male subject or a male social class and your English does not have to"
applies: [drafting, notes]
evidence: ["notes/reading.md#thread-reading-past-the-throne-and-past-the-male-default", "notes/reading.md#thread-the-mother-and-her-kin-the-feminine"]
check: none
supersedes: []
---

# Universalize over the male-default — and name the seam

**The rule.** The text exalts the feminine as principle and assumes the male as cultural default. Where the two collide, **render toward the universal** — and **say in the notes that you did.** Never erase the male-centrism silently.

**When it fires.** Whenever a Chinese term names a male role or class and the English has a neutral option: 士 (*shì*), 君子 (*jūn zǐ*), 聖人 (*shèng rén*), 大丈夫 (*dà zhàng fū*), and every pronoun for an archetypal figure.

---

## Why this holds

**Both halves are load-bearing, and each without the other fails.**

**Universalizing without the note falsifies the source.** It produces a text that looks as though a Warring States author wrote gender-neutrally, which he did not, and it removes the reader's ability to see what was changed. That is the same offence as an overlay, committed with better intentions.

**Noting without universalizing keeps the reader out.** The book's claims are about anyone who stands on the ground. A translation that reproduces 士 as an exclusively male officer class delivers a text about somebody else's society when the Chinese delivers one about the reader.

**And the tension is genuinely in the text, not imposed on it.** This is the book that makes 母 (*mǔ* — mother), 牝 (*pìn* — the female animal), 雌 (*cí* — the hen) and 谷 (*gǔ* — valley) its central images of power, while addressing rulers who were men. **Naming the seam is how the edition reports that honestly** rather than resolving it in either direction.

**The sage is never "he."** Singular *they* is not a compromise here; a gendered pronoun makes a claim about the archetype that the Chinese, which has no pronoun there at all, does not make.

---

## Why this principle exists

**The throne and the male default** run together as a reader-facing thread, which distinguishes *where the manuscripts side with us*, *where we universalize on our own authority and say so*, and *where the text needs no help*. That three-way sorting is the rule in practice. → [Thread](../../notes/reading.md#thread-reading-past-the-throne-and-past-the-male-default)

**The feminine thread** is the other half — 母, 牝, 雌, 谷, 嬰兒 — and it is why the seam exists at all. → [Thread](../../notes/reading.md#thread-the-mother-and-her-kin-the-feminine)

**士 is the worked instance.** Settled as *in service* across chapters 15, 41 and 68 — 說文 士，事也, one who handles **affairs** — with the seam noted: **士 named a male class and the English is deliberately neutral.**

---

## How it is implemented

| Where | What it does |
|---|---|
| **`check_locks.py`** · `sage-pronoun` | fails on *he / his / him* near the sage — an absolute rule, never gated on the Chinese |
| **`CLAUDE.md`** standing rules 1–2 · **`chapter-review` step 6** | the rule stated where drafting happens |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Half enforced.** The pronoun is gated; naming the seam in the note is not.

---

## Where it does not fire

**Where the maleness is the point, keep it.** 大丈夫 at ch 38 is a rank word about men; it reads *the great person* by Shalom's call, and the seam is recorded rather than papered.

**Where a character is grammatically feminine and the image requires it**, render it — 牝 and 雌 are hen and female animal, not neutral.

**And it does not extend to the throne.** Rulers in this book are rulers; universalizing 侯王 into leadership-in-general is a different act, and a distorting one. **The male default is incidental; the political address is not.**

---

## What it obliges

1. **Never "he" for the sage, or for any archetypal figure.** Singular *they*, or recast.
2. **When you universalize, put one sentence in the chapter note** saying what the Chinese assumed and what the English did.
3. **Sort each case three ways** — the manuscripts agree · we universalize on our own authority · the text needs no help — and say which.
4. **Where a neutral English would flatten a real image, keep the image** and note the cost instead.
