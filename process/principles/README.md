# Principles — the rules that outlive the decision that produced them

*One of this repository's authorities. `CLAUDE.md` says **what to do now**; `process/method.md` says **why**; `process/skills/` says **how, step by step**. This directory says **what we learned** — the transferable rules discovered while making particular decisions, which then govern every decision after.*

**Read this before adding an entry. `INDEX.md` and `principles.yaml` are generated — never hand-edit them.**

---

## The problem this exists to solve

A principle in this project is almost always born as a **by-product**. Someone settles one line in one chapter, and in settling it discovers a rule that applies to sixty other chapters nobody is looking at. That rule then gets written down where it was found — as the last paragraph of a chapter note, a thousand lines deep in `notes/translation.md` — and the next person to need it has no reason to be reading that chapter.

**This is documented, not theoretical.** `notes/translation.md` was built with a §1 *Standing principles* section for exactly this, and it holds six. At least eight more were born inside chapter notes and never migrated up — including one at line 2217 whose own heading reads *"and that is a standing principle."* The section existed; nothing carried anything into it.

So: **a principle gets its own file, addressable by name, loaded by the skills at the moment it applies.**

---

## What belongs here, and what does not

| | Goes where | Why |
|---|---|---|
| **A transferable rule** — *"where the Chinese repeats itself, repeat yourself"* | **here** | it governs work nobody has started yet |
| The case for one rendering in one chapter | `notes/translation.md`, under that chapter | someone working there will find it |
| Why a *term* renders as it does | `glossary/<term>.md` | that is what the entry is for |
| A textual fork between witnesses | `notes/manuscript.md` | |
| A rule Shalom has set aside | `process/shaloms-call.md` | a suspension, not a principle |
| What the manuscript still owes | `WORKLIST.md` | |
| A finding worth an essay | `DISCOVERIES.md` | |
| One of `CLAUDE.md`'s standing rules 0–6 | **stays in `CLAUDE.md`** | see below |

**Standing rules 0–6 are deliberately not kept here, and that is a decision rather than an oversight.** They are already indexed, already read at the start of every session, and several are enforced by `check_locks.py`. This directory exists for rules with **no** home; copying `CLAUDE.md` into it would rebuild precisely the failure that killed the hand-kept lock table — two copies, one of which goes stale. **Where a standing rule needs an argument rather than a statement, the argument goes in the layer that owns it** — `glossary/` for a term, `notes/translation.md` for a decision, a principle here only if it generalises past the rule.

**The test: does it tell you something about a chapter you have not read yet?** If it only explains one line, it is a chapter note.

---

## The two arguments, and why only one of them lives here

Every principle has a decision behind it, and the two must not be confused:

- **The chapter's argument** — *"ch 14 chose the explanations over the words, and here is the case for ch 14."* That stays in `notes/translation.md` under its chapter heading. **Do not copy it here.** A hand-kept second copy of a decision is how the lock table in `CLAUDE.md` went stale twice in one week.
- **The principle's own argument** — *"why does this hold beyond ch 14? When does it fire? Where does it not? What does it oblige you to do?"* **That belongs here, and it usually has to be written rather than moved** — a rule that has only ever been stated as a coda to the decision that produced it has never actually been argued as a principle.

An entry therefore carries the same weight as a glossary entry. `glossary/zhi-執.md` holds the full argument for 執 while chapters 14, 29, 35, 64, 69, 74 and 79 each hold their own note on how it lands on that page, and neither duplicates the other. Principles work the same way.

---

## Frontmatter — required, and it drives everything

```yaml
---
id: legibility-debt
title: "A rendering chosen for legibility owes its lost connection to the notes"
status: active
since: 2026-09-10
trigger: "you render a character by what it means here rather than by its word elsewhere in the book"
applies: [drafting, notes]
evidence: ["notes/translation.md#ch-14s-opening-triad--夷--希--微--the-names-and-why-the-verse-gives-their-meanings"]
check: none
supersedes: []
---
```

| Field | Meaning |
|---|---|
| `id` | kebab-case slug; the filename is `<id>.md`, and other entries link to it as `[[id]]` |
| `title` | the rule in one sentence, stated as a rule and not as a topic |
| `status` | `provisional` · `active` · `superseded` — see the threshold below |
| `since` | the date the rule was first stated |
| `trigger` | **the field that makes this actionable.** When does it fire? Written so a reader about to do the thing recognises themselves in it |
| `applies` | which work loads it: `drafting` · `glossary` · `notes` · `tooling` · `process`. **Must include at least one that something actually loads** — see *Where each kind of work loads its principles* below. The build checks |
| `evidence` | anchor links to the decisions that produced it — **verified by the build, so a rotted link is an error** |
| `check` | the tool that enforces it, or `none`. Most are `none`, and that is the point. **If it names a tool, *How it is implemented* must name it too** — the build checks |
| `supersedes` | ids this replaces |

**`trigger:` is the difference between this and an ADR.** An architecture decision record answers *"why is it built this way?"* and its `context` field is retrospective. A principle has to fire **prospectively**, in the middle of work, on someone who does not yet know they need it. If you cannot write the trigger, you do not yet have a principle — you have an observation.

**`check: none` is written, not omitted.** A principle no tool can enforce is the normal case here, and marking it makes the gap **visible** rather than assumed — the same honesty as the *"what no rule can enforce"* sections in the glossary entries. Where a tool does enforce it, name the tool, so the two kinds are never confused.

---

## The threshold: one case is an observation, two is a principle

**`status: provisional` until an entry has two or more independent cases in `evidence:`.** Then it may be promoted to `active`.

This is the forcing function, and it is deliberate. `process/shaloms-call.md` learned that `until:` must be a **required** field, because requiring it forces the choice between *for now* and *from now on*; without it, every override silently became permanent. A principles directory has the opposite failure mode — it becomes a place where nothing is ever deleted and every passing thought has the standing of a law. The evidence threshold is the counterweight.

The repository already teaches this twice over. `DISCOVERIES.md` §1's central claim was superseded, and carries a banner saying so. And `notes/translation.md` states the rule outright at ch 4: ***a distributional argument is a reason to look, not a reason to conclude.*** One chapter is a reason to look.

**Superseding, never deleting.** A principle that turns out to be wrong gets `status: superseded` and a closing section saying what replaced it and why. The reasoning that produced it was real even when the conclusion was not, and a reader who finds the rule quoted in an old chapter note needs to be able to follow it here and see that it fell.

---

## The shape of an entry

**A principle has two jobs: to be understood, and to run.** The first is argument; the second is wiring. An entry that argues well and is reached by nobody governs nothing — and when this standard was written, twenty-nine of thirty entries here said nothing about where they ran, and seven were loaded by no skill at all. So the shape below has a section for each job, and **the build refuses an entry that is missing either.**

```markdown
# <the rule, as a rule — the same sentence as title:>

**The rule.** One or two sentences, imperative, saying what to do.

**When it fires.** The moment, in the reader's own terms — same substance as `trigger:`.

## Why this holds
## Why this principle exists
## How it is implemented
## Where it does not fire
## What it obliges
```

**The five sections are required, in this order.** Other sections may sit between them where an entry needs one — `imported-register` has *The three tests* — but none of the five may be dropped or reordered. `build_principles.py --check` enforces this, along with the two opening paragraphs.

### Tell the story once

**A principle exists because something went wrong, and that story is told exactly once — in *Why this principle exists*.** Everywhere else, the entry says what the rule is and how it works, in the present tense.

| Section | Holds | Does not hold |
|---|---|---|
| **The rule** · **When it fires** | the instruction and its moment | the history |
| **Why this holds** | the general argument: why this is true of the book, the language, or English | *"ch 25 was drafted over…"* — that is the story |
| **Why this principle exists** | **the story, once**: what happened, in a short paragraph, with the cases linked | the full argument of each case — link to it, do not restate it |
| **How it is implemented** | where the rule runs | aspiration |
| **Where it does not fire** | the boundary | the story again |
| **What it obliges** | what someone now does | *"because last time…"* |

**Examples are not stories.** *"強 (qiáng — strong) is the disease at ch 76 and the cure at ch 52"* illustrates the rule and belongs in *Why this holds*. *"Ch 21 was drafted over a chronology the silks reverse, and nobody had looked"* is the failure that produced the rule, and belongs in *Why this principle exists*. The test: does the sentence say what **is** true, or what **happened**?

**Why once.** A story retold in every section turns guidance into a grievance, and it buries the instruction a reader came for. It also dates the entry: the next reader needs the rule, and needs the history only to trust it.

### How it is implemented — the section that makes a principle run

**This section names every place the rule is met or enforced.** A table, `| Where | What it does |`, with three kinds of row:

1. **Where it is applied** — the specific step of a skill, `process/method.md` or `CLAUDE.md` where someone doing the work meets it. Name the step, not the file: *`chapter-review` step 5, Before you offer a line*.
2. **What enforces it** — a `check_locks.py` rule, a CI step, a test, or a tool that makes it easy (`concordance.py --english`). Name the rule.
3. **Where it is loaded** — one row per `applies:` value, from the table below.

Then **one sentence on enforcement, honestly**: *enforced by X*, *partly enforced*, *not enforced, and cannot be — here is why*, or *deliberately not enforced* with the reason. **"Not enforced" is a legitimate answer; a missing answer is not.** Most principles here are judgment, and saying so makes the gap visible rather than assumed — the same honesty as `check: none` and the glossary's *What no rule can enforce*.

**If the rule has no step to be applied at, give it one before you ship it.** A principle whose only home is this directory is read after the mistake it exists to prevent. That usually means one line added to the skill step where the moment occurs — `search-the-record-first` became a command in `chapter-review` step 0; eight drafting rules became the six checks of *Before you offer a line* in step 5.

### Where each kind of work loads its principles

| `applies:` | Loaded by | When |
|---|---|---|
| `drafting` | `chapter-review` step 0 | before a chapter is drafted |
| `glossary` | `glossary-entry` §1 | before an entry is written |
| `notes` | `chapter-review` step 7 | at the logging step |
| `tooling` | `CLAUDE.md` → *The harness* | before anything in `tools/` or `data/` changes |
| `process` | `CLAUDE.md` → *Start here* | every session |

**The build refuses an entry none of whose `applies:` values is loaded anywhere.** It reads the loaders from the files themselves, so if a new kind of work is added, it must be given a loader before any principle can use it.

### And the writing itself

- **Gloss every Chinese character, every time** — 為 (*wéi* — "to do / to handle"), never bare 為.
- **Lowercase everything but the Tao**, and no em-dashes in quoted verse.
- **Argue generally.** A rule that has only ever been stated as a coda to one decision has not been argued as a principle; the general argument usually has to be written, not moved.
- **A rule with no boundary is a slogan.** If you cannot fill *Where it does not fire*, it is not yet a principle.

`process/skills/principle-entry` is the procedure that produces an entry of this shape — detection, deduplication, the trigger, the threshold, and the wiring.

---

## Finish — every time

```bash
python3 tools/build_principles.py
```

Regenerates `INDEX.md` and `principles.yaml`, **verifies every `evidence:` anchor resolves to a real heading in the file it names**, and **verifies the shape**: the opening paragraphs, the five sections in order, a *How it is implemented* that names its `check:` tool, and an `applies:` that something loads. Any failure writes nothing and exits non-zero, and CI runs it. A reworded heading becomes a build error instead of a dead link — which is why `notes/translation.md` requires that its headings carry only the stable claim, with dates and supersessions on the line beneath.
