## The Form Audit — the music of the Chinese, and what the English keeps

*A reference and a ledger. It names the formal devices the Chinese is built from, says how this translation carries each one, and records every chapter where the English departs from the form, and why. Consult it at step 6 of `chapter-review`, and whenever a line feels right word by word but wrong as a whole.*

### Why this exists

**To give the highest-fidelity rendering of the original text we can.** Fidelity is not only a matter of words. The Tao Te Ching is built from chains, parallel series, matched couplets, reversals, doubled characters, rhyme and fixed formulas, and much of what it means it says through that structure. Chapter 11's argument is one sentence said three times. Chapter 16's argument is a ladder, each rung standing on the last. An English that renders every word and drops the form has translated a different text.

**So every departure from a form is a conscious decision.** Sometimes English cannot carry a device: Old Chinese rhyme does not survive the trip, and a doubled character often reads as a stammer. Sometimes carrying it would cost the poetry, or the deeper meaning, in modern English. Then we let it go, on purpose, and say so here. **What this audit exists to prevent is the other kind of departure, the one nobody chose.** That kind is invisible at the level of the word: every line can be defensible on its own while the relation between them is gone. `DISCOVERIES.md` §6 is the case that taught it.

**Three verdicts, and the difference between the last two is whether anyone chose:**

| Verdict | Means |
|---|---|
| **Kept** | The English carries the device, in position |
| **Departed** | The English lets the device go, and the reason is recorded here: the trade it made for the poetry or the meaning |
| **Lost** | The English lets the device go and nobody decided it. Bring it to Shalom, one at a time, with a recommendation. It leaves this verdict as *kept* or *departed* |

**What this file is not.** It does not hold the rules. Those live in [`principles/lineation-is-ours.md`](principles/lineation-is-ours.md) (*the marks are ours; the music is the source's*) and [`principles/repeat-yourself.md`](principles/repeat-yourself.md) (*where the Chinese repeats itself, repeat yourself*). It holds the record of how the book meets them. A rendering decision about a word still goes in `notes/translation.md`; this file links there rather than repeating it.

---

### The page: lines, stanzas and marks

**The terms.** A **line** is one line of the English verse. **Lineation** is where the lines break. A **stanza** is a group of lines, and a **stanza break** is the blank line between two stanzas. On disk, a line break is a CommonMark hard break, two trailing spaces, and a stanza break is an empty line.

**The source has none of them.** The ancient text is unbroken columns of characters, with no punctuation and no line breaks. Every comma, full stop (。) and break in a modern edition is an editor's. So lineation, stanzas and punctuation are ours, which is also why the CC0 dedication is clean (`principles/lineation-is-ours.md`). But the source is not formless: it moves in regular character-beats, pairs and series, and the layout should follow that rhythm, not cut across it.

**Our logic for a stanza break:**

1. **Count the beats first.** A series of even phrases gets the same number of lines, laid out alike.
2. **Break where the Chinese turns:** to a new subject, a new formula, a conclusion (故 *gù* — "so"; 是以 *shì yǐ* — "therefore"), or a new speaker.
3. **Never break inside a chain or a series.** A blank line in the middle of a chain cuts the link it exists to make.
4. **Where a chapter shares phrases with another, follow the lineation already settled** (chapters 4 and 56).
5. **Breathing room is a reason, but not the only one.** A break the Chinese does not support is a departure, and goes here with its reason.

**What a break changes downstream.** Blank lines are not counted as lines, so a chapter still pairs line by line with its Chinese. `tools/build_db.py` numbers the stanzas, and `data/atlas-export.json` carries them to the Library and the atlas, so a stanza break is visible to every reader.

**Punctuation.** Ours, used deliberately. The dash is the one mark with a standing rule (`CLAUDE.md` standing rule 5): a dash must not leave a subject unnamed. Whether the verse's existing dashes stay is a call Shalom has deferred (`WORKLIST.md` T4-3).

---

### The devices

*Each with its name in Chinese rhetoric and in English, what it does, how this translation handles it, and its strongest examples. The examples come from the seed scan of 2026-10-25. The full audit (below) reads every chapter.*

#### 1 · The chain — 頂真 (*dǐng zhēn* — "capping"), anadiplosis

**What it is.** The last words of one clause become the first words of the next, so each line stands on the one before it. When the chain climbs step by step toward a conclusion, English rhetoric calls it a **sorites** or **climax**. In Chinese the device is also written 頂針 (*dǐng zhēn* — "thimble").

**Why it matters.** The chain is how the book argues. Chapters 16, 25 and 59 make their case as a ladder, and the claim is the ladder: each step follows from the last. A chain whose links are rendered in the wrong order still repeats its words, but no longer makes the argument.

**How we carry it.** **Position matters, not just repetition.** The repeated words must end one line and open the next. English grammar fights this, because an English possessive or prepositional phrase moves the repeated word: *"the gate of the dark female"* puts *the dark female* last.

| Ch | The Chinese | Our English | Verdict |
|---|---|---|---|
| 6 | 是謂玄牝。玄牝之門 (*shì wèi xuán pìn. xuán pìn zhī mén* — "this is called the dark female. The dark female's gate") | *"This is called the dark female. / The gate of the dark female,"* | **Lost.** The words repeat, but the link moves to the end of the line. See *Chapter 6* below |
| 16 | 歸根曰靜…復命曰常，知常曰明 (*guī gēn yuē jìng… fù mìng yuē cháng, zhī cháng yuē míng* — "returning to the root is called stillness… returning to what is given is called the ever-present, knowing the ever-present is called clear-seeing"), then 容乃公，公乃王 (*róng nǎi gōng, gōng nǎi wáng* — "containing leads to impartiality, impartiality leads to authority") | *"Returning to the root is called stillness. … Containing everything leads to impartiality. / Impartiality leads to supreme authority."* | **Kept**, every link in position, and the two linking verbs held apart: 曰 (*yuē*) *is called*, 乃 (*nǎi*) *leads to*. Departed in tempo only: three-character beats become longer English lines |
| 25 | 大曰逝，逝曰遠，遠曰反 (*dà yuē shì, shì yuē yuǎn, yuǎn yuē fǎn* — "great means departing, departing means far, far means returning") | *"Great means departing, / departing means going far, / going far means returning."* | **Kept** |
| 25 | 人法地，地法天，天法道，道法自然 (*rén fǎ dì, dì fǎ tiān, tiān fǎ dào, dào fǎ zì rán* — "humans model on earth, earth on sky, sky on the Tao, the Tao on being what it is") | *"Humans model themselves on the earth, / Earth models itself on the sky…"* | **Kept** |
| 37 | 萬物將自化。化而欲作 (*wàn wù jiāng zì huà. huà ér yù zuò* — "the countless things will transform of themselves. Transforming, they want to act") | *"the countless things will transform of themselves. / When the countless things urge action"* | **Lost.** 化 (*huà* — transform) drops out of the second line, and the subject is repeated in its place. The next links in the chapter hold |
| 42 | 道生一，一生二，二生三，三生萬物 (*dào shēng yī, yī shēng èr, èr shēng sān, sān shēng wàn wù* — "the Tao births one, one births two, two births three, three births the countless things") | *"The Tao births the one, the one births the two…"* | **Kept** |
| 59 | 夫唯嗇，是謂早服；早服謂之重積德 (*fū wéi sè, shì wèi zǎo fú; zǎo fú wèi zhī zhòng jī dé* — "only conserving is called accepting early; accepting early is called a heavy store of integrity"), and four links more | *"Only conserving is called accepting early, / accepting early is called a heavy accumulation of integrity…"* | **Kept**, every link in position |

**Also kept:** ch 1 (玄之又玄 *xuán zhī yòu xuán* — "dark, and dark again"), 21, 23, 28 (×3), 30 and 55, 48, 52, and 15.

#### 2 · The series — 排比 (*pái bǐ* — "arranged in a row"), isocolon

**What it is.** Three or more clauses on one frame, with only one slot changing.

**Why it matters.** The reader is meant to hear the frame repeat and feel the changing word click into it. A series rendered with varied wording reads as a list of separate claims.

**How we carry it.** Same frame, same English, one line per member. This is the device the book's tooling now watches best: `concordance.py --formulas N` prints every frame in a chapter beside its English.

| Ch | The frame | Verdict |
|---|---|---|
| 11 | 當其無，有▢之用 (*dāng qí wú, yǒu ▢ zhī yòng* — "right where its absence is, there is the ▢'s use") ×3 | **Kept**, since 2026-09-05 (`DISCOVERIES.md` §6) |
| 2 | ▢▢相▢ (*xiāng* — "each other") ×6 | **Kept** |
| 2 | 而弗▢ (*ér fú* — "and does not") ×4 | **Lost** in one member: three read *"and the sage does not…"*, one *"The sage acts, yet relies on nothing"* |
| 39 | 得一以▢ (*dé yī yǐ* — "got the one, and so") ×6, then its mirror 將恐▢ (*jiāng kǒng* — "is likely to") ×6 | **Kept** |
| 41 | the twelve 建言 (*jiàn yán* — "established sayings"), each ▢若▢ (*ruò* — "seems") | **Kept**, one saying per line. 大白若辱 (*dà bái ruò rǔ* — "great white seems soiled") breaks the 大 (*dà* — great) frame as *"The whitest white"* |
| 45 | 大▢若▢ (*dà ▢ ruò ▢* — "great ▢ seems ▢") ×5 | **Kept** |
| 56 | 不可得而▢ (*bù kě dé ér* — "cannot be made to ▢") ×6 | **Lost** in part: the three couplets survive, the six-fold frame folds into one *cannot* and *neither… nor* |

**Also kept:** ch 8's 善 (*shàn* — masterful at) ×7, ch 10's six questions, ch 15's ▢兮其若▢ (*▢ xī qí ruò ▢* — "▢, like ▢") ×7, ch 19, 30, 36, 54, 57 and 67.

#### 3 · The couplet — 對偶 (*duì ǒu* — "a matched pair"), parallelism and antithesis

**What it is.** Two clauses of the same length and shape that answer each other, often as opposites.

**How we carry it.** The two halves share one English for each shared character, so the pair still answers itself.

| Ch | The pair | Verdict |
|---|---|---|
| 33 | 知人者智，自知者明 (*zhī rén zhě zhì, zì zhī zhě míng* — "one who knows others is clever, one who knows themselves sees clearly") | **Kept** |
| 40 | 反者道之動，弱者道之用 (*fǎn zhě dào zhī dòng, ruò zhě dào zhī yòng* — "returning is the Tao's movement, yielding is the Tao's use") | **Kept** |
| 48 | 為學日益，為道日損 (*wéi xué rì yì, wéi dào rì sǔn* — "pursuing learning, increase daily; pursuing the Tao, decrease daily") | **Kept** |
| 64 | 為者敗之…無為故無敗 (*wéi zhě bài zhī… wú wéi gù wú bài* — "those who do it ruin it… not doing, so no ruin") | **Lost.** 為 (*wéi* — do) reads *handle* in one half and *do* in the other: *"Those who handle it ruin it"* against *"the sage does not do, and so ruins nothing"* |
| 22 · 24 | the two chapters mirror four pairs | **Lost** in one: 彰 (*zhāng* — to shine forth) reads *"their rightness shows"* at 22 and *"convince no one"* at 24 |

**Also kept:** ch 3, 52 (塞其兌 / 開其兌, *sāi qí duì / kāi qí duì* — "block the openings / open the openings") and 76.

#### 4 · The reversal — 回文 (*huí wén* — "returning text"), chiasmus

**What it is.** A pair whose second half reverses the first, A B / B A. Its larger cousin is **ring composition**: a chapter that ends where it began.

| Ch | The reversal | Verdict |
|---|---|---|
| 81 | 信言不美，美言不信 (*xìn yán bù měi, měi yán bù xìn* — "trustworthy words are not pretty, pretty words are not trustworthy"), and two more pairs | **Kept**, all three |
| 56 | 知者不言，言者不知 (*zhī zhě bù yán, yán zhě bù zhī* — "those who know do not speak, those who speak do not know") | **Kept** |
| 21 | 惚兮恍兮 / 恍兮惚兮 (*hū xī huǎng xī / huǎng xī hū xī* — "elusive, vague / vague, elusive") | **Kept** |
| 58 | 禍兮福之所倚，福兮禍之所伏 (*huò xī fú zhī suǒ yǐ, fú xī huò zhī suǒ fú* — "disaster, where fortune leans; fortune, where disaster hides") | **Kept** |
| 52 | 得其母…知其子；知其子…守其母 (*mǔ* — mother; *zǐ* — child) | **Kept** |
| 71 | 知不知，上；不知知，病 (*zhī bù zhī, shàng; bù zhī zhī, bìng* — "knowing not-knowing, highest; not knowing knowing, sickness") | **Lost** in part: *"To not know yet claim to know"* adds words that blur the mirror |
| 22 | ring: 曲則全 (*qū zé quán* — "bend and be whole") opens the chapter and is quoted at its close | **Kept** |

#### 5 · The same word turned — polyptoton

**What it is.** One character used twice in different roles, often a word set against its own negation. There is no single standard name for it in Chinese rhetoric; English calls it **polyptoton**, or **figura etymologica** when a verb takes its own noun.

| Ch | The figure | Verdict |
|---|---|---|
| 14 | 無狀之狀 (*wú zhuàng zhī zhuàng* — "the shape of no shape") | **Kept**: *"the shape of no-shape"* |
| 38 | 上德不德 (*shàng dé bù dé* — "high integrity does not integrity") | **Kept** |
| 71 | 病病 (*bìng bìng* — "to sicken of sickness") | **Kept**: *"sick of the sickness"* |
| 1 | 道可道 (*dào kě dào* — "the Tao that can be tao-ed") | **Departed**, a recorded choice: the verb 道 (*dào* — to lay out, to tell) becomes *made a way*, so the line reads *Tao · way · Tao* (`chapters/001.md`, notes) |
| 63 | 為無為，事無事，味無味 (*wéi wú wéi, shì wú shì, wèi wú wèi* — "do not-doing, serve not-serving, taste not-tasting") | **Lost** in the third: *"taste the flavorless"* breaks the pattern of the first two |
| 64 | 欲不欲 / 學不學 (*yù bù yù / xué bù xué* — "want not-wanting / learn not-learning") | **Lost** in the second: *"learns to unlearn"* beside *"wants the not-wanting"* |

#### 6 · The doubled character — 疊字 (*dié zì* — "stacked characters"), reduplication

**What it is.** One character said twice, for sound and intensity: 綿綿 (*mián mián* — unbroken, unbroken).

**How we carry it.** Mostly we do not, and **that has never been decided.** A doubled English word often reads as a stammer, so this may well become a recorded *departure* book-wide. Until Shalom rules, each one is *lost*.

| Ch | The doubling | Our English |
|---|---|---|
| 6 | 綿綿 (*mián mián* — unbroken) | *"Unceasing"* |
| 14 | 繩繩 (*shéng shéng* — cord upon cord, endless) | *"Continuously flowing"* |
| 16 | 芸芸 (*yún yún* — teeming) | *"Things come to their fullest"* |
| 20 | six: 熙熙 (*xī xī* — merry), 傫傫 (*léi léi* — listless), 沌沌 (*dùn dùn* — muddled), 昭昭 / 昏昏 (*zhāo zhāo / hūn hūn* — bright / dim), 察察 / 悶悶 (*chá chá / mèn mèn* — sharp / dull) | single words; the contrasts survive, the doubling does not |
| 58 | 悶悶 (*mèn mèn* — dull), 淳淳 (*chún chún* — simple), 察察 (*chá chá* — sharp), 缺缺 (*quē quē* — lacking) | **Departed** in a way that may be the answer: two words for one doubled character, *"dull and undiscerning," "pure and honest," "sharp and prying"*. The fourth breaks it: *"turn cunning"* |

**Also:** ch 39 (琭琭 / 珞珞, *lù lù / luò luò* — gleaming like jade / rough like stone), 49 (歙歙, *xī xī* — drawing in), 73 (恢恢, *huī huī* — vast).

#### 7 · Rhyme — 押韻 (*yā yùn*)

**What it is.** Much of the Tao Te Ching rhymes in Old Chinese, the pronunciation of its own era, though the rhymes are often lost in modern Mandarin.

**How we carry it.** We do not, anywhere, and **that has never been decided either.** English rhyme forced onto this text would cost more than it carries, so this is likely to become a recorded *departure* book-wide. But it should be decided, and where a chapter's rhyme binds lines together, that binding is evidence for its stanza shape.

**Only one claim is made here so far.** Chapter 6's 門 (*mén* — gate), 根 (*gēn* — root), 存 (*cún* — exist) and 勤 (*qín* — strain) fall in one traditional rhyme group, 文 (*wén*), which binds its last four lines. **Every other rhyme claim waits on a source.** The one to use first is Jiang Yougao's 老子韻讀 (*Lǎozǐ yùn dú* — "rhyme readings of the Laozi," Qing dynasty, public domain). The modern cross-check is William Baxter, "Situating the Language of the *Lao-tzu*" (1998), consulted for facts about sound, never for phrasing.

#### 8 · The formulas

**What they are.** Fixed phrases the book uses again and again, like a refrain. Each should read the same every time, so the reader hears it as one formula.

| Formula | How we carry it | Where it slips |
|---|---|---|
| 是謂 (*shì wèi* — "this is called") | *this is called* | **Lost** at ch 13 (*"This is what is meant:"*), 14 (*"This is the shape of no-shape"*), 27, 53 and 74, and **dropped** twice at ch 78 (是謂社稷主 *shì wèi shè jì zhǔ* — "this is called lord of the altars of soil and grain" → *"is the keeper of the soil and the grain"*). Some may be licensed; each needs a verdict |
| 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") and 故 (*gù* — "so") | *Therefore, the sage* and *So the sage*, both | The two connectives are not held apart: ch 57's 故聖人云 (*gù shèng rén yún*) reads *"Therefore the sage says:"* and ch 78's 是以聖人云 (*shì yǐ shèng rén yún*) reads *"So the sage says:"*, the mapping reversed. Wants one book-wide decision |
| 吾何以知…以此 (*wú hé yǐ zhī… yǐ cǐ* — "how do I know… by this") | *How do I know … is so? By this.* | **Kept** at 21, 54 and 57 (`notes/translation.md` → 以此) |
| 夫唯 (*fū wéi* — "only because") | *Only because…* | **Kept** at 2, 8, 15, 22, 67 and 71 |
| refrains across chapters: 沒身不殆 (*mò shēn bù dài* — "to the end of your days, no danger", 16 · 52), 知常曰明 (*zhī cháng yuē míng* — "knowing the ever-present is called clear-seeing", 16 · 55), 無為而無不為 (*wú wéi ér wú bù wéi* — "non-doing, yet nothing left undone", 37 · 48) | one English each | **Kept** |

#### 9 · The sung pause and the question — 兮 (*xī*) and 乎 (*hū*)

**What they are.** 兮 is a breath-particle from sung verse, a held pause with no meaning of its own. 乎 marks a question, often one that answers itself.

**How we carry them.** 兮 has no English word, so it is **departed** throughout, carried by the layout instead: a bare adjective and a comma (ch 4's *"Fathomless,"*, ch 15's *"Careful, like…"*), or full stops (ch 25's *"Silent. Empty. Solitary. Unchanging."*). Twice at ch 20 it becomes an exclamation (*"How muddled!"*). The reason should be written once, here, when the full audit reaches chapter 4. 乎's questions are **kept** at 10, 15, 44 and elsewhere. At ch 20, 相去 (*xiāng qù* — "how far apart") ×2 reads *"how much distance?"* and then *"how far apart?"*, **lost**.

#### 10 · The reversed saying — 正言若反 (*zhèng yán ruò fǎn*), paradox

**What it is.** The book names its own method at ch 78: *"Words on the mark seem like their opposite."* The soft overcomes the hard; the one who puts themselves last comes first.

**How we carry it.** The paradox must stay sharp: no softening word that resolves it. 若 (*ruò* — seems) reads *seems* throughout chs 41 and 45, and ch 7's 後其身而身先 (*hòu qí shēn ér shēn xiān* — "puts their body last, and their body comes first") keeps its turn. **Kept**, so far as the seed scan read.

---

### Chapter 6 — the first entry

*The chapter that opened this file, 2026-10-25.*

**Its devices.** Three couplets, each one sentence: 谷神不死，是謂玄牝。(*gǔ shén bù sǐ, shì wèi xuán pìn* — "the valley spirit does not die, this is called the dark female") · 玄牝之門，是謂天地根。(*xuán pìn zhī mén, shì wèi tiān dì gēn* — "the dark female's gate, this is called the root of sky and earth") · 綿綿若存，用之不勤。(*mián mián ruò cún, yòng zhī bù qín* — "unbroken, it seems to exist; use it, and there is no strain"). Across them run a **chain** (玄牝 *xuán pìn* — "the dark female" ends the first couplet and opens the second), the **formula** 是謂 (*shì wèi* — "this is called") twice, a **doubled character** (綿綿 *mián mián*), and a **rhyme** binding the last four lines: 門 根 存 勤 (*mén gēn cún qín* — gate, root, exist, strain).

**What the English did.** *"This is called the dark female. / The gate of the dark female,"* kept the repeated words and lost the chain: the English *of* moved *the dark female* to the end of the line, so the link where one line hands its last words to the next was gone. The formula is kept both times. The doubling is lost (*"Unceasing"*), and so is the rhyme.

**The proposal.** *Shalom's draft, 2026-10-25, not yet applied:*

> The spirit of the valley is deathless.  
> This is called the dark female.  
> The dark female's gate –  
> this is called the root of sky and earth.
>
> Unceasing yet barely perceptible,  
> use it, and there is no strain.

- **The chain, kept.** *The dark female's gate* opens on the words the line before it ended on, in the Chinese order: 玄 (*xuán* — dark) 牝 (*pìn* — female) 之 (*zhī* — 's) 門 (*mén* — gate). It also names her twice and ties the gate to her, which is what the 2026-10-24 ruling on this line asked for.
- **The stanza break, 4 / 2.** The first four lines name the thing twice with 是謂 and hold the chain inside one stanza. The last two turn to how it is used. The break cuts only the rhyme that ties 根 (*gēn* — root) to 存 (*cún*) and 勤 (*qín*), which the English does not carry anyway. *(Three couplets, 2 / 2 / 2, were considered and set aside: they put a blank line in the middle of the chain.)*
- **The dash.** It does not strand a subject: *this* picks it straight back up, as the Chinese 是 (*shì* — this) points back at its topic. Chapters 10 and 51 use the same mark in the same formula: *"growing them without ruling them – / this is called profound integrity."* The book's dashes as a whole remain Shalom's deferred call, `WORKLIST.md` T4-3.
- **The cost.** Chapter 1's 眾妙之門 (*zhòng miào zhī mén*) reads *"the gate of all subtleties,"* so 之門 (*zhī mén* — "'s gate") takes two shapes in the book. Chapter 6 has a chain to keep, and chapter 1 does not.

**Verdict:** chain *lost*, to be *kept* when the draft is applied. Doubling and rhyme *lost*, awaiting the book-wide decisions in §6 and §7.

---

### The full audit

*Owed: `WORKLIST.md` R4. Every chapter read for its forms, one at a time, in order.*

**How to read a chapter:**

1. Run `python3 tools/concordance.py --formulas N`. It lists every series, frame and repeat the chapter holds, with its English underneath.
2. Read the Chinese aloud in pinyin, and name every device from the list above that it uses.
3. For each device, give a verdict: *kept*, *departed* (with the reason), or *lost*.
4. Bring each *lost* to Shalom, one at a time, with a recommendation. Record what he decides: a fix goes in the chapter and `notes/translation.md`, and a departure gets its reason here.
5. Fill in the chapter's row below.

**The ledger.** *Devices noted* comes from the seed scan and is a starting point, not a reading. A chapter is **read** only once someone has worked through steps 1–5.

| Ch | Devices noted | Read | Open |
|---|---|---|---|
| 1 | chain, polyptoton | ⬜ | |
| 2 | series ×2, rhyme, only because | ⬜ | does-not series |
| 3 | couplet, therefore the sage | ⬜ | |
| 4 | sung pause, shares lineation with 56 | ⬜ | |
| 5 | question | ⬜ | |
| 6 | chain, this is called, doubling, rhyme | 🔶 | chain (draft), doubling, rhyme |
| 7 | paradox | ⬜ | |
| 8 | series, only because | ⬜ | |
| 9 | | ⬜ | |
| 10 | series of questions, this is called, dash | ⬜ | |
| 11 | series | ⬜ | |
| 12 | | ⬜ | |
| 13 | refrain, this is called, question | ⬜ | this is called |
| 14 | doubling, polyptoton, this is called | ⬜ | this is called, doubling |
| 15 | sung-pause series, chain, question, only because | ⬜ | |
| 16 | chain (sorites), doubling, refrain, rhyme | ⬜ | doubling |
| 17 | | ⬜ | |
| 18 | | ⬜ | |
| 19 | series | ⬜ | |
| 20 | doubling, sung pause, question | ⬜ | doubling, how far apart |
| 21 | chain, reversal, sung pause, by this | ⬜ | |
| 22 | ring, mirror of 24, only because, question | ⬜ | shine forth |
| 23 | chain, question | ⬜ | |
| 24 | mirror of 22 | ⬜ | shine forth |
| 25 | chain ×2, sung pause, rhyme | ⬜ | |
| 26 | | ⬜ | |
| 27 | this is called | ⬜ | this is called |
| 28 | chain ×3 | ⬜ | |
| 29 | | ⬜ | |
| 30 | series, chain | ⬜ | |
| 31 | | ⬜ | |
| 32 | | ⬜ | |
| 33 | couplets | ⬜ | |
| 34 | | ⬜ | |
| 35 | | ⬜ | |
| 36 | series, paradox | ⬜ | |
| 37 | chain, refrain | ⬜ | transform chain |
| 38 | polyptoton | ⬜ | |
| 39 | series ×2, doubling, question | ⬜ | doubling |
| 40 | couplet | ⬜ | |
| 41 | series | ⬜ | whitest white |
| 42 | chain | ⬜ | |
| 43 | | ⬜ | |
| 44 | questions | ⬜ | |
| 45 | series, rhyme | ⬜ | |
| 46 | | ⬜ | |
| 47 | | ⬜ | |
| 48 | chain, couplet, refrain | ⬜ | |
| 49 | doubling | ⬜ | doubling |
| 50 | | ⬜ | |
| 51 | this is called, dash | ⬜ | |
| 52 | chain, reversal, couplet, refrain | ⬜ | |
| 53 | this is called | ⬜ | this is called |
| 54 | series, by this | ⬜ | |
| 55 | chain, refrain | ⬜ | |
| 56 | series, reversal, shares lineation with 4 | ⬜ | cannot-be-made series |
| 57 | series, by this, so the sage | ⬜ | so / therefore |
| 58 | reversal, doubling | ⬜ | lacking, doubled |
| 59 | chain (sorites) | ⬜ | |
| 60 | | ⬜ | |
| 61 | | ⬜ | |
| 62 | | ⬜ | |
| 63 | polyptoton | ⬜ | taste the not-tasting |
| 64 | couplet, polyptoton | ⬜ | do / handle, learn not-learning |
| 65 | | ⬜ | |
| 66 | therefore the sage | ⬜ | |
| 67 | series, only because | ⬜ | |
| 68 | this is called | ⬜ | |
| 69 | | ⬜ | |
| 70 | | ⬜ | |
| 71 | reversal, polyptoton, only because | ⬜ | know-not-knowing mirror |
| 72 | therefore the sage | ⬜ | |
| 73 | doubling | ⬜ | doubling |
| 74 | this is called | ⬜ | this is called |
| 75 | | ⬜ | |
| 76 | couplet | ⬜ | |
| 77 | | ⬜ | |
| 78 | paradox, this is called ×2, therefore the sage | ⬜ | this is called ×2, so / therefore |
| 79 | | ⬜ | |
| 80 | | ⬜ | |
| 81 | reversal ×3 | ⬜ | |

**Two book-wide decisions come before most rows can close:** whether doubled characters (§6) and rhyme (§7) are departures by policy. Each is one call for Shalom, and each closes dozens of *lost* verdicts at once.
