---
id: search-the-record-first
title: "The repository's own record is a source, and it is the one nobody checks"
status: active
since: 2026-09-23
trigger: "you are about to research a character, a fork or a rendering from 說文, the commentaries, or the web"
applies: [drafting, glossary, notes]
evidence: ["notes/translation.md#亂-luàn-disorder-a-tangle-with-hands-in-it-not-a-void", "notes/translation.md#明-míng-the-frontmatter-catches-up-with-the-entry-and-道-stops-being-a-path", "notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word"]
check: none
supersedes: []
---

# The repository's own record is a source, and it is the one nobody checks

**The rule.** Before researching a character from the dictionary, the commentators or the open web, **grep this repository for it.** Eleven thousand lines of notes, fifty glossary entries and eighty-one sets of chapter notes have already been written, and the answer is often in them — argued, dated, and by someone with the evidence open.

**When it fires.** Any time you are about to open 說文解字, a commentary or a search engine on a character, a textual fork or a candidate rendering.

```bash
grep -rn "亂" glossary/ notes/ chapters/ WORKLIST.md | grep -v "^chapters/[0-9]*\.md:[0-9]*| "
```

---

## Why this holds

**The method names every source except this one.** `process/method.md` §3 sends you to the graph, the oldest witnesses, the classical commentaries and the locks. All four are **outside** the repository, or vendored into it from outside. Nothing in the method says *read what we have already decided* — so the omission is structural, not carelessness, and it will recur for exactly as long as it goes unwritten.

**The record is not indexed by the thing you are looking for.** A finding about 亂 (*luàn* — disorder) can live in `chapters/003.md`'s notes because that is where it was found, and the next person needing it is working on chapter 64. `notes/` is indexed by chapter, `glossary/` by term, `WORKLIST.md` by debt — and a finding often belongs to none of the three cleanly. **That is the same gap [[scope-is-data-reason-is-prose]] and `process/principles/` itself were built for**, and it is why grep beats browsing here.

**Rediscovery is not free, and it is not harmless.** It costs the research again, and it risks arriving at a *different* answer from the one already recorded — at which point the repository holds two rulings and no one knows which is live. The point of a record is that the second person does not have to be as lucky as the first.

---

## The cases

**亂, and the ch 3 note that already knew.** The entry written on 2026-09-21 established that 說文 defines 亂 by 治 (*zhì* — to govern), that the graph is hands at tangled silk with the tool that untangles, and that **亂 and 治 are one act read from both ends.** Every part of that had been written on **2026-08-31**, in `notes/translation.md` under Ch 3, during that chapter's rebuild. It was found again from the dictionary instead of from the paragraph. *(What was genuinely new was one further gloss — 𤔔，理也, which 說文 gives under 辭 — and it took the argument the rest of the way.)* → [亂](../../notes/translation.md#亂-luàn-disorder-a-tangle-with-hands-in-it-not-a-void)

**明, where the entry's own body was the answer.** `glossary/ming-明.md` had listed four grammatical forms in its *working register* section since it was written, while `render:` carried two. The gap was described as a discovery; it was a paragraph in the file being edited. → [明](../../notes/translation.md#明-míng-the-frontmatter-catches-up-with-the-entry-and-道-stops-being-a-path)

**保, where `WORKLIST.md` had already diagnosed it.** The holding-family row's own closing note said the ch 15 decision *"had been argued from ch 9's literal gloss table rather than its verse."* That is precisely the fault that surfaced a fortnight later when the lock was first asked to speak in chapter 9 — pre-diagnosed, in the file that tracks what is owed. → [the holding family](../../notes/translation.md#the-holding-family-執-守-保-持-four-hands-one-english-word)

---

## Where it does not fire

**Not as a substitute for the primary sources.** The record is a **first** stop, never the last. [[commentary-is-not-a-rendering]] and [[verify-the-flag]] still hold: what the repository says about a character is our own prior reasoning, not evidence, and it can be wrong. 亂's own case makes the point — the earlier note was right about 說文 and had not seen the 辭 gloss that settles which way the hands work.

**Not on a character with no history here.** Where grep returns nothing, that is the answer and it took one command.

**Not a reason to trust a note over a line.** A note records what was true when written. Where it disagrees with the verse, that is a finding — see the supersession blocks in `notes/translation.md`, which exist because this happens.

---

## What it obliges

1. **Grep before you research.** `glossary/`, `notes/`, `chapters/` and `WORKLIST.md`, on the character itself.
2. **Cite what you find**, so the second recording points at the first instead of competing with it.
3. **If the record is superseded, say so in place** — a supersession block where the old reasoning sits, not only a new note elsewhere. An old ruling with no mark on it will be found again and believed.
4. **If the record was right and you rediscovered it, record that too.** It is evidence about the method, and it is how this rule got written.
