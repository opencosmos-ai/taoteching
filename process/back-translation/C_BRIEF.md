# Comparer — the brief

You are the third pass of a blind back-translation audit of Shalom Ormsby's English Tao Te Ching (the repository at /home/user/taoteching). Two readers worked blind:

- **Reader A** saw only the English and wrote down, unit by unit, what it says to a careful English reader: claim, speech act, who acts, force, link, and what is open. Files: `bt/A_out/`.
- **Reader B** saw only the Chinese and the classical commentaries (Wang Bi, Heshang Gong, Han Fei) and wrote the same for the Chinese. Files: `bt/B_out/`.

Your job: **compare them, chapter by chapter, and find where a reader of the English comes away with something different from what the Chinese says.** You are not blind. You may and must read the repository to verify.

## Read first

1. `/home/user/taoteching/CLAUDE.md` — the operating context, above all **the gloss rule** and the standing rules. Follow the gloss rule in everything you write: every Chinese character, word or line gets pinyin with tone marks and an English rendering beside it, as 為 (*wéi* — "to do / to handle"). Names of people and books romanized only (Wang Bi, Heshang Gong, Han Fei, Shuowen), never in characters.
2. `/home/user/taoteching/process/accuracy-audit.md` — an audit already run tonight on omissions and additions. **Do not re-report its findings**; if your comparison independently confirms one, say so in one line under "Confirms".
3. `/home/user/taoteching/process/form-audit.md` — skim; do not re-report form findings (chains, parallels, stanza breaks).

## What counts as a divergence

| Class | Means |
|---|---|
| **CLAIM** | the English asserts something the Chinese does not, or drops a claim the Chinese makes |
| **ACT** | the speech act changed: a question became a statement or the reverse, a real question became rhetorical, a description became a command or the reverse, a conditional became flat |
| **WHO** | the doer or the done-to differs: a supplied subject the Chinese and both commentators make unlikely, or a subject changed |
| **FORCE** | scope or modality changed: sometimes → always, can → does, will → is, must added or dropped |
| **LINK** | a connective invented, dropped where it carries the logic, or changed (because ↔ therefore ↔ but) |
| **CLOSED** | the Chinese is genuinely double (Reader B's **Open**, with the grammar or the commentators actually dividing) and the English silently takes one side, with no note recording the choice. The project's ethos: *"where the text is genuinely double, say so and leave the tension open"* |
| **OPENED** | the English invites a reading the Chinese does not support: an ambiguity Reader A found, or a connotation (theistic, moral, mechanistic, gendered, modern) a reader would hear |
| **OPAQUE** | Reader A could not make sense of the English at all, where the Chinese is clear enough to Reader B |

Not a divergence: a difference of wording that leaves claim, act, doer, force and link the same. A choice that follows a **locked rendering** (`glossary/INDEX.md`) is not an error; report it only if it materially misleads the cold reader, labelled **LOCK**, as evidence for Shalom, not as a fault. Never argue 正/奇 (*zhèng / qí* — straight / crooked): it is deferred by Shalom (`WORKLIST.md` T4).

## How to verify each one, before you write it down

1. **Read the Chinese in the chapter's own source table** (`chapters/NNN.md` → `## Source`) and the English (`## Translation`). Reader B may be wrong; Reader A may misread. A divergence is real only if it survives the page.
2. **Read the commentaries yourself** where the call turns on a reading: `sources/commentaries/{wangbi,heshanggong,hanfeizi}/NNN.md`. Quote and gloss.
3. **Check whether it is already decided.** Read the chapter's `## Notes`, and grep `notes/translation.md`, `notes/manuscript.md`, `notes/reading.md`, the relevant `glossary/*.md`, `process/shaloms-call.md` and `WORKLIST.md`. A decision that is logged is **Logged**, with the pointer. Logged choices are still worth one line if the cold reader demonstrably got it wrong, because that is evidence the choice costs something, but mark them as logged.

## Severity

- **critical** — changes what the chapter says
- **major** — changes what a line claims, or who does it
- **minor** — a real shift in force or link that does not change the claim

## Output

Write to the output path you are given. Start with a summary list: every finding in one line, critical first. Then the entries:

    ### Ch N · Unit refs (A x / B y) · CLASS · severity
    - **Chinese:** the line, glossed
    - **English:** "the line"
    - **Reader A heard:** one line
    - **Reader B read:** one line
    - **The divergence:** two or three sentences, with the evidence (commentary quoted and glossed where it decides)
    - **Logged?** no · or yes, with the pointer
    - **Direction:** one line: what the English would have to do to close it. Not a finished rewrite unless it is obvious

End with **Confirms** (accuracy-audit findings you independently hit, one line each) and **Readers' errors** (places where Reader A or B misread, so the comparison was void there, one line each).

**Do not edit any file in /home/user/taoteching.** Read only. Be strict: a short list of real divergences is worth more than a long list of quibbles. When finished, reply with the path, the count by severity, and your three strongest findings in one line each.
