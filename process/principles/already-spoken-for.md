---
id: already-spoken-for
title: "A rendering already spoken for by another character is not available"
status: active
since: 2026-09-10
trigger: "a rendering you want is already doing duty for a different character somewhere in the book"
applies: [drafting, glossary]
evidence: ["notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word", "notes/translation.md#ch-12-38-72-故去彼取此-they-let-go-of-what-is-out-there-and-take-what-is-here", "notes/translation.md#ch-15-16-25-32-44-52-殆-danger-and-the-death-radical-that-was-missing-from-all-four-englishes"]
check: none
supersedes: []
---

# A rendering already spoken for by another character is not available

**The rule.** Before an English word goes into the verse, ask which character already wears it. If another does, the word is taken — **and it stays taken even in a chapter where that other character does not appear.** The book is one text, and a reader who meets *harm* in chapter 35 and again in chapter 56 is entitled to assume they have met the same Chinese word.

**When it fires.** Whenever you settle on a rendering. Every time, not only when something feels wrong — this is the fault that never feels wrong, because the offending line is always defensible where it stands.

---

## Why this holds

**A lock is a claim in both directions, and only one of them can be checked.** *Every 強 (qiáng) renders* strong *and every* strong *renders 強.* `check_locks.py` can test the first, because its evidence gate keys off the character being present. **The second direction is unreachable by any tool**, and it is where the damage accumulates: 固 (*gù* — firm) and 壯 (*zhuàng* — in its prime) were both found wearing 強's English **inside chapters that contain 強**, where no rule can see them.

**The reason it goes unnoticed is that each instance is individually correct.** Nobody renders a character wrongly here. They render it with a perfectly good word that happens to be somebody else's. The fault is only visible from **above the chapter**, by asking the reverse question — and the reverse question is nobody's job unless it is made one.

**The instrument exists.** `concordance.py --english "<word>"` lists every line carrying a rendering and says which are backed by the character and which are not. It judges nothing; it is a search, not a gate, deliberately — a tool that gated and searched at once would be too noisy to gate and too quiet to search.

**And the "absent character" clause is the part that gets dropped.** It is tempting to reason *"覺 is not in this chapter, so* wake *is free here."* It is not free. The reader carries the whole book; the concordance carries the whole book; only the drafter is inside one chapter.

---

## Why this principle exists

**The holding family.** 執 · 守 · 保 · 持 — four characters with four different hands in 說文解字 (*Shuōwén Jiězì*) — had collapsed into *hold* across seventeen chapters, and ***guard* was being worn by three characters at once**: 守 (*shǒu*) at ch 9, 保 (*bǎo*) at ch 15, 衛 (*wèi*) at ch 67. The ch 15 decision had been argued from ch 9's literal gloss table, landing 保 on the English that 守 wears in the very chapter cited. → [the holding family](../../notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word)

***Embrace* was doing duty for four characters** — 抱 (*bào* — to embrace), 守 (*shǒu* — to hold to), 有 (*yǒu* — to have) and 取 (*qǔ* — to take) — before the ch 12/38/72 sweep freed it. → [故去彼取此](../../notes/translation.md#ch-12-38-72-故去彼取此-they-let-go-of-what-is-out-there-and-take-what-is-here)

**殆 (*dài* — danger) had five occurrences and four Englishes, and two of those Englishes belonged to other characters**: *harm* is 害's (35, 56, 66, 73, 81) and *inexhaustible* is 窮's (6, 35). → [殆](../../notes/translation.md#ch-15-16-25-32-44-52-殆-danger-and-the-death-radical-that-was-missing-from-all-four-englishes)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py --english`** | the reverse check the rule depends on: every verse line wearing an English, and whether its character is present. Named in `chapter-review` step 3 and `glossary-entry` §1 |
| **`check_locks.py`** · `forbidden-rendering` | holds the enforceable half — a locked term's rejected Englishes, wherever its character stands in the chapter |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Partly enforced.** A word taken by a character in a chapter the two never share is invisible to any gate; `--english`, run by hand, is the only instrument that finds it.

---

## Where it does not fire

**A common English function word is not owned by anybody.** *Hold* in *"these words hold"* renders no character and claims none; that is ordinary English, and it is governed by [[renders-no-character]] instead.

**A locked flexion is not a collision.** 守 reads *hold to* and *guard*, both recorded; 執 reads *grasp* and *seize* at ch 74. A lock is on **register**, not on one English word, and the entry states which flexions are licensed.

**Two characters may legitimately share an English where no chapter holds both and the entries say so** — but this is rare, costly, and must be argued in the glossary rather than assumed. The default is that a word is taken.

**And a `forbidden:` list cannot enforce this.** It gates on the character being present, so it can never express *right for that character, wrong for this one, same chapter.* Both `chi-持.md` and `zhi-執.md` carry a section saying exactly which words they could not forbid and why. **That is the boundary of the machinery and the beginning of the reader's job.**

---

## What it obliges

1. **Run `concordance.py --english "<the rendering>"` on every lock you settle** — and on any rendering you are pleased with, which is the reliable signal that it came from English rather than from the character.
2. **When the word is taken, say whose it is in the note.** *"Harm is 害's"* — one clause, and it makes the decision auditable.
3. **When you free a word, sweep the chapters it was wrongly wearing, immediately.** Fix on discovery, not in a deferred batch.
4. **Record in the glossary entry which words could *not* be forbidden and why.** The unenforceable half is the half a future reader most needs told.
