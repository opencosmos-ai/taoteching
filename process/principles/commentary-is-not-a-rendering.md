---
id: commentary-is-not-a-rendering
title: "A commentator's gloss is an argument for a rendering, never a rendering"
status: active
since: 2026-08-30
trigger: "a word you are about to put in the verse came from a commentary rather than from the line"
applies: [drafting, glossary]
evidence: ["notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english", "notes/translation.md#ch-23-同-is-the-same-not-a-merging-2026-09-03", "notes/translation.md#ch-38-the-道-德-仁-義-禮-descent-rebuilt-and-the-rank-word-seam-named"]
check: none
supersedes: []
---

# A commentator's gloss is an argument for a rendering, never a rendering

**The rule.** We consult 王弼 (*Wáng Bì*), 河上公 (*Héshàng Gōng*) and 韓非 (*Hán Fēi*) on every chapter, and they settle referents, reopen decisions and supply readings nothing else can. **A gloss is evidence for what a line means. It is never a word for the line.** Quote it, gloss it, cite it — then render the Chinese.

**When it fires.** When you can name which commentator a word came from. If the honest provenance of an English word is a Han or Wei commentary rather than the eighty-one chapters, the word is out.

---

## Why this holds

**The failure is quiet, because the imported word is always *true*.** It is a real reading by a real authority, and it always reads well — because a gloss is **by construction more explicit than the text it glosses.** That is the tell: the gloss explains, and **the line stops pointing.**

**A commentary is a different genre doing a different job.** Its purpose is to remove ambiguity; the verse's purpose, frequently, is to hold it. Importing a gloss does not clarify the line — it replaces a poem with an explanation of a poem, in the poem's own clothes.

**And it silently picks a side.** A gloss is one commentator's. The moment it enters the verse, a choice between commentators has been made without being argued, and usually without being noticed — which is the failure [[divergence-stays-open]] exists to prevent, arriving by a different road.

**Shalom catches this reliably, which is itself the evidence that it is a distinct fault.** 王弼 explaining 贅 (*zhuì* — superfluous) as 肬贅 (*yóu zhuì* — a wart) does not make *wart* a candidate rendering. The commentary is the case for *superfluous*; it is not a synonym list.

**A related trap sits one step further out:** a gloss can also be evidence for what stood in **that commentator's own text**, which is a claim about the manuscript, not about the meaning. Those belong in `notes/manuscript.md`.

---

## Why this principle exists

**以此 at ch 21, 54 and 57.** *"By this, here, now"* was 河上公's 此，今也 (*"'this' means now"*) wearing the verse's clothes. The Chinese is two characters — 以 (*yǐ* — by means of) and 此 (*cǐ* — this) — and says only that. The import also **picked 河上公 over 王弼**, whose 此上之所云也 (*"'this' is what was said above"*) reads the pointer as anaphoric. → [以此](../../notes/translation.md#ch-21-54-57-以此-by-this-one-formula-one-english)

**Ch 23's *intensity*.** The word rendered no character at all: it was 王弼's gloss 暴疾 (*bào jí* — violent and rapid) lifted out of the commentary. **Two faults at once** — an import, and an addition ([[renders-no-character]]). → [ch 23](../../notes/translation.md#ch-23-同-is-the-same-not-a-merging-2026-09-03)

**Ch 38's *clutches at*.** The word renders 執 (*zhí* — to grasp), which **appears zero times in the chapter**. It came from 王弼's gloss 無執無用 on the line above, describing what 上德 (*shàng dé* — the highest integrity) lacks — and it displaced 失 (*shī* — to lose), the chapter's actual spine. → [ch 38](../../notes/translation.md#ch-38-the-道-德-仁-義-禮-descent-rebuilt-and-the-rank-word-seam-named)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py --commentary N`** | prints 王弼 and 河上公 on the chapter, so the gloss is read as evidence rather than remembered as wording. `chapter-review` step 0 |
| **`sources/commentaries/`** | the commentaries are vendored with no English, so every rendering of them in this repository is visibly ours |
| **`chapter-review` step 5**, *Before you offer a line* | *point every English word at a character* — a word that came from a gloss has none |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Not enforced.** Whether a word came from a commentary is a question about its origin, which no tool can see.

---

## Where it does not fire

**Convergence is strong evidence and should be used as such.** Where all three commentators land on the same reading, say so and let it settle the argument — the reading still has to be defensible from the characters.

**A commentator may supply a fact the verse assumes.** That a 芻狗 (*chú gǒu*) is a straw dog made for a sacrifice and thrown away after is a fact about the world, not a gloss to import — it belongs in the reader-facing note, not in the line.

**And a commentator's own text is a witness.** When 河上公 prints 知者 where 王弼 prints 智者, that is a manuscript fork and goes in `sources/variants.yaml`. **Using a gloss as evidence about a text is the legitimate use; using it as a word is not.**

---

## What it obliges

1. **Run `concordance.py --commentary N` before drafting and before changing a settled line** — the tool exists so the commentary is read, not remembered.
2. **Quote the Chinese with an English rendering, and cite it.** The commentaries in `sources/` carry no English; every rendering of them here is ours, and the pre-1931 rule governs *translations*, of which none are in this repository.
3. **Ask of any word you like: which chapter is this in?** If the answer is a commentary, take it out and keep the argument.
4. **Where the gloss is evidence about a text rather than a meaning, log it in `notes/manuscript.md`** and, if it is a textual fork, in `sources/variants.yaml`.
