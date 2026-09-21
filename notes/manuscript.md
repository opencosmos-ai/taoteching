# Manuscript Notes

*One of three notes layers. This one logs **textual forks between the witnesses** — where the older manuscripts disagree with our base text in a way that changes what a line says.*

---

## Using this file

**What goes here — and what does not.**

| Layer | Holds |
|---|---|
| **`notes/manuscript.md`** ← this file | **textual forks between witnesses** |
| `notes/translation.md` | our own rendering decisions and standing principles |
| `notes/reading.md` | reader-facing interpretation; cross-cutting **Threads** |

Our base text is the received **Wang Bi** recension (via the Chinese Text Project). Log only the **meaning-bearing** places where the older witnesses — **Guodian** (~300 BCE), **Mawangdui** (before 168 BCE), **Beida** (early Han), and the Tang-era **Fu Yi** text — diverge in a way that changes what a line says or how we have chosen to render it. Purely graphic or particle-only variants are not logged. Entry format: *chapter · the line · the fork · our call.*

**Never transcribe the Mawangdui or Guodian manuscripts.** Record the **fact** of a variant, never a modern editor's reconstruction of a damaged graph. `sources/PROVENANCE.md` explains why this is a licensing rule and not a preference.

**How it is ordered.**

| Level | What it is |
|---|---|
| `##` | one of the two sections below |
| `###` | a chapter, always written `Ch N · <the line or the fork>` |
| `####` | one fork, where a chapter has more than one |

1. **Punctuation and parsing forks** — where no character differs and only the editorial marks do.
2. **Witness forks** — **ascending by chapter number**. Within a chapter, in verse order.

**Three rules that keep it that way.**

1. **⚠ Every chapter heading must contain the literal string `Ch N ` — with a trailing space.** `check_locks.py`'s `unlogged-variant` rule substring-matches exactly that against this file, and fails the build when `sources/variants.yaml` records a fork this file has not logged. A heading reading `### Ch 21` alone, with no space after the number, **silently blinds the check.** Always write `### Ch 21 · …`.
2. **Every entry here should have a matching row in `sources/variants.yaml`**, and its `logged:` field should point back here. The two must not drift; the checker exists to stop them.
3. **New chapters are inserted in number order, never appended.** Chronology is git's job.

---

## Punctuation and parsing forks

*No character differs; only the editorial marks do. The Chinese carries no punctuation, so every mark in every edition is a later editor's.*

### Ch 32 · 道常無名。樸雖小 — where the break falls changes the subject

- **Received:** 道常無名**。**樸雖小，天下莫能臣也。 — *"The Tao is ever nameless. Though uncarved wood is small, nothing can subordinate it."* (樸 is the subject; the wood is what is small.)
- **Ours:** 道常無名**樸。**雖小，天下莫能臣也。 — *"The Tao is ever nameless, uncarved. Though small, nothing in the world can make it a subject."* (無名樸 is a compound attribute of the Tao; **the Tao** is what is small.)

We follow the second, on three grounds. **(1) The parallel with Chapter 37** is near-decisive — both chapters run *道常 + [attribute]*, then the identical sentence about rulers: 道常**無為**。侯王若能守之，萬物將自化 (37) / 道常**無名樸**。侯王若能守之，萬物將自賓 (32). Same frame, same rulers, same of-itself outcome. **(2) The pronoun.** 侯王若能守**之** — *if lords and kings can hold **it*** — takes the Tao as its antecedent naturally; under the received parse the nearest antecedent is a piece of timber. **(3) Chapter 34 already says the Tao is small**: 常無欲，可名於**小** — *"ever without desire, it may be named small"* — and, in the next breath, 可名為**大**, *"it may be named great."* Chapter 32 is that claim made a second time; 天下莫能臣也 is a real assertion about the Tao and a puzzle about wood.

*(A side benefit: with 樸 read attributively, the English needs no article, so nothing reifies the uncarved into an object — the same correction made when "block" was retired. See `glossary/pu-樸.md`.)*

### Ch 62 · 美言可以市尊，美行可以加人 — **resolved 2026-08-12: we keep the base text**

**Shalom's call, made against the recommendation.** Both readings are set out here in full, because the evidence is genuinely split and the argument on the losing side is worth preserving.

**The fork.** Our received base divides the line after 尊 and reads 美行 (*měi xíng* — fine conduct), giving a 美 / 美 parallel: *"fine words can buy honor; fine conduct can raise a person above others."* **Both Mawangdui silks**, the **Fu Yi** and **Fan Yingyuan** editions, and **both classical commentaries** instead divide after 市 and read 尊行 (*zūn xíng* — honored conduct). Heshang Gong's lemmas are printed as two separate units — 美言可以市 and 尊行可以加人 — and Wang Bi's comment splits identically, closing each half with its own 故曰 (故曰美言可以市也 … 故曰可以加於人也).

**For the base, which is where we land.** The ***Huainanzi*** (c. 139 BCE) quotes the line **twice**, in 人間訓 and 道應訓, with the 美 / 美 parallel — the oldest *quotation* of the line, against the oldest *manuscripts*. **Yu Yue** and **Zhu Qianzhi** both followed it. And the split camp is not unanimous: **Fu Yi reads 尊言, not 尊行**, so the witnesses that agree against our base do not agree with each other.

**The case against this call, recorded so it stays available.**

**1. Lectio difficilior.** Our base is the **smooth** reading — fully parallel, 美 answering 美. The split is **rough**: an asymmetric pair with 市 (*shì* — market) left standing alone as a bare verb. In a text this full of parallel couplets, a copyist meeting the rough reading has an obvious motive to regularize it and none to break a clean parallel, so the drift would run from the split toward our base rather than the reverse.

**2. Wang Bi's text contradicts Wang Bi's commentary**, and that is a documented systematic feature of this recension — some seventy-nine places where the Laozi transmitted *over* the commentary differs from readings quoted *inside* it, the received text having been supplanted by Heshang Gong-line readings. On that reasoning the text Wang Bi actually had read the split, and our base is later here than the commentary printed above it.

**What the call changed.** The verse, which had been drafted on the split. Chapter 62 now reads *"Fine words can buy honor. / Fine conduct can raise a person above others."* The line's function is unaffected either way — fine words and fine bearing have purchase, therefore no one is beyond reach, therefore 何棄之有.

**Still open, and a different question:** the line's **tone**. Heshang Gong reads it as a put-down (美言者獨可於市耳 — *"fine words are good for the marketplace, and that is all"*), Wang Bi as praise of the Tao, and Ch 81 will say 信言不美，美言不信. That is a reading question, not a textual one, and it lives in the Translation Notes.

---

## Witness forks

### Ch 9 · 功遂 / 功成名遂 — how many things are finished before the body withdraws

We print 功遂身退，天之道 — *"the work done, the body withdraws; this is the way of nature."* **The Siku compilers attach a collation note to their own 王弼 (*Wáng Bì*) text**: 〔案**河上公注本及各本俱作功成名遂身退**〕 — *"Heshang Gong's commentary text and all editions read 功成名遂身退."* Our vendored 河上公 prints the longer lemma, and glosses it 言人所為功成事立，**名迹稱遂**，不退身避位則遇於害.

**The fork is 名 (*míng* — name, reputation).** The longer reading finishes two things before the withdrawal: the work, **and the name**. That is not idle, because 河上公 then quotes the same shape back at ch 44's opening — 名遂則身退也 — where 名 is the first term of the chapter's question (名與身孰親, *"your name or your body, which is dearer?"*). On the longer reading ch 9 and ch 44 are one argument about reputation; on ours, ch 9 is about work alone.

**We keep the base**, per the standing rule that this is an edition of the received recension. Recorded because our base is here the **minority** reading among the editions the Siku compilers knew, and because the English turns on it. `sources/variants.yaml`.

### Ch 10 · two forks, and both sit on the lines our English had swapped

**能為雌乎 / 能無雌乎.** We print 能**為**雌乎, *"can you be the hen?"* 河上公 (*Héshàng Gōng*) reads 能**無**雌乎, *"can you be **without** the hen?"* — the opposite instruction. And **our own vendored 王弼 (*Wáng Bì*) prints 無 in the lemma**, with the Siku compilers' collation note attached: 〔案**注義無似作為**〕 — *"by the sense of the commentary, 無 appears to be 為."* The commentary does settle it: 雌**應而不倡，因而不為**。言天門開闔，**能為雌乎**？ — *"the hen responds and does not lead off; she goes along and does not act. It says: when the gate of the sky opens and closes, can you be the hen?"* **So our 為 follows the Siku editors' own correction of the text they print**, and that had never been recorded.

**能無為乎 / 能無知乎.** 河上公's text reads 能**無知**乎 at the sixth question — the same three characters he prints two questions earlier at 愛民治國 — so **his chapter asks the 無知 question twice and never asks the 無為 question at all.** He glosses this one 無有能知道滿於天下者, *"there is none who can know the Tao that fills the world."* 王弼 prints 無為 and glosses it 能無以為乎，則物化矣, quoting ch 37 verbatim. **We keep the base text.**

**Why both are worth having.** Our English had 無知 and 無為 **on each other's lines** (`WORKLIST` T1-1), and the fork sits on exactly those two lines — so a reader who found the old English and went looking would have had no way to tell an error from a witness. Both recorded in `sources/variants.yaml`.

### Ch 28 · the stanza order is an editorial restoration

Our vendored 王弼 (*Wáng Bì*) carries the Siku compilers' note on the opening block: 〔案**永樂大典此節在復歸於無極之後，據注仍宜在前**〕 — *"in the Yongle Dadian this section stands **after** 復歸於無極; on the evidence of the commentary it should still come first."* So the 雄/雌 stanza's position at the head of the chapter is **restored**, not simply transmitted, and the Ming encyclopaedia had it second.

**Not in `sources/variants.yaml`**, for the same reason as ch 38's 處/居: the 永樂大典 (*Yǒnglè Dàdiǎn*, 1408) is not one of the schema's witness ids, it is neither excavated nor a named older transmitted recension, and forcing it into the `witnesses:` map would put a Ming encyclopaedia where the file promises a witness. 河上公 (*Héshàng Gōng*) has the same order as our base, so no listed witness diverges. **Nothing in our English turns on it** — the three stanzas are a template and each is self-contained — but the chapter's shape rests on a collation decision, and that is worth a reader knowing.

### Ch 38 · 扔 / 仍 — both graphs mean *pull*, and our English had said *force*

Our base prints 攘臂而**扔**之. 河上公 (*Héshàng Gōng*)'s lemma reads **仍**, and the Siku 王弼 (*Wáng Bì*) carries the compilers' collation note 〔案**扔各本俱作仍**〕 — *"for 扔, all editions read 仍."* **Nothing turns on the choice**, and that is the point worth recording: 說文解字 glosses 扔 as **因也**, *"to draw along"*, and 仍 carries the same sense, which is why 河上公's own gloss is 攘臂**相仍引** — *"bare their arms and pull at one another"* (引, *to pull*). Our English read *"bares its arms and forces them,"* which follows **neither** graph. Both are about **pulling**. Recorded in `sources/variants.yaml`; the rendering is in `notes/translation.md`.

### Ch 38 · 處 / 居 — a Ming collation note, deliberately not in the apparatus

The closing stanza alternates 處 (*chǔ* — to dwell) and 居 (*jū* — to reside): 處其厚，不居其薄；處其實，不居其華. Our vendored 王弼 carries 〔案**焦竑云古本四句並作處**〕 — *"Jiao Hong says the old text has 處 in all four."* 焦竑 (*Jiāo Hóng*, 1540–1620) is a **Ming** scholar reporting a lost 古本, so this is neither an older witness nor a meaning-bearing fork, and **it is not in `sources/variants.yaml`** — there is no honest witness id for it, and forcing one into the `witnesses:` map would put a Ming report where the schema promises an excavated or named transmitted reading.

It is recorded here because it **licenses a rendering decision**: the two verbs are near-synonyms and the alternation may not even be original, so the English is free to use one verb across all four clauses rather than straining to mark a distinction the text may not be making.

### Ch 3 · 智者 / 知者 — one graph or two, and the commentators then describe different people

**Found 2026-08-31, while settling the chapter's knowing-family.** 王弼 (*Wáng Bì*)'s text — our base — writes 使夫**智**者不敢為也. 河上公 (*Héshàng Gōng*)'s writes **知**者, and appends a phonetic note: **知音智**, *"知 is read* zhì" — that is, read this 知 as the word 智. **He attaches it only here.** Two lines above, on 常使民無知無欲, he glosses 反朴守淳 (*"return to the uncarved, keep to the pure"*) and adds no note at all. So the tradition reads **two words in consecutive lines even where one graph is written**, and marks which is which.

**The fork is meaning-bearing because the two commentators then describe different people.** 王弼: 智者謂知為也 — *"the 智者 are those who know how to handle"* — the operators, and the line restrains them. 河上公: 思慮深，不輕言 — *"deep in deliberation, they do not speak lightly"* — which is almost word for word what he says of the unambiguously approving 知者 at ch 56, 知者貴行不貴言也 (*"the knower prizes action and does not prize speech"*). **王弼 has two graphs and two figures; 河上公 has one graph and one figure.**

**We print the base text's 智者 and keep the English open.** *"The knowers"* is a bare nominalization, as 者 (*zhě*) is in Chinese, and it leaves the line to say whether knowing is good here — where *"those who know how"* or *"the clever"* would both have picked 王弼's side. The rendering decision is in `notes/translation.md`.

### Ch 3 · 使民心不亂 — the 民 in the third clause is an eighteenth-century restoration

**河上公's lemma reads 使心不亂, with no 民** (*mín* — the people). And our own vendored 王弼 carries the Siku compilers' collation note on the passage: 〔案原本及各本俱無民字，惟永樂大典有之…今校〕 — *"the base edition and all editions lack the character 民; only the Yongle Dadian has it… now emended."* They restored it on the evidence of 王弼's own commentary.

**Nothing in the sense turns on it** — the subject is the people in either reading, and 王弼 glosses the line 故可欲不見，則心無所亂也, *"so when the desirable is not displayed, the heart has nothing to disorder it,"* with a bare 心. It is logged because **this file's companion note at ch 3 says "all three clauses are 使民X"** (`notes/translation.md`, 2026-08-30), and in the third clause that is an editorial restoration rather than a reading the witnesses agree on. We keep the base text as printed.

### Ch 4 · 湛兮似或存 / 似若存 — a hedge either way

河上公's lemma reads 似**若**存, and the Siku edition of 王弼 carries the collation note 〔案或一作若〕 — *"for 或, one edition reads 若."* 或 (*huò* — perhaps) and 若 (*ruò* — as if) are hedges of the same force, so **nothing turns on it**: the line carries a doubled hedge, 似 plus one of them, under either reading. Recorded so it is not rediscovered later as if it were news, since the line was rewritten on 2026-08-31. *(Ch 4 is **not attested at Guodian**; it rests on the silks and later.)*

### Ch 8 · 政善治 / 正善治 — and 說文 defines one as the other

**Found 2026-09-02, reviewing the chapter.** Our base text (王弼, *Wáng Bì*) prints 政善治 with 政 (*zhèng* — government, administration); 河上公 (*Héshàng Gōng*)'s lemma prints **正**善治 with 正 (*zhèng* — straight, on the mark). His gloss fits the graph he prints: 无有不洗，清且平也 — *"there is nothing it does not wash; clean and **level**,"* where 平 (*píng* — level) answers 正 rather than 政.

**It is barely a fork, and 說文解字 is why.** It defines the one by the other: **政，正也。从攴从正，正亦聲** — *"政 is 正; from 攴 (*pū* — a hand holding a stick) and 正, and 正 also gives the sound."* 政 is 正 with the stick added — the same word, with enforcement attached. Nothing in the line's sense turns on which is printed, though the pair are not identical in force, and the stick is exactly what this chapter's water does without.

**We keep the base text's 政**, rendered *governing*, which leaves 治 (*zhì* — to order) free for *order* — as at ch 64's 治之於未亂 — instead of colliding with it. 王弼 is **not vendored for ch 8**: the Siku transcription is unproofread for ten chapters, this among them, so the chapter has one classical commentary and not two.

**This does not touch T4-2**, the deferred 正 / 奇 (*zhèng / qí* — straight / crooked) call. That is a question about how 正 is rendered where we print it; this is a question about which graph is printed, and logging a fork settles nothing about the other.

### Ch 15 · 安以動之 / 安以久動之 — 河上公 has a 久 our base does not

*(2026-09-06.)* The second of the two 孰能 (*shú néng* — who can) questions reads 孰能安以動之徐生 in our base. **河上公 (*Héshàng Gōng*) carries the line with an extra 久 (*jiǔ* — long, for a long time): 孰能安以久動之徐生**, and his gloss leans on it — 誰能安靜以久徐徐以**長生**也, *"who can be settled and still **for long**, and slowly slowly attain **long life**."*

**It is meaning-bearing, and we keep the base.** With 久 the line acquires duration and, in 河上公's hands, 長生 (*cháng shēng* — long life) — the longevity reading that runs through his commentary and that this edition's naturalistic razor is wary of. Without it the line is a plain mirror of the one above it: a state, an action applied to it, a slow result. The parallel with 孰能濁以靜之徐清 is exact only without 久, and that parallel is the point of the pair.

### Ch 23 · three facts on one chapter — a dropped 道者, a 得/失 swap, and a Ming witness without 樂

**Found 2026-09-03, rebuilding the chapter. `--witnesses 23` had reported nothing: nobody had looked.**

**1. 王弼's own lemma reads 道者 where our base text does not.** Our base prints 故從事於道者，同於道 (*"so one who attends to affairs by the Tao is the same as the Tao"*); the vendored 王弼 (*Wáng Bì*) prints **故從事於道者，道者同於道**. With the extra 道者 (*dào zhě* — "the Tao-one") the stanza is a clean three-term parallel — 道者同於道；德者同於德；失者同於失 — and **without it the first line is a different shape from the two that follow.** The asymmetry is in the Chinese, not only in the English. *(This chapter's own note on 德 has been quoting the three-term version since 2026-08-31, i.e. quoting a text we do not print — corrected with this pass.)* **Not meaning-bearing:** the sense of the line is identical either way. **We keep the base text**, and the English mirrors its asymmetry rather than silently repairing it.

**2. 河上公's third line reads 失亦樂失之, not 失亦樂得之** — *"loss too gladly **loses** them"* against our *"loss too gladly **gets** them."* His gloss follows the graph he prints: 與失同者，失亦樂**失**之也. **Meaning-bearing, and the difference is real**: our base makes loss an acquirer, closing the three-term pattern (道 gets you, 德 gets you, 失 gets you); 河上公's makes loss a loser, so that what you get from loss is more losing. **We keep the base text**, on the parallel — 樂得之 stands in the first two lines under both readings, and breaking it in the third is the harder claim to justify than keeping it. The reading is recorded because it is the sort of thing that gets rediscovered as news.

**3. A Ming witness without 樂, deliberately not in the apparatus.** The Siku 王弼 carries 〔案**永樂大典無樂字**下二句同〕 — *"the Yongle Dadian lacks the character 樂 (lè — glad); the same for the two lines below."* The 永樂大典 (*Yǒnglè Dàdiǎn*, 1408) is a **Ming** encyclopedia, so this is a report of a lost reading and not an older witness. **It is not in `sources/variants.yaml`** — there is no honest witness id for it, exactly as with 焦竑's four 處 at ch 38. Recorded here because it would change the lines materially if true: without 樂, 道亦得之 is simply *"the Tao gets them too,"* and the gladness — which is what makes the third line bite — is ours by transmission rather than by the oldest text.

**4. 故 at 故飄風不終朝 — our base is the only witness that has it, and the English does not render it.** The Siku 王弼 carries 〔案**河上公注本及各本俱無故字**〕 — *"the Heshang Gong commentary edition and **all editions** lack the character 故 (gù — therefore)."* **Our vendored 河上公 confirms it**: his lemma is 飄風不終朝驟雨不終日, with no 故. So our base text is a **singleton reading** here, by its own editors' account. **We print it and leave it unrendered** *(Shalom's call, 2026-09-04)*: the verse sets the three statements side by side, as every other witness has them, and does not assert in English an inference our base alone claims. **This is not an emendation** — the 原文 table still prints 故, and a reader can see both the character and the decision. 說文 makes 故 unambiguously causal (使爲之也, *"to cause something to be done"*), so it could not have been softened into a comparison instead; *likewise* was proposed and declined. The reader-facing half of the decision is in `notes/reading.md`.

### Ch 19 · 絕聖棄智 / 絕仁棄義 — the oldest witness does not attack the Confucians

**The best-known meaning-bearing divergence in the whole Guodian Laozi, and it sits in a chapter we drafted with the apparatus silent.** Recorded 2026-08-28; this closes `PLAN.md` → G1.

Our base text severs three pairs: 絕**聖**棄**智** (sagehood and knowing), 絕**仁**棄**義** (humaneness and duty), 絕**巧**棄**利** (cunning and profit). **The Guodian slips (~300 BCE, bundle A, where this passage opens the bundle) carry neither 聖 nor 仁 nor 義 anywhere in it.** The reported readings are 絕**智**棄**辯** (*zhì / biàn* — knowing and disputation) and 絕**偽**棄**慮** (*wěi / lǜ* — artifice and anxious scheming), with 絕巧棄利 shared verbatim. That shared couplet is what makes the other two legible as **substitutions** rather than as a different passage altogether.

**We keep the base text**, and the reason is the same one that governs Ch 25: our edition is of the received recension, and a fork this size is a fact to record, not a text to replace. But it changes how the chapter should be *read*, and that belongs in the reading notes rather than here.

**What is solid and what is not.** That 仁義 and 聖 are absent is not in dispute and is reported consistently across the scholarship. The reconstruction of the second graph in 絕偽棄慮 **is** contested among editors — the slips are damaged and the 釋文 is 1998 living scholarship, which is also why no transcription appears in this repository. We record the absence, which is a fact about a text, and not the reconstruction, which is someone's editorial work. See `sources/PROVENANCE.md`.

**Why it matters beyond the apparatus.** Ch 18 and Ch 19 are the book's two most-quoted anti-Confucian passages, and 王弼's own commentary does not read them as an attack on goods: 聖智，才之善也；仁義，人之善也；巧利，用之善也 — *"sagehood and knowing are the best of talent; humaneness and duty are the best of persons; cunning and profit are the best of use."* Three pairs of **goods**, said to be insufficient as 文 (*wén* — cultural form), not three evils. The Guodian reading and the oldest commentary point the same way, from opposite ends of the transmission.

**A transmitted echo of the same seam.** The Siku Wang Bi runs Ch 18 and Ch 19 together, and its compilers note 〔永樂大典此章與上章合為一章〕 — *"the Yongle Dadian joins this chapter with the previous as one chapter."* Guodian runs Ch 17 and Ch 18 together (see `guodian-inventory.yaml`). The chapter divisions here are late and unstable in both directions.

### Ch 21 · 道之為物 / 道之物 — the silks drop the copula

Our base reads 道之**為**物，惟恍惟惚. Both Mawangdui silks read **道之物** with no 為, leaving 之 as a plain possessive: *the Tao's thingness*, rather than *the Tao's being a thing*. **Both point at the same sense**, so the reading is not in doubt — but the fork is worth logging because it settles what the line's **topic** is: not the Tao itself but *what the Tao amounts to as an entity*, which is a topic-comment construction and wants topic-comment English. Hence *"Whatever the Tao is, it is only vague, only elusive."* We keep the base text; nothing turns on 為. (The silks also read 唯 for 惟 and 望/朢 for 恍 — graphic and phonetic variants, not meaning-bearing.)

#### 自古及今 / 自今及古 — the direction of the inquiry

Our base reads 自**古**及**今** ("from ancient times until today"). **Both Mawangdui silks** read 自**今**及**古** ("from **now back to** antiquity"). **We keep the base text**, and log the fork because it is genuinely meaning-bearing: it reverses the direction of the inquiry. Mawangdui makes the chapter *start* from the present and trace backward; Wang Bi makes it *arrive* at the present. We render the arrival — the line ends on "today," and the closing "By this." completes the movement toward the reader, which is the movement of the whole chapter. *(That closing line read "By this, here, now" until 2026-08-30; the movement survives the trim, because the arrival is carried by "today," not by the demonstrative.)*

The same two lines carry two more forks. 以**閱**眾**甫** against the silks' 以**順**眾**父** (順 = *follow along with*, not *observe*) — we keep 閱; and 甫/父 needs no decision, since Ch 42 already settled that 父 here means *origin / root*, not "godfather," and both give "origin" in English.

#### 眾甫之狀 / 眾甫之然 — **resolved 2026-08-11: we follow 然**

Our base reads 眾甫之**狀** ("the *shape* of that origin"); four independent witnesses read **然** ("that it *is so*") — both Mawangdui silks, the Song Heshang Gong edition, and the Siku Quanshu compilers' own collation note on this very line, 〔案狀各本俱作然〕, *"for 狀, all editions read 然."*

**We follow 然**, and the decisive argument is not a manuscript one: 吾何以知…然哉？以此 is a **fixed closing formula** that Ch 54 and Ch 57 both use, so 然 completes it and 狀 breaks it. Full reasoning in the Translation Notes; `our_call: mawangdui-a` in `sources/variants.yaml`. The base text and Source table keep 狀; only the translation follows the witnesses, as at Ch 41, 42, 47 and 53.

*(An earlier version of this note ended "marked `undecided` pending Shalom's call." That was stale — the call was made and the apparatus records it. Corrected 2026-08-11.)*

The same Siku file carries a second collation note, 〔案此二句一本在下二句之下〕, recording a **line-order** variant: in one edition the 象 couplet follows the 物 couplet rather than preceding it. Logged, not acted on.

#### What the commentators say 此 means — they diverge, and the English holds neither

**⚠ Corrected 2026-08-30.** This section previously read *"our line holds both"* and claimed that the English *"By this, here, now"* carried Wang Bi and Heshang Gong at once. It did not: it carried Heshang Gong's gloss, dropped Wang Bi's entirely, and did it by lifting a commentator's word into the verse. The line now reads **"By this."** in all three chapters. See `notes/translation.md` → *以此 — one formula, one English*.

The two oldest commentaries gloss 以此 (*yǐ cǐ* — "by this") **differently, and that divergence is the finding — not something to average.**

- **王弼 (*Wáng Bì*), ch 21:** 此上之所云也…言吾何以知萬物之始於無哉，以此知之也 — *"'this' is what was said above… it says: how do I know the countless things begin in no-thing? By this I know it."* **Anaphoric** — 此 points back at the text, the whole descent through 象 (*xiàng* — image) / 物 (*wù* — thing) / 精 (*jīng* — vital essence) / 信 (*xìn* — trust).
- **河上公 (*Héshàng Gōng*), ch 21:** 此，今也。以今萬物皆得道精氣而生 — *"'this' means **now**. Because now the countless things all obtain the Tao's essence-breath and live."* **Deictic, in time.**
- **河上公, ch 57 — the same opening gloss, verbatim:** 此，今也…以今日所見知 — *"'this' means now… by what is seen today, he knows it."*
- **河上公, ch 54:** 以此五事觀而知之也 — *"by observing these five matters, he knows it"* — naming the referent as the five cultivations (body, family, community, state, world).

Two things follow. **Heshang Gong glosses ch 21 and ch 57 with the identical five characters**, which is independent evidence from the tradition that 吾何以知…然哉？以此 is one fixed formula — the claim `DISCOVERIES.md` §2 rests on. And **the two readings are incompatible**: *what was said above* is anaphora, *now* is time. A bare demonstrative in English holds both open; any English that specifies picks one and hides the fork.

Heshang Gong's reading also independently supports the Mawangdui 自今及古 (*zì jīn jí gǔ* — "from now back to antiquity") direction, from the opposite end of the tradition. *(All quoted from `sources/commentaries/`.)*

### Ch 25 · 王亦大 / 人亦大 — king or human among the four greats

**⚠ Corrected 2026-08-20. What stood here before was wrong, and wrong in the direction that flattered the edition.** It recorded that both Mawangdui silks read 人 (*rén* — human), that the older silk had no king in the passage at all, and that silk B could be caught "mid-drift." None of that survives checking. The correction was forced by `concordance.py --witnesses 25`, which had been flagging for some time that Guodian was never consulted here.

**Every excavated witness reads 王** (*wáng* — king). Guodian (~300 BCE, bundle A) reads 王 in both places — and orders the list 天大，地大，道大，王亦大, sky and earth *before* the Tao, where the received text puts the Tao first. Both Mawangdui silks and the Beida Han slips read 而王居一焉. So does 河上公. There is no excavated witness for the human reading and no visible moment of arrival: **the throne is in the oldest text we have.**

**人 is a transmitted reading, and a late one.** 傅奕 (*Fù Yì*, 555–639, Tang) carries 人亦大 and claims descent from a 古本 (*gǔ běn* — an ancient exemplar). The earliest extant witness for the second line, 人居其一焉, is 范應元 (*Fàn Yìngyuán*, Song) in 老子道德經古本集註; his own note reads that 人 follows Fu Yi and the ancient text, while 河上公 has 王. 奚侗 (*Xī Tóng*, early 20th c.) argued in 老子集解 that both should be 人 and that 王 was 尊君者之妄改 — *"a reckless emendation by those who revered the ruler."* Modern critical and popular editions often print 人 following this line of argument, **usually without marking it as an emendation** — which is how a translator working from a "帛書版" text online can come to believe the silks read 人. That is what happened here.

**We still follow 人 — and the grounds are now entirely different.** Not manuscript age, which runs the other way. Three things, in order of weight:

1. **The received text contradicts itself.** The next line is 人法地 ("humans follow earth"). A text that makes the *king* one of the four greats and then instantly makes *humans* the bottom rung of the ladder has a seam in it. This is Fan Yingyuan's argument and Xi Tong's, made on internal evidence centuries before any manuscript was dug up, and it is untouched by the excavations.
2. **The reading Fu Yi and Fan preserve may still be old.** A transmitted edition is not automatically younger than a buried one; it is only less certain. The claim is unprovable either way, and should not be leaned on.
3. **Standing rule 2**, universality over the incidental male-default — an *editorial* ground this edition avows openly. Note that it does not depend on the fork at all: 王 is not gendered in Chinese, and `glossary/wang-王.md` renders it *ruler / sovereign* everywhere, never *king*. Reading 王 here would still not produce a king in the English.

**域 / 國.** Our base reads 域中 (*yù zhōng*); Guodian, both silks and Beida all read 國中 (*guó zhōng* — within the state). Not meaning-bearing — 域 and 國 are one root 或 (*huò*) with two different classifiers, soil under it or a wall around it — but worth noticing that the **state** word is the one every excavated witness carries. The territorial frame is the oldest layer here. *(Note also 有物**混**成 / 有物**昆**成 — a graphic variant only, both "merged, undifferentiated"; not meaning-bearing.)*

**Source quality, stated honestly.** These readings were established from converging Chinese-language secondary sources, not from a printed critical apparatus. Before any of this is published, check against 高明 *帛書老子校注* and the 文物出版社 excavation reports. The convergence is strong — the sources agree on the non-obvious specifics, including Fan Yingyuan as the earliest 人居其一焉 — but it is not the same as having seen the plates.

*`DISCOVERIES.md` §1 and §4 rest on the superseded version of this note and both need rewriting. See the correction banners there.*

### Ch 31 · the Siku editors flag part of this chapter as absorbed commentary

*(2026-09-07.)* Our vendored 王弼 carries an unusual note in the running text, at 兵者不祥之器:

> 〔案自此句至言以喪禮處之，**似有注語雜入**，但河上公注本及各本俱作經文，今仍之〕
> *"From this sentence down to 言以喪禮處之, **it appears that commentary has been mixed in**; but the 河上公 edition and all editions treat it as canonical text, so we retain it."*

**That is a claim about textual stratification, not a variant reading**, and it has a second piece of evidence beside it: **王弼 leaves no commentary whatsoever on ch 31** — alone among the chapters vendored in `sources/commentaries/`, his text here is bare running characters with collation notes and nothing else. The traditional inference is that the commentary is missing because part of the passage was not scripture to him.

**We keep the received text, as every edition does, and record the doubt.** It is **not** in `sources/variants.yaml`: there is no fork between named witnesses to record, and no honest `witnesses:` id for *"the Siku editors suspect an interpolation."* Same reasoning as the 焦竑 note at Ch 38.

**What it touches, if true:** the stretch from 兵者不祥之器 through 言以喪禮處之 — which is most of the chapter's middle, including 非君子之器 and the general-seating lines. Readers should know the chapter's argument may be built partly of an early reader's marginalia that hardened into text.

### Ch 29 · 挫 / 載 and 歔 / 呴 — two forks in one four-line series

*(2026-09-07.)* Block 2 runs four 或▢或▢ pairs, and the last two both carry collation notes in the Siku edition of 王弼.

**或挫或隳 → we follow 河上公 and read 載.** 〔案挫河上公注本作**載**〕, and his lemma is 或載或隳. 挫 (*cuò*) is 說文 **摧也**, *to break*, standing beside 隳 (*huī* — to ruin): **two wrecking words, where the three pairs before it are all oppositions** — 行/隨 (go ahead / follow), 歔/吹 (breathe out / blow), 強/羸 (strong / frail). 載 (*zài*) is 說文 **乘也。从車**, *to carry*, on the **cart** radical, so *carried* against *toppled* restores the pattern. **王弼's own gloss requires one:** 凡此諸或，言物事**逆順反覆** — *"all these 'sometimes' speak of things and affairs going against and along, reversing and returning."* **⚠ Both witnesses are transmitted, not excavated** — Guodian does not carry ch 29 — so this follows a Han commentary against our Wei base **on internal grounds only**, and is recorded as an editorial call rather than a manuscript one.

**或歔或吹 → we keep the base.** 〔案歔河上公注本作**呴**〕. 河上公 reads his own text as a **temperature** pair: 呴溫也，吹寒也。有所溫必有所寒也 — *"呴 is to warm, 吹 is to cool; what warms one thing must cool another."* Our 歔 is 說文 欷也…一曰出气也, *to sob; to let out breath* — a soft breath against a hard blow rather than warm against cold. The reading is recorded, not adopted; **"some sigh, some blow."**

### Ch 41 · 大器晚成 / 免成 — late, or never

Received: 晚成, "completed **late**." Mawangdui reads 免成, Guodian reads 曼成 — both "**never** completed / free of completion." We follow the manuscript reading — *"the great vessel is never completed"* — because it completes the parallel with its neighbors (無隅 / 希聲 / 無形, each "the great X *lacks* its defining mark"). Flagged here rather than decided in silence.

### Ch 42 · 教父 / 學父 — father of teaching, or of learning

Received: 教父, "father of **teaching**." Mawangdui reads 學父, "father of **learning**." We follow 學父 — *"this I take as the root of learning"* — the bolder reading, and the older one in the silk. (Two further points on this line: 父 here means *origin / root*, not "godfather"; and there is no possessive in the Chinese — it is "the root of learning," not "of *my* learning." The 吾 is only the one who adopts it.)

### Ch 46 · 禍莫大於不知足 — the manuscripts remember a third clause

The received text gives **two** calamity-clauses: 禍莫大於不知足 (no *disaster* greater than discontent) / 咎莫大於欲得 (no *fault* greater than the desire to acquire). Mawangdui and the Fu Yi text open the run with a **third, prior** line: **罪莫大於可欲** — "there is no greater **crime** than desire" (可欲, "the desirable," the same phrase as Ch 3's 不見可欲). So the older witnesses remember a rising three-beat — **crime**/desire → **disaster**/discontent → **fault**/greed — that the received text trimmed to two. We keep the received pair, noting the manuscripts' fuller crescendo.

### Ch 47 · 不見而名 / 不見而明 — the homophone fork

Received: 不見而**名** (名, *to name / discern*) — "without seeing, discerns." Mawangdui reads 不見而**明** (明, *clarity / be clear*) — "without seeing, understands clearly." We follow **明**: it completes the parallel (*know / see-clearly / accomplish*, each without its usual means) and reads cleaner than 名 here. Worth noting the fork falls between two of our own glossary entries — 名 (the name / ledger) and 明 (clear-seeing) — the homophone pair, both *míng*.

### Ch 52 · 是謂襲常 / 習常 — two characters, and our English had been following the one we do not print

**Found 2026-08-31, by asking why ch 27 and ch 52 rendered the same character two ways.** They were not rendering the same character. Ch 27's *"inherited clarity"* read 襲 (*xí* — to layer a garment over another, hence to succeed to); ch 52's *"the practice of the ever-present"* read **習** (*xí* — to repeat, to drill). Our base text prints **襲** in both places, so ch 52's English was following a variant nobody had recorded.

**Both commentaries print 習.** 河上公 (*Héshàng Gōng*) glosses it outright: 人能行此，是謂**習修**常道 — *"if a person can do this, it is called **practising and cultivating** the constant Tao."* The Siku edition of 王弼 (*Wáng Bì*) also sets 習 in the lemma and attaches the compilers' collation note 〔案**習各本作襲**〕 — *"for 習, all editions read 襲"* — with the gloss 道之常也, *"the constancy of the Tao."*

**We keep the base text and read 襲, and the argument is structural rather than documentary.** 是謂襲明 (ch 27) and 是謂襲常 (ch 52) are the identical frame, and 明 (*míng* — clear-seeing) and 常 (*cháng* — the ever-present) are the book's own bonded pair: 知常曰明 (*zhī cháng yuē míng* — "knowing the ever-present is called clarity") stands verbatim at ch 16 and ch 55. **襲明 and 襲常 are one gesture applied to the two halves of that formula**, and reading 習 at ch 52 dissolves the pair into a coincidence. 習 is also the easier character of the two, which is the direction copying usually runs.

*Recorded in `sources/variants.yaml`; the rendering decision is in `notes/translation.md`. The fork was invisible to `check_locks.py`'s `unlogged-variant` rule, which fires only on variants a chapter **claims** — an English that quietly follows an unrecorded reading is exactly what no check can see.*

### Ch 53 · 是謂盜夸 / 盜竽 — the boast, or the lead-pipe

Received: 盜**夸** (dào kuā) — "the *swagger* / boast / extravagance of thieves." The Mawangdui silks read 盜**竽** (dào yú), and the oldest commentary on the *Laozi*, Han Feizi's *Jie Lao*, reads it so too. 竽 is the great reed mouth-organ that *led* the ancient ensemble; in Han Feizi's own words, "when the *yu* leads, the bells and zithers all follow; when the *yu* sounds, every instrument falls into harmony with it." So 盜竽 is not the *boast* of thieves but their **lead-pipe** — the tone-setter, the ringleader whose tune the whole band of lesser thieves plays along to. We follow **竽**: the gleaming ruler is not merely a loud thief but the chief one, the head the country's thievery falls in behind. (The variant sharpens the charge, too — 夸 accuses him of showing off; 竽 accuses him of *leading the theft*.)

### Ch 55 · 全作 / 朘作 — the newborn's quickening

**Correction, 2026-08-11:** this note previously said our base text reads 而**全**作. It does not — **our source table reads 而朘作**, the Mawangdui and Fu Yi reading, while the verse renders 全 (*"their whole being quickens with life"*). The received Wang Bi reading is indeed 全, as the Siku Quanshu printing confirms (`sources/commentaries/wangbi/055.md`). So the verse follows 全, the source table shows 朘, and the note had misdescribed both. Found by the commentary import. The rendering stands; only the account of where it came from was wrong.

Received Wang Bi: 而**全**作 — 全 = *whole, complete* — "yet it quickens wholly." The older **Mawangdui** and **Fu Yi** texts read 而**朘**作, where 朘 (zuī) is specifically *the infant boy's member* — an explicit male erection. The traditional gloss takes both as the reflex erection (全 as a decorous stand-in for 朘). We keep our base text's **全** and read it in its plain sense — *the whole being quickens with life* — which preserves the point (精之至: desireless potency arising from fullness) while keeping the emblem universal, for infants of every gender. (See the paired Translation Note, and Process guide §0 on the incidental male-default.)

### Ch 61 · 邦 / 國 — the Han name-taboo

Where our received base reads 國 (*guó* — state) seven times in this chapter, the Mawangdui silks read 邦 (*bāng* — state). This is the systematic Han substitution avoiding the personal name of the founding emperor Liu Bang (劉邦), and it runs through the received text wherever 邦 stood. Meaning-neutral, logged once here rather than at every occurrence.

#### 則取大國 — active, not passive

Received: 小國以下大國，則**取**大國 — *"a small state, by going below a large state, then **takes** the large state."* The Chinese carries no passive marker, yet most translations render the second half passively ("is taken by the large state"), and some editions supply 於 (取**於**大國) to license it. We keep the **active** reading in both halves. The chiastic repetition is the argument: the same move, made by either party, acquires the other. Heshang Gong reads it so as well, glossing the pair as the large state gaining the small state's goodwill and the small state gaining the large state's favour. Making the second half passive restores exactly the ordinary power relation this chapter exists to invert.

### Ch 62 · 奧 / 注 — the chapter's first word is not in the oldest witnesses

Both Mawangdui silks read **注** (*zhù*) where our base text reads **奧** (*ào*). Gao Ming's *帛書老子校注* takes 注 as a loan for **主** (*zhǔ* — master, lord), giving *"the Tao is the master of the countless things"*, and supports it from outside the *Laozi*: Zheng Xuan glosses 奧 as 主 in his commentary on the *Liji · Liyun* (奧猶主也), and the *Zuozhuan* (Zhao 13) has 國有奧主, *"the state has its 奧主."* So 奧 and 主 are not far apart in Han usage, and the emendation is the mainstream scholarly reading.

**We keep 奧, and the reason is internal.** Chapter 34 denies the mastery reading twice, in the identical two words: 衣養**萬物**而不為**主** and **萬物**歸焉而不為**主** — *"it clothes and feeds the countless things yet does not act as their master"; "the countless things return to it yet it does not act as their master."* A Ch 62 that reads 道者萬物之主 puts the book in flat contradiction with itself on 萬物 and 主, the same pair of words in both places. That is a heavy price, and the variant does not require us to pay it: 注 at face value is 氵 (water) beside 主 and means **to pour into**, which gives *"what the countless things pour into"* — a confluence image, sitting one chapter after Ch 61's 大國者下流 (*"the large state is the downstream flow"*) and 天下之交 (*"the confluence of the world"*), and answering Ch 32's 猶川谷之於江海. And Gao Ming's own chain runs through a room: 奧 can mean *master* only because the 奧 corner is where the household head presides. **The place is the older layer of the word, and both witnesses keep the place. Only the dominion is optional, and Ch 34 forbids it.**

#### 善人之寶，不善人之所保 — two forks, and one of them undoes a note

(1) Our base uses **two different graphs** — 寶 (*bǎo* — treasure), then 保 (*bǎo* — to keep safe). **The silks use the same graph twice**, and published transcriptions disagree about which one, a disagreement that is itself modern editorial work rather than a fact about the silk. So the received text's elegant pair may be a **later differentiation of a single word**, and the Translation Note that treated it as an original piece of wordplay has been corrected accordingly. (2) Separately, Dunhuang manuscripts, Yan Zun and Zhao Zhijian read 不善人之所**不**保 — *with a negation* — while Yan Kejun reports all editions reading 所保. We keep the base text: the negation would make the Tao what the unmasterful **fail** to keep, which contradicts the 何棄之有 three lines later.

#### 天子 stands in the silks

立天子 is present in the Mawangdui text, so the title is **not** a later accretion. *(This sentence formerly contrasted Ch 25, on the claim that the silks read 人 there. That claim was wrong — see the corrected Ch 25 note — and the contrast is withdrawn. The point stands on its own: 天子 is in the silks, so the distortion in "Son of Heaven" is entirely English.)* The grandeur is Laozi's own, put there to be knocked down. This settles the question left open when the chapter was drafted; see the Translation Notes on 天子 → *"a child of the sky,"* and `DISCOVERIES.md` §3.

#### 三公 / 三鄉 — the silks name the office with the word that means minister

Where our base reads 三**公** (*sān gōng*), the silks write 三**鄉**, which editors read as a loan for 三**卿** (*sān qīng* — the three high ministers). Not meaning-bearing, and logged only because it settles an English question: 公 is conventionally rendered *duke*, a borrowed European rank, and the oldest witness calls the office by the word that simply means **minister**. Our rendering turns out to be the older reading's own word.

#### Apparatus note · Wang Bi's commentary on this chapter is filed under Chapter 61

`tools/concordance.py --commentary 62` reports Wang Bi as *not vendored*, and the importer lists 62 among ten chapters whose Siku transcription is unproofread. But the text is present: the Siku printing runs Chapter 62 on into Chapter 61's block, opening with the chapter heading and the compilers' own collation note 〔案河上公注本此為為道章〕 (*"in the Heshang Gong recension this is the chapter titled 為道"*), and the whole of Wang Bi's Ch 62 commentary follows inside `sources/commentaries/wangbi/061.md`. Ch 62 was drafted with it. **The importer's chapter-splitting needs a look** — wherever else a chapter heading sits mid-block, the same thing will have happened. Logged in `WORKLIST.md`.

### Ch 63 · 報怨以德 is native to this chapter, not a stray from Ch 79

The line 報怨以德 (*bào yuàn yǐ dé* — "repay resentment with integrity") has long been suspected of being a fragment displaced from Ch 79, which is the book's other chapter on grievance (和大怨 — "reconciling a great resentment"). **Mawangdui A has it here**, in this chapter, immediately following 大小多少. So its placement is as old as our oldest witness to it, and the argument it picks with the *Analects* (see the Reading Notes) is the chapter's own and not an accident of transmission.

#### 夫輕諾必寡信 — damaged in both silks

The 輕諾 / 寡信 line is broken in both Mawangdui manuscripts; B preserves only fragments of the span between 輕 (*qīng* — light) and 信 (*xìn* — trust), with graphs missing. Our reading of it therefore rests on the **received text alone**, and so does the *trust* rendering of 信 at this line. Worth stating rather than rendering as though the witnesses concurred. (We record the fact of the damage and not any modern reconstruction of the lost graphs — see `sources/PROVENANCE.md`.)

### Ch 64 · 泮 or 破 — a brittle thing thaws or snaps

Our Wang Bi base reads 其脆易**泮** (*pàn*), a water-radical graph whose sense is ice going soft; Heshang Gong's lemma text reads 其脆易**破** (*pò* — to shatter). The Siku editors flag the head character as well, with 〔案脆釋文云一作膬〕 — the *Shiwen* reporting 膬 for 脆 (*cuì* — brittle). **We keep the base graph and render toward shattering**, because that is what brittleness does; a thing that thaws was never brittle. Small, but it is the difference between dissolving and snapping, and the chapter's whole point is that the thing is still catchable.

### Ch 64 · at Guodian the two halves are separate, and the second half is copied twice

*Corrected 2026-08-17. The first version of this note said the two halves sat in different bundles. That is not what the slips show, and the truth is sharper.*

**Bundle A carries both halves, far apart.** The second half (為者敗之 onward) stands in its first slip-unit, between Ch 15 and Ch 37; the first half (其安易持 onward) stands in its fourth unit, before Ch 56 and Ch 57. Six chapters lie between them. **Bundle C then carries the second half again** — making it the only passage in the Guodian Laozi copied twice.

So the two halves of our Chapter 64 never appear joined, in either bundle, in the order our base text gives them. What the received text presents as one chapter, the oldest witness presents as two circulating sayings, one of which was popular enough to be copied into two different collections.

**The seam is visible in the sense at exactly the point the slips break it.** The proverb-triad ends at 千里之行，始於足下 and a different argument starts at 為者敗之，執者失之 — *act early* giving way to *do not act*, with no bridge. We had already flagged that tension in the Reading Notes as something to leave open rather than smooth. The manuscript evidence says the tension is not Laozi's inconsistency; it is a join.

**We keep the received chapter.** Our base text is Wang Bi and the whole book is transmitted through it; unpicking a chapter our own recension presents as whole would be editing, not translating. But the note stands with the chapter. See `sources/guodian-inventory.yaml` for the full slip arrangement.

### Ch 65 · 稽式 or 楷式 — the same standard, two glosses

Our Wang Bi base reads 稽式 (*jī shì*), Heshang Gong's text reads 楷式 (*kǎi shì*), and the Siku compilers note it in the margin themselves: 〔案河上公注本稽作楷下同〕 — *"in the Heshang Gong recension 稽 is written 楷, and likewise below."* Both compounds name a standard or model, so nothing in the English turns on it.

**What does turn on it is the gloss, and there the two commentators part.** Wang Bi reads 稽 as 同 (*tóng* — held in common): 今古之所同則不可廢, *"what past and present hold in common cannot be discarded."* The standard is what does not change across time. Heshang Gong reads 楷式 as 法式 — the working pattern for governing self and state, a template you apply. Metaphysical against practical, from one graph. **We keep the base text and render 式 as "pattern",** which is already Ch 28's word for 為天下式.

### Ch 67 · 我道大 or 我大 — **resolved 2026-08-19: the chapter is about Laozi**

Our base reads 天下皆謂**我道**大 — *"everyone says my Tao is vast."* Heshang Gong's lemma reads 天下皆謂**我**大, *"everyone says **I** am vast."* **We follow Heshang Gong, against our own base text.** Six arguments converge, and only the second is about manuscripts.

**1 · 不肖 is a first-person humility word.** 肖 (*xiào*) is *to resemble*, and 不肖 (*bù xiào*) is a **self-deprecating pronoun** in classical Chinese — *"I, the unworthy one"* — built on the idea of a child who does not resemble its father. It survives in 不肖子 (*bù xiào zǐ* — unworthy son) and 不肖徒 (unworthy student). It is a word people apply **to themselves**. Applied to the Tao it is strained; applied to a speaker it is the ordinary idiom.

**2 · Heshang Gong's comment is unmistakably personal.** 老子言天下謂我德大，**我則佯愚似不肖** — *"Laozi says the world calls my integrity great; **I then feign foolishness** and seem unworthy."* 佯愚 (*yáng yú*) is to put on stupidity deliberately. That is a man doing something, not a Tao being something. He continues in the same register: 唯獨名德大者為**身**害 — *"only those whose name and integrity are called great suffer harm to their **person**."*

**3 · He reads 細 as a petty person, not a small thing.** 言辨惠者唯如**小人**也，非**長者** — *"the clever are just like **petty men**, not **elders**."* This is where the argument for the base text collapsed. The first version of this note kept 道 on the grounds that the following lines "argue about a thing." They do not. On the oldest full commentary they argue about a man.

**4 · The chapter does not change subject.** Line four is 我有三寶，持而保之 — *"I have three treasures; I hold them and keep them safe."* Under 我大 the chapter runs continuously in the first person from its first character. Under 我道大 the subject switches abruptly after three lines and switches back.

**5 · The pronoun is the right one, by our own glossary.** `glossary/wo-wu-我吾.md` settles 我 (*wǒ*) as **the self seen** — "the self that is positioned, contrasted, felt: I, as against others" — where 吾 (*wú*) is the self seeing. 天下皆謂**我** is literally *the world's verdict on me*, which is precisely 我's work.

**6 · Ch 20 and Ch 70 are this chapter in other words.** All three are first-person and all three are about being misread by 天下 (*tiān xià* — the world). Ch 20: 我獨異於人 (*"I alone differ from others"*) and 而我獨頑**似**鄙 (*"I alone am stubborn and **seem** coarse"*). Ch 70: 天下莫能知 (*"no one in the world can understand"*), 不**我**知 (*"they do not know **me***"), 知**我**者希 (*"those who know **me** are few"*). Chapter 67 shares Ch 20's 我 … 似 X shape exactly: 天下皆謂我大，**似**不肖.

**How 道 got in.** *"Everyone says I am vast"* reads at first glance as a boast, and a copyist who feels that inserts 道 to make it modest — *my Tao is vast*. Copyists move from the harder reading to the smoother one, not the reverse. And the boast dissolves the moment the line is finished: the second half is self-deprecation. **People say I am vast, and I look like nothing.**

**The base text and the Source table keep 道**; only the verse follows the witness. That is the practice already used at Ch 21, 41, 42, 47 and 53.

### Ch 67 · 器 or 事 — the oldest witness reads "affairs"

The Siku compilers note it in the margin: 〔案器韓非子作事〕 — *"for 器, the Han Feizi text reads 事."* Han Fei died in 233 BCE, which makes his the oldest witness to this passage by four centuries.

So: 成**器**長, *chief of vessels* (our base), against 成**事**長, *chief of affairs* (Han Feizi). Not a small difference. 器 (*qì* — vessel) is the counter-term to 樸 (*pǔ* — uncarved wood), and Ch 28 supplies the mechanism: 樸散則為器, *"when the uncarved is scattered it becomes vessels."* Under 器 the line says the one who refuses to be first becomes what all the specialised things answer to — precisely because they were never carved into one. Under 事 it says something much flatter about precedence in undertakings.

**We keep 器**, on Ch 28's support and because the vessel reading is what makes the third treasure a claim rather than a maxim. The older reading is logged rather than buried.

### Ch 73 · a line missing from our base text — **restored 2026-08-20**

After 天之所惡，孰知其故？ (*"what nature hates, who knows why?"*) the received Wang Bi and Heshang Gong texts both read **是以聖人猶難之** — *"therefore even the sage finds it difficult."* **Our base text does not have it,** in the Source table or in `source/chinese.md`.

This is not a variant reading. It is an absent line, and it is absent from a text we describe as the Wang Bi recension while the Siku printing of Wang Bi has it in the lemma.

**Both commentators build their reading of the chapter on it.**

- **王弼:** 孰，誰也。言誰能知天下之所惡意故耶？其唯聖人。夫聖人之明，猶難於勇敢，況無聖人之明而欲行之也 — *"孰 means 'who'. Who can know the reason for what is hated? Only the sage. And the sage's own clarity still finds daring difficult — how much more someone without the sage's clarity who means to act on it anyway."*
- **河上公:** 言聖人之明德猶難於勇敢，況无聖人之德而欲行之乎 — the same argument in almost the same words.

**Why it was probably deleted.** The identical six characters stand in Ch 63, followed there by 故終無難矣 (*"and so in the end has no difficulty"*). Modern editors — Ma Xulun among them — read Ch 73's occurrence as a copyist's importation from Ch 63 and strike it. That judgement is modern, and it is made against two commentaries that had the line in front of them and reasoned from it.

**What turns on it.** Without the line, 孰知其故？ hangs unanswered and the chapter jumps straight to 天之道. With it, the question gets its beat: *who knows? — even the sage finds this hard.* The whole chapter is about the unknowability of what nature refuses, and the line is where the speaker admits he does not know either.

**RESTORED, by Shalom's call.** The row now stands in `chapters/073.md` and in the derived `source/chinese.md`. **This is the first base-text addition in the project** — every earlier departure from the base left the Source table untouched and moved only the verse (Ch 21, 41, 42, 47, 53, 67). The distinction matters: those were places where we preferred another witness's *reading* of a line we had; this was a line we did not have at all, and no amount of choosing between readings could have recovered it.

*(The second time our base has proved not to be the Wang Bi recension at a given point — see Ch 2, where the Siku Wang Bi reads 相較 … 相傾 against our 相形 … 相盈. Worth a systematic check of the base against the Siku printing, now that both are in the repository.)*

### Ch 68 · 善勝敵者 or 善勝戰者 — the lemma slips, the commentary does not

Our base reads 善勝**敵**者，不與 — *"one masterful at overcoming **enemies** does not engage them."* Heshang Gong's lemma prints 善勝**戰**者, *"one masterful at winning **battles**."*

**His own commentary settles it against his lemma.** He glosses the line 不與**敵**爭而**敵**自服也 — *"does not contend with the **enemy**, and the **enemy** submits of itself"* — using 敵 twice. The text he was reading had 敵; the lemma has assimilated to 善**戰**者 in the line directly above.

Not meaning-bearing, and logged only because the four parallel 善X者 clauses are this chapter's entire structure — warrior, fighting, enemies, people — and a witness that repeats 戰 in two of them collapses one of the four.

### Ch 69 · 相若 or 相加 — our base leaves the Siku Wang Bi for the third time

Our base text reads 故抗兵**相若** (*gù kàng bīng xiāng ruò* — "so when the raised armies are alike"). The Siku printing of 王弼 and the Song 河上公 both lemmatise 故抗兵**相加**, and Wang Bi glosses the character: 抗舉也，加當也 — *"抗 means to raise; 加 means to be a match for."* Both readings arrive at *evenly matched*, so nothing in the English turns on it and we keep the base.

It is logged for a different reason. This is the **third** point at which the text we call the Wang Bi recension does not agree with the Siku printing of Wang Bi — chapter 2 (相形 … 相盈 against 相較 … 相傾), chapter 73 (a whole line missing), and now this. The systematic check of our base against the Siku text, suggested at Ch 73, is owed.

**Also noted and not logged as a fork:** 河上公's lemma prints 仍無敵 where our base has 扔無敵. His own gloss, 雖欲仍引之 (*"though you would drag at it"*), gives 仍 the sense of 扔, so the two are the same word with two graphs.

### Ch 72 · 狎 or 狹 — and the fork is not orthographic, it is the whole chapter

Our base reads 無**狎**其所居 (*wú xiá qí suǒ jū*). 河上公's lemma prints 無**狹**其所居 — same sound, different graph, and a different sentence.

- **狎** is 犭 (the dog radical) beside 甲 — to crowd in, to grow over-familiar, to make light of. Something **done to** the people from outside.
- **狹** is 犭 beside 夾 (*jiā* — squeezed between) — narrow, cramped. A **condition of** the space itself.

**We keep the base.** 王弼 uses 狎 in his own commentary — 自貴則物狎厭居生, *"exalt yourself, and things crowd and weary dwelling and living"* — so the reading is secure on the base side, and the graph he read is the one our text has.

**But the variant is exactly what 河上公's reading of the chapter needs**, which is why it is worth recording rather than filing as a copyist's slip. He glosses the line 謂心居神，當寬柔，不當急狹也 — *"this speaks of the heart as where the spirit dwells; it should be broad and yielding, not tight and cramped."* With 狹 the sentence stops being an instruction to a ruler about houses and becomes an instruction to anyone about their own interior. A one-graph fork carries an entire school's reading. Recorded in `sources/variants.yaml`.

### Ch 72 · 其 has no antecedent, and the two commentators supply different ones

無狎其所居，無厭其所生 — *"do not crowd **their** place of dwelling, do not weary **what gives them** life."* Classical Chinese lets 其 (*qí*) float; English cannot.

**王弼 reads it as the people's.** His note is entirely political: 離其清淨，行其躁欲，棄其謙後，任其威權，則物擾而民僻 — *"leave that pure stillness, act on restless desire, abandon humble deference, rely on awe and power: then the countless things are disturbed and the people turn crooked."* The subject is a ruler and the objects are subjects.

**河上公 reads it as your own.** 其所居 is where the **spirit** dwells — the heart. 其所生 is what **keeps you alive** — 人所以生者爲有精神，託空虛，喜清淨, *"what makes a person alive is having vital essence and spirit, lodged in emptiness, delighting in pure stillness."* The offence is not taxation but appetite: 飲食不節，忽道念色，邪僻滿腹，爲伐本厭神 — *"eating without restraint, neglecting the Tao and dwelling on lust, depravity filling the belly: this cuts down the root and crushes the spirit."* His chapter title is 〈愛己〉, **loving oneself**.

**Our call: 王弼.** 民 (*mín* — the people) is the topic of the line immediately before, and 其 takes the nearest available antecedent; 河上公 has to import 心 (heart) and 神 (spirit), neither of which appears anywhere in the chapter. That is his physiological school reading itself into the text, and it is the same move that turns Ch 6's valley spirit into an organ.

**It is not thereby worthless, and this is not averaged into a consensus.** The chapter's second half is four 自 (*zì* — self) in two lines — 自知, 不自見, 自愛, 不自貴 — the densest reflexive run in the book. The chapter really does turn inward, and 河上公's title names where it lands. See `notes/reading.md`.

### Ch 74 · the two commentators disagree about who does the killing, and it is not a textual fork

常有司殺者殺 — *"there is always one whose work is the killing."* The base text names an office and never fills it. Both commentators fill it, differently, and neither reaches for a god.

**河上公 fills it with nature.** 司殺者天 — *"the one who presides over killing is 天 (tiān — sky/nature)"* — and he immediately makes it impersonal and seasonal: 天道至明，司殺者常，猶春生夏長秋□冬藏 — *"the way of nature is utterly clear; the one who presides over killing is ever-present, like spring giving birth, summer growing, autumn [reaping], winter storing."* He closes the gloss on 天網恢恢踈而不失, **the line Ch 73 ends on**, which makes 73 and 74 one argument in his reading: the net already catches everything, so the ruler's axe is surplus.

**王弼 fills it with other people.** 為逆順者之所惡忿也，不仁者人之所疾也，故曰常有司殺也 — *"one who goes against the grain is what the compliant hate and resent; the un-humane (不仁, bù rén) is what people loathe; therefore it says there is always one who presides over killing."* No cosmology at all. The deviant is destroyed by the ordinary revulsion they provoke, and that revulsion is the standing executioner.

**Not averaged.** They agree on the only thing the chapter needs — that the office is already filled and the ruler is not in it — and they disagree about everything else. Our English keeps the office and names no occupant, which is what the base text does. This is the second chapter running where 王弼 and 河上公 supply different referents for a gap classical Chinese leaves open and English usually closes; see the Ch 72 entry above on 其.

### Ch 74 · 殺 once or twice

Our base: 夫**代司殺者殺**，是謂代大匠斫. 河上公's lemma: 夫**代司殺者**是謂代大匠斵 — one 殺, not two. The Siku editors record the divergence inside 王弼's own commentary text, 〔案河上公注本作夫代司殺者是謂代大匠斲〕. We keep the base; nothing in the English turns on it, because an office called *the one whose work is the killing* already carries the verb. Recorded in `sources/variants.yaml` as the fourth Siku-flagged departure of our base text (Ch 2, 68, 73).

### Ch 75 · the third charge, with or without 上

Our base text: 民之輕死，以其**上**求生之厚，是以輕死 — *"the people make light of death because **those over them** want their own lives so rich."*

**Both commentary printings in this repository lack the 上.** 王弼's Siku lemma runs 民之輕死以其求生之厚是以輕死, and 河上公's lemma is the same. Without 上, 其 (*qí*) falls back to 民 (*mín* — the people), and the sentence reverses its aim: the people make light of death because **they themselves** seek to live too thickly. That is not a copyist's shrug. It breaks the chapter's triple parallel — two charges against the rulers, then one against the governed — and it converts the line into a near-duplicate of Ch 50's 以其生生之厚.

**河上公 read it that way.** His gloss is unambiguous: 人民輕犯死者以其求生活之道太厚，貪利以自危 — *"the people make light of risking death because their way of seeking to live is too rich; they covet gain and so endanger themselves."* The subject is the people.

**王弼 did not, even though his lemma lacks the character.** His entire comment on the chapter is 言民之所以僻，治之所以亂，皆由上，不由其下也，民從上也 — *"this says that the reason the people go crooked and government falls into disorder is due **entirely to those above**, not to those below. The people follow those above."* 皆 (*jiē* — entirely, all of them) covers all three charges. He is reading the sense our base spells out, whichever graph sat in front of him.

**Our call: the base.** The 上 is in our text, the triple parallel is the chapter's whole rhetorical engine, and 王弼's 皆由上 licenses it explicitly. But the fork is real and it is doctrinal, not orthographic — it is the difference between a chapter about rulers and a chapter about appetite as such, and 河上公's whole physiological school lives on the second reading. The same split as Ch 72's floating 其, one chapter's distance away, and logged rather than averaged. Recorded in `sources/variants.yaml`.

*Also noted, not logged as a fork:* our base writes 飢 (*jī* — a person's hunger) where 王弼's Siku lemma writes 饑 (*jī* — crop failure, famine). Interchangeable in this period and nothing in the English turns on it; "the people go hungry" serves both.

### Ch 76 · 木強則折 — three readings, and both commentators leave our base

Our base has 折 (*zhé* — to snap). **王弼's lemma has 兵** (*bīng* — weapons), and his gloss commits to it: 物所加也, *"it is what gets applied to it."* The strong tree draws the axe — strength **attracts violence** rather than causing its own failure. **河上公's lemma has 共** (*gòng* — together), glossed 木強大枝弱共生其上也, *"the tree being big and strong, the weak branches grow together above it"* — which makes the line a setup for the closing couplet about below and above rather than an image of breaking.

We keep 折. The chapter's engine is physical from the first line (a corpse, a green stem, a dry stick), and 折 is the physics; 兵 imports an agent. And 兵 would repeat the character from the clause immediately before it, 兵強則不勝, which reads as transmission rather than design. Logged because this is the fifth place our base departs from a reading in the Siku 王弼 (see Ch 2, 68, 69, 73, 74).

### Ch 80 · 什伯之器 — a fifth Siku-flagged 人

Our base reads 什伯之器 (*shí bǎi zhī qì* — "ten- and hundred-fold tools"). The Siku compilers note inside 王弼's own text that 河上公's edition **and all editions** carry a 人 (*rén* — person) there: 〔案什伯下河上公注本及各本俱有人字〕. 河上公's lemma splits at that seam and confirms it. We keep the base; nothing in the English turns on it, since both readings mean tools that stand in for many hands. Recorded in `sources/variants.yaml`, with the fuller point that 河上公 takes his 人 somewhere 王弼 does not — 器謂農人之器, the tools are the *farmers'*, and 不用 is the state declining to requisition them and their season.

### Ch 16 · 致 / 至 — the opening couplet's fork is about agency

Our base reads 致虛極 (*zhì xū jí*). 致 (*zhì*) is 夊 (*suī* — a dragging foot) beneath 至 (*zhì* — to arrive); 說文解字: 送詣也, *"to send all the way there."*

**河上公 (*Héshàng Gōng*) reads 至虛極**, with the plain 至 — and his gloss keeps it: 得道之人捐情去欲，五內清淨，**至於虛極** — *"one who has gained the Tao sheds feeling and casts off desire; the five viscera are clear and still; and so **arrives at** the far end of empty."*

**The fork is about who is doing what.** 致 has someone carrying the emptying to its far point. 至 has them simply arriving there. It is the difference between a practice performed on yourself and a state you come to.

**Our call: the base, and an English with no object supplied.** *"Go totally empty"* is true to both readings rather than picking one, and it avoids the trap either way: every candidate object is imported. 河上公 supplies 五內 (*wǔ nèi* — the five viscera), chapter 3 supplies 其心 (*qí xīn* — their heart), and chapter 16 has neither. The Chinese elides the object in both lines of the couplet, and so does the English.

*Guodian (~300 BCE) carries this couplet and nothing else from the chapter — bundle A, unit A.3, standing alone as its own slip-unit. The chapter's later movement through 常 (*cháng* — the ever-present) is not attested there.*

### Ch 16 · 觀復 / 觀其復 — our base is alone again, and the English had supplied it anyway

河上公's lemma reads 吾以觀**其**復, with 其 (*qí* — their). The Siku editors say so inside our own 王弼 text and go further: 〔案觀下河上公注本及各本俱有其字〕 — *"below 觀, Heshang Gong's commentary edition **and all editions** have the character 其."*

So our base is the only witness without it — the mirror of Ch 23's 故, where our base was the only witness *with* one.

The sense is unchanged, so this is not a meaning-bearing fork. It is recorded because the English had been quietly rendering a character our base does not print: *"I observe **their** return."* Whatever replaces that line should either drop the possessive or take the 其 deliberately, rather than by accident. Recorded in `sources/variants.yaml`.

### Ch 51 · 莫之命 / 莫之爵 — a conferral, or an order

Our vendored 王弼 (*Wáng Bì*) prints 命並作爵 beneath 夫莫之命而常自然 — *"命 is written 爵 (jué — to confer a noble rank) [in other editions]"* — and the Siku editors flag the line itself as suspect: 〔案此句疑係命字下原校注語誤作弼注〕, *"this clause is suspected to be a collation note under the character 命, mistakenly taken as Wang Bi's comment."*

**The fork matters.** 命 (*mìng*) issues an order; 爵 (*jué*) confers a rank — its graph is the bronze ceremonial wine-vessel used in investiture. 夫莫之命而常自然 is *"with no one ordering it, it is always so of itself"*; 夫莫之爵而常自然 is *"with no one **ennobling** it…"* — and the line's subject is 道之尊，德之貴 (*"the Tao's being revered, integrity's being valued"*), which is about **status conferred**, not instructions given. The variant fits the sentence better than our base does.

**Our call: the base**, because the reading is transmitted only through a collation note whose own status the Siku editors doubt, and because no edition is named for it — the same reason the Ming facts at Ch 38 and Ch 23 stayed out of `sources/variants.yaml` under a witness id. It is recorded as a fact about our vendored text, with `wangbi_collation` rather than a witness name.

**Why it is worth keeping.** It is independent evidence for 命's **conferral** sense against its command sense, which is the open question in `glossary/ming-命.md` — and ch 51 currently renders 命 as *commands*, which is 令 (*lìng*)'s English in the identical 莫之X而 frame at ch 32.

### Ch 35 · 安平太 — three characters, three witnesses, and 太 never stands alone

Our base reads 安平太 (*ān píng tài*). The Siku editors flag the spot inside 王弼 (*Wáng Bì*)'s own text: 〔案平太，河上公注本作太平，永樂大典作平泰〕 — *"as for 平太: 河上公 (*Héshàng Gōng*)'s annotated edition reads 太平; the 永樂大典 (*Yǒnglè Dàdiǎn*, the Ming encyclopaedia of 1408) reads 平泰."* Three witnesses, three orders.

**王弼 declines to gloss it at all.** His comment on the line covers only 不害 (*bù hài* — not harmed): 無形無識，不偏不彰，故萬物得徃而不害妨也 — *"formless and unknowable, not partial and not conspicuous; so the countless things can go to it and are not harmed or hindered."*

**河上公 parses it in two, and names the Han term.** 則國安家寧而致太平矣 — *"then the state is 安 (at rest) and the household 寧 (níng — at peace), and it arrives at 太平."* 太平 (*tài píng* — Great Peace) is loaded: the 太平經 (*Tàipíng Jīng* — Scripture of Great Peace) and the 太平道 (*Tàipíng Dào* — Way of Great Peace, the Yellow Turban movement of 184 CE). 河上公 is a Han text and this is a Han reading.

**Our call: the base, and no Han term in the English.** The instability is itself the finding. 太 (*tài*) has **no 說文解字 entry** — it did not yet exist as a separate graph when 許慎 (*Xǔ Shèn*) wrote c. 100 CE, who has only 大 (*dà* — big) and 泰 (*tài*) 滑也, *"smooth."* And 太 appears three times in this book: 太上 (*tài shàng* — the highest, ch 17), 太牢 (*tài láo* — the great sacrificial feast, ch 20), and here. **It never stands alone.** So 安平太 is 安平 plus an intensifier, not a list of three — which is why the third slot is exactly where the scribes disagree. Rendered *"at rest, utterly even."*

### Ch 35 · 用之不可既 / 不足既 — whether the closing frame breaks

Our base reads 用之不可既 (*yòng zhī bù kě jì*). **Our vendored 王弼 lemma reads 用之不足既**, with the Siku editors noting 〔案足，河上公注本及各本俱作可〕 — *"as for 足: 河上公's annotated edition and all editions write 可."* Our base agrees with everyone except the Siku 王弼.

**The fork decides the shape of the whole close.** With 足 the three lines run unbroken — 視之不**足**見／聽之不**足**聞／用之不**足**既, *"not enough to see / not enough to hear / not enough to use up."* With 可 the third line breaks the frame: the first two say there is **not enough of it**, the third says it **cannot be done**.

**Our call: the base, and the English keeps the break.** 王弼's own commentary uses 不可 — 乃用之不可窮極也, *"thus using it cannot be exhausted to its limit"* — which argues the 足 in his lemma is transmission rather than his reading. The break is also the point: two lines of deficiency, then a reversal. *"There is not enough to see. There is not enough to hear. Use it. It never runs out."*

### Ch 11 · 埏 / 挻 — the 說文 sides with the minority graph

Our base reads 埏埴以為器 (*yán zhí yǐ wéi qì* — "work the clay to make a vessel"). The Siku editors note inside 王弼's text: 〔案埏各本俱作埏，惟釋文作挻〕 — *"all editions write 埏; only the 釋文 writes 挻."* The 釋文 is 陸德明 (*Lù Démíng*)'s 經典釋文 (*Jīngdiǎn Shìwén* — Textual Explanations of Classics and Canons), c. 583.

**Not meaning-bearing** — every reading gives *work the clay*, and the English is unaffected. Recorded because the evidence runs against our base graph. **說文解字 glosses 埏 as 八方之地也** — *"the land of the eight directions,"* the far reaches of the earth — with no kneading sense at all; **挻 (*shān*) is the graph that carries it.** 河上公 (*Héshàng Gōng*) takes the working sense on the majority graph regardless: 埏，和也 — *"埏 means to blend."* We keep the base and render *knead*.

*A second Siku note on this chapter — 〔案永樂大典無也字〕, "the 永樂大典 (Yǒnglè Dàdiǎn) lacks the character 也" — is orthographic and is not recorded.*

### Ch 36 · 韓非's text — 邦 for 國, and only three clauses of four

**韓非 (*Hán Fēi*, d. 233 BCE) reads 邦之利器** where our base has 國之利器. 邦 (*bāng* — a state) is the older word; 國 (*guó*) displaced it under the Han taboo on the personal name of 劉邦 (*Liú Bāng*, d. 195 BCE), the founder of the dynasty. **Our base therefore carries a Han substitution at this line, and 韓非 predates the taboo by a lifetime.** Not meaning-bearing — both are the state — but it dates the transmission, and the same substitution will be found wherever 邦 would be expected.

**He quotes three clauses of the four**, in a different order: 翕/張, 弱/強, 取/與 — and no 廢/興 (*fèi / xīng* — to bring down / to raise up). He also reads 翕 (*xī*) for our 歙 and **取 (*qǔ* — to take) for our 奪 (*duó* — to seize)**, which is a real difference of force: 奪 is 說文 手持隹失之也, *"a hand holding a bird and losing it"* — a snatching-away — where 取 is a plain taking.

**We keep all four clauses and the base graphs.** 韓非 is quoting the Laozi to illustrate two historical episodes — Yue's undoing of Wu, and Duke Xian's raid on Yu — not reproducing a text, so his silence on 廢/興 is weak evidence for absence. It is recorded because he is the oldest witness that exists and because the three he does quote, he quotes exactly.

### Ch 36 · 柔弱勝剛強 — one claim of four terms, or two of two

The Siku editors note inside our 王弼: 〔案永樂大典作柔勝剛弱勝强〕 — *"the 永樂大典 (Yǒnglè Dàdiǎn, 1408) reads 柔勝剛，弱勝強."* That splits *"the soft-and-weak overcomes the hard-and-strong"* into two paired claims: *"the soft overcomes the hard; the weak overcomes the strong."*

**韓非 supports the split** by quoting only half of it as a saying in its own right: 處小弱而重自卑損，謂「弱勝強」也 — *"to dwell in the small and weak and make much of humbling and diminishing oneself: this is what 'the weak overcomes the strong' means."*

**Our call: the base.** But the English renders it as two matched pairs regardless — *"The soft and yielding overcome the hard and strong"* — because 柔 (*róu*), 弱 (*ruò*), 剛 (*gāng*) and 強 (*qiáng*) are used separately everywhere else in the book, and binding them into two compounds in English would claim more than our own glossary does. 弱 and 強 are both locked; 剛 is still owed a mention (`WORKLIST` T4-4).

### Ch 39 · 故致數譽無譽 — we depart from the base, and our own 王弼 says why

**Our base reads 譽 (*yù* — praise). Our vendored 王弼 prints 輿 (*yú* — a carriage-body) and the Siku editors say the base's character is a mistake:** 〔案兩輿字，河上公注本作車，釋文作輿，**原本誤作譽**，今據釋文校改〕 — *"the two 輿 characters: 河上公's annotated edition writes 車 (chē — cart); the 釋文 (Lù Démíng, c. 583) writes 輿; **the original mistakenly wrote 譽**, now emended according to the 釋文."*

**Both commentaries explain a vehicle. Neither explains praise.**

- 王弼: 故致數輿乃無輿也 — *"so, counting the carriage through, there is then no carriage."*
- 河上公: 致，就也。言人就車數之，為輻、為輪、為轂、為衡、為轝，**無有名為車者**，故成為車 — *"致 means to go up to. If a person goes up to a cart and counts it out — spokes, wheel, hub, yoke, body — **there is nothing among them named 'cart'**; and so it comes to be a cart."*

**A commentator's gloss is evidence for what stood in his text**, and this is the rare case where that evidence points away from our base. The graphs are near-twins — 譽 is 言 (*yán* — speech) over 與; 輿 is 車 (*chē* — cart) within 舁.

**And 河上公's cart is not isolated.** Two lines earlier he reads 不轂 for our 不穀 (below), so **his close is a cart twice.** Rendered *"count the parts of a cart, and there is no cart,"* which lands chapter 11's image: 轂 is 說文 輻所凑也, *"what the spokes converge on."*

*The source table had already noticed the alternative and dismissed it in a parenthesis — "some texts translate this as 'taking a chariot apart leaves no chariot,' but 'highest praise is no praise' fits the vanity metaphor better" — with no evidence and no log. Shalom found it by asking where the word* highest *came from: there is no 上, 下 or 高 in the line.*

### Ch 39 · four more forks, from the Siku notes and 河上公's lemmas

**其致之 / 其致之一也.** 〔案各本致之下有一也二字，焦竑云開元本無〕 — *"all editions have the two characters 一也 after 致之; 焦竑 (Jiāo Hóng, 1540–1620) says the 開元 (Kāiyuán, 713–741) edition lacks them."* Not meaning-bearing; recorded because our base sides with the Tang edition against everyone else.

**侯王無以貴高 / 無以貞貴高.** 〔案各本以下有貞字〕 — *"all editions have 貞 below 以."* **Meaning-bearing, and it decides the chapter's shape.** With 貞 the sixth pair mirrors its own positive half (為天下**貞** / 無以**貞**) and the series runs six for six. **We keep the base, because the break is the hinge** — 貴高 (*guì gāo* — prized and high) is exactly what the next two lines pick up in 故貴以賤為本，高以下為基. The series stops mirroring at the point where the chapter turns from cosmology to rank. `WORKLIST` T3-6.

**為天下貞 / 為天下正.** 河上公 reads 正 (*zhèng* — upright) and glosses 為天下平正, *"be the world's level-and-upright."* 貞 is 說文 卜問也 — *"to inquire by cracking a shell"* — divination, hence what is consulted, hence steadfast. We keep 貞 and render *true for the world*, in the carpenter's sense. *(正 sits inside the deferred 正/奇 question, T4-2, which this does not touch.)*

**不穀 / 不轂.** 河上公 reads 不轂 (*"not a hub"*) and glosses 不轂喻不能如車轂為衆輻所湊 — *"being unable to be like a cart's hub, on which the many spokes converge."* 穀 and 轂 share the phonetic 𣪊. We keep the base, where 孤 (*gū* — orphaned), 寡 (*guǎ* — alone) and 不穀 are three self-deprecations of rank, which is what the passage argues.

### Ch 13 · 寵為下 / 辱為下 — which half of the pair is the low one

Our base reads 寵為下 (*"favor is the lower position"*). **河上公's lemma reads 辱為下** and glosses it 辱為下賤 — *"disgrace is low and cheap."*

**Meaning-bearing, and it decides whether the line says anything.** With 辱 it is the ordinary observation that disgrace degrades you, which the chapter has already said. **With 寵 it is counter-intuitive and is the chapter's whole argument**: to be favored is to be marked as the inferior party, because favor comes down from someone above — so it shakes you exactly as disgrace does.

**王弼 supports the base** by treating the two as one condition: 寵必有辱，榮必有患。驚辱等，榮患同也 — *"favor necessarily carries disgrace, glory necessarily carries trouble; being startled and being disgraced are equivalent, glory and trouble are the same."* We keep the base.

*Guodian (~300 BCE) attests this chapter — bundle B, unit B.1 — but no Guodian reading of any line here is recorded; see `sources/PROVENANCE.md` for why this repository holds no transcription of those slips.*

### Ch 13 · 若可 / 則可以 / 乃可以 — a particle, and what our own table made of it

Two Siku notes: 〔案若可寄，永樂大典作則可以寄，河上公注本作則可寄於天下〕 and 〔案若可託，永樂大典作乃可以託，河上公注本作乃可以託於天下〕. **Every variant is a consequential particle** — 則可以 and 乃可以 both mean *"then may"* — so the sense is unchanged.

Recorded because **our source table glosses 若 here as *seems*** (*"Seems they can be entrusted"*), which would soften the claim into a hedge. **No witness and neither commentator reads it that way**: 王弼 如此**乃可以**託天下也, 河上公 **則可**寄於天下. The English takes the consequence and drops the particle.

---

## The 韓非 harvest — 2026-09-10

*`WORKLIST.md` R1. The importer had marked **35 divergent lemmas across 14 chapters** since the library was vendored, and nobody had read them. Four are meaning-bearing and are recorded below; three more are in `sources/variants.yaml` with the base kept; three were already logged. **The remaining 25 are orthographic or grammatical** — graph variants (爲/為, 脩/修, 牗/牖, 闚/窺, 翕/歙, 衆/眾, 知/智, 奚/何) and 韓非's systematically fuller particles, sentence-final 也 · 矣 · 乎 and inserted 之 · 於 · 其. That is a property of a pre-Qin recension punctuated by particle rather than by mark, not a series of forks, and it is recorded here once so the instances are not re-harvested as findings.*

### Ch 38 · 失道而後德 / 失道而後失德 — a descent, or a cascade

**Our base prints 失 once per clause; 韓非 prints it twice, five clauses running.** 故失道而後德，失德而後仁 against 失道而後失德，失德而後失仁.

**The two texts make different claims.** Ours is a **descent**: lose the Tao, and then there is 德 (*dé* — integrity); lose 德, and then there is 仁 (*rén* — humaneness). Each rung *appears* as the one above it goes, which is why the chapter can be read as an account of how the lesser virtues arise. 韓非's is a **cascade**: lose the Tao and then lose 德, lose 德 and then lose 仁. Nothing appears. Everything is successively forfeited.

**This chapter was rebuilt in Pass D around 失 as its spine** (`WORKLIST` T1-4), on the finding that 失 has five occurrences here — more than in any chapter in the book — and had been deleted from its hinge. The English reads *"So when the Tao is lost, then integrity."* **The oldest witness says the second half is a loss too.**

**Undecided.** The decision changes five lines and reopens settled work, so it goes to Shalom rather than being taken here.

### Ch 64 · 輔 / 恃 — the sage supports 自然, or leans on it

以**輔**萬物之自然 against 韓非's **恃**萬物之自然. 輔 (*fǔ* — to assist; a cart's side-brace) against 恃 (*shì* — to lean your weight on).

**Our call: the base, and the argument is internal.** 恃 is locked here (`glossary/shi-恃.md` — *"the heart putting its weight on something"*), and the book's own formula 為而不恃 (*wéi ér bù shì* — "acts and does not rely on it") at chapters 2, 10, 51 and 77 makes 恃 **something the sage does not do.** 韓非's reading would have the sage 恃 approvingly, on the one line in the book where that is praised — which is possible, and is exactly the kind of thing a pre-Qin reader might have found unremarkable, but it cuts against four other chapters. We keep 輔 and record the older reading.

### Ch 58 · 劌 / 穢 — cut, or sullied

廉而不**劌** against 韓非's 廉而不**穢**. 劌 (*guì* — to cut, to wound) is built on 刀 (*dāo* — knife); 穢 (*huì* — filthy, weed-choked) on 禾 (*hé* — grain).

**Our call: the base, on the parallel.** The line sits in a four-beat series — 方而不割 · 廉而不劌 · 直而不肆 · 光而不耀 — in which **every member pairs a property with the harm it declines to do**: square but does not cut, edged but does not wound, straight but does not overreach, bright but does not dazzle. 劌 completes that pattern; 穢 breaks it, since being filthy is not a harm an edge does to anything. The two graphs are close enough that a slip is the likely explanation, and it is recorded rather than assumed away.

### Ch 60 · 傷人 / 傷民 — and it is evidence on a deferred call

非其神不傷**人**，聖人亦不傷**人** against 韓非's second clause, 聖人亦不傷**民**.

**韓非's text distinguishes the two clauses where ours flattens them**: the numinous does not harm **people**; the sage does not harm **the governed**. Both recensions have 人 in the first clause, so the divergence is only in the second — which is what makes it interesting rather than noise.

**Undecided, and deliberately so.** 民 (*mín* — the governed) against 人 (*rén* — a person) is one of the three calls Shalom has deferred (`WORKLIST` T4), and this chapter is not the place to settle it. **But it is evidence that the distinction was live in the oldest witness**, rather than a later copyist's variation — which is a fact the deferred call will want when it is taken up.

### An incidental finding: our base is inconsistent on the Han name-taboo

**Ch 54 reads 修之於邦; ch 36 reads 國.** 邦 (*bāng* — state) was tabooed under Liu Bang (劉邦, r. 202–195 BCE) and replaced with 國 (*guó*) in Han-era copying — which is what dates our base to Han hands. Ch 54 appears to have escaped a substitution ch 36 did not. Recorded as a fact about the recension; nothing in the English turns on it, since both render *state*.
