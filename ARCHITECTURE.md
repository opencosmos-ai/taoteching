# ARCHITECTURE — how this repository works

*A system-wide map: what holds authority, what is generated from it, what enforces the rules, and how a decision travels from a question about one character to a check that fails the build. For the translation **method**, see [`process/method.md`](process/method.md); for what the work still **owes**, see [`WORKLIST.md`](WORKLIST.md).*

---

## If you read only this

**This repository is a translation that behaves like a codebase.** Every settled decision about a Chinese word is written once, in prose, with its evidence — and then enforced mechanically across all 81 chapters, so it cannot quietly come undone.

Five things, and the first is the one to remember:

1. **If a command can rebuild it, never edit it by hand.** Three directories are edited by hand and hold the truth — `chapters/`, `glossary/`, and the YAML in `sources/`. Everything else, including the vendored commentaries, is generated and can be deleted and rebuilt.
2. **A glossary entry is both an essay and a machine-readable rule.** Its YAML frontmatter names the locked English, the **flexions** — secondary Englishes scoped to named chapters — and the forbidden alternatives; a build step turns that into `glossary/terms.yaml`, which the checker reads.
3. **The checker never fires on English alone.** A forbidden word is an error only when the Chinese character licensing it is present in *that same chapter's* source table. This is the design decision that makes the tool trustworthy enough to gate on.
4. **Two tools, opposite contracts.** `check_locks.py` optimizes precision and fails the build; `concordance.py` optimizes recall, judges nothing, and never fails.
5. **Every override is recorded and costs something** — one finding waived by a `lock-ok` comment carrying a reason, or a whole rule set aside in `process/shaloms-call.md` with an expiry. An unused waiver is itself an error, so the files self-clean.

```
  ┌── AUTHORITY ─ edited by hand ──────────────────────────────────────────────┐
  │                                                                            │
  │   chapters/001-081.md        glossary/*.md            sources/*.yaml       │
  │     verse                      essay                     variants.yaml     │
  │     source table               frontmatter               guodian-inventory │
  │     notes, frontmatter        (render, flexions,         component-glosses │
  │                                forbidden)                                  │
  └────────┬───────────────────────────┬──────────────────────────┬────────────┘
           │                           │                          │
           ├───────────────────────────┼──────────────────────────┤
           │                           │                          │
           ▼                           ▼                          │
     build_db.py                 build_index.py                   │
           │                           │                          │
           ▼                           ├──▶ glossary/INDEX.md     │  human lookup
  data/taoteching.sqlite               │                          │
           │                           └──▶ glossary/terms.yaml   │  the locks, as data
           ├──▶ data/*.csv                        │               │
           ├──▶ data/explorer.html                │               │
           └──▶ data/constellation-*.json         │               │
                                                  ▼               ▼
  ┌── ENFORCEMENT ────────────────────────  check_locks.py  ◀──────┘
  │                                                │
  │        ┌───────────────────────────────────────┴──────────────────┐
  │        ▼                                                          ▼
  │  .githooks/pre-commit                        .github/workflows/checks.yml
  │  staged chapters, errors only                whole book, every push and PR
  └────────────────────────────────────────────────────────────────────────────┘

  check_locks.py also reads chapters/ directly — it needs each chapter's own
  Chinese to decide whether a forbidden English is an error or a false friend.

  sources/commentaries/ and sources/shuowen/ are omitted above: they are build
  products too, written by the importers from gitignored wikitext caches.

  Everything below the AUTHORITY box is generated. Delete data/ and one command
  rebuilds it; delete chapters/ and the translation is gone.
```

---

## The one rule that explains most of the design

> **If a command can rebuild it, never edit it by hand.**

**Every file here is either edited or generated, and none is both.** Before changing any file, ask whether some command produces it. If one does, you are in the wrong file: your change will be silently overwritten by the next build, and whatever you meant to fix lives upstream in the file the tool read.

**Three directories are edited by hand, and they are the truth:**

- `chapters/001-081.md` — the manuscript, edited by Shalom (or another person)
- `glossary/*.md` — the rulings, essay and frontmatter together
- `sources/*.yaml` — the witness apparatus and the Guodian inventory, kept by hand as **facts**, never transcriptions

**Everything else is a build product** — `data/taoteching.sqlite`, every CSV, `explorer.html`, the constellation JSON, `glossary/INDEX.md`, `glossary/terms.yaml`, and **`sources/commentaries/` and `sources/shuowen/`, which are written by importers**. The Markdown build products carry a header saying so; the CSVs cannot, since a comment line would break parsing, so [`data/README.md`](data/README.md) covers them instead.

**`sources/` is therefore split, and the split matters:** the YAML files are hand-kept judgments about what the witnesses read, and the vendored directories are machine-written transcriptions of public-domain texts. Editing a commentary file by hand would break the guarantee that `import_commentary.py` reproduces it byte for byte.

**Why the rule earns its place.** It is what lets the repository be aggressive about tooling without the tooling becoming the work. Delete `data/` entirely and one command rebuilds it. Delete `chapters/` and the translation is gone. It also tells you where a fix belongs: 義 (*yì* — duty) once shipped in the character atlas glossed *"and"*, and the repair was not in the CSV that showed it but two levels upstream — a misplaced bracket in ch 18's source table, and a tie-break in `build_db.py`.

**Two places the rule bends, both deliberate:**

- **`source/chinese.md`** is *derived* from the chapters' own source tables but is **committed and hand-maintained**, because it is the convenient whole-text file several tools read. Change a source table and it must be rebuilt by hand. The `source-drift` rule exists to catch the two falling out of step.
- **`sources/commentaries/`** is generated by `import_commentary.py`, but from wikitext caches that are **gitignored**. So it is a build product whose inputs are not in the repository: re-runnable by anyone with network access, not by a fresh offline clone. That is the price of vendoring provenance rather than pasting text.

---

## The three authorities

| | Owns | Shape |
|---|---|---|
| **`chapters/001–081.md`** | **The manuscript.** The `## Translation` block *is* the translation — there is no upstream and nothing regenerates over it. Each file also carries the chapter's Chinese source table, its per-chapter Notes, and frontmatter (`status`, `retrofit`). | One file per chapter |
| **`glossary/*.md`** | **The rulings.** One entry per term: what the character is, what the conventional English gets wrong, what the classical commentators say, what is set aside and why. The frontmatter carries `render`, `flexions` and `forbidden`. | 48 entries, 14 secondary characters |
| **`sources/`** | **The evidence**, and the one mixed directory. Hand-kept: `variants.yaml` (the witness apparatus, as facts), `guodian-inventory.yaml`, `component-glosses.yaml`, `heshanggong-titles.yaml`. Machine-written: `commentaries/` (three classical commentaries in full) and `shuowen/` (說文解字 — *Shuōwén Jiězì*, the c. 100 CE etymological dictionary). | See *Provenance* below |

Everything else supports these. `notes/` records decisions thinly in three layers — manuscript forks, our own rendering calls, reader-facing threads — and `WORKLIST.md` tracks what is still owed.

**A fourth is emerging: [`process/principles/`](process/principles/README.md), the rules learned by making decisions.** It is not a fourth authority over the *text* — it owns no rendering — but it owns something the other three cannot hold, because a principle discovered while settling one line governs chapters nobody has read yet. The three above are all indexed by the thing they describe: a chapter, a term, a witness. A transferable rule has no such index, so it was landing wherever it was found. Same architecture as the glossary — frontmatter is the source of truth, `INDEX.md` and `principles.yaml` are generated, CI fails if stale — with one addition the glossary does not need: **every `evidence:` anchor is verified to resolve**, because a principle whose link has rotted looks checked.

---

## How a decision becomes an enforced rule

This is the operational heart of the system. A question about one character becomes a check that fails the build in six steps.

```
1. EVIDENCE      concordance.py <char>          every occurrence, line, gloss, verse
                 concordance.py --english "x"   the reverse: is the rendering backed by the character?
                 concordance.py --commentary N  王弼 (Wáng Bì) and 河上公 (Héshàng Gōng)
                 concordance.py --witnesses N   where the older manuscripts disagree
                        │
2. RULING        glossary/<pinyin>-<char>.md    the essay: graph, commentators, rejected
                        │                        candidates, the flexions, what stays open
                        │
3. FRONTMATTER   render: "keep safe"              the machine-readable shadow of the essay
                 flexions: [{english: "keep",   a flexion is DATA: the "where" is a chapter
                   chapters: [9], why: "…"}]    a tool can check, the "why" a sentence for
                 forbidden: ["preserve", …]     the reader. Never prose inside render:
                        │
4. GENERATE      build_index.py                  → glossary/terms.yaml  (the locks, as data)
                        │                        → glossary/INDEX.md    (the human lookup)
                        │
5. ENFORCE       check_locks.py                  reads terms.yaml; a new lock is a live check
                        │                        the moment it is regenerated — no code change
                        │
6. SWEEP         fix the chapters the new lock   mechanical swaps applied immediately;
                 now contradicts                 rewrites proposed first, then applied
```

**Step 5 is the point.** Adding a lock requires no change to the checker. Write the entry, run `build_index.py`, and the rule is live across all 81 chapters.

**Step 6 is the discipline.** The policy is *fix on discovery, not in a deferred batch* — a settled lock that has not been swept is a lock that is quietly false.

---

## What is generated, and from what

| Product | Built by | From | Committed? |
|---|---|---|---|
| `glossary/INDEX.md` · `glossary/terms.yaml` | `build_index.py` | every entry's frontmatter, plus chapter lists recomputed from `source/chinese.md` | yes — CI fails if stale |
| `process/principles/INDEX.md` · `process/principles.yaml` | `build_principles.py` | every principle's frontmatter | yes — **CI fails if stale, and if an `evidence:` anchor does not resolve** |
| `data/taoteching.sqlite` | `build_db.py` | `chapters/`, `glossary/`, `sources/` | yes |
| `data/*.csv` | `export.py` | the sqlite | yes — **CI fails if stale**; a binary blob cannot be diffed or reviewed, the CSVs can |
| `data/explorer.html` | `build_explorer.py` | the sqlite | yes — self-contained, no network |
| `data/constellation-*.json` | `build_graph.py` | the sqlite | yes — **CI fails if stale** |
| `sources/commentaries/*/` | `import_commentary.py` | cached wikitext (gitignored) | yes — re-runnable to byte-identical output |
| `sources/shuowen/entries.md` | `import_shuowen.py` | cached wikitext | yes |
| `source/chinese.md` | *by hand, from the chapters' source tables* | — | yes |

**Every committed generated file must be reproducible, and now every one is checked.** `data/constellation-chars.json` had **never agreed with `data/characters.csv`** — both entered the repository in `2466b4d`, but the JSON was built from an older database than the CSV beside it, so it published glosses the CSV had already withdrawn and older wordings for ninety more. Nothing rebuilt it and nothing compared them; a person found it, seven months later, by reading a diff. CI now rebuilds the atlas and fails on `git diff --exit-code data/`.

**A diff gate is only as good as the generator's determinism.** `export.py` orders all eleven of its queries, which is why the CSVs never drifted. `build_graph.py` ordered one of eight, so its row order came from SQLite's query planner — stable for one machine and one planner version, which is exactly the stability that breaks when the gate runs on another. Every query there is now ordered and the co-occurrence map is emitted sorted: **the output is a function of the data alone.** Before adding a diff gate to any generator, make it deterministic first, or the gate produces noise instead of findings.

**The importers verify themselves.** `import_commentary.py` checks every lemma it vendors against our own base text and marks the divergent ones with `*`. That check is what makes the vendored files evidence rather than decoration — and when it was missing for 韓非 (*Hán Fēi*), the files asserted an agreement nobody had tested.

---

## Two tools, opposite contracts

Merging them would produce something too noisy to gate on and too quiet to search with.

**`check_locks.py` — the gate. Optimizes precision.** Exits non-zero, runs in CI and the pre-commit hook, and must never cry wolf. Twelve rules, each citing a written decision. A rule with no citation would be a tool author's opinion wearing a build's authority.

**`concordance.py` — the report. Optimizes recall.** Judges nothing, never fails, exists to put evidence in front of a person before a decision is made.

```bash
python3 tools/concordance.py 明                    # a character: every chapter, line, gloss, verse
python3 tools/concordance.py --english "clarity"   # the reverse direction — see below
python3 tools/concordance.py --pairs 玄 妙          # a term and its partner
python3 tools/concordance.py --formulas            # every repeated Chinese segment and frame
python3 tools/concordance.py --formulas 36         # ...touching ch 36, with that chapter's English
python3 tools/concordance.py --witnesses 25        # where the older manuscripts disagree
python3 tools/concordance.py --commentary 63       # the classical commentators on a chapter
```

**`--english` is the mode that catches what no rule can.** A lock is a two-way claim: every 強 (*qiáng* — strong) renders as *strong*, **and** every *strong* renders 強. The checker can only ever test the first direction, because its evidence gate keys off the character being present. The second direction found 固 (*gù* — firm) and 壯 (*zhuàng* — in its prime) both wearing 強's English inside chapters that contain 強 — invisible to every rule, by construction. **Run `--english` on every lock.**

---

## The gates

Three, in widening scope.

| | Scope | Severity | Blocks |
|---|---|---|---|
| **`.githooks/pre-commit`** | only the chapters being committed, skipping `status: untranslated` | errors only | the commit |
| **`.github/workflows/checks.yml`** | the whole book, every push and PR | errors fail; warnings and info are logged in a separate step where they cannot be mistaken for failures | the merge |
| **running the tools by hand** | whatever you ask for | all | nothing |

Install the hook with `git config core.hooksPath .githooks`. It is deliberately narrow: a half-drafted chapter must never have to argue with a tool.

CI additionally runs the tools' own tests (95 of them) and verifies the verse's hard line breaks. It also runs three **staleness gates**, all the same shape — regenerate, then `git diff --exit-code`:

| Gate | Proves |
|---|---|
| `glossary/INDEX.md` · `terms.yaml` | the generated locks match the entries they came from |
| `data/` — the atlas | every committed CSV and JSON matches the manuscript and glossary it was built from |
| `check_worklist.py` | `WORKLIST.md`'s pass rows, chapter lists and tally match its own table |

**`check_worklist.py` is the odd one and earns its place.** Four hand-kept lists in this repository went stale in three days — `CLAUDE.md`'s lock table, the `glossary-entry` skill's instruction to update it, `WORKLIST.md`'s duplicate "order of work" table, and its item tally — and a person found every one by reading. Nothing in `tools/` read `WORKLIST.md` at all. Its six rules only enforce what the file already says about itself, and a `Ch` cell that *points at rows* rather than listing chapters is never checked: **declining to keep a second copy is the behaviour the tool exists to encourage.**

**No dependency install step, deliberately.** Every tool is stdlib Python only, so a fresh clone can run the whole gate with nothing else present.

---

## The thirteen rules

| Rule | Protects | Severity |
|---|---|---|
| `forbidden-rendering` | every locked term's `forbidden:` list | **error** when the character is in that chapter; `info` otherwise |
| `sage-pronoun` | 聖人 (*shèng rén* — the sage) is never "he" | **error**, never gated — absolute |
| `devotional-capitalization` | lowercase everything but the Tao; capitals turn a word into a doctrine | **error** when the character is present; `info` otherwise |
| `mechanistic-register` | "source code", "operating system", "generate" — our own besetting temptation | **error** |
| `status-coherence` | `status: drafted` must mean there is a translation | **error** |
| `flexion-chapter` | a declared flexion must name chapters its character actually stands in, must name some, and must not also be forbidden | **error** |
| `source-drift` | a chapter's Chinese must match `source/chinese.md` | **error** |
| `repeated-formula` | verbatim Chinese in two chapters should read alike in English | **warn** — a reading for a person, not a verdict |
| `em-dash` | dashes in the verse strand subjects | `info` |
| `unlogged-variant` | a meaning-bearing manuscript fork must have a logged decision | **error** (unlogged) · **warn** (logged to a file with no such entry) |
| `unmarked-lemma` | a vendored lemma differing from our base text must carry its `*` | **error** (unmarked) · **warn** (marked but agreeing) |
| `stale-shaloms-call` | an override that outlived its expiry | **error** |
| `shaloms-call-unparsed` | a call the tool cannot see is a rule silently not suspended | **error** |
| *(plus)* `unused-waiver` | a `lock-ok` that matches nothing | **error** |

### The evidence gate

**No rule fires on English alone.** *Virtue* is an error only when 德 (*dé* — integrity) is in that chapter's own Chinese; otherwise it drops to `info` in a separate false-friends list. This is possible because every chapter file carries its own source table, and it is the difference between twenty flags and nine findings.

It also has a known blind spot, stated plainly here so nobody rediscovers it as a surprise: **the gate cannot express *right for that character, wrong for this one, in the same chapter*.** So *integrity* cannot be forbidden for 信 (*xìn* — trust), because chapters 21, 23, 38 and 49 hold both 信 and 德. Those distinctions live in the entry's prose and in the reader.

Two consequences for writing a `forbidden:` list: **a capital in the string means the capital is the violation** (`"the Way"` leaves *the way of nature* legal), and **a forbidden phrase can be defeated by an inserted word** (`"the Way"` misses *the great Way*) — so forbid the bare word where register matters more than phrasing.

---

## Escape hatches, and why each costs something

Unsuppressable rules get disabled wholesale; free suppression rots. So both hatches are recorded and both expire.

| | Scope | Cost |
|---|---|---|
| **`lock-ok` comment** in a chapter's `## Notes` | one finding | must carry a reason, and an **unused waiver is itself an error** — so the files self-clean |
| **`process/shaloms-call.md`** | a whole rule | requires a scope, an expiry and a reason; the checker prints a footer naming active calls, and an expired call fails the build |
| **`git commit --no-verify`** | one commit | leaves no record — which is the point: a second `--no-verify` on the same rule is the signal that a call is owed |

**Never delete a rule to silence it.**

---

## Trust tiers in the character atlas

`data/characters.csv` carries a gloss for every character in the book, and the `gloss_source` column says how much to trust it.

| tier | source | trust |
|---|---|---|
| `locked` | a settled rendering in `terms.yaml` | high — the edition's own decision |
| `covers` | a secondary character absorbed by an entry | high |
| `apparatus` | the `[pinyin]` notes in the source tables' Literal column, where a **strict majority** of occurrences agreed | working approximation |
| `apparatus-split` | the apparatus glossed it and no English won a majority — **the cell is deliberately blank** | none |
| `none` | nothing in the repository glosses it yet | — |

**A plurality is not a definition.** A character glossed six different ways in six places has a context, not a meaning — so the build refuses to pick one, and records the agreement ratio instead. The apparatus glosses also speak **pre-lock English** ("virtue", "the ten thousand things"), which is exactly what this edition rejects; they are a starting point and never override a lock.

---

## Provenance — the licensing architecture

The repository is **CC0, with no exceptions**, and a companion volume must be able to draw on it commercially. That constrains what may be vendored, and the constraint is architectural rather than incidental.

| Material | Call | Why |
|---|---|---|
| 王弼 · 河上公 · 韓非 commentaries | **vendor** | pre-1929 printings exist; public domain by age |
| The Laozi base text | **vendor** | ancient; provenanced to four named pre-1929 printings |
| 說文解字 (*Shuōwén Jiězì*) | **vendor** | c. 100 CE |
| **Mawangdui** (excavated 1973) · **Guodian** (1993) | **never vendor** | every transcription is modern, and reconstructing damaged graphs is living scholarship |
| Modern critical apparatus, annotations, translations | **never vendor** | in copyright |

**For the excavated witnesses, record the fact rather than the text.** *"Mawangdui A and B read 自今及古 (*zì jīn jí gǔ* — from now back to antiquity) where Wang Bi reads 自古及今 (*zì gǔ jí jīn* — from antiquity until now)"* is a fact about a text, and facts are not copyrightable. That is what `sources/variants.yaml` is: an apparatus of facts, never transcriptions. `sources/guodian-inventory.yaml` answers only *does the oldest witness carry this chapter at all* — it carries 31 of 81.

Read [`sources/PROVENANCE.md`](sources/PROVENANCE.md) before adding anything to `sources/`.

**A separate rule governs consultation, not vendoring:** sources are consulted for **meaning, never for phrasing**, and only pre-1931 public-domain translations may be consulted at all. There are no English translations in this repository.

---

## The documents, and who each is for

| File | Audience | Answers |
|---|---|---|
| [`README.md`](README.md) | anyone arriving | what is this, how do I read it |
| **`ARCHITECTURE.md`** | anyone working on the system | how do the parts fit together |
| [`CLAUDE.md`](CLAUDE.md) · [`AGENTS.md`](AGENTS.md) | AI collaborators, loaded every session | the rules, the locks, the workflow, the current state |
| [`process/method.md`](process/method.md) | translator and collaborators | how a chapter is actually translated |
| [`process/overlay-audit.md`](process/overlay-audit.md) | same | reading Laozi without the missionary lens |
| [`process/skills/`](process/skills/README.md) | AI collaborators | the method made executable |
| [`WORKLIST.md`](WORKLIST.md) | whoever picks up the work | what is still owed, prioritized |
| [`PLAN.md`](PLAN.md) | tool builders | what the harness is, what it taught, what is deliberately not built |
| [`DISCOVERIES.md`](DISCOVERIES.md) | readers and writers | the findings worth an essay |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | outside contributors | four ways in, easiest first |
| [`data/README.md`](data/README.md) | data users | the corpus as CSVs, and two cautions |
| [`sources/PROVENANCE.md`](sources/PROVENANCE.md) | anyone adding a source | what may live there, on what authority |
| [`notes/`](notes/) | the record | manuscript forks · our rendering decisions · reader-facing threads |

---

## Invariants

The things that must stay true. Most are enforced; the ones that are not are marked.

1. **`chapters/*.md` is the manuscript.** Nothing regenerates over it.
2. **Generated files are never hand-edited** — `INDEX.md`, `terms.yaml`, everything in `data/`, everything in `sources/commentaries/`.
3. **A locked term's frontmatter is the single source of truth for its rule.** *(enforced: CI fails if the generated files are stale)*
4. **Verse line breaks are two trailing spaces.** A single newline renders as a space and collapses a stanza into a paragraph. Never trim trailing whitespace in `.md` here; `.editorconfig` and the VS Code settings guard it. *(enforced)*
5. **Every meaning-bearing manuscript fork has a logged decision.** *(enforced)*
6. **Every vendored lemma that differs from our base text carries its `*`.** *(enforced)*
7. **Stdlib only.** A fresh clone runs the whole gate with no install step. *(not enforced — hold the line by hand)*
8. **Never write a Chinese character without an English rendering beside it** — in any file, any commit message, any conversation. *(not enforced; the most-broken rule in the repository, which is why it is a banner at the top of `CLAUDE.md`)*
9. **Sources are consulted for meaning, never for phrasing.** *(not enforceable)*

---

## Runbook

**This is the canonical list.** `README.md` and `CLAUDE.md` carry audience-shaped subsets and point here; when a tool or flag changes, change it here first.

```bash
# before drafting or revising a chapter
python3 tools/concordance.py --witnesses N      # do the oldest manuscripts disagree here?
python3 tools/concordance.py --commentary N     # what do the classical commentators say?

# while working on a term
python3 tools/concordance.py 強                  # every occurrence, with the verse
python3 tools/concordance.py --english "strong"  # the reverse direction — run this on every lock

# after adding or changing a glossary entry — required
python3 tools/build_index.py

# the gate
python3 tools/check_locks.py                    # whole book
python3 tools/check_locks.py --chapter 61       # one chapter
python3 tools/check_locks.py --rule em-dash     # one rule
python3 tools/check_locks.py --severity error   # what CI blocks on
python3 -m unittest discover -s tools/tests

# after editing any chapter's verse
python3 tools/fix-linebreaks.py                 # restore hard breaks (--check to verify only)

# after editing chapters, glossary or sources — rebuild the derived corpus
python3 tools/build_db.py && python3 tools/export.py
python3 tools/build_explorer.py && python3 tools/build_graph.py

# vendoring a source (network; output is byte-identical on re-run)
python3 tools/import_commentary.py --source hanfeizi --write
python3 tools/import_shuowen.py --fetch

# install the pre-commit gate
git config core.hooksPath .githooks
```
