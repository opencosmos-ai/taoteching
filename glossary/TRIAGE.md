# Glossary triage — harvesting the early version

*Working document. The early glossary (`process/legacy-tao-source-code.md`) holds **48 entries** written partly in this project's voice and partly in a computational/thermodynamic framework applied by an earlier AI collaborator. This file classifies all of them, sets the harvest order, and records the rules for doing it. Delete once the harvest is complete and `INDEX.md` supersedes it.*

**Frequency counts below are real** — computed against `source/chinese.md`, all 81 chapters. They are the primary priority signal, alongside whether a term blocks current work.

---

## The rules for this harvest

**1. Verify; never inherit.** The early glossary contains at least one demonstrable error — 天 titled "The Cosmos," disproven by evidence from seven chapters. The same source wrote every etymology in it. So each graph claim is re-checked against Shuowen and oracle-bone/bronze forms, and each "Laozi uses this in chapter X" is re-checked against the actual text. Nothing carries forward on trust.

**2. Extract the observation; discard the metaphor.** The framework occasionally produced a true insight in wrong clothes. 心 "is prior to the heart/mind split" is correct and valuable; "mechanical processor," "the UI where consciousness meets reality," "overheats the system" are not. Keep the first, cut the second.

**3. Reject framework-generated renderings outright.** 成 → "Compiled / The Final Build" is not a candidate to weigh. It is an artifact of the metaphor and would corrupt the lock.

**4. Why this matters beyond style.** "The universe is software" implies a programmer. The mechanistic overlay smuggles in a designer exactly as "Heaven" smuggles in a God — the same error in different clothes. The 生 entry spent 1,500 words establishing that the cosmos was *borne, not built*; an entry saying the Tao "compiles" reality quietly restores the creator it removed.

**5. Rewrite to the standard, don't patch.** Every harvested entry is rebuilt to the established form: open with a live problem → read the character as a picture changing over time → let cross-textual evidence argue → name what is set aside → leave the real tension open. Both tests apply to every sentence — the **hymn test** and the **pointing test**. The computational frame fails the second as badly as the theological frame fails the first.

**6. One entry at a time.** These are the heart of the work. Better twelve excellent entries than thirty-seven adequate ones.

---

## Tier 0 — Do not harvest

**Superseded — the repo has better versions.** 道 · 德 · 生 · 母 · 常 · 玄 · 妙 · 我/吾

~~**常** (Cháng)~~ — ✅ **REWRITTEN 2026-10-14** → `chang-常.md`, to the entry standard. Found: 說文 says **a lower skirt** (the *always* sense is a phonetic loan); the Mawangdui silks write **two words**, 恒 (*héng*, a crescent moon between two lines) as the manner and 常 only as the name of ch 16/52/55; 韓非 gives 常 a birth with sky and earth, so *eternal* overclaims. *Ever-present* kept for ch 1; *ever / always* split by grammar; `shuowen:` frontmatter field introduced, and the explorer now shows its English.
*(Check the old 吾 entry, 41 lines, for any detail the pairing entry didn't absorb; likewise 吾 vs 身.)*

**Merged.** 食母 (ch 20) — already covered inside the 母 entry.

**Rejected.**

| Entry | Why |
|---|---|
| 成 (Chéng), "Compiled" | 28 framework markers, the most contaminated in the file. The etymology (戊, the battleaxe; the decisive strike ending a process) is sound and worth keeping — but as a *note*, not this entry. The rendering is an artifact. |
| ~~天 (Tiān), "The Cosmos"~~ | ✅ **DONE & LOCKED** → `tian-天.md`, 2026-08-24. "The Cosmos" superseded. 92 occurrences, the book's most frequent content character: 61 are 天下, 9 are 天地, **19 stand alone** and split — **sky** where 地 is in the series (7, 16, 25, 39), **nature** where 天 takes a verb (9, 47, 59, 67, 73, 77, 79, 81). Shuowen: 天，顛也 — *the crown of the head*. A body part, not a realm. 配天 (68) left open. |

**Not glossary entries at all** — zero occurrences in the text:

| Entry | Move to |
|---|---|
| 經 (Jīng), "Book" | Companion front matter — it explains the title, not a term |
| 老子 (Lǎozi) | Companion front matter — biography |

---

## Tier 1 — Blocking current work

| # | Term | Chapters | Old state | Why first |
|---|---|---|---|---|
| ~~1~~ | ~~**為** (Wéi) — "to do / to handle"~~ | 48 | — | ✅ **DONE** → `wei-為.md`. Found: the character is a hand on an **elephant**. |
| ~~2~~ | ~~**無為** (Wúwéi) — "non-doing"~~ | 10 | — | ✅ **DONE & LOCKED** → `wuwei-無為.md`. "Non-doing," not "non-action"; Ch 63's triple parallel decided it. |
| ~~3~~ | ~~**明** (Míng) — "clear-seeing"~~ | 12 | — | ✅ **DONE & LOCKED** → `ming-明.md`. Found: the old form 朙 is **moonlight through a window**. Ch 52's 用其光，復歸其明 decided it. 16/55 already agreed. |
| ~~4~~ | ~~**自然** (Zìrán) — "the self-so"~~ | 5 | — | ✅ **DONE & LOCKED** → `ziran-自然.md`. 自 is a **nose** — the part you point at to mean "me." Ch 25's ladder terminates; it does not reach past the Tao. |
| ~~5~~ | ~~**樸** (Pǔ) — "uncarved wood"~~ | 6 | — | ✅ **DONE & LOCKED** → `pu-樸.md`. 器 (vessel) is its counter-term; carving = naming = assigning function. Ch 57's "plain" confirmed as a licensed flexion. |
| ~~5b~~ | ~~**器** (Qì) — "vessel"~~ | 9 | *(was inside `pu-樸.md`)* | ✅ **DONE & LOCKED** → `qi-器.md`. Promoted out of 樸's `covers:` to its own entry: nine chapters is too much reach to be a footnote, and Ch 41 / Ch 67 use the **capacity** sense of 器 that 樸's entry had no room for. *Shuowen*: 皿也，象器之口，犬所以守之 — a yard of pots with a dog guarding them. |
| ~~5c~~ | ~~**眾** (Zhòng) — "the crowd"~~ | 6 | — | ✅ **DONE & LOCKED** → `zhong-眾.md`. Had drifted into four Englishes, including dropped entirely in Ch 8. Oracle bone shows labourers under the **sun** (later an eye) — the many who are worked and watched. Distinguished from 民 (the governed populace) and 百姓. |

**✅ Tier 1 complete.** Next: Tier 2, beginning with **無 / 有** (*wú / yǒu* — "absence / presence"), which appears in 40 chapters and currently has an eight-line stub.

## Tier 2 — High frequency, high value

| # | Term | Chapters | Old state | Note |
|---|---|---|---|---|
| ~~6~~ | ~~**無 / 有** — "absence / presence"~~ | 40 | — | ✅ **DONE & LOCKED** → `wu-you-無有.md`. 有 is a hand holding meat; 無 was originally a **dancer**. Ch 11's 無 is a literal hole. **Absorbs the old 利/用 pairing.** |
| ~~7~~ | ~~**萬物** — "the countless things"~~ | 27/16/17 | — | ✅ **DONE & LOCKED** → `wanwu-萬物.md`. **Three entries consolidated into one.** 萬 is a scorpion; 物 is a mottled ox. |
| ~~8~~ | ~~**心** (Xīn) — "heart"~~ | 6 | — | ✅ **DONE & LOCKED** → `xin-心.md`. The character is an **anatomical drawing** of the organ. English idiom (*learn by heart*, *change of heart*) never fully split heart from mind, so no hyphen needed. **Absorbs the old 腹 entry** — 腹 = *belly*, its counter-term, not "the wise core." |
| ~~9~~ | ~~**一** (Yī)~~ | 8 | 37L, 14 marks | ✅ **DONE & LOCKED** → `yi-一.md`, 2026-08-27. **The graph is a single stroke — nothing is depicted, so every mystical reading has to be imported.** 王弼 refuses it outright at Ch 22: 一，少之極也, *"the one is the extreme of few,"* anchored in 少則得，多則惑 one line above. Ch 42's 道生一 is the text's own refutation of a capital-O One: whatever 一 is, it is **borne**. Two registers held apart — the arithmetic (10, 11, 22, 67) and the cosmological (14, 39, 42). **Ch 22's *one thing* is a licensed per-chapter exception**, taken because *"the One"* now reads in English as a chosen-one trope. |

**✅ Tier 2 complete.**

## Tier 3 — Worth writing

| # | Term | Chapters | Old state | Note |
|---|---|---|---|---|
| 10 | **名** (Míng) | 9 | 51L, 10 marks | Ch 1 and 32. Pairs conceptually with 無名/有名. |
| 11 | **始** (Shǐ) | 7 | 47L | Consider as a **pairing with 母** — beginning vs. mother, the two halves of Ch 1's second couplet. |
| ~~12~~ | ~~**信** (Xìn) — "trust"~~ | 8 | 42L | ✅ **DONE & LOCKED** → `xin-信.md`. 人 beside 言 — a person by their word — and also a **split tally** (符契), so 信 is *correspondence that can be checked*, not an inner feeling. That is why "sincerity" and "faith" both fail. Kept being given 德's word: fixed in Ch 23 and Ch 38. Ch 49's 德信 puts both characters in one compound and settles it. 忠 (loyalty) absorbed here. Ch 81's 信言 left open until that chapter is drafted. |
| 13 | **王** (Wáng) | 8 | 41L, 11 marks | **Raised in priority.** Both Mawangdui silks read 人 (human) where our base reads 王 (king) in Ch 25's four greats, and the older silk has no king in the passage. See `DISCOVERIES.md` §1 — this entry now has a real argument to make. |
| 14 | **先** (Xiān) | 6 | 42L, 13 marks | |
| 14b | **希** (Xī) | 6 | — | **New, raised from Ch 70, 2026-08-24.** The graph is 爻 (crossed threads) over 巾 (cloth) — **loosely woven fabric you can see through.** *Sparse*, in six places and one sense, which this edition has been rendering three ways without noticing: ch 14 *the inaudible*, ch 23 *speak sparingly*, ch 41 大音希聲, ch 43 *few ever reach this*, ch 70 *those who know me are few*, ch 74 *rarely*. Rarity and inaudibility are the same property read across a crowd and across a sound — so Laozi's ideal of speech (23) and his account of his own reception (70) are **the same word**. Ch 70 also pairs it with 貴 (*guì* — precious): scarcity is where value comes from, and 河上公 makes the link explicit (希少也…故為貴也). |
| ~~14c~~ | ~~**貨** (Huò) — "goods"~~ | 5 | *(never triaged)* | ✅ **DONE & LOCKED** → `huo-貨.md`, 2026-08-30. **Never triaged because it looked like a common noun.** It turned out to be carrying chapter 3's political argument, and to have been wearing two other characters' English: *the precious* (貴's, chapters 3 and 64) and *rare treasures* (寶's, chapter 12), plus 富's *wealth* at chapter 44. Each of those made the line **circular** — *"do not prize the precious."* The graph is 貝 (*bèi* — a cowrie shell) under 化 (*huà* — a body turning over): **a shell that changes hands**, against 寶's hoard under a roof and 貴's position on a price scale. 難得之貨 → **rare goods** as a unit; *rare* renders no character, because 難's *hard* is 堅's and its *difficult* will not go attributive. Swept ch 3, 12, 44, 64. **Ties to 14b:** ch 70's 希/貴 couplet has 河上公 deriving value from scarcity, which these chapters tell a ruler to break — and 希 must not take *rare*, now spent. |
| ~~15a~~ | ~~**精** (Jīng) — "vital essence"~~ | 2 | 36L | ✅ **DONE & LOCKED** → `jing-精.md`. 米 (rice) + 青; *Shuowen*: **擇也**, to sift. **Hulled grain** — what is left when the bulk is removed, which is why Ch 21's "primordial mass" was the exact inversion. Written **standalone, not paired with 氣**: Ch 55 sets them against each other (精 a reserve, 氣 a current), and a paired entry would blur the distinction the chapter is built on. |
| 15b | **氣** (Qì) | 3 | 21L | **Now owed.** 精 is locked and argues against it by contrast, so 氣 needs its own entry to complete the pair. Note that "energy" cannot go on 精's forbidden list precisely because 氣 claims it in Ch 55. |
| 16 | **混** (Hùn) | 3 | 29L | Ch 25's 有物混成. **Rendering settled 2026-09-06 as *mixed* across 14, 15 and 25** (three chapters had three Englishes), but no entry written, so it is unenforced — `WORKLIST.md` T2-40. *Shuowen*: 豐流也, on the **water** radical 水 — abundant flow, which is why muddy water is the ch 15 simile. |
| 17 | **反 / 復** | 4 | 6L stub | A true pairing — the movement of the Tao. Currently framed as "a thermodynamic loop"; needs full rewrite. **Widen it to three:** 歸 (*guī*) shares their English. All three read *return* across 21 lines, where *Shuowen* keeps them apart — 反 覆也 (overturn, on 又 a hand), 復 往來也 (going and coming, on 彳 the step radical), 歸 女嫁也 (a woman marrying in — going where one belongs). 反 fixed as *returning* at 25 and 40, 2026-09-06. `WORKLIST.md` T2-44. |
| 18 | **仁** (Rén) | 5 | 21L | Overlay watchlist — Legge's "benevolence," never "charity." |
| ~~19~~ | ~~**爭** (Zhēng) — "contend"~~ | 9 | — | ✅ **DONE & LOCKED** → `zheng-爭.md`. Two hands pulling one object; *Shuowen* 引也, "to pull," and the classical gloss 引之使歸於己 — *pulling a thing so it comes to oneself*. **All nine occurrences are negated** — the word never appears as something done. Ch 73's 不爭而善勝 decided it against "compete", which collapses into 勝 (overcome). Swept ch 3, 8, 22, 66.
| ~~20~~ | ~~**王** (Wáng) — "ruler"~~ | 13 | — | ✅ **DONE & LOCKED** → `wang-王.md`. The graph is a **broad axe-head**, not a person — no gender in it. The "three strokes are sky/earth/human and the king joins them" reading is **董仲舒** (c. 179–104 BCE), fourteen centuries after the graph, and it entered every dictionary via the *Shuowen*. All eight chapters define 王 by **lowness**. Swept ch 39, 42, 66. Absorbs 侯. See `DISCOVERIES.md` §4. |
| ~~21~~ | ~~**敢** (Gǎn) — "push / venture"~~ | 10 | — | ✅ **DONE & LOCKED** → `gan-敢.md`. A hand with a hunting weapon going after a **boar**; *Shuowen*: 進取也, "to advance and take." **Appetite, not bravery.** "Not daring" reads as cowardice and inverts Ch 73's 勇於不敢則活, *"courage in not-venturing lives."* Caught by Shalom. Swept ch 30, 64, 67. *presume* blocked by 恃 (→ `shi-恃.md`, locked as *rely on*). |
| ~~22~~ | ~~**全** (Quán) — "whole"~~ | 1 | *(never triaged)* | ✅ **DONE & LOCKED** → `quan-全.md`, 2026-08-28. **Never triaged because it looked too small** — three occurrences, all Ch 22 — and it turned out to be the chapter's whole argument. The graph is 入 (*rù* — bring in) over **玉 (*yù* — jade)**: *"pure jade is called 全."* **You cannot repair jade**, which is why every repair verb had to go: 全 is **preservation, not restoration** (河上公: 全其身, *"keep their body whole"*). Two collisions found by the reverse check — *complete* belongs to 成 (14 chapters; and Ch 41's 大器晚成 shows the book distrusts completion), and *flawless* is already carrying 瑕 (*xiá* — a flaw in jade) at Ch 27. **Absorbs 曲** (*qū* — bend), also Ch 22 only, and blocks *yield* for it, which is 弱's locked word. |
| ~~23~~ | ~~**大** (Dà) — "great"~~ | 51 | *(never triaged)* | ✅ **DONE & LOCKED** → `da-大.md`, 2026-09-06. **Never triaged because it looked too ordinary** — and at 51 occurrences across 24 chapters it is the most frequent character in the book to have gone untouched. The graph is a **person seen head-on, arms and legs spread**; *Shuowen*: 天大，地大，人亦大。故大象人形 — and **that definition quotes Ch 25's own line**, with 人 (*rén* — human) rather than 王 (*wáng* — king), six centuries before our earliest witness for 人. **Expansion to *vast* was weighed and declined** (Shalom): it fails on two-thirds of the lines — the comparative 禍莫大於, the severity of 大患 / 大偽 / 大迷, the seniority of 大匠 and 大丈夫, and 大笑 which is no magnitude at all. **The deeper reason is that 大 is a worn word in Chinese and the wear is doing work** — Ch 25 names the Tao 大 as an admitted defeat (王弼: 大有繫則必有分，有分則失其極矣), so an English with more charge than the original would make the forced name sound like it succeeded. Licensed flexions: *large* (60, 61), *greater* (comparatives), *master* (大匠). Absorbs 小. |
| ~~24~~ | ~~**士** (Shì) — "in service"~~ | 5 | *(never triaged)* | ✅ **DONE & LOCKED** → `shi-士.md`, 2026-09-07. Five lines, three chapters, and it carried **three Englishes — *masters* (15), *student* (41), *warrior* (68) — two of them on the identical phrase 善為士者**. *Shuowen* gives the definition in two characters, **士，事也** — a 士 is 事, **affairs** — which points straight at an entry this glossary already holds, whose graph is *a hand gripping the badge of office*. **The 一 + 十 reading with its Confucius quotation is Han philosophy laid over a shape**, the same treatment 董仲舒 gave 王 (see `wang-王.md`). **The commentators diverge, and that chose the English:** 王弼 makes 士 an office — 士卒之帥也, *"the commander of the troops"* — where 河上公 makes it a disposition, 言貴道德，不好武力. *In service* leaves both standing; *officer* would pick 王弼 and was declined by Shalom as bureaucratic and negatively valenced. **Seam noted:** 士 named a male class. Kin to T4-7. |

**A note this entry earned: frequency is not importance.** 全 has three occurrences and sat below every triage threshold for the life of this project. It is also the only word Ch 22 states, quotes back, and closes on.

**And 大 is the inverse of the same lesson.** It has fifty-one, more than any other untriaged character, and was skipped for the opposite reason: it looked too ordinary to need an argument. It turned out to be the word the Tao is finally named with, and the argument was about exactly that ordinariness.

## Tier 4 — Stubs needing commission

Each is 6–14 lines; these are seeds, not drafts.

~~**事**~~ *(entry written 2026-08-12 — `shi-事.md`; a hand holding the badge of office, the second hand beside 為's elephant. 無事 left open)* · **容** (4) · **愚** (3) · **命** (2) · ~~**腹**~~ *(absorbed into `xin-心.md`)* · **敦** (1) · **芻狗** (1) · **上善** (1) · **大制** (1)

---

## Relocations — these are not glossary entries

| Entry | Destination | Why |
|---|---|---|
| **利 / 用** | `notes/translation.md` | Not what the characters mean — a choice made in English ("stripping the capitalist static"). A rendering decision. |
| ~~**公**~~ / **仁** | `notes/translation.md` | 公 has its own entry as of 2026-08-12 — `gong-公.md`; the Shuowen cites Han Feizi for its etymology. 仁 still here. |
| **經**, **老子** | Companion front matter | Zero occurrences in the text. |

---

## Pairings — the standing decision

**True lexical pairs stay in `glossary/`.** Two characters that cannot be explained apart, where the meaning lives in the seam: **我/吾**, **玄/妙**, **無/有**, **反/復**, and possibly **始/母** and **精/氣**. A glossary of a philosophical text is not a dictionary — it is a lexicon of *how this book uses words*, and some words are only usable in pairs.

**The lookup problem is solved separately**, by `glossary/INDEX.md`: every character mapped to its entry, pairings included, with the locked rendering beside it. That file also becomes the seed for `terms.yaml` in `PLAN.md`.

**The pairing standard is already written** — it heads the Pairings section of the early glossary, in this project's voice:

> *"The meaning lives in the space between the two words, not in either alone. Read the characters against each other; be honest about where the language earns the contrast and where we are supplying it; find the passage where the text itself sets the pair in tension (e.g., Zhuangzi's 吾喪我); and let the pairing open rather than close — most of all when the seam it marks is one the reader may be living from the inside."*

It needs a permanent home in `process/method.md` §6.

---

## Tally

| | Count |
|---|---|
| Entries in the early glossary | 48 |
| Already superseded or merged | 11 |
| Rejected / relocated | 6 |
| **To harvest or commission** | **~31** |
| Of those, substantial drafts | ~16 |
| Of those, stubs needing writing from scratch | ~15 |
