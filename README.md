# 道德經 · Tao Te Ching

**A new English translation from the classical Chinese, by Shalom Ormsby.**

**Everything here is public domain (CC0). It is a gift — take it, use it, build on it. No permission needed, no attribution required.**

*First draft complete — all 81 chapters. The editing pass is the work now; see [`WORKLIST.md`](WORKLIST.md).*

---

## What this is

A from-the-source translation of the Tao Te Ching, built chapter by chapter from the original Chinese, decades of study and meditation, and AI collaboration — **never from other people's translations.** No copyrighted version was consulted at any stage. Where older public-domain translations were read at all, it was to understand the *range of meanings* a line has carried, never to borrow words.

The work rests on three commitments:

- **Fidelity and poetry, together.** The literal meaning is honored; the English is living verse, not a gloss.
- **The feminine at the center.** The mother (母), the dark female (玄牝), the valley (谷), the yielding (柔) — Laozi's generative imagery kept warm and bodily, never abstracted into a sexless "Source."
- **The naturalistic razor.** The overlays come off — theistic ("Heaven"), moralistic ("virtue"), and mechanistic alike — and the text's own images are restored: water, root, valley, uncarved wood, the newborn, the mother.

Every consequential decision is documented. Nothing is asserted without evidence, and genuine ambiguities are left open rather than resolved by fiat.

## How it works

**This is a translation that behaves like a codebase.** Every settled decision about a Chinese word is written once — as an essay, with its evidence — and then enforced mechanically across all 81 chapters, so it cannot quietly come undone.

- **The glossary is both the ruling and the rule.** Each of the 35 entries argues a term from its oldest written form forward, quotes the classical commentators, and names what is set aside and why. Its frontmatter carries the settled English and the renderings that are forbidden; a build step turns that into machine-readable locks.
- **The checker is a gate, not advice.** It reads those locks and fails the build wherever the manuscript contradicts a decision already made. It never fires on English alone — *"virtue"* is an error only when 德 (*dé* — integrity) is in that chapter's own Chinese, and otherwise it is just an English word.
- **The evidence is in the repository, not in a bibliography.** Three classical commentaries in full — 王弼 (*Wáng Bì*, d. 249 CE, all 81), 河上公 (*Héshàng Gōng*, Han, all 81) and 韓非 (*Hán Fēi*, d. 233 BCE, the oldest there is) — the 說文解字 (*Shuōwén Jiězì*, c. 100 CE) analysis of 763 of the book's 798 characters, and an apparatus of 45 places where the excavated manuscripts disagree with the received text.
- **Where the manuscripts fork, the fork is recorded rather than resolved silently.** A meaning-bearing divergence with no logged decision fails the build.
- **Overrides are recorded and cost something.** A single finding can be waived with a reason; a whole rule can be set aside, but only with a scope and an expiry — and an unused waiver is itself an error, so the record cannot rot.

None of this decides anything. It only makes sure that what was decided once, on evidence, is still true on page 340 — and that a reader can check any of it without taking a word on trust.

[`ARCHITECTURE.md`](ARCHITECTURE.md) maps the whole system: what holds authority, what is generated, and what each gate covers.

## Read it

Start at [`chapters/001.md`](chapters/001.md). Each chapter carries the English verse, the Chinese with pinyin and a literal gloss, and any notes particular to it.

## Repository map

| Path | Contents |
|---|---|
| `chapters/001–081.md` | One file per chapter — translation, source text, notes |
| `source/chinese.md` | The base Chinese text (Wang Bi received recension) |
| [`glossary/INDEX.md`](glossary/INDEX.md) | **Start here for terms** — every locked rendering, generated from the entries |
| `glossary/` | Radical-level entries on the key terms — the heart of the work |
| `notes/manuscript.md` | Textual forks between the ancient witnesses, and which reading we follow |
| `notes/translation.md` | Our own rendering decisions, and the standing principles |
| `notes/reading.md` | Interpretive notes for readers; cross-cutting threads |
| `process/method.md` | The full working method |
| `process/overlay-audit.md` | Reading Laozi without the missionary lens |
| `process/skills/` | The method made executable, for AI collaborators |
| [`sources/`](sources/PROVENANCE.md) | The classical commentaries — Wang Bi and Heshang Gong (all 81 ch. each) — the variant apparatus, and per-file provenance |
| `tools/` | The harness — see below |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | **How the system fits together** — authorities, what is generated, the gates, the rules, provenance |
| `CLAUDE.md` · `AGENTS.md` | Operating context for AI collaborators and tools |
| [`DISCOVERIES.md`](DISCOVERIES.md) | **The findings worth writing about** — start here for what this research turned up: what later hands added, and what the book says once it comes off |
| `WORKLIST.md` | Known consistency debt across chapters |
| `PLAN.md` | The harness: what is built, what is deliberately not |

## The tools

Stdlib Python only — no dependencies, so a fresh clone can run them.

```bash
python3 tools/check_locks.py               # do the 81 chapters still obey the locks?
python3 tools/concordance.py 明             # every chapter, line, gloss and rendering
python3 tools/concordance.py --english "clarity"   # is a rendering backed by its character?
python3 tools/concordance.py --formulas    # Chinese segments repeated across chapters
python3 tools/concordance.py --witnesses 25 # where the older manuscripts disagree
python3 tools/concordance.py --commentary 63 # Wang Bi and Heshang Gong on a chapter
python3 tools/build_index.py               # regenerate glossary/INDEX.md and terms.yaml
python3 tools/fix-linebreaks.py            # restore the verse's hard line breaks
python3 -m unittest discover -s tools/tests
```

*The complete runbook is in [`ARCHITECTURE.md`](ARCHITECTURE.md).*

The two are opposite kinds of tool, deliberately. `check_locks.py` gates: it reads the locks out of the glossary entries' own frontmatter, reports where the manuscript contradicts a decision already made, and **never rewrites the verse**. `concordance.py` reports: it judges nothing and never fails. See [`ARCHITECTURE.md`](ARCHITECTURE.md) for why merging them would ruin both.

To have the locks checked before every commit:

```bash
git config core.hooksPath .githooks
```

The hook checks only the chapters you are committing, only at error severity, and skips chapters still marked `status: untranslated`. `git commit --no-verify` bypasses it once; `process/shaloms-call.md` is where a rule gets set aside for good.

## Method, briefly

The base text is the **Wang Bi** received recension. Where the older witnesses — **Guodian** (~300 BCE), **Mawangdui** (before 168 BCE), **Beida**, **Fu Yi** — differ in a way that changes meaning, the fork is logged and the choice explained.

Contested lines are read four ways before rendering: the **characters themselves** (Shuowen Jiezi, oracle-bone and bronze forms, radical decomposition), the **manuscript witnesses**, the **classical commentaries**, and the **internal evidence** of how a term behaves across all 81 chapters.

### The primary sources are in the repository

The commentaries are not consulted from memory or from a search engine. They are **in `sources/`**, with per-file provenance, and one command away:

```bash
python3 tools/concordance.py --commentary 21   # Wang Bi and Heshang Gong on a chapter
python3 tools/concordance.py --witnesses 21    # where the older manuscripts disagree
```

| Commentary | Date | Coverage | Edition |
|---|---|---|---|
| **王弼** Wang Bi | d. 249 CE | all 81 chapters | 欽定四庫全書 (Siku Quanshu), 1782 |
| **河上公** Heshang Gong | Han | **81 of 81** | Song woodblock, via *Sibu congkan* 0532 |
| **韓非** Han Feizi, 解老 / 喻老 | d. 233 BCE | 17 chapters he discusses | 韓非子, chs. 20–21 |

Every file names the printing it was transcribed from. Everything is public domain by age; the reasoning, and the rules for what may be added, are in [`sources/PROVENANCE.md`](sources/PROVENANCE.md). **The excavated manuscripts are deliberately *not* reproduced** — reconstructing the damaged graphs of the Mawangdui silks (1973) and Guodian slips (1993) is living scholarship, so the repository records the *fact* of each variant in [`sources/variants.yaml`](sources/variants.yaml) instead, which can be cited and checked.

The imports are reproducible (`tools/import_commentary.py`) and **they verify themselves**: each source interleaves or quotes the Laozi, so every quotation is matched against this edition's own base text. Wang Bi matches at 93%, Heshang Gong at 90%, Han Feizi at 100%. Lines that differ are reported as candidate variants, never quietly normalized.

**This is not decoration.** Having the sources to hand has already changed the translation. Wang Bi's own gloss settled what "this" refers to at the end of Chapter 21; the Siku compilers' collation note on the same line, 〔案狀各本俱作然〕, reopened a decision that had just been made; Heshang Gong's reading of Chapter 21 turned out to be a fourth witness against it; and Han Feizi supplied a reading of Chapter 63's hardest line that no modern discussion of it had suggested.

Terms are **locked**: once a rendering is settled it applies everywhere, and departures are logged. Where this translation departs from the English convention — *integrity* not "virtue," *sky and earth* not "heaven and earth," *the Tao* left untranslated — the reasoning is in [`glossary/`](glossary/) and [`process/overlay-audit.md`](process/overlay-audit.md).

## Status

**The first draft is complete — all 81 chapters, as of 2026-08-26.**

The editing pass is now the work. Early chapters predate several later decisions,
a number of renderings are still open, and the glossary covers 35 of the terms
that want entries. See [`WORKLIST.md`](WORKLIST.md) for what the manuscript still
owes.

A translation of this book is never finished. This one is readable now and will
keep moving.

## Take part

**You do not need to read Chinese to help, and the most useful contribution
doesn't require it.**

I have been inside this text long enough that I can no longer hear it cold. If a
line reads awkwardly, or sounds like a sermon, or simply thuds — say so. Open an
issue with the chapter and the line. No fix required, no reason required. That is
a complete contribution, and it is the one I cannot make myself.

If you want something more concrete:

- **389 of the book's 798 characters have no English gloss yet** — 87 of them
  appear three or more times. Each is small, self-contained, and useful.
- **32 chapters still carry em-dashes in the verse**, which the style forbids
  because a dash can hide a missing subject.
- **One decision is deferred across the whole book** — 民 (*mín* — the governed)
  against 人 (*rén* — a person). Chapter 57 currently renders 人 two ways, two
  lines apart.

[**CONTRIBUTING.md**](CONTRIBUTING.md) has the full map, including the part worth
saying plainly here: **I make the final call on every line.** A pull request is a
proposal to an editor, not a change to a commons — and disagreement is genuinely
wanted anyway. Several settled readings in this book exist because someone said
"that word feels wrong" and turned out to be right.

Longer conversation about *why this text still matters* happens at
[shalomormsby.substack.com](https://shalomormsby.substack.com/).

## License

[**CC0 1.0 Universal**](https://creativecommons.org/publicdomain/zero/1.0/) — public domain, no exceptions anywhere in this repository.

Reproduce it, adapt it, print it, perform it, translate it onward, train on it, or sell it. No permission needed, no attribution required, no strings. The Tao Te Ching belongs to everyone; a new English rendering of it should too.

*A companion volume — the story of how these decisions were made — is in preparation separately.*

---

*為而不爭* — act, and do not contend.
