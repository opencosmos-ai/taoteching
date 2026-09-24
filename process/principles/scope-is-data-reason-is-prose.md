---
id: scope-is-data-reason-is-prose
title: "When a rule has an exception, the scope goes in a field and the reason goes in prose"
status: active
since: 2026-09-20
trigger: "you are about to write a condition — where, until, when — inside a sentence that a tool will later need to know"
applies: [glossary, tooling, process]
evidence: ["ARCHITECTURE.md#how-a-decision-becomes-an-enforced-rule", "process/shaloms-call.md#how-a-call-works", "notes/manuscript.md#using-this-file"]
check: none
supersedes: []
---

# The scope goes in a field; the reason goes in prose

**The rule.** Every exception in this repository has two halves: **where it applies** and **why**. The *where* is a fact a tool must be able to read — a chapter number, a date, a boolean. The *why* is an argument only a person can weigh. Put them in one sentence and you get a string no tool can parse and no reader trusts. **Split them: the scope into a named field, the reason into prose beside it.**

**When it fires.** You are writing *"— and X where Y"*, *"except at chapter N"*, *"until the corpus is complete"*, or any other condition, inside a value a program will later have to act on.

---

## Why this holds

**A condition written in prose is invisible to everything that needs it.** The tool cannot branch on it, so it either ignores the exception (and reports a licensed variant as a breach) or matches the whole sentence (and reports nothing). Both failures are silent, and both look like the tool working.

**And the reason cannot be a field.** It is the part that survives the next person asking *"why is this here?"* — the thing an entry exists to carry. Compressed into an enum or a flag it stops being an argument and becomes a label, which is the failure [[perform-dont-label]] names in the verse and which applies just as well to a schema.

**So the split is not tidiness. It is the only arrangement in which both halves work.** Each field then earns a check the other could never carry: a scope can be verified to point at something real, while a reason can only be read.

**The forcing function is that a required field makes you choose.** `process/shaloms-call.md` learned this first: `until:` is **required**, because requiring it forces the author to decide between *for now* and *from now on*. Without the field, every override silently became permanent — not because anyone decided that, but because a sentence has no slot that insists.

---

## Why this principle exists

**Flexions in a glossary lock.** `render:` carried its exceptions as prose — *"keep safe — and bare keep where the object is not cherished (ch 9 alone)"*. No tool read it, so `concordance.py --english` could not tell a licensed flexion from a breach, and the character atlas printed `NOT FOUND` on **36 lines a flexion existed to license**. Now `flexions: [{ english, chapters, why }]`: the chapters are checked by a rule, the `why` is a sentence. → [ARCHITECTURE](../../ARCHITECTURE.md#how-a-decision-becomes-an-enforced-rule)

**`until:` in a `shaloms-call`.** The scope of a suspension is a date; the reason it was granted is a paragraph. The date is enforced — an expired call is a build error — and the paragraph is what a reader needs in order to renew or retire it deliberately. → [shaloms-call](../shaloms-call.md#how-a-call-works)

**`meaning_bearing:` in the variant apparatus.** `sources/variants.yaml` splits the same way: typed fields for chapter, line, witness and our call, a boolean saying whether the fork changes the meaning, and a free `note:` for the argument. The boolean drives `unlogged-variant`; the note is what makes the entry worth having. → [manuscript notes](../../notes/manuscript.md#using-this-file)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`flexions:`** in glossary frontmatter | a secondary English's scope as a chapter list; `check_locks.py` `flexion-chapter` verifies each chapter is real |
| **`until:`** in `process/shaloms-call.md` | a suspension's scope as a date; `stale-shaloms-call` fails it when it lapses |
| **`meaning_bearing:`** in `sources/variants.yaml` | a boolean `unlogged-variant` acts on, beside a free `note:` |
| **`CLAUDE.md`** → the frontmatter contract | says which conditions belong in a field and which stay prose |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |
| **`CLAUDE.md` → *Start here*** | `--applies process` lists it at the start of every session |

**Enforced wherever a field exists**, by the rule attached to it. Deciding to create the field is judgment.

---

## Where it does not fire

**Not on a condition no tool will ever need.** A sense that varies by grammar rather than by place — 明 (*míng*) takes the predicate form wherever it predicates, 虛 (*xū*) is adjective and verb — has no scope to record. Inventing a chapter list for it would assert a condition the language does not have, which is worse than prose. The test is whether the *where* is a thing in the world or a thing about the sentence.

**Not on everything an entry says.** Most of a glossary entry is argument, and should be. This fires only where an exception's applicability is being stated.

**Not as licence to add fields.** Each one needs a consumer. A field nothing reads is prose with extra punctuation, and it rots faster, because nothing fails when it goes stale.

---

## What it obliges

1. **Name the scope in a field a tool reads** — chapter, date, flag.
2. **Give that field a check**, even a trivial one. A scope nothing verifies is the prose problem again with a colon in it: `flexion-chapter` only asks whether the chapters are real, and that was enough to be worth adding.
3. **Keep the reason in prose**, in the layer that owns the argument, and do not try to encode it.
4. **Say in the contract where the boundary is**, so the next author knows which conditions belong in a field and which do not.

---

*Kin to [[edited-or-generated]], which is the same instinct one level up — a fact belongs in exactly one place, in the form its readers need. And to [[ruling-and-enforcement-are-two-facts]]: that rule says to disclose which claims the build holds; this one says how to write a claim so that it can.*
