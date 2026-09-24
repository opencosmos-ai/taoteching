---
id: record-the-fact
title: "For the excavated witnesses, record the fact — never the text"
status: active
since: 2026-08-11
trigger: "you are about to add an excavated reading whose only available transcription is a modern reconstruction"
applies: [notes, tooling]
evidence: ["sources/PROVENANCE.md#the-admission-rules", "sources/PROVENANCE.md#the-guodian-question-asked-properly-and-answered-no-2026-08-17"]
check: none
supersedes: []
---

# For the excavated witnesses, record the fact — never the text

**The rule.** Do not bring the Mawangdui or Guodian manuscripts into this repository **as text**. Record the *fact* of a variant instead — that this chapter reads X where our base reads Y — in `sources/variants.yaml`, and cite where the reading comes from.

**The rule is conditional, and the condition is the whole of it.** The manuscripts themselves are free; what is encumbered is the modern **釋文** (*shìwén* — the reading of damaged graphs into modern characters), which is reconstruction rather than transcription. **If an unencumbered transcription existed, this rule would not apply to it.** None does, today.

**When it fires.** Every time an excavated witness has something to say — which is often — and its only available reading is a reconstruction.

---

## Why this holds

**The manuscripts are not the problem. The reconstructions are.** The silks are second-century BCE and the slips ~300 BCE; no copyright subsists in either, and **a faithful transcription of a public-domain text creates no new copyright** — the position `sources/PROVENANCE.md` takes, citing *Feist* (1991) against "sweat of the brow" and *Bridgeman* (1999) for faithful reproductions. **So the exclusion cannot rest on the age of the object, and does not.**

**It rests on what a 釋文 of damaged bamboo actually is.** Reading lacunose silk and broken slips into modern characters — the brackets, the □ marks, the conjectural readings — **is not faithful transcription of anything legible.** It is original editorial work by living scholars, and reproducing it reproduces the scholarship. A Song woodblock of 王弼 (*Wáng Bì*) can be transcribed faithfully because there is something legible to be faithful to.

**And as things stand there is no unencumbered transcription of the Guodian slips.** The question was asked properly and answered no, in writing, with the reasoning kept. **Note the tense**: the standard 釋文 was published in 1998 and is squarely in copyright — *yet*, not *never*. The rule tracks what is available, and what is available will change.

**A `shaloms-call` cannot fix this one**, and that is worth stating: the override mechanism can set aside this repository's own rules, and it has no authority over somebody else's copyright. Every other rule here is ours to suspend. This one is not.

**The fact is not encumbered, and it is what the work actually needs.** *"Both Mawangdui silks reverse this chronology"* is a statement about the world. It supports every argument a transcription would, and the apparatus is more useful than a text would be — because what a chapter review needs is **where the witnesses disagree**, not another edition to read.

**This is why `guodian-inventory.yaml` exists**: an inventory of what the oldest witness contains, chapter by chapter — never a text.

---

## Why this principle exists

Two pressures produced this rule. The excavated witnesses exist only as modern transcriptions, which are living scholarship and somebody else's copyright — so this CC0 repository cannot hold them. And a popular online *"帛書版"* (*bó shū bǎn* — "silk-manuscript edition") had been silently emended; it was taken for the silks, and it cost `DISCOVERIES.md` §1 its central claim. Recording facts with their edition named, rather than text, answers both.

**The admission rules** — four conditions, all of which must hold, plus one category excluded outright on grounds unrelated to licence text. → [PROVENANCE](../../sources/PROVENANCE.md#the-admission-rules)

**The Guodian question**, asked properly and answered no, with the reasoning preserved rather than the conclusion alone. → [PROVENANCE](../../sources/PROVENANCE.md#the-guodian-question-asked-properly-and-answered-no-2026-08-17)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`sources/PROVENANCE.md`** | the rights reasoning for everything in `sources/`, and why the excavated witnesses are never transcribed |
| **`sources/variants.yaml`** | the apparatus schema records a witness and a reading, never a witness's text |
| **`concordance.py --witnesses N`** | reads the apparatus; `chapter-review` step 0 |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |

**Not enforced by a tool**, and it is the one rule no `shaloms-call` can set aside: it is somebody else's copyright.

---

## Where it does not fire

**Transmitted commentaries are different and are vendored in full.** 王弼, 河上公 and 韓非 are public domain by age, from nameable editions, with per-file provenance. Nothing was reconstructed from damage.

**A commentator's lemma is a witness and may be quoted.** When 河上公 prints 知者 where our base prints 智者, that is a transmitted reading, not an excavated one.

**And no modern translations, of anything, for any reason** — a separate rule with a separate basis. The pre-1931 limit governs *translations*, and none are in this repository.

### The condition, stated as a test

**This rule lapses for any excavated transcription that clears the four admission rules on its own merits.** That would require all of:

- **a transcription that is faithful rather than reconstructive** — legible graphs read as they stand, with no conjectural filling — or a reconstruction whose copyright has expired, or one its rights-holder has dedicated CC0;
- **a nameable edition**, cited exactly in the frontmatter. *"Found on the open web is not provenance"* is this file's own sentence;
- **any modern editorial layer absent, excluded, or marked** — punctuation especially;
- **a licence compatible with CC0 and with a companion volume intended to be sold.** This is what defeated the Chinese Wikisource 郭店楚墓竹簡 page independently of everything else: **CC BY-SA is copyleft**, and this repository is CC0 with no exceptions.

**Until one clears all four, record the fact.** And note that this repository is deliberately **stricter than the law requires** — so *"probably fine"* is not the test; the four rules are.

---

## What it obliges

1. **Read `sources/PROVENANCE.md` before adding anything to `sources/`.**
2. **Record variants as facts in `sources/variants.yaml`**, with the witness named and the difference stated — not the witness's text reproduced.
3. **Cite rather than copy**, and say which edition the claim rests on.
4. **Do not trust a manuscript claim that is not in `sources/variants.yaml`.** A transcription found elsewhere is somebody's edition, and it may have been emended.
