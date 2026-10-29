## The Back-Translation Audit — does a reader of the English come away with what the Chinese says?

*A ledger. Two kinds of reader worked blind. One saw only the English and wrote down what it claims. The other saw only the Chinese and the classical commentaries and did the same. Then the two accounts were compared, chapter by chapter, and every place they part was checked against the page. First run 2026-10-27; its counts are as of that day. The readers' raw reports are in [`back-translation/`](back-translation/README.md).*

### Why this exists

**Every other check in this repository reads the translation with the Chinese in view.** The locks, the form audit, the accuracy audit and every chapter review all compare the English to the source line by line, with the source open. None of them asks the question a reader asks: *reading only this English, what would I believe the book says?* A line can carry every word and still be heard as something else: a description heard as a command, a correction heard as an addition, a sentence nobody can parse.

**Back-translation is the standard test for that.** Clinical and survey translators use it because it catches what a bilingual reviewer cannot: the bilingual reviewer already knows what the line is supposed to mean, and reads that meaning into it. A blind reader cannot. This audit adapts it. Instead of translating the English back into Chinese, it has each side described in the same structured terms, so the two can be compared claim by claim:

| Field | Asks |
|---|---|
| **Says** | the proposition, as literally as possible |
| **Act** | asserts · advises or commands · asks (real or rhetorical) · if-then · names · describes a person |
| **Who acts** | the doer and the done-to, and whether the text says |
| **Force** | always · sometimes · can · must · will · past |
| **Link** | because · therefore · but · and · none |
| **Open** | where the text genuinely reads more than one way |

### How it was run

1. **Reader A, three readers, the English only**, chapters 1–27, 28–54 and 55–81. Each saw a packet of the verse and nothing else, and was told to read as someone meeting the book for the first time, not to draw on other translations, and to report the English's own ambiguities and connotations.
2. **Reader B, six readers, the Chinese only**, in batches of thirteen or fourteen chapters. Each saw the base text with pinyin, and the vendored Wang Bi, Heshang Gong and Han Fei, and nothing from this repository's English. Each followed the gloss rule.
3. **Three comparers** aligned the two accounts by content, and checked every candidate divergence against four things:
   - the chapter's own source table and verse
   - the commentaries, read directly
   - the record: the chapter's notes, the three `notes/` files, the glossary, the form audit, the accuracy audit and the calls

   A divergence that survived the page and was unrecorded is a finding. One that was recorded is listed as *logged*, and is still worth a line when the blind reader demonstrably paid for it.
4. **Every critical and major finding was then re-verified against the vendored commentaries**, and every commentary quoted below was matched to its file.

**Its limits, stated plainly.**
- **All the readers are AI.** Reader B's account of the Chinese is a reading, so it is evidence, not authority, exactly as `CLAUDE.md` says of the commentaries themselves.
- **Reader B read the base text.** Where the English deliberately follows another witness (ch 28, 29, 32, 38, 39, 41, 42), the comparison is void, and every such case was already logged.
- **Reader A was blind to the repository, but not to the world.** It may have recognized the Tao Te Ching, and it was told to set that aside. Once it silently restored a word the English drops (ch 77's *can*), which hid a finding. The accuracy audit had already caught it.

---

### What it found, deepest first

**One critical finding, eight major and twenty-three minor.** Five more are logged calls the cold reader paid for. And the comparison independently confirmed fifteen of the accuracy audit's seventeen findings, plus its ch 55 call: two methods, run blind to each other's results, landing on the same lines.

#### Critical

**1 · Ch 60 · 非 (*fēi* — "it is not that") read as *"not only"*, and the chapter contradicts itself.**

> 以道莅天下，其鬼不神；非其鬼不神，其神不傷人；非其神不傷人，聖人亦不傷人 (*yǐ dào lì tiān xià, qí guǐ bù shén; fēi qí guǐ bù shén, qí shén bù shāng rén; fēi qí shén bù shāng rén, shèng rén yì bù shāng rén* — "oversee the world with the Tao, and its ghosts do not act as spirits; it is not that the ghosts are not numinous, it is that their numinous power does not harm people; it is not that their power does not harm people, it is that the sage, too, does not harm people")

The English: *"Oversee the world with the Tao, and the ghosts lose their potency, / not only do ghosts lose their potency, their potency causes no harm to people, / not only does their potency do no harm, the sage, too, does no harm to people."*

The Chinese corrects itself twice. The English adds instead, and so says the ghosts lose a potency that, one line later, is still there doing no harm. Reader A called it *"logically odd."* Both commentators read the corrections:
- Heshang Gong: 其□非无精神也 (*qí [guǐ] fēi wú jīng shén yě* — "it is not that the [ghosts] are without spirit-essence"). The □ is a graph the transcribers could not encode, and the context makes it 鬼 (*guǐ* — ghost). He moves the cause to the sage: 以聖人在位不傷害人，故□不敢干之也 (*yǐ shèng rén zài wèi bù shāng hài rén, gù [guǐ] bù gǎn gān zhī yě* — "because the sage in office does not harm people, the [ghosts] dare not intrude on them").
- Wang Bi: 神不害自然也 (*shén bù hài zì rán yě* — "the numinous does not harm what is so of itself"). The power stays; it does no harm.

**Logged?** No. The chapter has no notes. The source table's literal column already says *"Not only,"* and the form audit records the chain as *Kept*, which as form it is. Nobody has argued the reading.

**Proposed:** *"Oversee the world with the Tao, and the ghosts do not act as spirits. / It is not that the ghosts have no potency: their potency does no harm to people. / It is not that their potency does no harm: the sage, too, does no harm to people."* The chain stays in position, so the form audit's verdict holds. *Lose their potency* goes, because 不神 (*bù shén* — "are not numinous / do not act as spirits") does not say they lose anything.

#### Major

**2 · Ch 62 · the verse contradicts its own notes, and lands on Matthew 7:7.**

> 不曰：求以得，有罪以免邪？ (*bù yuē: qiú yǐ dé, yǒu zuì yǐ miǎn xié?* — "is it not said: seeking, by it you find; having an offense, by it you are spared?")

The English: *"Did they not say: seek, and you find; / commit a crime, and you are spared?"* There are two moves here, and they compound.

- **有罪 (*yǒu zuì* — "to have an offense against you") became *commit a crime*.** The chapter's source table, `notes/translation.md` → *Ch 62 · 奧* (*ào* — the inner corner) and `notes/reading.md` → *Ch 62* all read *"have a crime against you,"* and the *sanctuary* argument rests on that legal sense. Heshang Gong: 有罪謂遭亂世闇君妄行刑誅，修道則可以解死 (*yǒu zuì wèi zāo luàn shì àn jūn wàng xíng xíng zhū, xiū dào zé kě yǐ jiě sǐ* — "'having an offense' means meeting a chaotic age and a benighted ruler who punishes and executes at random; cultivating the Tao, one can be released from death").
- **以 (*yǐ* — by it) is dropped from both halves.** Wang Bi makes it the hinge: 以求則得求，以免則得免 (*yǐ qiú zé dé qiú, yǐ miǎn zé dé miǎn* — "use it to seek and you get what you seek; use it to escape and you escape"). Without it, *seek, and you find* is an unconditional promise in the Gospel's cadence, and it fails the hymn test.

Together, the two lines rebuild what `notes/translation.md` → *善 / 不善* (*shàn / bù shàn* — masterful / unmasterful) says this chapter was rendered to avoid: *"a doctrine of grace."*

**Logged?** The legal reading is logged, and the verse contradicts it. Dropping 以 (*yǐ* — by it) is not discussed. **Proposed:** *"Did they not say: seek by it, and you find; / have a crime against you, and by it you are spared?"*

**3 · Ch 53 · 唯施是畏 (*wéi shī shì wèi* — "only acting is what I would fear") → *"my only fear would be to stray from it."***

Both commentators read 施 (*shī*) as *acting*, and the line as a fear of action even on the great road:
- Wang Bi: 唯施為之是畏也 (*wéi shī wéi zhī shì wèi yě* — "only taking action is what I fear")
- Heshang Gong: 獨畏有所施爲，失道意 (*dú wèi yǒu suǒ shī wéi, shī dào yì* — "I fear only that some action would lose the Tao's intent")

The English takes the reading of 施 (*shī* — to act) as a loan for 迤 (*yǐ* — to veer). That is a respectable philological reading, and the next line's 徑 (*jìng* — byways) supports it. But it is a choice against every commentary in the repository, and nothing records it. A second choice rides in the same line: 介然 (*jiè rán* — slightly / firmly), which Heshang Gong glosses 介，大也 (*jiè, dà yě* — "*jiè* means great"), and which the English renders as *"just a scrap,"* the opposite pole, without a note.

**Logged?** No. **Proposed:** keep *stray* and log the 迤 (*yǐ* — to veer) reading, with 徑 (*jìng* — byways) as its evidence and both commentators against it. Or follow them: *"my only fear would be to act."* I'd keep *stray*: the byways in the next line make the road image the chapter's own. But the choice has to be written down.

**4 · Ch 30 · 其事好還 (*qí shì hào huán* — "their affairs tend to turn back") → *"Such undertakings tend to come back on you."***

The English takes the recoil reading, that war rebounds on whoever wages it, the usual modern one. Neither commentator reads it so. Both make 其 (*qí* — their) the Tao-guided helper of the line before, and 還 (*huán* — to turn back) that person's own turning back:
- Wang Bi: 為始者務欲立功生事，而有道者務欲還反無為，故云其事好還也 (*wéi shǐ zhě wù yù lì gōng shēng shì, ér yǒu dào zhě wù yù huán fǎn wú wéi, gù yún qí shì hào huán yě* — "those who start things strive to make merit and create affairs, but one with the Tao strives to turn back to non-doing; so it says 'their affairs tend to turn back'")
- Heshang Gong: 其舉事好還自責，不怨於人也 (*qí jǔ shì hào huán zì zé, bù yuàn yú rén yě* — "in what they undertake they tend to turn back and blame themselves, and do not resent others")

*Such undertakings* and *on you* are both supplied, and together they close the line onto one reading. `glossary/shi-事.md` and `notes/reading.md` → *Ch 30's 還* (*huán* — to turn back) assume recoil without mentioning that both commentators read it the other way.

**Logged?** Assumed, not argued. **Proposed:** *"Such affairs tend to turn back."* This keeps the bare figure, which holds the recoil and the commentators' turning-back both, and is the honesty-over-closure move the ethos asks for. Log the split either way.

**5 · Ch 13 · 貴大患若身 (*guì dà huàn ruò shēn* — "great trouble is prized like the body") → *"Prize great trouble as your own body."***

A description became a command. The chapter quotes a saying, *favor and disgrace alike alarm; great trouble is prized like the body*, and then asks what each half means. The English turns the second half into an instruction to the reader. Neither commentator reads an instruction:
- Wang Bi: 人迷之於榮寵，返之於身，故曰大患若身也 (*rén mí zhī yú róng chǒng, fǎn zhī yú shēn, gù yuē dà huàn ruò shēn yě* — "people are deluded by glory and favor, and it rebounds onto the body; so it says 'great trouble as the body'")
- Heshang Gong: 貴，畏也；若，至也。畏大患至身，故皆驚 (*guì, wèi yě; ruò, zhì yě. wèi dà huàn zhì shēn, gù jiē jīng* — "*guì* means to fear, *ruò* means to arrive: fearing great trouble reaching the body, so all are alarmed")

**Logged?** No; the chapter's notes settle 貴 (*guì* — to prize) and say nothing of mood. **Proposed:** *"Great trouble is prized like one's own body."* The *"What does it mean…?"* that follows then asks about a saying, as the Chinese does.

**6 · Ch 13 · the closing couplet settles a divided reading, and the note cites the evidence one-sidedly.**

> 故貴以身為天下，若可寄天下；愛以身為天下，若可託天下 (*gù guì yǐ shēn wéi tiān xià, ruò kě jì tiān xià; ài yǐ shēn wéi tiān xià, ruò kě tuō tiān xià* — "so one who prizes the body as / for the world can be lodged with the world; one who loves the body as / for the world can be entrusted with it")

Heshang Gong reads the two lines as opposites:
- The first is a warning. 言人君貴其身而賤人，欲為天下主者，則可寄立，不可以久也 (*yán rén jūn guì qí shēn ér jiàn rén, yù wéi tiān xià zhǔ zhě, zé kě jì lì, bù kě yǐ jiǔ yě* — "a ruler who prizes his own body and holds others cheap, wanting to be lord of the world, can be set up only as a lodger, not for long").
- The second is praise, *entrusted … long without fault*.
- His contrast turns on 寄 (*jì* — to lodge) against 託 (*tuō* — to entrust).

Wang Bi reads both as praise, and swaps the two verbs. The English renders both lines as one positive claim with one verb, *trusted with*. The note logs that merger on Wang Bi's authority, cites Heshang Gong's second gloss in support, and does not mention his first.

**Logged?** Partly; the chosen reading is a call, but the record leaves out the evidence against it. **Proposed:** at minimum, correct the note to say that Heshang Gong reads the first line as a warning. Then decide whether the verse keeps 寄 (*jì* — to lodge) and 託 (*tuō* — to entrust) apart, which leaves his contrast available.

**7 · Ch 22 · 枉則直 (*wǎng zé zhí* — "bent, then straight") → *"Be wronged, and be made straight."***

The doer changed. *Wronged* gives 枉 (*wǎng* — bent, crooked) the legal sense of injustice done to you by others, and the passive *be made straight* supplies another outside agent. Both commentators put the bending on the self, and the straightness comes of itself:
- Heshang Gong: 枉屈己而申人，久久自得直也 (*wǎng qū jǐ ér shēn rén, jiǔ jiǔ zì dé zhí yě* — "bending oneself and letting others stretch out, in time one becomes straight of oneself")
- Wang Bi: 不自是則其是彰也 (*bù zì shì zé qí shì zhāng yě* — "not affirming oneself right, one's rightness shows")

The chapter's own notes map this line to 不自是，故彰 (*bù zì shì, gù zhāng* — "they do not insist they are right, and so their rightness shows"), and the English then breaks that mapping.

**Logged?** No. **Proposed:** *"Be bent, and grow straight."* This restores the physical image the series runs on (bend, hollow, worn) and the 不自是 (*bù zì shì* — "not insisting they are right") echo.

**8 · Ch 57 · the opening three become three commands joined by *and*, so the English endorses all three.**

> 以正治國，以奇用兵，以無事取天下 (*yǐ zhèng zhì guó, yǐ qí yòng bīng, yǐ wú shì qǔ tiān xià* — "by the straight a state is governed; by the crooked troops are used; by not meddling the world is won")

The English: *"Govern the state with uprightness, / wage war with surprise, / and win the world by not meddling."* Wang Bi reads the first two as what fails: 以正治國則不足以取天下而以竒用兵也 (*yǐ zhèng zhì guó zé bù zú yǐ qǔ tiān xià ér yǐ qí yòng bīng yě* — "governing by the straight is not enough to win the world, and so one ends up using troops by the crooked"). Heshang Gong reads all three as descriptions, and glosses 奇 (*qí* — crooked) as deceit. `notes/translation.md` → *Ch 57–58* reads ch 58 as *"deliberately unmaking 57"*. An English that commands the first two leaves 58 nothing to unmake.

**This touches only the mood and the added *and*, never the words for 正 / 奇 (*zhèng / qí* — straight / crooked), which Shalom has deferred.** So it does not belong in a chapter review. **It rides with T4-2** as evidence when that opens.

**9 · Ch 58 · 其民缺缺 (*qí mín quē quē* — "its people are lacking, broken") → *"the people turn cunning."***

The English makes the people the culprits; the Chinese makes them the casualties. Neither commentator reads craft into the word:
- Wang Bi: 民懐争競，故曰其民缺缺 (*mín huái zhēng jìng, gù yuē qí mín quē quē* — "the people harbor contention, so it says the people are lacking"), which means fractured
- Heshang Gong: 民不聊生 (*mín bù liáo shēng* — "the people cannot make a living"), which means impoverished

**Logged?** Not as a choice. **The form audit already proposes** *"the people are wanting"* (T2-67, for the doubled characters). This comparison confirms the content cost from both commentators, so that proposal is worth taking for two reasons, not one.

#### Minor

Each is real and none changes a chapter. Each is worth carrying into the next push that opens its chapter. **Logged** means the choice is recorded and the cold reader's response is evidence about its cost.

| Ch | The line | What a reader of the English gets | What the Chinese says, and the evidence |
|---|---|---|---|
| 1 | 常無欲，以觀其妙 (*cháng wú yù, yǐ guān qí miào* — "ever desireless, thereby observe its subtlety") → *"Ever desireless, observe its subtlety"* | a command | a capacity: both commentators write 可以觀 (*kě yǐ guān* — "can observe") |
| 1 | 徼 (*jiào*) → *"boundaries"* | an edge in space | Wang Bi: 徼，歸終也 (*jiào, guī zhōng yě* — "*jiào* is where things end"), set against 妙 (*miào* — subtle) as end against beginning. Choose and record |
| 2 | 音聲相和 (*yīn shēng xiāng hé* — "tone and voice harmonize") → *"Sound and tone"* | two synonyms in a series of opposites | Heshang Gong: 上唱下必和 (*shàng chàng xià bì hé* — "the one above sings, the one below answers"). Wants a pair English hears as two |
| 3 | *"By not exalting the exceptional, the people …"* ×3 | English grammar makes the people the ones who refrain | the ruler refrains, and the people are acted on. A dangling modifier |
| 14 | 不可致詰 (*bù kě zhì jié* — "cannot be questioned to the end") → *"defy comprehension"* | they cannot be understood at all | questioning cannot get to the bottom of them, which is why the *Therefore* follows |
| 17 | 太上 (*tài shàng* — "the very highest") → *"the greatest leaders"* | a grade only | Heshang Gong: 太古无名之君 (*tài gǔ wú míng zhī jūn* — "the nameless rulers of high antiquity"), a history of decline. The positional ladder T3-18 proposes keeps both |
| 19 | 見素 (*xiàn sù* — "show the undyed silk") → *"see"* | looking at plainness | Heshang Gong marks the sound *xiàn* (show). Ch 3 already reads the graph *display*. Record the fork |
| 21 | 孔 (*kǒng*) → *"greatest"* | | Wang Bi, our base: 孔，空也 (*kǒng, kōng yě* — "*kǒng* means empty"). Heshang Gong: *great*. Record it when accuracy-audit finding 2 lands, since 容 (*róng* — bearing / containing) is also forked |
| 23 | 德者同於德 (*dé zhě tóng yú dé* — "one of integrity is the same as integrity") | the reader cannot tell what *"one of loss"* means | Wang Bi reads 德 (*dé* — integrity) as 得 (*dé* — gain), giving gain against loss. The verse can stay on the lock; a note should record his reading |
| 28 | 復歸於嬰兒 (*fù guī yú yīng ér* — "and returns again to the infant") ×3 → *"Return again to the infant."* | a fourth command | the outcome of the stanza's conduct (Wang Bi). *"…and you return again to the infant"* |
| 29 | 吾見其不得已 (*wú jiàn qí bù dé yǐ* — "I see they will not get it") → *"will not succeed"* | | sound, but the same 不得已 (*bù dé yǐ* — "it cannot be helped") is *unavoidable* at 30 and 31. One line in the notes |
| 30 | 果而不得已 (*guǒ ér bù dé yǐ* — "succeed only as what could not be avoided") → *"They succeed because their actions are unavoidable"* | unavoidability causes success | it restricts: they succeed only where force cannot be avoided. *"They succeed only where it cannot be avoided"* |
| 30 | 果而勿矜 (*guǒ ér wù jīn* — "succeed, and do not preen") … ×4 → *"They succeed without boasting"* … | a description | 勿 (*wù* — do not!) is a prohibition. Heshang Gong reads it so, and Wang Bi descriptively. Record the choice. Accuracy-audit finding 5's proposal carries the description forward |
| 32 | 夫亦將知止 (*fū yì jiāng zhī zhǐ* — "one too will know to stop") → *"one must know when to stop"* | an obligation | a promise: the same 夫亦將 (*fū yì jiāng* — "they too will") frame as ch 37, where accuracy-audit finding 7 restores *will*. Move them together |
| 34 · 63 | 故能成其大 (*gù néng chéng qí dà* — "so can complete its greatness") → *"and so completes"* | a result | 能 (*néng* — can), a capacity, as at ch 7 and 77 in the accuracy audit. One formula, so fix all together |
| 37 | 化而欲作 (*huà ér yù zuò* — "as they transform, desire stirs") → *"When the countless things urge action"* | the things pressing the ruler | desire stirring inside things as they change (Wang Bi: 作，欲成也 (*zuò, yù chéng yě* — "*zuò* is desire coming to fruition")). Ride with T3-8 |
| 42 | 人之所教，我亦教之 (*rén zhī suǒ jiào, wǒ yì jiào zhī* — "what others teach, I also teach") with a colon after | the strong-die line is what *others* teach | Heshang Gong: I teach the opposite. `glossary/qiang-強.md` quotes him under this English without noticing. A full stop for the colon |
| 48 | *"The world always comes to you by not meddling with it"* | the world does not meddle | the rendering is logged; the dangling modifier is not. *"When you do not meddle, the world always comes to you"* |
| 50 | 入軍不被甲兵 (*rù jūn bù pèi jiǎ bīng* — "enters an army and is not reached by / does not wear armor") → *"can enter into battle untouched"* | invulnerability, and *can* | Han Fei quotes 不備甲兵 (*bù bèi jiǎ bīng* — "without armor or weapons"): unarmed, not invulnerable. Record the fork; *can* is added twice |
| 54 | 善建者不拔 (*shàn jiàn zhě bù bá* — "one masterful at planting is not uprooted") → *"What is masterfully planted"* | a thing | Heshang Gong and Han Fei read a person, and `glossary/shan-善.md` lists ch 54 under *masterful at*. The adverb departs from the lock |
| 61 | 夫兩者各得所欲 (*fū liǎng zhě gè dé suǒ yù* — "for the two each to get what they want") → *"Both get what they want."* | a fact, then an unconnected *ought* | Wang Bi: 各得其所欲則大者宜為下 (*gè dé qí suǒ yù zé dà zhě yí wéi xià* — "if each is to get what it wants, then the large one ought to be underneath"). *"For both to get what they want"* |
| 65 | 將以愚之 (*jiāng yǐ yú zhī* — "meant to make them guileless") → *"to return them to being guileless"* | a fall and a restoration | no *return* in the text or either commentator. *"to make them guileless"* |
| 73 | 疏而不失 (*shū ér bù shī* — "wide-meshed, yet loses nothing") → *"Its mesh is wide, and nothing slips through"* | an addition | a concession, the chapter's own *yet* four times above it. *"…yet nothing slips through"* |

#### Logged calls the cold reader paid for

Not faults. Each is a recorded choice, and the blind reader's response is evidence about its cost, to weigh if the choice is ever reopened.

| Ch | The line | What Reader A made of it |
|---|---|---|
| 17 · 23 | 有不信 (*yǒu bù xìn* — "there is untrust") → *"there is no trust"* | a tautology, twice. 有 (*yǒu* — there is) asserts that distrust appears, as both commentators say. *"there is distrust"* keeps the logged reading and loses the tautology |
| 29 | 天下神器 (*tiān xià shén qì* — "the world is a numinous vessel") → *"sacred vessel"* | *holy*, *religious*: the register the overlay watchlist exists to catch. Evidence for T2-37 |
| 39 | 其致之 (*qí zhì zhī* — "they brought it about by it") → *"Follow it through:"* | an instruction to the reader. The note says the English *"holds both readings"*, and the reader heard neither |
| 52 · 27 | 是謂襲常 (*shì wèi xí cháng* — "this is called cloaking the ever-present") → *"the ever-present worn covered"* | could not parse it. *Worn* reads as *worn out*. The choice of 襲 (*xí* — a robe worn over another) is argued; the English phrase has no syntax a reader can follow. Ch 27's twin, *"clarity worn covered,"* was likewise *"opaque"* |
| 75 | 無以生為 (*wú yǐ shēng wéi* — "make no doing of living") → *"don't use living for doing"* | opaque |

**One logged call the reader supported.** At ch 55, 心使氣曰強 (*xīn shǐ qì yuē qiáng* — "the heart driving the breath is called forcing") reads *"that is called strong,"* under the 強 (*qiáng* — strong) lock, which asks whether the misheard approval *"is a flaw or the point."* Reader A heard the beat and resolved it from context. That is evidence for the lock.

#### What it confirmed in the accuracy audit

The comparers had `process/accuracy-audit.md` in hand and were told not to re-report it. They were asked to note where their comparison independently hit the same line. It hit **fifteen of its seventeen findings**, and the ch 55 call:
- Findings 1–8 and 10–16 surfaced as a gap between what Reader A heard and what Reader B read.
- Finding 9 (ch 77's *can*) was hidden by Reader A restoring the word.
- Finding 17 is a note correction, which a reader of the verse cannot see.

**That is the strongest result of the night.** Two methods with nothing in common, one reading Chinese against English and the other comparing blind accounts, landed on the same lines. Where both fire, the finding is not one reader's taste.

#### Two stray things a reader found

- **Ch 53's verse prints *"It is not the Tao\!"*** with a Markdown escape, the only `\!` in any verse. It renders correctly on GitHub, but the escape reaches `data/` raw. A one-character fix, outside this audit.
- **Readers' notes are in the comparers' reports**, under *Readers' errors*. None of them voided a finding listed here.

---

### What to do with each

**Ch 60 first.** It is the only finding where the English says something the Chinese contradicts, and the fix keeps the form. One chapter, no lock touched.

**Ch 62 next**, because the verse disagrees with its own notes. Bringing it back is a correction, not a new call. Register the withdrawn wording in `process/retractions.yaml` when it lands.

**Ch 53 and 30 are records owed before they are rewrites.** Each takes a reading against both commentators, and each may be right. Write down the choice and its evidence, then decide whether the line moves.

**Ch 13 and 22 are rewrites with the evidence above.** Ch 13's note needs correcting whatever the verse does.

**Ch 57 waits for T4-2, and ch 58 for T2-67.** Neither is settled here.

**The minor table and the logged table ride with whatever next opens each chapter.** Three of the minor rows are better done as sets:
- ch 32 with ch 37 (夫亦將 (*fū yì jiāng* — "they too will"))
- ch 34 and 63 with ch 7 and 77 (能 (*néng* — can))
- ch 52 with ch 27 (襲 (*xí* — worn covered))
