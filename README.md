# The Open Tao Te Ching · 道德經

**A new English translation by Shalom Ormsby, refined in the open by its readers. Public domain (CC0): a gift to use and build on as you wish. No permission needed, no attribution required.**

*First draft complete — all 81 chapters. Announced on 17 October 2026 in [**Welcome to the Open Tao Te Ching**](https://shalomormsby.substack.com/p/welcome-to-the-open-tao-te-ching); the chapters are being shared one at a time, with notes. The editing pass is the work now; see [`WORKLIST.md`](WORKLIST.md).*

---

## Why another translation?

The Tao Te Ching has been translated more than 2,000 times, into 97 languages. I founded the Open Tao Te Ching because I believe three things:

1. **Open surpasses closed.** The wisdom of the Tao Te Ching should be openly and freely available to everyone, without copyright limitations, to read, quote, and use however they wish. I wouldn't hold this belief if Laozi were still alive, out of respect for authorship. But this text is more than 2,500 years old, and a vibrant English translation of it is far too important not to live in the public domain.
2. **Collaborative by nature.** The more hearts and minds that help clean away the cultural, political, religious, and philosophical overlays placed upon this text, the more useful and valuable it becomes. No one individual should be able to hoard this wealth. It is part of our shared human heritage.
3. **We can do better.** Current, copyrighted translations carry unexamined biases and overlays: 天 (*tiān* — sky) translated as "heaven," or 聖 (*shèng* — the sage) called "he" by default.

No one living person has all the answers. I certainly don't. But when we put our hearts and minds together, we can make something far greater than any of us could alone. So this project is more than a translation of a single text. It's a community, and I offer it not only the translation but every tool, platform, and resource I used to craft, refine, and house it.

## What this is

A new English translation of the Tao Te Ching, made directly from the classical Chinese and given freely to the public domain. Because the ever-present Tao cannot be made a way, or set in type, this translation stays open and fluid. It changes as our understanding deepens and as we remove centuries of cultural overlays.

Each chapter was worked out line by line from the Chinese, the classical commentaries, and the character etymologies, never from earlier English translations, and no phrasing is borrowed from them. The aim is an honest, living English free of the overlays that dynastic, Christian missionary, and New Age readings have laid over the text.

The work draws on decades of study and meditation, and on AI collaboration under tight constraints: the AI researched, cross-checked, and proposed alternatives; every final rendering is mine; and the method is public in [`process/method.md`](process/method.md). Its origin traces back to [Creative Powerup](https://creativepowerup.com/), a community I founded to support its members' creative empowerment through the heart-led use of technology. What I didn't anticipate was how much it would accelerate my own ability to design, build, and keep improving everything here.

The work rests on three commitments:

1. **Openness.** Every consequential decision is documented, viewable, and open to comment. Nothing is asserted without evidence, and genuine ambiguities are left open rather than resolved by fiat.
2. **Freedom from overlays.** The sage is not "he." 天 is "sky," not "Heaven." Theistic and moralistic overlays are set aside so the text's own images come forward: water, root, valley, uncarved wood, the newborn, the mother. The feminine is as central here as it is in Laozi's Chinese.
3. **Integrity and poetry, together.** The literal meaning is honored to its depth, and the English is living verse. Where the two pull apart, the tension is flagged openly, with context for anyone who wants to look further.

## One line, to show what that means

The first six characters of the book:

> 道可道，非常道
> *dào kě dào, fēi cháng dào*

You don't need to read Chinese to see that 道 (*dào* — Tao) appears three times. Literally: *"The Tao that can be Tao'ed is not the ever-present Tao."* If the paradox of this line doesn't stop you in your tracks, the translation has failed to do its job. The familiar English, *"The Tao that can be told is not the eternal Tao,"* sounds poetic, but it reduces the opening of the book to a secret you can't tell anyone. It trades a profound paradox for poetic license, and that is a trade this project refuses to make.

In Laozi's time 道 was an everyday word. It meant a road, and it was both a noun (a way you can walk) and a verb (walking the way). Its parts are 辶 (*chuò*), a foot moving along a road, and 首 (*shǒu*), a head, the part of you that faces where you're going. The line turns 道 back on itself, with 可 (*kě* — can be) as the hinge. So this translation uses *Tao* in both its familiar, untranslated form and its unfamiliar, translated one:

> **The Tao that can be made a way is not the ever-present Tao.**

The cost is that the opening line loses some of its music. I don't make that trade lightly, but I think a translation devoted to preserving paradox owes it. **If you can think of a more fitting solution, please say so.** The full reasoning is in [chapter 1's notes](chapters/001.md) and the [道 entry](glossary/dao-道.md).

## How it works

**This is a translation that behaves like a codebase.** Every settled decision about a Chinese word is written once, as an essay, with its evidence, and then enforced mechanically across all 81 chapters, so it cannot quietly come undone.

- **The glossary is both the ruling and the rule.** Each entry ([`glossary/INDEX.md`](glossary/INDEX.md) lists them all) argues a term from its oldest written form forward, quotes the classical commentators, and names what is set aside and why. Its frontmatter carries the settled English and the renderings that are forbidden; a build step turns that into machine-readable locks.
- **The checker is a gate, not advice.** It reads those locks and fails the build wherever the manuscript contradicts a decision already made. It never fires on English alone — *"virtue"* is an error only when 德 (*dé* — integrity) is in that chapter's own Chinese, and otherwise it is just an English word.
- **The evidence is in the repository, not in a bibliography.** Three classical commentaries in full — 王弼 (*Wáng Bì*, d. 249 CE, all 81), 河上公 (*Héshàng Gōng*, Han, all 81) and 韓非 (*Hán Fēi*, d. 233 BCE, the oldest there is) — the 說文解字 (*Shuōwén Jiězì*, c. 100 CE) analysis of <!-- count: shuowen -->764 of the book's <!-- count: characters -->798 characters, and an apparatus of <!-- count: variants -->96 places where the other witnesses — the excavated manuscripts and the received editions — disagree with the base text.
- **Where the manuscripts fork, the fork is recorded rather than resolved silently.** A meaning-bearing divergence with no logged decision fails the build.
- **Overrides are recorded and cost something.** A single finding can be waived with a reason; a whole rule can be set aside, but only with a scope and an expiry — and an unused waiver is itself an error, so the record cannot rot.

None of this decides anything. It only makes sure that what was decided once, on evidence, applies throughout the text, and that a reader can check any of it without taking a word on trust.

[`ARCHITECTURE.md`](ARCHITECTURE.md) maps the whole system: what holds authority, what is generated, and what each gate covers.

## Where to read it, and where to talk about it

You don't need any of this but the first. Everything else is here for whoever wants to dig deeper.

- **[The Open Tao Te Ching on Substack](https://shalomormsby.substack.com/s/open-tao-te-ching).** Each chapter with its notes: the challenges, the overlays removed, the tradeoffs made, and any surprises. To take part, just read and comment, or just read. It lives within *The Daily Mystic* as a Tao-focused section.
- **[The Library on OpenCosmos](https://opencosmos.ai/library/sources/taoism-tao-te-ching)**, the translation's native home. Click any English line to jump to its Chinese, then click any character to open its atlas entry.
- **[The Open Classical Chinese Character Atlas & Glossary](https://chinese-atlas.opencosmos.ai/).** The atlas maps where, and how often, each character is used, gives its English, and shows the parts it is built from. Essential characters link to their [glossary](https://chinese-atlas.opencosmos.ai/glossary/) entries: the character's etymology, the meaning of its parts, its history, and its significance in the text.
- **This repository**, the open collaboration engine. The Library and the atlas are built from it and continually improved here. You don't need to know GitHub to take part; see [Take part](#take-part).
- **[Cosmo](https://opencosmos.ai/dialog)**, the AI companion in OpenCosmos's left sidebar, which draws on a wide range of public-domain wisdom texts and is ready to support your exploration of the Tao Te Ching or any text in the Library.

**In this repository**, start at [`chapters/001.md`](chapters/001.md). Each chapter carries the English verse, the Chinese with pinyin and a literal gloss, and any notes particular to it.

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
| [`sources/`](sources/PROVENANCE.md) | The three classical commentaries (Wang Bi, Heshang Gong, Han Fei), 說文解字, the variant apparatus, the hand-kept gloss lists, and per-file provenance |
| [`data/`](data/README.md) | The corpus as CSVs, and `atlas-export.json`, the one file the Library and the atlas are built from — all generated |
| `tools/` | The harness — see below |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | **How the system fits together** — authorities, what is generated, the gates, the rules, provenance |
| `CLAUDE.md` · `AGENTS.md` | Operating context for AI collaborators and tools |
| [`DISCOVERIES.md`](DISCOVERIES.md) | **The findings worth writing about** — start here for what this research turned up: what later hands added, and what the book says once it comes off |
| `WORKLIST.md` | What the manuscript still owes |
| `WORKLIST-CLOSED.md` | What it owed and no longer does, row by row |
| [`CHANGELOG.md`](CHANGELOG.md) | What landed, and when |
| [`process/principles/`](process/principles/INDEX.md) | The transferable rules this work has learned by making decisions |
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

The imports are reproducible (`tools/import_commentary.py`) and **they verify themselves**: each source interleaves or quotes the Laozi, so every quotation is matched against this edition's own base text, and how many match for each source is in [`sources/PROVENANCE.md`](sources/PROVENANCE.md). Lines that differ are reported as candidate variants and marked, never quietly normalized.

**This is not decoration.** Having the sources to hand has already changed the translation. Wang Bi's own gloss settled what "this" refers to at the end of Chapter 21; the Siku compilers' collation note on the same line, 〔案狀各本俱作然〕, reopened a decision that had just been made; Heshang Gong's reading of Chapter 21 turned out to be a fourth witness against it; and Han Feizi supplied a reading of Chapter 63's hardest line that no modern discussion of it had suggested.

Terms are **locked**: once a rendering is settled it applies everywhere, and departures are logged. Where this translation departs from the English convention — *integrity* not "virtue," *sky and earth* not "heaven and earth," *the Tao* left untranslated — the reasoning is in [`glossary/`](glossary/) and [`process/overlay-audit.md`](process/overlay-audit.md).

## Status

**The first draft is complete — all 81 chapters, as of 2026-08-26.**

The editing pass is now the work. Early chapters predate several later decisions,
a number of renderings are still open, and not every term that wants a glossary
entry has one yet — [`glossary/INDEX.md`](glossary/INDEX.md) lists those that do.
See [`WORKLIST.md`](WORKLIST.md) for what the manuscript still owes.

A translation of this book is never finished. This one is readable now and will
keep moving.

## Take part

**You do not need to read Chinese to help, and the most useful contribution
doesn't require it.**

I have been inside this text long enough that I can no longer hear it cold. If a
line reads awkwardly, or sounds like a sermon, or simply thuds — say so. The
easiest place is a comment on [Substack](https://shalomormsby.substack.com/s/open-tao-te-ching),
where there is nothing new to learn; or open an issue here with the chapter and
the line. No fix required, no reason required. That is a complete contribution,
and it is the one I cannot make myself.

Every character on the atlas has a **Suggest an edit** button, and
[`CONTRIBUTING.md`](CONTRIBUTING.md) has two prompts to paste into an AI
assistant. Either will find where your suggestion belongs and help you send it,
asking you before anything is posted.

If you want something more concrete:

- **<!-- count: gloss:word -->459 characters carry only a short hand-written gloss** (`sources/word-glosses.yaml`),
  a reader's aid rather than a ruling. Checking one against its lines, or
  promoting it to a full glossary entry, is small, self-contained, and useful.
- **<!-- count: dash-chapters -->8 chapters still carry dashes in the verse**, which the style
  forbids because a dash can hide a missing subject
  (`python3 tools/check_locks.py --rule em-dash` lists them).
- **Two decisions are deferred across the whole book** — 正 / 奇 (*zhèng / qí* —
  straight / crooked), and the em-dashes in the verse. A third, 民 / 人 (*mín /
  rén* — the people / a person), was settled in October 2026.

[**CONTRIBUTING.md**](CONTRIBUTING.md) has the full map, including the part worth
saying plainly here: **I make the final call on every line.** A pull request is a
proposal to an editor, not a change to a commons — and disagreement is genuinely
wanted anyway. Several settled readings in this book exist because someone said
"that word feels wrong" and turned out to be right.

Let's discuss, debate, and continually improve this translation, together. The
longer conversation, about *why this text still matters*, happens at
[shalomormsby.substack.com/s/open-tao-te-ching](https://shalomormsby.substack.com/s/open-tao-te-ching).
Subscribing is free and always will be.

## License

[**CC0 1.0 Universal**](https://creativecommons.org/publicdomain/zero/1.0/) — public domain, no exceptions anywhere in this repository.

Reproduce it, adapt it, print it, perform it, translate it onward, train on it, or sell it. No permission needed, no attribution required, no strings. The Tao Te Ching belongs to everyone; a new English rendering of it should too.

*A companion volume — the story of how these decisions were made — is in preparation separately.*

---

*為而不爭* — act, and do not contend.
