# `data/` — the corpus as data

**Generated. Do not edit by hand.** Rebuild with:

```bash
python3 tools/build_db.py      # writes data/taoteching.sqlite (gitignored)
python3 tools/export.py        # writes the .csv files in this directory
```

The manuscript is `chapters/001–081.md`. Everything here is derived from it, the
way `glossary/INDEX.md` and `glossary/terms.yaml` are derived from the glossary
entries. Anything here that disagrees with a chapter file is a bug in the tools.

## Reading these files without reading Chinese

Every row that carries a Chinese character carries its pinyin and an English
rendering beside it. That is `CLAUDE.md` standing rule 0, and `tools/export.py
--check` fails the build if any row breaks it.

**The `gloss_source` column tells you how much to trust a gloss.**

| value | where it came from | trust |
|---|---|---|
| `locked` | a settled rendering in `glossary/terms.yaml` | high — this is the edition's own decision |
| `covers` | a secondary character absorbed by a glossary entry | high |
| `apparatus` | the `[pinyin]` notes in the Literal column of the source tables | **working approximation** |
| `none` | nothing in this repo glosses this character yet | — |

`apparatus` glosses are harvested from the source tables' literal column, which
`CLAUDE.md` warns speaks pre-lock English. They are a starting point, never a
ruling, and they never override a lock. The `gloss_agreement` column shows how
many of a character's glossed occurrences agreed on the winning English: `17/31`
means the character was glossed 31 times and the chosen English won 17 of them.
**A low ratio means the character is contextual, not that the gloss is wrong** —
之 (*zhī*) is a particle and will never have one English.

`none` is not hidden. Roughly 389 of the 798 distinct characters have no per-
character English in this repository yet. That gap is the glossary's worklist.

## The files

| file | one row per | good for |
|---|---|---|
| `characters.csv` | distinct character | frequency, coverage, what is glossed |
| `compounds.csv` | multi-character locked term | 萬物, 無為, 天地, 自然, 知足 |
| `lines.csv` | source line | Chinese, pinyin, literal gloss and our English side by side |
| `translation.csv` | verse line | the whole book in English, stanzas intact |
| `chapters.csv` | chapter | ratios, Guodian attestation, Heshang Gong's titles |
| `variants.csv` | witness reading at a fork | where the manuscripts disagree |
| `witnesses.csv` | witness | who they are, when, and on what rights basis |
| `locked-renderings.csv` | locked character occurrence | whether the lock is honored at that line |
| `commentary.csv` | commentary lemma | 王弼, 河上公, 韓非, with our English for the lemma |

## Two cautions that matter

**`alignment_method` is not decoration.** Our English verse lines and the Chinese
source lines are 1:1 in only 30 of 81 chapters (835 verse lines against 798
source lines). Where the counts match, `alignment_method` is `exact-count` and
the pairing is certain. Where they do not, it is `proportional` — a positional
guess at confidence 0.3, recorded so it can be improved, and **not evidence of
anything**. `rendering_present = NOT FOUND` on a `proportional` row usually means
the alignment is wrong, not the translation.

**`expected_rendering` is the lock's primary English, and `rendering_present`
also consults its flexions.** A flexion is a secondary English scoped to named
chapters — 保 (*bǎo*) reads *keep safe* generally and bare *keep* at chapter 9,
執 (*zhí*) reads *grasp* and *seize* at chapter 74 — declared as data in the
entry's frontmatter. The column counts a line honored if it carries the primary
render **or** a flexion licensed in that chapter. Before 2026-09-20 the flexions
were prose inside `render:` and this column printed `NOT FOUND` on 36 lines that
were correct, all of them on flexed locks. `expected_rendering` still shows only
the primary render, so a flexed line reads as `keep safe · yes`; the licence is
in `glossary/terms.yaml`.

**The excavated manuscripts are facts here, never text.** 郭店 (*Guōdiàn*),
馬王堆 (*Mǎwángduī*) and 北大 (*Běidà*) appear only in `variants.csv`, as recorded
disagreements with citations. `sources/PROVENANCE.md` explains why: reconstructing
damaged graphs is living scholarship, and this repository is CC0 with no
exceptions. `witnesses.csv` marks them `FACTS ONLY` in the rights column.
