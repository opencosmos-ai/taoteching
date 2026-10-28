## The Accuracy Audit — what the Chinese says that the English drops, and what the English says that the Chinese does not

*A ledger. It reads every line of the 81 chapters, Chinese against English, for the two most basic accuracy errors: an **omission**, where the Chinese says something the English drops, and an **addition**, where the English says something with nothing in the Chinese behind it. It records every departure it found, says whether anyone chose it, and proposes a line for each one nobody chose. Its companion is `process/form-audit.md`, which reads for the music; this one reads for the content. First run 2026-10-27; its counts are as of that day.*

### Why this exists

**The locks test the words, and the form audit tests the shape. Neither tests whether the content arrived.** A line can carry every locked term correctly and keep its parallel, and still drop the word that made its claim, or add one that changes it. Ch 5's *"Speaking of this is a dead end"* passes every gate in this repository, and the Chinese says something else (finding 1 below).

**The standard frameworks name these errors first.** Translation-quality typologies divide accuracy into *addition*, *omission* and *mistranslation* (the MQM framework: Mariana, Cox and Melby, *The Journal of Specialised Translation* 23, 2015). This audit takes the first two, and adds a third that matters more in a text this compressed: a **shift**, where nothing is dropped or added but the claim's force changes, such as *sometimes* becoming *always*, *can* becoming *does*, or *will* becoming *is*.

**Most departures in this manuscript were chosen, and that is the good news.** The read flagged about 140 places. Most of them are logged, deliberate calls, with reasons in a chapter's notes, `notes/translation.md`, `notes/manuscript.md`, the glossary or the form audit, and they are listed at the end so nobody re-flags them. **What this audit exists to find is the other kind: the departure nobody chose.** It found seventeen, and one logged call that a newer rule now overrules.

### The verdicts

| Verdict | Means |
|---|---|
| **Kept** | Everything the Chinese says is in the English, and nothing more. Not listed: a line absent from this ledger was read and kept |
| **Departed** | The English drops, adds or shifts, and the reason is logged where the line's decisions live. Listed at the end, with the pointer |
| **Lost** | The English drops, adds or shifts, and nothing records a choice. Each gets a proposed line. **No verse is changed by this audit**: a rewrite goes to Shalom first (`CLAUDE.md` → *Fix on discovery*) |

### How it was read

1. **Every line, Chinese beside English**, from `data/lines.csv`, which pairs each source line with the English aligned to it. All 857 English lines are aligned to some Chinese line, so no English line escaped the read.
2. **Each flag checked against the record** before it was called *Lost*: the chapter's own `## Notes`, the three `notes/` files, the glossary entry for any term involved, `process/form-audit.md`, `process/shaloms-call.md` and `WORKLIST.md`. A flag with a logged reason became *Departed*.
3. **Each *Lost* line verified against its own chapter's Chinese**, and against the commentaries where the line turns on a reading (`sources/commentaries/`).
4. **A mechanical seed pass was tried first and set aside.** It matched each character's glosses against the aligned English, and flagged 539 of 798 lines, almost all noise. A character-to-word match cannot tell a choice from a loss. The read is the audit.

**What it does not cover.** Form, which the form audit owns. Witness forks, which `sources/variants.yaml` owns. Whether a locked rendering is right, which the glossary owns: a line that follows its lock is *Kept* here even when the lock is arguable. And mood (statement against command, a real question against a rhetorical one), which the back-translation audit, run the same night, reads.

---

### First: a logged call that a newer rule overrules

**Ch 55 · 朘作 (*zuī zuò* — "the infant boy's member stirs") → *"their whole being quickens with life."***

This is logged (`notes/manuscript.md` → *Ch 55 · 全作 / 朘作* (*quán zuò* / *zuī zuò* — "wholly stirs" / "the member stirs"); `notes/reading.md` → *Where we universalize on our own authority*), so it is not *Lost*. But its reason no longer stands.

- **Our printed Chinese reads 朘 (*zuī* — the infant boy's member).** The source table prints 而朘作 (*ér zuī zuò* — "and his member stirs"), the Mawangdui and Fu Yi reading. The verse renders a different witness, the received Wang Bi text's 全 (*quán* — whole). So the verse does not translate the Chinese printed beside it.
- **The logged reason is universality**: *"keeping the emblem universal, for infants of every gender."* That was written on 2026-08-11.
- **Rule 1's fourth part, set 2026-10-26, refuses exactly that move.** *"The male the text names stays named … no English that erases either sex where the Chinese names it."* It names the flinch: *"the same flinch that turns 母 (mǔ — mother) into the Source."* And 牡 (*mǔ* — the male) stands one clause earlier in this same line, 未知牝牡之合 (*wèi zhī pìn mǔ zhī hé* — "not yet knowing the union of female and male"), which the English already keeps.

**My recommendation: render 朘 (*zuī* — the infant boy's member), as the printed Chinese reads.** *"They do not yet know the union of female and male, / yet the boy's member stirs — this is vital essence at its utmost."* The point of the line survives intact: potency that arises from fullness, before desire has any object. What changes is that the English stops softening the body the text names. **The cost:** the image is no longer available to infants of every gender. That is the cost the 2026-10-26 rule decided to pay at 父 (*fù* — father), and paying it at 父 (*fù* — father) but not here would apply the rule to the father and not to the son.

**The alternative, if you would rather keep the received reading:** follow Wang Bi's 全 (*quán* — whole) on the evidence of the witness, not on the ground of universality, and say so in the note. That is a witness call, which the rule allows. Universality as the reason is what it does not allow.

---

### The lost lines, deepest first

#### Changes what the line claims

**1 · Ch 5 · 多言數窮 (*duō yán shuò qióng* — "much talk soon runs out") → *"Speaking of this is a dead end."***
**Lost:** 多 (*duō* — much) and 數 (*shuò* / *shù* — soon / by reckoning). **Added:** *of this*. The Chinese makes a claim about talking too much. The English makes a different claim, that the subject cannot be spoken of, and the line does not say that. Both commentators read it as a line about much talk. Heshang Gong: 多事害神，多言害身 (*duō shì hài shén, duō yán hài shēn* — "much business harms the spirit, much talk harms the body"). Wang Bi: 必窮之數也 (*bì qióng zhī shù yě* — "it is bound, by reckoning, to run out"). A phonetic note in Heshang Gong's printed text, a later editor's addition, records both readings: Wang Bi's *shù* (reckoning) and the Tang emperor Xuanzong's *shuò* (soon). Nothing in the chapter's notes discusses the line.
**Proposed:** *"Much talk is bound to run out. / Instead, hold to the center."* *Bound to* carries both readings of 數 (*shuò* / *shù* — soon / by reckoning). The second line is unchanged.

**2 · Ch 21 · 孔德之容 (*kǒng dé zhī róng* — "the bearing of great integrity") → *"The greatest integrity follows only the Tao."***
**Lost:** 容 (*róng* — bearing, outward form). The Chinese says the *bearing* of great integrity follows the Tao. The English says integrity itself does. The glossary builds on the word the verse drops. `glossary/de-德.md` reads this line as *"the form of great 德 (*dé* — integrity) follows the Tao alone. De is what the Tao looks like once it takes a body."* Nothing records the omission.
**Proposed:** *"The bearing of the greatest integrity / follows only the Tao."* I'd use *bearing*, not the entry's *form*, because the book spends *form* on 形 (*xíng* — shape), as in 41's 大象無形 (*dà xiàng wú xíng* — "the great image has no form").

**3 · Ch 12 · 五色 · 五音 · 五味 (*wǔ sè · wǔ yīn · wǔ wèi* — "the five colors, the five tones, the five flavors") → *"The full spectrum of colors … of tones … of flavors."***
**Lost:** 五 (*wǔ* — five), three times. **Added:** *spectrum*. The five colors, five tones and five flavors are a named classical system, and the chapter's force is a count: five of each and the senses are glutted. *Spectrum* is Newton's word, so it fails the pointing test (`CLAUDE.md` → *The overlay watchlist*), and it is a cousin of the mechanistic register the watchlist names as our besetting temptation. Its third use, *a spectrum of flavors*, does not hold as an image at all. The chapter's notes restore 人 (*rén* — a person) in these same lines and say nothing about 五 (*wǔ* — five).
**Proposed:** *"The five colors make people's eyes blind. / The five tones make people's ears deaf. / The five flavors make people's palates dull."*

**4 · Ch 42 · 故物或損之而益，或益之而損 (*gù wù huò sǔn zhī ér yì, huò yì zhī ér sǔn* — "so with things: some are decreased and gain, some are increased and lose") → *"For so it is: what is decreased is thereby increased, and what is increased is thereby decreased."***
**Lost:** 或 … 或 (*huò … huò* — some … some). An observation about *some* things becomes a law about *all* of them. The book already has English for this construction: ch 29's 或行或隨 (*huò xíng huò suí* — "some go ahead, some follow") reads *"some go ahead, some follow."*
**Proposed:** *"For so it is with things: some are decreased and so increased, / some increased and so decreased."*

**5 · Ch 30 · 果而勿強 (*guǒ ér wù qiáng* — "succeed, and do not force") → *"They succeed without using excessive force."***
**Added:** *excessive*. That word licenses force short of excess, and the line forbids force. `glossary/qiang-強.md` reads all three 強 (*qiáng* — strong / to force) in this chapter as force and dominance themselves (*"you do not strengthen a country by invading it"*), and quotes Heshang Gong on this very line: 果敢勿以為強兵堅甲以侵凌人也 (*guǒ gǎn wù yǐ wéi qiáng bīng jiān jiǎ yǐ qīn líng rén yě* — "succeed, but do not make strong troops and hard armor to trample people"). The form audit records the series as *Kept*, and it is, as form. The word *excessive* is not logged anywhere.
**Proposed:** *"They succeed without forcing."* That keeps the series *They succeed without boasting … without bragging … without arrogance.*

**6 · Ch 43 · 無有入無間 (*wú yǒu rù wú jiàn* — "what has no presence enters where there is no gap") → *"The formless enters the seamless."***
**Shift, against a lock.** 無 (*wú* — absence) / 有 (*wú* / *yǒu* — absence / presence) is locked, and its entry names *form and formless* as a rendering it declines: *"they name a different distinction — about visibility rather than"* presence (`glossary/wu-you-無有.md`). No waiver or note covers ch 43. `check_locks.py` cannot see it, because *formless* is not on the forbidden list.
**Proposed:** *"What is not there enters the seamless."* This reuses ch 11's locked wording, *in what is not there*.

**7 · Ch 37 · 夫亦將無欲 … 天下將自正 (*fū yì jiāng wú yù … tiān xià jiāng zì zhèng* — "they too will be without desire … the world will right itself") → *"The nameless uncarved wood is without desire. / Relinquishing desire, being still, the world rights itself."***
**Lost:** 將 (*jiāng* — will), twice, and 亦 (*yì* — too). The chapter makes three promises, each with 將 (*jiāng* — will): the countless things *will* transform, *will* be without desire, and the world *will* right itself. The English keeps *will* in the first and drops it from the other two, so a promise turns into a description. The last line also dangles its modifier: it is the world that relinquishes desire.
**Proposed:** *"The nameless uncarved wood — they too will be without desire. / Not desiring, and so still, the world will right itself."* This touches only 將 (*jiāng* — will) and 亦 (*yì* — too). Two other questions are left alone: 正 (*zhèng* — straight), which is deferred (T4), and the chain through 化 (*huà* — transform), which T3-8 already owes. **Let this ride with T3-8**, which opens the same lines.

**8 · Ch 21 · 道之為物 (*dào zhī wéi wù* — "the Tao, as a thing") → *"Whatever the Tao is, it is only vague, only elusive."***
**Lost:** 物 (*wù* — thing), and with it the answer the chapter gives two lines later. That line is 其中有物 (*qí zhōng yǒu wù* — "within it there is a thing"), and the English renders it *"there is a thing."* The Chinese says that the Tao, taken as a thing, is vague, and yet a thing is in it. *Whatever the Tao is* hedges, and the hedge breaks the echo.
**Proposed:** *"The Tao, as a thing, / is only vague, only elusive."*

#### Changes the force

**9 · Ch 77 · 孰能有餘以奉天下 (*shú néng yǒu yú yǐ fèng tiān xià* — "who can have a surplus and offer it to the world?") → *"Who has more than enough, / and offers it up to the world?"***
**Lost:** 能 (*néng* — can). The question asks who is *able*, and the English asks who *does*. The answer, *Only those who are with the Tao*, is about capacity.
**Proposed:** *"Who can have more than enough / and offer it up to the world?"*

**10 · Ch 46 · 禍莫大於不知足 (*huò mò dà yú bù zhī zú* — "no disaster is greater than not knowing enough") → *"There is no greater disaster than discontent."***
**Lost:** 知 (*zhī* — to know). 知足 (*zhī zú* — knowing enough) is a book-wide formula. It reads *knows they have enough* at 33 and *Know when you have enough* at 44, and two lines later in this chapter 知足之足 (*zhī zú zhī zú* — "the enough of knowing enough") reads *"the contentment of knowing you have enough."* *Discontent* names a feeling where the Chinese names a knowing, and it breaks the repetition inside the chapter. The parallel at ch 69 copies this line's frame on purpose (`notes/translation.md` → *Ch 69*), and that frame is unaffected.
**Proposed:** *"There is no greater disaster than not knowing when you have enough,"*

**11 · Ch 41 · 若存若亡 (*ruò cún ruò wáng* — "as if keeping it, as if losing it") → *"keep some, forget some."***
**Lost:** 若 (*ruò* — as if), twice. Wavering becomes keeping part of it. Ch 4's notes already pair 存 (*cún* — to be still there) against 亡 (*wáng* — to be gone) in exactly this line.
**Proposed:** *"Those middling in service hear the Tao / and seem to keep it, seem to lose it."*

**12 · Ch 50 · 善攝生者 (*shàn shè shēng zhě* — "one masterful at tending life") → *"one who truly tends life."***
**Shift, against a lock.** 善 (*shàn*) is locked, and `glossary/shan-善.md` lists ch 50 by name under *善 (*shàn* — masterful) + verb → masterful at*. *Truly* is neither the lock nor a recorded flexion.
**Proposed:** *"It's been said that one masterful at tending life"*

**13 · Ch 27 · 是謂要妙 (*shì wèi yào miào* — "this is called the essential subtlety") → *"This is the essential secret."***
**Shift, against a lock**, and **lost:** 謂 (*wèi* — called). 妙 (*miào* — subtle) is locked to *subtle*. `glossary/xuan-miao-玄妙.md` names this very line *"the essential subtlety"* and refuses *mystery*. *Secret* carries the same esoteric charge by another word.
**Proposed:** *"This is called the essential subtlety."*

**14 · Ch 45 · 躁勝寒 (*zào shèng hán* — "agitation overcomes cold") → *"Movement overcomes cold."***
**Shift.** 躁 (*zào* — agitation, restlessness) reads *agitated* and *agitation* at ch 26, in the same pair: 靜為躁君 (*jìng wéi zào jūn* — "stillness is the ruler of the agitated"). *Movement* turns a fault into a neutral fact and breaks the 靜 / 躁 (*jìng / zào* — still / agitated) pair between the two chapters. Not logged.
**Proposed:** *"Agitation overcomes cold; stillness overcomes heat."* This belongs to the 靜 (*jìng* — stillness) entry, which `glossary/TRIAGE.md` already queues with 躁 (*zào* — agitation) as its opposite.

**15 · Ch 27 · 不貴其師，不愛其資，雖智大迷 (*bù guì qí shī, bù ài qí zī, suī zhì dà mí* — "not to value the teacher, not to love the material: though clever, greatly lost") → *"Not valuing the master and not loving their raw material is a sign of great confusion. / Even those who appear intelligent are lost."***
**Added:** *is a sign of*, *appear*. **Doubled:** 大迷 (*dà mí* — greatly lost) is rendered twice, once as *great confusion* and once as *lost*. The Chinese is one sentence: whoever fails both ways is greatly lost, however clever.
**Proposed:** *"Not to value the master, not to love the raw material — / however clever, this is to be greatly lost."*

**16 · Ch 79 · 而不責於人 (*ér bù zé yú rén* — "and makes no demand on people") → *"and never asks for the other."***
**Lost:** 人 (*rén* — people). The object moves from people to the tally's other half. The chapter's notes leave the left tally's side open on purpose, and say *"the English renders the character"*. It renders 責 (*zé* — to demand payment) but not 人 (*rén* — people), and the claim is about how the sage treats people.
**Proposed:** *"So the sage grasps the left half of the tally / and makes no demand on anyone."*

**17 · Ch 11 · the note and the verse disagree.** The chapter's notes say *"當 (*dāng* — right at) → **right where**, not through,"* and the verse reads *"In what is not there"* three times. One of the two is wrong. The verse is the settled wording of 無 (*wú* — absence)'s lock, which already includes *in*, so I'd **correct the note**: 當 (*dāng* — right at) is carried by *in*, and *right where* was a draft. Also lost, and fine to leave: 其 (*qí* — its), in 當其無 (*dāng qí wú* — "right at its absence").

#### Smaller, gathered

Real, but each is a word, and none changes a claim. They are worth carrying into the next push that opens the chapter, not a pass of their own.

| Ch | Chinese | English | What it adds or drops |
|---|---|---|---|
| 3 | 使民不爭 (*shǐ mín bù zhēng* — "makes the people not contend") | *the people have no cause to contend* | adds *cause* |
| 7 | 故能成其私 (*gù néng chéng qí sī* — "so they can complete their private self") | *And so their private self is fulfilled* | drops 能 (*néng* — can) and the doer |
| 8 | 居善地，心善淵 (*jū shàn dì, xīn shàn yuān* — "dwelling, masterful at ground; heart, masterful at depth") | *masterful at **choosing** ground … at **staying** deep* | adds two verbs |
| 14 | 繩繩 (*shéng shéng* — "cord on cord, unbroken") | *Continuously flowing* | the cord becomes water |
| 16 | 知常容 (*zhī cháng róng* — "knowing the ever-present, capacious") | *you contain **everything*** | adds *everything* |
| 27 | 故善人者，不善人之師 (*gù shàn rén zhě, bù shàn rén zhī shī* — "so the masterful person is the unmasterful person's teacher") | *the masterful one **naturally** teaches the novice* | adds *naturally* |
| 31 | 不得已而用之，恬淡為上 (*bù dé yǐ ér yòng zhī, tián dàn wéi shàng* — "used only when unavoidable, calm detachment is best") | *Used only when unavoidable, calm detachment is best* | English grammar: the modifier dangles onto *detachment* |
| 46 | 天下有道 (*tiān xià yǒu dào* — "the world has the Tao") | *the world **embraces** the Tao* | adds a verb the world does |
| 49 | 聖人皆孩之 (*shèng rén jiē hái zhī* — "the sage treats them all as infants") | *sees them **pure** as infants* | adds *pure* |
| 52 | 天下有始 (*tiān xià yǒu shǐ* — "the world has a beginning") | *The world has an **origin*** | 始 (*shǐ* — beginning) reads *beginning* at ch 1. For the 始 (*shǐ* — beginning) entry, already queued |
| 54 | 子孫以祭祀不輟 (*zǐ sūn yǐ jì sì bù chuò* — "descendants sacrifice without ceasing") | *offering sacrifices **honoring this*** | adds an object |
| 55 | 終日號而不嗄 (*zhōng rì háo ér bù shà* — "cries all day and does not go hoarse") | ***It** cries all day* | the infant is *them / they* for three lines, then *it* |
| 56 · 62 | 故為天下貴 (*gù wéi tiān xià guì* — "so they are prized by the world") | *the **most** honored in the world* | adds *most*, in both chapters alike, so fix both or neither |
| 74 | 夫代司殺者殺 (*fū dài sī shā zhě shā* — "to kill in place of the one in charge of killing") | *To take their place is to take the place of the master carpenter* | drops both acts, 殺 (*shā* — to kill) and 斫 (*zhuó* — to hew); the next line restores *carve* |
| 80 | 使有什伯之器而不用 (*shǐ yǒu shí bǎi zhī qì ér bù yòng* — "let them have tools of tens and hundreds, and not use them") | *yet **no need** to use them* | adds a reason |

#### A tally for T3-12: where 故 (*gù* — so) has no English

Of the source lines that hold 故 (*gù* — so), these have no English for it. The rest carry it as *so*, *therefore*, *thus* or *for*, or absorb it into a construction that already says it: 夫唯 … 故 (*fū wéi … gù* — "only because … therefore") as *Only because … does*, and 何故 (*hé gù* — "for what reason") as *Why?*

| Ch | Line | English |
|---|---|---|
| 1 | 故常無欲 (*gù cháng wú yù* — "so, ever desireless") | *Ever desireless, observe its subtlety* |
| 12 · 38 · 72 | 故去彼取此 (*gù qù bǐ qǔ cǐ* — "so, let go of that and take this") | *They let go of what is out there and take what is here* (a refrain, consistent in all three) |
| 23 | 故飄風不終朝 (*gù piāo fēng bù zhōng zhāo* — "so a squall does not last the morning") | *A squall does not last out the morning* |
| 24 · 31 | 故有道者不處 (*gù yǒu dào zhě bù chǔ* — "so those with the Tao do not dwell there") | *Those who are with the Tao do not dwell among them* (a refrain, consistent in both) |
| 56 | 故不可得而親 (*gù bù kě dé ér qīn* — "so they cannot be drawn near") | *You cannot draw them near* |
| 61 | 故或下以取 (*gù huò xià yǐ qǔ* — "so one goes low to take") | *The large state takes by going low* |
| 62 | 故立天子 (*gù lì tiān zǐ* — "so when they raise up a child of the sky") | *When they raise up a child of the sky* |

**This is evidence for T3-12, not a finding of its own.** T3-12 is waiting on one book-wide decision about the two connectives. Whatever that decision is, these are the lines it has to reach, and two of them are refrains, which should move together.

---

### What was flagged and found already decided

Listed so the next reader does not re-flag them. Each pointer is where the reason lives.

| Ch | The departure | Where it is decided |
|---|---|---|
| 2 · 10 · 51 · 77 | 為而不恃 (*wéi ér bù shì* — "acts, and does not rely on it") → *relies on nothing* | `notes/translation.md` → the 恃 (*shì* — to rely on) sweep |
| 3 · 30 · 64 · 67 · 69 · 73 · 74 | 敢 (*gǎn* — to venture) → *push*, and *dare* forbidden | `glossary/gan-敢.md`, locked |
| 5 | 不仁 (*bù rén* — "not humane") → *not concerned with humaneness* | the chapter's notes |
| 8 | 幾於道 (*jī yú dào* — "near the Tao") → *nearly the Tao* | the chapter's notes |
| 13 | 寵辱若驚 (*chǒng rǔ ruò jīng* — "favor and disgrace alike alarm") → *are both a shock*; 寄 / 託 (*jì / tuō* — to entrust) both → *trusted with* | `process/form-audit.md`; the chapter's notes (T3-7) |
| 17 | the ladder named by grade, and 悠兮 (*yōu xī* — "unhurried!") gone | `process/form-audit.md`, both open there |
| 22 | 抱一 (*bào yī* — "embraces one") → *embraces one thing*; 誠全而歸之 (*chéng quán ér guī zhī* — "truly whole, return to it") → *These words hold. Return to them. Stay whole.* | the chapter's notes |
| 22 · 24 | 彰 (*zhāng* — to shine forth) → *their rightness shows* / *convince no one* | `process/form-audit.md`, departed |
| 25 | 王 (*wáng* — king) → *humans* | `notes/manuscript.md` → *Ch 25*; `notes/reading.md` |
| 28 | 知其榮 (*zhī qí róng* — "know the glory") → *Know the white*; 則為官長 (*zé wéi guān zhǎng* — "becomes chief of the officers") with the sage as subject | the chapter's notes; `notes/manuscript.md` → *Ch 28* |
| 29 | 挫 (*cuò* — to break) → *carried*, following Heshang Gong's 載 (*zài* — to carry) | `notes/manuscript.md` → *Ch 29* |
| 32 | 川谷 (*chuān gǔ* — "streams and valleys") → *small valleys*, following Guodian | the chapter's notes |
| 34 | 而不為主 (*ér bù wéi zhǔ* — "and does not act as master") ×2 in two Englishes; 功成 (*gōng chéng* — "the work done") → *It works* | `process/form-audit.md`, open there |
| 35 | 道之出口 (*dào zhī chū kǒu* — "the Tao, passing the mouth") → *bland in the mouth* | `notes/translation.md` → *Ch 35* |
| 36 | 示人 (*shì rén* — "show to people") → *shown* | the chapter's notes |
| 38 | 失道而後德 (*shī dào ér hòu dé* — "the Tao lost, then integrity") → *then integrity is lost*, following Han Fei | the chapter's notes (T1-25); `notes/manuscript.md` |
| 39 | 輿 (*yú* — cart) for 譽 (*yù* — praise); jade and stone as *neither … nor* | the chapter's notes |
| 41 | 晚成 (*wǎn chéng* — "completed late") → *never completed*, following the excavated witnesses | `notes/manuscript.md` → *Ch 41* |
| 48 | 取天下 (*qǔ tiān xià* — "take the world") → *the world comes to you* | `notes/translation.md` → *取天下 (*qǔ tiān xià* — "take the world")* |
| 52 | 其母 (*qí mǔ* — "its mother") → *our mother*; *outer light*, *inner clarity* | `notes/translation.md` → *其母 (*qí mǔ* — "its mother")*; the chapter's notes |
| 53 | 是謂盜夸 (*shì wèi dào kuā* — "this is called the thieves' boast") → *This exposes the ringleader of thieves* | `notes/translation.md` → *是謂 (*shì wèi* — "this is called") → "This exposes…"*; `notes/manuscript.md` |
| 57 | 自樸 (*zì pǔ* — "plain of themselves") → *become plain* | `glossary/pu-樸.md`, a licensed flexion |
| 64 | 學不學 (*xué bù xué* — "learns the not-learning") → *learns to unlearn* | `notes/translation.md` → *Ch 64* |
| 65 | 明民 (*míng mín* — "make the people clear-sighted") → *make the people clever* | the chapter's notes (T1-17), a declared exception |
| 69 | 主 / 客 (*zhǔ / kè* — host / guest) → *move first / move second*; *into another's ground* | `notes/translation.md` → *Ch 69*, logged open |
| 71 · 75 | the closing 是以 (*shì yǐ* — therefore) repetition cut | the chapters' notes |
| 72 | 大威 (*dà wēi* — "the great dread") → *the great collapse* | `process/form-audit.md`, Shalom's call |
| 74 | 司殺者 (*sī shā zhě* — "the one in charge of killing") → *one who does the killing* | the chapter's notes; `notes/manuscript.md` |
| 75 | 有為 (*yǒu wéi* — "having doing") → *will not stop doing* | the chapter's notes |

### What to do with each

**Ch 55 is a call**, the only one here, and it is Shalom's: render 朘 (*zuī*), or keep 全 (*quán*) on the witness's authority and rewrite the note's reason.

**Findings 1–16 are rewrites**, so each is proposed, not applied. When a chapter is next open, its finding rides along. Findings 1, 2, 3 and 4 change what a line claims and are worth opening a chapter for. Findings 6, 12 and 13 sit against a lock, so `--english` should be run on the proposed line before it lands.

**Finding 17 is a note correction**, and needs no call.

**The smaller table** rides with whatever next opens each chapter.

**The 故 (*gù* — so) tally** waits on T3-12.
