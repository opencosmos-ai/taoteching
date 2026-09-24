---
name: principle-entry
description: Recognize, record, or revise a principle in process/principles/ — the transferable rules this project learns by making particular decisions. Use when a decision yields a rule that will govern chapters nobody has read yet, when the user says "that's a principle" or "worth keeping", when harvesting principles out of the notes, when auditing existing entries, or when an entry needs promoting, demoting or superseding. Enforces detection, deduplication, the trigger standard, the entry shape, the wiring that makes a principle run, and the evidence threshold.
---

# Recording a principle

A principle here is almost always a **by-product**. Someone settles one line in one chapter and, in settling it, discovers a rule that governs sixty chapters nobody is looking at. Left where it was found, it is invisible — which is why `process/principles/` exists and why this procedure does.

**Read [`process/principles/README.md`](../../principles/README.md) for the standard.** This skill is the part the README does not cover: how to **find** one, how to know it is one, how to write the field that makes it fire, and how to wire it so it runs.

**Gloss every Chinese character, every time** — 為 (*wéi* — "to do / to handle"), never bare 為. Shalom does not read Chinese.

---

## 0. First, is it already recorded?

```bash
python3 tools/build_principles.py --applies drafting     # or glossary, notes, tooling, process
grep -i "<a keyword from your rule>" process/principles.yaml
```

**Do this before writing anything.** The most likely failure of a principles directory is not an empty one — it is three entries saying the same thing in different words, which is worse than none because a reader cannot tell which governs. If you find a near-match, the right move is usually to **add your case to its `evidence:`** and sharpen its wording, not to open a new file. Adding a second case is also what promotes it from `provisional` to `active`, so a merge is often more valuable than a new entry.

---

## 1. Detection — three passes, decreasing precision

Use all three when harvesting. Use the third habitually, because it is the one that finds what nobody labelled.

**Pass 1 — self-declared.** The rule announces itself.

```bash
grep -rniE "standing principle|general rule|general finding|the finding that outlives|principle this yields|rules? (came out of it|worth keeping)" notes/ CLAUDE.md DISCOVERIES.md ARCHITECTURE.md PLAN.md WORKLIST.md glossary/
```

High precision, poor recall. It only finds principles someone already knew were principles.

**Pass 2 — principle-shaped.** A universal or imperative claim that names **no chapter and no character**.

```bash
grep -noE "^\*\*[A-Z][^*]{25,110}\.\*\*" ARCHITECTURE.md process/method.md DISCOVERIES.md PLAN.md
```

A bolded lead sentence stating a rule is a principle that got scoped to one document. *"A diff gate is only as good as the generator's determinism"* is a principle; it was living in `ARCHITECTURE.md` where no one drafting a chapter would meet it.

**Pass 3 — repeated reasons.** The same justification given many times, abstracted never. **This is the richest source and no keyword search finds it.** Look at *why* things were rejected, and cluster.

The method: take a rejection reason you have just written, and grep for how many times the repository has already given it.

```bash
grep -rocE "is [^ ]+( \([^)]*\))?'s (own )?(word|English)" glossary/ notes/ chapters/ | awk -F: '{s+=$2} END{print s}'
```

**Two of this project's load-bearing rules were found exactly this way** — *"X is Y's word"* (45 instances) and *"this English renders no character"* (78) — each stated over a hundred times across the corpus and indexed zero times.

**Also hiding:** rules that exist only as **behaviour** (a workflow step in a skill, an ordering in `CLAUDE.md`'s tie-breaking list) and rules implied by **Shalom's corrections** (`CLAUDE.md` → *How Shalom works*). Those last are `applies: process` — about the collaboration, not the text.

---

## 2. The test that decides: write the trigger

**If you cannot write `trigger:`, you do not have a principle.** You have an observation, or a chapter note.

Complete this sentence: ***"When you are about to ___, this fires."***

| | |
|---|---|
| **completes naturally, names no chapter** | a principle |
| **requires naming a chapter or character to make sense** | a chapter note — it belongs in `notes/translation.md` |
| **completes, but fires on everything** | a rejection, not a principle |

That last row is the one that kills a principles directory. *"When you are translating"* fires always and therefore never. A trigger has to describe a **recognisable moment**, narrow enough that someone not looking for it still recognises themselves in it.

### Worked triggers

| | |
|---|---|
| ✅ | *"you are about to render a character by what it means in this line rather than by the word it carries elsewhere in the book"* |
| ✅ | *"you are about to put an English word in the verse that renders no character in the Chinese"* |
| ✅ | *"a rendering you like is already doing duty for a different character somewhere in the book"* |
| ❌ | *"you are drafting a chapter"* — fires on everything |
| ❌ | *"when accuracy matters"* — names no moment at all |
| ❌ | *"when working on chapter 14"* — that is a chapter note |

**Write the trigger in second person, present tense, describing the act — not the virtue.** The reader is mid-decision and needs to recognise what they are doing, not be told what to value.

---

## 3. Write the entry

Follow [`process/principles/README.md`](../../principles/README.md) → *The shape of an entry*. **The build enforces that shape**, so an entry that skips it will not ship: the two opening paragraphs, then **Why this holds · Why this principle exists · How it is implemented · Where it does not fire · What it obliges**, in that order.

**Tell the story once.** The failure that produced the rule goes in *Why this principle exists* — a short paragraph with the cases linked — and nowhere else. Every other section says what the rule is and how it works, in the present tense. The test for a sentence: does it say what **is** true, or what **happened**? Only the second belongs in the story, and only there.

**Why this holds is the general argument** — why the rule is true of the book, the language or English, not why it held in the case that produced it. It usually has to be **written rather than moved**: a rule only ever stated as a coda to one decision has never been argued as a principle.

**Do not copy the chapter's argument.** Link to it. A hand-kept second copy of a decision is how the lock table in `CLAUDE.md` went stale twice in one week.

**Always include *Where it does not fire.*** If you cannot name a boundary, the rule is too broad to be useful.

---

## 4. Make it run — the wiring

**A principle that lives only in `process/principles/` is read after the mistake it exists to prevent.** Before shipping, answer three questions, and put the answers in *How it is implemented*:

1. **At what exact step does someone meet the moment in `trigger:`?** Find that step in a skill, in `process/method.md`, or in `CLAUDE.md`. If the step exists but says nothing, **add the line** — usually one row or one command. If no step exists, the trigger may be describing a moment nobody reaches; reconsider it.
2. **Can anything enforce it?** A `check_locks.py` rule, a CI step, a test, a tool. If yes, set `check:` and name it in the section. If no, **say so and say why** — *"not enforced, and cannot be: a collocation is innocent word by word"* is a complete answer.
3. **Is it loaded?** Pick `applies:` from the loader table in the README. The build refuses an entry whose `applies:` nothing loads.

```bash
grep -rn "<a phrase from your trigger>" process/skills/ process/method.md CLAUDE.md   # is the moment already a step?
python3 tools/build_principles.py --check                                             # shape, loaders, anchors
```

**If the wiring needs a tool that does not exist, that is a real finding** — `search-the-record-first` produced `concordance.py --record`. Build it or record the gap; do not ship a principle that claims wiring it lacks.

---

## 5. The evidence threshold, and how to earn the second case

**`provisional` until two independent cases; then `active`.** The build enforces it.

**Be honest about this rather than hunting for a second case to justify a rule you like.** One case is an observation — the repository has been burned by exactly that (`DISCOVERIES.md` §1's central claim was superseded), and `notes/translation.md` states the rule at ch 4: ***a distributional argument is a reason to look, not a reason to conclude.***

To look for a genuine second case:

```bash
python3 tools/concordance.py --english "<the rendering the rule is about>"
grep -rn "<the reason, in the words the notes would use>" notes/ glossary/ chapters/
```

A second case must be **independent** — a different chapter, a different term, arrived at separately. The same decision described twice is one case.

---

## 6. Anchors — the evidence links are checked

`evidence:` entries are `path/to/file.md#anchor`, and **the build verifies every one resolves to a real heading.** A principle whose link has rotted is worse than one with no link: it looks checked.

```bash
python3 -c "import sys; sys.path.insert(0,'tools'); from build_principles import slug; print(slug('''<paste the heading text, without the #s>'''))"
```

**If the target has no stable heading, add one** — do not link to a line number, ever. `notes/translation.md` requires that its headings carry only the stable claim, with dates and *(was: …)* on the line beneath, precisely so these links survive. Follow that rule when you add a heading there.

---

## 7. Revising: promote, demote, supersede

- **Promote** `provisional` → `active` when a genuine second case arrives. Add it to `evidence:` and say in the entry what the new case added.
- **Demote** `active` → `provisional` if a case turns out not to be independent. This is not an embarrassment; it is the threshold working.
- **Supersede** — set `status: superseded`, add `supersedes:` on the replacement, and close the old entry with a section saying what replaced it and why. **Never delete.** A reader who finds the old rule quoted in a chapter note needs to follow it here and see that it fell.

**When a harvested "principle" does not survive scrutiny, record it as `provisional` with its one case — do not quietly promote it, and do not drop it.** Dropping it means the next person rediscovers it and has no idea it was weighed.

---

## 8. When not to write one

- **It explains one line.** Chapter note.
- **It is about one term.** Glossary entry — that is what the entry's prose is for.
- **It is a rule Shalom has set aside.** `process/shaloms-call.md`.
- **It is a fact about the witnesses.** `notes/manuscript.md` and `sources/variants.yaml`.
- **It restates something already written.** Merge into that entry instead.
- **You cannot name where it does not fire.** Not yet a principle.

---

## 9. Finish — every time, no exceptions

```bash
python3 tools/build_principles.py
```

Regenerates `process/principles/INDEX.md` and `process/principles.yaml`, validates the frontmatter, enforces the threshold, and verifies every anchor. **Never edit the generated files by hand.**

Then:

1. **Add the `evidence:` anchor's own note a pointer back**, if the decision that produced the rule does not already name it.
2. **If the principle contradicts something already written elsewhere in the repo, that is a finding** — `CLAUDE.md` → *"if you find them disagreeing, that is a finding: fix both and say which was wrong."* Do not silently pick a side.
3. **Report**: the rule, the trigger, the cases, **where it is implemented**, and whether it shipped `provisional` or `active`.
