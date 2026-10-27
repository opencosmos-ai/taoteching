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

**Punctuation.** Ours, used deliberately. The dash is the one mark with a standing rule (`CLAUDE.md` standing rule 3): the spaced em-dash ( — ), and only where its subject is named on both sides. It often marks the Chinese topic–comment shape, a topic held up and then named again.

---

### Where the list of devices comes from

*Added 2026-10-26, before the second read. The first list (§1–§10) came from a seed scan of this book's own text. This one checks it against what scholarship has already found, so the audit is not inventing the categories as it goes.*

**What the scholarship supplies, and what each source adds here:**

| Source | What it finds in the text | What it adds to this audit |
|---|---|---|
| Rudolf Wagner, "Interlocking Parallel Style: Laozi and Wang Bi," *Études Asiatiques* 34.1 (1980), and *The Craft of a Chinese Commentator* (2000), ch. 3 | A structure of two or more parallel strands, usually lettered a, b and c, running through a passage, often closed by a line that joins them. He finds it in 39 of the 81 chapters (2000, p. 95), with ch 64 as his chief example, and argues Wang Bi read the text this way | §11: a new device, and a new kind of loss — a strand whose English changes, so the reader can no longer follow it |
| Andrej Fech, "Avoiding the Trap of Parallelism: Interlocking Parallel Style in the Interpretation of Laozi 29," *Religions* 13.9 (2022) | Tests the strands on ch 29, and warns that forcing them where the text does not hold them misreads it | §11's rule of restraint: a strand is claimed only where its words visibly recur |
| Liu Xiaogan, *Laozi: niandai xinkao yu sixiang xinquan* (*Laozi: A New Study of Its Date and Thought*), and *Laozi gujin* (*The Laozi Past and Present*) | Compares the Laozi's verse with the Book of Odes and the Songs of Chu, finds it closer to the Odes, and treats the chain, the ring, and **rings between chapters** as its devices | Confirms §1 and §4, and makes the cross-chapter formulas (§8, `WORKLIST.md` T3-17) a device in their own right, not a tidiness rule |
| William Baxter, "Situating the Language of the *Lao-tzu*," in Kohn and LaFargue, eds., *Lao-tzu and the Tao-te-ching* (1998) | Rhymed, rhythmic paragraphs, usually built in grammatically parallel pairs of lines; dates the bulk to the mid or early fourth century BCE | Confirms that the couplet is the text's basic unit (§3), and rhyme as evidence for structure (§7) |
| Michael LaFargue, "Interpreting Aphorisms in the Tao Te Ching" (1990), and *Tao and Method* (1994) | Chapters assembled from short sayings, often with a comment or an application attached | §17: the turn from a saying to its application, usually 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") |
| David Lebovitz, "Molecular Incoherence, Continuity, and the Perfection of the Laozi," *Early China* 44 (2021) | The patterns that make a chapter hold together are made by the same forces that set chapters side by side, and the joining phrases are where editors worked | §17: a connective such as 故 (*gù* — so) or 是以 (*shì yǐ* — therefore) marks a seam, so one English for each lets a reader see the seams |
| Zhu Qianzhi, *Laozi jiaoshi* (*The Laozi Collated and Explained*), its *rhyme* entries, citing Jiang Yougao and Yao Wentian | Chapter by chapter, which lines rhyme and in which rhyme group | §7: confirms the ch 6 claim, and finds a second rhyme there |
| Zhang Yaolong, *Cong wenti tezheng kaobian Laozi yi shu de yuliao shuxing* (*What Kind of Language the Laozi Is, Judged from Its Style*), Malaysian Sinology | A chapter-by-chapter count of simile, series, couplet and gradation | §12 (gradation) and §16 (simile) |
| The standard catalogue of Chinese rhetoric, as taught: 頂真 (*dǐng zhēn* — the chain), 排比 (*pái bǐ* — the series), 對偶 (*duì ǒu* — the couplet), 層遞 (*céng dì* — gradation), 回文 (*huí wén* — reversal), 互文 (*hù wén* — mutual completion), 設問 (*shè wèn* — the question asked to be answered), 反問 (*fǎn wèn* — the rhetorical question), 引用 (*yǐn yòng* — quotation), 雙關 (*shuāng guān* — double sense), 比喻 (*bǐ yù* — simile and metaphor), 疊字 (*dié zì* — doubled characters) | Names and definitions | The names for §12–§16 |

**How far this research went, said plainly.** This environment's network blocks every page fetch, so the sources above were read through search results: abstracts, tables of contents, and quoted passages. **Wagner's own list of his 39 chapters, and Liu Xiaogan's full analysis, were not read.** So §11's instances are this audit's identification, made with Fech's restraint, not Wagner's list, and they should be checked against his book when it can be read. Every claim marked from a source above is one the search results state.

**Not devices, and why.** *Person:* the Chinese rarely names a subject, and the English must, so *you*, *they* and *the sage* are a translation decision, governed by standing rules 1 and 3, not a form of the source. *Tempo:* the source moves in three- and four-character beats that English cannot match syllable for syllable. Its form survives as rule 1 of *The page* (a series gets one shape), which every reading already checks.

---

### The devices

*Each with its name in Chinese rhetoric and in English, what it does, how this translation handles it, and its strongest examples. §1–§10 come from the seed scan of 2026-10-25; §11–§17 were added on 2026-10-26 from the research above, before the second read. The full audit (below) reads every chapter for all seventeen.*

#### 1 · The chain — 頂真 (*dǐng zhēn* — "capping"), anadiplosis

**What it is.** The last words of one clause become the first words of the next, so each line stands on the one before it. When the chain climbs step by step toward a conclusion, English rhetoric calls it a **sorites** or **climax**. In Chinese the device is also written 頂針 (*dǐng zhēn* — "thimble").

**Why it matters.** The chain is how the book argues. Chapters 16, 25 and 59 make their case as a ladder, and the claim is the ladder: each step follows from the last. A chain whose links are rendered in the wrong order still repeats its words, but no longer makes the argument.

**How we carry it.** **Position matters, not just repetition.** The repeated words must end one line and open the next. English grammar fights this, because an English possessive or prepositional phrase moves the repeated word: *"the gate of the dark female"* puts *the dark female* last.

| Ch | The Chinese | Our English | Verdict |
|---|---|---|---|
| 6 | 是謂玄牝。玄牝之門 (*shì wèi xuán pìn. xuán pìn zhī mén* — "this is called the dark female. The dark female's gate") | *"This is called the dark female. / The dark female's gate —"* | **Kept**, since 2026-10-25. *The gate of the dark female* had kept the words and moved the link to the end of the line. See *Chapter 6* below |
| 16 | 歸根曰靜…復命曰常，知常曰明 (*guī gēn yuē jìng… fù mìng yuē cháng, zhī cháng yuē míng* — "returning to the root is called stillness… returning to what is given is called the ever-present, knowing the ever-present is called clear-seeing"), then 容乃公，公乃王 (*róng nǎi gōng, gōng nǎi wáng* — "containing leads to impartiality, impartiality leads to authority") | *"Returning to the root is called stillness. … Containing everything leads to impartiality. / Impartiality leads to supreme authority."* | **Kept**, every link in position, and the two linking verbs held apart: 曰 (*yuē*) *is called*, 乃 (*nǎi*) *leads to*. Departed in tempo only: three-character beats become longer English lines |
| 25 | 大曰逝，逝曰遠，遠曰反 (*dà yuē shì, shì yuē yuǎn, yuǎn yuē fǎn* — "great means departing, departing means far, far means returning") | *"Great means departing, / departing means going far, / going far means returning."* | **Kept** |
| 25 | 人法地，地法天，天法道，道法自然 (*rén fǎ dì, dì fǎ tiān, tiān fǎ dào, dào fǎ zì rán* — "humans model on earth, earth on sky, sky on the Tao, the Tao on being what it is") | *"Humans model themselves on the earth, / Earth models itself on the sky…"* | **Kept** |
| 37 | 萬物將自化。化而欲作 (*wàn wù jiāng zì huà. huà ér yù zuò* — "the countless things will transform of themselves. Transforming, they want to act") | *"the countless things will transform of themselves. / When the countless things urge action"* | **Lost.** 化 (*huà* — transform) drops out of the second line, and the subject is repeated in its place. The next links in the chapter hold |
| 42 | 道生一，一生二，二生三，三生萬物 (*dào shēng yī, yī shēng èr, èr shēng sān, sān shēng wàn wù* — "the Tao births one, one births two, two births three, three births the countless things") | *"The Tao births the one, the one births the two…"* | **Kept** |
| 58 | 其無正。正復為奇 (*qí wú zhèng. zhèng fù wéi qí* — "it has no straight. The straight turns crooked") | *"It has no fixed norm — / The straight turns crooked"* | **Lost.** 正 (*zhèng* — straight) reads *norm*, then *straight*. Left to the 正/奇 (*zhèng / qí* — straight / crooked) call, `WORKLIST.md` T4-2 |
| 59 | 夫唯嗇，是謂早服；早服謂之重積德 (*fū wéi sè, shì wèi zǎo fú; zǎo fú wèi zhī zhòng jī dé* — "only conserving is called accepting early; accepting early is called a heavy store of integrity"), and four links more | *"Only conserving is called accepting early, / accepting early is called a heavy accumulation of integrity…"* | **Kept**, every link in position |

**Also kept:** 15 (×2), 21, 23, 28 (×3), 30 and 55, 32 (×2), 35, 40, 48, 52, 60, 61, 67 and 69; ch 74's link keeps its words but falls mid-line.

**Kept in words, cut by a stanza break** *(found in the full read, 2026-10-26)*: ch 1 (同謂之玄。玄之又玄 *tóng wèi zhī xuán. xuán zhī yòu xuán* — "together they are called dark. Dark, and dark again"), 25 (名曰大。大曰逝 *míng yuē dà. dà yuē shì* — "named it great. Great means departing"), 28's fourth link (復歸於樸。樸散 *fù guī yú pǔ. pǔ sàn* — "return to the uncarved wood. The uncarved wood scatters"), 55 (和之至也。知和 *hé zhī zhì yě. zhī hé* — "harmony at its utmost. Knowing harmony") and 65 (玄德。玄德 *xuán dé. xuán dé* — "profound integrity. Profound integrity"). The words are in position, and a blank line falls across the link, which rule 3 above forbids. `WORKLIST.md` T3-15.

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
| 41 | the twelve 建言 (*jiàn yán* — "established sayings"), each ▢若▢ (*ruò* — "seems") | **Kept**, one saying per line. 大白若辱 (*dà bái ruò rǔ* — "great white seems soiled") breaks the 大 (*dà* — great) frame as *"The whitest white"*: **departed**, Shalom's call of 2026-09-07, recorded in `chapters/041.md` |
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
| 22 · 24 | the two chapters mirror four pairs | **Departed** in one: 彰 (*zhāng* — to shine forth) reads *"their rightness shows"* at 22 and *"convince no one"* at 24, because the subjects differ (`chapters/024.md`) |

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
| 71 | 知不知，上；不知知，病 (*zhī bù zhī, shàng; bù zhī zhī, bìng* — "knowing not-knowing, highest; not knowing knowing, sickness") | **Departed**: *"To not know yet claim to know"* follows Heshang Gong's reading, and holds the reversal at the front of each line (`chapters/071.md`) |
| 22 | ring: 曲則全 (*qū zé quán* — "bend and be whole") opens the chapter and is quoted at its close | **Kept** |

#### 5 · The same word turned — polyptoton

**What it is.** One character used twice in different roles, often a word set against its own negation. There is no single standard name for it in Chinese rhetoric; English calls it **polyptoton**, or **figura etymologica** when a verb takes its own noun.

| Ch | The figure | Verdict |
|---|---|---|
| 14 | 無狀之狀 (*wú zhuàng zhī zhuàng* — "the shape of no shape") | **Kept**: *"the shape of no-shape"* |
| 38 | 上德不德 (*shàng dé bù dé* — "high integrity does not integrity") | **Kept** |
| 71 | 病病 (*bìng bìng* — "to sicken of sickness") | **Kept**: *"sick of the sickness"* |
| 50 | 生生之厚 (*shēng shēng zhī hòu* — "the thickness of their living life") | **Departed** in form: *"they cling too tightly to life"* keeps the sense and not the doubled verb. Needs its reason recorded |
| 1 | 道可道 (*dào kě dào* — "the Tao that can be tao-ed") | **Departed**, a recorded choice: the verb 道 (*dào* — to lay out, to tell) becomes *made a way*, so the line reads *Tao · way · Tao* (`chapters/001.md`, notes) |
| 63 | 為無為，事無事，味無味 (*wéi wú wéi, shì wú shì, wèi wú wèi* — "do not-doing, serve not-serving, taste not-tasting") | **Departed** in the third: *"taste the flavorless"*, an accepted departure whose recorded reason has lapsed (T3-13) |
| 64 | 欲不欲 / 學不學 (*yù bù yù / xué bù xué* — "want not-wanting / learn not-learning") | **Lost** in the second: *"learns to unlearn"* beside *"wants the not-wanting"* |
| 72 | 不畏威，則大威至 (*bù wèi wēi, zé dà wēi zhì* — "do not fear dread, and the great dread comes") and 夫唯不厭，是以不厭 (*fū wéi bù yàn, shì yǐ bù yàn* — "only because you do not press down, they are not fed up") | **Departed**, both recorded: the first repetition killed by Shalom, the second split into *oppress* / *tire of* (`notes/translation.md` → *Ch 72*) |
| 46 | 不知足…知足之足 (*bù zhī zú… zhī zú zhī zú* — "not knowing enough… the enough of knowing enough") | **Lost**: *discontent*, then *the contentment of knowing you have enough* (T3-18) |
| 39 | 數譽無譽 (*shù yù wú yù*, read as 輿 *yú* — "count the cart, and there is no cart") | **Kept**: *reduce a cart to the count of its parts, and there is no cart* |

#### 6 · The doubled character — 疊字 (*dié zì* — "stacked characters"), reduplication

**What it is.** One character said twice, for sound and intensity: 綿綿 (*mián mián* — unbroken, unbroken). It is often descriptive, a texture or a mood more than a meaning.

**How we carry it.** *(Shalom's call, 2026-10-25.)* **No book-wide rule. Every doubled character is listed and tracked here, and whether to carry the doubling is decided line by line.** A doubled English word often reads as a stammer, so most will not be carried; the point is to know where each one stands and what the English did with it. Each is **noted** until its chapter is read, when it gets a verdict: *kept*, or *departed* with its reason.

**The full list,** drawn from every chapter's source table on 2026-10-25:

| Ch · line | The doubling | Our English | Carried? |
|---|---|---|---|
| 6 · 5 | 綿綿 (*mián mián* — unbroken, like a silk thread) | *"Unceasing yet barely perceptible,"* | no |
| 14 · 11 | 繩繩 (*shéng shéng* — cord upon cord, endless) | *"Continuously flowing, it cannot be named"* | no |
| 16 · 5 | 芸芸 (*yún yún* — teeming, flourishing) | *"Things come to their fullest,"* | no |
| 20 · 6 | 熙熙 (*xī xī* — merry, bustling) | *"The crowd is merry, as if at a great feast,"* | no |
| 20 · 11 | 傫傫 (*léi léi* — weary, drooping) | *"listless, as if with nowhere to return."* | no |
| 20 · 15 | 沌沌 (*dùn dùn* — muddled, unformed) | *"How muddled!"* | no; the exclamation carries the intensity |
| 20 · 16–17 | 昭昭 / 昏昏 (*zhāo zhāo / hūn hūn* — bright / dim) | *"The worldly are bright. I alone am clouded."* | no |
| 20 · 18–19 | 察察 / 悶悶 (*chá chá / mèn mèn* — sharp / dull) | *"The worldly are sharp. I alone am dull."* | no |
| 39 · 20–21 | 琭琭 / 珞珞 (*lù lù / luò luò* — gleaming like jade / rough like stone) | *"Do not want to be gleaming like jade, / or common like stone."* | no |
| 49 · 8 | 歙歙 (*xī xī* — drawing in, as a breath) | *"the sage breathes gently"* | no |
| 58 · 1 | 悶悶 / 淳淳 (*mèn mèn / chún chún* — dull / simple) | *"dull and undiscerning … pure and honest"* | partly: two words for one doubled character |
| 58 · 2 | 察察 / 缺缺 (*chá chá / quē quē* — sharp / lacking) | *"sharp and prying … turn cunning"* | partly: the fourth breaks the pattern |
| 73 · 10 | 恢恢 (*huī huī* — vast, wide) | *"Nature's net is vast."* | no |

**Two things the list shows.** **察察 and 悶悶 (*chá chá* and *mèn mèn* — sharp and dull) stand in both 20 and 58, and read two ways:** single words in 20 (*sharp*, *dull*) and pairs in 58 (*sharp and prying*, *dull and undiscerning*). Where the Chinese repeats across chapters, the English should repeat too, or record why not. And **ch 58's pairs may be the answer** wherever a doubling is worth carrying: two English words for one doubled character keep the weight without the stammer.

**Not doubling, though the characters repeat:** 生生 (*shēng shēng* — "living life", ch 50), 知知 (*zhī zhī* — "knowing knowing", ch 71) and 病病 (*bìng bìng* — "sick of sickness", ch 71). Each is a verb taking its own word as object, and they belong to §5.

#### 7 · Rhyme — 押韻 (*yā yùn*)

**What it is.** Much of the Tao Te Ching rhymes in Old Chinese, the pronunciation of its own era, though many of the rhymes are lost in modern Mandarin.

**This translation makes no attempt to render the Chinese rhyme.** *(Shalom's call, 2026-10-25.)* Rhyme is a **departure by policy**, everywhere. No chapter's rhyme is a loss, and none needs a verdict. English rhyme forced onto this text would cost the words more than it gives the ear.

**The rhyme is still evidence.** Where rhyme binds lines in the Chinese, that is a fact about the source's structure, and it may inform where a stanza breaks. Chapter 6's 門 根 存 勤 (*mén gēn cún qín* — gate, root, exist, strain) fall in one traditional rhyme group, 文 (*wén*), which binds its last four lines, and 死 / 牝 (*sǐ / pìn* — die / female) rhyme in the 脂 (*zhī*) group, with 牝 (*pìn*) read like 匕 (*bǐ*), binding its first two. **Confirmed 2026-10-26** from Zhu Qianzhi's *Laozi jiaoshi*, which records Jiang Yougao's reading of the chapter, with Yao Wentian agreeing. Zhu's rhyme entries cover every chapter, so they are where a stanza question that turns on rhyme should look first. Any rhyme claim needs a source: Jiang Yougao's 老子韻讀 (*Lǎozǐ yùn dú* — "rhyme readings of the Laozi," Qing dynasty, public domain) first, and William Baxter, "Situating the Language of the *Lao-tzu*" (1998), as the modern cross-check, consulted for facts about sound, never for phrasing.

#### 8 · The formulas

**What they are.** Fixed phrases the book uses again and again, like a refrain. Each should read the same every time, so the reader hears it as one formula.

| Formula | How we carry it | Where it slips |
|---|---|---|
| 是謂 (*shì wèi* — "this is called") | *this is called* | **Lost** at ch 14 (*"This is the shape of no-shape"*) and 27, and **dropped** twice at ch 78; **departed**, by recorded decisions, at 13 (*"This is what is meant:"*), 53 and 74 (是謂社稷主 *shì wèi shè jì zhǔ* — "this is called lord of the altars of soil and grain" → *"is the keeper of the soil and the grain"*). Ch 65's 是謂玄德 (*shì wèi xuán dé* — "this is called profound integrity") reads *is called profound integrity*, where 10 and 51 give the same three characters *— / this is called*. Some may be licensed; each needs a verdict (T3-11, T3-17) |
| 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") and 故 (*gù* — "so") | *Therefore, the sage* and *So the sage*, both | The two connectives are not held apart: ch 57's 故聖人云 (*gù shèng rén yún*) reads *"Therefore the sage says:"* and ch 78's 是以聖人云 (*shì yǐ shèng rén yún*) reads *"So the sage says:"*, the mapping reversed. **The full read's tally** of 是以聖人 (*shì yǐ shèng rén*), 19 times in 18 chapters: *Therefore (,) the sage* at 2, 12, 22, 27, 29, 47, 58, 64 ×2, 70 and 77; *So the sage* at 7, 63 ×2, 73, 78 and 79; *This is how the sage* at 3; *And so the sage* at 72; and **no English at all** at 66 (*"The sage stands above"*). Wants one book-wide decision (T3-12) |
| 吾何以知…以此 (*wú hé yǐ zhī… yǐ cǐ* — "how do I know… by this") | *How do I know … is so? By this.* | **Kept** at 21, 54 and 57 (`notes/translation.md` → 以此) |
| 夫唯 (*fū wéi* — "only because") | *Only because…* | **Kept** at 2, 8, 15, 22, 67 and 71 |
| verbatim phrases across chapters that wear two Englishes, from the full read: 孤、寡、不穀 (*gū, guǎ, bù gǔ* — "orphaned, lone, unworthy", 39 · 42), 禍莫大於 (*huò mò dà yú* — "no disaster greater than", 46 · 69), 不言之教 (*bù yán zhī jiào* — "the teaching without words", 2 · 43), 生而不有 (*shēng ér bù yǒu* — "gives life and does not possess", 2 · 10 · 51), 不自見 (*bù zì jiàn* — "do not show themselves", 22 · 72), ▢之又▢ (*▢ zhī yòu ▢* — "▢, and ▢ again", 1 · 48), 以無事取天下 (*yǐ wú shì qǔ tiān xià* — "take the world by not meddling", 48 · 57), 抱一 (*bào yī* — "embrace one", 10 · 22), 扔 (*rēng* — to pull, 38 · 69), 功成 (*gōng chéng* — "the work done", 2 · 34 · 77), 民不畏 (*mín bù wèi* — "the people do not fear", 72 · 74), 利器 (*lì qì* — sharp tools, 36 · 57) | one English each, or a recorded reason | **Lost**, each awaiting a verdict. Several may be licensed by context; ch 69's is not, since its note says it matches ch 46 and the page does not (T3-17) |
| refrains across chapters: 沒身不殆 (*mò shēn bù dài* — "to the end of your days, no danger", 16 · 52), 知常曰明 (*zhī cháng yuē míng* — "knowing the ever-present is called clear-seeing", 16 · 55), 無為而無不為 (*wú wéi ér wú bù wéi* — "non-doing, yet nothing left undone", 37 · 48) | one English each | **Kept**, and so are 去彼取此 (*qù bǐ qǔ cǐ* — "let go of that, take this", 12 · 38 · 72), 物或惡之，故有道者不處 (*wù huò wù zhī, gù yǒu dào zhě bù chǔ* — "living things recoil from them, so those with the Tao do not dwell there", 24 · 31), 物壯則老 (*wù zhuàng zé lǎo* — "things in their prime decay", 30 · 55), 信不足焉 (*xìn bù zú yān* — "where trust is not enough", 17 · 23), 為者敗之，執者失之 (*wéi zhě bài zhī, zhí zhě shī zhī* — "those who handle it ruin it, those who grasp it lose it", 29 · 64), 為而不恃 (*wéi ér bù shì* — "acts, yet does not rely on it", 2 · 10 · 51 · 77), 是以聖人猶難之 (*shì yǐ shèng rén yóu nán zhī* — "so the sage still finds it difficult", 63 · 73), 侯王若能守之 (*hóu wáng ruò néng shǒu zhī* — "if rulers can hold to this", 32 · 37), 天之道 · 天道 (*tiān zhī dào · tiān dào* — "the way of nature", 9 · 47 · 73 · 77 · 79 · 81) and 是謂襲▢ (*shì wèi xí ▢* — "this is called ▢ worn covered", 27 · 52) |

#### 9 · The sung pause and the question — 兮 (*xī*) and 乎 (*hū*)

**What they are.** 兮 is a breath-particle from sung verse, a held pause with no meaning of its own. 乎 marks a question, often one that answers itself.

**How we carry them.** 兮 (*xī*) stands in nine chapters: 4, 14, 15, 17, 20, 21, 25, 34 and 58. It has no English word, so it is **departed** throughout, carried by the layout instead: a bare adjective and a comma (ch 4's *"Fathomless,"*, ch 15's *"Careful, like…"*), or full stops (ch 25's *"Silent. Empty. Solitary. Unchanging."*). Twice at ch 20 it becomes an exclamation (*"How muddled!"*). At 14, 17 and 34 it simply goes, and at 58, 禍兮 (*huò xī* — "disaster!") holds a topic up, which the English carries as *Disaster is what…*. The reason should be written once, here (T3-14). 乎's (*hū*) questions are **kept** at 10, 15, 44 and elsewhere; every question form in the book is now read under §14. At ch 20, 相去 (*xiāng qù* — "how far apart") ×2 reads *"how much distance?"* and then *"how far apart?"*, which the seed scan called **lost** and the full read found **kept**: the Chinese varies its own word there (§13).

#### 10 · The reversed saying — 正言若反 (*zhèng yán ruò fǎn*), paradox

**What it is.** The book names its own method at ch 78: *"Words on the mark seem like their opposite."* The soft overcomes the hard; the one who puts themselves last comes first.

**How we carry it.** The paradox must stay sharp: no softening word that resolves it. 若 (*ruò* — seems) reads *seems* throughout chs 41 and 45, and ch 7's 後其身而身先 (*hòu qí shēn ér shēn xiān* — "puts their body last, and their body comes first") keeps its turn. **Kept**, so far as the seed scan read.

#### 11 · Interlocking strands — Wagner's interlocking parallel style

**What it is.** Two strands of thought, a and b, run side by side through a passage, each keeping its own words, and a closing line often takes up both. Ch 64 is the model: 為者敗之，執者失之 (*wéi zhě bài zhī, zhí zhě shī zhī* — "those who do it ruin it, those who grasp it lose it") sets up strand a (doing) and strand b (grasping), and 無為故無敗，無執故無失 (*wú wéi gù wú bài, wú zhí gù wú shī* — "not doing, so no ruin; not grasping, so no loss") answers each in order.

**Why it matters.** The reader follows a strand by its words. When strand a's word changes in English, the answer no longer meets its question, though every line is defensible on its own. Wang Bi read the text this way, so this is the commentary's own structure as well as the text's.

**How we carry it.** Each strand keeps one English from end to end. **Restraint, after Fech:** a strand is claimed only where its words visibly recur.

| Ch | The strands | Verdict |
|---|---|---|
| 13 | 寵辱若驚 (*chǒng rǔ ruò jīng* — "favor and disgrace are both a shock") and 貴大患若身 (*guì dà huàn ruò shēn* — "prize great trouble as your body"), each asked about in turn with 何謂 (*hé wèi* — "what does it mean") | **Kept** |
| 26 | 重 / 輕 (*zhòng / qīng* — heavy / light) and 靜 / 躁 (*jìng / zào* — still / agitated), closed by 輕則失本，躁則失君 (*qīng zé shī běn, zào zé shī jūn* — "lightness loses the root, agitation loses the lord") | **Kept** |
| 27 | 善人 (*shàn rén* — the masterful) with 師 (*shī* — teacher), and 不善人 (*bù shàn rén* — the unmasterful) with 資 (*zī* — material) | **Lost**: *master* crosses from strand b's partner to strand a (T3-16) |
| 29 | 為 (*wéi* — handle) and 執 (*zhí* — grasp): 不可為也，不可執也 / 為者敗之，執者失之 (*bù kě wéi yě, bù kě zhí yě / wéi zhě bài zhī, zhí zhě shī zhī*) | **Kept**: *handled · grasped · handle · grasp* |
| 44 | 名 / 身 (*míng / shēn* — reputation / body) with 甚愛 (*shèn ài* — great attachment), and 貨 (*huò* — goods) with 多藏 (*duō cáng* — much hoarding), both closed on 亡 (*wáng* — loss) | **Kept** |
| 46 | 禍…不知足 (*huò… bù zhī zú* — "disaster… not knowing enough") and 咎…欲得 (*jiù… yù dé* — "fault… craving to get"), strand a closed by 知足之足 (*zhī zú zhī zú* — "the enough of knowing enough") | **Lost**: strand a reads *discontent*, then *knowing you have enough* (T3-18) |
| 47 | 出 (*chū* — going out) and 見 (*jiàn* — seeing), closed by 不行而知，不見而名 (*bù xíng ér zhī, bù jiàn ér míng* — "knows without going, names without seeing") | **Kept**: *venture* carries the going-out strand into its close. This withdraws the T5-14 claim that *venture* was an invented echo |
| 63 | 難 / 易 (*nán / yì* — difficult / easy) and 大 / 細 (*dà / xì* — great / slight), each stated twice | **Kept** |
| 64 | 為 / 執 (*wéi / zhí* — doing / grasping) | **Lost**: *handle* in the question, *do* in the answer (T3-9) |
| 66 | 上 (*shàng* — above) with 言 (*yán* — speech), and 先 (*xiān* — ahead) with 身 (*shēn* — body), then 處上 / 處前 (*chǔ shàng / chǔ qián* — "stands above / stands in front") | **Kept** |
| 70 | 知 (*zhī* — know) and 行 (*xíng* — follow) | **Kept** |
| 73 | 敢 / 不敢 (*gǎn / bù gǎn* — pushing / not pushing), closed by 或利或害 (*huò lì huò hài* — "one benefits, one harms"), which names the strands in the reverse order | **Kept**: *one benefits and one harms* leaves the mapping as open as the Chinese does |
| 76 | 生 / 死 (*shēng / sǐ* — life / death) with 柔弱 / 堅強 (*róu ruò / jiān qiáng* — soft and yielding / hard and strong), reversed in the summary | **Kept** |

**Also kept:** 3 (heart and ambition against belly and bones), 7, 15, 45, 52, 58, 61, 77 and 81.

#### 12 · Gradation — 層遞 (*céng dì* — "step by step"), climax

**What it is.** Three or more terms in rising or falling order, with no word carried from one step to the next. It differs from the chain (§1), where each step stands on the last one's words.

**How we carry it.** The order kept, the steps alike in shape, and no step named by a judgment the Chinese leaves to the order.

| Ch | The gradation | Verdict |
|---|---|---|
| 54 | 身 · 家 · 鄉 · 邦 · 天下 (*shēn · jiā · xiāng · bāng · tiān xià* — body, family, community, state, world), twice | **Kept** |
| 38 | 道 · 德 · 仁 · 義 · 禮 (*dào · dé · rén · yì · lǐ* — Tao, integrity, humaneness, duty, ritual), falling | **Kept** |
| 64 | 合抱之木 · 九層之臺 · 千里之行 (*hé bào zhī mù · jiǔ céng zhī tái · qiān lǐ zhī xíng* — the tree, the terrace, the journey) | **Kept** |
| 41 | 上士 · 中士 · 下士 (*shàng shì · zhōng shì · xià shì* — the highest, middling, lowest in service) | **Kept** |
| 17 | 太上 · 其次 · 其次 · 其次 (*tài shàng · qí cì* — the highest, then the next, the next, the next) | **Lost**: named *Good*, *Poor*, *The worst* (T3-18) |

**Also kept:** 16 and 59, which are also chains, 25's four great things, and 42's count.

#### 13 · Varied repetition — 錯綜 (*cuò zōng* — "interweaving"), and mutual completion — 互文 (*hù wén*)

**What they are.** The mirror of the series. **Varied repetition:** the Chinese keeps a frame and *changes* a word that could have stayed, as ch 39 does with six different verbs of collapse. **Mutual completion:** two halves that complete each other, as 天長地久 (*tiān cháng dì jiǔ* — "sky long, earth lasting") means *sky and earth are long and lasting*.

**Why it matters.** `principles/repeat-yourself.md` says: where the Chinese repeats, repeat. The converse is the same rule: **where the Chinese varies, vary**, unless a recorded reason says the variation is only for the ear.

| Ch | The variation | Verdict |
|---|---|---|
| 39 | 裂 · 發 · 歇 · 竭 · 滅 · 蹶 (*liè · fā · xiē · jié · miè · jué* — split, burst, cease, run dry, die out, topple) | **Kept** |
| 20 | 幾何 / 若何 (*jǐ hé / ruò hé* — "how much / how") in the two 相去 (*xiāng qù* — "how far apart") questions | **Kept**: the Chinese varies its own second word, so *how much distance?* / *how far apart?* follows it. This withdraws the seed scan's *lost* (T3-13) |
| 13 | 寄 / 託 (*jì / tuō* — lodge with / entrust to) | **Departed**, recorded: both *trusted with*, because Wang Bi swaps the two in his own commentary and the Shuowen defines each by the other (`chapters/013.md`) |
| 26 | 根 / 本 (*gēn / běn* — root / base) | **Departed**, the reason to record: both *root*, and the commentary equates them. On the baggage line Wang Bi writes 以重為本故不離 (*yǐ zhòng wéi běn gù bù lí* — "takes the heavy as the base, so does not leave it"), using the closing line's 本 (*běn* — base) for what the opening line, 重為輕根 (*zhòng wéi qīng gēn* — "the heavy is the root of the light"), calls 根 (*gēn* — root) |
| 74 | 畏 / 懼 (*wèi / jù* — dread / startle) | **Kept**: *fear* / *frighten* (`notes/translation.md` → *Ch 74*) |
| 22, 25, 36, 46, 61 | 明 / 彰 (*míng / zhāng*), 字 / 名 (*zì / míng*), 張 · 強 · 興 · 與 (*zhāng · qiáng · xīng · yǔ*), 禍 / 咎 (*huò / jiù*), 以取 / 而取 (*yǐ qǔ / ér qǔ*) | **Kept**: each varied word has its own English |
| 7, 52 · 56 | 天長地久 (*tiān cháng dì jiǔ*); 塞其兌，閉其門 (*sè qí duì, bì qí mén* — "block the openings, close the gates") | **Kept**: ch 7 distributes *lasting* and *enduring*, then joins them, *last and endure* |

#### 14 · The question — 設問 (*shè wèn*) and 反問 (*fǎn wèn*)

**What they are.** The **set question** is asked to be answered at once: 孰為此者？天地 (*shú wèi cǐ zhě? tiān dì* — "who does this? Sky and earth", ch 23). The **rhetorical question** answers itself: 豈虛言哉 (*qǐ xū yán zāi* — "were these empty words?", ch 22).

**How we carry them.** As questions, with the answer, where there is one, set right after. This supersedes §9's question half, which named only 乎 (*hū*).

**Kept, every one found:** set questions at 13 (×2), 21, 23, 50 (×2), 54, 57, 62 and 77; rhetorical questions at 5, 7, 10 (×6), 15 (×2), 20 (×2), 22, 23, 26, 39, 44 (×3), 58, 62, 73, 74 (×2), 77 and 79.

#### 15 · The quoted saying — 引用 (*yǐn yòng*)

**What it is.** The text cites: 古之所謂 (*gǔ zhī suǒ wèi* — "what the ancients called", 22), 建言有之 (*jiàn yán yǒu zhī* — "the established sayings have it", 41), 人之所教 (*rén zhī suǒ jiào* — "what others teach", 42), 聖人云 (*shèng rén yún* — "the sage says", 57 and 78), 用兵有言 (*yòng bīng yǒu yán* — "those who use arms have a saying", 69), and reported speech at 17 and 62.

**How we carry it.** The quotation is marked, by quotation marks or a colon, so the reader hears a second voice.

**Kept, every one:** 17, 22, 41, 42, 57, 62, 69 and 78.

#### 16 · Double sense, simile, and the book's images

**Double sense — 雙關 (*shuāng guān*).** One word doing two jobs, or two words sharing a sound. **Departed, every one recorded:** 1's verb 道 (*dào* — to tell), 62's 寶 / 保 (*bǎo* — treasure / keep safe), 69's 兵 (*bīng* — weapons, soldiers), and 72's 威 (*wēi* — dread, authority) and 厭 (*yàn* — to press down, to be fed up). **Kept:** 71's 病病 (*bìng bìng* — "sick of the sickness") and 39's 譽 / 輿 (*yù / yú* — praise, read as cart). **Lost:** 26's 輜重 (*zī zhòng* — the heavy wagons), whose 重 (*zhòng* — heavy) answers line 1 (T3-18).

**Simile — 比喻 (*bǐ yù*).** The markers 若 (*ruò* — like, seems), 如 (*rú* — as if), 猶 (*yóu* — like), 譬 (*pì* — compare) and 似 (*sì* — resemble). **Kept**: every simile reads as a simile, and none has been turned into a statement of identity. At ch 13, 若驚 (*ruò jīng* — "like a shock") reads *both a shock*, and the note there records that 若 (*ruò* — like) was weighed.

**The images.** The book returns to a few images, and a reader learns them by their English: water, the valley, the infant, the uncarved wood, the mother, the female, the root, the gate. **The locks hold most of them** (`glossary/INDEX.md`): 谷 (*gǔ* — valley), 樸 (*pǔ* — uncarved wood), 母 (*mǔ* — mother), 牝 (*pìn* — the female), 水 (*shuǐ* — water). **Two slip:**

- **門 (*mén* — gate)** is *the gate* at 1, 6 and 10, and *the doors* at 52 and 56, in 閉其門 (*bì qí mén* — "close the gates"). It has no lock (T3-19).
- **樸 (*pǔ*)** reads *the uncarved wood* in five chapters and *plain* at ch 57's 而民自樸 (*ér mín zì pǔ* — "and the people become uncarved of themselves"), the image lost in the one chapter where it is the people's own state (T3-19).

#### 17 · The turn — from saying to application

**What it is.** A chapter states a saying or an observation, then turns, usually on 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") or 故 (*gù* — so), and applies it. LaFargue reads the chapters as built this way; Lebovitz shows that the joining phrases are where editors worked.

**How we carry it.** The turn gets a connective, and a stanza break where the Chinese turns (*The page*, rule 2). One English for each connective, so the seams read alike.

**Kept** in every chapter but one: the connective is present, and the stanza break usually falls at the turn. Where it does not (64's first turn, 63's second, 70 and 73), the application closes the stanza of the saying it answers, which in 64 keeps a pair of strands together (§11) and elsewhere is a single line that would not stand alone. Leave those. **Lost** at ch 66, where 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") has no English at all. **The connectives themselves** are T3-12.

---

### Chapter 6 — the first entry

*The chapter that opened this file, 2026-10-25.*

**Its devices.** Three couplets, each one sentence: 谷神不死，是謂玄牝。(*gǔ shén bù sǐ, shì wèi xuán pìn* — "the valley spirit does not die, this is called the dark female") · 玄牝之門，是謂天地根。(*xuán pìn zhī mén, shì wèi tiān dì gēn* — "the dark female's gate, this is called the root of sky and earth") · 綿綿若存，用之不勤。(*mián mián ruò cún, yòng zhī bù qín* — "unbroken, it seems to exist; use it, and there is no strain"). Across them run a **chain** (玄牝 *xuán pìn* — "the dark female" ends the first couplet and opens the second), the **formula** 是謂 (*shì wèi* — "this is called") twice, a **doubled character** (綿綿 *mián mián*), and a **rhyme** binding the last four lines: 門 根 存 勤 (*mén gēn cún qín* — gate, root, exist, strain).

**What the English did.** *"This is called the dark female. / The gate of the dark female,"* kept the repeated words and lost the chain: the English *of* moved *the dark female* to the end of the line, so the link where one line hands its last words to the next was gone. The formula is kept both times. The doubling is not carried (*"Unceasing"*), and the rhyme is not rendered, by policy.

**The chain restored.** *Shalom's call, 2026-10-25:*

> The spirit of the valley is deathless.  
> This is called the dark female.  
> The dark female's gate —  
> this is called the root of sky and earth.
>
> Unceasing yet barely perceptible,  
> use it, and there is no strain.

- **The chain, kept.** *The dark female's gate* opens on the words the line before it ended on, in the Chinese order: 玄 (*xuán* — dark) 牝 (*pìn* — female) 之 (*zhī* — 's) 門 (*mén* — gate). It also names her twice and ties the gate to her, which is what the 2026-10-24 ruling on this line asked for.
- **The stanza break, 4 / 2.** The first four lines name the thing twice with 是謂 and hold the chain inside one stanza. The last two turn to how it is used. The break cuts only the rhyme that ties 根 (*gēn* — root) to 存 (*cún*) and 勤 (*qín*), which the English does not carry anyway. *(Three couplets, 2 / 2 / 2, were considered and set aside: they put a blank line in the middle of the chain.)*
- **The dash.** It does not strand a subject: *this* picks it straight back up, as the Chinese 是 (*shì* — this) points back at its topic. Chapters 10 and 51 use the same mark in the same formula: *"growing them without ruling them — / this is called profound integrity."* This line is the case on which the dash rule was rewritten the same day (`CLAUDE.md` standing rule 3).
- **The cost.** Chapter 1's 眾妙之門 (*zhòng miào zhī mén*) reads *"the gate of all subtleties,"* so 之門 (*zhī mén* — "'s gate") takes two shapes in the book. Chapter 6 has a chain to keep, and chapter 1 does not.

**Verdict:** chain *kept*. Rhyme *departed*, by policy (§7). The doubling 綿綿 (*mián mián* — unbroken) is noted in §6 and awaits its verdict.

---

### The full audit

*`WORKLIST.md` R4. **All 81 chapters read on 2026-10-26**, one at a time, against the Chinese, the `--formulas` scan, and the notes, so that a form already let go by a recorded decision is marked* departed *and not reopened.*

**How to read a chapter:**

1. Run `python3 tools/concordance.py --formulas N`. It lists every series, frame and repeat the chapter holds, with its English underneath.
2. Read the Chinese aloud in pinyin, and name every device from the list above that it uses.
3. For each device, give a verdict: *kept*, *departed* (with the reason), or *lost*.
4. Bring each *lost* to Shalom, one at a time, with a recommendation. Record what he decides: a fix goes in the chapter and `notes/translation.md`, and a departure gets its reason here.
5. Fill in the chapter's row below.

**What the full read changed.** Steps 1–3 are done for every chapter. Step 4 is the work now owed: the losses are filed in `WORKLIST.md`, and no line of the translation was changed by this pass. Four patterns came out of the whole book that no single chapter shows:

- **A chain cut by a stanza break.** Five chapters hand a chain's words from one line to the next across a blank line, which this file's own rule 3 forbids: 1, 25, 28, 55 and 65. `WORKLIST.md` T3-15.
- **Ch 27's mirror, and a word doing two jobs.** 善人 (*shàn rén* — the masterful person) and 不善人 (*bù shàn rén* — the unmasterful person) trade places in a chiasmus, and the English renders them *the masterful one*, *the novice* and *the master*, while 師 (*shī* — teacher) reads *teaches* and then *the master*. So *master* names two characters in adjacent lines, and the mirror is gone. T3-16.
- **Formulas that drift between chapters.** The seed scan read repeats inside a chapter well. Across chapters, a dozen verbatim phrases wear two Englishes, and in one case, ch 69, the note says the English was matched to ch 46 on purpose while the page no longer matches. T3-17.
- **A cross-chapter formula and a within-chapter series can pull in opposite directions.** 為而不恃 (*wéi ér bù shì* — "acts, yet does not rely on it") reads *acts, yet relies on nothing* or *acting yet relying on nothing* at 2, 10, 51 and 77, one English every time. That consistency is exactly what breaks the 而不 (*ér bù* — "and does not") series inside ch 2, 10 and 51. Whoever decides T3-13's ch 2 decides all four chapters.

**The second read, 2026-10-26.** After the research above added §11–§17, every chapter was read again for those seven. Their instances and verdicts are in the device tables, not repeated chapter by chapter. The second read also checked every *lost* against the chapter's own notes and `notes/translation.md`, and **moved ten to *departed*, because a recorded decision had already let the form go:** 12's *hinder*, 13's *this is what is meant* and *trusted with*, 41's *whitest white*, 53's *exposes*, 63's *flavorless*, 65's *robs*, 71's *claim to know*, 74's equation, and 80's *next door*. One more, 20's *how far apart*, is now *kept*, because the Chinese varies its own word there. It found two new losses in the images (§16) and one lock breach (ch 27's *secret*). **And every departure now has a recommendation:** see *What to do with each departure*, below the ledger.

**Where the losses are tracked.** The seed scan's losses are T3-8 → T3-14, with ch 6's doubling at T2-67 and ch 58's chain under T4-2. The full read added T3-15 → T3-19, widened T3-12 and T3-14, and added evidence to T4-2 and T5-14. A ruling there updates the verdict here.

**The ledger.** ✅ read, every device kept, or let go by a recorded decision. 🔶 read, with something still open: the *Open* column names the row, and *What to do with each departure* gives the recommendation. *Devices* lists the main ones; §11–§17's instances are in their own tables. Rhyme needs no verdict: it is not rendered, by policy (§7). Doublings do: each is decided line by line, against the full list in §6.

| Ch | Devices | Read | Open |
|---|---|---|---|
| 1 | polyptoton, couplets ×2, chain | 🔶 | T3-15 · T3-17 |
| 2 | couplet, series ×2, chain, only because | 🔶 | T3-13 · T3-17 · T3-18 |
| 3 | series, couplets, polyptoton, therefore the sage | 🔶 | T3-12 |
| 4 | sung pause ×2, series shared with 56, simile | 🔶 | T3-14 · T5-14 |
| 5 | couplet, question | ✅ | |
| 6 | chain, this is called ×2, doubling, rhyme, dash | 🔶 | T2-67 |
| 7 | couplet, paradox, chain | ✅ | |
| 8 | series, only because, ring | ✅ | |
| 9 | couplets ×2 | 🔶 | T3-18 |
| 10 | series of questions, series, this is called | 🔶 | T3-13 · T3-17 · T3-18 |
| 11 | series | ✅ | |
| 12 | series, therefore the sage, refrain | ✅ | |
| 13 | strands, refrains, this is called, couplet | 🔶 | T3-18 |
| 14 | series, doubling, polyptoton, this is called ×3 | 🔶 | T3-11 · T3-14 · §6 |
| 15 | sung-pause series, chain ×2, questions, only because ×2 | 🔶 | T3-14 |
| 16 | couplet, chain (sorites), doubling, refrain | 🔶 | §6 |
| 17 | gradation, polyptoton, refrain, sung pause, quotation | 🔶 | T3-14 · T3-18 |
| 18 | series | ✅ | |
| 19 | series, couplet | ✅ | |
| 20 | doublings, sung pause, questions, varied repetition | 🔶 | T3-14 · §6 |
| 21 | series, reversal, chain, sung pause, by this | 🔶 | T3-14 |
| 22 | series ×2, ring, mirror of 24, only because, quotation | 🔶 | T3-17 |
| 23 | couplet, chain, series ×2, refrain | ✅ | |
| 24 | couplet, mirror of 22, refrain shared with 31 | 🔶 | T3-17 |
| 25 | sung pause, couplet, chain ×2, series | 🔶 | T3-14 · T3-15 · T3-18 |
| 26 | strands, ring, double sense, varied repetition | 🔶 | T3-18 |
| 27 | series, couplet, chiasmus, strands, this is called ×2 | 🔶 | T3-11 · T3-16 · T3-18 |
| 28 | three parallel stanzas, chain ×4 | 🔶 | T3-15 |
| 29 | series ×2, couplet | ✅ | |
| 30 | series, chain, refrain shared with 55 | 🔶 | T3-18 |
| 31 | couplets ×3, chain, refrain shared with 24 | ✅ | |
| 32 | chain ×2, formula shared with 37 | ✅ | |
| 33 | couplets ×4 | ✅ | |
| 34 | sung pause, frame ×2, chain | 🔶 | T3-14 · T3-17 · T3-18 |
| 35 | chain, series | ✅ | |
| 36 | series, this is called | 🔶 | T3-17 |
| 37 | chain ×3, refrain | 🔶 | T3-8 |
| 38 | polyptoton, series, chain (cascade), refrain | 🔶 | T3-17 |
| 39 | series ×2, couplet, doubling, question | 🔶 | T3-17 · §6 |
| 40 | couplet, chain | ✅ | |
| 41 | series ×3, chain, gradation, quotation | ✅ | |
| 42 | chain, reversal | 🔶 | T3-17 |
| 43 | couplet, echo | 🔶 | T3-17 |
| 44 | questions, couplets ×2 | ✅ | |
| 45 | series, couplet | 🔶 | T4-2 |
| 46 | strands, couplets ×2, polyptoton | 🔶 | T3-17 · T3-18 |
| 47 | strands, series | ✅ | |
| 48 | couplet, chain, refrain | 🔶 | T3-17 |
| 49 | parallel stanzas, polyptoton, doubling | 🔶 | T3-18 · §6 |
| 50 | series ×2, frame ×2, polyptoton | 🔶 | T3-14 · T3-18 |
| 51 | series ×2, refrain shared with 10 | 🔶 | T3-13 · T3-18 |
| 52 | chain, reversal, couplets, refrain, images | 🔶 | T3-19 |
| 53 | series ×2, this is called | ✅ | |
| 54 | couplet, series ×2, gradation, by this | ✅ | |
| 55 | series, chain ×2, refrain shared with 30 | 🔶 | T3-15 · T3-18 |
| 56 | reversal, series ×2, shared with 4 and 52, images | 🔶 | T3-13 · T3-19 |
| 57 | series ×3, by this, so the sage, quotation, images | 🔶 | T3-12 · T3-17 · T3-18 · T3-19 |
| 58 | doublings, reversal, chain, series | 🔶 | T4-2 · §6 |
| 59 | chain (sorites) | ✅ | |
| 60 | chain | 🔶 | T3-18 |
| 61 | chiasmus, chain, couplet | ✅ | |
| 62 | sound-pair, couplet | ✅ | |
| 63 | polyptoton ×3, strands, couplets | 🔶 | T3-13 |
| 64 | series ×2, couplets, polyptoton, strands, gradation | 🔶 | T3-9 |
| 65 | couplet, chain, this is called | 🔶 | T3-15 · T3-17 |
| 66 | ring, strands, refrain shared with 22 | 🔶 | T3-12 |
| 67 | chain, series ×3, only because | ✅ | |
| 68 | series, this is called ×3 | ✅ | |
| 69 | couplet, series, chain | 🔶 | T3-17 |
| 70 | couplets ×3, only because | ✅ | |
| 71 | reversal, polyptoton, only because | ✅ | |
| 72 | polyptoton ×2, couplets | 🔶 | T3-17 |
| 73 | couplet, series, doubling | 🔶 | §6 |
| 74 | chain, this is called, varied repetition | 🔶 | T3-17 |
| 75 | series with refrain | ✅ | |
| 76 | couplets ×3 | ✅ | |
| 77 | couplets, chiasmus, refrain | 🔶 | T3-18 |
| 78 | paradox, this is called ×2, therefore the sage | 🔶 | T3-11 · T3-12 |
| 79 | couplet | ✅ | |
| 80 | series ×3 | ✅ | |
| 81 | reversal ×3, couplets | ✅ | |

---

### What to do with each departure

*Every place the English differs from a form the Chinese uses, with a recommendation: **resolve** it, and how, or **leave** it, and the reason to record. A recommendation is not a ruling. Each comes to Shalom one at a time, and his ruling replaces it here. Proposed English follows the locks in `glossary/INDEX.md` and standing rule 3's dash rule. Departures already settled by a recorded decision are listed at the end, so nothing is missing from the count.*

**The order to take them in.** Deepest first: **T3-16** (ch 27, where the mirror and a lock both break), then **T3-13's ch 2 / T3-17's 為而不恃** (*wéi ér bù shì* — "acts, yet does not rely on it"), which decides four chapters at once, then **T3-12** (the connectives, book-wide), then the rest by row.

#### T3-16 · Ch 27 — the mirror on the masterful

The couplet and its sequel are one structure with two strands (§11): 善人 (*shàn rén* — the masterful) goes with 師 (*shī* — teacher), and 不善人 (*bù shàn rén* — the unmasterful) goes with 資 (*zī* — material). **Resolve.**

> So the masterful are the teachers of the unmasterful.  
> The unmasterful are the raw material of the masterful.  
> Not to value the teacher, not to love the raw material,  
> even for the clever, is great confusion.  
> This is called the essential subtlety.

- *Masterful / unmasterful* is the lock's English for 善 (*shàn*) of people, and what chs 49 and 62 already say. *Novice* and *master* go, *naturally* goes (it has no character), and *master* stops naming two characters.
- 雖智大迷 (*suī zhì dà mí* — "though clever, greatly lost") keeps 迷 (*mí*) as *confusion* and folds *Even those who appear intelligent are lost* into the line it belongs to.
- **And a lock:** 是謂要妙 (*shì wèi yào miào* — "this is called the essential subtlety") reads *This is the essential secret*. 妙 (*miào*) is locked to *subtle*, and *secret* is the register the lock exists to refuse, so this repairs T3-11's ch 27 and the lock at once.
- *The masterful* lands four times in two lines. The Chinese does exactly that, so the weight is honest.

Ch 27's other member, 善言無瑕謫 (*shàn yán wú xiá zhé* — "masterful speech has no flaw to fault"), **resolve:** *"Masterful speaking leaves no flaw."* It rejoins the *leaves no* / *uses no* frame, and answers line 1's *leaves no tracks*, as 無轍跡 / 無瑕謫 (*wú zhé jì / wú xiá zhé*) answer each other.

#### T3-13 (ch 2) and T3-17 (生而不有, *shēng ér bù yǒu*) · the formula that decides four chapters

為而不恃 (*wéi ér bù shì*) reads *acts, yet relies on nothing* at 2 and 77, and *acting yet relying on nothing* at 10 and 51. That consistency is a recorded decision (`notes/translation.md` → 恃 (*shì* — rely on), swept 2026-08), and it is what breaks the 而不 (*ér bù* — "and does not") series in all three chapters that have one. **Resolve, book-wide:** **acts without relying on it.**

- **10 and 51:** *giving birth without possessing, / acting without relying on it, / growing them without ruling them —* three *without*s, the series whole.
- **77:** *Therefore the sage acts without relying on it.*
- **2:** the series is *…, and the sage does not…* ×4, so:

> The countless things arise, and the sage does not begin them.  
> The sage gives them birth, and does not possess them;  
> acts, and does not rely on it.  
> The work is done, and the sage does not stay in it.

  The fourth line stays as it is: 功成 (*gōng chéng* — "the work completes") is impersonal (`notes/translation.md` → *Ch 77*), and ch 77 reads the same.
- **Why *on it*:** the note's own stated cost is that *relies on nothing* reads as Stoic self-sufficiency. Heshang Gong on ch 2 says what is not relied on is the act's return: 道所施為，不恃望其報也 (*dào suǒ shī wéi, bù shì wàng qí bào yě* — "what the Tao does, it does not rely on, expecting a return"), and he repeats it at 10 and 51. *It* is the thing done, which is the plainer reading, and it removes the cost.
- **生而弗有** (*shēng ér fú yǒu* — "gives birth and does not possess") at ch 2 then reads *The sage gives them birth, and does not possess them*, beside 10 and 51's *giving birth without possessing*. Heshang Gong's subject at ch 2 is the giver: 元氣生萬物而不有 (*yuán qì shēng wàn wù ér bù yǒu* — "the primal breath gives birth to the countless things and does not possess them"). This resolves T3-17's 生而不有 (*shēng ér bù yǒu*) too.

#### T3-12 · 故 (*gù* — so) and 是以 (*shì yǐ* — therefore)

**Resolve: hold them apart, one English each.** 是以 (*shì yǐ*) → **Therefore**; 故 (*gù*) → **So** (and *and so* inside a sentence). The research is the reason: these are the joints where the chapters were put together (§17), and a reader who hears one word for each can hear the seams.

The rule is for the connective that opens a line; inside a sentence both may read *and so*. **是以 (*shì yǐ*) to *Therefore*:** 7 (*So the sage*), 63 ×2, 72 (*And so the sage*), 73, 78 and 79; 3's *This is how the sage governs:* → *Therefore, the sage governs like this:*; 38, 39 and 76's *This is why…* → *Therefore…*; and 66, which has no English at all: *Therefore the sage stands above, and the people are not weighed down*. **故 (*gù*) to *So*:** 57 (*Therefore the sage says:*), and the *Therefore*s now on a 故 (*gù*) at 2 (*Therefore presence and absence…*), 14 (*Therefore, they mix into one*), 25 (*Therefore, the Tao is great*), 41 (*Therefore, as the established sayings have it*), 54 (*Therefore, observe the body*) and 69 (*Therefore, when the armies…*), with 51's *Thus*. 是故 (*shì gù* — "therefore", ch 44) reads with 是以 (*shì yǐ*).

#### T3-15 · Chains cut by a stanza break

- **Ch 1 — resolve.** Delete the blank line, so *"Together, they are called profound darkness. / Dark, and dark again, the gate of all subtleties."* is one stanza.
- **Ch 25 — resolve.** Delete the blank after *"Forcing a name on it, I call it great."* The naming and the chain it starts become one stanza of six.
- **Ch 55 — resolve, by moving the break.** Put it after *"…this is vital essence at its utmost."*, so the second stanza opens *"It cries all day and never goes hoarse — this is harmony at its utmost. / Knowing harmony is called the ever-present…"* Both of the chapter's chains, 和…知和 (*hé… zhī hé* — "harmony… knowing harmony") and 常…知常 (*cháng… zhī cháng* — "the ever-present… knowing the ever-present"), then sit inside one stanza.
- **Ch 65 — resolve.** Delete the blank before *"Profound integrity is deep"*.
- **Ch 28 — leave, and record the reason.** The three matched stanzas are the chapter's form, and rule 1 (a series keeps one shape) outranks a single link here, because the coda turns: the uncarved wood scatters into vessels, and the Chinese turns with it (rule 2). Ch 6 is not a precedent against this: there no series was at stake.

#### T3-8 · Ch 37 — the chain through 化 (*huà* — transform)

**Resolve.** *"…the countless things will transform of themselves. / Transforming, if they desire to act, / I will stabilize them with the nameless uncarved wood."* This restores the link, and it also restores a second chain the old line hid: 欲 (*yù* — desire) runs 化而欲作 · 將無欲 · 不欲以靜 (*huà ér yù zuò · jiāng wú yù · bù yù yǐ jìng* — "transforming, they desire to act · will be without desire · not desiring, by stillness"), and *urge* was the one place it did not read *desire*.

#### T3-9 · Ch 64 — the strands of doing and grasping

**Resolve:** *"Therefore, the sage does not handle it, and so ruins nothing, / does not grasp it, and so loses nothing."* Strand a (§11) reads *handle* in the question, here and at ch 29, so the answer must too. **The cost:** 無為 (*wú wéi*) is locked to *non-doing*, and here it is a verb phrase answering 為者 (*wéi zhě* — "those who handle it"), so *Grammar overrides a lock* (`process/skills/glossary-entry/SKILL.md` → *How the locks behave*) applies, as it does for 弱其志 (*ruò qí zhì* — "weaken their ambition"). The current *does not do* is no closer to the lock.

#### T3-10 · Ch 22 / 24 — 彰 (*zhāng* — to shine forth)

**Leave, and the row is closed** (`WORKLIST-CLOSED.md`). Recorded in `chapters/024.md`: the subjects genuinely differ, Wang Bi supplying *their rightness* at 22 and Heshang Gong the person at 24, and an earlier repair that forced them together was withdrawn.

#### T3-11 · 是謂 (*shì wèi* — "this is called")

- **13 — leave.** 何謂…是謂… (*hé wèi… shì wèi…* — "what is meant by… this is what is meant by…") is a question-and-answer frame, and *What does it mean… / This is what is meant* keeps it. Record that as the reason; `chapters/013.md` records only that *this is why* was refused.
- **14 — resolve.** *"This is called the shape of no-shape, the image of no-thing. / This is called the elusive."* The Chinese says *this is called* twice in two lines, and so should the English.
- **27 — resolve**, under T3-16.
- **53 — leave.** Recorded: *exposes* is a deliberate departure (`notes/translation.md` → 是謂 (*shì wèi*) at ch 53), on grammar and force.
- **74 — leave.** Recorded: the line was built as *a clean equation, place for place, which is what 是謂 (shì wèi) asks for* (`notes/translation.md` → *Ch 74*).
- **78 — resolve, minimally:** *"whoever takes on the shame of the state / is called the keeper of the soil and the grain. / Whoever takes on the ill omen of the state / is called the ruler of the world."* *Is called* is the formula's own form at 59 and 65, and it keeps *whoever*.

#### T3-13 · the other series members

- **20, 相去 (*xiāng qù* — "how far apart") ×2 — leave, and the verdict is now *kept*.** The Chinese varies its own second word, 幾何 / 若何 (*jǐ hé / ruò hé* — "how much / how"), and the English follows (§13).
- **41, 大白 (*dà bái* — great white) — leave.** Recorded, Shalom's call 2026-09-07: *the great white* imports an English phrase with a racial history, and *the whitest white* is a deliberate exception to 大 (*dà*)'s lock.
- **56, 不可得而 (*bù kě dé ér* — "cannot be made to") ×6 — resolve.** *"They cannot be drawn near, and cannot be held off. / They cannot be benefited, and cannot be harmed. / They cannot be honored, and cannot be debased. / And so they become the most honored in the world."* Six *cannot*s for six. The subject *they* is the people the line before describes; the current *You cannot…* puts the reader in a sentence the Chinese does not.
- **63, 味無味 (*wèi wú wèi* — "taste the flavorless") — leave, and rewrite the reason.** The recorded reason is a chime with ch 35's *bland and flavorless*, and ch 35 no longer says *flavorless*: it reads *It has no flavor*. The rendering still stands on its own: 無味 (*wú wèi*) is a noun, *no flavor*, so *taste the not-tasting* would misread it, and *flavorless* is the honest English.
- **71, 知不知 / 不知知 (*zhī bù zhī / bù zhī zhī* — "knowing not-knowing / not knowing knowing") — leave.** Recorded in `chapters/071.md`: *claim to know* follows Heshang Gong, who reads 言 (*yán* — to say) into both halves, and the reversal is held at the front of each line.

#### T3-14 · Departures whose reasons are owed

- **兮 (*xī* — the sung pause) — leave everywhere but ch 17, with this reason.** *"兮 (xī) is a held breath with no meaning of its own, and English has no word for it. A held breath is what punctuation is for, so the English gives it a mark instead: a comma after a bare adjective (4, 15), a full stop (25), an exclamation (20). Where it falls inside a line rather than closing a word (14, 34), the line's own pause carries it. At 58, 禍兮 (huò xī — "disaster!") holds a topic up, and the English names the topic."*
- **Ch 17's 悠兮 (*yōu xī* — "unhurried!") — resolve.** The pause went, and so did its adjective, 悠 (*yōu* — unhurried). *"Unhurried, they hold their words precious."* This restores 貴 (*guì* — to prize) too, which *speak sparingly* had turned into a description.
- **Ch 50's 生生之厚 (*shēng shēng zhī hòu* — "the thickness of their living life") — resolve.** *"Why? Because they live life too thickly."* English has the figure this one needs: *live life* is a verb taking its own noun, and 厚 (*hòu*) is *thick* at ch 38. Ch 75's 求生之厚 (*qiú shēng zhī hòu* — "seeking life's thickness"), *want their own lives so rich*, can stay: it is a different verb, and *rich* there is what the rulers want.
- **The rhyme claim at ch 6 — confirmed.** Zhu Qianzhi's critical edition records Jiang Yougao's reading: 門 根 存 勤 (*mén gēn cún qín* — gate, root, exist, strain) in the 文 (*wén*) group, as the audit said, and 死 / 牝 (*sǐ / pìn* — die / female) rhyming in the 脂 (*zhī*) group, with 牝 (*pìn*) read like 匕 (*bǐ*). So **a second rhyme binds lines 1 and 2**, which the 4 / 2 stanza layout keeps together. No change. Yao Wentian agrees with Jiang.

#### T3-17 · Verbatim phrases across chapters

- **孤、寡、不穀** (*gū, guǎ, bù gǔ* — "orphaned, lone, unworthy"), 39 · 42 — **resolve** ch 42 to *"orphaned, alone, or unworthy"*. 寡 (*guǎ*) here is the ruler's self-name, 寡人 (*guǎ rén* — "the lone one"), so *alone* is the word.
- **禍莫大於** (*huò mò dà yú* — "no disaster greater than"), 46 · 69 — **resolve** ch 69 to *"There is no greater disaster than making light of the enemy."* The note says it was matched on purpose; the page drifted.
- **不言之教** (*bù yán zhī jiào* — "the teaching without words"), 2 · 43 — **resolve** ch 43 to *"The teaching without words, the benefit of non-doing —"*.
- **生而不有**, 2 · 10 · 51 — **resolved** under T3-13 above.
- **不自見** (*bù zì jiàn* — "do not show themselves"), 22 · 24 · 72 — **resolve** ch 72 to *"knows themselves and does not show themselves off"*. Its notes argue for *display* as a concept and never as against ch 22's English.
- **▢之又▢** (*▢ zhī yòu ▢* — "▢, and ▢ again"), 1 · 48 — **resolve** ch 48 to *"Decrease, and decrease again, until you reach non-doing."*
- **取天下 … 以無事** (*qǔ tiān xià… yǐ wú shì* — "take the world… by not meddling"), 48 · 57 — **leave, and record why.** Ch 48 states how the world is won and chose the receptive *comes to you* (recorded). Ch 57's line closes a series of three imperatives, *Govern… wage war… win*, and needs an active verb in the series' own voice. **But** ch 29's *take the world* is the third English of 取天下 (*qǔ tiān xià*), and the note at 取天下 (*qǔ tiān xià*) leaves that open: settle it there.
- **抱一** (*bào yī* — "embrace one"), 10 · 22 — **leave; the verdict is now *departed*.** The lock carries *one thing (ch 22)* as a flexion, so the split is data, not drift.
- **扔** (*rēng* — to pull), 38 · 69 — **resolve** ch 69 to *"dragging where there is no enemy"*.
- **功成** (*gōng chéng* — "the work done"), 2 · 34 · 77 — **resolve** with ch 34, under T3-18.
- **民不畏** (*mín bù wèi* — "the people do not fear"), 72 · 74 — **resolve** ch 72 to *"When the people do not fear authority"*. *No longer* adds a before and after that neither chapter has.
- **是謂玄德** (*shì wèi xuán dé* — "this is called profound integrity"), 10 · 51 · 65 — **resolve** ch 65 to *"Always to know the pattern — / this is called profound integrity."* The dash is the topic–comment shape standing rule 3 allows, as at 10 and 51.
- **利器** (*lì qì* — sharp tools), 36 · 57 — **resolve, with less confidence:** ch 57 to *"The more tools of advantage the people have, the more clouded the state becomes."* 器 (*qì*) is locked to *vessel / tool*, and *weapons* is 兵 (*bīng*)'s English. Wang Bi reads ch 57's 利器 (*lì qì*) as tools for one's own advantage, which *tools of advantage* says. The cost is the sharper image.

#### T3-18 · One member out of step

- **2, 斯不善已 (*sī bù shàn yǐ* — "this is already not-good") — resolve:** *"When the world knows good as good, the not-good arises."* The lock allows *good* where the text names the category, and it does; the negation of the line's own word is the point.
- **9 — resolve:** *"Fill what you hold to the brim, and you would do better to stop. / Hammer a point ever sharper, and it will not keep for long."* Both halves now run *do X, and Y*.
- **10, 能無離乎 (*néng wú lí hū* — "can you be without parting?") — resolve:** *"Housing your aliveness and embracing the one, can you be undivided?"* All four 能無 (*néng wú* — "can you be without") then read *can you be…*.
- **12, 令人行妨 (*lìng rén xíng fáng*) — leave.** Recorded: *the fifth* makes *is carried by the verb* (`chapters/012.md`, Shalom's call 2026-10-20).
- **13, the second 天下 (*tiān xià* — the world) — resolve:** *"…can be trusted with the world."* in both lines. 寄 / 託 (*jì / tuō*) as *trusted with* stays, as recorded.
- **17, the ladder — resolve:**

> Of the highest, those below know only that they are there.  
> Next, those who are loved and praised.  
> Next, those who are feared.  
> Next, those who are despised.

  The rungs are named by position, as 其次 (*qí cì* — the next) names them, and *leaders*, which has no character here (`notes/translation.md` → 王 (*wáng* — ruler)), goes.
- **25, 獨立而不改，周行而不殆 (*dú lì ér bù gǎi, zhōu xíng ér bù dài*) — resolve:** *"Silent. Empty. / It stands alone and never changes. / It moves in a circle and is never in danger, / and can be taken as the mother of the world."* 寂兮寥兮 (*jì xī liáo xī* — "silent! empty!") keeps its two full stops.
- **26, 輜重 (*zī zhòng*) — resolve:** *"travels all day without leaving the heavy wagons."* *Heavy* comes back from line 1, which is why the noble keeps to them.
- **30, 強 (*qiáng* — to force) ×3 — resolve,** to the lock's *forcing*: *"does not force the world with arms"*, *"succeeds and stops there, and never pushes on to take by force"*, *"They succeed without forcing."* *Never pushes on* is 不敢 (*bù gǎn*), locked to *push*.
- **34, 而不為主 (*ér bù wéi zhǔ* — "and does not act as master") ×2 and 功成 (*gōng chéng* — "the work done") — resolve:**

> The countless things rely on it to live, yet it refuses none.  
> The work is done, and it does not claim to own it.  
> It clothes and nourishes the countless things, yet does not act as their master.  
> Ever desireless, it can be called small.  
> The countless things return to it, yet it does not act as their master: it can be called great.

  The two 為主 (*wéi zhǔ*) read alike, *owner* and *ownership* stop falling on two characters, and 功成 (*gōng chéng*) reads as at 2 and 77.
- **46, 不知足 (*bù zhī zú*) — resolve:** *"There is no greater disaster than not knowing you have enough,"* the lock's own words, so the closing 知足之足 (*zhī zú zhī zú*) answers it.
- **49, 亦 (*yì* — also) — resolve:** *"the untrustworthy, I trust too."*
- **50, 無死地 (*wú sǐ dì* — "no deadly ground") — resolve:** *"Why? Because in them there is no deadly ground."* The chapter's last words answer its first stanza again.
- **51, 道生之，德畜之 (*dào shēng zhī, dé xù zhī*) — resolve:** the second reads *"Thus, the Tao gives birth to them and integrity rears them,"* as the first does.
- **55, 益生曰祥 (*yì shēng yuē xiáng* — "increasing life is called ominous") — resolve:** *"Increasing life is called an ill omen."* The four 曰 (*yuē*) then all read *is called*, and *force*, which belongs to 強 (*qiáng*) two lines later, leaves this line.
- **57, 我無▢ (*wǒ wú ▢*) ×3 — resolve:** *"I do not desire, and the people become uncarved of themselves."* *I do not do · I do not meddle · I do not desire*. The cost: 無欲 (*wú yù*) reads *desireless* at 1, 3 and 34. For *uncarved*, see T3-19.
- **60, 不傷人 (*bù shāng rén* — "does not harm people") ×3 — resolve:** *"their potency does no harm to people, / not only does their potency do no harm to people, the sage, too, does no harm to people."* The chain then repeats word for word, as the Chinese does.
- **65, 國之賊 / 國之福 (*guó zhī zéi / guó zhī fú*) — leave.** Recorded (`notes/translation.md` → *Ch 65*): *robs the state / is the state's good fortune* was built deliberately as the pair, on the way out of the overlay *blessing* for 福 (*fú* — good fortune).
- **77, 損 / 補 (*sǔn / bǔ*) — resolve:** *"What is too much is taken from. What is too little is mended."* 補 (*bǔ*) is *mends* by a recorded call (`chapters/077.md`), so the bow image takes the law's verbs.
- **80, 相 (*xiāng* — each other) ×3 — leave.** Recorded at length (`notes/translation.md` → 不相往來 (*bù xiāng wǎng lái* — "do not go to and fro")): *never once go next door* names the motion and its destination, which *visit one another* did not.

#### T3-19 · The book's images

- **門 (*mén* — gate) at 52 and 56 — resolve:** *"Block the openings, close the gates."* It joins the gate of 1, 6 and 10, the body's openings read as the same gates. It has no lock; this would make it one.
- **樸 (*pǔ*) at 57 — resolve,** with T3-18's ch 57: *"…and the people become uncarved of themselves."* It is the lock's English, and the image the book has been building since ch 15.

#### T5-14 · An echo the Chinese does not make

- **Ch 4, 象帝之先 (*xiàng dì zhī xiān* — "an image of what came before the gods") — resolve:** *"It is the image of what came before any god."* *Seems* then belongs to 似 (*sì* — to resemble) alone, and 象 (*xiàng*) reads *image*, as at 14, 21, 35 and 41. 帝 (*dì*) keeps its lock, *any god*.

#### T2-67 and §6 · The doubled characters

*Shalom's call: decided line by line. Ch 58's pairs are the model for the ones worth carrying: two English words for one doubled character.*

| Ch | Doubling | Recommendation |
|---|---|---|
| 6 | 綿綿 (*mián mián* — unbroken, like a drawn thread) | **Resolve:** *"Unbroken and fine, it seems to be here, / use it, and there is no strain."* *Fine* is in the graph (the Shuowen's 聯微也 (*lián wēi yě*), *"joined and fine"*), and *seems to be here* is ch 4's English for 似或存 (*sì huò cún* — "seems perhaps to be here"), beside this line's 若存 (*ruò cún* — "seems to be here") |
| 14 | 繩繩 (*shéng shéng* — cord upon cord) | **Resolve:** *"Strand upon strand, it cannot be named"*. *Flowing* has no water in it; the doubled cord is the image |
| 16 | 芸芸 (*yún yún* — teeming) | **Resolve:** *"Things teem and flourish, / each returns again to its root."* *Come to their fullest* was 盈 (*yíng* — full)'s word, and 盈 (*yíng*) is not here |
| 20 | 熙熙, 傫傫, 沌沌 (*xī xī, lěi lěi, dùn dùn* — merry, drooping, muddled) | **Leave.** Single words, carried by the similes and by *How muddled!* |
| 20 · 58 | 昭昭 / 昏昏, 察察 / 悶悶 (*zhāo zhāo / hūn hūn, chá chá / mèn mèn* — bright / clouded, sharp / dull) | **Leave ch 20; resolve ch 58 to match it,** so 察察 (*chá chá*) and 悶悶 (*mèn mèn*) read *sharp* and *dull* in both: *"When the government is dull, the people are simple. / When the government is sharp, the people are wanting."* 淳淳 (*chún chún* — simple) and 缺缺 (*quē quē* — lacking) then read alike too, and *turn cunning*, which no character says, goes |
| 39 | 琭琭 / 珞珞 (*lù lù / luò luò* — gleaming / rough) | **Leave.** *Gleaming like jade / common like stone* gives each its simile |
| 49 | 歙歙 (*xī xī* — drawing in) | **Leave.** *Breathes gently* is the drawing-in |
| 73 | 恢恢 (*huī huī* — vast and wide) | **Leave.** *Vast*, and the next line's *wide* carries the second beat |

#### Settled already — departed by a recorded decision

So that the count is whole: 1's verb 道 (*dào*); 12's *hinder*; 13's 寄 / 託 (*jì / tuō*) and its 是謂 (*shì wèi*); 22's 抱一 (*bào yī*); 26's 根 / 本 (*gēn / běn*); 28's 白 (*bái* — white) for 榮 (*róng* — glory), a text decision; 38's cascade; 41's *whitest white*; 48's *comes to you*; 53's *exposes*; 62's 寶 / 保 (*bǎo*); 63's *flavorless*; 64's *learns to unlearn*; 65's *robs*; 69's 兵 (*bīng*); 71's trailing 是以不病 (*shì yǐ bù bìng*) and its *claim to know*; 72's 威 (*wēi*) and 厭 (*yàn*); 74's equation; 75's refrain; 80's *next door*; rhyme everywhere. Each is in the readings, with where it is recorded.

---

### The readings, chapter by chapter

*Each reading names the devices, then the verdicts. Rhyme is left out: it is departed by policy everywhere (§7). Where a verdict rests on a decision already made, the reading says where it is recorded.*

#### Ch 1
**Kept:** the couplet 道可道 / 名可名 (*dào kě dào / míng kě míng* — "the Tao that can be tao-ed / the name that can be named"), both halves ending *is not the ever-present* ▢. The couplets 無名 / 有名 (*wú míng / yǒu míng* — "the nameless / the named") and 常無欲 / 常有欲 (*cháng wú yù / cháng yǒu yù* — "ever desireless / ever desiring"). **Departed:** the verb 道 (*dào* — to tell) as *made a way*, recorded in the chapter's notes. **Lost:** the chain 同謂之玄。玄之又玄 (*tóng wèi zhī xuán. xuán zhī yòu xuán* — "together they are called dark. Dark, and dark again") keeps its words, *profound darkness* / *Dark*, but a stanza break falls between them (T3-15). And the frame ▢之又▢ (*▢ zhī yòu ▢* — "▢, and ▢ again") reads *Dark, and dark again* here and *Decreasing and decreasing* at ch 48 (T3-17).

#### Ch 2
**Kept:** the couplet 美之為美 / 善之為善 (*měi zhī wéi měi / shàn zhī wéi shàn* — "beauty as beauty / good as good"); the six 相 (*xiāng* — each other); the chain 弗居。夫唯弗居 (*fú jū. fū wéi fú jū* — "does not stay. Only because it does not stay"); 夫唯 (*fū wéi* — only because). **Lost:** the 而弗 (*ér fú* — "and does not") series, one member out (T3-13), and that member is the book-wide formula 為而不恃 (*wéi ér bù shì* — "acts, yet does not rely on it"), so the fix decides chs 10, 51 and 77 too. 生而弗有 (*shēng ér fú yǒu* — "gives life, and does not possess") reads *They are born, and the sage does not possess them*, where 10 and 51 read *giving birth without possessing* (T3-17). 斯不善已 (*sī bù shàn yǐ* — "this is already not-good") reads *the bad arises*, so the negation of the line's own word is gone (T3-18). 不言之教 (*bù yán zhī jiào* — the teaching without words) reads *the teaching without words* here and *the wordless teaching* at 43 (T3-17).

#### Ch 3
**Kept:** the series 不▢…使民不▢ (*bù ▢… shǐ mín bù ▢* — "not ▢… so the people do not ▢") ×3; the couplets 虛其心，實其腹 / 弱其志，強其骨 (*xū qí xīn, shí qí fù / ruò qí zhì, qiáng qí gǔ* — "empty their hearts, fill their bellies / weaken their ambition, strengthen their bones"); 為無為 (*wéi wú wéi* — "do the not-doing"), the same English as ch 63; 治 (*zhì* — govern) turned to 無不治 (*wú bù zhì* — "nothing ungoverned"). **Lost:** 是以聖人之治 (*shì yǐ shèng rén zhī zhì* — "therefore the sage's governing") reads *This is how the sage governs:*, the formula's fifth shape in the book (T3-12).

#### Ch 4
**Kept:** the pair 淵兮，似… / 湛兮，似… (*yuān xī, sì… / zhàn xī, sì…* — "deep, it seems… / submerged, it seems…"), *Fathomless, it seems… / Submerged, it seems…*; the four-member series 挫其銳…同其塵 (*cuò qí ruì… tóng qí chén* — "blunt the sharpness… same as the dust"), two to a line, as at ch 56. **Departed, reason owed:** 兮 (*xī* — the sung pause), carried by the comma (T3-14). **Invented echo:** 象帝之先 (*xiàng dì zhī xiān* — "an image of what came before the gods") reads *It seems older*, so *seems* stands three times for two 似 (*sì* — to resemble) and one 象 (*xiàng* — image) (T5-14).

#### Ch 5
**Kept:** the couplet 天地不仁 / 聖人不仁 (*tiān dì bù rén / shèng rén bù rén* — "sky and earth are not humane / the sage is not humane"), each closing on *straw dogs*; the question 其猶橐籥乎 (*qí yóu tuó yuè hū* — "is it not like a bellows?"); the pair 虛而不屈，動而愈出 (*xū ér bù qū, dòng ér yù chū* — "empty and not depleted, moving and yielding more").

#### Ch 6
See *Chapter 6* above. Chain kept; doubling open (T2-67). The second read confirmed the rhyme behind the 4 / 2 layout and found a second one, 死 / 牝 (*sǐ / pìn* — die / female), binding lines 1 and 2 (§7).

#### Ch 7
**Kept:** 天長地久 (*tiān cháng dì jiǔ* — "sky long, earth lasting") picked up as *last and endure*; the couplet 後其身而身先 / 外其身而身存 (*hòu qí shēn ér shēn xiān / wài qí shēn ér shēn cún* — "puts their body last and it comes first / puts their body outside and it survives"); the turn on 私 (*sī* — the private self), *no private self… their private self is fulfilled*; 故能 (*gù néng* — "and so can") twice as *and so*.

#### Ch 8
**Kept:** the seven 善 (*shàn* — masterful at); the ring on 不爭 (*bù zhēng* — does not contend), which opens and closes the chapter in one English; 夫唯 (*fū wéi* — only because) as *Only because*.

#### Ch 9
**Lost:** two couplets lose their shape. 持而盈之，不如其已；揣而銳之，不可長保 (*chí ér yíng zhī, bù rú qí yǐ; chuǎi ér ruì zhī, bù kě cháng bǎo* — "hold it and fill it, better to stop; hammer it and sharpen it, it cannot keep long") reads *Rather than keep filling what you hold, stop* against *Hammer a point ever sharper, and it will not keep for long*: one half inverted, the other not (T3-18). **Kept:** the second couplet, *Gold and jade fill the hall… / Grow arrogant with wealth…*; 天之道 (*tiān zhī dào* — "the way of the sky") as *the way of nature*, as at 47, 73, 77, 79 and 81.

#### Ch 10
**Kept:** the six questions 能▢乎 (*néng ▢ hū* — "can you ▢?"); the closing 生而不有，為而不恃，長而不宰 (*shēng ér bù yǒu, wéi ér bù shì, zhǎng ér bù zǎi* — "gives life and does not possess, acts and does not rely, grows and does not rule"), word for word as ch 51; 是謂玄德 (*shì wèi xuán dé* — "this is called profound integrity") with its dash. **Lost:** of the four 能無▢乎 (*néng wú ▢ hū* — "can you be without ▢?"), three read *can you be…* and the first reads *can you keep these from parting?* (T3-18). The closing series breaks in its middle member, as at ch 2 (T3-13). 抱一 (*bào yī* — embrace one) reads *embracing the one*, where ch 22's recorded call made it *one thing*; the call's reason is ch 22's own 少 / 多 (*shǎo / duō* — little / much), which ch 10 does not have, so the split may be licensed, but it is not yet recorded (T3-17).

#### Ch 11
**Kept**, since 2026-09-05 (`DISCOVERIES.md` §6).

#### Ch 12
**Kept:** 五▢令人▢▢ (*wǔ ▢ lìng rén ▢ ▢* — "the five ▢ make people's ▢ ▢") ×3; 為腹不為目 (*wèi fù bù wèi mù* — "for the belly, not for the eye"); 去彼取此 (*qù bǐ qǔ cǐ* — "let go of that, take this") in one English at 12, 38 and 72. **Departed:** 令人 (*lìng rén* — "makes people") stands five times. Four read *makes people's…*; the fifth, 令人行妨 (*lìng rén xíng fáng* — "makes people's conduct hindered"), reads *Rare goods hinder people's conduct*, on Shalom's call (2026-10-20): *the fifth* makes *is carried by the verb* (`chapters/012.md`).

#### Ch 13
**Kept:** 寵辱若驚 (*chǒng rǔ ruò jīng* — "favor and disgrace are both a shock") ×3 and 貴大患若身 (*guì dà huàn ruò shēn* — "prize great trouble as your body") ×2, one English each; the two 何謂 (*hé wèi* — "what does it mean") questions; 得之若驚，失之若驚 (*dé zhī ruò jīng, shī zhī ruò jīng* — "getting it, a shock; losing it, a shock"). **Kept, the strands (§11):** the two sayings are asked about in turn and answered in their own words. **Departed:** 是謂 (*shì wèi* — "this is called") as *This is what is meant*, answering the 何謂 (*hé wèi* — "what does it mean") question in its own frame; and 寄 (*jì* — to lodge with) and 託 (*tuō* — to entrust to) both as *trusted with*, because Wang Bi swaps them (`chapters/013.md`). **Lost:** the second 天下 (*tiān xià* — the world) becomes *it* (T3-18).

#### Ch 14
**Kept:** the series 視之不見，名曰夷 (*shì zhī bù jiàn, míng yuē yí* — "look and do not see it, its name is the invisible") ×3; 其上 / 其下 (*qí shàng / qí xià* — "its top / its bottom"); 無狀之狀 (*wú zhuàng zhī zhuàng* — "the shape of no-shape"); 迎之 / 隨之 (*yíng zhī / suí zhī* — "meet it / follow it"); 古 / 今 (*gǔ / jīn* — ancient / now). **Lost:** 是謂 (*shì wèi* — this is called) as *This is the shape…*, one of three (T3-11). **Noted:** the doubling 繩繩 (*shéng shéng* — cord upon cord), §6. **Departed, reason owed:** 兮 (*xī*), dropped (T3-14).

#### Ch 15
**Kept:** the seven 兮 (*xī*) likenesses, one per line; the two chains through 夫唯 (*fū wéi* — only because), *could not be read. / Only because they could not be read* and *no wish to be full. / Only because they are never full*; the two questions 孰能 (*shú néng* — "who can"). **Departed, reason owed:** 兮 (T3-14).

#### Ch 16
**Kept:** the couplet 致虛極，守靜篤 (*zhì xū jí, shǒu jìng dǔ* — "reach emptiness to the utmost, hold stillness steadily"); every link of the chain, §1; the refrains 知常曰明 (*zhī cháng yuē míng* — "knowing the ever-present is called clear-seeing", as at 55) and 沒身不殆 (*mò shēn bù dài* — "to the end of your days, no danger", as at 52); 是謂 (*shì wèi*). **Noted:** 芸芸 (*yún yún* — teeming), §6.

#### Ch 17
**Lost:** the ladder 太上…其次…其次…其次 (*tài shàng… qí cì…* — "the highest… the next… the next… the next") names its rungs by position, and the English names them by grade, *Good… Poor… The worst*. The three 其次 (*qí cì* — the next) get three Englishes, and *good* and *poor* add a verdict the Chinese leaves to the order (T3-18). **Kept:** 信不足焉，有不信焉 (*xìn bù zú yān, yǒu bù xìn yān* — "where trust is not enough, there is no trust"), the same English as ch 23. **Departed, reason owed:** 悠兮 (*yōu xī* — "unhurried!"), the sung pause absorbed into *speak sparingly* (T3-14).

#### Ch 18
**Kept:** the four 有▢ (*yǒu ▢* — "there is ▢"), each *…appear*.

#### Ch 19
**Kept:** 絕▢棄▢ (*jué ▢ qì ▢* — "cut off ▢, abandon ▢") ×3; 孝慈 (*xiào cí* — devotion and tenderness) as at ch 18; 見素抱樸 (*jiàn sù bào pǔ* — "see the undyed silk, embrace the uncarved wood").

#### Ch 20
**Kept:** 我獨 (*wǒ dú* — "I alone") ×6, *I alone…* every time; 眾人 (*zhòng rén* — the crowd) ×3; 俗人 (*sú rén* — the worldly) ×2; 如…如… (*rú… rú…* — "as if… as if…"); 人之所畏，不可不畏 (*rén zhī suǒ wèi, bù kě bù wèi* — "what people fear must be feared"). **Kept (§13):** 相去 (*xiāng qù* — "how far apart") ×2 reads *how much distance?* and *how far apart?*, following the Chinese's own variation, 幾何 / 若何 (*jǐ hé / ruò hé* — "how much / how"). The seed scan's *lost* is withdrawn. **Noted:** six doublings, §6. **Departed, reason owed:** 兮 (*xī*) ×6 (T3-14).

#### Ch 21
**Kept:** 惟恍惟惚 (*wéi huǎng wéi hū* — "only vague, only elusive"); the reversal 惚兮恍兮 / 恍兮惚兮 (*hū xī huǎng xī / huǎng xī hū xī* — "elusive, vague / vague, elusive"); 其中有 (*qí zhōng yǒu* — "within it there is") ×4; the chain 有精；其精 (*yǒu jīng; qí jīng* — "there is vital essence; its essence"); 眾甫 (*zhòng fǔ* — the father of the many) ×2; 吾何以知…以此 (*wú hé yǐ zhī… yǐ cǐ* — "how do I know… by this"). **Departed, reason owed:** 兮 (T3-14).

#### Ch 22
**Kept:** ▢則▢ (*▢ zé ▢* — "▢, and then ▢") ×6; 不自▢，故▢ (*bù zì ▢, gù ▢* — "they do not ▢ themselves, and so ▢") ×4; the ring on 曲則全 (*qū zé quán* — "bend, and stay whole"); the chain 不爭，故天下莫能與之爭 (*bù zhēng, gù tiān xià mò néng yǔ zhī zhēng* — "they do not contend, so no one in the world can contend with them"), the same English as ch 66; 為天下式 (*wéi tiān xià shì* — "serve as the world's pattern"), as at ch 28. **Departed:** 抱一 (*bào yī*) as *embraces one thing*, recorded in `notes/translation.md` → 抱一 (*bào yī* — embrace one). **Departed:** 彰 (*zhāng* — to shine forth) against ch 24, recorded in `chapters/024.md`: the subjects differ, *their rightness* here and the person there. **Lost:** 不自見 (*bù zì jiàn* — "do not show themselves") reads *do not show themselves off* here and *does not display themselves* at ch 72 (T3-17).

#### Ch 23
**Kept:** the couplet 飄風不終朝，驟雨不終日 (*piāo fēng bù zhōng zhāo, zhòu yǔ bù zhōng rì* — "a squall does not last the morning, a downpour does not last the day"); the chain 天地。天地 (*tiān dì. tiān dì* — "sky and earth. Sky and earth"); 同於▢ (*tóng yú ▢* — "the same as ▢") ×3 and its mirror ▢亦樂得之 (*▢ yì lè dé zhī* — "▢ too gladly gets them") ×3; the refrain shared with ch 17.

#### Ch 24
**Kept:** 企者不立；跨者不行 (*qǐ zhě bù lì; kuà zhě bù xíng* — "those on tiptoe do not stand; those striding do not go"); three of the four pairs mirrored from ch 22; 物或惡之，故有道者不處 (*wù huò wù zhī, gù yǒu dào zhě bù chǔ* — "living things recoil from them, so those with the Tao do not dwell there"), word for word as ch 31. **Departed:** 彰 (*zhāng* — to shine forth), recorded; see ch 22.

#### Ch 25
**Kept:** 強字之 / 強為之名 (*qiǎng zì zhī / qiǎng wèi zhī míng* — "forcing a label on it / forcing a name on it"); the chain 大曰逝，逝曰遠，遠曰反 (*dà yuē shì, shì yuē yuǎn, yuǎn yuē fǎn* — "great means departing…"); the four 大 (*dà* — great); the chain 人法地… (*rén fǎ dì* — "humans model on earth…"). **Lost:** the chain 名曰大。大曰逝 (*míng yuē dà. dà yuē shì* — "named it great. Great means departing") keeps its words in place, *I call it great. / Great means departing*, but a stanza break falls between them (T3-15). The couplet 獨立而不改，周行而不殆 (*dú lì ér bù gǎi, zhōu xíng ér bù dài* — "stands alone and does not change, moves in a circle and is not endangered") is split: its first half joins the four fragments *Silent. Empty. Solitary. Unchanging.*, and its second becomes a sentence, *It moves in a circle, never in danger* (T3-18). **Departed, reason owed:** 寂兮寥兮 (*jì xī liáo xī* — "silent! empty!") carried by full stops (T3-14).

#### Ch 26
**Kept:** the couplet 重為輕根，靜為躁君 (*zhòng wéi qīng gēn, jìng wéi zào jūn* — "the heavy is the root of the light, stillness is the lord of the agitated") and its ring in the closing couplet, *Lightness loses the root. / Agitation loses the ruler*, all four words in place. **Lost, an echo:** 輜重 (*zī zhòng* — the baggage train, literally "the heavy wagons") carries line 1's 重 (*zhòng* — heavy), which is why the noble does not leave it; *baggage wagons* drops the weight. `chapters/026.md`'s notes chose the English and quotes Wang Bi's 以重為本故不離 (*yǐ zhòng wéi běn gù bù lí* — "takes the heavy as the base, so does not leave it"), but does not say the echo was let go (T3-18). **Departed (§13):** 根 / 本 (*gēn / běn* — root / base) both read *root*, which Wang Bi's same gloss licenses.

#### Ch 27
**Kept:** 善▢無▢ (*shàn ▢ wú ▢* — "masterful ▢ has no ▢") ×5 in its frame, four of them *uses no* or *leaves no*; 常善救人，故無棄人 / 常善救物，故無棄物 (*cháng shàn jiù rén, gù wú qì rén / … wù* — "always masterful at rescuing people, so no one is abandoned / … things"); 是謂襲明 (*shì wèi xí míng* — "this is called clarity worn covered"), matched with ch 52. **Lost:** the chiasmus 善人者，不善人之師；不善人者，善人之資 (*shàn rén zhě, bù shàn rén zhī shī; bù shàn rén zhě, shàn rén zhī zī* — "the masterful are the teachers of the unmasterful; the unmasterful are the material of the masterful"), and the next line's 師 / 資 (*shī / zī* — teacher / material) (T3-16). 善言無瑕謫 (*shàn yán wú xiá zhé* — "masterful speech has no flaw") reads *is flawless*, the one member out of the *uses no* frame (T3-18). 是謂要妙 (*shì wèi yào miào* — "this is called the essential subtlety") as *This is the essential secret*: the formula slips, and *secret* breaks 妙 (*miào*)'s lock, *subtle* (T3-11, T3-16).

#### Ch 28
**Kept:** the three stanzas on one frame, 知其▢，守其▢，為天下▢ (*zhī qí ▢, shǒu qí ▢, wéi tiān xià ▢* — "know the ▢, hold to the ▢, serve as the world's ▢"), every slot in place; the chain 為天下▢。為天下▢ (*wéi tiān xià ▢. wéi tiān xià ▢* — "serve as the world's ▢. Serve as the world's ▢") ×3; 常德 (*cháng dé* — the ever-present integrity) ×3; 復歸於 (*fù guī yú* — "return again to") ×3. The third stanza's 白 (*bái* — white) for 榮 (*róng* — glory) is a text decision, `notes/manuscript.md` → *Ch 28*. **Lost:** the fourth chain, 復歸於樸。樸散則為器 (*fù guī yú pǔ. pǔ sàn zé wéi qì* — "return to the uncarved wood. The uncarved wood scatters and becomes vessels"), crosses a stanza break, and closing it would make the third stanza longer than the first two (T3-15).

#### Ch 29
**Kept:** 不可為也，不可執也 / 為者敗之，執者失之 (*bù kě wéi yě, bù kě zhí yě / wéi zhě bài zhī, zhí zhě shī zhī* — "cannot be handled, cannot be grasped / those who handle it ruin it, those who grasp it lose it"), word for word as ch 64; 或▢或▢ (*huò ▢ huò ▢* — "some ▢, some ▢") ×4; 去 (*qù* — let go of) ×3.

#### Ch 30
**Kept:** 果而勿▢ (*guǒ ér wù ▢* — "succeed, and do not ▢") ×4, with 果而不得已 (*guǒ ér bù dé yǐ* — "succeed only because it is unavoidable") where the Chinese also breaks the frame; the chain 不道，不道早已 (*bù dào, bù dào zǎo yǐ* — "not-Tao; not-Tao ends early"); the refrain 物壯則老 (*wù zhuàng zé lǎo* — "things in their prime decay"), word for word as ch 55. **Lost:** 強 (*qiáng* — to force) binds the chapter, three times, and reads three ways, *dominate the world*, *seize dominance*, *excessive force*. Two of them are the lock's *forcing* flexion; *dominate* and *dominance* are not (T3-18).

#### Ch 31
**Kept:** 不祥之器 (*bù xiáng zhī qì* — "tools of ill omen") ×2; 貴左 / 貴右 (*guì zuǒ / guì yòu* — "prizes the left / the right"), 尚左 / 尚右 (*shàng zuǒ / shàng yòu* — "honors the left / the right"), 居左 / 居右 (*jū zuǒ / jū yòu* — "takes the left / the right"); the chain 美之…樂殺人。夫樂殺人者 (*měi zhī… lè shā rén. fū lè shā rén zhě* — "glorify it… delight in killing. Those who delight in killing"); 以喪禮處之 (*yǐ sàng lǐ chǔ zhī* — "place them by the rites of mourning") ×2; the refrain shared with ch 24.

#### Ch 32
**Kept:** the chain 有名，名亦既有 (*yǒu míng, míng yì jì yǒu* — "there are names; since names exist"); the chain 知止，知止 (*zhī zhǐ, zhī zhǐ* — "know when to stop; knowing when to stop"); 侯王若能守之，萬物將自▢ (*hóu wáng ruò néng shǒu zhī, wàn wù jiāng zì ▢* — "if rulers can hold to this, the countless things will ▢ of themselves"), word for word as ch 37.

#### Ch 33
**Kept:** the four couplets, each ▢者▢ (*▢ zhě ▢* — "one who ▢ is ▢"), with 知人 / 自知 (*zhī rén / zì zhī* — "knows others / knows themselves") and 勝人 / 自勝 (*shèng rén / zì shèng* — "overcomes others / overcomes themselves") mirrored. *Has force* for 有力 (*yǒu lì* — has strength) two lines above *forces themselves onward* for 強行 (*qiáng xíng* — presses on) is not an invented echo: `glossary/qiang-強.md` covers 力 (*lì* — force) inside 強's (*qiáng* — strong) own lock, so the two are kin by decision.

#### Ch 34
**Kept:** 可名於小 / 可名為大 (*kě míng yú xiǎo / kě míng wéi dà* — "can be called small / can be called great"); the chain 不自為大，故能成其大 (*bù zì wéi dà, gù néng chéng qí dà* — "does not make itself great, so it can complete its greatness"), matched with ch 63. **Lost:** 而不為主 (*ér bù wéi zhǔ* — "and does not act as master") stands twice and reads *claims no ownership*, then *Without acting as their master*; and 功成而不名有 (*gōng chéng ér bù míng yǒu* — "the work done, it does not claim to possess it") reads *It works without claiming to be the owner*, so *owner* and *ownership* fall on two different characters (T3-18). 功成 (*gōng chéng* — the work done) reads *The work is done* at 2 and 77 (T3-17). **Departed, reason owed:** 汎兮 (*fàn xī* — "overflowing!") (T3-14).

#### Ch 35
**Kept:** the chain 天下往。往而不害 (*tiān xià wǎng. wǎng ér bù hài* — "the world goes to it. Going, it is not harmed"), *comes to you. / It comes*; the series 視之 / 聽之 / 用之 (*shì zhī / tīng zhī / yòng zhī* — "look at it / listen for it / use it").

#### Ch 36
**Kept:** 將欲▢之，必固▢之 (*jiāng yù ▢ zhī, bì gù ▢ zhī* — "if you would ▢ it, you must first ▢ it") ×4; 是謂微明 (*shì wèi wēi míng* — "this is called the hidden clarity"). **Open:** 利器 (*lì qì* — sharp tools) reads *tools of advantage* here and *sharp weapons* at ch 57. The contexts differ, so this may be licensed, but it wants a verdict (T3-17).

#### Ch 37
**Kept:** the chain 無名之樸。無名之樸 (*wú míng zhī pǔ. wú míng zhī pǔ* — "the nameless uncarved wood. The nameless uncarved wood"); the refrain 無為而無不為 (*wú wéi ér wú bù wéi* — "non-doing, yet nothing left undone"), as at ch 48. **Lost:** the chain through 化 (*huà* — transform), T3-8.

#### Ch 38
**Kept:** 上德不德 (*shàng dé bù dé* — "high integrity does not do integrity"); the frame 上▢為之而▢以為 (*shàng ▢ wéi zhī ér ▢ yǐ wéi* — "the highest ▢ acts, and has ▢ to act for"); the cascade 失▢…失▢ (*shī* — lose), following Han Fei, `chapters/038.md`; 處其厚，不居其薄；處其實，不居其華 (*chǔ qí hòu, bù jū qí bó; chǔ qí shí, bù jū qí huá* — "dwells in the thick, not the thin; in the substance, not the blossom"); the refrain 去彼取此 (*qù bǐ qǔ cǐ*). **Open:** 攘臂而扔之 (*rǎng bì ér rēng zhī* — "bares its arms and pulls them along") reads *drags*, and ch 69's 攘無臂，扔無敵 (*rǎng wú bì, rēng wú dí* — "baring no arm, pulling no enemy") reads *baring an arm… hauling*, so 扔 (*rēng* — to pull) wears two Englishes (T3-17).

#### Ch 39
**Kept:** ▢得一以▢ (*▢ dé yī yǐ ▢* — "▢ got the one and so ▢") ×6 and its mirror ▢無以▢，將恐▢ (*▢ wú yǐ ▢, jiāng kǒng ▢* — "▢ with no way to ▢ is likely to ▢") ×6; 貴以賤為本，高以下為基 (*guì yǐ jiàn wéi běn, gāo yǐ xià wéi jī* — "the prized takes the cheap as root, the high takes the low as footing"), and its echo in the question; 數譽無譽 (*shù yù wú yù* — "count the cart, and there is no cart"), the polyptoton kept on the 輿 (*yú* — cart) reading. **Lost:** 孤、寡、不穀 (*gū, guǎ, bù gǔ* — "orphaned, lone, unworthy") reads *orphaned, alone, and unworthy* here and *orphaned, meager, or unworthy* at ch 42 (T3-17). **Noted:** 琭琭 / 珞珞 (*lù lù / luò luò* — gleaming / rough), §6.

#### Ch 40
**Kept:** the couplet 反者道之動，弱者道之用 (*fǎn zhě dào zhī dòng, ruò zhě dào zhī yòng* — "returning is the Tao's movement, yielding is the Tao's use"); the chain 生於有，有生於無 (*shēng yú yǒu, yǒu shēng yú wú* — "born from presence, presence born from absence").

#### Ch 41
**Kept:** 上士 / 中士 / 下士聞道 (*shàng / zhōng / xià shì wén dào* — "the highest / middling / lowest in service hear the Tao"); the chain 大笑之。不笑 (*dà xiào zhī. bù xiào* — "laugh aloud at it. Not laughed at"); the established sayings, one per line, each *seems*; the four 大▢ (*dà ▢* — the great ▢). **Departed:** 大白 (*dà bái* — great white) as *The whitest white*, Shalom's call (2026-09-07), recorded in the chapter's notes as a deliberate exception to 大 (*dà*)'s lock.

#### Ch 42
**Kept:** the chain 道生一… (*dào shēng yī* — "the Tao births one…"); the reversal 損之而益，益之而損 (*sǔn zhī ér yì, yì zhī ér sǔn* — "decreased and so increased, increased and so decreased"); 人之所教，我亦教之 (*rén zhī suǒ jiào, wǒ yì jiào zhī* — "what others teach, I also teach"). **Lost:** 孤、寡、不穀 (*gū, guǎ, bù gǔ* — "orphaned, lone, unworthy") against ch 39 (T3-17).

#### Ch 43
**Kept:** 天下之至柔 / 天下之至堅 (*tiān xià zhī zhì róu / zhì jiān* — "the softest in the world / the hardest in the world"); 無有入無間 (*wú yǒu rù wú jiàn* — "what has no presence enters what has no gap"); 無為之有益 / 無為之益 (*wú wéi zhī yǒu yì / wú wéi zhī yì* — "the benefit of non-doing") twice in one English. **Lost:** 不言之教 (*bù yán zhī jiào* — "the teaching without words") against ch 2 (T3-17).

#### Ch 44
**Kept:** the three questions ▢與▢孰▢ (*▢ yǔ ▢ shú ▢* — "▢ or ▢, which ▢?"); 甚愛必大費，多藏必厚亡 (*shèn ài bì dà fèi, duō cáng bì hòu wáng* — "great attachment surely costs much, much hoarding surely loses heavily"); 知足不辱，知止不殆 (*zhī zú bù rǔ, zhī zhǐ bù dài* — "know enough and no disgrace, know when to stop and no danger"), matched with chs 32 and 46; 可以長久 (*kě yǐ cháng jiǔ* — "and so can last long"), as at ch 59.

#### Ch 45
**Kept:** 大▢若▢ (*dà ▢ ruò ▢* — "great ▢ seems ▢") ×5; 其用不弊 / 其用不窮 (*qí yòng bù bì / bù qióng* — "in use it does not wear out / does not run dry"); 躁勝寒，靜勝熱 (*zào shèng hán, jìng shèng rè* — "movement overcomes cold, stillness overcomes heat"). 大直若屈 (*dà zhí ruò qū* — "great straightness seems bent") is a rider on T4-2: see ch 58.

#### Ch 46
**Kept:** 天下有道 / 天下無道 (*tiān xià yǒu dào / wú dào* — "when the world has the Tao / lacks the Tao"); 禍莫大於…咎莫大於 (*huò mò dà yú… jiù mò dà yú* — "no disaster greater than… no fault greater than"). **Lost:** 不知足 (*bù zhī zú* — not knowing enough) reads *discontent*, then 知足之足 (*zhī zú zhī zú* — "the enough of knowing enough") reads *the contentment of knowing you have enough*, so the line's own antithesis, not-knowing-enough against knowing-enough, is in two vocabularies (T3-18). 禍莫大於 (*huò mò dà yú* — "no disaster greater than") against ch 69 (T3-17).

#### Ch 47
**Kept:** 不出戶 / 不闚牖 (*bù chū hù / bù kuī yǒu* — "without going out the door / without looking out the window"); 其出彌遠，其知彌少 (*qí chū mí yuǎn, qí zhī mí shǎo* — "the further you go out, the less you know"); 不▢而▢ (*bù ▢ ér ▢* — "without ▢, ▢") ×3. **Kept, the strands (§11):** 出 (*chū* — go out) reads *venture*, and the closing 不行 (*bù xíng* — without going) reads *without venturing*. The first read called this an invented echo (T5-14); it is the going-out strand carried into the line that closes it, and the claim is withdrawn.

#### Ch 48
**Kept:** 為學日益，為道日損 (*wéi xué rì yì, wéi dào rì sǔn* — "pursuing learning, increase daily; pursuing the Tao, decrease daily"); the chain 無為。無為 (*wú wéi. wú wéi* — "non-doing. Non-doing"); the refrain shared with ch 37. **Departed:** 取天下 (*qǔ tiān xià* — "take the world") as *the world comes to you*, recorded in `notes/translation.md` → 取天下 (*qǔ tiān xià* — take the world). **Lost:** that note leaves 取天下 (*qǔ tiān xià*) across 29, 48 and 57 open. Ch 48's 取天下常以無事 (*qǔ tiān xià cháng yǐ wú shì* — "take the world always by not meddling") and ch 57's 以無事取天下 (*yǐ wú shì qǔ tiān xià* — "take the world by not meddling") are one claim in the same words, and read *the world always comes to you by not meddling* and *win the world by not meddling*. And ▢之又▢ (*▢ zhī yòu ▢* — "▢, and ▢ again") against ch 1 (T3-17).

#### Ch 49
**Kept:** the two stanzas on one frame, ▢者，吾▢之；不▢者，吾亦▢之；德▢ (*▢ zhě, wú ▢ zhī; bù ▢ zhě, wú yì ▢ zhī; dé ▢* — "the ▢, I ▢; the un-▢, I also ▢; integrity is ▢"); 以百姓心為心 (*yǐ bǎi xìng xīn wéi xīn* — "takes everyone's heart as their heart"). **Lost:** 亦 (*yì* — also) reads *too*, then *as well* (T3-18). **Noted:** 歙歙 (*xī xī* — drawing in), §6.

#### Ch 50
**Kept:** 出生入死 (*chū shēng rù sǐ* — "emerge into life, enter into death"); 十有三 (*shí yǒu sān* — "three in ten") ×3; 夫何故？以其 (*fū hé gù? yǐ qí* — "why? because they") ×2, *Why? Because…* both times; ▢無所▢其▢ (*▢ wú suǒ ▢ qí ▢* — "the ▢ has nowhere to ▢ its ▢") ×3. **Lost:** 死地 (*sǐ dì* — deadly ground) stands in the first movement and 無死地 (*wú sǐ dì* — "no deadly ground") ends the second; the English reads *deadly ground* and then *give death no foothold*, so the chapter's last words no longer answer its first stanza (T3-18). **Departed, reason owed:** 生生之厚 (*shēng shēng zhī hòu*), T3-14; ch 75's 求生之厚 (*qiú shēng zhī hòu* — "seeking life's richness") reads *want their own lives so rich*, which the reason should take into account.

#### Ch 51
**Kept:** 道生之，德畜之，物形之，勢成之 (*dào shēng zhī, dé xù zhī, wù xíng zhī, shì chéng zhī* — "the Tao births them, integrity rears them, matter forms them, circumstance completes them"); 尊道而貴德 / 道之尊，德之貴 (*zūn dào ér guì dé / dào zhī zūn, dé zhī guì* — "revere the Tao and value integrity / this reverence, this valuing"); ▢之▢之 (*▢ zhī ▢ zhī* — "▢ them and ▢ them") ×3; the closing as ch 10. **Lost:** 道生之，德畜之 (*dào shēng zhī, dé xù zhī*) is said twice, the second time as a summary, and reads *gives birth to*, then *births* (T3-18). The closing series, T3-13.

#### Ch 52
**Kept:** the reversal on 母 / 子 (*mǔ / zǐ* — mother / child); 沒身不殆 (*mò shēn bù dài*), word for word as ch 16; the couplet 塞其兌，閉其門 / 開其兌，濟其事 (*sè qí duì, bì qí mén / kāi qí duì, jì qí shì* — "block the openings, close the doors / open the openings, multiply your affairs"), and its refrain 終身不▢ (*zhōng shēn bù ▢* — "to the end of your days, not ▢"); 見小曰明，守柔曰強 (*jiàn xiǎo yuē míng, shǒu róu yuē qiáng* — "seeing the small is called clarity, holding to the soft is called strong"); 是謂襲常 (*shì wèi xí cháng* — "this is called the ever-present worn covered"), matched with ch 27. **Lost (§16):** 閉其門 (*bì qí mén* — "close the gates") reads *close the doors*, where 門 (*mén*) is *the gate* at 1, 6 and 10 (T3-19).

#### Ch 53
**Kept:** the series 朝甚除，田甚蕪，倉甚虛 (*cháo shèn chú, tián shèn wú, cāng shèn xū* — "the court very clean, the fields very overgrown, the granaries very empty"), one clause each, and the four-part series after it. **Departed:** 是謂盜夸 (*shì wèi dào kuā* — "this is called the boast of thieves") as *This exposes…*, recorded in `notes/translation.md` as a deliberate departure, on grammar and force.

#### Ch 54
**Kept:** 善建者不拔，善抱者不脫 (*shàn jiàn zhě bù bá, shàn bào zhě bù tuō* — "the well planted is not uprooted, the well held does not slip"); 修之於▢，其德乃▢ (*xiū zhī yú ▢, qí dé nǎi ▢* — "cultivate it in the ▢, and its integrity becomes ▢") ×5; 以▢觀▢ (*yǐ ▢ guān ▢* — "observe the ▢ through the ▢") ×5; *By this*, as at 21 and 57.

#### Ch 55
**Kept:** 毒蟲不螫，猛獸不據，攫鳥不搏 (*dú chóng bù shì, měng shòu bù jù, jué niǎo bù bó* — "venomous creatures do not sting, fierce beasts do not seize, birds of prey do not strike"); ▢之至也 (*▢ zhī zhì yě* — "this is ▢ at its utmost") ×2; the chain 知和曰常，知常曰明 (*zhī hé yuē cháng, zhī cháng yuē míng* — "knowing harmony is called the ever-present, knowing the ever-present is called clear-seeing"); the refrain shared with ch 30. **Lost:** the link 和之至也。知和 (*hé zhī zhì yě. zhī hé* — "harmony at its utmost. Knowing harmony") crosses a stanza break (T3-15). 曰 (*yuē* — is called) stands four times in two lines, and the third, 益生曰祥 (*yì shēng yuē xiáng* — "increasing life is called ominous"), reads *is an ill omen*, the one out of the *is called* run (T3-18).

#### Ch 56
**Kept:** the reversal 知者不言，言者不知 (*zhī zhě bù yán, yán zhě bù zhī* — "those who know do not speak, those who speak do not know"); 塞其兌，閉其門 (*sè qí duì, bì qí mén*), as at ch 52; the four from ch 4, two to a line, as at ch 4; 是謂玄同 (*shì wèi xuán tóng* — "this is called profound sameness"); 為天下貴 (*wéi tiān xià guì* — "the most honored in the world"), as at ch 62. **Lost:** 不可得而▢ (*bù kě dé ér ▢* — "cannot be made to ▢") ×6, T3-13; and 閉其門 (*bì qí mén*) as *close the doors*, as at ch 52 (T3-19).

#### Ch 57
**Kept:** 以正治國，以奇用兵，以無事取天下 (*yǐ zhèng zhì guó, yǐ qí yòng bīng, yǐ wú shì qǔ tiān xià* — "govern the state by the straight, wage war by surprise, take the world by not meddling"); *How do I know it is so? By this*; the four *The more…, the more…*; 而民自▢ (*ér mín zì ▢* — "and the people ▢ themselves") ×4. **Lost:** 我無▢ (*wǒ wú ▢* — "I do not ▢") stands three times and reads *I do not do*, *I do not meddle*, then *I am desireless* (T3-18). 民自樸 (*mín zì pǔ* — "the people become uncarved of themselves") reads *become plain*, the one place 樸 (*pǔ* — uncarved wood) loses its image (T3-19). 故聖人云 (*gù shèng rén yún* — "so the sage says"), T3-12. 以無事取天下 (*yǐ wú shì qǔ tiān xià* — "take the world by not meddling") against ch 48 and 利器 (*lì qì*) against ch 36 (T3-17).

#### Ch 58
**Kept:** the reversal 禍兮福之所倚，福兮禍之所伏 (*huò xī fú zhī suǒ yǐ, fú xī huò zhī suǒ fú* — "disaster, where fortune leans; fortune, where disaster hides"), with its 兮 (*xī*) as a held topic; 正復為奇，善復為妖 (*zhèng fù wéi qí, shàn fù wéi yāo* — "the straight turns crooked, the good turns monstrous"); 方而不割 (*fāng ér bù gē* — "square but does not cut") and three more on the frame ▢而不▢ (*▢ ér bù ▢* — "▢ but does not ▢"). **Lost:** the chain through 正 (*zhèng* — straight), T4-2. **A rider for T4-2:** the closing series' 直 (*zhí* — straight) also reads *straight*, three lines after 正 (*zhèng* — straight) does, and ch 45's 大直若屈 (*dà zhí ruò qū* — "great straightness seems bent") reads *straightness… crooked*, which is 正復為奇's (*zhèng fù wéi qí* — "the straight turns crooked") English too. So *straight* and *crooked* each carry two characters across 45 and 58, and whatever 正 / 奇 (*zhèng / qí*) becomes will have to sit beside 直 / 屈 (*zhí / qū* — straight / bent). **Noted:** 悶悶 / 淳淳 / 察察 / 缺缺 (*mèn mèn / chún chún / chá chá / quē quē* — dull / simple / sharp / lacking), §6.

#### Ch 59
**Kept:** every link of the sorites, §1; 莫若嗇。夫唯嗇 (*mò ruò sè. fū wéi sè* — "nothing like conserving. Only conserving"); 有國 (*yǒu guó* — have the state) ×2 as a link; 可以長久 (*kě yǐ cháng jiǔ*), as at ch 44; 是謂 (*shì wèi*).

#### Ch 60
**Kept:** the chain 其鬼不神；非其鬼不神，其神不傷人；非其神不傷人 (*qí guǐ bù shén; fēi qí guǐ bù shén, qí shén bù shāng rén; fēi qí shén bù shāng rén* — "the ghosts lose their potency; not only do the ghosts lose their potency, their potency does not harm people; not only does their potency not harm people"), every link in position. **Lost:** 不傷人 (*bù shāng rén* — "does not harm people") ×3 reads *causes no harm to people*, *do no harm*, *does no harm to people* (T3-18).

#### Ch 61
**Kept:** 天下之交，天下之牝 (*tiān xià zhī jiāo, tiān xià zhī pìn* — "the confluence of the world, the female of the world"); the chain 以靜…以靜 (*yǐ jìng* — by stillness); the chiasmus 大國以下小國…小國以下大國 (*dà guó yǐ xià xiǎo guó… xiǎo guó yǐ xià dà guó* — "the large state going below the small… the small going below the large"); 大國不過欲 / 小國不過欲 (*dà guó / xiǎo guó bù guò yù* — "the large / small state wants nothing more than").

#### Ch 62
**Kept:** 美言 / 美行 (*měi yán / měi xíng* — fine words / fine conduct); 此道 (*cǐ dào* — this Tao) ×2; 故為天下貴 (*gù wéi tiān xià guì*), as at ch 56. **Departed:** the sound-pair 寶 / 保 (*bǎo / bǎo* — treasure / keep safe), *treasure* and *keeps safe*, which keeps both senses and loses the chime; recorded in `notes/translation.md` → 寶 / 保 (*bǎo / bǎo* — treasure / keep safe), which also withdraws the claim that the pun is original.

#### Ch 63
**Kept:** 圖難於其易，為大於其細 (*tú nán yú qí yì, wéi dà yú qí xì* — "plan the difficult while it is easy, do the great while it is small") and its pair 天下難事 / 天下大事 (*tiān xià nán shì / dà shì* — "the world's difficult / great affairs"); 不為大，故能成其大 (*bù wéi dà, gù néng chéng qí dà*), as at ch 34; 是以聖人猶難之 (*shì yǐ shèng rén yóu nán zhī* — "so the sage still finds it difficult"), word for word as ch 73. **Departed, the reason to rewrite:** 味無味 (*wèi wú wèi* — "taste the flavorless") as *taste the flavorless*, an accepted departure in `notes/translation.md` whose recorded reason, a chime with ch 35's *flavorless*, has lapsed: ch 35 now reads *It has no flavor* (T3-13).

#### Ch 64
**Kept:** 其▢易▢ (*qí ▢ yì ▢* — "what is ▢ is easy to ▢") ×4; 為之於未有，治之於未亂 (*wéi zhī yú wèi yǒu, zhì zhī yú wèi luàn* — "handle it before it exists, order it before disorder"); the three images on ▢之▢，▢於▢ (*▢ zhī ▢, ▢ yú ▢* — "the ▢ of ▢ ▢ from ▢"); 為者敗之，執者失之 (*wéi zhě bài zhī, zhí zhě shī zhī*), word for word as ch 29; 未兆 (*wèi zhào* — no sign yet), *shows no sign*, as at ch 20. **Lost:** T3-9.

#### Ch 65
**Kept:** 以智治國 / 不以智治國 (*yǐ zhì zhì guó / bù yǐ zhì zhì guó* — "govern the state with guile / not with guile"); 稽式 (*jī shì* — the pattern) ×2; 深矣，遠矣，反矣 (*shēn yǐ, yuǎn yǐ, fǎn yǐ* — "deep, far, turned back"). **Lost:** the chain 玄德。玄德 (*xuán dé. xuán dé* — "profound integrity. Profound integrity") crosses a stanza break (T3-15). The pair's second half, 國之賊 / 國之福 (*guó zhī zéi / guó zhī fú* — "the state's thief / the state's good fortune"), reads *robs the state* against *is the state's good fortune*, a verb against a noun, **departed** as a pair built on purpose (`notes/translation.md` → *Ch 65*). 是謂玄德 (*shì wèi xuán dé*) reads *is called profound integrity*, without the *— / this is called* that chs 10 and 51 give the same three characters (T3-17).

#### Ch 66
**Kept:** the ring 能為百谷王 (*néng wéi bǎi gǔ wáng* — "can be king of the hundred valleys") ×2; 欲上民，必以言下之；欲先民，必以身後之 (*yù shàng mín, bì yǐ yán xià zhī; yù xiān mín, bì yǐ shēn hòu zhī* — "to be above the people, speak from below; to be ahead, put your body behind"); 處上 / 處前 (*chǔ shàng / chǔ qián* — "stands above / stands in front"); the refrain shared with ch 22. **Lost:** 是以聖人 (*shì yǐ shèng rén* — "therefore the sage") is dropped, *The sage stands above*, the one place in the book it has no English (T3-12).

#### Ch 67
**Kept:** the chain 似不肖。夫唯大，故似不肖 (*sì bù xiào. fū wéi dà, gù sì bù xiào* — "looks like nothing. Only because it is great does it look like nothing"); 一曰…二曰…三曰 (*yī yuē… èr yuē… sān yuē* — "the first is… the second… the third"); ▢故能▢ (*▢ gù néng ▢* — "▢, and so you can ▢") ×3; 捨▢且▢ (*shě ▢ qiě ▢* — "abandon ▢ and grab ▢") ×3; 慈 (*cí* — tenderness) ×6.

#### Ch 68
**Kept:** 善▢者，不▢ (*shàn ▢ zhě, bù ▢* — "the one masterful at ▢ does not ▢") ×4; 是謂 (*shì wèi*) ×3, *This is called* every time.

#### Ch 69
**Kept:** 不敢為主而為客；不敢進寸而退尺 (*bù gǎn wéi zhǔ ér wéi kè; bù gǎn jìn cùn ér tuì chǐ* — "I dare not be host but guest; I dare not advance an inch but retreat a foot"); ▢無▢ (*▢ wú ▢* — "▢ where there is no ▢") ×4; the chain 輕敵，輕敵 (*qīng dí, qīng dí* — "making light of the enemy; making light of the enemy"). **Lost:** 禍莫大於 (*huò mò dà yú* — "no disaster greater than") reads *There is no disaster greater than*, where ch 46 reads *There is no greater disaster than*, and `notes/translation.md` → *Ch 69* says the two were kept parallel on purpose. 扔 (*rēng*) against ch 38 (T3-17).

#### Ch 70
**Kept:** 甚易知，甚易行 / 莫能知，莫能行 (*shèn yì zhī, shèn yì xíng / mò néng zhī, mò néng xíng* — "very easy to know, very easy to follow / no one can know, no one can follow"), with 莫能行 (*mò néng xíng*) as at ch 78; 言有宗，事有君 (*yán yǒu zōng, shì yǒu jūn* — "words have an ancestor, affairs have a ruler"); 知我者希，則我者貴 (*zhī wǒ zhě xī, zé wǒ zhě guì* — "those who know me are few, those who pattern on me are precious").

#### Ch 71
**Kept:** 病病 (*bìng bìng* — "sick of the sickness") ×2 in one English. **Departed:** the trailing 是以不病 (*shì yǐ bù bìng* — "therefore not sick"), cut on Shalom's call, 2026-08-24, `notes/translation.md` → *Ch 75*. **Departed:** the mirror 知不知 / 不知知 (*zhī bù zhī / bù zhī zhī* — "knowing not-knowing / not knowing knowing") read with *claim to*, following Heshang Gong, and held at the front of each line (`chapters/071.md`).

#### Ch 72
**Kept:** 無狎其所居，無厭其所生 (*wú xiá qí suǒ jū, wú yàn qí suǒ shēng* — "do not crowd their dwellings, do not oppress their livelihoods"); 自知，不自見；自愛，不自貴 (*zì zhī, bù zì jiàn; zì ài, bù zì guì* — "knows themselves, does not display themselves; loves themselves, does not prize themselves"); 去彼取此 (*qù bǐ qǔ cǐ*). **Departed:** 威 (*wēi* — dread, authority) turned in 不畏威，則大威至 (*bù wèi wēi, zé dà wēi zhì* — "do not fear dread, and the great dread comes"), the repetition killed by Shalom as unworkable in English; and 厭 (*yàn* — to press down; to be fed up) turned in 夫唯不厭，是以不厭 (*fū wéi bù yàn, shì yǐ bù yàn*), split between *oppress* and *tire of*. Both are recorded in `notes/translation.md` → *Ch 72*. **Lost:** 不自見 (*bù zì jiàn*) against ch 22, and 民不畏 (*mín bù wèi* — "the people do not fear"), *no longer fear* here and *do not fear* at ch 74 (T3-17).

#### Ch 73
**Kept:** 勇於敢 / 勇於不敢 (*yǒng yú gǎn / yǒng yú bù gǎn* — "brave in daring / brave in not daring"); 此兩者 (*cǐ liǎng zhě* — "these two"), as at ch 1; 不▢而▢ (*bù ▢ ér ▢* — "does not ▢, yet ▢") ×4; 是以聖人猶難之 (*shì yǐ shèng rén yóu nán zhī*), as at ch 63. **Noted:** 恢恢 (*huī huī* — vast), §6.

#### Ch 74
**Kept:** 民不畏死 / 民常畏死 (*mín bù wèi sǐ / mín cháng wèi sǐ* — "the people do not fear death / always fear death"); the chain 代大匠斫。夫代大匠斫 (*dài dà jiàng zhuó. fū dài dà jiàng zhuó* — "carving in place of the master carpenter. Carving in place of the master carpenter"), its words kept, *of the master carpenter. / Of those who carve in place of the master carpenter*, though the link now falls mid-line. **Departed:** 是謂 (*shì wèi* — "this is called") as *is*, a line built as *a clean equation, place for place* (`notes/translation.md` → *Ch 74*). **Kept:** 民不畏 (*mín bù wèi* — "the people do not fear") reads *do not fear*; the slip is ch 72's (T3-17).

#### Ch 75
**Kept:** 民之▢，以其上▢ (*mín zhī ▢, yǐ qí shàng ▢* — "the people's ▢ is because those above ▢") ×3, carried as anaphora. **Departed:** each charge's closing 是以▢ (*shì yǐ ▢* — "therefore ▢"), cut on Shalom's call, 2026-08-25, `notes/translation.md` → *Ch 75*.

#### Ch 76
**Kept:** 人之生也柔弱，其死也堅強 (*rén zhī shēng yě róu ruò, qí sǐ yě jiān qiáng* — "a person alive is soft and yielding, dead is hard and strong") and its pair for the grasses and trees; 死之徒 / 生之徒 (*sǐ zhī tú / shēng zhī tú* — "followers of death / of life"), as at ch 50; 兵強 / 木強 (*bīng qiáng / mù qiáng* — "a strong army / a strong tree"); 處下 / 處上 (*chǔ xià / chǔ shàng* — "dwell below / above").

#### Ch 77
**Kept:** 天之道 / 人之道 (*tiān zhī dào / rén zhī dào* — "the way of nature / the way of people"); 高者抑之，下者舉之 (*gāo zhě yì zhī, xià zhě jǔ zhī* — "the high pressed down, the low lifted"); the chiasmus 損有餘而補不足 / 損不足以奉有餘 (*sǔn yǒu yú ér bǔ bù zú / sǔn bù zú yǐ fèng yǒu yú* — "takes from too much and mends too little / takes from too little to offer to too much"); 為而不恃 (*wéi ér bù shì*) and 功成而不處 (*gōng chéng ér bù chǔ* — "the work done, does not stay"), as at ch 2. **Lost:** 損 (*sǔn* — reduce) and 補 (*bǔ* — mend) open the chapter in the bow image and are restated as its law, and the English changes verbs between them, *drawn off* and *filled in*, then *takes from* and *mends* (T3-18).

#### Ch 78
**Kept:** 莫…莫… (*mò… mò…* — "nothing… nothing…"); 弱之勝強，柔之勝剛 (*ruò zhī shèng qiáng, róu zhī shèng gāng* — "the yielding overcomes the strong, the soft overcomes the hard"); 受國之垢 / 受國之不祥 (*shòu guó zhī gòu / shòu guó zhī bù xiáng* — "takes on the state's shame / the state's ill omen"); 正言若反 (*zhèng yán ruò fǎn* — "straight words seem reversed"). **Lost:** 是謂 (*shì wèi*) dropped twice (T3-11); 是以聖人云 (*shì yǐ shèng rén yún* — "therefore the sage says") (T3-12).

#### Ch 79
**Kept:** 怨 (*yuàn* — grudge) ×2; 有德司契，無德司徹 (*yǒu dé sī qì, wú dé sī chè* — "those with integrity keep the tally, those without keep the levy"); 天道 (*tiān dào* — the way of nature), as at 9, 47, 73, 77 and 81.

#### Ch 80
**Kept:** 使 (*shǐ* — let) ×3, *Let the people…*; 雖有▢，無所▢之 (*suī yǒu ▢, wú suǒ ▢ zhī* — "though there are ▢, there is no call to ▢ them") ×2; 甘其食，美其服，安其居，樂其俗 (*gān qí shí, měi qí fú, ān qí jū, lè qí sú* — "their food sweet, their clothes fine, their homes restful, their ways a joy"). **Lost:** 相 (*xiāng* — each other) stands three times in the closing, *within sight of each other*, *hear each other's*, then 不相往來 (*bù xiāng wǎng lái* — "do not go to and fro with each other") as *never once go next door*, **departed** on purpose, so that the line names the motion and where it goes (`notes/translation.md` → 不相往來 (*bù xiāng wǎng lái* — "do not go to and fro")).

#### Ch 81
**Kept:** all three reversals, §4; 既以為人己愈有，既以與人己愈多 (*jì yǐ wéi rén jǐ yù yǒu, jì yǐ yǔ rén jǐ yù duō* — "having done for others, they have more; having given to others, they have more still"); 天之道 / 聖人之道 (*tiān zhī dào / shèng rén zhī dào* — "the way of nature / the way of the sage"), each closing on ▢而不▢ (*▢ ér bù ▢* — "▢ and does not ▢").
