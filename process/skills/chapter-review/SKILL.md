---
name: chapter-review
description: Draft or review one chapter of the Tao Te Ching translation, from the Chinese. Use when the user names a chapter number, says "draft ch N", "let's do 61", "review chapter 14", or asks to work on the next undrafted chapter. Enforces the per-chapter workflow, the locks, the overlay watchlist, and the notes logging — and takes a stand rather than presenting a menu.
---

# Reviewing a chapter

The method in `CLAUDE.md` is stable enough to execute rather than remember. This is it, in order. **Do not skip the reading to get to the rendering** — the whole value of the process is that the deepest reading is on the table *before* the poetry starts.

**Gloss every character, every time.** 為 (*wéi* — "to do / to handle"), never bare 為. Shalom does not read Chinese; unglossed Chinese makes the work unreadable to the person whose work it is. This applies to titles, compounds, and terms already discussed earlier in the session.

---

## 0. Before anything, check what is already decided

```bash
python3 tools/concordance.py --witnesses N                   # where the witnesses disagree
python3 tools/concordance.py --commentary N                  # 王弼 and 河上公 on this chapter
python3 tools/check_locks.py --chapter N --severity info     # what this chapter already violates
python3 tools/concordance.py --formulas N                    # the repeated frames, with this chapter's English
python3 tools/concordance.py --record 亂                      # what we have already written about a character
```

**`--formulas N` is not optional, and it is the newest of these.** It prints every Chinese segment and frame this chapter repeats — **within itself as well as across the book** — with the chapter's English underneath, so a flattened parallelism is visible in one screen. **Where the Chinese repeats, the English must repeat too.** Chapter 11 says one identical sentence over a cart, a pot and a room, and our English varied all three; the fault is invisible line by line, and was invisible to every tool until 2026-09-05. `DISCOVERIES.md` §6.

**Run `--witnesses` first, before reading the base text closely.** Ch 21 was drafted over a chronology both Mawangdui silks reverse; Ch 25 was drafted with a king the oldest witnesses do not have. Neither was carelessness — nobody had looked. If the command reports nothing, read that as *nobody has checked this chapter yet*, not as *there are no forks*: `sources/variants.yaml` is built by hand, chapter by chapter.

```bash
python3 tools/build_principles.py --applies drafting   # the rules this work fires
```

**Run it, and read the *fires when* line on each.** `process/principles/` holds the rules this project learned by making particular decisions — they govern chapters nobody has read yet, which is exactly why they cannot be left where they were discovered. A 🔶 is **provisional**: one case so far, so weigh it rather than obey it. `process/principles/README.md` has the standard.

**`--record` is the one that is easy to skip, and it is the cheapest.** Every other command here queries a source; this one queries **us**. A finding gets written where it is found — in the notes of the chapter that produced it — and the next person who needs it is working on a different chapter. Ch 3's notes held 說文's 亂，治也 and the tangled-silk graph from August; the 亂 entry rebuilt that argument from the dictionary in September. Run it on each contested character before you open anything else. `process/principles/search-the-record-first.md`.

Read `process/shaloms-call.md`. If a call is in effect that touches this chapter, **the call wins** — say so once and proceed. Do not re-argue it.

---

## 1. Read the Chinese cold

Read the `## Source` block in `chapters/NNN.md` before reading anyone's opinion, including the literal gloss's. The glosses in that table are **pre-lock English** — they say "virtue", "ten thousand things", "eternal", "mysterious" — which are precisely the words this edition rejects. They are a starting point, not a reading.

Decompose the contested characters to radicals. This is where the real findings come from: 萬 (*wàn*) is a **scorpion** borrowed for its sound, so "ten thousand" is a phonetic accident; 為 (*wéi*) is a **hand on an elephant**, so it is *handling*, not neutral doing; 自 (*zì*) is a **nose**, the thing you point at to mean "me".

---

## 2. Check the witnesses, then the commentaries

Wang Bi is the base text. Check Mawangdui, Guodian, Fu Yi, and Beida for **meaning-bearing** forks only — orthographic variants are not findings. Then the commentaries — **`concordance.py --commentary N`, from `sources/`, not from memory.** 王弼 (d. 249), 河上公 (Han, all 81 chapters), and 韓非 (d. 233 BCE, the oldest, in `sources/commentaries/hanfeizi/` for the 17 chapters he discusses).

**Record what you find in `sources/variants.yaml`** — as *facts*, never as transcriptions, and never by copying anyone's reconstruction of a damaged graph. `sources/PROVENANCE.md` explains why, and it is a licensing rule, not a preference. Once recorded, `check_locks.py`'s `unlogged-variant` rule will fail the build if a meaning-bearing fork has no logged decision, so the apparatus and `notes/manuscript.md` cannot drift apart.

**Consult sources for *meaning*, never for *phrasing*.** Pre-1931 public domain only. Waley (1934) and everything later is off-limits. If a phrase arrives in your head fully formed and elegant, be suspicious of where it came from.

---

## 3. Run the term evidence

For every locked term in the chapter, and every term that looks like it wants an entry:

```bash
python3 tools/concordance.py 明                    # every chapter, line, and rendering
python3 tools/concordance.py --english "clarity"   # is this rendering backed by its character?
python3 tools/concordance.py --pairs 正 奇          # threaded pairs
```

The `--english` direction is the one that catches what the Chinese cannot: a rendering applied in a chapter where the character licensing it is **absent**. A lock is a two-way claim.

---

## 4. Apply the watchlist

`CLAUDE.md`'s overlay watchlist, then the two tests:

- **The hymn test.** Would this line sit in a sermon? Then go back and check the character.
- **The pointing test.** Could Laozi have pointed at it? "Sky" passes. "Heaven" does not. "Source code" does not.

Flag on sight: 聖 (*shèng* — *acute hearing*, not "holy") · 神 (*shén* — *numinous potency*, not "God") · 鬼 (*guǐ* — *ghosts/the dead*, not "demons") · 罪 (*zuì* — *crime*, not "sin") · 義 (*yì* — *duty*, not "righteousness") · 仁 (*rén* — *humaneness*, not "benevolence") · 一 (*yī* — "one", not "the One").

And our own besetting temptation, the **mechanistic**: "operating system", "source code", "generate", "system", "function". `check_locks.py` catches these, but catch them first.

---

## 5. Take a stand

**This is the step that earns the collaboration.** Not deferential review — active advocacy for the deepest, truest reading.

- **Lead with the deepest thing.** The most important claim or danger goes first, never buried under small notes.
- **Name what a word *carries* that a candidate rendering *drops*.** Say what is lost, not just what is "off".
- **Commit to a lean.** "I'd do X, because ___." Give alternatives, then defend a choice. Shalom wants a recommendation with the evidence and the cost, not a menu.
- **Push back honestly.** Respectful disagreement is worth more than agreement. Never flatter a choice into acceptance.
- **Surface the deeper claim even when not asked.**

### Before you offer a line, read it back

Six checks on the **finished English**. Each is a principle, and this is the step where it fires — they cannot be run earlier, because they are about the line you have made, not the line you are reading.

| Check | Principle |
|---|---|
| **Point every English word at a character.** A word that renders nothing is either scaffolding English grammar requires — say so in the note — or it comes out | `renders-no-character` · `supplied-verb-is-scaffolding` |
| **Read the English alone, without the Chinese beside it, and say what it claims.** Then check that claim against the source | `defensible-but-a-different-claim` |
| **Ask what the line implies about the people in it.** Would this book say the same of the sage? | `collocation-carries-a-verdict` · `no-verdict-the-chinese-lacks` |
| **Ask what every pronoun points at.** If two things could be *it*, the English has chosen; choose deliberately or recast | `name-the-referent` |
| **Where the commentators split, has the English chosen between them?** If so, try for a line that holds both, or say in the note what choosing cost | `divergence-stays-open` |
| **Where you used two English words for one Chinese modifier, name the single word you avoided** | `one-modifier-one-modifier` |

**A line you are especially pleased with is the first place to look**, not the last. Pleasure is the reliable sign that the English came from English rather than from the character — run `--english` on its key word.

Then **offer clay**: a full rendering he can accept, reject, or reshape. His poetic intuition is the final arbiter — exercised *after* the deepest reading is on the table, not instead of it.

---

## 6. Honor the typography

- **Lowercase everything but the Tao.** *the sage*, *the mother*, *the uncarved*, *stillness*. English capitals confer status; they turn a word into a doctrine. 道 keeps its capital as a proper name. Nothing else does.
- **The sage is never "he."** Singular *they/their*, or recast. Applies to every archetypal figure.
- **Universality over the incidental male-default.** Where the text's exaltation of the feminine collides with its assumption of the male as cultural default: render toward the universal, **note the seam**. Never erase the male-centrism silently.
- **No em-dashes in the verse.** They read as a machine tell, and they **strand subjects** — classical Chinese omits them freely, English cannot, and a dash disguises the gap instead of closing it. Name the subject and end the sentence.
- **Let the layout track the original's rhythm.** The marks are ours; the music is the source's. Stay consistent within any parallel series.
- **Two trailing spaces on every verse line.** Markdown collapses a single newline into a space.

---

## 7. Log it, then verify

Log **only what changes meaning**. Notes stay thin so they stay usable; the glossary carries the weight.

```bash
python3 tools/build_principles.py --applies notes   # the rules for writing the record
```

| File | What goes there |
|---|---|
| `notes/manuscript.md` | textual forks **between witnesses** |
| `notes/translation.md` | **our own** rendering decisions and standing principles |
| `notes/reading.md` | reader-facing interpretive notes; cross-cutting **Threads** |

Then, every time:

```bash
python3 tools/check_locks.py --chapter N        # must be clean, or waived with a reason
python3 tools/fix-linebreaks.py                # verse hard breaks
python3 tools/build_index.py                   # if a glossary entry changed
```

Set the chapter's frontmatter: `status: drafted`, and `retrofit: []` only if it truly is.

**Retrofit policy — fix on discovery, not in a deferred batch.** If this chapter settles a term, sweep the affected chapters *now*. Mechanical term-swaps: apply them. Lines needing a rewrite: propose to Shalom first, then apply. Log anything left open in `WORKLIST.md`.

**Always verify a flagged line against the Chinese in its own chapter before changing it.** Roughly a third of the first automated sweep's flags were false positives: 常 (*cháng* — constant) vs 長 (*cháng* — long); "Block the openings" (塞) vs "uncarved block" (樸). The checker's evidence gate handles most of this, but it cannot handle all of it.

---

## When the chapter resists

**Honesty over false closure.** Where the text is genuinely double, say so and leave the tension open. A strain case named in the notes is worth more than a smooth line that decides something the Chinese does not decide. `notes/translation.md` already carries several: 天門 (10), 天將救之 (67), 天子 (62).

## Tie-breaking order

characters/radicals → oldest witnesses → classical commentaries → internal consistency and the locks → this edition's ethos → Shalom's poetic intuition.
