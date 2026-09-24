---
id: divergence-stays-open
title: "Where the commentators diverge, the English must not settle it"
status: active
since: 2026-09-10
trigger: "the commentators disagree about a line and you are choosing an English that picks one of them"
applies: [drafting, notes]
evidence: ["notes/translation.md#ch-4-56-挫其銳解其紛和其光同其塵-the-nouns-unified-the-subject-deferred", "notes/translation.md#ch-3-the-closing-movement-restored-and-a-sinister-register-that-was-ours", "notes/translation.md#信不足焉有不信焉-where-trust-runs-short-there-is-no-trust-ch-17-and-ch-23-alike"]
check: none
supersedes: []
---

# Where the commentators diverge, the English must not settle it

**The rule.** When the classical commentaries read a line two ways, **the divergence is the finding.** Do not average them into a consensus and do not quietly adopt the more convenient one. Look for an English that holds both; where none exists, take a side **on stated grounds**, and record what the other side would have said.

**When it fires.** The moment `concordance.py --commentary N` returns two glosses that do not agree — which is more often than it looks, because a commentator who agrees about the *sense* may disagree about the *subject*, the *referent*, or *who is doing the thing*, and those decide the English.

---

## Why this holds

**Convergence and divergence are different kinds of evidence and must not be flattened into one.** Where 王弼 (*Wáng Bì*), 河上公 (*Héshàng Gōng*) and 韓非 (*Hán Fēi*) agree, that is strong evidence for a reading, and the reading still has to survive the character. Where they disagree, **the disagreement is data about the text** — usually that the Chinese genuinely underdetermines something English is forced to specify.

**English forces specification that classical Chinese does not.** Subject, number, tense, definiteness: the Chinese can leave all of them open, and the commentators' split is frequently a record of exactly that openness. An English that picks one is not resolving an ambiguity in the commentary. **It is inventing a determinacy the source does not have**, and doing it invisibly, because a determinate English reads as more confident, not less faithful.

**Averaging is worse than choosing.** A consensus reading belongs to neither commentator, has no witness behind it, and cannot be traced. At least a stated choice is auditable.

**And this is the honesty-over-false-closure rule applied to evidence.** The edition's standing commitment is that where the text is genuinely double, it says so. The commentaries are one of the two places that doubleness is discoverable; the witnesses are the other.

---

## Why this principle exists

**Ch 4 and ch 56 share four lines, and the subject is left split — deliberately.** 王弼 reads ch 4's 挫其銳 with **the Tao** as subject (銳挫而無損…同塵而不渝其真) and ch 56's as **a person's practice** (含守質也). 河上公 reads both as instruction to a person. **The contexts back 王弼**, so the nouns were unified across both chapters and the verb forms were not. → [ch 4, 56](../../notes/translation.md#ch-4-56-挫其銳解其紛和其光同其塵-the-nouns-unified-the-subject-deferred)

**Ch 3's 智者 — any English specific enough to settle it picks a side.** 王弼 prints 智者 and glosses 智者謂知為也 (*"those who know how to handle"*); 河上公 prints 知者 with the phonetic note 知音智 and glosses 思慮深不輕言 — near-identical to what he says of the *approving* 知者 at ch 56. **The neutral *the knowers* was chosen because it declines**, and the fork is logged in `sources/variants.yaml`. → [ch 3](../../notes/translation.md#ch-3-the-closing-movement-restored-and-a-sinister-register-that-was-ours)

**信不足焉 — the commentators cross in *both* directions, and the English had been split on context.** 王弼 reads the line at ch 17 as impersonal natural law (此自然之道也); 河上公 supplies a ruler at ch 23 (君信不足於下). The old Englishes each asserted **reciprocity**, which is only 河上公's reading — 王弼's is **emergence**, with no second party. The line is now **agent-free and holds both**. → [信不足焉](../../notes/translation.md#信不足焉有不信焉-where-trust-runs-short-there-is-no-trust-ch-17-and-ch-23-alike)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`concordance.py --commentary N`** | puts both commentators on the screen before drafting. `chapter-review` step 0 |
| **`check_locks.py`** · `unlogged-variant` | holds the textual half: a meaning-bearing fork in `sources/variants.yaml` must have a logged decision |
| **`chapter-review` step 5**, *Before you offer a line* | *where the commentators split, has the English chosen?* |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`chapter-review` step 7** | `--applies notes` lists it at the logging step, before a note is written |

**Partly enforced.** Textual forks are gated; interpretive divergence between commentators is held only by the read-back.

---

## Where it does not fire

**A commentator's gloss is not a candidate rendering.** When 王弼 explains 贅 (*zhuì* — superfluous) as 肬贅 (*yóu zhuì* — a wart), that does not make *wart* an option. Divergence about glosses that were never candidates is not a fork worth preserving.

**The character can still overrule both.** The tie-breaking order puts graphs and radicals above commentary. 專 (*zhuān*) is a spindle whorl in 說文解字 and 河上公 agrees; **王弼 says the opposite** (專，任也). The character decided, and the divergence was logged rather than held open in the English.

**A split about *volume* versus *quantity* may resolve by chapter.** 希 (*xī*) at ch 23 follows 河上公's quantity reading because the chapter's weather images argue for it, while 王弼's audibility reading survives elsewhere in the book at ch 14 and 41. **Holding both was unnecessary because the book holds both, in different places.**

**And where only one commentary covers the chapter, there is no divergence** — only a single witness, which is weaker evidence than two agreeing and should be said to be.

---

## What it obliges

1. **Run `concordance.py --commentary N` before drafting and before changing a settled line.** A divergence nobody looked for is not an absence of divergence.
2. **Log the fork in `notes/manuscript.md`**, and in `sources/variants.yaml` if it is textual rather than interpretive.
3. **Try for an English that holds both before taking a side.** *Agent-free* and *neutral noun* are the two moves that most often work.
4. **When you must choose, say in the note what the other reading was and what choosing cost.** A future reader with new evidence needs to find the door you closed.
