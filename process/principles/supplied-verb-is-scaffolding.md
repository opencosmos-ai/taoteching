---
id: supplied-verb-is-scaffolding
title: "A supplied verb is scaffolding, not a character's English"
status: active
since: 2026-09-02
trigger: "the Chinese object is a position or a place and your English needs a verb the Chinese does not print"
applies: [drafting, glossary]
evidence: ["notes/translation.md#ch-8-善s-showcase-and-the-grammar-that-decides-it-2026-09-02", "notes/translation.md#ch-66-處前而民不害-the-people-are-not-hindered-and-the-reading-we-did-not-take", "notes/translation.md#ch-61"]
check: none
supersedes: []
---

# A supplied verb is scaffolding, not a character's English

**The rule.** Where the Chinese object is a **position** and English needs a verb to hold the slot, **supply a stance verb and name it as supplied.** It is scaffolding: it belongs to the English construction, not to the character. Because it belongs to no character, **the same stance verb may serve several** without either losing its own word — and because it is supplied, the note has to say so.

**When it fires.** When a construction works for most of a parallel series and collapses on one or two members, and the ones it collapses on are places.

---

## Why this holds

**English predicates want activities, and Chinese objects are often locations.** 善X (*shàn X*) is *masterful at X*, and that construction requires X to name something one **does**. It holds where the noun is a quality or a practice — 仁 (*rén* — humaneness), 信 (*xìn* — trust), 治 (*zhì* — governing), 能 (*néng* — what can be done), 時 (*shí* — timing) — and **collapses where the noun is a place**. *"Masterful at ground"* communicates nothing, and 淵 (*yuān* — a deep pool) is a place too.

**The alternative is worse than scaffolding.** Letting the bare noun stand and hoping produces a line that is technically complete and actually empty. The reader does not notice a gap; they notice that a line in a famous chapter says nothing, and conclude the text is vague.

**And naming it as scaffolding is what stops it becoming a lock.** If *staying* is treated as 下's English, then 下 is committed and the word is spent. If it is treated as a construction, **一 verb can serve 下 at ch 66, 下 again at ch 61, and 淵 at ch 8**, while each character keeps its own rendering — *below*, *low*, *deep*. This is the exemption that keeps [[already-spoken-for]] from firing on a word that renders nothing in particular.

**It is also the boundary of [[renders-no-character]].** A supplied verb *does* render no character, and it is nevertheless allowed — because English grammar requires it, and because the note declares it. Supplying is legitimate; **supplying silently is not**, and supplying a verb that smuggles a claim never is.

---

## Why this principle exists

**Ch 8** — seven 善X couplets, one shape. A stance verb is supplied at exactly two of them, where the object is a place: **choosing ground** (地) and **staying deep** (淵). The other five take the bare construction. → [ch 8](../../notes/translation.md#ch-8-善s-showcase-and-the-grammar-that-decides-it-2026-09-02)

**Ch 66 is the precedent, and it predates ch 8.** 善下之 already read *"masterful at **staying** below them"* — 下 (*xià* — below) is a position and the English supplied the verb, before anyone had stated the rule. → [ch 66](../../notes/translation.md#ch-66-處前而民不害-the-people-are-not-hindered-and-the-reading-we-did-not-take)

**Ch 61 does the same with *staying low***, which is what made the pattern visible as a pattern rather than a one-off. → [ch 61](../../notes/translation.md#ch-61)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *point every English word at a character* — a supplied verb is allowed, and must be named in the note |
| **`glossary-entry` §2** | a supplied verb never goes in `render:` |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Not enforced.** The line between scaffolding and a rendering is judgment.

---

## Where it does not fire

**It does not license a verb that carries a claim.** *Staying* is inert; *mastering*, *commanding* or *embracing* would each assert something. The scaffolding must be as close to grammatically empty as English allows.

**It does not apply where a verb exists in the Chinese.** If the line prints one, render it.

**And it is not a general licence to supply.** The trigger is narrow — a **position** in an object slot that English cannot leave bare. Outside that, [[renders-no-character]] governs.

---

## What it obliges

1. **Test the construction across the whole parallel series before adopting it.** The member it collapses on is the finding.
2. **Say in the note that the verb is supplied, and why** — which slot, and what made the bare noun fail.
3. **Do not enter a supplied verb in a glossary `render:`.** It belongs to the construction; putting it in the frontmatter commits a character to a word that was never its own.
4. **Reuse the same stance verb across chapters** rather than inventing a new one each time; consistency is what marks it as scaffolding rather than as a rendering.
