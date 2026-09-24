# Changelog — the Tao Te Ching translation

The dated spine of the work: **what landed, and when.** Newest first.

**Last updated:** 2026-09-23

> **This file exists because the dates were scattered and nothing held them.** *"The first draft is complete since 2026-08-26"* is in `WORKLIST.md`; *"built 2026-08-11"* is in `PLAN.md`; *"found at Chapter 11, 2026-09-05"* is in `DISCOVERIES.md`; the suspensions are dated in `process/shaloms-call.md` and the rules in `process/principles/`. Every one of those dates is authoritative where it sits. None of them is anywhere you can read the project's shape from.
>
> **`WORKLIST.md` is the single forward-looking file and this is the single backward-looking one.** Between them the repository's doctrine is unchanged: *nothing belongs in two of those.*

## What goes here, and what does not

This is a **spine that points into the other layers**, never a second copy of them.

| | Lives in | Not here because |
|---|---|---|
| What the manuscript still owes | [`WORKLIST.md`](WORKLIST.md) | that file is the forward-looking one, and it has its own closing ledger |
| A term's ruling and its full argument | [`glossary/`](glossary/INDEX.md) | the entry *is* the argument |
| A rendering call, thin | [`notes/translation.md`](notes/translation.md) | |
| A manuscript fork between witnesses | [`notes/manuscript.md`](notes/manuscript.md) | |
| A reader-facing thread | [`notes/reading.md`](notes/reading.md) | |
| A finding worth an essay | [`DISCOVERIES.md`](DISCOVERIES.md) | |
| A transferable rule | [`process/principles/`](process/principles/INDEX.md) | each entry carries its own `since:` |
| A rule Shalom has set aside | [`process/shaloms-call.md`](process/shaloms-call.md) | a suspension is dated where it is logged |
| What is generated from what | [`ARCHITECTURE.md`](ARCHITECTURE.md) | |
| What to do now | [`CLAUDE.md`](CLAUDE.md) | |

**Entries are milestones, not commits.** `git log` holds every change; this holds the ones that changed the shape of the work. One heading per date that mattered, a sentence of context, then bullets that link out.

**Counts are a snapshot on the entry's date, not a table anyone maintains.** `chapter-tally` and the generated indexes hold the live numbers — a hand-kept copy of a derivable list is what `edited-or-generated` forbids, and what the old locks table did before it was deleted.

**On the other changelogs.** This repository is one of four with a work history, and the rule across all of them is **one change, one changelog — the one that owns the decision.** The system is written down once, in the [opencosmos root `CHANGELOG.md`](https://github.com/shalomormsby/opencosmos/blob/main/CHANGELOG.md). What touches this project from outside: `glossary/terms.yaml` is **vendored into** the opencosmos I Ching substrate as its lock table, and this repository's `process/principles/` is **inherited wholesale** by that project. Both are logged there as consumption, and here only when the thing consumed actually changed.

---

## 2026-09-23 — Three characters were wearing 玄's word, and the governance pair gets settled

The 身 sweep left a loose thread nobody had pulled: **玄 (*xuán* — dark or profound) is one of the book's biggest words, and three other characters were wearing its English.** Pulling it ran through four locks and ended at the pair the book uses for governing and its failure.

- **昧 (*mèi*) → *murky*** (14, 41) and **昏 (*hūn*) → *clouded*** (18, 20, 57). Both were defensible about their own character — 說文 gives 昧 一曰闇也 and 昏 日冥也, *the sun below the line* — and neither was **available**: *dark* is 玄's across six lines, among them ch 1's 玄之又玄, *"dark, and dark again."* An English chiming where the Chinese does not asserts a thread the author never wrote. **`--english "dark"` went from ten lines with four unbacked to six and six.** At ch 18, 昏 had not been rendered at all, folded into 亂.
- **亂 (*luàn*) → *disorder*, locked** — [`glossary/luan-亂.md`](glossary/luan-亂.md). **說文 defines it as its own opposite, twice**: 亂，治也, and — under 辭, which stands at ch 34 — 𤔔，理也. So the two hands in the graph are **untangling**, and 亂 names a tangle somebody has their hands in. That is why *chaos* is the wrong shape: it is a condition with nobody in it, and you cannot catch it early. *Unravelled* and *untangled* are both recorded as declined, for opposite reasons.
- **治 (*zhì*) → *govern*, locked** — [`glossary/zhi-治.md`](glossary/zhi-治.md), with a declared flexion to *order* at ch 8 and 64. **說文 files it as a river**, 治，水。出東萊曲城陽丘山，南入海 — the governing sense is the extension, and the metaphor is 大禹治水, channelling rather than damming. 王弼 supplies the content at ch 60: 不擾也, *"it is not to disturb."*
- **政 (*zhèng*) → *government***, so ch 8 reads *"In government, masterful at order."* **The decision turned on part of speech, not consistency** — 其政 at ch 58 can only be nominal, and ch 8's other six slots are each rendered by their own part of speech, three verbs and three nouns.
- **50 glossary entries**, and the chapter count for the branch: seventeen.

**And two pieces of method, both about a change being believed on trust rather than checked.**

- **The grep the glossary-entry skill now requires was run, and found five stale places** — including `luan-亂.md`'s own *Left open* saying 治 had no entry two commits after 治 was locked. The one that mattered: `notes/translation.md`'s ch 3 note **already contained** 說文's 亂，治也 and the tangled-silk graph, written 2026-08-31, and the September entry rediscovered it from the dictionary instead. That became a principle.
- **A third principle: [*the repository's own record is a source, and it is the one nobody checks*](process/principles/search-the-record-first.md).** `process/method.md` §3 names the graph, the witnesses, the commentaries and the locks — every source **outside** the repo, and none inside it. Three cases in one week. 30 principles.
- **A baseline bump now costs a sentence.** `BASELINE` in `tools/build_db.py` is `(count, note)` with the note required, and the failure message names what the number counts and what to do. Three counts moved in a week, and a reviewer had only a code comment to tell a real corpus change from a test bent to pass. Recorded in [`ARCHITECTURE.md`](ARCHITECTURE.md) as a fourth escape hatch, beside `lock-ok` and `shaloms-call`.

## 2026-09-20 — 身 is locked, and two early chapters give up what they were hiding

Pass E's second term family. 身 (*shēn* — body) stood twenty times across nine chapters and read **six** ways, and at chapter 9 it was not rendered at all. Settling it opened the two chapters that had been carrying the fault, and both turned out to owe more than the one character.

- **身 → *body*, locked** — [`glossary/shen-身.md`](glossary/shen-身.md), the 48th entry. *Self* was refused because it belongs to 我/吾 and, at chapter 7, to 私 (*sī* — private interest), where 王弼 makes their difference the argument. One declared flexion: 終身 and 没身 mark the span of a life.
- **Chapters 9 and 26 rebuilt.** Ch 9's spine is three characters for keeping — 持, 保, 守 — and the English had rendered one. Ch 26 turns on heavy against light, and 輕 had three Englishes while 天下 had been deleted from the chapter's central line.
- **保 gains a declared flexion**, bare *keep* at chapter 9 — and the lock turned out never to have been tested there, because that verse rendered 保 nowhere and the ruling had been argued from the chapter's gloss table.
- **A new principle: [*say which rulings the build can hold*](process/principles/ruling-and-enforcement-are-two-facts.md).** Four glossary entries carried a ruling no check can enforce; two stated it as though it were enforced and two omitted it entirely. Shalom found the first kind by reading. 28 principles now.
- **T2-53 opened** — the calamity family, where *disaster* is currently worn by both 禍 and 凶.

**And the flexions became data**, which the 保 decision exposed as a gap. A lock's secondary Englishes had been prose inside `render:` — *"keep safe — and bare keep where the object is not cherished (ch 9 alone)"* — a sentence in a YAML string that **no tool could read.**

- **`flexions: [{ english, chapters, why }]`** — the *where* is a chapter a tool checks, the *why* stays a sentence for the reader. Seven locks converted: 保 · 執 · 守 · 身 · 一 · 王 · 極. Only where the condition is a **chapter**; a sense varying by grammar stays prose, because there is nothing to check. The contract is in [`CLAUDE.md`](CLAUDE.md) and the [glossary-entry skill](process/skills/glossary-entry/SKILL.md), the schema in [`ARCHITECTURE.md`](ARCHITECTURE.md).
- **What it was costing.** `concordance.py --english` could not tell a licensed flexion from a breach, and `data/locked-renderings.csv` printed `NOT FOUND` on **36 lines a flexion existed to license** — including both flexed characters in the chapter rebuilt the same day.
- **A thirteenth rule, `flexion-chapter`**, and a **refusal with its own test**: nothing checks whether a flexion's English appears *outside* its chapters, because inflection and insertion make that the thin-translation trap declined as T5-1. 144 tests.
- **A second principle: [*the scope goes in a field, the reason goes in prose*](process/principles/scope-is-data-reason-is-prose.md).** The repository had been doing this twice already without saying so — `until:` in a `shaloms-call`, `meaning_bearing:` in the variant apparatus — and the flexions were the third case, written the wrong way. 29 principles.
- **T2-46 closed, and it drew the boundary from the other side.** 明's four grammatical forms were unlicensed by its frontmatter while its own *working register* had listed them for months — but they stayed **prose**, because 明 predicates wherever it predicates. The entry also rendered 道 as *path* in three places, locked untranslated: **the file defining one lock was breaching another.**

## 2026-09-10 — The principles become a layer, and the oldest commentator is harvested

Rules had been getting written down where they were discovered — as the last paragraph of a chapter note, a thousand lines into `notes/translation.md` — and the next person to need one had no reason to be reading that chapter. One of them carried a heading that read *"and that is a standing principle"* and had still never moved anywhere.

- **[`process/principles/`](process/principles/INDEX.md) founded, and harvested to 27 entries** — 25 active, 2 provisional. Each carries a `trigger:` written so that someone about to do the thing recognises themselves in it, which is the field that separates a principle from an architecture decision record: an ADR explains why something is built as it is; a principle has to fire **prospectively**, on someone who does not yet know they need it.
- **The evidence threshold is the counterweight to a directory where nothing is ever deleted.** `status: provisional` until an entry has two independent cases. One case is an observation — the rule the project already states at ch 4, *a distributional argument is a reason to look, not a reason to conclude*, turned on itself.
- **`tools/build_principles.py` generates `INDEX.md` and `principles.yaml`** and **verifies every `evidence:` anchor resolves to a real heading**, so a reworded heading is a build error rather than a dead link.
- **The 韓非 (*Hán Fēi*) harvest** — 35 lemmas read, 7 forks logged. The oldest surviving commentary on the Laozi, five centuries before 王弼 (*Wáng Bì*), and the only one that argues by anecdote.
- **T5-1 declined — prototyped, not argued.** Recorded as a decline rather than dropped, because a prototype that was never given its argument is not evidence either way.

## 2026-09-07 — Pass D closes: the editing pass reaches 19 of 19

The first draft had been complete since 2026-08-26; the editing pass was the work. Pass D was the chapter-level rewrites, and it had been given **one row per chapter** on 2026-09-02 precisely so they could be checked off one at a time and could not drift as a block.

- **Pass D complete — chapters 3 · 4 · 8 · 10 · 11 · 13 · 16 · 22 · 23 · 28 · 29 · 31 · 32 · 35 · 36 · 38 · 39 · 41 · 64.** Gate green: 0 errors, 124 tests, hard breaks intact, worklist consistent with itself.
- **The 大 (*dà*) family settled** — how this book measures, and what it declines to import. 大 locked to *great* as the 42nd glossary entry.
- **士 (*shì*) locked to *in service*** — the 43rd entry, and the commentators chose it rather than us.
- **Ch 31: 君子 (*jūnzǐ*) stops wearing 聖人 (*shèngrén*)'s clothes**, and 左/右 restored.
- **The constellation graph regenerated after CI caught `data/` stale** — the gate doing the job the gate exists for.

## 2026-09-05 — The repetition *is* the argument, and the tools could not see it

Chapter 11 is the book's clearest single argument and it is built out of literal repetition: 當其無 (*dāng qí wú*) letter for letter, three times, over a cart, a vessel and a room, with only the object changing. **Our English changed everything else instead**, supplying a different location each time — and there was nothing left to click.

- **The finding recorded as [DISCOVERIES § 6](DISCOVERIES.md).** The tools could not see it because the formula finder worked *across* chapters and not *within* one.
- **The formula finder extended to within a chapter as well as across** — the fix to the blind spot, made in the same pass that found it.
- **Six chapters closed** — 11, 13, 16, 35, 36, 39 — including ch 39's cart line, where the mirror had been inverted, and ch 16's chain, where 容 (*róng*) had two Englishes and that was the only broken link.
- **復命 (*fùmìng*) → *returning to what is given***, with 命 (*mìng*) given its own entry: 天命 and 性 are both absent from this book, and the rendering had been importing them.
- **王 (*wáng*) → *supreme authority* in ch 16 — sovereignty was the overlay.**
- **The Progress line's counts stop being hand-kept.** `chapter-tally` derives them. A hand-kept tally had read *"43 open · 18 done"* and matched nothing.

## 2026-08-30 — The documentation stops duplicating itself

Three copies of the lock table existed, one of which had gone stale twice in a week. `CLAUDE.md` was restating `WORKLIST.md`. A "Current state" section held status that belonged in one file and rules that belonged in several others.

- **The hand-kept locks table deleted, and two more copies with it.** `glossary/terms.yaml` is generated from the entries and is the only one.
- **"Current state" dissolved** — status to `WORKLIST.md`, rules to where they apply.
- **[`ARCHITECTURE.md`](ARCHITECTURE.md) written** — the system mapped, and *what is generated and from what* stated once.
- **Two gates added for files that had none, and a generator made deterministic** — the ordering that became the `deterministic-before-gated` principle.
- **Three files, three questions — and no symlinks.**

## 2026-08-29 — A coordinate-addressed corpus, and RETROFIT becomes WORKLIST

- **The corpus becomes coordinate-addressed**, with the character atlas and a front door.
- **`RETROFIT.md` renamed to [`WORKLIST.md`](WORKLIST.md)** so `git log --follow` still reaches the project's start; `EDITING-PASS.md` merged into it the following day and both old files deleted. The old debt list had grown to 343 lines and gone stale, which is why closed items now leave the file and become one line in a ledger.
- **Three new locks and their sweeps.**
- **The `unmarked-lemma` defect fixed** — after which 35 of 53 commentary lemmas diverged and carried `*`, and `check_locks` could see them.

## 2026-08-28 — The first draft is complete: 81 of 81

- **Every chapter drafted.** Chapter 22 repaired in the same pass.
- **`no-new-tooling` set aside permanently** — Shalom's call, `until: standing`. It existed to keep tooling from displacing the first round of translation, and that round had closed. The sentence it suspends stays where it was written, per that ledger's doctrine that a call suspends and never deletes.
- **Passes 0, A and B run** — five text bugs; 強 (*qiáng*) → **strong**, completing the four-word table; 仁 (*rén*) → **humaneness**, 慈 (*cí*) → **tenderness**, 孝 (*xiào*) → **devotion**.
- **The ch 19 Guodian fork recorded as facts** in `sources/variants.yaml`.

## 2026-08-24 — Four locks, the oldest witness, and a discovery stamped wrong

- **敢 · 爭 · 王 · 天 locked** — *"a boar, a tug of war, and no Heaven."* 天 (*tiān*) away from "Heaven" is the single most consequential of the four.
- **`sources/guodian-inventory.yaml` built** — which chapters sit on which slips, in which bundle and in what order. Facts about an object recovered from the ground, never a text. `concordance.py --witnesses N` now answers *does the oldest witness even have this chapter?* before drafting.
- **A discovery stamped as wrong rather than deleted.** The contrast `DISCOVERIES.md` § 1 drew was withdrawn on 2026-08-20 — the Ch 25 silks do not read what it claimed — and the banner stays so a reader who finds the old claim quoted elsewhere can follow it here and see that it fell.

## 2026-08-17 — The Guodian question, asked properly and answered no

Shalom asked for a public-domain Guodian concordance to be vendored. It was **searched for rather than ruled out from memory**, because `sources/PROVENANCE.md` had already been wrong about a licence once.

- **There is no public-domain transcription of the Guodian slips, and there cannot be one yet.** The standard 釋文 was published by 文物出版社 in 1998 and is squarely in copyright. Chinese Wikisource hosts a page, and three separate reasons rule it out — a reconstruction is not a faithful transcription, it names no edition, and it carries an unmarked editorial layer.
- **The search is recorded in full so nobody repeats it**, including the finding that *a `shaloms-call` cannot fix this one*: a call sets aside a rule of this repository, and cannot set aside someone else's copyright.

## 2026-08-11 — The harness, and all three classical commentaries

The original plan deferred every check to Chapter 81, on the grounds that building checks before the corpus exists is premature. **That was sound and it expired**: 62 of 81 chapters existed and had been swept, so the last 19 could be drafted *into* a checked corpus. The proof was ch 53, which rendered 大道 correctly and then incorrectly one line below, inside the range the hand sweep had certified clean.

- **The harness built** — the locks become tests. `build.py` stays deferred on its own merits, because the text is still moving and every edition built now would be built twice.
- **All three classical commentaries vendored** — 王弼 (71 of 81 chapters), 河上公 (81 of 81), 韓非子 (the 17 he discusses) — and **every importer verifies itself** against our own base text, marking divergent lemmas rather than normalising them away.
- **The variant apparatus founded** (`sources/variants.yaml`) and base-text provenance written.
- **Ch 21's parallelism resolved**, which is what forced the commentaries to be fetched in the first place.
- **Hard line breaks restored across all 61 drafted chapters** — the marks are ours, the music is the source's.

## 2026-08-10 — Eight core terms locked, every chapter swept, the Google Doc retired

The first hand sweep, roughly 40 chapters, every lock then settled. **It cost twice**, and both of its misses were later found by Shalom reading the page rather than by any tool — which is the origin of the rule that a check must fire on evidence and never on English alone.

- **Eight core terms locked** and swept across the manuscript.
- **The Google Doc retired.** The manuscript becomes the repository.

## 2026-08-09 — The repository founded

- **Initial commit: translation, glossary, notes, and method.** 61 chapters drafted, the glossary begun, and `process/method.md` written first — the operating system for everything after.
- **Public domain from the start.** CC0, with no exceptions, so the free gift and the paid companion volume can both stand on it.
