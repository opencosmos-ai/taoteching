---
id: name-the-referent
title: "Classical Chinese can leave a referent floating where English cannot — name it and end the sentence"
status: active
since: 2026-09-06
trigger: "your English carries a pronoun, a participle or a dash whose subject the reader has to guess"
applies: [drafting]
evidence: ["notes/translation.md#ch-22", "notes/translation.md#typography-lowercase-and-no-em-dashes-in-the-verse", "notes/translation.md#ch-9-three-verbs-for-keeping-and-the-english-had-one"]
check: none
supersedes: []
---

# Classical Chinese can leave a referent floating where English cannot

**The rule.** Classical Chinese drops subjects and carries light particles that do not demand resolution. English has neither habit: an unresolved pronoun or a dangling participle does not read as *open*, it reads as **misdirection**. So where the Chinese leaves a referent floating, **name it and end the sentence** — do not reproduce the floating with an English word that behaves differently.

**When it fires.** Any time the English has an *it*, a *they*, a participle, or a dash standing where the Chinese has a particle or nothing at all.

---

## Why this holds

**The two languages fail in opposite directions.** 之 (*zhī*) is a light particle; a Chinese reader passes over it without being asked to settle anything. English *it* arriving after two live candidates **actively selects** — usually the nearer one — so a translator who declines to resolve has not preserved the openness. **They have made a choice and hidden it in a pronoun.** The Chinese is not vague there; the English is.

**And the same fault wears a second costume.** A dash lets a clause trail into a participle whose actor is unnamed. Ch 2's *"the sage does not begin them — giving birth without possessing…"* left a reader unable to tell whether the sage or the countless things were doing the giving. **That is the real reason the em-dash is barred from the verse** — not the machine-prose tell, which is the lesser of the two arguments. Classical Chinese omits subjects freely; English cannot, and **a dash disguises the omission instead of resolving it.**

**Shalom catches this from the reader's side, and that is the diagnostic.** The question *"what does 'it' refer to?"* is never answerable by pointing at the Chinese — the Chinese does not say. It is answerable only by deciding, which means the decision was already being made silently.

**The genuine ambiguities are elsewhere and are handled differently.** Where a line is really double, the answer is an English that holds both, argued and recorded. See [[divergence-stays-open]]. A floating pronoun holds nothing; it just hides which way the sentence fell.

---

## Why this principle exists

**Ch 22's 之.** An intermediate draft read *"Stay whole, and return to it,"* and Shalom asked what *it* referred to — the words, or wholeness. **The Chinese does not say, and English had already answered.** The referent was named. → [ch 22](../../notes/translation.md#ch-22)

**Ch 2's stranded subject** is the same fault behind a dash, and it is what the typography rule is actually protecting against. → [Typography](../../notes/translation.md#typography-lowercase-and-no-em-dashes-in-the-verse)

**Ch 9's 之, twice.** A draft read *"To hold it and fill it is not as good as stopping"* for 持而盈之, and Shalom asked what was being held and filled. The old published line had answered the question by **inventing a vessel** — 器 (*qì*) is not in the chapter, and is a locked term belonging to nine other chapters. **Both are the same failure**: one hid the choice in a pronoun, the other made the choice and imported a noun to carry it. The resolution was to name the referent **grammatically** — *what you hold* — which resolves the pronoun without adding a character. → [ch 9](../../notes/translation.md#ch-9-three-verbs-for-keeping-and-the-english-had-one)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *ask what every pronoun points at* |
| **`chapter-review` step 6** | no em-dashes in the verse |
| **`check_locks.py`** · `em-dash` | flags a dash in the verse, at `info` |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |

**Partly enforced.** The dash is flagged; a floating pronoun is not, because nothing can tell which of two antecedents the English meant.

---

## Where it does not fire

**A pronoun with one candidate is fine.** English needs pronouns; the rule is about **competing** referents, not about pronouns as such.

**Deliberate agentlessness is not a floating referent.** *"Where trust runs short, there is no trust"* has no agent **on purpose**, because 王弼 (*Wáng Bì*) reads the line as emergence with no second party. That is a resolved decision to name nobody, and it is recorded. A floating *it* is an unresolved decision to name somebody.

**And it does not license inserting a subject the Chinese excludes.** Where naming the referent would supply a person the line does not have, recast instead — the sentence can end without one.

---

## What it obliges

1. **Read every pronoun in a finished line and ask what it points at.** If there are two candidates, the English has chosen; decide deliberately or recast.
2. **No em-dashes in the verse.** Name the subject and end the sentence.
3. **When a referent is resolved, say in the note what the Chinese left open** — so the resolution is visible as ours rather than passing as the text's.
