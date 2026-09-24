---
id: ruling-and-enforcement-are-two-facts
title: "Say which of an entry's rulings the build can hold, and which only the reader can"
status: active
since: 2026-09-20
trigger: "you are writing a lock line whose never-list includes a word that another character in the same chapters may legitimately print"
applies: [glossary, tooling]
evidence: ["notes/translation.md#身-shēn-body-one-character-that-had-six-englishes", "notes/translation.md#the-error-that-had-no-name-guard-was-worn-by-three-characters"]
check: none
supersedes: []
---

# Say which rulings the build can hold, and which only the reader can

**The rule.** A glossary entry states two different kinds of thing and they look identical on the page: **what the verse may not say**, and **what `check_locks.py` will stop it saying**. Every entry must make the difference visible at the point where a reader first meets the never-list, and name the unenforceable rulings rather than quietly leaving them out.

**When it fires.** You are writing or revising a lock line, and one of the words you want to forbid is a word some *other* character can legitimately print in one of the same chapters.

---

## Why this holds

**The gate is chapter-scoped, and rulings are not.** `check_locks.py` earns its trust by never firing on English alone — a forbidden word is an error only when its character stands in **that chapter's own Chinese**. See [[evidence-gate]]. The consequence is structural: the checker **cannot express *right for that character, wrong for this one, same chapter***. So the moment two characters share a chapter and one of them owns the English word the other must not take, the ruling becomes unenforceable — permanently, and by design rather than by oversight.

**An entry that does not say so misleads in one of two directions.** List the word beside enforced ones and the reader concludes the build is holding it, which it is not. Leave it out to avoid the confusion and the reader never learns the ruling exists at all — which is worse, because the unenforceable words are exactly the ones a future draft will reach for. They are unenforceable *because* a neighbouring character makes them plausible.

**Both failures were live in this repository at once.** Four entries in the holding family carry an unenforceable ruling. Two of them stated the word in the opening never-list as though the build held it; two omitted it entirely and disclosed it only at the foot of the page. None of the four said which kind of claim it was making until 2026-09-20.

**This is the glossary's version of `check: none`.** `process/principles/README.md` requires that field to be *written, not omitted*, so that the gap is visible rather than assumed. The same honesty is owed inside an entry, and for the same reason: a rule nobody enforces is fine, and a rule everybody assumes is enforced is not.

---

## Why this principle exists

**身 (*shēn*) and *self*.** The entry's opening ruled out *spirit*, *soul* and *self* in one breath. The first two are on the `forbidden:` list; the third cannot be, because 身 shares chapter 7 with 私 (*sī* — private interest) and chapters 13, 16 and 54 with 我/吾 (*wǒ / wú*), all of which may legitimately print *self*. Shalom read the entry, hit *"never the self"* at the top and *"'self' is not on the forbidden list, and cannot be"* near the bottom, and asked which it was. → [身](../../notes/translation.md#身-shēn-body-one-character-that-had-six-englishes)

**守 (*shǒu*) and *keep*, and two more beside it.** 守's entry avoided the contradiction by **omission** — *keep* appeared nowhere in the opening and surfaced only in the closing section. 保 (*bǎo*) does the same with *guard*, 持 (*chí*) with *grasp*. Each is blocked by a sibling: 保 stands with 守 in chapters 9 and 67, 執 (*zhí*) with 持 in chapter 64. The silence is the worse failure of the two, because it gives a future drafter no warning at all. → [the holding family](../../notes/translation.md#the-error-that-had-no-name-guard-was-worn-by-three-characters)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`glossary-entry` §2** | the entry standard: a word ruled out but not forbiddable is named in the lock line and explained under *What no rule can enforce* |
| **Glossary entries** | `bao-保`, `chi-持`, `shou-守`, `shen-身` and `zhi-治` each carry the section |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |

**Not enforced.** Whether an entry discloses what its list cannot hold is a reading question.

---

## Where it does not fire

**Not on every word left off a `forbidden:` list.** Most omissions are ordinary — the list holds the renderings that have actually been tried or are actually tempting, not every English word the term is not. This rule fires only where there is a **ruling** the entry means to make and the gate structurally cannot carry.

**Not on a declared flexion.** 執 → *seize* at chapter 74 and 保 → bare *keep* at chapter 9 are the opposite case: a sense the lock **licenses** in a named place. Those are already required to be stated, and they are enforceable by reading the entry rather than by running the build.

**Not on `CLAUDE.md`'s standing rules.** They are read every session and several are enforced; the asymmetry this rule addresses is one that lives inside a single entry.

---

## What it obliges

1. **Name the unenforceable ruling in the lock line**, marked as such, with a pointer to the section that explains it. Do not omit it, and do not list it as though it were held.
2. **In *What no rule can enforce*, state both facts and separate them** — *the ruling holds; the enforcement does not exist* — then say which words the build **does** hold, so the two sets are visible side by side.
3. **Name the blocking character and the shared chapters.** That is what makes the claim checkable by a reader, and it is the only evidence there will ever be.

A narrower string is sometimes available and is worth taking: `身` forbids `"the separate self"` and `"the ego"`, which no other character can claim, while leaving the plain word to the reader. **Say when you have done this**, or the frontmatter and the prose will read as a contradiction to anyone who opens `terms.yaml`.

---

*Kin to [[already-spoken-for]], which is the rule that creates these collisions in the first place, and to [[evidence-gate]], which is why they cannot be gated. [[never-silence-a-rule]] governs the other direction: an enforced rule is never deleted to quiet it.*
