# CLAUDE.md — operating context for this translation

*Read this first, every session.*

**Three files, three questions, no overlap in authority.** This one answers **what to do now**. [`process/method.md`](process/method.md) answers **why**: the reasoning behind every rule here, and the collaboration loop the two of us work in. [`process/skills/`](process/skills/README.md) answers **how**, step by step, and is invoked rather than remembered. Where this file compresses `method.md`, it must not contradict it. **If you find them disagreeing, that is a finding: fix both and say which was wrong.**

---

# ⛔ The gloss rule: before you write anything, gloss every Chinese character, every time

**Shalom does not read Chinese.** Never write a Chinese character, word, phrase, line, or chapter title — in conversation, in a document, in a commit message, in a table, anywhere — without an English rendering immediately beside it.

**The format, always:** 為 (*wéi* — "to do / to handle"). Character, then pinyin with tone marks and English in parentheses right after it. Never a bare 為.

**Names are the one exception: write them romanized, with no Chinese at all.** Commentators, authors, dictionaries and witnesses go by their romanized names: Wang Bi, Heshang Gong, Han Fei, Xu Shen, the Shuowen, Guodian, Mawangdui. Never "王弼's grammar," and not "王弼 (*Wáng Bì*)" either: a name in characters is one more thing the reader has to get past. *(Shalom's call, 2026-10-25. Older files still write names in characters; romanize them when you are editing that passage anyway.)*

**A verse quote is the other exception: its English stands beside its Chinese, and is its gloss.** When a glossary entry quotes the book's own verse as a block, it gives our English lines, then the Chinese lines, broken where the English breaks, then the chapter, with no pinyin and no literal gloss. Where an argument needs a literal reading, write it in the prose beside the quote, glossed as above. *(Shalom's call, 2026-10-26. The shape is in `process/skills/glossary-entry/SKILL.md` §3.)*

**This applies even when:**
- the term was glossed earlier in the same session, or in the same message
- it is a chapter title, a compound, or a quoted line
- it is "obviously" familiar — 道, 德, 天, 無為 all still get glossed
- you are quoting Wang Bi or Heshang Gong; **quoted commentary gets a full English rendering, not a paraphrase**
- you are asking a question and think the answer is obvious

A working approximation is fine and expected; the *deep* meaning is what the glossary entry is for. **Unglossed Chinese makes the work unreadable to the person whose work it is** — it silently converts a question into a thing he cannot answer.

---

## What this is

A from-the-source English translation of the Tao Te Ching by **Shalom Ormsby**, built chapter by chapter from the original Chinese, decades of study and meditation, and AI collaboration — **never** from other people's translations.

Two intentions, both sacred:

1. A **high-fidelity English Tao Te Ching in the public domain** — a gift to humanity. **This repository is entirely CC0, with no exceptions.** Everything here — translation, glossary, notes, method — is given away.
2. A **companion volume** of research and reflection, so the work can sustain its maker and his family. It lives in a **separate private repo (`shalomormsby/taocompanion`)** and is a *rewrite for readers*, drawing on this material without duplicating it. Nothing is withheld from this repo to make room for it.

**The ethos:** fidelity *and* poetry, together · the feminine at the center · universality over the text's incidental male-default · the end of all subordination, never the masculine put under the feminine · the naturalistic razor (strip theistic, moralistic, and mechanistic overlays) · **honesty over false closure: where the text is genuinely double, say so and leave the tension open.**

---

## How Shalom works

**He decides; the AI argues.** Bring him a **clear recommendation with the evidence and the cost**, not a menu — then do what he says. **The prime directive is to take a stand: help him see what he cannot see.** His pushback is usually right; treat a challenge as a finding, not a complaint.

- **Lead with the deepest thing**, never buried under small notes.
- **Name what a word *carries* that a candidate rendering *drops*.** Say what is lost, not just what is "off."
- **Take a position.** "I'd do X, because ___." Give alternatives, but commit to a lean and defend it.
- **Push back honestly.** Never flatter a choice into acceptance. **Own misses cleanly**: fix it and log it, with no collapse.
- **★ Intuition is last as an *arbiter* and often first as a *detector*.** When he says a word feels off, that is **a research assignment, not a preference to accommodate.** Go find what the discomfort is detecting.
- **★ One question at a time.** Bring the deepest one, with a recommendation; take his answer; then bring the next.
- **A commentator's gloss is not the text.** Offer what the line says; keep the commentary as evidence for it.
- **Where the Chinese repeats itself, repeat yourself.** A varied English renders a text that was never written. Run `concordance.py --formulas N` before drafting.
- **Verify a flagged line against the Chinese in its own chapter before changing it.**
- **Fix on discovery.** When a lock is settled, sweep the affected chapters now: apply mechanical term-swaps, and propose any line that needs a rewrite first.

**Every rule here, and every lock, is subject to `shaloms-call`.** When Shalom sets a rule aside, it is recorded in **`process/shaloms-call.md`**, and where a call is in effect, the call wins: say so once and proceed. **Argue hard *before* the call. Execute *after* it, without relitigating.** The AI never writes a call on its own initiative.

## Standing rules — non-negotiable

1. **No one is subordinated: the female is never put under, and the male is never the default.** The goal is the end of all subordination, not the masculine put under the feminine. Four parts, one rule:
   - **No rendering that could be used to justify the domination of the female.** Before a line about her goes into the verse, lift it out of its chapter and read it as a sentence someone could quote about women. That covers 牝 (*pìn* — the female), 雌 (*cí* — the hen), 母 (*mǔ* — mother), the dark female's gate, and the soft, the still and the low wherever they stand for her. If the line could serve as a rationale for keeping her under, it does not go in. Keep her the subject of what she does, never the object of someone's ruling on her place. **This does not soften her.** In this book her power *is* being underneath, soft and still, and the English keeps all three. What it refuses is English that turns them into her assigned place: *fitting*, *belongs*, *suits*, *passive*, *submissive*. **The rule binds the English, so it can outweigh a witness.** Where no English for the oldest reading passes this test, keep the reading that does, and give the other reading and its cost in the notes, so nothing the Chinese says is hidden. *(Shalom's call, 2026-10-26, at ch 61, where both Mawangdui silks read 故宜為下 (*gù yí wéi xià* — "therefore it is fitting that she be underneath") and the base was kept: `notes/manuscript.md`. The hen entry's refusal of *passive* is the same rule: `glossary/ci-雌.md`.)*
   - **Never refer to the sage as "he."** Use singular *they/their*, or recast. This is an impermissible gender bias, and it applies to every archetypal figure.
   - **Universality over the incidental male-default.** The text exalts the feminine as principle yet assumes the male as cultural default. Where they collide: **render toward the universal, note the seam.** Never erase the male-centrism silently.
   - **The male the text names stays named.** The rule refuses the male only where the text *assumes* him. It never reaches a male the text names on purpose: 父 (*fù* — father) is *father*, 牡 (*mǔ* — the male) is *the male*, 雄 (*xióng* — the rooster) is *the rooster*. Cooling any of them into *origin*, *root* or a sexless abstraction lays this rule over the text as an overlay, the same flinch that turns 母 (*mǔ* — mother) into *the Source*. An edition that kept the mother and unnamed the father would build its feminine center by subtraction. **The test mirrors the first part's:** no English that could be quoted to justify anyone's domination, and no English that erases either sex where the Chinese names it. *(Shalom's call, 2026-10-26, at chapters 21 and 42: `glossary/fu-父.md`.)*
2. **Consult sources for *meaning*, never for *phrasing*.** Pre-1931 public domain only. Waley (1934) and later are off-limits.
3. **Typography: lowercase everything but the Tao; a dash in the verse only where its subject is named on both sides.** English capitals confer status — they turn a word into a doctrine (*the sage*, *the mother*, *stillness*, never *the Sage*). 道 keeps its capital as a proper name; nothing else does. **The verse's dash is the spaced em-dash ( — ).** It may hold a topic up for the next words to name again — *this*, *which*, *its*, a question — as in *"The dark female's gate — / this is called the root of sky and earth."* It may never trail into an action whose doer goes unnamed: classical Chinese omits subjects freely and English cannot, so name the subject. Keep dashes rare. *(Shalom's call, 2026-10-25. Full reasoning in `notes/translation.md` → *Typography*.)*
4. **Every strategic decision gets logged**, in the one layer that owns it, and only what changes meaning. Notes stay thin so they stay usable; the **glossary** carries the weight.

   | File | Holds |
   |---|---|
   | `notes/manuscript.md` | forks **between witnesses**: chapter · line · fork · our call |
   | `notes/translation.md` | **our own** rendering decisions: chapter · phrase · choice · why |
   | `notes/reading.md` | reader-facing notes, and the cross-cutting **Threads** |
   | `process/principles/` | the transferable rules, which are not *about* a chapter, a term or a witness |

---

## Start here, every session

1. **`WORKLIST.md`** — everything the manuscript owes, prioritized, with the pass order. **Work by term, in passes, not chapter by chapter:** one decision touches a dozen chapters, and walking 1→81 re-opens the same argument twenty times.
2. **`process/shaloms-call.md`** — the rules Shalom has set aside.
3. **`process/principles/INDEX.md`** — the rules this project learned by making decisions, each with a **trigger** saying when it fires. The skills load the relevant ones at the step where they apply. The collaboration itself has no skill, so load its rules here:

   ```bash
   python3 tools/build_principles.py --applies process   # how to work with Shalom
   ```

   A 🔶 is provisional — one case so far, so weigh it rather than obey it.
4. **`DISCOVERIES.md`** — the findings worth an essay, newest first. **§1's central claim was superseded**, and the file carries a banner. **Do not trust a manuscript claim that is not in `sources/variants.yaml`.**

**One call is deferred by Shalom and must not be quietly settled inside a chapter review** — 正/奇 (*zhèng / qí* — straight / crooked), `WORKLIST.md` T4. Argue it with new evidence if you have it; otherwise leave it.

## Doing the work

**Invoke the skill; do not work from memory.** A chapter: `process/skills/chapter-review`. A glossary entry: `process/skills/glossary-entry`, which also holds how the locks and the frontmatter behave. A principle: `process/skills/principle-entry`.

**Tie-breaking order:** characters and radicals → oldest witnesses → classical commentaries → internal consistency and the locks → this edition's ethos → Shalom's poetic intuition, exercised *after* the deepest reading is on the table.

**Consult the sources — they are in the repo, and this is not optional.** The commentaries of Wang Bi, Heshang Gong and Han Fei are vendored in `sources/commentaries/`. Run `concordance.py --witnesses N` and `--commentary N` before drafting a chapter and before changing a settled line: from the files, not from memory or a search engine. A blank `--witnesses` result means nobody has checked that chapter yet, not that it has no forks. **Quote, gloss, and cite them; never copy their English.** **When they disagree, that is the finding**: log it, never average it. Record a new fork in `sources/variants.yaml` as a **fact, never a transcription** — read `sources/PROVENANCE.md` before adding anything to `sources/`.

**The locks live in [`glossary/INDEX.md`](glossary/INDEX.md)**, generated from each entry's frontmatter. Read it; never keep a second copy.

## The overlay watchlist

The English Tao Te Ching was largely built by missionaries, and the standard renderings are theology sedimented into words. Full audit: `process/overlay-audit.md`.

Flag on sight: **聖** ("holy" — it means *acute hearing*) · **神** ("God" — *numinous potency*) · **鬼** ("demons" — *ghosts, the dead*) · **罪** ("sin" — *crime*) · **義** ("righteousness" — *duty*) · **仁** ("benevolence" — *humaneness*) · **精/魄** ("soul" — *vital essence* / the *corporeal* soul) · **一** ("the One" — Neoplatonism) · **福** ("blessing" — *good fortune*) · **善** ("good" — often *skilled*) · **道法自然** (never "the Tao follows Nature" — that inverts the chapter).

Watch **register** too: KJV cadence, devotional capitals, abstraction drift — and our own besetting temptation, the **mechanistic** ("operating system", "source code", "generate"). **Two tests:** *the hymn test* — would this line sit in a sermon? *The pointing test* — could Laozi have pointed at it?

## What bites

- **`chapters/NNN.md` is the manuscript.** Edit it directly; nothing regenerates over it. `source/archive-google-doc-final-export-2026-08-09.md` is a frozen archive: never edit it and never generate from it. Git history is the translation's edit history, so commit meaningfully.
- **A chapter's frontmatter is not evidence that the chapter is sound.** `status: drafted` has sat on chapters with whole lines missing. A chapter's open debt is the open `WORKLIST.md` rows naming it. **Read the page.**
- **Never hand-edit a generated file**: `glossary/INDEX.md`, `glossary/terms.yaml`, `process/principles/INDEX.md`, `sources/commentaries/`, `sources/shuowen/`, `data/`. Rebuild them. `ARCHITECTURE.md` lists what generates what.
- **Every verse line ends in two trailing spaces**, a hard break. Run `fix-linebreaks.py` after editing verse, and never trim trailing whitespace from `.md` here.
- **The literal glosses in the source tables speak pre-lock English** ("virtue", "the ten thousand things"). A starting point, never a reading.
- **A correction has two halves: fix the line, and register the claim** in `process/retractions.yaml`, so `check_retractions.py` fails on every other copy.
- **A count in prose is a copy of a fact a tool knows.** Link to what prints it, or mark it (`<!-- count: name -->N`) so `check_counts.py` holds it.

## The harness

**Read `ARCHITECTURE.md` before changing anything in `tools/` or `data/`**: what holds authority, what is generated, and what each gate covers, with the full runbook. Load the rules the harness has learned:

```bash
python3 tools/build_principles.py --applies tooling   # before changing anything in tools/ or data/
```

**Two tools, opposite jobs.** `check_locks.py` optimizes precision: it gates the pre-commit hook and CI, and no rule fires on English alone. `concordance.py` optimizes recall: it judges nothing and never fails. **Run `--english` on every lock you settle**: a lock is a claim in both directions, and the checker can test only one. **When a check is wrong**, a `lock-ok` comment in the chapter's `## Notes` waives one finding, with a reason; a `shaloms-call` sets aside a whole rule. Never delete a rule to silence it.

The commands that come up while working on the text:

```bash
python3 tools/check_locks.py --chapter 61        # the gate, while drafting (no flag: whole book)
python3 tools/concordance.py 明                   # every chapter, line, gloss, verse
python3 tools/concordance.py --english "clarity"  # is a rendering backed by its character?
python3 tools/concordance.py --formulas 36        # the repeated segments and frames touching ch 36
python3 tools/concordance.py --witnesses 25       # where the older manuscripts disagree
python3 tools/concordance.py --commentary 63      # Wang Bi and Heshang Gong on a chapter

python3 tools/build_index.py                      # after any glossary edit
python3 tools/build_principles.py                 # after any principles edit
python3 tools/fix-linebreaks.py                   # after editing any verse
python3 tools/build_db.py && python3 tools/export.py && python3 tools/build_graph.py \
  && python3 tools/export_atlas.py                # after editing chapters or glossary: data/ is gated
python3 -m unittest discover -s tools/tests       # the tools' own tests; CI runs the rest
```

## Where everything else lives

| File | Holds |
|---|---|
| `ARCHITECTURE.md` | how the system fits together: every document and who it is for, what is generated, the gates, the runbook |
| `process/method.md` | the full working guide, and why |
| `process/form-audit.md` | the source's formal devices, and how the English carries each |
| `sources/PROVENANCE.md` | what may live in `sources/`, and on what authority |
| `WORKLIST-CLOSED.md` | every closed worklist row, word for word |
| `README.md` · `CONTRIBUTING.md` · `AGENTS.md` | the front door, the ways in for contributors, and this context for other tools |
