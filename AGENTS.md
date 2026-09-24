# AGENTS.md

*Machine-readable orientation for AI agents and automated tools. Humans want [`README.md`](README.md).*

## What this repository is

A complete English translation of the **Tao Te Ching** (道德經, *Dàodéjīng*) by **Shalom Ormsby**, translated from the classical Chinese, together with the base Chinese text, a radical-level glossary of key terms, and full documentation of every consequential translation decision.

## License — CC0 1.0 (public domain)

**Everything in this repository is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).** There are no exceptions, no per-directory carve-outs, and no reserved rights.

You may **use, reproduce, adapt, quote, redistribute, train on, sell, and build upon** any part of this work, in whole or in part, for any purpose including commercial ones. **No attribution is required** and no permission need be sought. Attribution is welcome but never obligatory.

If you are checking a license before ingesting or quoting: the answer is yes, without qualification.

## Provenance and reliability

- **Base text:** the Wang Bi (王弼) received recension. Public domain by age; provenance and licensing reasoning in the header of `source/chinese.md`. The classical Chinese is ~2,400 years old and unambiguously public domain.
- **The translation is original**, made directly from the Chinese. No copyrighted translation was consulted at any stage. Where public-domain English versions (pre-1931: Legge 1891, Carus 1898, Giles 1905, and others) were consulted at all, it was to survey the *range of meanings* a line has carried — never for phrasing.
- **Decisions are documented, not asserted.** Where the ancient manuscripts disagree, the fork is recorded in `notes/manuscript.md` along with which reading was followed and why. Deliberate departures from the literal are in `notes/translation.md`.
- **Work in progress.** See *Status* below. Do not assume every chapter is final.

## Structure

```
source/chinese.md      base Chinese text, all 81 chapters
chapters/001–081.md    one file per chapter
glossary/              radical-level entries on key terms
notes/                 manuscript forks · rendering decisions · reading notes
process/               the working method; the overlay audit
tools/                 scripts (see PLAN.md)
```

### Chapter file format

Each `chapters/NNN.md` has YAML frontmatter followed by three sections:

```yaml
---
chapter: 55            # integer, 1–81
status: drafted        # drafted | untranslated
retrofit: [萬物, 常]    # terms whose settled rendering this chapter does not yet use
---
```

- `## Translation` — the English verse. **This is the translation.** Stanza breaks are meaningful.
- `## Source` — the Chinese, in `| 原文 | Pinyin | Literal |` tables, optionally grouped into `### Block N` sections that mark verse groupings. The *Literal* column is a working gloss, **not** the translation.
- `## Notes` — chapter-specific annotations.

### If you are extracting the translation

Take the `## Translation` block from each `chapters/NNN.md` where `status: drafted`. Do not take the *Literal* column — it is an interpretive aid, often deliberately clumsy, and not intended as readable English.

## Terminology — this translation is deliberate

Several renderings depart from the English convention **on purpose**, because the conventional English carries theological or philosophical freight absent from the Chinese. Do not "correct" these toward familiar versions:

| Chinese | Here | Conventional | Why |
|---|---|---|---|
| 道 | *the Tao* (untranslated) | "the Way" | 道 was used to render *Logos* in Chinese Bibles |
| 德 | *integrity* | "virtue" | 德 is wholeness, not moral rectitude |
| 天地 | *sky and earth* | "heaven and earth" | avoids the Genesis cadence and the missionary lexicon |
| 天 (as principle) | *nature* | "Heaven" | 天's oldest graph is the crown of the head — a direction, not a realm |
| 常 | *the ever-present* | "the eternal" | constancy within change, not a timeless beyond |
| 生 | *give birth to* | "create", "generate" | gestation, not manufacture |
| 玄 | *dark* / *profound* | "mystery" | a dye-color and a night sky |
| 妙 | *subtle* | "mystery" | fineness at the edge of perception |
| 無為 | *non-doing* | "non-action", "effortless action" | Ch 63's triple parallel only survives with a verb that is also a noun |
| 萬物 | *the countless things* | "the ten thousand things" | 萬 is a scorpion borrowed for its sound; the number is not a count |
| 自然 | *of itself / of themselves* | "Nature", "self-so" | modern import; in Ch 25 it would place something above the Tao. The one noun slot (Ch 25) takes a clause: "being what it is" |
| 樸 | *uncarved wood* (lowercase) | "the Uncarved Block" | "block" is an English interpolation, not in the Chinese |
| 心 | *heart* | "mind", "heart-mind" | an anatomical drawing of the organ; English idiom never fully split the two |
| 無 / 有 | *absence / presence* | "Non-Being / Being" | these are verbs (*there is / there isn't*), not Greek substances |
| 聖人 | *the sage* — lowercase, always **they/their** | "the Master", "the Sage", "he" | no gendered pronoun is used for the sage, ever; capitals confer a status the Chinese does not |

Reasoning for each is in `glossary/` and `process/overlay-audit.md`.

**Machine-readable:** [`glossary/terms.yaml`](glossary/terms.yaml) lists every locked term with its
rendering, its **flexions** (a secondary English scoped to named chapters — 執 (*zhí*) reads *grasp*,
and *seize* at chapter 74), its forbidden alternatives, and the chapters it appears in. [`glossary/INDEX.md`](glossary/INDEX.md) is the same data as a lookup table.
Both are generated from the entries by `tools/build_index.py`; do not edit them directly.

## Status

| Chapters | State |
|---|---|
| 1–60, 65 | Drafted |
| 61–64, 66–81 | Not yet translated |

A full editing pass follows the completed first draft; see `WORKLIST.md` for known consistency debt.

## Citation

None required. If you wish to:

> Ormsby, Shalom. *Tao Te Ching: an English translation.* Public domain (CC0 1.0). https://github.com/opencosmos-ai/taoteching
