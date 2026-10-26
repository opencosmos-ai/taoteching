# PLAN — the harness

**Status: built 2026-08-11**, except `build.py`, which stays deferred. See `process/shaloms-call.md` → *no-new-tooling* for the call that authorized it, and the reasoning.

*The original plan deferred all of this to Chapter 81, on the grounds that "building it earlier means building checks before the corpus exists to check." That was sound, and it expired: 62 of 81 chapters existed and were swept, so the remaining 19 could be drafted **into** a checked corpus rather than swept afterward. The proof the deferral had outlived its logic was Ch 53, which rendered 大道 (dà dào — "the great Tao") as "the great Way" one line below rendering it correctly, in a chapter carrying `retrofit: []` inside the range the hand sweep had certified clean.*

**The rule this plan originally protected — do not stop drafting to build tooling — resumes when phases A–F are done.** `build.py` remains deferred on its own merits: the text moves in 19 more chapters, and every edition built now would be built twice.

> **⚠ Superseded 2026-08-28. The rule above is set aside permanently** — Shalom's call, logged at `process/shaloms-call.md` → *2026-08-28 · no-new-tooling*, `until: standing`. It existed to keep tooling from displacing the first round of translation, and that round closed at 81 of 81 on 2026-08-26. The sentence stays where it is written, per that ledger's doctrine that a call suspends and never deletes; read it as history, not as a live constraint. **`build.py` is still deferred, but now on its own merits alone** — the text is still moving.

---

## Why this ordering

The failures this harness prevents are already documented and real: 德 slipping back to "virtue" in a Ch 59 draft; 常 vanishing four times in Ch 1; 萬物 becoming "all things"; 明 rendered two ways across a repeated formula; the Sage once called "he." Every one is a **memory** failure, not a filing failure.

`CLAUDE.md` addresses that class of error *now*, by loading the rules into every session. The harness addresses what `CLAUDE.md` cannot: **mechanical verification across 81 chapters at once.** That is an editing-pass activity.

---

## 1. ~~`glossary/terms.yaml` — the locks as data~~ ✅ **DONE (2026-08-10)**

*Built early, deliberately: adding frontmatter to 17 entries was cheap, and retrofitting it to 40 later would not have been. `tools/build_index.py` generates both `terms.yaml` and `INDEX.md` from each entry's frontmatter, recomputing chapter lists from `source/chinese.md` so they cannot drift. `check_locks.py` should read `terms.yaml` rather than a hand-kept list.*

<details><summary>Original spec</summary>

The glossary entries are essays; they carry the reasoning and must stay prose. This file is their machine-readable shadow.

```yaml
- term: 德
  pinyin: dé
  render: integrity
  forbidden: [virtue, Virtue, moral excellence]
  status: locked
  entry: glossary/de-德.md
  chapters: [10, 21, 23, 38, 41, 49, 51, 54, 55, 59, 60, 63, 65, 68, 79]

- term: 明
  pinyin: míng
  render: null              # UNDECIDED — see WORKLIST.md
  candidates: [clear-seeing, illumination]
  status: open
  chapters: [10, 16, 22, 24, 27, 33, 36, 41, 52, 55, 65]
```

Fields: `term · pinyin · render · forbidden · status (locked|open|watchlist) · entry · chapters · notes`.

**Seed it from:** the locks table in `CLAUDE.md`, the watchlist in `process/overlay-audit.md`, and `WORKLIST.md`.

</details>

## 2. `tools/check_locks.py` — principles become tests ✅ **DONE (2026-08-11)**

*Nine rules, 39 tests, 0.16s on the whole book. The design decision that made it usable is the **evidence gate**: no rule fires on English alone, because every chapter file carries its own Chinese. First run found 9 errors with zero false positives — see `WORKLIST.md` → Open. Two rules were not in this spec and earned their place: `mechanistic-register` (which found "source code" live in ch 21) and `stale-shaloms-call`.*

<details><summary>Original spec, and what changed</summary>

The highest-value tool by a wide margin. Reads `terms.yaml`, scans the `## Translation` block of every chapter file, reports violations.

Checks:

- **Forbidden renderings** — "virtue", "heaven", "eternal", "cosmos", "mystery", "sin", "righteousness", "the myriad things", "Holy Man".
- **The Sage pronoun rule** — any `he/his/him` within a sentence of "Sage" or "Master". Zero tolerance; this is a standing rule.
- **Repeated-formula consistency** — lines identical in Chinese across chapters (知常曰明 in 16/55; 生而不有 in 10/51; 不道早已 in 30/55; 玄德 refrains) must be identical in English. Detect by matching source rows, then diff the corresponding English.
- **Devotional capitalization** — flag capitalized Way, Virtue, Heaven, Nature, Being, One outside sentence start.
- **Status coherence** — `status: drafted` with an empty translation block, or a chapter whose `terms:` frontmatter omits a term present in its source rows. **⚠ NOT BUILT.** This is the one bullet in the spec that was never implemented, and the section is stamped ✅ DONE above it. Two chapters (65, 20) later turned out to be exactly what it describes and were found by hand instead. Carried forward as `incomplete-draft` under *Proposed rules, unbuilt*.

Output: grouped by chapter, with the rule cited and the glossary entry linked. Exit non-zero on violations so it can run in CI.

**What changed in the building:**

- **Repeated-formula consistency is a `warn`, not an `error`, and does not attempt alignment.** The spec assumed you could "detect by matching source rows, then diff the corresponding English." You cannot: verse lines align to source rows in only 27 of 62 drafted chapters, and the literal glosses speak pre-lock English (玄德 is glossed "dark/mysterious virtue/power" where the verse correctly reads "profound integrity"), so gloss-matching fails exactly where the locks matter. Three attempts at inference all failed. The rule now asks an alignment-free question — two chapters sharing a verbatim Chinese segment should have *some* pair of similar lines — which took it from 21 warnings to 11, most of them real, and caught ch 23's 信不足焉.
- **Formulas are indexed as comma-segments, not n-grams.** Sub-segment n-grams produce fragments no translator rendered as a unit (難得之貨 inside 不貴難得之貨), each a warning about nothing.
- **Case policy is derived, not configured.** A forbidden string written with a capital means the capital is the violation. This needed no frontmatter changes and cleared six false positives on "Being".
- **`--staged` mode, error-only, skipping `status: untranslated`** — so a half-drafted chapter never argues with the hook.

</details>

### Proposed rules, unbuilt

*~~Both are blocked on the same thing: `no-new-tooling` is back in force, so each needs its own `shaloms-call`.~~ **Unblocked 2026-08-28** — the rule is set aside permanently, so neither needs a call. Both close a hole a human sweep has already fallen through, which is the argument for them.*

*Where they stand now. **`glossary-self-check` is the live one**, and independent of any other work — build it. **`incomplete-draft` is subsumed**: it and the thin-translation heuristic in `WORKLIST.md` T5-1 are both ratio statistics over the corpus, and both fall out of the witness database's analysis layer rather than needing a separate rule. Doing it there once beats doing it here twice.*

- [ ] **`incomplete-draft`** — error when `status: drafted` but the `## Translation` block is empty, is placeholder text, or has fewer verse lines than a floor derived from the chapter's source rows. **This was in the §2 spec as "status coherence" and never built.** The cost of not having it is measured: Ch 65 carried `status: drafted` over three ellipses and a fragment, and Ch 20 over 10 verse lines against 25 source rows, missing its whole opening movement. Both survived the 2026-08-10 hand sweep and every session after it, and both were found by Shalom reading the page. **No existing rule can catch this** — every lock keys off the Chinese to judge the English, so a chapter with no English passes all of them trivially.

- [ ] **`glossary-self-check`** — run the forbidden-rendering rules over `glossary/*.md` as well as `chapters/*.md`. **The locks are currently enforced against the manuscript but never against the files that define them.** Found 2026-08-23: a single line of `glossary/ziran-自然.md` carried two violations at once — a stale "dare" for 敢 and "the ten-thousand things" for 萬物, which is forbidden outright — inside a `status: locked` entry. *Design note: this cannot reuse the chapter rule as-is, because a glossary entry **has to** print the forbidden word — quoting it and arguing against it is the entry's whole job, and `gan-敢.md` says "dare" eleven times on purpose. So invert the chapter rule's default: instead of scanning everything and excluding, scan **only the entry's own English** and ignore the argument around it. That means the `> *…*` gloss lines under a quoted Chinese line, plus the `render:` frontmatter and the "Where it stands" table — which is exactly where the two `ziran-自然.md` violations sat. Everything else in an entry is prose about words and must stay exempt.*

## 3. `tools/concordance.py` — term in, evidence out ✅ **DONE (2026-08-11)**

*The highest-value mode turned out to be the one this spec did not have: `--english`, the reverse direction. A lock is a two-way claim — every 明 renders as clear-seeing **and** every clear-seeing renders 明 — and only that direction catches a rendering applied where its character is absent.*

<details><summary>Original spec</summary>

Replaces the ad-hoc `bash`/`docx` greps used throughout drafting. Given a character or phrase:

- every chapter containing it, with the full Chinese line
- the current English for that line
- whether renderings are consistent, and where they diverge

This is how you catch drift across 81 chapters, and how future glossary entries get their evidence base. (The 天地 entry was built exactly this way — the finding that 陰 appears *once* in the whole book, and 天地 in exactly seven chapters, came from this kind of sweep.)

Add `--pairs` to compare two terms across chapters (the 我/吾, 玄/妙, 正/奇 work).

</details>

## 4. `tools/build.py` — one command to the book ⏸ **still deferred**

*The one item where the original ordering holds. Every edition built while the text is moving is built twice; build it when the editing pass settles. (The draft finished on 2026-08-26; the Library and the Character Atlas are built from the export meanwhile.)*

Assembles `chapters/*.md` into deliverables, ending the Google Drive round-trip:

- **Reading edition** (.docx / .pdf / .epub) — verse only, clean typography, the public-domain gift.
- **Study edition** — verse plus source table, pinyin, literal gloss, and the notes for that chapter. *(Named for what it is for, not who it is for: "Scholar's edition" quietly tells an ordinary reader the book is not theirs.)*
- **Companion draft** — glossary entries, threaded reading notes, the method and audit, in reading order.

Three editions, one source of truth. Use `pandoc` where possible; `python-docx` for fine control (the existing v2 table styling is a known-good starting point).

## 5. A chapter-review skill ✅ **DONE (2026-08-11)**

*`process/skills/chapter-review/`. The `glossary-entry` skill was updated in the same pass to use `concordance.py` instead of its inline heredoc.*

The per-chapter workflow (`CLAUDE.md` → *Per-chapter workflow*) is stable enough to encode as a reusable skill: read the Chinese cold → decompose contested characters → check witnesses and commentaries → check locks and the overlay watchlist → **take a stand** → offer clay → log the notes → record retrofit.

Encoding it makes the method **portable and repeatable** — identical whether Claude or Fable is driving — and means the process guide gets *executed*, not merely hoped over. This is also how the method transfers to Fable for the final refinement pass without depending on someone remembering to read `process/method.md`.

## 6. CI ✅ **DONE (2026-08-11)**

`.github/workflows/checks.yml` runs the tests, `check_locks.py`, `fix-linebreaks.py --check`, and a `git diff --exit-code glossary/` proving the generated files are current. `.githooks/pre-commit` gates locally on staged chapters at error severity only — install with `git config core.hooksPath .githooks`.

## 7. `shaloms-call` — the override of record ✅ **DONE (2026-08-11)**

Not in the original plan, and the reason this one could be written at all. `process/shaloms-call.md` records a rule Shalom has set aside, with scope, expiry, and reason. Suspensions are never silent (the checker prints a footer naming them) and an expired call is an error, so each is renewed or retired deliberately. Without it, an override lived only as a sentence in one conversation — invisible in the repo, and leaving the AI to re-argue a settled decision next session.

## 8. `sources/` — the witnesses and commentaries, in the repo ✅ **DONE (2026-08-11)**

**Built:** `sources/PROVENANCE.md`, `sources/variants.yaml` (23 forks), **all three classical commentaries — Wang Bi (71 ch.), Heshang Gong (all 81), Han Feizi (the 17 he discusses)**, `tools/import_commentary.py`, `concordance.py --witnesses N` and `--commentary N`, and `check_locks.py`'s `unlogged-variant` rule. 53 tests.

**The licensing blocker did not exist.** This section previously said Wikisource was unusable because its content is CC BY-SA. Its *copyright policy* says the opposite — a faithful transcription of a public-domain work creates no new copyright, and "the CC BY-SA default license for contributions never comes into play for mainspace content." The Siku Quanshu (1782) transcription is tagged `{{PD-old}}` and, by its own editorial policy, carries **no punctuation** — the authorial layer only. Recorded as a correction in `PROVENANCE.md` rather than edited away.

**The import verifies itself**, which is what makes it trustworthy: the source interleaves Laozi lemmas with Wang Bi's comment on each, so every lemma is checked against our own `source/chinese.md`. 328 matched exactly, 26 with variants, 93%. Lemmas that differ are reported, never normalized.

**And it paid for itself on the first run**, which is the argument for having done it:

- **Ch 21** — the Siku compilers' own collation note reads 〔案狀各本俱作然〕, *"for 狀, all editions read 然."* Our reading is a minority one across the editions they knew, not merely a divergence from the silks. A decision made hours earlier now wants reopening.
- **Ch 2** — the Siku Wang Bi reads 相較 / 相傾 where our base reads 相形 / 相盈, which are the *Mawangdui* readings. **Our "Wang Bi base text" already carries non-Wang-Bi readings.**
- **Ch 55** — `notes/manuscript.md` claimed our base text reads 全 and that we kept it. Our source table reads 朘; the verse renders 全. The note misdescribed our own text.
- **Ch 63** — Wang Bi sets 大小多少報怨以德 as **one lemma** and glosses it 小怨則不足以報…順天下之所同者徳也, which dissolves the "four bare characters" crux and makes 報怨以德 a rule against private revenge rather than personal forbearance.

**Heshang Gong added the same day**, assembled from 77 scan pages of *Sibu congkan* 0532 (a Song woodblock), complete at 81/81 with his own chapter titles preserved. **Han Feizi added the same day** — the oldest commentary there is, indexed by matching his 「」 quotations against our base text. **The "53 of 53 exact" originally recorded here was the bug, not the result** — `_parse_essays` never ran the fidelity check the other two importers run, so every quotation was written as an exact lemma. Corrected 2026-08-29: 35 of 53 diverge and now carry `*`, and `check_locks.py`'s `unmarked-lemma` rule enforces it. **Nothing in `process/method.md` §3 is now missing, and every chapter has at least one commentary.** What could still be added: the 10 unproofread Wang Bi chapters, the Fu Yi recension, and a variant sweep for chapters not yet in `variants.yaml`.

*Proposed 2026-08-11, after Ch 21 required fetching Wang Bi, Heshang Gong, and both Mawangdui silks from the open web to answer one question about one line. ~~**Needs its own `shaloms-call`** — the existing suspension of the no-new-tooling rule covers phases A–F only, and this is new scope.~~ **Built 2026-08-11**, and the rule that gated it is set aside permanently as of 2026-08-28.*

### Why

The research process currently depends on a search engine every time a line is contested. Three problems with that, in order of severity:

1. **Search summarizes, and a summary can be wrong.** On Ch 21 the first search correctly reported the 自古及今 / 自今及古 fork — but the three *other* forks in the same two lines (順/閱, 父/甫, 然/狀) only appeared after fetching the actual silk text. A paraphrase of a variant is not evidence of a variant.
2. **It is not reproducible.** No reader can audit the claim "both Mawangdui silks read 自今及古" against anything in this repo. For a CC0 edition whose whole argument is *we show our work*, that is a real gap.
3. **It does not scale to the operation we actually need.** What Ch 21 required — align the witnesses for a line, spot the meaning-bearing forks — is mechanical, and should be one command for any of the 81 chapters, run *before* drafting rather than after.

### What it buys

- `concordance.py --witnesses 21` — the forks for a chapter, aligned, before a word is drafted.
- A new `check_locks.py` rule: **a meaning-bearing variant present in the apparatus but absent from `notes/manuscript.md`** — a fork translated over without a logged decision. This would have caught Ch 21's reversed chronology before the chapter was drafted.
- **It audits backwards.** Sixty-two chapters were drafted with no variant apparatus. This finds the other places a Wang Bi reading quietly decided a line.

### The licensing analysis — read this before copying anything

**The trap:** the obvious sources are not CC0-compatible.

| Source | License | Compatible with CC0? |
|---|---|---|
| **ctext.org** structured data | CC BY-**NC**-SA 3.0 | **No** — ShareAlike cannot be relicensed CC0, and **NonCommercial poisons the companion volume** |
| **zh.wikisource.org** | CC BY-SA 4.0 | **No** — ShareAlike |
| Pre-1929 printed editions | US public domain by date | **Yes** |

**The NonCommercial clause is the sharper problem than the CC0 one.** `shalomormsby/taocompanion` exists so this work can sustain a family. An NC-licensed dependency anywhere in a commercial book's derivation chain is exactly the wrong shape — worse than the CC0 issue, because CC0 is a gift Shalom controls and the companion is income he needs.

**The legal reality is probably fine, and that is not good enough.** Copyright covers original expression; 道可道非常道 is 4th-century BCE and free, and a faithful transcription of a public-domain text attracts no new copyright in the US (*Feist v. Rural Telephone*, 1991, rejecting "sweat of the brow"; *Bridgeman v. Corel*, 1999, for faithful reproductions). What a site **can** own is the compilation, the metadata, and the **added punctuation** — and `notes/translation.md` already establishes that all punctuation in the Chinese is a later editor's addition, not the source's.

But a repository whose first line is *"entirely CC0, with no exceptions"* must not rest its cleanliness on a doctrinal argument about originality. It must be **obviously** clean to a reader who does not want to litigate *Feist*.

### What may and may not be vendored

| Material | Call | Why |
|---|---|---|
| Wang Bi commentary (c. 249 CE) | **vendor** | pre-1929 printings exist in quantity |
| Heshang Gong commentary (Han) | **vendor** | same |
| Han Feizi 解老 / 喻老 (3rd c. BCE) | **vendor** | same |
| Laozi base text | **vendor, re-provenanced** | ancient; re-derive from a named pre-1929 edition, not from ctext |
| **Mawangdui** (excavated 1973) | **do not vendor** | every transcription is modern, and reconstructing the damaged characters is genuine editorial work |
| **Guodian** (excavated 1993) | **do not vendor** | same |
| Modern critical apparatus, annotations, translations | **do not vendor** | in copyright |

**For the excavated witnesses, record the facts rather than the text.** "Mawangdui A and B read 自今及古 where Wang Bi reads 自古及今" is a *fact about a text*, and facts are not copyrightable. This is already what `notes/manuscript.md` does in prose; the change is to make it machine-readable and cite the scholarship instead of reproducing it. Arguably better research practice than copying a transcription, not merely safer.

### Shape

```
sources/
  PROVENANCE.md         per-file: work, author, date, edition, where obtained,
                        rights reasoning, and what in it is editorial
  wangbi/               commentary, by chapter
  heshanggong/          commentary, by chapter
  hanfeizi/             解老 / 喻老
  variants.yaml         the apparatus: chapter · line · witness · reading · our call
                        (facts only — no reconstructed transcriptions)
```

Every vendored file carries frontmatter naming the **specific printed edition** it was transcribed from. A file whose edition cannot be verified does not go in.

### Immediate, separable action ✅ **DONE (2026-08-11)**

**Re-provenance `source/chinese.md`.** Done. The header now rests the CC0 dedication on **the age of the text and nothing else**, cites *Feist* (1991) and *Bridgeman* (1999) for why a faithful transcription of a public-domain work creates no new copyright, and names four **independent pre-1929 printings** where the recension can be verified: the Ming *Zhengtong Daozang* (1445), the *Siku Quanshu* (1782), the Zhejiang *Ershi'er zi* (1875), and the Commercial Press *Sibu congkan* (first series from 1919).

It also states plainly that **the punctuation is editorial and forms no part of the source** — the one element of a modern edition that could carry a thin claim, and the one this project already treats as its own on the record (`notes/translation.md`, *Standing principle · Lineation and punctuation*). ctext keeps a courtesy credit as a transcription check, with its licence named, and nothing depends on it. `process/method.md` §3 and `AGENTS.md` updated to match.

---

## What is left

1. ~~**Resolve the 8 open findings** in `WORKLIST.md` → *Open*.~~ *Done: `check_locks.py --severity error` is green.*
2. ~~**Re-provenance `source/chinese.md`** off ctext~~ ✅ **done 2026-08-11** (§8).
3. ~~**Build `sources/`** (§8)~~ ✅ **done 2026-08-11** — all three commentaries in.
4. ~~**Draft chapters 70–81**~~ *Done: all 81 were drafted by 2026-08-26, through the `chapter-review` skill.*
5. **`build.py`**, when the text has stopped moving.

---

## Open todos — the Guodian debts

*Opened 2026-08-17, from building `sources/guodian-inventory.yaml`. The inventory answered a question nobody had been able to ask before — **does the oldest witness even carry this chapter?** — and asking it across all 81 surfaced work owed on chapters already drafted. Each of these is a fact-recording job, not a transcription: see `PROVENANCE.md` → "The Guodian question, asked properly and answered no."*

- [x] **G1 · Ch 19 — the largest unrecorded divergence in the book.** *(Closed 2026-08-28: recorded in `variants.yaml`, logged in `notes/manuscript.md` · Ch 19.)* The best-known meaning-bearing fork in the entire Guodian Laozi sits in this chapter: the received text's attack on 聖 (*shèng* — sagehood) and 仁義 (*rén yì* — humaneness and duty) is **not** what the slips carry. Ch 19 is drafted, carries `retrofit: []`, and our apparatus is silent. Record the fork in `variants.yaml` as a fact, decide, and log in `notes/manuscript.md`. **Highest value of anything on this list** — it may change a drafted chapter's argument, and it bears directly on the overlay watchlist, since 聖 and 仁義 are two of its flagged characters.

- [ ] **G2 · Ch 25 — `DISCOVERIES.md` §1 is missing its oldest witness.** *Checked 2026-08-20, and the premise was backwards:* Guodian, both silks and Beida all read 王 (*wáng* — king); 人 (*rén* — human) is 傅奕's and 范應元's. `variants.yaml` and `notes/manuscript.md` are corrected. **Still owed:** rewriting `DISCOVERIES.md` §1, which carries a *do not write from this* banner until then.

- [ ] **G3 · Ch 17–18 are one passage at Guodian, with no chapter division.** The slips run them continuously. If that holds, the collapse of 大道 (*dà dào* — the great Tao) into 仁義 in Ch 18 reads as the *consequence* of Ch 17's ladder of rulers rather than a fresh assertion — an interpretive shift across two drafted chapters. Belongs in `notes/reading.md` as a Thread, not just an apparatus line.

- [ ] **G4 · Ch 5 and Ch 16 — the famous parts are the missing parts.** Guodian carries only the *middle* of Ch 5, so 天地不仁 ("sky and earth are not humane") is unattested there; and only the *opening* of Ch 16, so its movement through 常 (*cháng* — the ever-present) is unattested. Both are drafted. Worth a reading note: the oldest witness is silent exactly where the chapters are most quoted.

- [ ] **G5 · A Guodian sweep of the remaining 26 attested chapters.** The inventory names 31; G1–G4 cover five. The rest have no Guodian line in `variants.yaml` at all. Work chapter by chapter, recording facts only. Low urgency per chapter, high value in aggregate.

- [ ] **G6 · Chapters 67–81 have no Guodian witness — say so once, in the apparatus.** 66 is the highest-numbered chapter attested anywhere at Guodian. Chapters 67–81 rest on the Mawangdui silks and later witnesses alone. `--witnesses N` now prints this per chapter; the *pattern* deserves a note, because it is a fact about the book's formation and not only about our sources.

**Not on this list, deliberately: vendoring a Guodian text.** Asked and answered 2026-08-17 — there is no public-domain transcription and there cannot be one yet. The 釋文 is 1998 living scholarship. See `PROVENANCE.md`; a `shaloms-call` cannot reach it, because it is someone else's copyright and not our rule.

*Steps 1–2 of the original ordering are already done: the Google Docs import is complete and the Doc retired; `terms.yaml` was built 2026-08-10. The open locks 明 and 無為 were settled before this build, so the sweep happened once, as intended.*

---

## What the building taught

Kept here because the next tool in this repo should start from it.

- **The evidence gate is the whole design.** A checker that fires on English alone is a grep with opinions, and at ~33% noise it gets switched off inside a week. This one never fires without the character to prove it, which is possible only because every chapter file carries its own Chinese. It is the difference between 20 flags and 9 findings.
- **Two tools, opposite contracts.** Precision for the gate, recall for the report. Merging them yields something too noisy to gate and too quiet to search.
- **Do not infer what the data cannot support.** Three attempts to align verse lines to source rows all failed, for three independent reasons. The rule that works asks a question needing no alignment at all. When inference keeps failing, change the question rather than tuning the guess.
- **The literal glosses are pre-lock English.** They say "virtue", "ten thousand", "mysterious". Any tool that matches the manuscript against them will fail hardest on exactly the terms the locks exist to protect.
- **Encode invariants, never taste.** Every rule cites a written decision. A rule with no citation is a tool author's opinion wearing a build's authority — which is the "automated quality scoring" refused below.
- **Suppression has to exist, and has to cost something.** Unsuppressable rules get disabled wholesale; free suppression rots. Hence `lock-ok` with a required reason and an unused-waiver error, and `shaloms-call` with a required `until:` and a stale-call error.

---

## Deliberately not building

- **A translation memory / alignment database.** The glossary already does this, in prose, better.
- **Automated quality scoring.** The whole method rests on human judgment sharpened by argument; a metric would be a false authority.
- **Anything that suggests renderings.** The AI's role is to argue for the deepest reading, not to autocomplete the verse. The verse stays Shalom's own.

---

## The 2026-08-10 hand sweep — the record

| Term | → | Chapters fixed |
|---|---|---|
| **樸** | uncarved wood *(lowercase)* | 15, 19, 28, 32, 37 — plus 2 dependent lines in 32 |
| **萬物** | **the countless things** *(re-locked; see below)* | 1, 2, 4, 8, 10, 16, 32, 34, 37, 39, 40, 41, 42, 51 |
| **天地 / 天下 / 天** | sky and earth · the world · nature | 7, 9, 10, 22, 23, 25, 32, 37, 39, 40, 47, 59 |
| **玄** | dark · profound | 4, 6, 10, 15, 51, 65 |
| **常** | the ever-present | 16, 34, 46 |
| **一** | lowercase *the one* | 10, 22, 39, 42 |
| **明** | clear-seeing · clarity | 33, 36, 52 |
| **無為** | non-doing | 37, 43, 48, 57 |
| **無 / 有** | absence / presence | 2, 40 |
| **自然** | of itself / of themselves · so of itself | 23, 25 |
| **義 / 仁** | duty · humaneness | 18, 19, 38 |
| **知足** | knowing you have enough | 33, 46 |
| **天** (Ch 16 ladder) | the open sky | 16 — see below |

**萬物 re-locked as "the countless things"** *(was briefly "the ten-thousand things")*. 萬 is a **scorpion** borrowed for its sound — the quantity is a phonetic accident, and 萬 meant *beyond reckoning*, which "ten thousand" now inverts for a reader who knows the scale of the universe. Rejected: *"all things"* (a totality where 萬物 is a teeming plurality) and *"beings"* (imports Buddhist 眾生, over-narrows to inner life, and collides with the "Being/Non-Being" rendering already rejected for 有/無). *Ruling: `glossary/wanwu-萬物.md`.*

**Three corrections the verification pass caught:**

> **ch 30 / ch 55** — 物壯則老 is **verbatim in both** and was rendered two different ways. Now identical in both: *"When things reach their peak strength, they decay."*
> **ch 25** — "All matter was formed from the formless" → *"**Something** formed in the undifferentiated."* 有物混成 says *there is a **something***, singular and indefinite — not "all matter," which makes it plural and material and quietly turns the pre-cosmic Tao into stuff.
> **ch 10, 41** — both contained "the ten-thousand things" where the Chinese has **no 物 at all** (生之畜之 in 10; 善貸且成 in 41 — the object is only the pronoun 之, *them*). Swept for consistency, but flagged: the noun is **supplied by the translator**, not present in the source.

**Ch 16's ladder, resolved.** 王乃天，天乃道 now reads *"Sovereignty leads to the open sky. / The open sky leads to the Tao."* Two constraints decided it: Ch 16 and Ch 25 share this exact 天→道 step, so both must say **sky**; and the passage is *anadiplosis* (each line ends on the word the next begins with), so the qualifier had to repeat rather than be introduced once and dropped. **公 was corrected in the same pass** — "equanimity" → **"impartiality"** (公 is the opposite of 私, *private/selfish*), which makes the whole ladder legible as one continuous widening beyond the self. *Logged in `notes/translation.md` and `notes/reading.md`.*

**Also corrected in passing:** Ch 36's "the tools of nature" → *"the sharp instruments of the state"* (國之利器 — 國 is the **state**; "nature" was simply wrong). Ch 22's "therefore is eternal" → *"therefore endures"* (長, not 常). Ch 7's whole opening — 天長地久 is 長/久 (*lasting/enduring*), not 常.

---

## What Chapter 11 taught the tools — 2026-09-05

*One lesson, and it inverted what two tools were built to do. `DISCOVERIES.md` §6 carries the finding about the text; this is the harness record. Tests in `tools/tests/test_concordance.py`.*

**A formula repeating *inside* one chapter was structurally invisible.** `check_locks.py`'s `repeated-formula` rule and `concordance.py --formulas` both indexed each Chinese segment into a **set of chapter numbers**, then reported the segments appearing in more than one. Three occurrences in a single chapter therefore collapsed to one entry and were dropped as *"not shared."*

Chapter 11 repeats 當其無 (*dāng qí wú* — "right where its absence is") verbatim three times, and 有X之用 three times, and our English rendered every one of them differently. **Neither tool could report it**, and no lock could either — every lock keys off a character to judge the English, and each of those lines was defensible on its own. It was found by Shalom reading the page, which is now the third time that has been the finding mechanism (ch 65, ch 20, ch 11).

Stated as the failure it is:

> **The tools enforced consistency where the text was not repeating, and were silent where it was.**

**Three things the repair had to get right, each of which is a test:**

1. **Count occurrences, not chapters.** The set was the whole bug. `_segments()` returns a list of `(chapter, row)`.
2. **A frame is not a segment.** Ch 36's four 將欲X之 clauses are not identical, so exact matching finds nothing; they share a skeleton. `_templates()` clusters same-length segments that agree in all but one or two positions. **The floor is two fixed characters and half the frame** — one anchor is a character, not a frame, and 不▢▢ would collect half the book. That floor is also why ch 8's X善Y is *not* found, and 善's own concordance is where it lives.
3. **Rank by concentration, not frequency.** A frame four times in ch 36 and once in ch 65 is that chapter's formula; one appearing once each in fifteen chapters is grammar. Without that separation 是謂▢▢ (*shì wèi* — "this is called") topped the list, and every real finding was below the fold.

**What was deliberately not done.** `check_locks.py` still compares across chapters only, and is not fed from the new index. Recall reports 152 within-chapter repeats; a gate that fired on those would cry wolf, which is the one thing that checker must never do — and `CLAUDE.md` is explicit that the searching tool and the gating tool stay apart. Whether the gate can carry any of this is open as `WORKLIST` **T5-12**, to be decided after Pass D on the evidence the finder is now producing.

*A fourth thing, found while repairing: the `--json` path carried its own second copy of the indexing and had already drifted from the printed one — `min_len` 4 against 3, and the same fatal set. It reads the shared index now. A fact written down twice, one copy updated, which is the pattern `check_worklist.py` exists for.*

## What the 2026-08-10 sweep taught the checker

*All three below are implemented, and each has a test in `tools/tests/test_check_locks.py` named after it. Three further lessons the build itself taught are at the foot of this section.*

Three failure modes this sweep exposed. Build the checker against them:

1. **Match stems, not whole words.** `\beternal\b` misses "eternal**ly**" — which hid two chapters. Use `eternal`, `everlast`, `illuminat`, `righteous`.
2. **Case-sensitivity cuts both ways.** A case-insensitive scan flags "the one" (correct) as "the One" (wrong), and a case-sensitive one misses "The cosmos" at the start of a line. The checker needs per-rule case policy, not one global flag.
3. **Homophones and false friends are the real trap.** 常 (*cháng*, constant) vs 長 (*cháng*, long); 自然 (*of itself*) vs the ordinary English word "nature"; 一 (*one*) vs the English pronoun "one"; "Block the openings" (塞) vs "uncarved block" (樸). **Every flagged line must be verified against the Chinese in its own chapter before it is changed** — roughly a third of this sweep's initial 93 flags were false positives.

*Moved here from `WORKLIST.md` on 2026-08-28, when that file was merged into `WORKLIST.md`. It is a record of what was done and learned, not work owed, so it belongs beside *What the building taught* rather than in a forward-looking list.*

