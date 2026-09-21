---
name: glossary-entry
description: Write or revise a glossary entry for a term in the Tao Te Ching translation. Use when adding a new term to glossary/, locking a rendering, revising an existing entry, or when the user names a Chinese character and asks to work on it. Enforces the entry standard, the frontmatter format, the evidence rules, and regenerates the index.
---

# Writing a glossary entry

The glossary is the heart of this project. Entries are **published research**, not working notes — they ship in a public-domain repository and are the source material for the companion volume. Write them for a reader who was not in the room.

Work through these phases in order. Do not skip the research.

---

## 1. Gather evidence before writing a word

**Never write from memory.** Every claim gets checked against the corpus in this repo.

```bash
python3 tools/build_principles.py --applies glossary   # the rules this work fires
```

**Run it, and read the *fires when* line on each.** `process/principles/` holds the rules this project learned by making particular decisions — they govern chapters nobody has read yet, which is exactly why they cannot be left where they were discovered. A 🔶 is **provisional**: one case so far, so weigh it rather than obey it. `process/principles/README.md` has the standard.


```bash
python3 tools/concordance.py 明                     # every chapter, line, gloss, and verse
python3 tools/concordance.py --english "clarity"    # is this rendering backed by the character?
python3 tools/concordance.py --pairs 玄 妙           # the term and its partner
python3 tools/concordance.py --formulas             # segments repeated across chapters
```

That covers the first, second, and last of the four below; the character's history still needs you.

- **Every occurrence**, with chapter and full line. Frequency is a real signal.
- **The current English** for each, and — via `--english` — whether any chapter uses the rendering *without* the character to license it. A lock is a two-way claim, and only that direction catches the second half.
- **The character's oldest form.** Oracle-bone and bronze graphs, and the *Shuowen Jiezi* gloss. Web search is appropriate here; cite sources in chat.
- **Counter-terms and companions.** Most keywords have a partner — 器 for 樸, 腹 for 心, 光 for 明, 利/用 for 無/有. The pairing is often the argument.
- **Repeated formulas.** If a line appears verbatim in two chapters, both must read identically.

**Read the glosses in the source tables as a starting point, not a reading.** They speak pre-lock English — "virtue", "the ten thousand things", "eternal", "mysterious" — which are precisely the words this edition rejects.

**Verify, never inherit.** `process/legacy-tao-source-code.md` holds a superseded glossary with at least one demonstrable error (天 as "The Cosmos") and a discarded computational framework. Harvest observations from it; re-check every claim.

**Watch for false friends.** Roughly a third of automated flags are wrong. 常 (*cháng*, constant) vs 長 (*cháng*, long). English "one" the pronoun vs 一. "The way of nature" is correct for 天之道, not a 道 breach. **Always confirm against the Chinese in that chapter before changing a line.**

---

## 2. The entry standard — the shape every entry takes

1. **Open with the character, not with a critique.** An entry is not a design brief. Name the term, say how it sounds, give its frequency, state the ruling — then the graph, and what the character means. A reader wants to know what the word *is* before they hear what anyone got wrong, and an entry that opens by cataloguing our own past renderings is doing the thing §3 forbids. Follow the house shape:

   ```markdown
   ## 眾 (Zhòng) — The Crowd

   *Say "jong," falling. Nine appearances across six chapters.*

   **Locked: 眾 → "the crowd" (of people) / "the many" (of things).** *(Not "the masses.")*
   ```

   Then the body, in `###` subsections. Use **Recommended:** in place of **Locked:** where `status: open`.
2. **Read the character as a picture changing over time.** Oracle bone → seal → modern. This is where entries earn their keep: 為 is a hand on an elephant, 無 was a dancer, 自 is a nose, 明 is moonlight through a window, 萬 is a scorpion.
3. **Let cross-textual evidence argue.** Quote the Chinese with a gloss, cite chapters, let the pattern make the case.
4. **Name what is set aside, and why.** Each rejected rendering gets its own reason. Often the most useful section in the entry, and **this is where the critique lives** — what the *conventional* English costs, never what this manuscript used to say (§3).
5. **State the working register.** How the term flexes by grammar, with examples. Include a table of protected verbs where the noun cannot carry the whole sense.
6. **Leave the real tension open.** Every good entry ends somewhere honest and unresolved. If nothing is unresolved, look harder.

**Two tests on every sentence:**

- **The hymn test** — would this sit comfortably in a sermon? Then it is probably an imported overlay.
- **The pointing test** — could Laozi have pointed at it? His vocabulary is water, valley, wood, infant, dust.

---

## 3. What must never appear in an entry

The rule most often broken. An entry is not a work log.

**Purge on sight:**

- **Draft-state commentary** — *"the draft currently renders this three ways," "at present the manuscript has…"* Stale the moment a sweep runs, and meaningless to a reader.
- **Work-tracking** — *"Sweep required: chapters 3, 8, 12," "Swept 2026-08-10."* That belongs in `WORKLIST.md`.
- **Harvest provenance** — *"the early glossary," "the old entry," "rejected with the framework it came from."* Reject the *rendering* on its merits; the reader does not need its biography.
- **Editorial asides** — *"pending confirmation," "our only quarrel is," "build the others toward this," "worth logging as an exception."*
- **Instructions to the project** — *"a Reading Note should connect…"* Put the note in `notes/reading.md`; do not write about writing it.

**Also:**

- **Lowercase everything but the Tao** — *the sage*, *the mother*, *the uncarved*, *stillness*. English capitals confer status the Chinese does not.
- **No em-dashes in quoted verse.** They strand subjects. Prose in the entry may use them.
- **Gloss every Chinese character in English, every time** — 為 (*wéi* — "to do"). Shalom does not read Chinese.
- **Never "he" for the sage.** Singular *they/their*, or recast.

---

## 4. Frontmatter — required, and it drives everything

Every entry opens with this block. It is the single source of truth for the locks.

```yaml
---
term: "心"
pinyin: "xīn"
render: "heart"
forbidden: ["mind", "heart-mind", "the wise core", "consciousness"]
chapters: [3, 8, 12, 20, 49, 55]
status: locked
pairing: false
covers:
  - { char: "腹", render: "belly" }
---
```

| Field | Meaning |
|---|---|
| `term` | the character(s); pairings use `"我 & 吾"` |
| `pinyin` | with tone marks; pairings use `"wǒ / wú"` |
| `render` | the primary locked English. Slashes for senses that vary by grammar |
| `flexions` | a secondary English **scoped to named chapters** — data, not prose. See below |
| `forbidden` | rejected renderings — feeds the future lock checker |
| `chapters` | recomputed automatically on build; put your best list in |
| `status` | `locked` or `open` |
| `pairing` | `true` if the meaning lives between two characters |
| `covers` | secondary characters treated inside this entry |

**Flexions go in `flexions:`, never in a sentence inside `render:`.**

```yaml
render: "keep safe"
flexions:
  - { english: "keep", chapters: [9], why: "the object is not cherished" }
```

The **where** is a chapter list a tool can check; the **why** is a sentence for the reader. `check_locks.py`'s `flexion-chapter` rule verifies the licence points at a chapter the character stands in, and `concordance.py --english "keep"` then reports it as a declared flexion with its scope instead of looking like a breach.

**Use it only where the condition is a chapter.** A sense that varies by grammar — adjective against verb, or a verb that takes an object — stays prose in `render:`, because there is nothing for a tool to check and inventing a chapter list would be making a decision rather than recording one.

**Filename:** `pinyin-字.md`, no tone marks — `xin-心.md`, `wu-you-無有.md`.

---

## 5. Finish — every time, no exceptions

```bash
python3 tools/build_index.py
```

Regenerates `glossary/INDEX.md` and `glossary/terms.yaml`. **Never edit those by hand.**

**If you changed `render:`, `flexions:` or `forbidden:`, grep the repo for the old English beside the term and reconcile every hit.** A lock's English is authored here and *restated in prose* across `notes/`, `WORKLIST.md` and the chapter notes, and **no check compares them** — so a change here silently leaves stale copies behind. This is measured: the 保 flexion of 2026-09-20 updated three places and left three saying the old thing, including a glossary entry asserting an English its own chapter had just stopped using.

The frontmatter's `forbidden:` list becomes a live check the moment you run this — `tools/check_locks.py` reads `terms.yaml` and needs no code change to enforce a new lock. Two things follow, so write the list with care:

- **Capitalization in a forbidden string is meaningful.** Writing `"the Way"` means the capital *is* the violation, and *"the way of nature"* stays legal. Writing `"eternal"` lowercase means the word in any case, which is what catches "eternally". Choose deliberately.
- **A forbidden *phrase* can be defeated by an inserted word.** `"the Way"` does not match "the great Way". Where the register matters more than the exact phrase, forbid the bare word.

Then confirm the lock holds, and sweep:

```bash
python3 tools/check_locks.py --severity info
```

1. **Sweep the chapters** if a rendering changed. Fix on discovery; do not defer. Mechanical term-swaps: apply them. Lines needing a rewrite: propose to Shalom first.
2. **Do not copy the lock anywhere.** `glossary/INDEX.md` and `terms.yaml` are generated from the frontmatter you just wrote, and they are the only lists. *(A hand-kept table in `CLAUDE.md` was deleted on 2026-08-28 after going stale twice in a week; see `CLAUDE.md` → The locks.)*
3. **Log the reasoning** in `notes/translation.md` if the choice departs from convention.
4. **Update `glossary/TRIAGE.md`** — strike the term through, record what was found.
5. **Regenerate chapter frontmatter** so `retrofit:` reflects reality.
6. **Report**: the finding, the evidence, the choice, and what was left open.

---

## 6. When the term is not yet decided

Write the entry with a **recommendation**, not a lock. Set `status: open`, present the candidates with their costs, take a clear position, and ask. Do not sweep until confirmed.

A useful pattern: test each candidate against the **hardest line** the term appears in. Chapter 63's triple parallel (為無為，事無事，味無味) decided 無為; Chapter 52's 用其光，復歸其明 decided 明; Chapter 3's 實其腹 decided *belly* over *gut*. Find that line and let it choose.
