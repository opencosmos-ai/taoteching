# Translation Notes

*One of three notes layers. This one logs **our own rendering decisions** — the places where we deliberately depart from the most literal English for reasons of meaning, ethos, or clarity, and want the reasoning on record so a future reader (or a future us) can see it was a choice, not an accident.*

---

## Using this file

**What goes here — and what does not.**

| Layer | Holds |
|---|---|
| `notes/manuscript.md` | textual forks **between witnesses** |
| **`notes/translation.md`** ← this file | **our own rendering decisions and standing principles** |
| `notes/reading.md` | reader-facing interpretation; cross-cutting **Threads** |

Log only **deliberate departures** from the literal, never routine word-choices. Entry format: *chapter · the phrase · the choice · why* — and where a rendering was retired, say what it was and when.

**How it is ordered.**

| Level | What it is |
|---|---|
| `##` | one of the four sections below, in this fixed order |
| `###` | a chapter (`Ch 62`), or — in sections 1–3 — a single principle, lock, or thread |
| `####` | one decision, titled `character → "rendering"` |

1. **Standing principles** — ⚠ **emptied 2026-09-10.** Every one moved to [`process/principles/`](../process/principles/README.md), one file each, with a **trigger** saying when it fires and loading by the skills at the moment it applies. The headings remain as redirects so existing links resolve. **Add new principles there, never here.**
2. **Locks — the rationale** — ⚠ **dissolved 2026-09-10, and its self-description was wrong.** It read *"the lock itself lives in `CLAUDE.md` and the glossary; the argument lives here"* — but **the full argument belongs in the glossary entry**, which is what `WORKLIST.md` has said all along and what every entry actually does. The section had exactly **one** occupant in its whole life, 無為, and that occupant was a summary closing with *"Full reasoning: `glossary/wuwei-無為.md`."* It described a layer that was never used. Lock rationale goes in `glossary/<term>.md`.
3. **Cross-chapter decisions** — threads and sweeps belonging to no single chapter.
4. **Chapter notes** — **ascending by chapter number**. Within a chapter, entries follow the order the lines appear in the verse.

**What this file holds now: our own rendering decisions, per chapter and across chapters.** Rules that govern every chapter are in `process/principles/`; rulings on a term are in `glossary/`; forks between witnesses are in `notes/manuscript.md`.

**Four rules that keep it that way.**

1. **Every decision gets an `####` heading**, even when a chapter has only one. Uniform outline, and every decision gets an anchor that can be linked to from a chapter file or from `CLAUDE.md`.
2. **The heading carries only the stable claim** — `#### 奧 → "the sanctuary"`. Supersessions, dates, and *(was: …)* go on the line beneath it. A heading that records history rots every link pointing at it.
3. **New chapters are inserted in number order, never appended.** Chronology is git's job, and git does it better.
4. **No `---` between entries.** Headings do that work. Rules separate the four `##` sections only.

**Before adding an entry, check whether the chapter already has one.** Appending blind has produced a real duplicate here once already (三公, merged 2026-08-11).

**No machine reads this file.** `check_locks.py` parses only `notes/manuscript.md`, and only by substring-matching `Ch N `. So this file can be reorganized freely; `manuscript.md` cannot lose that literal string per chapter without blinding the `unlogged-variant` rule.

---

## Standing principles

*⚠ **Migrating to [`process/principles/`](../process/principles/README.md).** A principle here is indexed by nothing — it governs chapters nobody has read yet, so it needs its own file, a **trigger** saying when it fires, and loading by the skills at the moment it applies. Add new ones there, not here. What remains below is awaiting harvest.*

### Lineation and punctuation — "the marks are yours; the music isn't"

**Migrated to [`process/principles/lineation-is-ours.md`](../process/principles/lineation-is-ours.md), 2026-09-10.** The heading stays so existing links resolve; the argument lives in the entry, with its trigger and its cases, and is loaded by the skills at the moment it applies.

The marks are ours; the music is the source's. The ancient text carries no punctuation and no line breaks, so lineation is ours to use freely — but the source moves in regular character-beats and parallel series, and the layout must track that pulse rather than cut across it. **Also load-bearing for the CC0 dedication:** because the lineation is demonstrably our own, no editorial claim travels with it.

### Typography — lowercase, and no em-dashes in the verse

**The rule itself is `CLAUDE.md` standing rule 5**, and `check_locks.py` enforces it — `_DEVOTIONAL` carries `"Mother": "母"`, so a capital in the verse has always been a hard error. It is restated for outside contributors in [`CONTRIBUTING.md`](../CONTRIBUTING.md). This section held a third full copy.

**The 母 decision moved to [`glossary/mu-母.md`](../glossary/mu-母.md), 2026-09-10**, under *"On the capital, which she does not take."* 母 (*mǔ* — mother) is the strongest candidate in the book for a second capital and she stays lowercase, on five grounds — ch 25 withholding the name the capital would confer, the grammar never naming her, both commentators calling it a comparison, the Jungian Great Mother as the modern overlay, and the capital promoting her out of the body into a pantheon, **which is how she was lost the first time**.

**Why the em-dash is barred, kept here because it is the case rather than the rule.** Ch 2's *"the sage does not begin them — giving birth without possessing…"* left a reader unable to tell whether the sage or the countless things were doing the giving. A dash lets a clause trail into a participle whose actor is unnamed; classical Chinese omits subjects freely and English cannot, so **the dash disguises the omission instead of resolving it.** The general rule is [`name-the-referent`](../process/principles/name-the-referent.md). *(The machine-prose tell is the lesser of the two arguments.)*

**Sweep, 2026-08-11:** 45 instances lowercased across eight files. `chapters/` was already clean — the drift was entirely in the prose *about* the verse.

### The commentaries are evidence, never candidate renderings

**Migrated to [`process/principles/commentary-is-not-a-rendering.md`](../process/principles/commentary-is-not-a-rendering.md), 2026-09-10.** The heading stays so existing links resolve; the argument lives in the entry, with its trigger and its cases, and is loaded by the skills at the moment it applies.

A commentator's gloss is an argument for a rendering, never a rendering. The failure is quiet because the imported word is always *true* and always reads well — a gloss is by construction more explicit than the text it glosses, and the tell is that **the gloss explains and the line stops pointing**. *(The divergence half of the old section is now [`divergence-stays-open`](../process/principles/divergence-stays-open.md).)*

### Register — no modern spiritual idiom

**Migrated to [`process/principles/imported-register.md`](../process/principles/imported-register.md), 2026-09-10.** The heading stays so existing links resolve. The entry absorbs this section, the hymn and pointing tests, and [`process/overlay-audit.md`](../process/overlay-audit.md)'s watchlist into one rule.

Register asserts what vocabulary does not: a rendering can translate every character correctly and still tell the reader **what kind of book this is**. Three registers are foreclosed — **devotional** (the missionary inheritance), **modern spiritual idiom** (*Be Here Now*, 1971), and **mechanistic** (*operating system*, *source code*), which is this edition's own besetting temptation. Three tests: the hymn test, the pointing test, and *could this have been printed in 1968?*

### Collocation carries a verdict — the third way a rendering asserts what the Chinese does not

**Migrated to [`process/principles/collocation-carries-a-verdict.md`](../process/principles/collocation-carries-a-verdict.md), 2026-09-10.** The heading stays so existing links resolve; the argument lives in the entry, with its trigger and its cases, and is loaded by the skills at the moment it applies.

A collocation carries a verdict its component words do not. A line in which every word is a defensible gloss can still assert what the Chinese never says, because the *combination* is a fixed idiom with a meaning of its own — invisible to any word-based check, by definition.

### The 天 family — "no heaven, and no cosmos either"

**Moved to [`glossary/tian-天.md`](../glossary/tian-天.md) and [`glossary/tiandi-天地.md`](../glossary/tiandi-天地.md), 2026-09-10.** The heading stays so existing links resolve.

**This was a ruling on one character, filed among rules that govern every chapter.** It was also a *summary* of the glossary entry — which carries the 天 (*tiān* — sky / nature) split in full, *why not "heaven"*, *why not "the Cosmos"*, the 天之道 formula, the strain cases at 10 and 62, and the contested 配天 at 68 — and it closed by saying so: *"Full argument and evidence: Glossary — 天地."* A second copy of a ruling is how the hand-kept lock table in `CLAUDE.md` went stale twice in one week.

## Locks — the rationale

### 無為 → "non-doing"

**Moved to [`glossary/wuwei-無為.md`](../glossary/wuwei-無為.md), 2026-09-10.** The heading stays so existing links resolve.

The entry carries all of it — the chime (無為而無不為 repeats 為, so the English must repeat *doing*), the register (為 is a hand on a hide: *doing* is bodily where *action* is Latinate), the grammar (the structure needs a verb that also works as a noun), and the outright rejection of ***effortless action***, an interpretation smuggled into a rendering. This section closed by pointing there: *"Full reasoning: `glossary/wuwei-無為.md`."*

## Cross-chapter decisions

### Ch 10 · five Englishes attached to characters that are not in the chapter

*(2026-09-01, Pass D. `WORKLIST.md` T1-1, closing T2-22 and the ch 28 riders. The chapter's own Notes carry the line-by-line.)*

**全 (*quán* — whole), 萬物 (*wàn wù* — the countless things) and 鑑 (*jiàn* — a mirror) each have zero occurrences in ch 10, and each had an English here** — *"can you remain whole?"*, *"the countless things"*, *"the dark mirror."* **And the book's two great negations had swapped lines:** 能**無知**乎 read *"can you lead without doing?"*, 能**無為**乎 read *"can you be unknowing?"*, four lines apart. **Every one is invisible to `check_locks`**, whose evidence gate keys off the character being present. This is the class `--english` exists for, and this chapter is its worst case. **疵 was deleted rather than mistranslated** — 能無疵乎, *"can you be without blemish?"* (說文 病也, under the sickness radical), read *"can you see what truly is?"* **國 was dropped** from 愛民治國.

***"The dark mirror" survived a challenge, and my objection to it was wrong.*** I argued it rendered 鑑/監, which we do not print — the ch 52 襲/習 fault. **說文 defeats that: 覽，觀也。从見、監，監亦聲** — **監 is a constituent of the character we do print**, and 監 is a person over a water basin at their own reflection, the ancestor of 鑑. **The mirror is the graph's own base.** The replacement draft, *"the dark seeing,"* then failed on the verb: **滌除 needs a washable surface**, 河上公 names it (當洗其心使潔淨也, *"wash the heart clean"*), and **疵 is a spot, which sits on a surface** — 王弼: 能不以物**介**其明，**疵之**其神乎. **Recorded cost:** both commentators gloss 覽 with activity verbs, so the mirror reads the **graph**, not the lemma. *(Caught by Shalom.)*

**載營魄 → "housing your soul," settled by a character that is not in this book.** **魂 (*hún* — the cloud-soul) occurs zero times in all 81 chapters**; 魄 and 營 occur once each, both in this line. So 河上公's 營魄，**魂魄**也…魂在肝，魄在肺 is a **Han two-soul system imported onto a text that never uses the other half of the pair** — which is why a draft *"the body's soul"* read as jargon. **王弼 needs nothing imported**: 載猶處也。營魄，人之**常居處**也 — *"營魄 is a person's constant dwelling place"* — and a person's constant dwelling place is the body. The graphs agree: 營 **市居也。从宮**, a walled residence; 魄 **陰神也。从鬼**, the yin spirit billeted in the flesh, not the one that leaves; 載 **乘也。从車**, to ride, with a cart in it. **營魄 is one thing, not two souls: the quarters your animating part is camped in.**

**The general finding — do the watchlist's work with a verb, not a label.** CLAUDE.md flags 精/魄 → *soul*, and the corrective for 魄 is that it is the **corporeal** one. *"The body's soul"* stated that with a possessive and became jargon; ***housing*** performs it, and renders 營's own graph while doing so. ***These*** then carries 能無離乎 onto the two things just named, which is how both commentators read the parting — 王弼 抱一清神，**能常無離乎**; 河上公 抱一使**不離於身**. *(Shalom's line; **housing** replaces his **embodying**, because *embody* wore 為 at ch 28 until this pass removed it and still wears 執 at ch 35, `WORKLIST` T1-12.)* **Four Englishes were blocked, and it is worth recording which:** *spirit* is 神's (6, 39, 60); *flesh* is Pauline — the flesh against the spirit, Romans 8 — which is the hymn test; *quarters* is taken four lines below by this chapter's own 四達; and ***body* is 身's** (13, 54, 76) — 身 does not occur here, so nothing clashed inside the chapter, but the noun was **avoided rather than borrowed**. Cross-referenced on T2-1.

**專 → "gathering," on the graph against a commentator.** 說文 makes 專 a **spindle whorl** (紡專); 河上公 agrees (專守精氣使不亂); **王弼 says the opposite** — 專，任也, *"to entrust oneself to."* The character decides, per the tie-breaking order, and the divergence is logged rather than averaged. **氣 → "breath"** on 河上公's bodily reading (呼吸精氣); T2-4 still owes the book-wide call.

**Two forks recorded, and both sit on the swapped lines.** 河上公 reads 能**無**雌乎 where we read 能**為**雌乎 — the opposite instruction — and **our own Siku 王弼 prints 無 with the note 〔案注義無似作為〕**, so our text follows the Siku editors' correction of the text they print. And **河上公's chapter asks 能無知乎 twice and never asks 能無為乎 at all.** A reader who found the old English would have had no way to tell an error from a witness. See `notes/manuscript.md`.

**Riders closed and opened.** 雌 → **the hen**, the rider ch 28 left, with 王弼 tying her to this chapter's own last question: 雌應而不倡，**因而不為**. 嬰兒 → **an infant** at ch 10, 20 and 28, leaving 赤子 → *a newborn* at ch 55 — **T2-22 closed.** 生之畜之 → **things**, not the locked 萬物, which both commentators supply because the Chinese has no antecedent either. And **長 → "growing" repairs ch 51 as well**, where 長 was reading *grows* and *leading* four lines apart in one stanza.

### Ch 28 · the pointing test, failed on nearly every line

*(2026-09-01, Pass D. `WORKLIST.md` T1-7 · T1-15 · T1-16 · T3-5, and the last of T2-15. The chapter's own Notes carry the line-by-line.)*

**說文解字 makes almost every term in this chapter a physical object, and our English had made almost every one a concept** — *assertive energy · yielding energy · **reservoir** · the limitless · **master orchestrator** · **the great orchestrator*** — all in one register, the mechanistic with the modern spiritual idiom beside it. ***Energy* renders no character**: 氣 is not in the chapter.

**雄/雌 → rooster and hen, and the forcing argument is distributional, not etymological.** 說文 defines the book's **two** male/female pairs in exactly parallel words in different animal classes — 雄 **鳥父**也 / 雌 **鳥母**也 (from 隹, a bird) against 牡 **畜父**也 / 牝 **畜母**也 (from 牛, cattle) — and **牝/牡 already hold *the male* and *the female*** in our English at ch 6, 55 and 61. So 雌/雄 must have their own words and the graph says which. *Cock* and *hen* are the exact English pair (a *cock pheasant*, a *hen harrier*) and *cock* is unusable; **the cost is that *rooster* is narrower than 雄, which is any male bird.** Both commentators read the pair as **position** — 王弼 雄先之屬，雌後之屬也; 河上公 雄以喻尊，雌以喻卑 — which is a reading for the note, not a rendering.

**谷 → valley; *reservoir* was backwards.** 谷 is 泉出**通川**為谷 (*"a spring that runs through to a river"*) against 谿's 山瀆**無所通**者 (*"a watercourse with no outlet"*): **the two are distinguished on whether the water gets out**, and a reservoir holds it in. 谷 is already *valley* in six other chapters.

**為天下X → "serve as the world's X"** — 為's own locked English — **closing T2-15's last pair**, with ch 22's *"sets a pattern for the world"* now reading *"serves as the world's pattern."* **守 → "hold to,"** matching ch 32 and 37 and not pre-empting T2-19; 說文 守官也，从宀从寸, *"to hold an office"* — a charge you are answerable for, where *attune to* inverted the grammar as well as the register. **白/黑 → white and black**, because 光 already holds *light* and 明 holds *clarity*. **無極 → the endless**, because *limitless* is wearing 淵 at ch 8 and both commentators gloss by **exhaustion** (不可窮也 / 無窮極).

**The template is the chapter.** Three stanzas of 知其X，守其Y / 為天下Z / 為天下Z，常德不W / 復歸於V. Ours gave 守 four Englishes, 復歸於 three shapes, invented *we must*, and **dropped 常 — a locked term — from all three 常德**. That is T3-5, and it is the second chapter this pass to lose 常 (ch 3 was the first).

**則為官長 — the grammar decides where the commentators split.** 河上公 has the sage **become** chief (聖人升用則為百官之元長也); 王弼 has the sage **establish** officers (為之立官長, reading 為 as *wèi*). **樸散則為器 is the identical 則為 one line above**, so if that is *becomes vessels*, this is *becomes chief*. This is ch 4's lesson run forward: check the grammar before concluding.

**大制不割 → "the great carving severs nothing" — a paradox the old English had erased.** 制 carries the same word at ch 32 and 說文 makes it a knife on timber (裁也。从刀从未); 割 is a **different** cut (剥也, *to flay*), so it takes *sever*. *"The great orchestrator itself does not carve"* had put **one mechanistic word on two different characters** — 官長 and 大制 — and lost the knife inside both. 王弼: 大制者，以天下之心為心，故無割也.

**Two em-dashes went with the rewrite, not as a decision. T4-3 stays deferred**; ch 28 simply leaves its list.

### Ch 38 · the 道 → 德 → 仁 → 義 → 禮 descent rebuilt, and the rank-word seam named

*(2026-08-31, Pass D. `WORKLIST.md` T1-4. The chapter's own Notes carry the line-by-line.)*

**失 (*shī* — to lose) is the chapter's spine and had been deleted from its hinge.** Five occurrences, more than in any chapter in the book — 下德不**失**德, then 失道 · 失德 · 失仁 · 失義 — and line 2 read *"clutches at integrity,"* with 失 gone. **The argument that vanished with it: the refusal to lose is what produces the losing.** 王弼 (*Wáng Bì*) states the mechanism — 求而得之，必有失焉 (*"seek and get it, and there must be loss"*) — and closes 所謂失道而後德也. **And *clutches* renders 執 (*zhí* — to grasp), which is not in the chapter**; it came from 王弼's gloss on the line above (無執無用), describing what 上德 lacks. 河上公 (*Héshàng Gōng*) reads the contrast as **visibility**, not grasping: 其德不見 against 其德可見，其功可稱.

**One character, one English, three times over.** **上** (*shàng*) read *highest* ×2 and ***Ultimate*** ×3 — a capital, on the rung-marker of a ladder, changing halfway down — against ch 41's *"the highest integrity"* and `glossary/wei-為.md`'s own *"上仁 highest humaneness."* **首 / 始** both read *"the beginning of"* in adjacent lines, though 始 is *beginning* everywhere in the book and 首 (only twice in the book) is 說文's **head with the hair on it**. **華 / 實** had three Englishes across two stanzas, though 河上公 sets them against each other on the page: 失道之**實**，得道之**華**.

**以為 → "has something it acts for."** 王弼: 無以為者，**無所偏為**也. 河上公: 無**以名號**為. *"Deliberate motive"* was an abstraction pointing at neither. The four lines are a 2×2 grid — *does it act?* and *is there something it acts for?* — and the grid is now visible.

**Refused, and why.** ***"The fruit, not the blossom"*** was the better music — 華/實 is the botanical pair, 華而不實 the idiom — but *fruit* against *flower* is heavily churched in English (Matthew 7:16), which is the hymn test firing; **substance** is what the idiom means and what 說文's 富 (a roof over strung cowries) shows. ***"Follows"*** for 而後 was unavailable: it is 從's English at ch 21.

**大丈夫 → "the great person" — the gendered reference removed deliberately, on Shalom's call.** *(This is standing rule 2's **default**, so it is not a `shaloms-call`; the violation was doing it silently.)* 說文 defines 夫 by a ruler and a hairpin — 人長八尺，故曰丈夫, and 一以象簪也, the capping at twenty — so **the word is a measurement and a public marker of adulthood, and there is no gender-neutral reading of it in the Chinese.**

***"The mature person"* failed on two counts**: *maturity* is an **inward** achievement and 丈夫 is **outward and measurable**; and it **fails the 1968 test**, being Allport-and-Maslow vocabulary. ***"A person of full stature"* failed on a subtler one**, and this is the transferable finding: **大丈夫 is a title in an honour system, not a description of a psychological type — and you cannot tell a personality trait to move somewhere else.** 大 → *great* is the book's own intensifier, and 說文's 大象人形 (*"大 depicts a human form"*) means both content graphs are the same standing figure.

**The seam, named rather than erased.** On one reading the chapter **borrows the opposition's vocabulary**: 大丈夫 is a hapax, 聖人 appears in 25 chapters and **not once here**, and ch 38 is where the Confucian ladder lives (禮 in two chapters book-wide, 義 in three). **It is a reading, not a fact** — 河上公 glosses 大丈夫 as 得道之君, our figure and not theirs. **And no English noun could carry it regardless**, because the borrowing rests on a register contrast English readers do not have; the frame the preceding fourteen lines build is what carries it, and the noun's job is only not to fight that frame.

**This is a family, and it now has a row.** 大丈夫 (38), 君子 (*jūn zǐ* — "a ruler's son", 26, 31), 士 (*shì* — a male service rank, 15, 41, 68) are all **male rank-words**, dissolved in two opposite directions: ch 38 turned a title into a psychological type, while **君子 → *"the sage"* hands the opposition's honorific to Laozi's own figure**, whose name is a different word. `WORKLIST` T4-7, cross-referenced to T2-3, T2-6 and T4-1.

### Ch 3 · the closing movement restored, and a sinister register that was ours

*(2026-08-31, Pass D. `WORKLIST.md` T1-3. The chapter's own Notes carry the line-by-line; the general finding is [`collocation-carries-a-verdict`](../process/principles/collocation-carries-a-verdict.md).)*

**The three closing clauses had the opposite grammar from the Chinese.** 常使民無知無欲 (*cháng shǐ mín wú zhī wú yù*) / 使夫智者不敢為也 (*shǐ fú zhì zhě bù gǎn wéi yě*) / 為無為，則無不治 (*wéi wú wéi, zé wú bù zhì*) are built on 使 (*shǐ* — to cause), 使, and 為 (*wéi* — to do / to handle). The English was built on three *"Without"*s — an anaphora nothing in the Chinese repeats. **The Chinese sage acts; the English sage merely abstained.**

**為無為 → *"Without effort"* was a lock breach on the one line the lock's own entry cites as its proof.** `glossary/wuwei-無為.md` argues from ch 3 and 63 that *"為無為 … settles the question: 無為 is something you **actively do** … Keeping your hand off something you are certain you could improve is continuous, **effortful**, and difficult."* Ch 3 now carries ch 63's English exactly: **"Do the not-doing."** *(Harness: `check_locks.py` could not see this. The forbidden list held `"effortless action"` and not `"without effort"`; `"effortless"` and `"without effort"` are now on 無為's list and verified firing. `WORKLIST` T5-3.)*

**治 (*zhì* — to govern / to order) is the chapter's frame word, and it had been dropped from the hinge.** 是以聖人之治 — *"therefore, the sage's governing"* — read only *"Therefore the sage."* 治 opens the second movement and closes the chapter, and the ring was broken. Both ends carry it now, and **無不治 reads "nothing is left ungoverned,"** which makes audible an echo the Chinese has and the English had lost: 無不治 here against 無不為 (*wú bù wéi*) at ch 37 and 48, already rendered *"nothing is left undone."* Same shape, one word apart. Ch 65 — this chapter's sibling, 民之難治 (*mín zhī nán zhì* — "the people are hard to govern") — already renders 治 as *govern* three times.

**Ch 57 is this chapter's own gloss, and it shows that the mechanism is subtraction.** 我無為，而民自化 … 我無欲，而民自樸 — *"I do not do, and the people transform themselves … I am desireless, and the people become plain of themselves."* The operative character is 自 (*zì* — of themselves). All three of stanza 1's 使 clauses have a **not** as their cause, and 王弼 spells the mechanism out: 故可欲不見，則心無所亂也 — *"so when the desirable is not displayed, the heart has nothing to disorder it."* Nothing is put into anyone. The second movement's two 使 clauses are now treated exactly as stanza 1 already treats its three: **result of the arrangement, not an act performed on persons.**

**河上公 reads the whole movement as a body, not a population.** He opens it 聖人治國與治身同也 — *"the sage's governing of the state and the governing of the self are one and the same"* — and glosses 實其腹 as 懷道抱一守五神 (*"harbor the Tao, embrace the one, guard the five spirits"*) and 強其骨 as 愛精重施，髓滿骨堅 (*"cherish the vital essence and be sparing in spending it; the marrow fills and the bones grow firm"*). *Govern* does not shut that reading out; it is the word that holds both.

**What is not smoothed.** It remains a ruler arranging the conditions under which other people want things, and 河上公 titles the chapter 安民 (*ān mín* — "settling the people"). **Paternalist is not sinister, and the chapter owns the first.** What the old English added — withholding, breaking wills, suppressing the clever — is a register the Chinese does not have.

**常 → "ever," 無欲 → "desireless."** 常…無欲 is a formula this manuscript already renders **"Ever desireless"** twice, at ch 1 (of the reader) and ch 34 (of the Tao). The 常 lock licenses plain *ever / always* adverbially; it had been dropped from this line altogether, the same fault as ch 28's three 常德.

**弱其志 → "ambition," not "striving."** 說文解字: 志，意也 — *"intent."* 王弼: 志生事以亂 — *"ambition generates affairs, and so brings disorder."* CLAUDE.md's own gloss of the line is *"weaken their ambition."* 弱 keeps **weaken** because it takes an object, which the lock licenses; the coercion was in *will*, not in *weaken*. **志 is still split** — *ambition* here against *will* at ch 33 — and that is `WORKLIST` T2-7, not settled here.

**敢 applied; it had been dropped outright.** 不敢為 → **"never push to act,"** joining ch 30, 64, 67, 69, 73 and 74.

**智者 → "the knowers," and the choice is governed by a fork, not by a preference.** *"Cunning"* is gone — it had covered both 知 (*zhī* — to know) and 智 (*zhì* — knowing-how) in consecutive lines and renders no character it owns. **無知 → *unknowing***, ch 10's word for the same compound (能無知乎), where it is asked of the practitioner. **智者 → *the knowers*.** *(Shalom's word, against two of mine.)*

**王弼 (*Wáng Bì*) prints 智者 and 河上公 (*Héshàng Gōng*) prints 知者 — and they then describe different people.** 王弼: 智者謂知為也, *"those who know how to handle"* — the operators the line restrains. 河上公: 思慮深，不輕言, *"deep in deliberation, they do not speak lightly"* — almost verbatim what he says of the approving 知者 at ch 56 (知者貴行不貴言也, *"the knower prizes action and does not prize speech"*). His phonetic note 知音智 sits on this line and **not** on the 無知 two lines above, so the tradition reads two words in consecutive lines even where one graph is written. **This is the *commentaries are evidence* rule in force:** *"those who know how"* and *"the clever"* are each specific enough to settle the fork, and settling it picks 王弼's side. ***The knowers* is a bare nominalization — what 者 (*zhě*) does in Chinese — and holds both.** Fork logged in `sources/variants.yaml` and `notes/manuscript.md`.

***"Those who know" was tried and refused*** — it is 知者's English at ch 56 (知者不言) and ch 81 (知者不博), in both places naming the sage's side. The **string** collided; the **family resemblance** did not, and 河上公 makes that resemblance deliberately. *The knowers* also chimes with *unknowing* one line above, which is what his text does with one graph twice. **The book-wide 智 split stays open** — disparaged at 18, 19, 65 and neutral at 33. `WORKLIST` T2-2.

**Ch 3 · 心 restored to line 3, and 亂 → "disturbed."** 使民心不亂 had dropped 心 (*xīn* — heart) at its first appearance, two lines before 虛其心 empties it — the joint that makes 王弼's anatomy legible (心懷智而腹懷食，虛有智而實無知也 — *"the heart harbors clever knowing and the belly harbors food: empty what has 智, fill what has no 知"*). **Knowing lives in the heart, so 虛其心 and 常使民無知 are one instruction.** *Perturbed* rendered no character.

**The choice was between the ring and the organ, and the organ won.** 說文解字 glosses 亂 as **治也** — *"to put in order"* — the graph being hands at tangled silk with the tool that untangles it, so **亂 and 治 are one act read from both ends** and this chapter opens on the first and closes on the second (無不治). No English word holds both. *Disordered hearts* is clinical, and 亂 here is done **to** the heart from outside (王弼: 心無所亂也). ***Confused* was refused on the stronger ground** that it puts the damage in the **knowing**, which the chapter has just spent two lines separating from the heart; 河上公's 不惑亂也 pairs 亂 with 惑 (*huò* — led astray) and is still agitation, not misunderstanding. **Rider:** ch 26's *"undisturbed"* wears the word for 燕處超然, which has no 亂 — it goes with T2-5/T2-6.

**Still open on this chapter:** line 1's *"have no cause to contend"* asserts a causal claim 不爭 does not make, and it is the last of the three opening clauses whose negation does not match the other two.

### Ch 4 · the chapter rebuilt, and 帝 restored — Pass D's first

*(2026-08-31. `WORKLIST.md` T1-2, closing T2-14c. Full argument for 帝 in `glossary/di-帝.md`, now locked; the chapter's own Notes carry the line-by-line.)*

**Four faults and a missing line.** 道沖 was **inverted and given 器 (*qì* — vessel)'s word** — 沖 (*chōng*) is *empty*, 不盈 is *never fills*, and the English said *"a vessel that never runs empty"*, both halves flipped. 淵 (*yuān* — a pool of turning water) was **dropped**, taking with it one of two matched 兮 frames. 吾不知誰之子 (*"I do not know whose child it is"*) was **not translated at all**. And 帝 (*dì*) was **erased into "ancestor."**

**The 帝 finding is the one that matters, and it is the inverse of the overlay we usually hunt.** The naturalistic razor strips theism read **into** a word. Here the Chinese names a god and the English **deleted** him — deleting with him Laozi's own demotion of him. **帝 comes to this text as a god the Zhou had already deposed**, replaced by 天 (*tiān*) when they invented 天命 (*tiān mìng* — the Mandate of Heaven) to justify the conquest; by 288 BCE living kings were taking the title (東帝 / 西帝) and by 221 秦始皇帝 had fixed it to the throne. **Read against 誰之子 two lines above — and against 天子 (*tiān zǐ*, "child of the sky") at ch 62 — the line takes the floor out of legitimation:** authority descends, and a thing with no parent standing before any god leaves the chain with nothing at the bottom.

***"Any god," not "the high god."*** The definite article asserts a singular supreme deity at the top of a hierarchy — which the scholarship on Shang religion has not settled — and it does so where no reader weighs it. **A rendering must not assert what the entry says is unsettled, and the definite article confers status exactly as a capital does** (standing rule 5). *Any* is also the stronger claim: precede only *the* high god and a claimant can answer *"my line descends from a different power."* **This is now a general principle: *the* can smuggle a doctrine as effectively as a capital letter.**

**兮 (*xī*) never hedges**, across all twelve occurrences: **[asserted quality] 兮，[hedged predicate]**, as ch 15's seven-line series shows. So in 湛兮，似或存 the submersion is *stated* and only 存 is in doubt — which killed a draft reading *"Submerged. It seems to be."*, where English's ellipsis reached backward and took *submerged* as the missing complement.

**存 (*cún*) is being-still-there, against 亡 (*wáng* — to perish)** — ch 41's 若存若亡, and 河上公's gloss on this line, 長存**不亡**. Two candidate Englishes were refused on evidence: ***remain* imports a depletion frame the chapter's first line denies** (leftovers are what survive consumption; 用之或不盈 says the Tao is not consumed), and ***exist* belongs to 有 (*yǒu*)** at ch 32, 39 and 64. *"It seems to be here"* reads as **presence**, not location, which is what 存 is.

**象 is the comparison, not the noun, and the argument went the other way first.** 象 (*xiàng*) is *image* at 無物之象 (14), 其中有象 (21), 執大象 (35), 大象無形 (41), and 似 is the dedicated hedge already used twice in this chapter — so a draft closed on *"An image, older than any god."* **The grammar defeats it: wherever 象 is unambiguously a noun it is marked as one, by 之, 有 or 大; here it stands bare before a noun phrase, which is verb-plus-object.** Both commentaries agree, and ch 4 is 象's first appearance, so *image* would land where no reader could yet hear it. **A distributional argument is a reason to look, not a reason to conclude.**

**A stranded subject, and a rule that reaches further than em-dashes.** A draft split the quatrain into two sentences and left the second without a subject: *"Dims its own light, merges with the dust."* **Standing rule 5's reasoning is about the fault, not about the dash** — *"classical Chinese omits subjects freely, English cannot"* — and a full stop strands a subject exactly as a dash does. The couplet now runs on a comma with a lowercase continuation line, this manuscript's convention at ch 2, 7, 16, 19, 25, 31, 34, 43, 47, 48 and 49. **Ch 56 needs no repair**: its version is imperative, so each line is already a complete sentence.

**誰之子 → "whose child," and *descendant* is refused on 說文's own distinction.** 孫 (*sūn* — grandchild) is glossed 子之子曰孫。从子从系。系，續也 — *"the 子 of a 子 is called 孫; from 子 and 系 (to connect), and 系 means to continue."* **The generations are separated in the language, and the compound for descendants — 子孫 — is one this book uses**, at ch 54's 子孫以祭祀不輟. Ch 4 writes bare 子, a **pictograph of an infant**. The distinction carries the argument: **天子 at ch 62 is the *child* of 天, one generation, direct**, and ch 52 pairs 母/子. *Descendant* would soften the line to *"its ancestry is untraceable"* when the claim is that **there is no parent at all.**

**The quatrain keeps the Tao as its subject**, closing Pass C's one deferred question. With 道沖 restored the subject chain runs unbroken, which is 王弼's reading of these four lines here against 河上公's imperative; ch 56 keeps the imperative, and the divergence is now argued rather than inherited.

### Ch 31, 26 · 君子 → "the noble", and 左/右 restored

*(2026-09-07. Full argument in ch 31's own `## Notes`.)*

**君子 (*jūn zǐ*) was reading "the sage," which is 聖人's word in 38 English lines.** 君子 is literally *a ruler's child* and is the **Confucian** honorific; giving it 聖人's English made Laozi's figure and Confucius's the same person. Now **the noble**, at ch 31 and at ch 26, its only other appearance. *The gentleman* was the alternative — it would have made the borrowing visible on the page — and was declined for the male default *(Shalom's call)*. **Seam noted:** 君子 named a male class and the English is deliberately neutral. T4-7.

**左 and 右 had been deleted from 君子居則貴左，用兵則貴右** and replaced with *creation* and *destruction*, while the same two characters read literally four lines later. **The substitution also reversed the argument:** the old English had the sage *choosing destruction* in war, where 河上公 says 此言**兵道與君子道反** — *"the way of arms and the way of the 君子 are opposed"* — and the next line says outright 非君子之器, *not the 君子's instrument*. **左/右 are also this book's own pair:** 河上公 glosses them 貴**柔弱**也 against 貴**剛強**也, the locked *yielding* against the locked *strong*.

**Four flattenings in one chapter:** 器 ran *instruments* / *tools* (locked *vessel / tool / implement*); 兵 ran *weapons* / *the military*; 美 ran *revel* / *glorify* in adjacent lines; and **以喪禮處之 — five identical characters, twice — ran *placed by the rites of mourning* against *treated like a funeral rite*.** All unified.

**偏將軍 / 上將軍 → "the deputy general" / "the higher general."** *Lieutenant general* and *supreme commander* imported modern ranks and lost the passage's point — 河上公: the deputy is 卑 (lower) yet takes the yang side 以其**不專殺**也, *because he is not in charge of the killing*; the senior is 尊 (honoured) yet takes the right 言其**主殺**也, *meaning he presides over it*. **The senior officer takes the inferior seat because he is the one who kills.**

### Ch 41 · the 建言 catalogue rebuilt, and 建 licensed to flex

*(2026-09-06 / 07. Full argument in ch 41's own `## Notes`.)*

**故建言有之 introduces a quotation, and twelve proverbs followed it packed onto five English lines.** `--formulas 41` shows the chapter is almost nothing but frames — ▢士聞道 ×3, ▢道若▢ ×3, ▢德若▢ ×3, 大▢無▢ ×2, and 大▢若▢ five times across **ch 41 and ch 45 together**. The English also changed shape as it went (*"Bright Tao seems dark"* against *"The highest integrity seems **like** a valley"*). Now one saying per line.

**大白若辱 → "The great white seems disgraced."** *(Was "true purity seems soiled.")* **大 had been replaced by *true*** — a breach of `glossary/da-大.md` that **no check can catch**, since every rule keys off a forbidden word and this is an absence. 白 is *white*, not *purity*; and 王弼 quotes ch 28 outright — 知其白守其黑，大白然後乃得 — so the old line severed a link the commentator states. 辱 → **disgraced**, matching ch 28's 守其辱 and ch 13's 寵辱.

**建 (*jiàn*) takes two Englishes in one chapter, deliberately** — *"the **established** sayings"* (建言) and *"**Sturdy** integrity"* (建德). They were unified to *established* first and the unification was undone: in English *"established integrity"* collapses into **long-standing**, a reputation, which is the opposite of the line. **The grammar licenses the split** — 建言 is a fixed compound (a received body of maxims), 建德 is 建 modifying a noun — the same pattern as 事 and 弱. The cost is that a reader cannot see the shared character; the chapter notes carry it.

**廣 → "boundless."** *Broad* stated a width without implying abundance, so *broad → not enough* was no paradox. 說文 廣: 殿之大屋也, *"a great hall of a palace,"* on 广 (a roof); 王弼: 廓然無形，**不可滿也**. **Boundless says why it seems insufficient — there is no edge to arrive at.** 廣 still reads *reach far* at ch 67; two chapters, two Englishes, `WORKLIST.md` T2-45.

**Also: 夷 → level** (王弼: 不執平以割物, tying it to ch 28's 大制不割); **不足 → not enough**, carrying ch 35's settled rendering; **質真 → substantial truth**, the superlative in *"the most solid truth"* being invented.

**⚠ `--formulas` missed a third 德 saying.** It reported ▢德若▢ ×2 and did not catch 廣德若不足, because 不足 is two characters and the finder matches whole comma-segments — `WORKLIST.md` T5-13, confirmed on a live line for the first time.

**士 (*shì*) is now locked to "in service"** (`glossary/shi-士.md`), across ch 15, 41 and 68. 說文 defines it in two characters — **士，事也**, *a 士 is 事, affairs* — which is the character whose graph is a hand gripping the badge of office; the 一 + 十 reading attached to a Confucius quotation is Han philosophy over a shape, as 董仲舒's is for 王. **The commentators diverge and that decided it:** 王弼 reads 士 as an office (士卒之帥也, *"the commander of the troops"*), 河上公 as a disposition (言貴道德，不好武力). *In service* leaves both standing where *officer* — the stronger English, and 王弼's reading exactly — would pick one, and was declined as bureaucratic. *Student* was never available: nobody in ch 41 is at school, and 河上公's middle 士 is 治國以太平, governing a state. **Seam noted per standing rule 2:** 士 named a male class, and the English is deliberately neutral.

### Ch 14, 15, 25 · 混 → "mixed", and 大 locked to "great"

*(2026-09-06. Full argument in ch 25's own `## Notes`.)*

**大 is now locked to "great"** (`glossary/da-大.md`, 2026-09-06), with *large* (60, 61), *greater* (comparatives) and *master* (大匠) as licensed flexions. **Expansion to *vast* across the whole book was weighed and declined.** It has more force in English than *great*, which has been worn smooth — but it fails on two-thirds of the 51 lines: the comparative 禍莫**大**於 gives *"no vaster disaster"*; the severity of 大患, 大偽, 大迷 is *severe*, not immense; 大匠 is a **master** carpenter and 大丈夫 a **great person**, both seniority; and 下士聞道，**大**笑之 is laughing *aloud*, no magnitude at all. **The deciding argument is that 大 is a worn word in Chinese and the wear is load-bearing.** 說文: 天大，地大，人亦大。故**大象人形** — *"therefore 大 depicts a human form"* — a person with their arms out, the plainest bigness there is. Ch 25 names the Tao 大 as an admitted defeat (王弼: 大有繫則必有分，有分則失其極矣, *"大, once tied, must have divisions; having divisions, it loses its utmost"*), so an English carrying more charge than the original would make the forced name sound like it worked. *Vast* is also spoken for — 廣 (*guǎng* — broad) at ch 41 and 恢 (*huī*) at ch 73.

**大 (*dà*) was *vast* in ch 25 and *great* in 41 lines everywhere else** — and ch 25 uses it **seven times**, as the Tao's own forced name. **Ch 34 makes the identical move and reads differently:** 可名為大 → *"it can be called great"* against ch 25's 強為之名曰大 → *"I call it the vast."* The reverse direction was worse: *vast* also carried 廣 (*guǎng* — broad, ch 41) and 恢 (*huī*, ch 73), so one English wore three characters. Ch 25 now reads **great** throughout. **⚠ Ch 67 is deliberately not swept** — its 天下皆謂我**道**大 reads *"Everyone says **I** am vast,"* with 道 dropped and the sentence handed to the speaker; the term swap would only make the existing fault louder. T2-42.

**混 (*hùn*) had three Englishes in three chapters** — *blend* (14), *Blended* (15), *undifferentiated* (25) — and is now **mixed** in all three. 說文: 豐流也。从**水**昆聲, *"abundant flow,"* on the water radical: the mixing sense comes from a full river carrying everything along, which is exactly what muddy water is at ch 15. Ch 15's seven similes are seven **single words**, which ruled out the two-word candidates on the spot *(Shalom's call)*. Ch 25's 有物混成 → *"Something mixed and complete"*, keeping 混成's paradox: undifferentiated, and already whole.

**The reverse search found a rider.** *Blend* was also doing duty for 沖 (*chōng*) at ch 42 — 沖氣以為和, *"blending the vital breath"* — where ch 4's Pass D work settled 沖 as **empty**. Freeing the word from 混 isolates ch 42 rather than fixing it. T2-41.

### Ch 15 · the chapter reworked whole, and 蔽 read as *covered* rather than *worn out*

*(2026-09-06, Pass D. Full argument in the chapter's own `## Notes`.)*

**The closing line had stopped meaning anything, which is how the rework started.** 故能蔽而不新成 (*gù néng bì ér bù xīn chéng*) read *"They can become weathered, and have no interest in appearing new"* — an English that takes 敝 (*bì* — worn out) where our base prints **蔽** (*bì* — to cover, to screen). 河上公 (*Héshàng Gōng*) prints 蔽 and glosses it 蔽者**匿光榮**也, *"蔽 means **hiding one's radiance and glory**."* The line is about staying out of sight; *weathered* had made it about patina.

**The 說文解字 (*Shuōwén Jiězì*, c. 100 CE) separates the two graphs cleanly.** 蔽 is 小艸也。从**艸**敝聲 — *"small grasses,"* on the 艸 (*cǎo* — growing plants) radical: the covering is **foliage**. 敝 is 帗也。一曰**敗衣** — *"a cloth; one definition says worn-out clothing"* — on 㡀 (*bì* — cloth in tatters). **Plant cover against a rag.** They share a phonetic, which is why manuscripts confuse them, and why the base's 蔽 has to be honoured rather than silently read as 敝.

**The chain that makes the line legible: 盈 (*yíng* — full) is 滿器也, "a full vessel," on the 皿 (*mǐn* — container) radical.** A full vessel is a finished vessel, and a finished thing is a thing there is something to say about. 河上公 runs it himself: 夫唯不盈滿之人**能守蔽**不為新成. Someone who never fills has nothing that needs showing, so being overlooked costs them nothing. **能 (*néng*) is *can*, a capacity — not a wish to hide**; an English that makes concealment a goal puts a strategy into a chapter that recommends none.

**新 (*xīn*) is 取木也。从斤新聲 — "to take wood," on 斤 (*jīn* — an axe).** 樸 (*pǔ* — uncarved wood) six lines up is timber the axe has not finished with; 新成 is timber it has. The etymology is not the reading — 新 means *new* by the Warring States and we render it so — but it explains why the chapter's last image answers its middle one.

**A rendering retired the same day it was written.** The closing first read *"they can stay covered, never finished, never new"* — a chime that split **不新成 into two negations when it is one compound**, giving 新 an independent negation the Chinese does not have. 不新成 is *not newly-completed*, not *not-new and not-completed*. Now **"they can stay covered, and never newly made."*

**Against it, and why it loses.** Ch 22's 敝則新 (*bì zé xīn*) pairs the worn-out graph with 新 and looks like the same formula. But the base prints **敝** at 22 and **蔽** at 15, and under the wear reading the chapters collide: worn-out-becomes-new is the good outcome at 22, worn-out-and-not-new at 15. Under *covered* there is no clash.

**此 (*cǐ*) is anaphoric, not partitive.** 保此道者 had read *"One who holds the Tao"*; the literal *"those who guard **this** Tao"* implies a second Tao in English, which the Chinese does not. 此 points back at the two 孰能 questions — 河上公 expands it to 保**此徐生**之道 — so the pointer now attaches to the manner: **"Those who guard the Tao like this."** 保 also moves from *holds* to **guard**, matching ch 9's 不可長保.

**Two formulas repeat inside this one chapter and had been rendered twice each.** 不可識 (*bù kě shí*) ran *"fathomed"* then *"known"*; it is now **"could not be read"** both times. 說文 defines 識 as 一曰**知**也, on the **言** (*yán* — speech) radical — telling *what a thing is*, which is why *perceived*, a sensory word, drifts from it. **"Named" was refused hardest:** 名 (*míng*) runs 21 lines across 9 chapters and **ch 14 has 繩繩兮不可名, *"it cannot be named"*** — same grammar, adjacent chapter, different character, so *named* here would assert a formula the text lacks. **"Known" was refused on scale:** *know* carries 58 English lines, nearly all 知 (*zhī*), while 識 appears in two chapters; 知 is absent from ch 15, so the clash is book-wide rather than local, but it buys nothing. *Read* is free on a whole-manuscript reverse search. An intermediate *"could not be made out"* was retired the same day: it read as slang, and it **invented a parallel with *newly made* in the closing line** where 識 and 新成 share nothing. **Where the Chinese does not repeat, the English must not either** — the mirror of `DISCOVERIES.md` §6, and no tool looks for it (`WORKLIST.md` T5-14). 夫唯 (*fū wéi*) ran *"Because they cannot be known"* against *"Because they don't seek to become full"*; both are now **"Precisely because"**, and the invented *seek* is gone. `DISCOVERIES.md` §6 in miniature.

**靜 and 安 had been swapped.** 靜 (*jìng* — stillness) was rendered *"sit"* while 安 (*ān* — at rest) took *"still"*, and the second question's *"move in ways that gradually stir life"* padded a strict grammatical mirror out of parallel. The two 孰能 lines are now the same shape: *"by stilling it slowly come clear"* / *"by moving it slowly come to life."*

**Three restorations in the seven similes.** 將 (*jiāng* — about to) had been dropped — the ice is **about to** melt, and the not-yet is the point in a chapter of not-yet things. 涉 (*shè*) is to **ford**, so 冬涉川 is crossing a river *in winter*, not a *frozen* river. And 若 (*ruò*) appears in all seven similes, so all seven now carry **"like"**; *"as if wary of"* had broken the series at line two.

**士 (*shì*) is rendered "in service" here, provisionally.** Three Englishes across 15, 41 and 68 for one character, two of them on the identical phrase 善為士者 — `WORKLIST.md` T2-3, and the rank-and-gender question at T4-7. **Note the seam:** 士 named a male class and the English is deliberately neutral.

### Ch 45, 81 · 辯 → "argue" — and the 大X若Y frame does not endorse its X

*(2026-08-31, Pass C. `WORKLIST.md` T2-9. Closes Pass C.)*

**辯 (*biàn*) read *eloquence* at ch 45 and *argue* at ch 81, and ch 81's own Notes had licensed the split**: *"there 辯 is praised and paired with 訥 (stammering), a different slot."* **The premise is wrong.** Ch 45 now reads *"Great argument seems halting."*

**The frame does not praise its X — it says the greatest form of X is unrecognizable as X.** Ch 45 runs five: 大成若缺 · 大盈若沖 · 大直若屈 · 大巧若拙 · 大辯若訥. **And the line directly above 大辯若訥 proves it.** 大巧若拙 puts 巧 (*qiǎo*) in the frame, and 巧 is condemned twice elsewhere — ch 19's 絕巧棄利 (*jué qiǎo qì lì* — "cut off cunning, abandon profit") and ch 57's 人多伎巧 ("the more cunning people become, the more strange contrivances appear"). Nobody read *that* as praise, and 大辯 sits in the same list.

**The commentators put 大辯 and 不辯 almost on top of each other.** 王弼 (*Wáng Bì*) on ch 45: 大辯**因物而言**，己**無所造**，故若訥也 — *"great 辯 speaks according to things; the self **invents nothing**, and so it seems halting."* 河上公 (*Héshàng Gōng*) on ch 45: 大辯者智無疑，如訥者口尤辭 — *"one of great 辯 knows without doubt, and like a halting person has few words."* And 河上公 on ch 81's 善者不辯: 善者以道修身，**不綵文**也 — *"the masterful cultivate themselves by the Tao and do not **ornament** their words."* **Both chapters say: do not manufacture speech.** The paradox is that the greatest arguing looks like inarticulacy *because it is not arguing.*

**So this is not the 強 (*qiáng*) case.** There, the character genuinely carries opposite valences — the disease at ch 76 and the cure at ch 52 — and an English carrying a verdict cannot do both jobs. Here there is no double to preserve: **"eloquence" manufactured the appearance of one.**

**And *eloquence* is not what 辯 means.** 說文解字: **治也。从言在辡之閒** — *"to put in order; from 言 (*yán* — words) placed between 辡."* 辡 is **two 辛 (*xīn*, tattooing knives, the convict's mark) facing each other**: words between two disputants. Fine speech is a different word in ch 81's own opening — 美言 (*měi yán* — "pretty words").

**訥 → "halting," not "awkward."** 說文: **言難也** — *"difficulty in speech."* It is specifically about speech; *awkward* is generic and could be any clumsiness, which is 拙 (*zhuō*)'s job one line above. *Halting* is what both commentators describe (河上公's 口尤辭, *"the mouth has few words"*).

**Left open, and now a row of its own: 巧 has the identical problem** — *skill* at ch 45 against *cunning* at ch 19 and ch 57 — in the very line above this one. It is not folded in here because ch 19's Notes carry an argument about 巧利 as **goods** (王弼: 巧利，用之善也, *"cunning and profit are the best of use"*) that deserves its own hearing. `WORKLIST` T2-20.

### Ch 27, 52 · 襲 → "covered" — the layered robe, not the inheritance

*(2026-08-31, Pass C. `WORKLIST.md` T2-10. The manuscript half is in `notes/manuscript.md`; the fork is now in `sources/variants.yaml`.)*

**The two Englishes were not two readings of one character — they were readings of two characters.** Ch 27's *"inherited clarity"* rendered 襲 (*xí*); ch 52's *"the practice of the ever-present"* rendered **習** (*xí* — to repeat, to drill), which our base text does not print. Both commentaries do print 習 at ch 52, and 河上公 (*Héshàng Gōng*) glosses it 習修常道, *"practising and cultivating the constant Tao"* — so the English was following a real reading, just not ours, and nobody had recorded the fork. **We keep 襲 in both**, on the structural argument set out in the manuscript note: 是謂襲明 and 是謂襲常 are the identical frame, and 明 / 常 are bonded by 知常曰明 at ch 16 and ch 55.

**襲 is grave-clothes.** 說文解字: **左衽袍** — *"a robe with the lapel closed to the left."* The living close a robe right over left; **the dead are dressed left over right.** The graph is 衣 (*yī* — clothing) with 龖 abbreviated for sound, and every later sense — to double, to succeed to, to fall upon — descends from **one garment put on over another**. So 襲明 is not clarity received from ancestors. It is **clarity worn, and therefore covered.**

**Which is what both chapters are about.** Ch 27 opens 善行無轍跡 (*shàn xíng wú zhé jì* — "masterful traveling leaves no tracks") and runs through five masteries that leave no mark, closing on this line; the summary says the clarity is under something. The book says it elsewhere in plain images — 被褐懷玉 (*bèi hè huái yù* — "wears coarse cloth, carries jade at the breast," ch 70) and 光而不耀 (*guāng ér bù yào* — "bright but not dazzling," ch 58). Ch 52's line closes a movement that has just said 用其光，復歸其明 — *"use the outer light, return to your inner clarity"* — the same motion of putting the shine away.

```
ch 27   This is called clarity worn covered.
ch 52   This is called holding the ever-present covered.
```

**"Inherit" is gone from the book, and *practice* returns to ch 41 alone**, where it renders 行 (*xíng* — to walk, to carry out) in 勤而行之.

**Rejected: keeping *practice* at ch 52 on the commentators' authority.** It is a real reading with both of them behind it, and the cost of refusing it is that we render against 王弼 and 河上公 on their own printed text. We accept that cost because the pair is stronger evidence than the copy: 習 is the easier character, which is the direction copying runs, and no argument explains why the identical frame 是謂襲X would take a different character in its second appearance.

### Ch 15, 16, 25, 32, 44, 52 · 殆 → "danger" — and the death radical that was missing from all four Englishes

*(2026-08-31, Pass C. `WORKLIST.md` T2-11.)*

**殆 (*dài*) occurred five times and wore four different Englishes, and not one of them was 殆.** *"Not even death threatens this"* (16), *"Inexhaustible"* (25), *"depletion"* (32, 44), *"no harm will come to you"* (52). It now reads **danger** in all five, and *danger* now renders nothing else.

**說文解字: 危也 — "peril."** The graph is 歺 (*è*) with 台 (*tái*) for sound, and **歺 is the bare-bone radical** — the death element in 死 (*sǐ* — to die) and 殃 (*yāng* — calamity). There is no exhaustion in the character and no energy in it.

**The commentators converge completely — five places, both of them, one word.** No divergence to preserve, which is rare here.

- 河上公 (*Héshàng Gōng*), ch 16: 無殃無咎…乃與天地俱没，**不危殆**也 — *"no calamity, no blame… then one sinks away together with sky and earth, **not in peril**."*
- 河上公, ch 52, the whole gloss: **不危殆也**.
- 河上公, ch 44: 知可止則財利不累身…則身**不危殆**也 — *"knowing when to stop, wealth and profit do not burden the body… then the body **is not in peril**."*
- 王弼 (*Wáng Bì*), ch 25: 周行無所不至而**免殆**, with the Siku note 〔案免永樂大典作危〕 — peril under either reading, never exhaustion.

**Two of the four Englishes were another character's word.** *Harm* belongs to 害 (*hài*) — ch 35, 56, 66, 73, 81. *Inexhaustible* belongs to 窮 (*qióng*) at ch 6 and 35. *Depletion* belongs to nothing at all: it is an energy metaphor, our named besetting temptation, and it is what `WORKLIST` had flagged.

**Ch 16 was not merely inconsistent — it was a mistranslation, and 没身不殆 is verbatim at ch 52.** 没身 (*mò shēn*) is *"to the end of one's body,"* an idiom for **all one's life** — exactly what ch 52 already did with it. Ch 16 read it as *death itself* and handed the sentence to the Tao: *"Not even death threatens this."* 河上公 settles the subject — 乃與天地俱没 — it is **the person** who has climbed 公 → 天 → 道 who sinks away, and **they** who are not in peril. Both chapters now close on *"and to the end of your days, no danger will find you."*

**Ch 25 gained a line it had been missing.** 周行而不殆 read *"Inexhaustible"* — 周行 (*zhōu xíng* — "moves in a circle") was dropped entirely, a debt `WORKLIST` already carried, and 不殆 took 窮's word. It now reads *"It moves in a circle, never in danger, / and can be taken as the mother of the world."*

**Ch 15's *"danger"* was invented, and 河上公 supplies something better.** 猶兮若畏四鄰 (*yóu xī ruò wèi sì lín*) read *"Watchful, aware of danger from all sides"* — **there is no 殆 in ch 15 and no danger in the Chinese**, so no check could ever see it; it surfaced only because the reverse search on *danger* had to be run before locking the word. 河上公: 其進退猶猶如拘制，若人犯法**畏四鄰知之**也 — *"their advancing and retreating is hesitant as if held back, like someone who has broken the law **fearing the four neighbours will find out**."* **It is not peril from every side; it is the fear of being seen.** Now *"Hesitant, like someone wary of the neighbors on all four sides."* *(The "as if" became "like" in the 2026-09-06 rework, restoring the 若 series; "wary" is unchanged.)*

**畏 flexes here, and the flexion is recorded rather than left implicit.** 畏 (*wèi*) reads **fear** in six other lines (17, 20, 53, 72, 74 ×2), always fear *of a thing* — authority, death, what people fear. Here the construction is different: 河上公's 畏四鄰**知之** is fear *that they will find out*, social exposure rather than a threat. English *"fearing the neighbors"* names them as the danger; *"wary of"* keeps the watching. 畏 has no entry yet and this is the line that will decide its shape.

**殆 has no glossary entry**, so *danger* is correct across the book but unenforced. Owed.

### Ch 4, 56 · 挫其銳，解其紛，和其光，同其塵 — the nouns unified, the subject deferred

*(2026-08-31, Pass C. `WORKLIST.md` T2-14, third of three. **This one does not fully close, and that is the finding.**)*

Four verbatim lines — 挫其銳，解其紛，和其光，同其塵 (*cuò qí ruì, jiě qí fēn, hé qí guāng, tóng qí chén* — "blunt its sharpness, untangle its knots, dim its light, share its dust") — in ch 4 and ch 56, with two Englishes. Ch 4 read *"It blunts sharpness, / Untangles the tangled, / Softens brilliance, / Is one with every grain of dust."* It now reads **"It blunts the sharpness, untangles the knots. / Dims its own light, merges with the dust."**

**The live error was a lock breach, and `glossary/ming-明.md` had already ruled on this line.** *Brilliance* is on 明 (*míng* — clear-seeing)'s `forbidden:` list, and the entry names 光 (*guāng*) as 明's counter-term and glosses **both chapters together**: *"光 is outward light — the light a thing **emits**. It is what the sage is told to soften in **Chapters 4 and 56** (和其光 — ***dim your light***)."* The verse contradicted its own entry. `check_locks.py` filed it as `info` rather than an error because 明 is not in ch 4 — the evidence gate — so **only the reverse check could find it.** Third instance this session of an entry ruling one way and the verse going another, after *gut* (ch 12) and the 以此 note (ch 21).

**The subject is genuinely contested, and unlike ch 17/23 the commentators do not cross the split.** 王弼 (*Wáng Bì*) reads ch 4's four lines with **the Tao** as subject — 銳挫而無損，紛解而不勞，和光而不汙其體，同塵而不渝其真 (*"the sharp is blunted and nothing is lost; the tangle is undone and there is no toil; it harmonizes with the light and does not soil its substance; it shares the dust and does not alter its truth"*) — and ch 56's as **a person's practice**: 含守質也 (*"holding to and keeping one's substance"*), 除爭原也 (*"removing the source of contention"*). 河上公 (*Héshàng Gōng*) reads **both** as instruction to a person, in near-identical language. The contexts agree with 王弼: ch 4's lines sit between 淵兮，似萬物之宗 and 湛兮，似或存, both about the Tao, while ch 56's follow 塞其兌，閉其門 (*"block the openings, close the doors"*), unmistakably addressed to a person.

**So this closes only as far as the evidence allows.** The **nouns are outcome-independent** — sharpness, knots, light, dust are the same four things under either subject, and only the verb forms depend on who is acting. Those are unified now. **The subject question travels with ch 4's Pass D rewrite** (`WORKLIST` T1-2), because it is downstream of three things currently broken in that chapter: 道沖 (*dào chōng*) is inverted and given 器 (*qì* — vessel)'s word, 吾不知誰之子 (*"I do not know whose child it is"*) is dropped entirely, and 帝 (*dì* — the Lord) is erased into *"ancestor."* Deciding the subject before those are fixed means deciding it twice.

**Ch 4 is also the weaker witness.** Ch 56 is attested **complete at Guodian** (~300 BCE, bundle A, unit 4), the oldest text there is; **ch 4 is not attested at all** and rests on the silks and later. Where the two disagree, ch 56 holds the older ground.

**Lineation follows the principle rather than a new choice.** [`lineation-is-ours`](../process/principles/lineation-is-ours.md) already settled ch 56's six phrases as **three couplets** — close the senses · blunt-and-untangle · dim-and-merge — and requires consistency within a parallel series. Ch 4 carries four of those six phrases, so they group the same way: two couplets, not four lines.

**What was lost, on the record.** *"Is one with every grain of dust"* was the prettiest line in ch 4 and it is gone. *Every grain* is not in 同其塵, and the extra beat was doing what *"here, now"* and *"precisely"* were doing elsewhere in this pass — expanding where the Chinese points.

### Ch 3, 12, 44, 64 · 難得之貨 → "rare goods" — and 貨 locked to *goods*

*(2026-08-30, Pass C. `WORKLIST.md` T2-14, first of three. Full argument in `glossary/huo-貨.md`; this is the thin record.)*

**The error was not inconsistency. All three Englishes made the line circular.** 不貴難得之貨 (*bù guì nán dé zhī huò*) is a causal claim about **what a ruler does**: the goods are hard to get, the ruler prizes them, people steal. Ours read *"By not valuing **the precious**"* (3), *"**Rare treasures**"* (12), *"does not prize **precious goods**"* (64) — each of which puts the value **in the object**, so *"do not prize the precious"* argues in a circle and the ruler drops out of the sentence. 王弼 (*Wáng Bì*) puts the cause where the Chinese does: 貴貨過用，貪者競趣，穿窬探篋，沒命而盜 — *"prize goods beyond their usefulness, and the greedy race for them: they tunnel through walls, rifle chests, and steal at the cost of their lives."*

**貨 had been wearing three other characters' English.** *the precious* is 貴 (*guì*)'s, and 貴 is the **verb in the same line** at ch 3 and ch 64; *treasures* is 寶 (*bǎo*)'s (ch 62, 67, 69); *wealth* at ch 44 is 富 (*fù*)'s (ch 9, 33, 57). All three are the class of error `check_locks.py` cannot see. **貨 → "goods" in all five places**, ch 44 swept; ch 53's 財貨 is a bound compound and keeps *wealth and goods*, 財 (*cái* — property) holding its own word.

**"Rare," and what it costs.** *Rare* renders **no character** — 難 (*nán* — difficult) goes unspoken. That is deliberate and both alternatives were closed: **"hard" is 堅 (*jiān* — rigid)'s word** (ch 36, 43, 76, 78, where 堅強 is what a corpse is), and 難's own English elsewhere is *difficult* (ch 2, 63, 73), which will not go attributive in verse. *Scarce* was rejected on a stronger ground than register: **scarcity means a need going unmet, and these chapters deny there is any need** — nobody needs jade, and if the wanting were a real shortfall the ruler could not be blamed for it, which unmakes ch 3's stanza. Ch 12 says the same from the other end, 腹 (*fù* — belly, which can be satisfied) against 目 (*mù* — eye, which cannot).

**A general rule this settled, worth keeping.** *"Rare and scarce"* was considered and refused: **one Chinese modifier, one English modifier.** Near-synonym doublets read as emphasis rather than as two facts, and the habit is a period tell — the KJV pairing (*"assemble and meet together," "acknowledge and confess"*) that `process/overlay-audit.md` catalogues. Where a character's sense will not fit one English word, lose part of it and say so in the notes; do not paper the gap with a second word.

**Why the English kept drifting to a value word, in three chapters independently.** There is **no one-word English adjective meaning "difficult to obtain" that is not also a value word**, because in English, difficulty of acquisition is *how we say* a thing is valuable. Naming that pull is what lets us stop on the near side of it.

**Ch 3 gained two things beyond the noun.** 不貴 now reads *prizing* in both ch 3 and ch 64 (was *valuing* / *prize*), matching 貴食母 (*guì shí mǔ* — "prize feeding from the mother") at ch 20. And 民 (*mín* — the people) is restored to the middle clause of the triad — 使民不爭 / 使民不為盜 / 使民心不亂 all carry it, and ours had rendered it *"no one"* in the second alone. **This introduces no word the stanza does not already use, and settles nothing about the deferred 民/人 call** (`WORKLIST` T4-1).

**The Chinese triad is deliberately lopsided and our English had flattened it.** Ch 3's three objects are 賢 (*xián* — the talented, 1 character), 難得之貨 (4), 可欲 (*kě yù* — what can be desired, 2). *"The exceptional / the precious / the desirable"* imposed a neat symmetry by shrinking the longest object to two words. The middle line is now the heaviest again, as it is in the Chinese.

**Left open in the entry, and it is real:** ch 70's couplet 知我者希，則我者貴 (*"those who know me are few; those who pattern themselves on me are precious"*) has 河上公 (*Héshàng Gōng*) deriving value **from** scarcity — 希，少也…故為貴也 — which is the very inference ch 3 and ch 64 tell a ruler to break. Same commentator, opposite direction. The book does not say where the line falls.

### Ch 12, 38, 72 · 故去彼取此 → "They let go of what is out there and take what is here."

*(2026-08-30, Pass C. `WORKLIST.md` T2-13. The companion to the 以此 note below — same 此 (*cǐ* — this), now with its opposite 彼 (*bǐ* — that, yonder) beside it.)*

**彼 occurs exactly three times in the whole book, and all three are this formula.** 故去彼取此 (*gù qù bǐ qǔ cǐ* — "therefore let go of that and take this") is a **stock closing tag**: five characters, three chapters, always the chapter's last line. There is no competing context anywhere in the text, so there was never a reason for three Englishes — and we had three: *"Rejects the hungry gaze, chooses gut wisdom"* (12), *"Rejects surfaces and embraces life's thickness"* (38), *"They let go of what is out there and take what is here"* (72). **All three now carry ch 72's line.**

**Only ch 72 was translating the line.** Ch 12 and ch 38 rendered the **referents** and deleted the **deixis** — they said what 彼 and 此 point at and dropped 彼 and 此 themselves. Ch 72 does the opposite: it renders the axis and names no referent. That is the distinction settled when a bare *"that / this"* draft was killed there — pointing is not the problem; **English *that/this* cannot sort four items into two pairs**, and ch 38 has four referents too (厚 *hòu* thick · 薄 *bó* thin · 實 *shí* fruit · 華 *huá* flowery display).

**The axis is the same in all three, and it is spatial: what is rejected is always the thing that requires reaching outside yourself.**

- **Ch 12** · 彼 = 目 (*mù* — eye), 此 = 腹 (*fù* — belly). 王弼 (*Wáng Bì*): 為腹者，以物養己；為目者，以物役己 — *"one who acts for the belly uses things to nourish themselves; one who acts for the eye uses things to enslave themselves."* 河上公 (*Héshàng Gōng*): 去彼目之妄視，取此腹之養性 — *"let go of that, the eye's reckless looking; take this, the belly's nourishing of one's own nature."*
- **Ch 38** · 彼 = 薄 + 華, 此 = 厚 + 實. 河上公, flatly: 去彼華薄，取此厚實 — *"let go of that flowery thinness; take this thick substance."* The two lines above are already **locational** — 處 (*chǔ* — to dwell) and 居 (*jū* — to reside), twice each — so the spatial English fits ch 38 best of the three.
- **Ch 72** · 彼 = 自見 (*zì jiàn* — self-display) + 自貴 (*zì guì* — self-pricing), 此 = 自知 (*zì zhī* — self-knowing) + 自愛 (*zì ài* — self-loving). Display and pricing need an audience; knowing and loving need nobody.

**故 (*gù* — therefore) stays unrendered**, as at ch 24 and ch 31: English carries the inference by adjacency, and three flat closing verdicts read better than a chain.

**What was lost, on the record.** Ch 12's *"the hungry gaze"* was the most vivid phrase in the chapter. It goes, and should: 目 is already *"the eye"* in the line directly above, so the image is not lost but merely not repeated — and *hungry* was borrowed from 河上公's gloss 妄視 (*wàng shì* — reckless looking), a commentator's word, not the text's. Ch 38 lost nothing: its old line **repeated** *thickness* from the line above, restating where the Chinese points.

**A third gain: *embrace* is freed.** The word had been renderng **four characters** — 抱 (*bào* — to embrace: ch 19, 22, 42, 54), 守 (*shǒu* — hold fast: ch 16, which is `WORKLIST` T1-6, the 守/抱 swap), 有 (*yǒu* — there is: ch 46's 天下有道), and 取 (*qǔ* — to take: ch 38, here). Ch 38's was the loosest and comes off free. Two remain, and they belong to T2-19, the holding family.

**Ch 12's *"gut wisdom"* was a lock breach, and closing it exposed a hole in the harness.** See the entry note in `glossary/xin-心.md`: 腹 (*fù* — belly) sits inside 心 (*xīn* — heart) as a `covers:` character, and **`covers:` records a `render:` but no `forbidden:` list**, so *gut* was unforbidden book-wide. The entry has a paragraph headed *"Why 'belly' and not 'gut'"* naming *trust your gut* as the import that must not happen and citing ch 12 as its evidence — and ch 12 used the word anyway, one line below its own correct *belly*. `"gut"` is now on **心's** `forbidden:` list, which works because 心 is present in both chapters where 腹 appears; verified firing. **It is also the second instance of the register principle above** — *trust your gut* is the same family as *be here now*, and it swaps a Warring States claim about **hunger** for a modern one about **intuition**.

### Ch 21, 54, 57 · 以此 → "By this." — one formula, one English

*(2026-08-30, Pass C. `WORKLIST.md` T2-12.)*

Three chapters close on the same seven-character formula — 吾何以知…**然**哉？**以此** (*wú hé yǐ zhī… rán zāi? yǐ cǐ* — "how do I know… it is so? by this") — and it had **three different Englishes**: *"By this, here, now"* (21), *"By precisely this"* (54), *"By this:"* (57). `DISCOVERIES.md` §2 rests on the claim that Laozi asks one question about the world, about the origin of everything, and about his own political claims, and gives the **identical** answer each time. The manuscript did not show it. **All three now read "By this."**

**以此 is 以 (*yǐ* — by means of) + 此 (*cǐ* — this). Two characters, two words, nothing added.** *"Precisely"* has no warrant in the Chinese. *"Here, now"* had worse than none — it was 河上公's gloss 此，今也 (*"'this' means now"*) lifted into the verse, which is the error the standing principle above now names, and it landed the book's central epistemological line in 1971 American mindfulness idiom. Both additions did the same damage in opposite registers: **they explained, where 以此 only points.**

**Ch 57 keeps its colon** — *"By this:"* — because the colon is punctuation, not a word, and the lineation is ours by standing principle. Its 以此 is the only one of the three that points **forward**, opening the list of four 天下多… lines that follow; 21 and 54 are chapter-final and point back. The formula still reads identically.

**Rider, same line: ch 57's 其 (*qí* — it, its) had been rendered *"this"***, putting two different characters in the same English word one clause apart — *"How do I know **this** is so? By **this**:"*. Now *"How do I know **it** is so?"*, which is also what the Source table's own gloss says, and *this* belongs to 此 alone.

**What the commentaries contribute, and what they do not.** 河上公 glosses ch 21 and ch 57 with the **identical five characters**, 此，今也 — independent evidence from the tradition that this is one fixed formula, which is the point §2 turns on. But he and 王弼 **disagree about what 此 points at**: 王弼 reads 此上之所云也 (*"'this' is what was said above"*), anaphora pointing back at the text; 河上公 reads it as *now*, deixis in time. Those are incompatible, and a bare *this* is the only English that leaves both standing. Full quotations in `notes/manuscript.md` → *What the commentators say 此 means*.

**The cost, accepted.** Ch 21 now ends the chapter on two syllables and a full stop. That thinness is the reading: the answer to the largest question in the book is a **gesture, not an explanation** — look at what is in front of you. Every word we were adding was an attempt to make a pointing finger say something.

**The thread continues at 故去彼取此** (ch 12, 38, 72), where the same 此 is opposed to 彼 (*bǐ* — that, yonder).

### Ch 57–58 · 正 / 奇 — one thread, and 其無正 ≠ "no limit"

Two linked calls. First, 其無正 (孰知其極？其無正) is "it has no fixed norm," *not* "no limit" — 極 (limit) is the prior clause; 正 here is the *normative / correct*, and it has to survive into the next line, whose subject is that same 正: 正復為奇 ("the straight turns crooked"). Render 正 as "limit" and the keyword vanishes. Second — the reason this is logged — 正 and 奇 must read the **same** in 57 and 58, because 58 is deliberately unmaking 57: there the ruler governs *with* 正 and wages war *with* 奇 (以正治國，以奇用兵), certain of the boundary; here 正復為奇 erases it. We thread them **straight / crooked** — 57's "govern with the straight" and "the people straighten themselves" (民自正), 58's "the straight turns crooked" — so the reader feels 58 pull 57 apart. (奇 keeps a little play — "surprise / the oblique" where 57 means battlefield tactics — but 正 holds as *straight / upright* throughout both.)

### Sweep · Ch 8, 20, 21, 31, 38 — the four locks 信, 精, 器, 眾

Four entries were written together (`xin-信.md`, `jing-精.md`, `qi-器.md`, `zhong-眾.md`) and each obliged changes in the verse. Logged together because the pattern matters more than the individual lines.

**眾 → the crowd.** The word had drifted into four Englishes: *all* (1), **dropped entirely** (8), *the masses* six times (20), *the many* (21). "The masses" is out — it imports a nineteenth-century class politics Laozi has no word for, and Ch 20's crowd is *merry at a spring festival*, not a proletariat. Ch 20's six lines now read *the crowd*, with agreement adjusted. Ch 31's 殺人之眾 becomes *"when many have been killed."*

**Ch 8 · 處眾人之所惡 was not translated at all.** The line had become *"It seeks the lowest places"* — which keeps the water and deletes the people the water is being measured against. 惡 (*è*) is *to find distasteful*, and the claim is comparative: water goes where **the crowd will not**. Now *"It dwells where the crowd will not go."* This is the most substantive change in the sweep, and it was invisible to the checker, which can only see renderings that are wrong, never ones that are missing.

**Ch 8 · 言善信 → "In speech, it is trustworthy"** *(was "In spoken words, it is sincerity")*. 信 is a **split tally** — a correspondence that can be checked — not an inner state. Sincerity is unfalsifiable; you can be sincerely unreliable.

**Ch 38 · 忠信之薄 → "the thinning of loyalty and trust"** *(was "the waning of integrity")*. Two characters had collapsed into one, and that one belonged to 德: 忠 (*zhōng* — loyalty) vanished, and 信 took 德's locked word for the second time in the book (Ch 23 was the first). 薄 (*bó*) is literally **thin**, which matters because the chapter closes on the same axis — 處其厚，不居其薄, *dwell in the thickness, not the thinness*. "Waning" broke a thread the chapter returns to.

**Ch 21 · 精 → "vital essence"** *(was "the primordial mass of creation")*. 精 is 米 (*mǐ* — rice) with *Shuowen*'s gloss **擇也**, to sift: **hulled grain**, what is left when the bulk is taken away. "Primordial mass" was the precise inversion — mass is the husk 精 is winnowed *from* — and it dated the text to the twentieth century. The following line's 其中有信 also surfaced properly: *"This essence is utterly real, and it can be trusted."*

**器 → vessel / tool / implement**, promoted out of 樸's `covers:` into its own entry. Nine chapters is too much reach for a footnote, and Ch 41's 大器 and Ch 67's 器長 use a **capacity** sense — what a person can hold — that 樸's entry had no room for. No verse changed: Ch 29 was fixed earlier in the session and the rest were already inside the lock.

**One thing this sweep taught, now recorded in `CLAUDE.md`.** A `forbidden:` rendering must be a word **no other character in those same chapters can legitimately claim.** "Integrity" cannot be forbidden for 信, because chapters 21, 23, 38 and 49 hold both 信 and 德. "Energy" cannot be forbidden for 精, because Ch 55 holds both 精 and 氣 and 氣 rightly takes *vital energy* there. The checker gates on presence of a character and cannot say *right for that one, wrong for this one, same chapter*. Those two distinctions are held by the entries and by the reader, not by the tool.

---

## Chapter notes

### Ch 7

#### 非以其無私邪？故能成其私 → "Is it not because they have no private self? / And so their private self is fulfilled"

*(restored 2026-08-12. The second line had no English at all.)*

Block 2 has four Chinese lines, and the fourth had been replaced rather than translated. 故能**成其私** is *therefore they can **complete their own***; the verse read *"The sage simply does what needs to be done"*, in which no character of the Chinese survives — nothing there means *need*, *do*, or *done*. And the third line had lost its question: 非…邪 is an explicit rhetorical frame, *is it not because…?*, which exists to set up the fourth line as its answer. Flattened to *"Free of selfish desires,"* it became a description, and the answer had nothing to answer.

**私 is the hinge and it appears twice** — 無私 then 成其私, emptied then fulfilled. The graph is 禾 (*hé* — standing grain) beside 厶 (*sī* — a self-enclosing curl): **grain held back for yourself**, the harvest withheld. One English word has to carry both halves or the paradox does not close. We use **private self** in both, which is also the wording of the 公 entry, where 私 is the counter-term (`glossary/gong-公.md`).

**This is the chapter's third self-negation, not its first.** 後其身而**身先** and 外其身而**身存** run the same move on 身 (*shēn* — a picture of a pregnant body, the physical person). So the stanza is three paradoxes in a row, and the last was missing.

**In the same pass: 身存 → "their selves endure"** *(was "their spirits endure")*. 身 is the body, and it is the same character rendered *themselves* one line above; *spirit* is the opposite register and it broke the 身 / 身 / 身 chain the couplet runs on.

### Ch 31

#### 吉事尚左，凶事尚右 → "Auspicious occasions honor the left; inauspicious occasions honor the right"

*(2026-08-12. Was: "Life-generating processes amplify creative energy. Life-negating processes invoke destruction.")*

**Four inventions in three lines.** *Processes* is the mechanistic overlay, and it turns a room of people observing a protocol into physics. 尚 (*shàng*) means only *to esteem, to place above* — nothing in the line says *amplify* or *invoke*. And the next line's *"the place of creation"* / *"the place of destruction"* are supplied outright: 偏將軍居左，上將軍居右 is simply *the secondary general stands left, the highest general stands right*.

Those glosses also buried the point. 吉事 and 凶事 are the Zhou ritual categories — 吉禮 (auspicious rites) and 凶禮 (rites of mourning) — and the chapter's shock is that **the more senior your command, the more you are seated as a mourner.** The text says so itself in the line that follows, 言以喪禮處之, *that is to say, they are placed by the rites of mourning*, which needed no help from us.

*(With this repaired, `"processes"` was added to 事's `forbidden:` list; see `glossary/shi-事.md`.)*

### Ch 14

#### 無物 → "no-thing," both times

*(was: "nothingness" and "no-image")*

**無物** (*wú wù* — "no-thing") occurs **twice in the whole book, both in this chapter**, and was rendered two different ways, neither of them right.

| Chinese | Was | Problem |
|---|---|---|
| 復歸於**無物** | "returns to nothingness" | "nothingness" is forbidden for 無 — it imports the Void as a substance where 無 is simply *absence* |
| **無物**之象 | "the image of no-image" | 物 is a **thing**, not an image — and 象 (*xiàng* — image) is already the other half of the phrase |

That second line rendered the couplet 無狀之狀，**無物**之象 as *"the shape of no-shape, the image of no-image."* The symmetry is seductive and it was built on a mistranslation: **the line got its parallelism by duplicating 象 and deleting 物.** Now *"the shape of no-shape, the image of no-thing"* — genuinely parallel in the way the Chinese is, 無X之X twice with **different** X's.

"No-thing" keeps 物 audible and keeps 無 as absence. *(Hyphenated deliberately: "no thing" open reads as an emphatic "not anything," where 無物 is a **state** the thing returns to.)*

#### 執古之道，以御今之有 → "Grasp the ancient Tao, and steer what is present now"

*(was: "to direct your present existence")*

Three repairs. **"Existence" is forbidden for 有** — 今之有 is *the presence of now*, what there currently is, not a person's lifetime. **"Your" was supplied**, and it shrank the line: the Chinese steers *what is*, not one's own affairs. And **御** (*yù*) is *to drive a chariot* — "steer" keeps the reins where "direct" is bloodless.

**A resonance across chapters, and the English now carries it.** 執 (*zhí* — to grasp) is the same character as Ch 29's 不可**執**也, *"it cannot be grasped."* Ch 29 forbids grasping **the world**; Ch 14 commands grasping **the ancient Tao**. That is deliberate: you cannot take the world into custody, so take the thread instead. **The line read *"Hold"* until 2026-09-08**, on the argument that *grasp the Tao* risks reading as *comprehend the Tao* — which this chapter spends fourteen lines denying is possible. Two facts overturned it. First, the collision that argument was registering is **in this chapter, not in the idiom**: 搏之不得 (*bó zhī bù dé*) read *"you cannot grasp it"* thirteen lines above, so 搏 (*bó* — to grope for and grip; 說文 索持也, *"to search out and grip"*) had taken 執's English inside 執's own page. That line now reads *"Reach, but you cannot **touch** it."* 得 (*dé* — to get) is the **generic completion verb** in this frame rather than a lexical *obtain*, and 河上公 (*Héshàng Gōng*) shows it: he uses 得 as a bare modal in the two lines above (不可**得**視而見之 / 不可**得**聽而聞之) and frames the whole triad by what is absent — 無**色**曰夷 · 無**聲**曰希 · 無**形**曰微. Colour, sound, form. Chinese has 見 and 聞 for the first two senses and nothing dedicated for the third, so it reaches for 得; English has *touch*. **Cost recorded:** 得 renders *get* at 13, 23, 31, 61 and *received* at 39, and this line departs. *Grasp* is 執's and stands in this chapter; *hold* is 持's. Second, ch 35's 執大象 was settled as **Grasp the great image** in Pass D, so keeping *Hold* here split one character across the two chapters that print the identical construction. See `glossary/zhi-執.md`.

### Ch 16

#### 王乃天，天乃道 → "the open sky"

*(not "nature," not bare "sky")*

Two decisions in one line. **First, it stays "sky."** Ch 16 and Ch 25 share this exact step — 王乃**天**，**天**乃道 (16) and 地法**天**，**天**法道 (25) — so rendering one "nature" and the other "sky" would hide from the reader that they are the same climb. The 天-family policy allows *nature* for 天 as an impersonal principle, but internal consistency outranks local fit; "reads better" is not a reason to break a lock.

**Second, the qualifier had to survive repetition.** The passage is *anadiplosis* — each line ends on the word the next begins with (容乃公，公乃王，王乃天，天乃道) — and the chain is the form. So a qualifier introduced once and dropped ("the all-covering sky… / The sky…") would break the link exactly where the poem holds itself together. **"The open sky"** repeats without thudding, stays an image rather than an abstraction, and carries both the vastness and the ownerlessness that make 天 the rung above 王: a king rules a domain, but the sky is over everything without preference (天無私覆).

#### 公 → "impartiality," not "equanimity"

公 is the direct opposite of 私 (*sī* — private, selfish): the public, the common, what belongs to no one. Equanimity is inner calm and sends rung two back inside the person, stalling an ascent whose whole motion is *outward*. With "impartiality," the ladder reads as one continuous widening of the circle beyond the self. *(See the Ch 16 Reading Note. This is the rendering Ch 42 and Ch 62 will have to answer to when 公 is given a glossary entry — see `WORKLIST.md`.)*

### Ch 21

#### 道之為物 → "Whatever the Tao is, it is only vague, only elusive"

*(was "In the manifest realm, the Tao appears intangible and dark", then briefly "As a thing, the Tao is…")*

Two things were wrong with the original. **"The manifest realm" imports a two-realm metaphysics** — a manifest world set against an unmanifest one — that the line does not contain and the book does not hold. And **"dark"** was doing duty for 惚, where the lock reserves *dark* for 玄.

The first repair rendered it *"As a thing, the Tao is…"*, which was accurate and badly built. 道之為物，惟恍惟惚 is **topic–comment**: the topic is *what the Tao amounts to as an entity*, the comment is *only indistinct*. "As a thing," as a sentence opener, is neither an English topic construction nor a plain subject, so it dangles — and modern colloquial English has given *"a thing"* a sense (*is that a thing?*) that actively interferes. **"Whatever the Tao is"** renders the topic directly and idiomatically.

**The witnesses confirm the topic and settle nothing else.** Both Mawangdui silks read 道之物 without 為, making 之 a plain possessive — *the Tao's thingness*. Same sense, no copula. Logged in the Manuscript Notes and in `sources/variants.yaml`.

*Cost, on the record:* **物 is lost here.** It returns four lines later in 其中有物 (*"within it there is a thing"*), so the Chinese has an echo the English no longer carries — the Tao is a 物 with a 物 inside it. Traded deliberately: the echo is a scholar's pleasure and the clarity is the reader's, and the chapter's force is in the reversal, which lands harder from a plain opening.

*And 惟…惟… → "only… only…" is a choice, not a translation.* 惟 can be restrictive (*only*) or a mere emphatic particle, in which case the line is simply *"indistinct and vague."* We keep "only" because the chapter needs **nothing but vagueness** for the "and yet" of the descent to pay off — but the restrictive force is ours.

#### The four-fold descent — restoring 其中有X, the chiasmus, and the anadiplosis

The middle of Chapter 21 is one continuous structure and the English had dissolved it into five unrelated observations. The Chinese:

> 道之為物，惟恍惟惚。
> 惚兮恍兮，其中有象；
> 恍兮惚兮，其中有物。
> 窈兮冥兮，其中有精；
> 其精甚真，其中有信。

**Three devices, all of them load-bearing.**

**The refrain.** 其中有X occurs **four times** — 象 (*xiàng* — image), 物 (*wù* — thing), 精 (*jīng* — vital essence), 信 (*xìn* — trust). One phrase, four objects, each more real than the last: a semblance, then something actual, then its concentrate, then the fact that it holds. The English had rendered the four as *"appear forms," "appear entities," "lies vital essence," "it can be trusted"* — four different constructions, so the descent read as a list of findings rather than one repeated act of looking deeper into the same place.

**The chiasmus.** 惚兮恍兮 and then 恍兮惚兮: the same two words, reversed. The preamble introduces them as 恍-惚, line three reverses that, line four reverses again. Rendering both as some version of "intangible and dark" flattened a deliberate turn. Now **"Elusive and vague"** then **"Vague and elusive."**

**The anadiplosis.** Line four ends on 精 and line five opens 其精 — the same hinge Ch 16's ladder runs on (公乃王，王乃天…), where each line begins on the word the last one ended with. Now *"…within it there is vital essence. / Its essence utterly real…"*

**And the nesting was wrong.** 其中 is "within **it**" — the Tao — in all four lines. The English read *"within these intangible, dark **forms** appear entities,"* making the forms a container for the entities and inventing a hierarchy the Chinese does not have. Everything is found in the same place, at four depths of attention.

**"Dark" is gone from this stanza.** It had been doing duty for 惚 (*hū*), where the lock reserves *dark* for 玄 (*xuán*). 恍 and 惚 are near-synonyms for *blurred, indistinct, hard to fix* — the pairing is the point — so they take **vague** and **elusive**, which can also reverse in English. *(This also keeps faith with Ch 14, where the same compound 惚恍 already reads "the elusive.")*

*Not carried over: 兮 (xī), the sighing exclamatory particle, four times. English has no unembarrassing equivalent, and the doubled adjectives carry the incantatory quality instead.*

*Worth noticing, and left in the reading notes rather than the verse: the darkest word in the stanza, 冥 (míng — dim, obscure), is a homophone of 明 (míng — clear-seeing), the book's word for sight that is unobstructed. The chapter finds the real thing at the bottom of the dim.*

#### 以閱眾甫 → "In this name, I observe the origin of the many"

*(was: "the unerasable source code of all creation")*

The old rendering carried our own besetting temptation, the **mechanistic** — and almost certainly inherited it from `process/legacy-tao-source-code.md`, whose framework is superseded. Three things were wrong with it.

**"Source code" adds what the Chinese refuses.** 眾甫 (*zhòng fǔ*) is *the origin of the many*: 甫 is a **seedling in a field**, borrowed early as a respectful word for a man and so *father / beginning / that from which things come*. Code is **written, by someone**, which reinstalls the author the chapter is at pains to leave out, and it **executes deterministically**, where a seedling unfolds. Both imports are exactly backwards.

**閱 (*yuè*) is *to observe*, not *to be*.** The old line said the Tao **is** the origin; the Chinese says the persisting name is what lets you **see** the origin. A different and much smaller claim, and the honest one. *(Heshang Gong dissents, glossing 閱 as 稟 — to bestow — so that the Tao confers on the many and the question becomes how one knows they receive 氣 from it. We decline: that reads a Han cosmology of qi-transmission back into the line, and the closing question is explicitly epistemic — 何以**知**.)*

**"It" and "this" had no antecedents.** 其名不去，以閱眾甫: the instrument of 以 (*yǐ* — thereby) is 其名, **the name** — Wang Bi confirms it (以無名說萬物始也, "it is by the nameless that the beginning of the countless things is explained"). Naming it in the English fixes the first pronoun. The second is fixed by repetition: **"In *this* name … By *this*"** gives 此 a visible antecedent for the first time. *Cost, on the record:* pointing 此 at the name narrows it — Wang Bi glosses 此 as 上之所云, "what was said above," meaning the whole descent through 象 / 物 / 精 / 信. **We accept the narrowing and let the bare demonstrative carry the width.** *(Revised 2026-08-30. The closing line formerly read "By this, here, now," and this paragraph argued that "here, now" widened the referent back out to the present encounter, so the line held both readings. It did not — it imported 河上公's gloss 此，今也 and picked his reading over Wang Bi's. See the cross-chapter note on 以此.)*

**And "the many," not "the countless things."** 眾 (*zhòng*) is not 萬物, and 萬物 does not occur in this chapter. Borrowing the 萬物 lock here would repeat the error just corrected in Ch 23, where 信 had been given 德's locked word. Elsewhere 眾 is rendered *all* (Ch 1's "the gate of all subtleties") and *the crowd* (Ch 20), so "the many" is in register. **"I," not "we,"** because the chapter's voice is 吾 (*wú* — the self *seeing*), which the next line makes explicit.

#### 吾何以知眾甫之狀哉 → "How do I know the origin of the many is so?"

*(was: "…the origin of the many?", with the contested word untranslated)*

The line's last content word is contested. Our base text reads **狀** (*zhuàng* — shape, form, condition); four older sources read **然** (*rán* — so, thus, that it is so). The English had rendered **neither**, asking simply "How do I know the origin of the many?" — which is why nothing had broken: the line was true under either reading, and silently so.

**We follow 然, and the decisive argument is not a manuscript one.** 狀 occurs **twice** in the whole book (here, and Ch 14's 無狀之狀, "the shape of no-shape"). 然 occurs **twelve** times. And 吾何以知…然哉？以此 is a **fixed closing formula**:

> Ch 54 · 吾何以知天下**然**哉？以此 — *"How do I know the world is so? By this."*
> Ch 57 · 吾何以知其**然**哉？以此 — *"How do I know it is so? By this:"*
> Ch 21 · 吾何以知眾甫之**然**哉？以此 — *"How do I know the origin of the many is so? By this."*

**然 completes the formula; 狀 breaks it.** Three chapters ask one question and answer it one way, and the English now lets a reader hear that.

**Then the witnesses, all agreeing:** both Mawangdui silks read 然; the Song Heshang Gong edition reads 然; and the Siku Quanshu compilers wrote a collation note on this very line — 〔案狀各本俱作然〕, *"as for 狀, all editions read 然."* Our 狀 may be close to unique.

**And the word is load-bearing elsewhere.** 然 is the second half of **自然** (*zìrán* — so of itself): 自 (*zì* — self) + 然 (*rán* — so). The character that closes these three questions is the one Laozi builds his term for *being as one is, of oneself* out of. So the question "how do I know it is **so**?" is asked in the vocabulary of self-so-ness, and answered 以此 — *by this*: by the thing in front of you, being what it is of its own accord. *(The English of 以此 was unified across all three chapters on 2026-08-30 — see the cross-chapter note above.)* *(See `glossary/ziran-自然.md` for 然's history — it began as a picture of roasting and was borrowed for its sound, so it is grammar rather than image.)*

**The base text is unchanged.** The Source table keeps 狀, and only the translation follows the older reading — the practice already established at Ch 41 (免成), Ch 42 (學父), Ch 47 (明) and Ch 53 (竽). `source/chinese.md` stays a faithful transcription of one recension rather than becoming a composite.

*Found because Shalom asked whether 然 was related to 自然. It is, and the relation is the argument.*

### Ch 22

*(2026-08-27. The whole chapter was revisited from the `WORKLIST.md` debt on 不自是. Five decisions, and the stanza that opened the debt turned out to be the third-largest problem in the chapter.)*

#### 抱一 → "embraces one thing"

*(was: "embraces the one." A **deliberate de-mystification**, and it is the reason this entry exists.)*

**The problem is not accuracy. It is that the accurate rendering now lies to a modern reader.** *"The sage embraces the one"* is a defensible English sentence, and in 2026 it reads as prophecy. **"The One" has become a chosen-one trope** — destiny, the anointed figure, the revealed secret. A reader meets the line and hears that something is being disclosed to them. 一 (*yī*) is a single horizontal stroke: the mark you make when you have counted to one. The Chinese is doing arithmetic.

**王弼 refuses the mystical reading outright**, in five characters: **一，少之極也** — *"the one is the extreme of 少 (*shǎo* — few, little)."* And he anchors it in the line directly above: 少則得，多則惑 — *little, then gain; much, then confusion.* If less is better, the least you can hold is one. 是以 (*shì yǐ* — **therefore**) welds the two, and Wang Bi is telling us the *therefore* is load-bearing.

河上公 keeps it equally functional: 抱，守也…聖人**守一**乃知萬事 — *"抱 means hold fast to… the sage holds fast to one and thereby knows the countless affairs."*

**So the fix was grammatical, not lexical.** The mysticism was never in the idea; it was in **the definite article**, which turns a count into a title. *One thing* answers 多 (*duō* — much) directly, which is the chapter's own sequence — 少 / 多 / 一. And 抱 (*bào*) stays **embrace**, per the lock that pairs it with 守 and forbids swapping them.

**The intent, stated plainly for the record:** we want a reader who can *act* on this line. **"Embrace one thing" is something a person can go and do. "Embrace the One" is an invitation to feel reverent** — and that substitution, awe in place of practice, is the exact overlay this edition exists to strip. The hymn test fails on sight. The pointing test decides it: Laozi could point at one thing; nobody can point at the One.

**Cost, on the record — this is a per-chapter call, not a lock.** 一 carries real cosmological weight at Ch 39 (昔之得一者, *"those of old who attained the one"*), Ch 14 (混而為一), and Ch 42 (道生一, *"the Tao gives birth to the one"* — which is also the book's own refutation of a capital-O One: whatever 一 is, it is **borne**). *One thing* would be wrong in all three. What licenses it here is that **Ch 22 is the only chapter where 一 sits inside an explicit few/much sequence with a *therefore* pointing at it.** Recorded so a future sweep reads it as a decision. Full argument in `glossary/yi-一.md`.

**Two rejected.** *"Embraces the undivided"* — defensible from the graph, but it collides with 樸 (*pǔ* — uncarved wood), which already holds the not-yet-divided slot; don't let 一 borrow it. *"Embraces oneness"* — an abstraction, and it fails the pointing test in the other direction.

#### 為天下式 → "sets a pattern for the world"

*(was: "sets the example for everyone." An intermediate draft read "serves as the world's pattern.")*

Two repairs. **天下** (*tiān xià*) is locked to **the world** and had become *everyone*. And **式** (*shì*) is not an *example* in the moral sense — it is 弋 (*yì* — a stake driven in) with **工 (*gōng* — a carpenter's square)**: a **form-giving instrument**, the template you cut everything else to. 王弼: 式猶**則**之也 (*"式 is like 則"* — and 則 is a rule inscribed on bronze). 河上公: **法式**也, a standard.

**Ch 28 settles the register in its own next line.** 為天下式，常德**不忒** — 忒 (*tè*) is **to deviate, to err off true**. You can only deviate *from a standard*, so 式 must be a measuring thing.

*"Serves as the world's pattern"* was rejected because modern *pattern* means either wallpaper or an observed regularity, neither of which is normative. **"Sets a pattern for the world"** keeps the word but the preposition does the normative work the possessive could not. *(Shalom's rewrite, and better than the draft it replaced.)*

*Owed: ch 28 carries 為天下式 twice, currently "Embody the pattern of the world," and should be brought into line. Logged in `WORKLIST.md`.*

#### The four 不自X lines are the four opening paradoxes restated

**王弼 maps stanza three onto stanza one, in order, one-to-one** — and no English rendering of this chapter had carried it:

| stanza 1 | 王弼's gloss | stanza 3 |
|---|---|---|
| 曲則全 (bent, then whole) | 不自見其明**則全**也 | 不自見，故明 |
| 枉則直 (bent, then straight) | 不自是**則其是彰**也 | 不自是，故彰 |
| 窪則盈 (hollow, then full) | 不自伐**則其功有**也 | 不自伐，故有功 |
| 敝則新 (worn, then new) | 不自矜**則其德長**也 | 不自矜，故長 |

The chapter is **one argument stated twice** — first as a paradox of form, then as conduct. And note Wang Bi's move on the second: 不自是則其**是**彰也 — he *repeats the character*. **What you refuse to claim is what comes to you.** The English now runs that shape through all four: *they do not X, and so X is theirs.*

#### 不自見，故明 → "they do not show themselves off, and so they see clearly"

*(was: "The sage does not display self, and is therefore luminous.")*

**The glossary had already decided this line and the manuscript never heard.** `glossary/ming-明.md` uses this very phrase as its own worked example — *"不自見，故明 (22) — they do not display themselves, therefore they **see clearly**"* — and its register table lists 不自見，故明 under *sees clearly*. The entry was right; the verse was stale against it. `concordance.py --english "luminous"` returned exactly one line in the whole book: this one, backed by no locked term.

**明 is reception, not emission** — moonlight through a window. *Luminous* makes the sage a light source, the precise reading the lock exists to refuse. And 河上公 makes the case unanswerably: 聖人**不以其目視**千里之外也，乃**因天下之目以視**，故能明達也 — *"the sage does not see a thousand li with their own eyes; they see **by means of the world's eyes**."*

**The other three in the same pass.** 不自是 → *"they do not insist they are right"* — 是 (*shì*) is *to affirm as right*, and 河上公 gives the full shape: 不自以為是**而非人**, *"does not take themselves right **and others wrong**."* The previous *"does not debate"* borrowed the English belonging to 辯 (*biàn*), which does not occur in this chapter. 彰 (*zhāng*) → *their rightness shows* (was *"unrivaled,"* which imports a comparison); 彰 is 章 (a pattern) with 彡 (strokes), **to show up plainly**. 不自伐 → *"they do not claim the work"* — 河上公 glosses flatly 伐，**取**也, *"伐 means to take,"* so this is claiming credit, not boasting. 不自矜 → *"they do not make themselves great"* — 矜，**大**也, and 聖人不自貴大.

*Wang Bi adds 德 to the last one (其德長也 — their **integrity** endures). Left in the notes rather than the verse, since the Chinese does not say 德.*

#### 誠全而歸之 → "These words hold. Return to them. Stay whole."

*(was: "Try and see for yourself" — which is not a translation of anything. Two intermediate drafts were rejected on Shalom's objections; both failures are recorded below, because each was detecting something real.)*

**The largest error in the chapter, and it was invisible to every checker**, because a line that renders nothing violates no lock. 誠 (*chéng* — genuinely; the 言 + 成 *word-carried-to-completion* decomposed at ch 81), 全 (*quán* — whole), 而 (*ér* — and), 歸之 (*guī zhī* — return to it). The old line dropped **全**, which is the word the chapter opens on (曲則**全**) and quotes back verbatim two lines earlier (古之所謂「曲則全」者).

**That quote-back forced the opening line too.** 曲則全 had read *"Yield and remain unbroken,"* which loses both 曲 (*qū* — bent) and 全 (*quán* — whole); it is now **"Bend, and stay whole,"** so the closing line has something to land on.

**誠 answers 虛言, and the pair is a chime no English had carried.** 豈**虛言**哉！**誠**全而歸之 — 虛言 (*xū yán* — **empty words**) answered by 誠, which is 言 (*yán* — words) + 成 (*chéng* — to complete): **words carried through to completion.** The question asks whether the saying is hollow talk; the answer is the character for talk that is *made good*. Hence **"These words hold"** rather than a bare adverbial *in truth* — 誠 is doing two jobs, and *in truth* does only one.

**"These," not "those."** 古之所謂 (*gǔ zhī suǒ wèi* — "what the ancients called") does mark distance, but the saying has just been quoted verbatim in the line above: the words are on the page. And it is the book's own deixis — **以此** (*yǐ cǐ* — "by this") closes chapters 21, 54 and 57. Laozi points **near**. *Those words* files the teaching under *the ancients, long ago*; the line exists to collapse exactly that distance. *(Shalom's change.)*

**全 is preservation, not repair — and two drafts failed on this before it was named.** A first pass read *"In truth, this makes you whole,"* and Shalom objected: if the chapter's opening line is *bend and stay whole*, nothing should need to make you whole afterwards. He was right, and 河上公 proves it — his gloss on 曲則全 is 曲己從眾，不自專，則**全其身**也, *"bend yourself and follow the crowd, do not act on your own authority, then you **keep your body whole**."* **全 there is a transitive verb meaning *keep intact*.** The chapter is about not getting broken in the first place.

*His own proposed fix, "this restores your wholeness," was declined for the same reason and it is worth recording why: **to restore is to bring back to a former condition, so it presupposes the loss.** It is "make whole" with better manners. If 全 is preservation, no repair verb of any kind fits — and the error had simply migrated from 全 onto 歸.*

**歸 → "return," and the person is the one who moves.** Everywhere else in this book 歸 is intransitive and self-directed, with the destination always the original state: 各復**歸**其根 and **歸**根曰靜 (16), 復**歸**於無物 (14), 復**歸**於嬰兒 / 於樸 (28), 萬物**歸**焉 (34). *Restores your wholeness* would make wholeness an object handed to you by an outside agent; 歸 makes **you** the one who goes home. **"Return" is also already the manuscript's word for 歸 in seven chapters** (14, 16, 25, 28, 34, 40, 52), so anything else here would have made ch 22 the outlier — and it puts the line inside ch 40's 反者道之動, *"Returning is the Tao's movement."*

*A drafted "come home" was rejected on a point worth keeping: **English "come" encodes speaker-position** — toward where the speaker stands — which quietly installs a narrator waiting at home. 歸 has no such deixis, so "return" is the neutral verb and the one already in use.*

#### 之 → "them" — and *home* refused on principle

*(Shalom's call, 2026-08-28, reversing a rendering he had adopted two hours earlier. **This is the decision that produced `DISCOVERIES.md` §5**, and the general principle is stated there.)*

**"Return home" was drafted, accepted, and then withdrawn — not because it was wrong, but because it was right in the wrong place.** 歸 genuinely carries homecoming: the graph turns on going where one belongs, and every destination this book gives the verb is the original state — 根 (*gēn* — root, ch 16), 樸 (*pǔ* — the uncarved, ch 28), 嬰兒 (*yīng ér* — the infant, ch 28), 無物 (*wú wù* — no-thing, ch 14). Homecoming is the deep sense of the line and we are not claiming otherwise.

**But no word in the line means *home*.** The object is 之 (*zhī* — it), and the strongest grammatical reading is the nearest topic: 古之所謂「曲則全」者, the ancient saying, quoted verbatim one line above. So **之 → "them," the words**, and the chapter closes in a circle, back on the line it opened with.

**Shalom's reason, and it is the point:** *"Even if the words point to 'home' as the deeper meaning, I don't want to supply that for the reader — rather allow them to find this themselves."* The verse delivers the text; the depth is the reader's to arrive at. **The log and the companion volume are where the homecoming gets said.** That is what the apparatus is for, and it is why this repository can afford a restraint an unannotated translation could not.

*Practical benefit, secondary but real: the borrowing disappears. "Home" would have shown as unbacked under `concordance.py --english "home"` — the same class as* heard *at ch 81. "Them" is simply 之.*

#### The clause order is reversed, deliberately

*(Shalom, 2026-08-28. The Chinese runs 全 then 歸; the English runs return then whole.)*

**The line has to prove something, and only one order proves it.** It answers 豈虛言哉 (*"how could those be empty words!"*), so it must show the saying working. *"Return to them, and stay whole"* makes the saying the **instrument** of wholeness — come back to this, and it keeps you whole. *"Stay whole, and return to them"* leaves the causal relation murky and demotes the returning to an afterthought, so the proof never lands.

**And it restores the chapter's own grammar of consequence.** Every line of the opening stanza is built on 則 (*zé* — then, thus): 曲**則**全, 枉**則**直, 窪**則**盈, 敝**則**新. **Wholeness is the outcome in all four, never the precondition.** Bend → whole. Putting 全 first in English inverted a shape the chapter states four times in its first three lines.

It also brackets the chapter on its keyword: it opens *"Bend, and stay whole"* and now closes on *whole*. 全 occurs three times in ch 22 and **nowhere else in the book**.

**Cost, on the record.** 誠**全**而**歸之** puts 全 first, and 歸之 are the final two characters of the chapter — so the source ends on the returning and our line ends on the wholeness. 而 (*ér*) is a neutral conjunction rather than a sequencer, so no grammar is broken, but the stress moves. 河上公 also reads the source order (實其肌體，**歸之**於父母 — *keep the body intact, then hand it back*); we have already declined his referent, and here we decline his sequence too.

*One flag kept visible: "return to them" carries a faint devotional pull in English — **return to the Word**. It is checked by 古之所謂 (what the ancients **called** it), which frames the line as an old proverb rather than revelation, and by* them *pointing at a saying quoted two lines above. Judged to pass the hymn test, but by a smaller margin than the alternative.*

#### 而 goes unmarked — three sentences, not one

*(Shalom, 2026-08-28. Was: "Return to them, and stay whole.")*

**The conjunction was echoing the proverb it had just quoted.** With *and*, lines 23 and 24 ran *"bend, **and stay whole**"* immediately followed by *"Return to them, **and stay whole**"* — the same frame twice, back to back, one line after the quotation marks closed. Read aloud it is a stammer, not a bracket.

**而 (*ér*) is the lightest connector available and can go unmarked.** Line 11's 曲**則**全 uses 則 (*zé* — then, thus), genuinely consequential, and it earns its *", and."* 而 is plain coordination. If either link is to lose its English marker, it is this one — and the Chinese has no punctuation at all, so the marks here are ours by the standing principle above.

**The causal reading survives the cut, because "These words hold" carries it.** Three beats now stage the argument rather than asserting it: *the words are reliable* → *act on them* → *you stay whole*. The instrumentality that justified reversing the clause order is intact; it has moved from a conjunction into the sequence.

*No typographic objection: lines 11, 12 and 13 are each two sentences. Three in the closing line is a variation inside the chapter's own idiom.*

**Why 之 was resolved at all, rather than left as "it."** An intermediate draft read *"Stay whole, and return to it,"* and Shalom asked what *it* referred to — the words, or wholeness. The answer is that **classical Chinese can leave a referent floating in a way English cannot.** 之 is a light particle that does not demand resolution; English *it*, arriving after two live candidates, actively misdirects. This is the same principle already governing em-dashes and stranded subjects in the Standing principles above: *name it and end the sentence*. The Chinese is not vague there; the English was.

**The candidates for 之, and what was declined.** Grammatically the strongest is **the saying** — 古之所謂「曲則全」者 is the topic of the sentence immediately before — which would give *"come back to them."* Accurate, and flat: it can read as *reread this*. **Wholeness** is near-tautological, since 全 stands in the same clause. And 河上公 reads it as **the body returned to one's parents** — 實其肌體，歸之於父母，無有傷害也 — which is 身體髮膚，受之父母 from the *Xiaojing*, a **Han Confucian filial import** he has to supply 於父母 to make, since the text does not say it. Declined on that ground. *Return home* holds the root, wholeness, and the teaching at once without choosing among them, which is the openness the Chinese actually has.

### Ch 23

#### 信不足焉，有不信焉 → "Where trust runs short, there is no trust" — ch 17 and ch 23 alike

*(**Resolved 2026-08-30, Pass C, `WORKLIST.md` T2-14.** This section previously argued for a deliberate divergence and was marked "⟡ Flagged for the editing pass." This is that pass, and **the divergence does not survive it.** Ch 17 read *"When leaders don't trust the people, no one trusts the leaders"*; ch 23 read *"Where trust is withheld, trust is withheld in return."* Both are gone, and ch 23's `lock-ok` waiver with them. What the split got right is kept below.)*

The seven characters 信不足焉，有不信焉 (*xìn bù zú yān, yǒu bù xìn yān* — "trust is not sufficient; there is untrust") close both ch 17 and ch 23, verbatim. **Both chapters now read: "Where trust runs short, there is no trust."**

**The old argument was that the two chapters put the line in different mouths** — ch 17 being about rulers (太上 *tài shàng*, the highest; 其次 *qí cì*, the next) and so licensing *leaders* and *the people* as restored subjects, while ch 23 is about 同 (*tóng* — merging) and would be narrowed by a political frame. **The commentators cross that split in both directions, which is what undid it.**

- **王弼 (*Wáng Bì*) reads it at ch 17 — the political chapter — as impersonal natural law:** 夫御體失性則疾病生，輔物失真則疵釁作。信不足焉，則有不信，**此自然之道也**。已處不足，非智之所齊也 — *"govern the body and lose its nature, and sickness arises; assist a thing and lose its truth, and flaws and cracks appear. Where trust is insufficient, there is untrust. **This is the way of things being so of themselves.** Once one stands in insufficiency, it is not something cleverness can set right."*
- **河上公 (*Héshàng Gōng*) supplies a ruler at ch 23 — the non-political chapter:** 君信不足於下，下則應君以不足也 — *"the ruler's trustworthiness is insufficient toward those below, and those below answer the ruler with insufficiency."*

Each frame appears in the chapter that was said to exclude it, so **context cannot license two Englishes.**

**Ch 17's line was also wrong in a way the mismatch hid: the arrow ran backwards.** 信 is not an attitude the ruler holds. `glossary/xin-信.md` locks it as a **符契** (*fú qì* — a split tally, a token broken in two so the halves can be matched later): *a correspondence that can be checked*, not a warm inner disposition. 河上公 on ch 17: 君信不足**於下**，下則應之以不信而**欺其君**也 — *"the ruler's trustworthiness is insufficient **toward** those below; those below respond with untrust and **deceive** their ruler."* **The deceiving mirrors a ruler who could not be relied on, not a ruler who was suspicious.**

**Both old versions asserted reciprocity, and 王弼's reading is not reciprocal.** *"In return"* and *"no one trusts the leaders"* both require a second party giving something back. 王弼's shape is **emergence**: his analogy is disease arising in a body whose nature has been violated — nothing is returned, the deficiency simply produces its own consequence. The English is now agent-free and holds both readings, per the standing principle that where the commentators diverge the English must not settle it.

**What the line is doing in ch 23, settled by 河上公's second gloss there** — and it is not an appendix: 此言物相歸，**同聲相應**，雲從龍，風從虎，水流濕，火就燥，自然之道也 — *"this says that things return to their kind, that **like sounds answer each other**: clouds follow the dragon, wind follows the tiger, water flows to the damp, fire goes to the dry — this is the way of being so of itself."* That is the 易經 (*Yìjīng* — Book of Changes) formula for resonance, which makes the 信 line **the fourth term of ch 23's 同 series** — 同於道者，道亦樂得之 (*"those who merge with the Tao, the Tao gladly receives them"*), then 德 (*dé* — integrity), then 失 (*shī* — loss), then trust. Like joins like.

**The English, word by word.** 信 → *trust* twice, because the Chinese uses 信 twice (信不足 / 不信) — both old versions had that instinct right. 不足 → *runs short*: 足 (*zú*) is *enough* at ch 44 and 46's 知足 (*zhī zú* — "know when you have enough"), and `glossary/xin-信.md` already glosses ch 63's 寡信 as *"run short on trust."* 有 → *there is*. The doubled final particle 焉 (*yān* — there, therein) is mirrored by *"Where… there is."*

**The near-tautology is the argument, not a defect.** A shortfall of trust does not stay partial; it goes to zero. There is no slightly-healthy body in 王弼's analogy either.

**What the earlier correction got right, and is kept.** Before the divergence was written, ch 23's line read *"When integrity is weak, the system winds down,"* which was wrong twice. **信 is not 德**: 信 is 人 (*rén* — a person) beside 言 (*yán* — speech), a person standing by their word, and rendering it *integrity* borrows 德's locked word three lines after the chapter has used 德 explicitly (德者同於德), collapsing a deliberate change of subject. And **"the system winds down" is not in the text** — 有不信焉 is a closed loop, where *winds down* is entropy, something losing energy on its own rather than producing its own answer.

### Ch 25

*(revised 2026-08-20 — three decisions in one pass, each of which uncovered the next. The passage remains open pending Guodian; see the note at the foot.)*

#### 天下母 → "the mother of the world"

*(was: "the mother of creation")*

可以為天下母. **天下** (*tiān xià* — under-sky) is locked to **the world**, and the previous rendering deleted the locked term in favour of **creation** — a word `glossary/tiandi-天地.md` sets aside outright: *it implies a creator, and this cosmos was borne, not made.* In a chapter whose opening line is 先天地生 (*born before sky and earth*), installing a creation is the precise overlay the 天-family policy exists to prevent.

Now consistent with Ch 52, which renders 以為天下母 as *"which serves as the mother of the world."*

**Worth recording as a checker gap, not just a fix.** `check_locks.py` keys off the Chinese to judge the English, so it fires when a *wrong* word is present. It cannot fire on a **locked word that is absent** — a rendering that simply deletes 天下 passes every rule silently. Same class of blind spot as the empty `## Translation` blocks found in Ch 20 and Ch 65: the tools cannot see what is not there. A candidate rule for `PLAN.md`.

#### 人 → "humans are also vast" / "one of them is human"

*(was: "the aligned human," in both lines. Supersedes the entry written when the throne was first removed.)*

**⚠ The manuscript grounds collapsed the same day this entry was written, and the reading survives on other grounds.** It is not true that the silks read 人. **Every excavated witness reads 王** (*wáng* — king) — Guodian (~300 BCE), both Mawangdui silks, the Beida Han slips. 人 is a *transmitted* reading: 傅奕 (Tang) for the first line, 范應元 (Song) for the second. We follow it because **the received text contradicts itself** — the next line is 人法地, "humans follow earth" — an internal argument Fan Yingyuan and 奚侗 both made long before the excavations, and one the excavations do not touch. Full apparatus, and the honest account of how the error entered, in the Manuscript Notes.

**This does not disturb the English.** 王 is not gendered in Chinese and `glossary/wang-王.md` renders it *ruler / sovereign* in all eight chapters, never *king*. Even reading 王 here, the line would not have produced a throne.

**What changed: "aligned" is gone.** Nothing in the Chinese licenses it. 人 is simply *human*, and the qualifier was deciding **which** humans are among the four vast things — doing in miniature what the throne did in full. It was ours, not the text's, and it has been deleted.

**Then the real difficulty surfaced, and it is not solvable by word choice.** Three of the four items are **definite singular uniques** — there is one Tao, one sky, one earth. The fourth is a **class term**. English "the human" tries to make it a unique too and lands in taxonomic register (*the human, the domestic cat*): a specimen, not us. "Humans are one of them" fails the other way, on number agreement.

**The asymmetry is in the Chinese and cannot be dissolved, so it should not be disguised.** 人 is deliberately the odd item — the one category in the list that contains the reader.

The solution is to change grammatical strategy between the two lines. The list line takes the natural English **plural** (*humans are also vast*); the count line makes 人 a **predicate** rather than a counted item (*one of them is human*), so nothing has to agree in number. It also puts **human** in final stressed position — the slot the received text gave the king, and the last word before the ladder begins.

This also settles the passage internally: the ladder three lines down already reads *"Humans model themselves on the earth"* (人法地), which is the very line the received text contradicts. Nothing in the passage now argues with it.

**Cost, on the record: 居 flattens to "is."** 居 (*jū*) is properly *to dwell, to occupy a position*. Both commentaries read it here as rank rather than residence — Wang Bi glosses 而王居其一焉 as 處人主之大也 (*"occupies* [處 *chǔ*] *the greatness of the lord of people"*), and Heshang Gong's edition carries the note 居一作處, *"居 is written 處 in one edition."* A verb of position, close to a copula. The loss is small and the gain in the line is large.

**而 is kept as "and."** A draft dropped it for compression; Shalom restored it. It is in the Chinese — 而人居其一焉.

**Correction to the earlier version of this entry**, which offered the three-strokes reading of 王 (sky, human, earth joined by one vertical) as a co-equal etymology. It is not one. That reading is **董仲舒** (*Dǒng Zhòngshū*, c. 179–104 BCE), roughly fourteen centuries younger than the graph, and it entered the dictionaries through the *Shuowen*. The graph is an axe. See `glossary/wang-王.md` and `DISCOVERIES.md` §4.

#### 域中 → "Within all bounds"

*(was: "Within the realm"; before that, "Within this system of four vast things")*

**域** (*yù*) is a **bounded stretch of ground**. The older graph underneath it is 或 (*huò*) — a dagger-axe 戈 (*gē*) standing over a walled enclosure 囗 (*wéi*) on a line — and the *Shuowen Jiezi* reads it 或，邦也。从口从戈以守一。一，地也 (*"或 is a state; 囗 and 戈, guarding 一; 一 is the ground"*). 或 was then borrowed for its sound to mean *or*, and the territorial sense was rebuilt twice: **域** with soil under it, **國** (*guó*) with a wall around it. 域 occurs **exactly once in all 81 chapters**, here.

That fact resolves the witness fork rather than deepening it. **Both silks read 國中有四大** where the base reads 域中. These are not two words but **one root with two classifiers**, which is why `sources/variants.yaml` logs the fork as non-meaning-bearing. Whichever is written, the word means *bounded territory*.

**Why "realm" had to go, and it is our own besetting error.** A realm is **what a king rules**. Having taken 王 out of the line, the container word put the throne back one word to the left — in the English only, with nothing in the Chinese asking for it. That is `DISCOVERIES.md` §4's third installation, committed by us, in the same sentence from which we had just removed the fourth.

**Why Laozi could not have used 天下 here, and why the choice looks deliberate.** 天下 means *under-sky*: it is defined by lying beneath 天. This sentence **counts 天 as one of the four vast things**, and it must also hold the Tao, which the same chapter calls 先天地生 (*born before sky and earth*). A container named *the part underneath the sky* excludes two of the four items by construction. And the proof it is deliberate stands three lines earlier in this very chapter — 可以為天下母. He has 天下 in hand, uses it for what the Tao mothers, then **switches** the moment he needs a container wide enough to hold the sky. Two container words, one chapter, doing two jobs. That is about as strong an argument for intent as this text ever offers.

**The commentaries split here, and we follow Heshang Gong.** He reads 域 concretely — 八極之内有四大, *"within the eight extremities there are four vast things"*: a place, out to the horizon. **Wang Bi reads it as the un-nameable** — 無稱不可得而名曰域也…道天地王皆在乎無稱之内, *"what has no designation cannot be named; we call it 域. The Tao, sky, earth and the ruler are all inside the un-designated."*

**We reject Wang Bi's reading, on this chapter's own last line.** His gloss puts a container **around** the Tao — something the Tao is merely one item within. That is the identical inversion this edition refuses in 道法自然 (*dào fǎ zìrán*), where "the Tao follows Nature" installs a higher thing. He is solving a puzzle the chapter does not pose, and paying for it with the cosmology. He is also visibly uncomfortable, which is itself the tell: 國 is a *state* word, and the oldest witnesses put the four vast things inside a walled political territory. The territorial frame is older than the throne — a separate finding, and a live one.

**"Within the bounds of this world" — drafted and rejected the same day.** The demonstrative was reaching for something right: pointing is this book's own epistemic move, 以此 (*yǐ cǐ* — *by this*), the answer Chapters 21, 54 and 57 all give. But **"this world" in English carries a built-in opposite — the next one** (*not of this world*, John 18:36). 域 has an **edge, not an elsewhere**. And it collided: with 天下母 now correctly rendered *the world*, the word *world* would have done two different jobs eight words apart, erasing on the page the very distinction that justified the word choice. An earlier pass on this line had already recorded that 域中 carries **no demonstrative**.

**Cost, on the record:** *all bounds* is slightly strange English, and it drops the **ground** that 土 puts under 域. Accepted for now, and the frame may reopen.

#### Open — this passage is not settled

`sources/variants.yaml` records **Mawangdui only** for Chapter 25, and `concordance.py --witnesses 25` flags it: Guodian (~300 BCE, bundle A) **carries this chapter and has never been checked at the four greats.** `DISCOVERIES.md` §1 rests on the claim that the oldest witnesses read 人. Until Guodian is recorded, that claim is supported by the silks alone, and 域/國, 王/人, and the whole container frame stay open.


### Ch 27

#### 救 → "rescue", never "drawing in" — and the couplet's lost axis

*(2026-08-12, prompted by the Ch 62 retrofit. The line had read "masterful at drawing in people, ensures that no one is lost.")*

**The couplet had no axis.** 常善**救**人，故無**棄**人 turns on a pair of opposites: 救 (*jiù* — **rescue**) and 棄 (*qì* — **abandon**). The 故 (*gù* — "therefore") only does work because they pull against each other — *always masterful at rescuing, therefore no one is abandoned.* The English had paired *"drawing in"* with *"lost"*, which are not opposites and not even on one axis, so the "therefore" joined two unrelated observations.

**救 is not "drawing in."** The graph is 求 (*qiú* — to seek, to beg) beside 攴 (*pū* — a hand holding a stick, the action radical): intervening to pull someone out of trouble. Both commentators are explicit — Heshang Gong on 常善救物: 聖人所以教民順四時，以**救**萬物之殘傷, *"the sage teaches the people to follow the four seasons, in order to **rescue** the countless things from injury and mutilation"*; and on 常善救人: 欲以**救**人在命, *"wishing thereby to save people's lives."*

**"Rescue" and not "save," deliberately.** *Save* is the obvious English and it fails the hymn test outright — *"the sage is always good at saving people"* belongs in a sermon, and 救 has no soteriology in it. *Rescue* keeps the physical act. **This is also simply the house word already:** Ch 52 renders 終身不救 as *"your life is beyond saving"* — Ch 27 was the outlier, not the precedent. 救 also stands at Ch 67 (天將救之), still undrafted, which should follow.

#### 物 → "things", never "entities"

*"Entities"* occurred **exactly once in all 81 chapters of verse** — this line — and was tied to no locked term. 物 (*wù*) is a mottled ox: things, kinds, stuff. Heshang Gong's gloss settles the register: 聖人不賤石而貴玉，視之如一, *"the sage does not despise stone and prize jade; he sees them as one."* Stones and jade, not entities. The 萬物 lock forbids *"beings"* for the same reason — see `glossary/wanwu-萬物.md` — and *entities* is that abstraction in a lab coat.

#### 襲明 → "inherited clarity", not "innate clarity"

`glossary/ming-明.md` had already ruled this: 襲明 → **"inherited clarity."** The verse said *innate*, which claims the opposite about where it comes from — 襲 (*xí*) is to inherit, to receive in succession, to put on in layers. *Innate* says it was born in you; *inherited* says it was handed to you. The glossary decided; the verse had not been told.

#### 常 restored

常 (*cháng* — always) had been dropped from both halves. It is the word that makes this a standing disposition rather than an occasion, and it is why the sage's rescuing is the *reason* nobody ends up discarded.

**Retrofit closed.** This was the debt opened when Ch 62 settled 棄 → *abandon*; `WORKLIST.md` can drop it. The wider point is logged as a Thread in `notes/reading.md`: Wang Bi glosses this very line with 不造進向以殊**棄不肖** — *"does not create tracks of advancement that single out and discard **the unfit**"* — and 不肖 is Ch 62's 不善人.

### Ch 29

#### 天下神器 → "the world is a sacred vessel"

*(was: "a sacred system")*

**器** (*qì*) is a **vessel**, and it is already locked that way inside `glossary/pu-樸.md` (`covers: 器 → vessel / tool`). It holds everywhere else in the book: Ch 11's clay worked into 器, Ch 28's 樸散則為器 ("when the uncarved wood is carved, it is made into tools"), Ch 31's 不祥之器 (weapons, "instruments of ill omen"), Ch 36's 國之利器 ("the sharp instruments of the state"). Ch 29 was the sole outlier, and "system" was the mechanistic overlay this edition exists to strip.

**The vessel is also what makes the rest of the chapter work.** The next clause is 不可**執**也 — "it cannot be **grasped**" — and then 執者失之, "those who grasp it lose it." You grasp at a vessel and break it. You do not grasp a system. The image and the warning are one gesture, and "system" severed them. *(This was already right in the notes: the Ch 48 entry cites Ch 29's 神器 as "a sacred vessel" — the reasoning was settled and only the verse had drifted. Found by `tools/check_locks.py`.)*

**執 was also rendered two ways, two lines apart** — "controlled," then "grasp." The Chinese is a tight chiasmus, 不可為也，不可執也 · 為者敗之，執者失之, and it only lands if 為 and 執 each keep one English word. Now: *"It cannot be forced. It cannot be grasped. / Those who force it ruin it. Those who grasp it lose it."* Four beats for four. "Controlled" also lost the hand — 執 is a graph of a hand seizing.

**And "try to" is gone from 為者/執者.** The Chinese says *those who do it*, not *those who attempt it*. The attempt is not the failure; the doing is.

*Left alone: the em-dash in this chapter's first line is one of the defensible ones — both clauses carry named subjects ("Those who wish…" / "I see…"), so it strands nothing. Noted so a later em-dash sweep does not remove it reflexively.*

*Still open here, not fixed: 取 (qǔ — seize) has vanished from 將欲取天下而為之, where "force their will upon the world" merges 取 and 為 into a single gesture. The Ch 48 entry makes much of 取's severed-ear violence, so 取天下 across Ch 29 / 48 / 57 may want one consistent treatment.*

### Ch 40

#### 弱者道之用 → "Yielding is the Tao's use"

*(was: "the Tao's function")*

"Function" was the mechanistic overlay twice over: **用** (*yòng*) is locked to **use** inside `glossary/wu-you-無有.md` (`covers: 用 → use`), and "function as" is on 為's forbidden list. **"Use" is simply the lock applied.**

It also repairs the couplet. Ch 40 is the shortest chapter in the book and is built entirely of parallels: 反者道之**動** / 弱者道之**用** — returning is the Tao's **動** (*dòng* — movement), yielding is its **用**. 動 and 用 are a matched pair, *how it moves* and *how it works*. "Movement" is concrete and observable where "function" is abstract and mechanical, and the mismatch broke the one structure the chapter has.

**And it restores a link to Ch 11**, which renders 有器之用 and 有室之用 as *"A clay vessel becomes useful"* and *"A room becomes useful."* Both chapters make one argument: **usefulness comes from what is hollow or yields.** Rendering 用 as "function" here and "useful" there hid it.

*A note on the genitive, which is deliberately left double.* "The Tao's use" can be read as *how the Tao operates* or as *how the Tao is put to use*. 道之用 carries both and classical Chinese does not disambiguate, so the English should not either. (Rejected: "working" — accurate to 用's sense of efficacy, but in modern ears it reads as employment, a job of work.)

### Ch 48

#### 取天下 → "the world comes to you"

*(not "win" or "take the world")*

The literal 取 is *seize / take* — its graph is a hand (又) gripping an ear (耳), the severed left ear of a slain enemy, counted on the battlefield for reward. It is the most grasping word in the language. But Laozi *subverts* it: the world is a 神器, a sacred vessel that 不可執 — "cannot be grasped" — and 執者失之, "whoever grasps it loses it" (Ch 29). The conqueror's verb names precisely the thing that fails.

- We rejected **"win"** because it imports *competition and victory*, the very thing Laozi renounces (不爭, non-contention). "Win the world" sounds hard-fought; the teaching is that you come to it by *not* fighting for it.
- We chose the receptive reframe — **"the world comes to you"** — because it says aloud what 取天下 only implies: the non-grasping ruler is one the world *gravitates toward* (cf. 天下往, "the world goes to him," Ch 35; 天下樂推, "the world delights to carry him forward," Ch 66), not one who seizes it.
- The failure-clause 及其有事 (literally "once there are affairs / once one meddles") we render **"the moment you grab at it, it slips away,"** letting "grab" carry the 取/執 grasping-image and echo 執者失之.

Net: fidelity to the *word* traded for fidelity to the *teaching*. A conscious choice, logged here.

### Ch 48

#### The closing stanza was drafted twice, and the superseded draft was kept

*(repaired 2026-08-12)*

Block 2 carries **two** lines of Chinese — 取天下常以無事 and 及其有事，不足以取天下 — and the English rendered them **four** times: the logged reading, then a second, more literal pass that had lost its subject (*"always won by non-interference."*) and used *"win the world,"* the exact word the 取天下 entry above argues against. The second stanza was dead draft. It is deleted, not repaired.

#### 取天下常以無事 → "The world always comes to you by not meddling with it"

The couplet is **framed and pivoted**, and the English had kept neither. 取天下 opens it and closes it; between those, one character flips — **無事 → 有事**, absence of undertaking to presence of it, built on the 無/有 pair this edition locks as *absence / presence*.

The old second line rendered 有事 as *"you grab at it."* Grabbing is 執 (*zhí*), a hand seizing — Chapter 29's word, and not in this chapter. **有事 is milder and more insidious: having a project.** Wang Bi glosses it 自已造也, *"manufactured by oneself"*; Heshang Gong, 好有事，則政教煩, *"fond of having undertakings, and governance turns troublesome."* Officiousness, not violence.

Now: *"The world always comes to you by not meddling with it. / The moment you meddle, it stops coming."* 常 (*cháng* — always) returns; 取天下 frames it twice as *comes to you* / *stops coming*, keeping the logged decision that 取 is reception and not conquest; and 無事/有事 becomes one English word negated and then affirmed, so the line turns on a hinge instead of drifting.

**Still open here:** 取天下 reads *"comes to you"* in this chapter and *"win the world"* in Ch 57, which the Ch 29 note already flagged as wanting one treatment across 29 / 48 / 57. Not addressed.

### Ch 57

#### 無事 → "I do not meddle"

*(was: "I practice non-interference")*

The line sits third in a quartet, and it was the only member that was not a plain saying:

> 我**無為**，而民自化 — *I do not do, and the people transform themselves*
> 我好靜，而民自正 — *I love stillness, and the people right themselves*
> 我**無事**，而民自富 — *I do not meddle, and the people enrich themselves*
> 我無欲，而民自樸 — *I am desireless, and the people become plain of themselves*

In the Chinese, 無為 and 無事 are visibly the same construction — the same negation over two different hands (`glossary/shi-事.md`). Four plain statements now, and the pairing is audible. The chapter's other 無事, 以無事取天下, follows: *"win the world by not meddling."*

### Ch 49

#### 善者，吾善之 → "The masterful, I count as masterful"

*(2026-08-14. Was: "The good, I am good to.")*

善 stands four times in two lines — twice for the kind of person, twice as a **verb**, *to reckon as 善*. Rendering it *good* made this a chapter about kindness to the wicked. It is not; it is a chapter about **refusing to grade people**, which is a stranger and better claim, and the same one Ch 27 (無棄人) and Ch 62 (何棄之有) make.

**Wang Bi decided it, by reading Ch 49 in Ch 27's own vocabulary.** On the couplet: 各**因**其**用**，則善不失也, *"go along with each according to their **use**, and then 善 is not lost."* On the tag 德善, three characters: **無棄人也**, *"there are no discarded people"* — Ch 27's own line. And at the chapter's close: 能者與之，**資**者取之, *"those with ability, go along with; those who are **raw material**, take them up"* — 資 being the exact character Ch 27 gives the unmasterful. Heshang Gong reads it morally instead (百姓雖有不善者，聖人化之使善也) and that stays on the record. Full argument in `glossary/shan-善.md`.

#### 德善 / 德信 → "Integrity is mastery" / "Integrity is trust"

*(was: "for integrity is good" / "for integrity is trustworthy")*

Two characters, no verb, and **no causal word** — no 故, no 因. The English had supplied a *because*, turning a bare tag into a moral premise. Removing it makes the stronger claim: **integrity is not the reason for the refusal to grade; integrity *is* the refusal to grade.**

*Rejected: reading 德 as its homophone 得 (dé — to obtain), giving "and so mastery is gained."* It is a common reading and Wang Bi's 無棄人也 fits it, but this edition locks 德 → integrity everywhere and a search-level consensus is not sufficient warrant to break a lock. **Shalom's call.**

#### 歙歙焉 → "breathes gently" · 渾其心 → "let their heart go muddy"

歙 (*xī*) is to draw in, to inhale. Wang Bi glosses 歙歙焉 as 心無所主也, *"the heart presides over nothing."* **"Breathes gently"** keeps the breath; what it lets go is the self-effacement Wang Bi hears. *(An edition fork, undecided: Heshang Gong's text reads 怵怵 — chù chù, wary — and the 釋文 records 惵惵.)*

渾 (*hún*) is to blend, to make turbid. The earlier *"merges their heart with the world"* had the sense and lost the water. **Muddy** chimes with Ch 15's 混兮其若濁, *"Mixed, like muddy water"* — where muddiness is the good state you sit still inside until it clears. Wang Bi: 意無所適莫也, *"the intention has no for and no against."*

#### 百姓皆注其耳目，聖人皆孩之 → "The people pour out their attention, all eyes and ears; / the sage sees them pure as infants"

**注** (*zhù*) is water pouring — the same character the Mawangdui silks put at the head of Ch 62. Both commentators gloss it as 用 (*yòng* — to use). English supplies the gift here: ***all eyes and ears*** is a live idiom for rapt attention **and is literally 耳目**, so the idiom carries the sense while the organs survive.

**孩** (*hái*) is not primarily *child*. The *Shuowen* defines its older form 咳 as 小兒笑也, **"a small child's laughing"** — the sense *child* came from the smile. And Ch 20 uses it that way: 如嬰兒之未**孩**, *"like an infant that has not yet smiled."* Those two are the only occurrences in the book, so Ch 20 is our dictionary for Ch 49. *(The Siku editors note the 釋文's claim that Wang Bi's text read 咳 here — the same word, the older graph.)*

**Why "sees them" and not "makes them."** 孩之 is grammatically causative, and Wang Bi reads it so (皆使和而無欲，如嬰兒也). But **the chapter's machinery is three acts of regard, not three interventions** — 吾善之 (*I count them masterful*), 吾信之 (*I trust them*), 孩之 (*the sage sees them as infants*). Rendering the last as something done *to* the people breaks that, in a chapter whose whole subject is not managing them. It leans to Heshang Gong's 愛念 (*cherishes, holds in mind*) over Wang Bi's causative, and *pure* is supplied — it does the work of telling a modern reader which property of infancy is meant, since English *infantile* runs the wrong way. **Both costs are Shalom's call, taken deliberately.**

### Ch 52

#### 其母 / 天下母 → "our mother"

*(not "the mother")*

The Chinese is 其母, "its mother," and 天下母, "the mother of the world" — *the*, not *our*. We add the possessive on purpose, and its warrant is already in the text: the mother of *all-under-heaven* is the mother of *us*, and of everything — so "our" invents no relationship, it only draws out the one Laozi states. It also turns her children (其子) into our *siblings*: we and the rivers and the stars, all born of one mother — as Taoist a thought as the book holds.

But the possessive is held under one strict condition, the same the 母 entry draws: **"our" means *belonging*, never *possession*.** The cosmic mother is fierce, not fond (天地不仁, 5); she bears all and clings to none, and favors no one. She is "ours" only the way the sky is ours — everyone's, possessed by none. Read as *the mother of us all*, "our mother" may be the truest word in the chapter; let it drift toward *our own dear mom* and it betrays her. The warmth is earned only while it stays inclusive.

A note on placement: in Chapter 52 we keep line 1's cosmic naming — "the mother of the world" (天下母) — and turn to "our mother" only from line 2 (其母), as the movement goes inward, toward return and homecoming. Awe first, then intimacy: she is named as the mother of *everything* before she is held as the mother of *us*.

### Ch 53

#### 是謂 → "This exposes…"

*(not "This is called…")*

The formula 是謂 X means "this is called X" — a *naming*. In this one line (是謂盜竽) we render it "**exposes**": *"This exposes the ringleader of thieves."* The departure is deliberate, and it buys two things.

*Grammar.* The literal "This is the ringleader of thieves" welds a *scene* (the immaculate court, the silk, the gorging) to a *person* (the ringleader) with a bare "is," and the seam shows — a tableau is not a man. "Exposes" is a verb a scene can rightly do to a person: it reveals, unmasks, lays him bare.

*Force.* It draws out what the naming *does* here. All the ruler's splendor poses as legitimate majesty; to *name* it "the ringleader of thieves" is to strip that majesty off and show the criminal beneath. "Exposes" turns the whole description into an unmasking — the robes torn away to reveal the thief.

It is not literal (是謂 is "is called," not "exposes") — but to name a robed ruler the chief of thieves *is* to expose him; we let the English verb do what the Chinese naming does in force. A small liberty that repairs a real referential seam, and turns splendor into disguise.

### Ch 55

#### 全作 → "its whole being quickens with life"

*(setting aside the traditional male-erection gloss)*

The line proves the newborn's intact vitality: 未知牝牡之合而全作，精之至也 — *not yet knowing the union of female and male, yet [it] stirs — vital essence at its utmost.* The traditional reading is the male infant's reflex erection (explicit in the older 朘 variant; see Manuscript Notes). We read our base text's 全 ("whole") in its plain sense — *the whole being quickens with life* — a defensible **minority** reading, chosen deliberately so the emblem holds for infants of every gender. Nothing essential is lost: the desirelessness (*not yet knowing… yet*), the spontaneity (*with life, of itself*), and 精之至 (vital essence at its fullest) all remain — arguably *deepened*, since it is now the whole infant alive with undesiring vitality, not one organ. Faithful to the point; universal in the image. *(Governing principle: Process guide §0, "universality over the incidental male-default.")*

### Ch 57

#### 取天下 → "win the world through non-interference"

*(the Ch 48 rule, second instance)*

The phrase returns from 48. There, 取天下常以無事 taught that the world is won only through non-doing, and we rendered 取天下 not as "take" or "seize" but as the world *coming to you* — 取 as reception, not conquest. Here the same lesson is compressed into a single clause: 以無事取天下. The draft reached for "master the world," but 無事 and "master" cancel each other — the line's whole claim is that you gain the world by *not* mastering it. So we hold the 48 reading: "win the world through non-interference," the world gained by the open hand. 取 is what falls to you when you stop grabbing for it — in 57 as in 48. (One consistency note travels with it: 無事 stays **non-interference** in both of its appearances here — 以無事取天下 and 我無事而民自富 — and stays distinct from 無為, *non-doing*, which the same stanza uses separately. See the open seam under Ch 63 · 事無事.)

### Ch 61

#### 為下 → "is underneath" / "ought to be underneath"

*(not "takes the lower position")*

為下 (*wéi xià* — "be the low one") occurs exactly twice in the chapter: once of the female animal (以靜**為下**) and once in the closing line (大者宜**為下**). Nothing else in the chapter uses that construction; the middle lines use 以下 and bare 下. So the two are a clasp, binding the barnyard to the statecraft, and **they must read identically in English** or the chapter stops being one thought.

We render both **"underneath."** The safe alternative, "takes the lower position," is bureaucratic and holds only one of the three things 下 is doing here. 下 runs nine times through nine lines — in 下流 (*xià liú* — downstream), twice inside 天下 (*tiān xià* — "under-sky," the world), in 以下 / 下以 / 下而, and in the two 為下 — and it means, simultaneously, *downstream*, *humbled*, and *underneath in mating*. The chapter's argument runs on that convergence. "Underneath" is the only plain English that holds all three, and it lets the final line land as hard as the Chinese does: the great power's proper posture is the cow's posture. That discomfort is the chapter.

#### 或下以取，或下而取 → "the large state takes by going low, the small state by staying low"

A recap line (故 — *gù*, "so"), seven characters against the fourteen-character couplet it summarizes. The only difference between its halves is a particle: 下**以**取 (以 marks purpose — lowers *in order to* take) against 下**而**取 (而 marks mere sequence — lowers, *and* takes). We do not build on that contrast. Heshang Gong reads the line as a plain restatement of the two cases and does not treat 以/而 as semantic, so the distinction may be rhythmic; and an English recap that reproduces the couplet with a hairline change reads as repetition, not summary.

What we render instead is the asymmetry that is certainly present and that the final line acts on: **who has to move.** Both parties go low, but only the large one has anywhere to come down from. "Going / staying" carries that in one aspectual pair while keeping the single lexical item "low" in both halves, mirroring the single 下 the Chinese repeats. An earlier draft used "stooping" for the large state; it was dropped because English *stoop* carries condescension (*stoop to conquer*) that 下 does not, and disdain for lowness is precisely the hierarchy this chapter inverts. **Cost, on the record:** the Chinese puts the difference in grammar and we have put it in vocabulary, and the non-purposive force of 而 is not carried.

#### 牝 stays an animal

牝 (*pìn*) is 牛 (*niú* — cattle) plus a phonetic: the female of a domestic animal, with a secondary sense of the genitals. Its partner 牡 (*mǔ* — the male animal) is 牛 with a component that in the oracle bones draws a penis, later regularized to 土 (*tǔ* — earth). The book's only other use of the pair, Ch 55's 未知牝牡之合 ("not yet knowing the joining of female and male"), is unambiguously about mating. So we render "the female" and "the male," and we keep *she*. **Not "the receptive female"** — 受 or any word for receptivity is simply not in the line, and the adjective tells the reader how to feel about the animal so that they never have to meet her. What "the female" still drops is that this is a stockbreeder's word; the glossary carries that, on the same principle as 心 (*xīn* — heart) and 物 (*wù* — things).

#### 取 stays "take," distinct from 勝

The chapter switches verbs deliberately: 勝 (*shèng* — overcome) appears once, and only of the animal; 取 (*qǔ* — take) appears four times, and only of the states. Rendering both "overcome" collapses the analogy into an identity. 取 is also the richer word — the graph is 又 (*yòu* — a hand) seizing 耳 (*ěr* — an ear), the tally taken from the fallen, and it is the original form of 娶 (*qǔ* — to take a wife). A war-trophy word and a marriage word, in a chapter arguing that you acquire by lying down. We let the double stand.

### Ch 62

#### 奧 → "the sanctuary"

*(never "mystery." Revised 2026-08-11; "the sheltered corner" was the first rendering and is retired.)*

道者萬物之奧. The source gloss offered *"the profound mystery/sanctuary of the ten thousand things"*, and *mystery* is the overlay. 奧 (*ào*) is a **place in a house**: the southwest corner of a dwelling, away from the door, dark — where the household shrine stood and the honored guest was seated. Concrete enough to point at, which is the test.

Both commentators gloss it as a place, and they diverge on which property matters:

- **河上公:** 奧，藏也。道為萬物之藏，無所不容也 — *"奧 is a storehouse. The Tao is the storehouse of the countless things; there is nothing it does not hold."* → **containment**.
- **王弼:** 奧猶曖也，可得庇䕃之辭 — *"奧 is like 曖 (ài — dim, shaded); it is a word for what one can get shelter under."* → **shade**.

We follow Wang Bi, because the two clauses that immediately follow are both about people taking refuge (寶 / 保). **The first rendering was "the sheltered corner."** It was accurate and it was opaque: a modern reader has no way to know why a corner of a house should matter, and the line's whole job is to say what the Tao *is* to everything.

**Why "sanctuary" — a word this note originally forbade.** Shalom challenged the rejection, and the challenge was right. "Sanctuary" was ruled out by reflex as an imported church, but the 奧 corner **was** the household's altar space: the seat of the presiding domestic spirit and the place of honour for the head of the family. *Analects* 3.13 turns on exactly that — 與其媚於**奧**，寧媚於灶, *"rather than court the 奧 [the spirit of the house's honoured corner], court the 灶 (zào — the stove god)."* Rendering a cult site as a cult site is translation, not overlay.

**And the decisive argument is one neither of us had going in.** English *sanctuary* carries two live senses: a holy place, **and the right of a fugitive to take refuge and not be seized.** The chapter's closing line is 求以得，有罪以免 — *"seek, and you find; have a crime against you, and you are spared"* — and Heshang Gong glosses it with no piety whatever: 遭亂世闇君，妄行刑誅，修道則可以解死, *"to meet a chaotic age and a benighted ruler, where punishments and executions fall at random; cultivating the Tao, one can be released from death."* **The chapter ends on the legal sense of the word.** *Sanctuary* does not import a church here; it anticipates the ending, and it primes 寶 / 保 (treasure / safekeeping) two lines earlier.

**The cost, named.** In English a sanctuary is somewhere you *go* — a building, a destination. The 奧 is where you already are: the part of the single room you live in that is furthest from the door. That domesticity matters in a book whose Ch 47 reads *"Without leaving home, you know the whole world."* The corner is therefore moved into the reader-facing note rather than dropped. And nothing is borrowed from the locks: 玄 (*xuán*) keeps *dark*, 妙 (*miào*) keeps *subtle* — 奧 takes neither.

#### 奧 — answering the 注 / 主 variant

*(added 2026-08-11)*

Both Mawangdui silks read **注** (*zhù*) where our base reads 奧. The standard modern critical edition, Gao Ming's *帛書老子校注*, takes 注 as a loan for **主** (*zhǔ* — master), yielding *"the Tao is the master of the countless things"* — and supports it from Zheng Xuan on the *Liji · Liyun* (奧猶主也, *"奧 is like 主"*) and from the *Zuozhuan*'s 國有奧主. That is a serious reading and it deserves to be answered rather than ignored.

**We answer it from Chapter 34, which denies it twice in the same two words:**

> 衣養**萬物**而不為**主** — *"it clothes and feeds the countless things, yet does not act as their master."*
> **萬物**歸焉而不為**主** — *"the countless things return to it, yet it does not act as their master."*

A Ch 62 reading 道者萬物之主 would set the book against itself on 萬物 and 主 — the identical pair, one chapter apart, asserted here and denied there. And nothing forces us to pay that: **注 at face value is 氵 (water) beside 主 — to pour into.** Read plainly, the silks say *what the countless things pour into*, which is a **confluence**, arriving one chapter after Ch 61's 大國者下流 (*the downstream flow*) and 天下之交 (*the confluence of the world*), and answering Ch 32's 猶川谷之於江海.

**And Gao Ming's own chain runs through a room.** 奧 can mean *master* only because the 奧 corner is where the household head presides — the *Shuowen* defines it flatly as 宛也，室之西南隅, *"the winding place; the southwest corner of a room."* The corner is prior; the mastery is derived from it. **So every witness here keeps the place, and only the dominion is optional — and Ch 34 forbids the dominion.** "The sanctuary" holds exactly what 奧 and 注 share and declines exactly what the book denies elsewhere.

#### 善 / 不善 → "masterful" / "unmasterful"

*(not "good" / "bad")*

The single decision that keeps this chapter out of the sermon. 善人 and 不善人 slide easily into *good person* and *bad person*; three lines later stands 有罪以免, and 罪 (*zuì*) is **crime**, not sin. Put those two renderings together and Ch 62 reads as a doctrine of grace, with 奧 supplying the sanctuary to receive it — a gospel assembled out of three separate slips, none of which the Chinese makes.

Held as **masterful / unmasterful** (following Ch 27, which renders 善 the same way), the chapter argues about **competence** instead: the Tao is the treasure of those who are adept and the safekeeping of those who are not, so why abandon anyone? Ch 62's 何棄之有 and Ch 27's 無棄人 are the same claim, and they should sound like it.

Heshang Gong confirms the register from the other end. His gloss on 有罪 is not moral at all — 遭亂世闇君，妄行刑誅，修道則可以解死 — *"to meet a chaotic age and a benighted ruler, where punishments and executions are inflicted at random; cultivating the Tao, one can be released from death."* Literal criminal jeopardy under an arbitrary state. Nobody is being absolved of anything.

#### 寶 / 保 — a sound-pair, and possibly a later one

*(corrected 2026-08-11)*

善人之**寶**，不善人之所**保** — both are *bǎo*. 寶 is treasure; 保 is 人 (person) beside 子 (child) — to keep safe, to hold. Wang Bi separates them exactly: 寶以為用也 (*"treasure, because they put it to use"*) / 保以全也 (*"safekeeping, because it keeps them whole"*). We render **treasure** / **safekeeping**, which keeps the two senses and loses the chime.

**This note first called the pair an original feature of the line. The witnesses do not support that.** Both Mawangdui silks use **one graph in both positions**, and published transcriptions disagree about which — so the received text's two graphs may be a **later differentiation of a single word**, and what we are rendering as a pun may be a Han editor's clarification of something the older text left as plain repetition. We keep the base text and the two senses, which Wang Bi's gloss independently supports. But the claim that Laozi wrote a pun here is withdrawn. *(Apparatus in the Manuscript Notes.)*

#### 美言 — a tension with Ch 81 that we are not resolving

Ch 62 grants 美言 (*měi yán* — fine words) real purchase: they can be traded, and honored conduct can set a person apart. **Ch 81 flatly distrusts them:** 信言不美，美言不信 — *"trustworthy words are not beautiful; beautiful words are not trustworthy."* The commentators split on the tone here too: Heshang Gong reads the line as a put-down (美言者獨可於市耳 — *"fine words are good for the marketplace, and that is all"*; 未足以尊道 — *"not enough to honor the Tao"*), while Wang Bi reads it as praise of the Tao, whose good report 奪衆貨之賈, *"outbids the price of every other good."*

We render it **positively and plainly**, because the line that follows depends on it: fine words and fine conduct work even on the inept, therefore no one is beyond reach, therefore 何棄之有 — why abandon them? Under Heshang Gong's dismissal that sentence does not follow from anything. But the tension with Ch 81 is genuine and stays open; it is not to be smoothed when Ch 81 is drafted.

*(The line also carries a textual fork — the silks and both commentaries divide it differently — resolved 2026-08-12 in favour of our base text. See the Manuscript Notes. The verse now reads "Fine words can buy honor. / Fine conduct can raise a person above others.")*

#### 何棄之有 → "why abandon them?"

*(was: "why would you throw them away?" — retired 2026-08-11, flagged by Shalom)*

Two faults in one clause, and the grammar is the first.

**何 … 之有 is a fixed classical idiom, and it is impersonal.** Literally *"what ___ is there?"* — the same construction as the *Analects*' 何陋之有 (*hé lòu zhī yǒu* — *"what meanness is there in it?"*), where 之 (*zhī*) fronts the object before the verb. Its force is an **emphatic denial in the shape of a question**: *there is no such thing.* The earlier rendering supplied a **"you"** the Chinese does not have, converting a statement about how things stand into a reproach aimed at the reader.

**And 棄 is graver than "throw away".** The graph is three elements: an **infant drawn upside-down** (head-first, as at birth), a pair of **hands**, and a **winnowing basket** — two hands lifting a basket with a newborn in it. The word is *infant exposure*. It was not a dead metaphor: the Zhou agricultural ancestor Hou Ji was **named** 棄, *Abandoned*, from the story that his mother left him at birth and he survived. Heshang Gong uses it as a social category — 無有**棄民**, *"there were no abandoned people"* — and Wang Bi glosses the line with 放 (*fàng* — **banishment**), the formal penalty of expulsion.

So the register is exposure, banishment, a person put outside where they cannot live. **"Throw away" is the wrong size**: in modern English it means trash, which sounds harsher and lands lighter. **"Abandon"** is the ordinary English word for what the character depicts — *an abandoned child* is this picture exactly.

**Rejected as a trap:** *"what is there to abandon?"* is the most literal rendering of the idiom and the most misleading, because English hears it as *there is nothing in them worth keeping* — the reverse of the chapter's claim. *"How could they be abandoned?"* is closer to the idiom's flatness and was the runner-up; *"why abandon them?"* keeps the force and the mouth-feel.

**Retrofit owed:** Ch 27's 故無棄人 currently reads *"ensures that no one is lost."* Same character, same argument, and Ch 27 is now the softer of the two. See `WORKLIST.md`.

#### 立 → "raise up", to keep the 立 / 坐 axis

立 (*lì*) is a person standing on a ground-line — to stand a thing upright, and the ordinary verb for establishing a ruler. 坐 (*zuò*) is to sit. The chapter's two halves are 故**立**天子 and 不如**坐**進此道: they *stand a ruler up*, and the answer is to *sit down*. We render "raise up" rather than "enthrone" — which was the first draft, and which both flattens the verb and adds a throne the Chinese does not have, in a chapter about not adding thrones. **Stated honestly: 立 is idiomatic for enthroning and the contrast may not be deliberate.** But 坐進此道 *is* marked — "sitting and offering" is odd enough that Wang Bi glosses it out (不如坐而進此道) — so the axis is available in the Chinese, and keeping it costs the English nothing.

#### 天子 → "a child of the sky"

*(was: "Son of Heaven" — retired 2026-08-11, and with it the strain case that protected it)*

**The rendering "Son of Heaven" was the only "Heaven" in all 81 chapters.** Every other 天 (*tiān*) in this edition is *sky* or *nature*. One phrase in one chapter was carrying the entire theistic vocabulary of the English Tao Te Ching by itself, protected by a strain-case note arguing that the title should be kept "the way one keeps *Pope*." The analogy runs backwards: *Pope* is what Catholics actually call him, whereas **no Chinese speaker has ever said "Son of Heaven."** It is an English phrase about a Chinese title.

**The characters.** 天 is a picture of a standing person with the head marked — 大 (a human, arms out) under a stroke. *Shuowen Jiezi* (~100 CE): 天，顛也，至高無上，从一大 — *"天 is 顛 (diān — the crown of the head); the highest, with nothing above it; composed of 一 over 大."* The word is the top of a person, hence what is overhead, hence sky. No realm, no occupant. 子 is a **swaddled infant** — big head, arms, wrapped legs — and this book uses it that way in both places it matters: Ch 4's 吾不知誰之**子** (*"I do not know whose child it is"*) and Ch 52's 既得其母，以知其**子**, where 子 is fixed by direct opposition to 母 (mother), a lock. So 天子 is **the sky's child**.

**Where "Son of Heaven" comes from — two layers, both already named by this project.** The *Chinese* layer: 天子 is not an old neutral word for a ruler. Shang kings called themselves 王 and appealed to 帝 (*dì* — the high ancestral god); the Zhou, having conquered them, produced 天命 (*tiān mìng* — the sky's mandate) to explain why the Shang's own god had abandoned them, and 天子 is the title that doctrine minted. A legitimation device, made by the winners — the same move `DISCOVERIES.md` §1 catches in Ch 25, where our base text reads 王 (king) and both Mawangdui silks read 人 (human). The *English* layer: Legge and his contemporaries rendered 天 as "Heaven" throughout and 天子 as "Son of Heaven," in an English where *Son of ___* had one resonance. These are the translators who put 太初有道 at John 1:1. The phrase was built to sound like scripture.

**Checked, 2026-08-11 — and the silks have it.** When this decision was first made, `--witnesses 62` was blank and we declined to claim 天子 was an interpolation on the strength of not knowing. **The Mawangdui text carries 立天子.** So the title is Laozi's own and *not* an accretion of the Ch 25 kind. **The overlay was never in the Chinese. It was entirely in the English.** Nor should we have wanted it otherwise: Ch 62 names the apex of state ceremony — the enthronement, the three highest offices, jade borne ahead of four-horse teams — in order to knock it over with 不如坐進此道, *better to sit where you are*. Remove the grandeur and the argument goes with it. **We keep the title and change the English.**

**Why "child of the sky" is right, and the argument is internal.** In this book the sky is not the top of anything:

> 人法地，地法天，**天法道**，道法自然 (25)
> *the human follows earth, earth follows the sky, **the sky follows the Tao**, the Tao models itself on being what it is.*

And the Tao is 先天地生, *born before sky and earth*. **The sky is itself a child.** Ch 4 leaves the Tao's own parentage unknown and puts it before 帝; Ch 52 gives the world a mother. So within Laozi's own cosmology, 天子 is not a claim of divine descent — it is kinship with a junior member of the family, whose actual parent is the 母. **The title deflates on contact with Ch 25.** "Son of Heaven" prevents that; "a child of the sky" performs it. In a chapter whose whole argument is that this apparatus is worth less than sitting down, the smaller-sounding phrase is the more accurate one.

**Three locks recovered at once:** 天 keeps *sky*; the capital goes, per standing rule 5; and *Son* goes, which the graph never supported. **The seam, noted and not erased:** every historical 天子 was a man, and the title was male in every practical sense. 子 is not — it is an infant in swaddling. We render toward the universal, as at Ch 16's 公乃王 and Ch 55's 朘, and say so here.

**Cost, on the record:** we have traded office for image. 天子 was a piece of ordinary state vocabulary — as ordinary as *Prime Minister*, which is made of "first" and "servant" and which nobody hears — and the English now foregrounds a picture the Chinese kept in the background. Worth it in this chapter, whose business is shrinking the office. It would not be worth it in a chapter that needed the institution to sit there inertly. 天子 occurs nowhere else, so the trade is never retested. *(Fuller treatment in the Reading Notes; `DISCOVERIES.md` §3.)*

#### 三公 → "the three ministers"

*(not "the Three Dukes." Two entries on this were merged 2026-08-11.)*

公 (*gōng*) is 八 (*bā* — to divide; two strokes parting) over 厶 (*sī* — private, the self, the old form of 私). The word is **the dividing-up of what is private** — hence *public, common, impartial*; *Shuowen*: 公，平分也, *"公 is fair division."* This edition already renders it that way at Ch 16 (容乃**公**，**公**乃王 → *"Embracing all leads to impartiality. Impartiality leads to sovereignty."*).

As an office title 公 is conventionally *duke*, a borrowed European feudal rank we reject; *minister* says the same thing about an office of state without importing a peerage. Lowercase, per standing rule 5.

**The silks settle it in our favour:** where our base reads 三公 they write 三鄉, which editors read as a loan for 三**卿** (*sān qīng*) — the word that simply means *high minister*. Our "three ministers" turns out to be the oldest witness's own word.

It still drops the 公 etymology, and Ch 42's 王公 currently reads *"kings and lords."* Three chapters, three treatments. **公 wants a glossary entry**, and when it gets one, Ch 42 and Ch 62 will have to answer to Ch 16. Logged in `WORKLIST.md`.

#### 拱璧以先駟馬 → "jade discs too wide for one pair of arms, borne ahead of a team of four horses"

拱 (*gǒng*) is the gesture of both arms encircling — Wang Bi writes 拱抱寶璧, *"jade discs one embraces."* 璧 (*bì*) is the ring-shaped ceremonial jade. The jade travelling **in front of** the horses is the protocol of the highest state gift. The whole image exists to be set against 坐進此道 — 坐 (*zuò* — to sit). A procession, against sitting still. We keep both verbs concrete: *"better to sit where you are and offer this Tao."*

### Ch 63

#### 事無事 → "serve the not-serving"

*(2026-08-12. Was "tend the not-tending," briefly; the glossary entry had illustrated it as "attend the not-attending.")*

The triple 為無為，事無事，味無味 is the line that forced the 無為 → *non-doing* lock (`glossary/wuwei-無為.md`). **Each beat is one character twice with 無 (*wú* — there is no) between them**, so the verb has to hold in two positions at once — as a verb, and as the thing that verb is done to. That constrains the middle beat in a way the other 無事 lines are not constrained, because at Ch 48 and Ch 57 無事 stands alone with nothing to rhyme against.

**The verb must also be neutral.** *Do* is neutral, *taste* is neutral, and the paradox lives in the negation. *Meddle* — the word chosen for 48 and 57 — fails twice here: you meddle *in* something, so the bare transitive is not English, and a verb that is already a rebuke flattens the line into a plain prohibition, which is the one thing it must not become.

**Serve** is 事's oldest verb sense and the one the graph draws — a hand holding the badge of office is a hand *in service*. It is also already this edition's word for 事 at Ch 59 (治人**事**天 → *governing people and serving nature*) and Ch 61 (入**事**人 → *enter and serve people*), so the middle beat now ties to the two chapters where 事 is unambiguously *serve*. And it is one syllable, which keeps the three beats even against *do* and *taste*.

*A loss the triple already accepts:* 味無味 reads **"taste the flavorless"** — two English words for one character — because *flavorless* buys the chime with Ch 35's 淡乎其無味, where the Tao itself is bland and flavorless. The internal echo is worth having and is not sacred.

*Why "tend" was retired within the day:* tending is what you do to a garden to make it grow, so *not tending* implies neglect that kills — the reverse of what these chapters claim, which is that things flourish once the hand comes off (民自富, *the people grow rich of themselves*). Caught by Shalom.

#### 味無味 → "taste the flavorless"

*(not "taste the tasteless")*

Ch 35 already renders 淡乎其無味 as *"It is bland and flavorless"* — and the thing being described there is the **Tao**. Matching the word makes 味無味 legible as what it is: not a general counsel of blandness but an instruction to **taste the Tao**. Wang Bi reads it the same way — 以恬淡為味, *"takes the calm and bland as its flavor."*

#### 大小多少 → "Great or small, many or few" — a quantifier, not a maxim

Four bare characters — 大 (*dà* — great), 小 (*xiǎo* — small), 多 (*duō* — many), 少 (*shǎo* — few) — with no grammar between them. Three readings are genuinely available, and each classical commentator takes a different one:

- **王弼 (Wang Bi):** binds them to the clause that follows. His comment on the joint lemma 大小多少報怨以徳 is entirely about resentment — 小怨則不足以報，大怨則天下之所欲誅，順天下之所同者，德也, *"a small resentment is not worth repaying; a great resentment is what the whole world wishes to punish; to go along with what the world holds in common — that is integrity."* So: **great or small, many or few [resentments]**, repay resentment with integrity.
- **河上公 (Heshang Gong):** 欲大反小，欲多反少，自然之道也 — *"want the great, revert to the small; want the many, revert to the few — this is the way of what is so of itself."* So: shrink the large.
- **The common modern reading**, supported obliquely by Han Feizi's 敬細以遠大 (*"respect the minute in order to keep the great at a distance"*): magnify the small — *treat the small as great, the few as many*.

**We follow Wang Bi**, on three grounds. He is the commentator on our own base text. His is the only reading under which the eight characters of the line form one thought rather than two unrelated ones — which matters now that Mawangdui A confirms 報怨以德 belongs here (see the Manuscript Notes). And the scale-doctrine the other two readings extract is already stated outright two lines down, in 圖難於其易，為大於其細 — the chapter does not need 大小多少 to say it a second time.

**The cost, stated plainly:** a famous aphorism becomes a grammatical particle. We accept it. Where the chapter argues scale it argues it in full sentences; this line is about grievance.

#### 細 → "slight", never "small"

細 (*xì*) is 糸 (*mì* — silk thread) over 田 — **thread-fineness**, not size, and the distinction is the chapter's. Han Feizi's illustrations of 細 are all hairline things: a thousand-yard dike bursting through **an ant's hole** (螻蟻之穴), a hundred-foot house burning from **smoke in a crack** (突隙之煙), a disease caught at the 腠理 (*còu lǐ* — the pores of the skin). Those are not small. They are *thin*. 小 (*xiǎo*) keeps *small*; 細 takes **slight**. The two must not collapse into one English word, here or at Ch 67's 其細也夫.

### Ch 64 · 始於足下 → "begins beneath your feet", never "with a single step"

There is no step in the line. 足下 (*zú xià*) is 足 (*zú* — foot) under 下 (*xià* — below): **under the foot**, the ground you are standing on. The received English — *"a journey of a thousand miles begins with a single step"* — inserts a step, and with it a whole doctrine of effortful beginnings that the chapter does not hold.

The commentaries settle it. 河上公 glosses the three proverbs in three matched phrases: 從小成大 (*"from small it becomes great"*), 從卑至高 (*"from low it reaches high"*), 從近至遠 (*"**from near** it reaches far"*). **Near**, not *few*. The axis is distance from where you stand, not a count of steps.

**What "a single step" drops:** the chapter's argument. Every other image here is of a thing that is small and close and *not yet anything* — 未兆 (not yet cracked into a sign), 微 (faint), 毫末 (a hair's tip), 累土 (a heap of dirt). "A single step" converts that into motivation. "Beneath your feet" keeps it as location — **this, the thing you are standing on**, which is the same epistemology as the 以此 formula in `DISCOVERIES.md` §2.

### Ch 64 · 毫末 → "a hair's tip", never "a tiny sprout"

毫 (*háo*) is the fine hair of an animal's winter coat; 末 (*mò*) is 木 (tree) with a stroke marking the **tip** of the branch. **The tip of a hair.** Our source-table gloss reads "a tiny sprout," which domesticates the image into botany to match the tree — and loses the scale, which is the point. Laozi is not saying a big tree starts as a small tree. He is saying it starts as something as fine as a hair.

### Ch 64 · 未兆 → "gives no sign" — and a note on keeping research out of the verse

兆 (*zhào*) is the **fissure in a heated oracle bone or turtle plastron** — the crack the diviner reads. That is a real finding and it settles the reading: 未兆 is not "before it shows signs" in some loose metaphorical sense but *before anything readable has appeared*, which is why the paired verb is 謀 (*móu* — to plan, to lay a scheme). Wang Bi ties the whole opening to it — 謀之無功之勢, *"you plan it while the situation has not yet yielded any result"* — and Heshang Gong glosses the state as 未有形兆, *"has not yet taken shape or sign."*

**But the etymology stays in this file.** The line was first drafted as *"What has not yet cracked into a sign is easy to plan for"* and Shalom caught it as awkward, which it was, in two ways worth naming because the failure will recur:

1. **The research was in the poem.** The oracle-bone crack explains why the reading is right; it is not what a listener heard. Laozi's audience heard *before there is any sign of it*. Run the pointing test on the English, not only on the Chinese.
2. **The proportion was wrong.** The Chinese quatrain runs 4–5–4–4 characters — 其安易持 · 其未兆易謀 · 其脆易泮 · 其微易散. The draft ran 7–13–7–7 words. The Chinese lengthens that line by one character; the English nearly doubled it, and a stanza built on parallel shows the bulge immediately. **Count the characters before deciding an English line is finished.**

**Settled: "What shows no sign is easy to plan for."** Eight words against the neighbours' seven, matching the slight stretch the Chinese itself allows. It keeps 兆's own noun.

*The accepted loss:* 未 (*wèi*) is "not **yet**," and *shows no sign* drops the *yet*. The stanza recovers it two lines down, where 為之於未有 reads *"handle it while it is not yet there"* — so the temporal frame is stated once rather than twice. Alternates considered and set aside: *"What shows no sign yet"* (keeps 未 exactly, costs a beat on the trailing word) and *"What has not yet shown itself"* (closest to Heshang Gong's 未有形兆, but ten words, and the bulge returns).

### Ch 64 · 復眾人之所過 → "brings the crowd back from where they have gone too far"

過 (*guò*) carries both *pass by* and *go too far*, and English can hold both — going past **is** overshooting. The commentaries take the second, and they agree:

- **王弼:** 不學而能者自然也，喻於不學者過也，故學不學以復衆人之過 — *"what one is capable of **without** learning is what is so of itself; being instructed away from the unlearned is the **overshooting**; so one learns the not-learning in order to bring back the crowd's overshooting."*
- **河上公:** 衆人學問反過本為末，過實為華 — *"the crowd's learning turns the wrong way: they **overshoot** the root for the branch, overshoot the substance for the flower"* — and 復之者使反本也, *"to 復 them is to make them return to the root."*

So 復 (*fù*) is **bring back**, not *recover*, and what is brought back is people, not lost knowledge. The common English *"restores what the multitude has passed over"* reads 過 as *passed by* and turns the sage into an archivist of neglected things.

**Wang Bi's gloss is the chapter's hinge**, and worth stating plainly: he equates 不學 (*bù xué* — the unlearned) with 自然 (*zìrán* — so of itself). That makes the last line, 以輔萬物之自然，the thesis rather than the coda, and makes 學不學 the same move as 為無為 — get your hand off the thing that already works.

### Ch 64 · 欲不欲 / 學不學 keep Ch 63's shape

欲不欲 (*yù bù yù*) and 學不學 (*xué bù xué*) are grammatically identical to Ch 63's triple 為無為，事無事，味無味, rendered there *"Do the not-doing, serve the not-serving, taste the flavorless."* So here: **"wants the not-wanting"** — and, by an accepted departure, **"learns to unlearn."**

*Why the second one breaks the pattern.* The parallel wants "learns the not-learning," and 不學 is strictly the capacity that **precedes** learning — Wang Bi's 不學而能者自然也, *"what one is capable of without learning is what is so of itself"* — where *unlearn* implies erasing something already acquired. Related, not identical. Shalom kept "learns to unlearn" for its compression, with the cost named: the four-line series loses one of its two matched hinges. Logged so the departure is visible rather than looking like drift.

Heshang Gong reads both lines differently — 聖人欲人所不欲, *"the sage desires what people do not desire"* — a comparative rather than a reflexive. We keep the reflexive, on internal consistency: this construction is a signature of the book and it must not shift shape between adjacent chapters.

### Ch 64 · 自然 → "being so of themselves", and 不敢為 → "never pushes them"

Two closing decisions, both about resisting a smoother English.

**以輔萬物之自然** was drafted as *"supports the countless things in being what they truly are."* That is lovely and it imports a metaphysics the Chinese does not have: *truly* implies a false self to be told apart from a real one. 自然 (*zìrán*) is **so-of-itself** — process, not essence, and nothing underneath it to be true to. Settled as **"in being so of themselves."**

**而不敢為** was drafted as *"without forcing anything."* Two losses. First, 為 (*wéi*) is already rendered **handle** twelve lines above, in 為者敗之 — the same character cannot be two English words inside one chapter. Second, 敢 (*gǎn*) disappears altogether: the sage *could* and refuses to, which is restraint before what is so of itself rather than a description of manner. It also matters for this chapter specifically, whose logic is also the logic of preemption (see the Reading Notes on the shadow). 不敢為 is the constraint that keeps the chapter honest, and a prohibition must not soften into a style.

**First settled as "and does not dare to do," then superseded on 2026-08-20 by the 敢 lock** — see `glossary/gan-敢.md` and the sweep note below. *Dare* reads as fear in modern English and Ch 73 makes 不敢 a form of courage. **Now "and never pushes them,"** which carries 敢為 as one verb rather than splitting it; the argument above stands unchanged, only the English moved.

*A limit of the harness, recorded because it will recur:* **"force" cannot be forbidden for 為 mechanically.** Six chapters carry both 為 and 強 (*qiáng* — strong, to force), and Ch 25's *"Forcing a label upon it"* renders 強 legitimately. The checker's evidence gate cannot say *right for that character, wrong for this one, same chapter*. So this stays a judgment call, and the Ch 29 debt in `WORKLIST.md` has to be argued rather than swept.

### Ch 66 · 處前而民不害 → "the people are not hindered" — and the reading we did not take

害 (*hài*) is *harm*, and the line is genuinely double.

**河上公 reads it as the people's intent:** 民親之若父母，無有欲害之心也 — *"the people are close to them as to father and mother, and have no heart wishing to harm them."* On that reading, 不害 describes what the people do **not want to do to the leader**.

**We read it as the people's experience**, on the parallel. The couplet is built as 處**上**而民不**重** / 處**前**而民不**害** — position, then consequence, twice. Above produces weight; in front produces obstruction. Reading the second half as a shift from the people's burden to the people's intent breaks a parallel the Chinese builds carefully.

And Heshang Gong supplies the obstruction reading himself, in the same breath: 不以光明蔽後 — *"does not use their brilliance to **eclipse** those behind."* 蔽 (*bì*) is to screen or cover over. That is the harm of standing in front, and 害 carries *hinder* within its range (cf. 妨害). **Settled as "the people are not hindered."** The alternative is real and is recorded here rather than dissolved.

### Ch 66 · 爭 → "compete", carried forward — but the term is owed an entry now

爭 (*zhēng*) is two hands, 爪 above and 又 below, pulling at one object between them: a tug of war. Rendered **"compete"** here to match the three drafted chapters that already use it — ch 3 (使民不爭), ch 8 (twice), and ch 22, which shares this chapter's closing formula 故天下莫能與之爭 verbatim and reads *"no one in the world can compete with them."*

**But "compete" is not obviously right, and the decision is about to get expensive.** 爭 is elemental grabbing, not rule-governed rivalry; modern English "compete" carries sport and markets. *Contend* is closer to the two hands. Three undrafted chapters are queued on this word — **68** (不爭之德, "the integrity of not-爭"), **73** (不爭而善勝), and **81** (為而不爭) — and 68's line in particular reads very differently as *the integrity of not contending*.

**Recommendation: settle 爭 with a glossary entry before drafting 68.** Deciding it now costs one entry; deciding it after 68, 73 and 81 costs a four-chapter retrofit on a term that appears in seven.

### Ch 65 · 明 → "clever" — a licensed departure from the lock, on Wang Bi's authority

明 (*míng*) is locked to **clear-seeing / clarity**, never "enlightenment" or "brilliance." **Ch 65 departs from it**, rendering 非以明民 as *"did not use it to make the people clever."* The departure is deliberate and is the only one in the book.

**Wang Bi defines the word himself, in this chapter, and defines it against the lock:**

> 明謂多見巧詐，蔽其樸也 — *"明 here means seeing much and artful deceit, screening over their uncarved."*
> 愚謂無知守真，順自然也 — *"愚 here means without cunning, holding fast to the true, following what is so of itself."*

That is not the 明 of Ch 33 (自知者明 — *"to know oneself is clear-seeing"*) or Ch 52. Here 明 is transitive and causative — 明民, *to make the people 明* — and what it produces, on Wang Bi's reading, is **巧詐** (*qiǎo zhà* — artifice and deceit). Heshang Gong reads it identically: 不以道教民明知巧詐也, *"does not use the Tao to teach the people bright-knowing and artful deceit."*

**So the lock is not broken; the character is being used in a second sense, and both classical commentators say so in as many words.** Rendering "clear-seeing" here would produce the opposite of the chapter: it would have the ancients withholding clarity from the people, which is precisely the authoritarian misreading this chapter has suffered for a century.

*This is the case `CLAUDE.md` anticipates — "departures require a logged reason." The reason is above.*

### Ch 65 · 愚 → "guileless", not "ignorant"

愚 (*yú*) is the word that makes this chapter look like a programme for keeping subjects stupid. It is not, and the evidence is internal.

**The sage claims 愚 for themselves.** Ch 20, already drafted, renders 我愚人之心也哉 as *"I have the heart of a fool!"* — a boast, in a passage where the speaker is proud to be the dull one among the bright. The ruler in Ch 65 is not lowering the people beneath themselves. They are bringing everyone to where the sage already stands. That is levelling, not subjugation, and it collapses the standard reading.

**And both commentators gloss 愚 with this edition's own locked terms.** Wang Bi: 無知守真，**順自然**也 — following what is **so of itself**. Heshang Gong: 使**朴質**不詐偽 — making them **plain and uncarved**, not deceitful. 愚 is the uncarved state, not a deprivation.

**"Guileless" over "simple" or "ignorant".** *Simple* is ambiguous in English and slides toward *simple-minded*; *ignorant* imports exactly the deprivation the Chinese does not have. *Guileless* says what both commentaries say — **without 巧詐, artifice** — and is unambiguously a virtue. The cost: it loses the verbal link to Ch 20's *fool*, which the Reading Notes carry instead.

### Ch 65 · 福 → "good fortune", never "blessing"

福 (*fú*) sits on the overlay watchlist, and the literal gloss in this chapter's own Source table says **"a blessing to the state."** *Blessing* imports a blesser — an agent who confers favor — and there is none here. 國之福 is the state's **good fortune**, the plain counterpart of 國之賊, *the state's thief*. Rendered as the pair the Chinese builds: *robs the state* / *is the state's good fortune*.

### Ch 65 · 與物反矣 → "turns back together with things" — 反 holds both senses, and the book already chose

反 (*fǎn*) is 厂 (a slope) with 又 (a hand) — a hand turning something over, or a climb back across a ridge. From that one gesture come **reverse**, **oppose**, and **return**. The two commentators take different halves:

- **王弼:** 反其真也 — *"it returns to **their** true."* 反 as *return*.
- **河上公:** 玄德之人與萬物反異，萬物欲益己，玄德施與人也 — *"runs **counter** to the countless things: they wish to benefit themselves; profound integrity gives to others."* 反 as *contrary*.

**The line was first drafted on Heshang Gong's reading** — *"It runs contrary to things"* — argued from the 反/順 hinge, since 順 (going with the current) is 反's natural opposite and the paradox needs the opposition. **That was wrong, and for a reason worth recording: the argument never checked what 反 already means elsewhere in our own translation.**

- **Ch 25:** 遠曰**反** → *"going far means **returning**."*
- **Ch 40:** **反**者道之動 → *"**Returning** is the Tao's movement."*

**And Ch 65 puts 反 immediately after 遠, which is Ch 25's exact sequence.** 深矣，遠矣，與物反矣 traces the same arc as 大曰逝，逝曰遠，遠曰反 — deep, far, and then the turn. The chapter is not making a new claim about opposition; it is saying that profound integrity moves the way the Tao moves.

**The grammar settles it too.** 與 (*yǔ*) marks accompaniment — *together with*. Laozi did not write 逆物 (*against things*) or 反於物 (*opposed to things*), but 與物反: *with things, turned back*. Under the contrary reading, 與 is left doing nothing.

**Settled as "and turns back together with things."** *Turns back* carries both senses in ordinary English — you turn back toward home, and you turn back an advance — so the paradox survives intact without the book contradicting itself. **The paradox is inside the character**, and it is a physical fact rather than a mystical one: turning around and going against are the same act, seen from two positions. To anyone still walking forward, the one who has turned for home is coming straight at them.

### Ch 65 · 大順 → "runs with the great current", never "the great accord"

順 (*shùn*) is 川 (*chuān* — a river, three strokes of running water) over 頁 (*yè* — a head, the radical in 頭, 顏, 頸). **A head facing downstream.** Not agreement — *orientation*. Its opposite is 逆 (*nì*), an inverted person plus the movement radical: going upstream.

Drafted first as **"the great accord"** and caught by Shalom as vague. It was, in three ways: Latinate and abstract where 順 is a picture; *bilateral* (accord is mutual agreement) where 順 is unilateral and directional; and it flattened the chapter's close into conflict resolution — *runs contrary… then reaches agreement* — when the claim is that you turn from what things grab for and the current takes you.

**How the error happened, since the mechanism will recur:** *harmony* was unavailable — it belongs to 和 (*hé*) at ch 18, 42 and 55 — so the draft reached for the nearest synonym instead of going back to the character. A thesaurus standing in for a radical.

**Two facts raise the stakes.** 順 appears **exactly once in the whole book**, this line; 逆 never appears at all. It is a hapax at a chapter's final word, so it gets one shot and no consistency constraint. Rendered **"and only then runs with the great current"** — one verb, two prepositions, so the English performs the reversal the Chinese performs. *Current* keeps the water without taking 流's *flow* at Ch 61's 下流.

### Ch 65 · 智 → "guile", and why not "clever" or "cunning"

**The draft collapsed two characters into one word.** 明民 read *"make the people clever"* and 以其智多 read *"they are too clever"* — 明 (*míng*) and 智 (*zhì*), four lines apart, both *clever*. The same fault as 眾人/俗人 in Ch 20, and the checker cannot see it for the same reason.

**"Cunning" was the obvious repair and is already spoken for three times over:** ch 3 uses it for **知** (無知無欲) *and* for **智** (使夫智者) in adjacent lines, ch 57 for **巧** (人多伎巧), and ch 58 once more. A fourth character would make it useless.

**愚 and 智 are this chapter's own antonym pair** — 將以**愚**之 against 以其**智**多 — and 愚 is already rendered *guileless*. So 智 takes **guile**, and the English pair mirrors the Chinese pair exactly, in the same proportion: 愚 once and 智 three times, *guileless* once and *guile* three times.

**It is also what the commentators say.** 王弼: 多**智巧詐** — *"much 智, artful deceit."* 河上公: 以其**智**多，故為**巧偽** — *"because their 智 is much, they practise artifice and falsity."* Neither reads 智 here as innocent intelligence.

*The cost, stated:* 智 is a Confucian **virtue** — one of 仁義禮智 (humaneness, duty, ritual, wisdom) — so a neutral English word keeps Laozi's polemic sharp, attacking a thing everyone admires. *Guile* pre-loads the verdict. **We accept that here and not elsewhere:** the polemic lives in Ch 19's 絕聖棄智, which keeps *cleverness*. In Ch 65 both commentators say 智 has already curdled into artifice. A licensed split by chapter, like 無事.

### 王 → "ruler / sovereign / to rule", never "king" — swept 2026-08-19

The full argument is in `glossary/wang-王.md` and `DISCOVERIES.md` §4. The rendering decisions, chapter by chapter:

| Chapter | Chinese | was | now |
|---|---|---|---|
| 16 | 公乃王，王乃天 | sovereignty | **unchanged** — already ungendered |
| 25 | 王亦大 *(silks: 人)* | the aligned human | **unchanged** — already follows the witnesses |
| 32, 37 | 侯王 | rulers | **unchanged** |
| 39 | 侯王 ×3 | **wise** rulers | **rulers** |
| 42 | 王公 | **kings** and lords | **rulers and lords** |
| 66 | 百谷王 ×2 | **king** of the hundred valleys | **rule** the hundred valleys |

**The principle: 王 carries no gender and English *king* cannot shed one.** Chinese nouns have no grammatical gender and the graph is an axe-head, not a person. So *king* does not translate a gender; it adds one — and seats it on a throne in eight chapters that define authority by lowness.

**Ch 66 takes the verb.** 王 works verbally in classical Chinese (*wàng* — to reign over), and 能為百谷王 accepts it: *rivers and seas can **rule** the hundred valleys.* The verb keeps the power and seats nobody. Shalom's line.

**Ch 39's "wise" was ours.** 侯王 is a flat class term for the ruling stratum. Rendering it *wise rulers* three times handed the office a compliment the Chinese withholds — in the chapter whose own line is 是以侯王自謂孤、寡、不穀, *"this is why rulers call themselves orphaned, meagre, unworthy."* Deleted. Recorded rather than quietly fixed, because it is the clearest instance in this repository of the translator's politics leaking into the verse, and it was found only because three older overlays were being chased.

**Ch 42 keeps 公's word.** 王公 is 王 + 公, and 公 is locked to *lord / minister*, so the compound reads *rulers and lords*.

**Left open, and proposed rather than applied: Ch 25's "the aligned human."** Both silks read 人 (*rén* — human) where the received text reads 王, and our verse follows them — correctly. But it renders bare 人 as *the aligned human*, and nothing in the Chinese licenses *aligned*. The qualifier does in miniature what the throne did in full: it decides which humans are among the four great things. `DISCOVERIES.md` §1 rests on the line reading simply **the human**. Recommended deletion; a different character from 王 and Shalom's own word, so it waits on him.

### Ch 66 · 百谷王 → "rule the hundred valleys"

Two further reasons beyond the gender, both about this chapter specifically.

**The referent is water.** 百谷王 is said of rivers and seas. There is no monarch in the sentence to be male or female, so standing rule 2's *note the seam* does not apply — there is no seam in the Chinese to note, only one we would be making.

**And the chapter is arguing against the throne's own metaphor.** 以其善下之 — the sea rules the valleys *because it is masterful at staying below them*. Every English monarch-word encodes elevation, which is precisely the spatial claim being inverted. 河上公 keeps the water in view: 江海以卑故眾流歸之 — *"rivers and seas, being low, so the many streams come home to them."*

### Ch 67 · 慈 → "tenderness", never "compassion" or "mercy"

**慈 (*cí*) is a parent's love for a child, and the direction is the whole word.** It lives in the pair 孝慈 (*xiào cí*), which this book uses twice — Ch 18's 六親不和，有孝慈 and Ch 19's 絕仁棄義，民復孝慈. The two halves run opposite ways: 孝 is the child's devotion **upward** to the parent, 慈 is the parent's love **downward** to the child. 慈母 (*cí mǔ*) is the ordinary Chinese phrase for a loving mother.

河上公 glosses the first treasure with no abstraction at all: 一曰慈 → **愛百姓若赤子**, *"loving the hundred surnames as if they were **newborn infants**."* 赤子 is a just-born child.

**Why "compassion" fails.** *Com-passion* is suffering-with: a response to another's pain, horizontal, offered to anyone. 慈 is not a response to anything. It is the standing disposition of a parent toward a child, present whether or not the child suffers, and pointed at one's own. The received word also fails the hymn test on contact — *"the sage is full of compassion"* is a sermon — and it carries Buddhist freight (慈悲, *cíbēi*, is the standard Buddhist compound) that postdates this text.

**Why "mercy" is worse.** Mercy is punishment withheld. It requires a judge, a sentence, and a power to inflict it. Nothing in 慈 has any of that.

**Why not simply "love".** English *love* covers eros, liking, charity and God, and carries none of 慈's direction. It is not wrong, and it is the alternate if *tenderness* proves too soft.

**Why "tenderness", including the objection to it.** It is bodily rather than moral — you can point at someone handling an infant tenderly, and you cannot point at compassion. It is not a virtue-word in English, so the naturalistic razor leaves it intact.

The objection is that it sounds passive, in a chapter that claims this treasure **wins wars**. That softness is the point and should not be engineered away. **The chapter's rhetorical structure is: here is the softest thing there is, and it is the most powerful** — so an English word that already sounds strong pre-resolves the paradox the Chinese builds. Ch 78's 柔弱勝剛強 is the same move.

**And the mechanism is not sentimental.** Both commentators explain how tenderness wins, and neither appeals to providence. 王弼: 相慜而不避於難，故勝也 — *"they feel for one another and do not shirk danger, therefore they win."* 河上公: 百姓親附，并心一意 — *"the people draw close and attach, joining hearts into one intent."* Unit cohesion. People who love each other do not run.

*Consequence, and it is owed:* Ch 18 currently renders 孝慈 as **"filial piety"** alone — 慈 is dropped outright — and Ch 19 renders it *"filial piety and love."* Logged in `WORKLIST.md`.

### Ch 67 · 儉 → "frugality", and 且 → "grab at"

**儉 (*jiǎn*)** appears only in this chapter, and it is economic rather than ascetic. 王弼: 節儉愛費，天下不匱 — *"sparing, and careful of expenditure, so the world does not run short."* 河上公 makes it fiscal: 賦儉若取之於己也 — *"taxing sparingly, as if taking from one's own."* Hence **frugality**, and the paradox stands as the Chinese has it: 儉故能廣, *spend little and your reach is wide.*

**且 (*qiě*)** in 今捨慈且勇 is usually read as a bland conjunction, *and*. 王弼 says otherwise, in three characters: 且猶取也 — ***"且 is like 取 (to grab, to take)."*** So the line is not "abandon tenderness and be brave" but **"abandon tenderness and grab at courage."** The grabbing is what makes the triple an indictment rather than a description, and it is why the verdict is 死矣, *that is death*.

### Ch 67 · 成器長 → "chief of the vessels"

器 is locked to **vessel / tool / implement**, and Ch 28 supplies the reading: 樸散則為器 — *"when the uncarved is scattered it becomes vessels."* Vessels are the specialised things, each carved into one use. So 成器長 says the one who refuses to go first becomes what all the specialised things answer to, **because they were never carved into a use of their own.** 王弼: 唯後外其身，為物所歸 — *"only by putting themselves behind and outside do they become what things return to."*

Left visible rather than smoothed: 河上公 reads 成器長 as 得道人 — the chief of those who have attained the Tao, so a leader of people rather than of implements. And **Han Feizi's text reads 事 (affairs) for 器**, which is the older witness. See the Manuscript Notes.

### Ch 67 · 守 → "defend" — a licensed flexion

守 (*shǒu*) is locked to **hold fast to**, paired against 抱 (embrace). In 以守則固 it is plainly military — to hold a position under siege, against 戰 (*zhàn* — to give battle) in the same line. 河上公 writes it out: 以守衛則堅固, *"used in defending the walls, it is solid."* Rendered **"defend with it and you hold firm"**, which keeps *hold* audible without pretending the lock's sense is the one operating.

### Ch 67 · 天將救之 — the strain case, kept open

Already flagged in this file as one of the readings that will not settle: **天將救之，以慈衛之 reads agentive.** 天 is locked to *nature / the natural* and never *Heaven*, but this line has nature **doing** something — rescuing, and then guarding.

河上公 does not soften it either: 天將救助善人，必與慈仁之性 — *"when nature is about to help a good person, it necessarily **gives** them a nature of loving-kindness."* On his reading nature hands over the tenderness, which then does the guarding.

**Rendered "When nature would rescue someone, it guards them with tenderness."** *Would rescue* keeps the conditional 將 and stops short of a promise; *rescue* rather than *save* follows the decision already logged at Ch 27 and Ch 52 — 救 has no soteriology in it. The agency stays where the Chinese puts it, and the strain stays named.

### Ch 67 · 似不肖 → "look like nothing", and 細 → "petty"

**The chapter opens on Laozi, not on the Tao** — see the Manuscript Notes, where the base text's 道 is set aside on six converging arguments.

**似不肖 carries a pun and English can hold it.** 肖 (*xiào*) is *to resemble*; 不肖 (*bù xiào*) is both **not resembling anything** and, as a fixed humility term, **a nobody**. 王弼 takes the first — 肖則失其所以為大矣, *"if it resembled, it would lose what makes it great"* — and 河上公 takes the second, glossing the whole line as 佯愚, *feigning foolishness*. Rendered **"look like nothing"**, which in English means both *resembles nothing* and *appears to be no one*, and which lets the next two lines run as a chain: *look like nothing · look like nothing · looked like something*.

**細 → "petty" here, "slight" at Ch 63 — a licensed flexion.** The Ch 63 decision established that 細 (*xì*) is thread-fineness and must never collapse into 小 (*xiǎo* — small). *Petty* keeps that distinction and fits the subject, which on the settled reading is a **person**: 河上公 glosses 其細 as 唯如小人也，非長者 — *"just like a petty man, not an elder."* *Slight* is right for a task at Ch 63 and wrong for a man here.

**The line, settled:**

> Everyone says I am vast, and look like nothing.
> Only because I am vast do I look like nothing.
> If I looked like something, I would long ago have become petty.

### 敢 → "push / venture", never "dare" — swept 2026-08-20

Full argument in `glossary/gan-敢.md`. The short of it: **"not daring" reads as fear in modern English, and the book says the reverse.** Chapter 73 — 勇於敢則殺，勇於**不敢**則活, *"courage in 敢 kills; courage in **not**-敢 lives"* — makes 不敢 a form of courage, which *not daring* cannot carry.

敢 is a hand with a hunting weapon going after a boar; the *Shuowen* has 進取也, *"to advance and take."* **Appetite, not bravery.** And 不敢 is a politeness formula in classical Chinese — 不敢高攀, *"I could not presume upon your attention"* — the language of declining to help yourself, not of being afraid.

| Chapter | Chinese | was | now |
|---|---|---|---|
| 30 | 不敢以取強 | doesn't **dare** to seize dominance | never **pushes on** to seize dominance |
| 64 | 而不敢為 | and never **dares** to handle them | and never **pushes** them |
| 67 | 不敢為天下先 ×2 | not **daring** to be first in the world | never **pushing** to be first in the world |

**Ch 64 renders 不敢為 as a unit.** *"And never pushes them"* carries 敢為 in one English verb, because *push to handle* will not stand. The chapter's contrast is sharper for it: 輔 (*fǔ*) is the spare timber lashed alongside a cart-wheel to brace it, and a brace holds from the side where a push moves from behind. **Support them; do not push them.**

**On sharing "push" with 推.** Ch 66's 天下樂推 reads *"the world gladly pushes them forward"*, so one English word now covers 推 (*tuī*) and 敢 in adjacent chapters. Accepted deliberately, and it is not the 眾人/俗人 fault: those two collapsed **inside one chapter** and hid a distinction that chapter was drawing. These two sit in neighbouring chapters doing **complementary** work — the same physical act with opposite agents. *They never push themselves forward; the world pushes them forward.* That is what Chapters 66 and 67 jointly argue, and the shared verb states it.

### Ch 73 · 敢 stays "pushing" even where the grammar would allow "pursuit"

`glossary/gan-敢.md` left one question open: Ch 73 holds the book's **only affirmative 敢**, nominalised after 於 in 勇於敢則殺, so the slot wants a noun and *pursuit* — the word closest to the character's boar-hunting picture — becomes grammatically available for the first time.

**Settled as "pushing", on 河上公's gloss.** He reads 敢 here as 有為 (*yǒu wéi* — having-doing, acting): 勇敢**有為**即殺身也, *"brave-daring and **acting** is killing yourself,"* and 勇於不敢**有為**則活其身, *"brave in not-daring-to-act keeps the body alive."* And on 天之所惡 he is blunter still — 惡**有為**也, *"what it hates is **acting**."*

So 敢 in this chapter is not chasing a quarry. It is **pressing forward to act at all**, which is the same forward press rendered *push* at Chapters 30, 64 and 67. *Pursuit* would import a target the chapter does not have, and would split the term across the one chapter that defines it.

**The line reads:** *"Brave in pushing, and you are killed. Brave in not pushing, and you live."* 勇 (*yǒng* — courage) sits on both sides, which is the point: this is not courage against cowardice but two directions of courage.

### Ch 73 · 繟然 → "unhurried", and the net that is not a watcher

**繟然 (*chǎn rán*)** is glossed by 河上公 in two characters — 繟，寬也, *"繟 means wide, loose."* Wang Bi fills in the behaviour: 安而不忘危，未召而謀之 — *"at ease and not forgetting danger; plans before being summoned."* Rendered **"unhurried"**: it keeps the ease and avoids *slack*, which is a fault in English. The looseness echoes 疏 (*shū* — wide-meshed) two lines later, and a reader who hears that is hearing the chapter's shape.

**天網恢恢，疏而不失 must not become surveillance.** 河上公 reads it morally — 司察人善惡，無有所失, *"it watches over human good and evil, and nothing is lost"* — and that reading is the seed of every later use of 天網恢恢 as a slogan about divine justice catching criminals.

**We decline it.** There is no watcher in the Chinese, only a net; 失 (*shī*) is *to lose*, not *to convict*. Rendered **"Nature's net is vast. Its mesh is wide, and nothing slips through."** That is a statement about how consequence works — loosely, at a distance, without haste, and completely — not about anyone keeping a ledger. The naturalistic razor applies here as much as to 天 itself, and the moral reading is exactly the overlay this edition strips.

**天之所惡 stays agentive, and is flagged.** *What nature hates* has nature doing something, as 天將救之 does at Ch 67. Both commentators read it that way and neither softens it. Kept, and named here rather than dissolved — the same strain case, now in a second chapter.

### Ch 73 · 天之道 → "the way of nature"

Established at Ch 9 (*"This is the way of nature"*) and Ch 47, and not a breach of the 道 lock: the lock forbids **the Way** as a rendering of 道 standing alone, where it carries *Logos*. 天之道 is a possessive — nature's way of going about things — and lowercase *way* inside it is ordinary English. Chapters 77, 79 and 81 all carry 天之道 or 天道 and should follow.

### Ch 73 · 惡 → "turns against", and 難 → "finds this hard"

**惡 (*wù*) is to loathe, not to dislike.** The first draft read *"what nature hates"*; the revision tried *dislikes*, which weakens a word this chapter makes lethal — a nature that merely dislikes pressing forward does not get people killed for it. But *hates* gives nature a feeling, which is the agentive strain already flagged at Ch 67's 天將救之.

**Settled as "what nature turns against."** It keeps 惡's full aversive force and makes it an orientation rather than an emotion, which is the naturalistic razor applied to a verb rather than a noun.

**難 (*nán*) is difficult, not unknown.** 是以聖人猶難之 was drafted as *"Even the sage doesn't know"* — a natural reading of the English sequence, since the line follows 孰知其故？ (*"who knows the reason?"*). Both commentators refuse it, and Wang Bi refuses it in four characters:

> 言誰能知天下之所惡意故耶？**其唯聖人。**夫聖人之明，猶難**於勇敢**，況無聖人之明而欲行之也
> *"Who can know the reason for what is hated? **Only the sage.** And the sage's own clarity still finds it difficult **with respect to daring** — how much more someone lacking that clarity who means to act anyway."*

其唯聖人 says the sage **does** know. And both gloss 難 as 難**於勇敢** — difficult *with respect to pressing forward*. The sage's difficulty is about **acting**, not about **knowing**.

**Settled as "Even the sage finds this hard."** The true reading is the harder one: not that everyone is equally in the dark, which would be a comfort, but that the person best equipped to judge when to press forward is the one most reluctant to.

### Ch 68 · 不與 → "does not engage them" — Wang Bi glosses it with 爭

不與 (*bù yǔ*) is two characters and no verb: *does not [go] with.* 與 (*yǔ*) is the accompaniment marker already met at Ch 65's 與物反 (*turns back together with things*) and at Ch 22 and 66's 莫能與之爭 (*no one can contend **with** them*).

**王弼 supplies the missing verb in three characters:** 不與**爭**也 — *"does not contend with them."* So 不與 is the same refusal as 不爭, stated by dropping the verb rather than negating it. Rendered **"does not engage them"** — a military idiom in English, which is the register the whole chapter is in, and which keeps *contend* free for the 不爭之德 three lines later where 爭 actually appears.

河上公 reads the mechanism rather than the word: 不與敵爭而敵**自**服也 — *"does not contend with the enemy, and the enemy submits **of itself**."* 自 (*zì* — self) again, doing the work 自然 does everywhere else in this book.

### Ch 68 · 士 → "warrior", and the term is rendered three ways across the book

**王弼 defines it in this chapter:** 士，卒之帥也 — *"士 is the commander of troops."* So in Ch 68 the word is unambiguously military, and the paradox is built on it: *one masterful as a **warrior** is not **martial**.*

**But 士 is doing different work elsewhere and our English shows it:**

| Chapter | Chinese | rendered |
|---|---|---|
| 15 | 古之善為**士**者 | "The ancient **masters**" |
| 41 | 上**士** · 中**士** · 下**士** | *(undrafted)* |
| 68 | 善為**士**者 | "One masterful as a **warrior**" |

Ch 15 and Ch 68 open on the **identical construction** — 善為士者, *"one masterful at being a 士"* — and take different English. Some spread is legitimate: 士 named the warrior-retainer class of the Zhou and drifted toward the scholar-official, and Ch 41's 上士/中士/下士 hearing the Tao are men of rank rather than soldiers. But Ch 15 also collapses 善為 entirely, and *masters* sits close to a word `CLAUDE.md` forbids for 聖人. Logged in `WORKLIST.md`.

### Ch 68 · 配天 → "matched with nature", and 極 is a ridgepole

**配 (*pèi*)** is the character of pairing — it is the word in 配偶 (*pèi ǒu* — a spouse). Not *accords with*, not *corresponds to*: **matched with**, as one of a pair. 河上公: 能行此者，德**配**天地 — *"one who can do this, their integrity is matched with sky and earth."*

**極 (*jí*)** is the **ridgepole** — the highest beam of a house — and from there the utmost, the pole, the limit. 古之極 is not "the ancient principle" but *the furthest the ancients got*. 河上公: 是乃古之極要道也.

Rendered **"being matched with nature, the utmost the ancients reached."**

### Ch 68 · the fourth clause breaks the pattern, and should

Three clauses negate — 不武, 不怒, 不與 — and the fourth does not: 善用人者，**為之下**, *"one masterful at using people **puts themselves below** them."* Three refusals, then one positive act, and the positive one is the one the chapter names twice more in its closing triple.

王弼 says why it has to be an act rather than an abstention: 用人而不為之下，則力不為用也 — *"use people and fail to put yourself below them, and their strength will not be usable."* The lowness is not modesty. It is the mechanism.

### Ch 69 · 吾寶 is Ch 67's 三寶, and Wang Bi says so

The line is 輕敵幾**喪吾寶** (*qīng dí jī sàng wú bǎo* — "making light of the enemy comes close to losing my treasures"). **王弼 glosses it in four characters: 寳，三寳也** — *"寶 means the three treasures"* — and closes 故曰幾亡吾寶.

Two chapters back, Ch 67: 我有**三寶**，持而保之 — *"I have three treasures. I hold them and keep them safe."* 慈 (*cí* — tenderness), 儉 (*jiǎn* — frugality), 不敢為天下先 (*bù gǎn wéi tiān xià xiān* — never pushing to be first in the world).

**So Ch 69 is Ch 67's treasures worked out on a battlefield, and the chapter's two ends are its first and third treasures.** The opening 吾不敢**為主** (*"I do not push to move first"*) is 不敢**為天下先** in military dress — the third treasure, the refusal to go first. The closing 哀者勝矣 (*"the one who grieves wins"*) is the first, 慈, in its hardest case. 河上公 makes the same connection from the other end: 哀者，**慈**仁 — *"the one who grieves is tender and humane."*

**河上公 reads 寶 as 身 instead** — 寶身也，欺輕敵者近喪身也, *"寶 means the body; one who makes light of the enemy comes near to losing his life."* That is the prudential reading and it is flatter. We follow Wang Bi, on the strength of the verbal echo: 吾寶 two chapters after 我有三寶 is not an accident.

**Rendered "my treasures", plural and undefined**, so a reader who has come through Ch 67 hears it and a reader who has not is not told something Laozi does not say here.

**喪 is *lose*, not *destroy*** — the mourning word, and 王弼 glosses the line with 亡 (*wáng* — to lose, to perish). *Destroy* would make it something an enemy does to you from outside; the chapter says the opposite, that contempt is how you let go of your own tenderness. Rendered **"nearly costs me my treasures"**, which keeps 輕敵 as the agent, as the Chinese grammar has it, without the wrecking.

### Ch 69 · 主 / 客 — the image is jargon, and jargon has to be translated

不敢**為主**，而**為客**. The characters are lovely: 主 (*zhǔ*) is a **lamp with its flame standing on it** — whoever keeps the fire, so whoever's house it is. 客 (*kè*) is 宀 (a roof) over 各 (a foot arriving at a threshold) — whoever comes under someone else's roof.

**Drafted first as "I do not push to be the host. I come as the guest," and changed on Shalom's objection: he could not tell what the saying meant, and neither could any reader who had not been told.** The objection is correct, and the reason is that **主/客 was a term of art**, not an image. Warring States military writing used the pair the way English uses *offense* and *defense*. A reader in 400 BCE heard technical vocabulary; a modern English reader hears a dinner party. **Jargon rendered as image is a mistranslation, not fidelity** — the same argument that sends 天 to *nature* rather than *Heaven*.

The reason first given for keeping the image also fails. It was said to preserve the link to Ch 34's 衣養萬物**而不為主**, the identical construction — but Ch 34's English already reads *master* and *owner*, not *host*. The link was broken at the far end before this chapter was drafted.

**河上公 supplies the sense outright:** 主先也，不敢先舉兵 — *"主 means **first**; he does not push to be the first to raise troops"* — and 客者和而不倡 — *"the 客 harmonises and does not **initiate**."*

Drafted next as *"I do not push to move first. I answer the one who does,"* **and objected to again on the same ground**: the reader has to carry *moves first* across the sentence boundary and supply it, and *answer* is a literary word doing the work of *respond*. Two demands on one short line.

Rendered **"I do not push to move first. I move second."** 河上公's sense, with nothing left to infer — 客 is the second party by definition. *First* is deliberate: it puts the line in the same words as Ch 67's third treasure, 不敢為天下先, *"never pushing to be first in the world."* The lamp and the threshold live in this note.

### Ch 69 · 進寸 / 退尺 — an inch of whose ground?

不敢**進寸**，而**退尺**. Read bare, this is *"advance not an inch, retreat a foot"* — and it sounds like flinching, which is precisely the charge `glossary/gan-敢.md` exists to prevent.

**河上公 says what the two verbs denote, and it is not tactical at all:** 侵**人**境界，利人財寶為**進**；閉門守城為**退** — *"to cross into **another's** borders and take profit from their goods is what **進** means; to shut your gate and hold your own city is what **退** means."*

So 進 is **trespass**, and 退 is **staying home**. Which makes the inch and the foot an argument rather than a ratio of nerve: **an inch of someone else's ground is not worth a foot of your own.** 寸 (*cùn*) is the inch measured at the wrist-pulse and 尺 (*chǐ*) is ten of them; English inch-to-foot is twelve, close enough, and both are body-measures, so the pointing test holds.

Drafted as **"I do not push an inch into another's ground. I give up a foot of my own"** — the English naming what the Chinese leaves implicit, on 河上公's authority, and closing off the purely tactical reading (*give ground to draw the enemy in*, ordinary Sunzi, which the bare characters permit).

**Shortened on 2026-08-24 to "I do not push forward an inch. I give up a foot."** The gain is the line: the long version was the only place in the chapter where the English ran past its Chinese, and it sat badly against the plain second half of the couplet.

**The cost, stated plainly, because it is real.** The bare English loses the *asymmetry* that was the note's whole finding — an inch of **someone else's** ground is not worth a foot of **your own** — and it reopens the tactical reading. Two things hold the line up anyway, neither of them as strong as naming it. *Push forward* carries 敢 (*gǎn* — the forward press to take), so the refusal is of appetite and not of nerve; and *give up* implies what is given up is one's own. The 河上公 gloss now lives in the reader-facing note at `notes/reading.md`, which is where a claim the verse does not make belongs.

### Ch 69 · 行無行 — the one line where the character repeats, and the English can too

The four negations are not all the same shape. Three are verb-無-noun: 攘無臂, 扔無敵, 執無兵. **The first repeats the graph**: 行無行 — but 行 is two words in one character, *xíng* (to go, to march) and *háng* (a row, a rank), and the line uses both. 王弼 settles which is which: 行謂行陳也, *"行 here means 行陣, the battle formation."* If both instances were ranks the line would have no verb at all.

**So all four are verb-無-noun after all**, and the English should say so. Drafted as *"forming ranks where there are no ranks,"* which preserved the repetition at the price of making the first member the odd one out. **Changed 2026-08-24 to "marching where there are no ranks"** — the plainer verb sense, and the four-line parallel becomes true rather than merely claimed. Then *baring / hauling / gripping where there is no X*. Descending length, 4-3-3-3, as in the Chinese.

What is lost is the graph's own echo, which no English can carry without inventing a pun the Chinese is not making.

**攘 and 扔 are Ch 38's pair, negated.** Ch 38: 則**攘臂**而**扔**之 — ritual, when no one answers it, *"bares its arms and hauls them in."* Ch 69 takes the identical gesture and empties it. The aggression makes every motion it knows and each one closes on nothing. 王弼: 言無有與之抗也 — *"there is nothing there to push back against."*

### Ch 69 · 哀 is grief, not compassion — and Ch 31 is the proof

哀 (*āi*) is 口 (a mouth) enclosed in 衣 (a garment): a cry inside mourning clothes. It occurs **twice in the book**, and the other is Ch 31: 殺人之眾，以悲**哀**泣之 … 戰勝以**喪**禮處之 — *"when many have been killed, weep for them with sorrow and grief … a victory in battle is handled by the rites of mourning."* Same subject, same battlefield, same word.

Both commentators pull it toward 慈 (*cí* — tenderness), and they are right about where it leads, but the character is **mourning**, and the claim is stronger for staying there. 王弼 gives the mechanism exactly: 哀者必相惜而不趣利避害，故必勝 — *"those who grieve necessarily cherish one another, and do not chase advantage or dodge harm, and so they must win."* **The grieving army does not calculate.** That is why it wins — not because grief is admirable but because a soldier already in mourning has nothing left to protect.

Rendered **"the one who grieves wins."** Not "the sorrowful", not "the compassionate", not "the one who mourns the war" — the text does not say what the grief is for, and naming it would decide something the Chinese leaves open.

### Ch 69 · 禍莫大於 matches Ch 46, and 兵 puns across the chapter

**禍莫大於輕敵** takes Ch 46's English for the identical formula 禍莫大於不知足: *"there is no greater disaster than …"* Kept parallel deliberately.

**兵 (*bīng*) — two hands holding an axe — opens and closes the chapter.** 用**兵**有言 and 執無**兵**. The graph means both *the weapon* and *the people carrying it*, and the chapter uses one sense at each end: the saying belongs to the people who hold the thing that turns out not to be there.

**Drafted as *"among those who wield weapons there is a saying"* so that the English repeated *weapons* at both ends and the pun survived. Changed 2026-08-24 to "Soldiers have a saying," and the pun is the price.** The objection was register: the long form is stiff and archaic. *Warriors* was proposed and rejected — the word is ennobling in modern English (warrior spirit, the inner warrior) and this chapter deflates the whole enterprise; Ch 31 calls 兵 不祥之器, *instruments of ill omen*. **The honest cost of *soldiers* is twofold**: the English echo at the two ends is gone, and 用兵 is strictly what a *commander* does — 河上公 glosses the line 不敢先舉兵, *does not push to be first to raise troops*, which is a command decision, not a private's. Plainness was judged worth both. Ch 31 renders 兵 as *weapons*; Ch 30 renders 不以兵強天下 as *military force*, which is the looser use and stands.

**執 → "gripping", not "grasping."** 執 is a kneeling figure with the hands manacled — a physical seizing. Ch 29's 執者失之 (*"those who grasp it lose it"*) is the abstract sense and keeps *grasp*; here the hand is on a hilt.

### Ch 69 · whose "I" this is

河上公 flags the voice before anything else: 老子疾時用兵，故託巳設其義也 — *"Laozi loathed the militarism of his age, so he borrowed the first person to set out its meaning."* The 吾 of 吾不敢為主 is a **quoted** I, and 用兵有言 is rendered as an explicit attribution — *"soldiers have a saying"* — so the borrowing is visible on the page. By 吾寶 in the last movement the voice has come back to Laozi's own, which is what makes 吾寶 reach for Ch 67's 我有三寶.

### Ch 69 · 不敢 twice, and the lock makes the Ch 67 link audible

The chapter opens with 敢 (*gǎn*) twice — 吾**不敢**為主 … **不敢**進寸 — and `glossary/gan-敢.md` forbids *dare* outright: in modern English *he did not dare* means *he was afraid*, and Ch 73's 勇於不敢 (*"courage in not-敢"*) requires a word that can be brave. 敢 is a hand with a hunting weapon going after a boar; the *Shuowen* glosses it 進取 — **to advance and take**.

Rendered **"I do not push to move first … I do not push forward an inch."** The repetition is the Chinese's own. And *push* is the verb Ch 67 already uses for the third treasure — *"never pushing to be first in the world"* — so the reader hears the treasure being spent without being told about it, which is the whole argument of the note above.

### 自然 · "the self-so" retired — the lock committed the error it was written to prevent

**Reopened by Shalom, 2026-08-24, on the grounds that the word felt wrong.** It was, and the fault was structural rather than stylistic. Full argument in `glossary/ziran-自然.md` → *Why "the self-so" was retired*. The three findings:

**1 · It was a noun, and both commentators refuse to name a thing.** 王弼 on 道法自然: 自然者，**無稱之言**，窮極之辭也 — *"自然 is a term that **designates nothing**, an expression of the ultimate."* 河上公 on the same line: 道性自然，**無所法也** — *"the Tao's nature is 自然; **there is nothing it takes as a model**."* English *"the self-so"* is a definite noun phrase, and *the* instructs a reader to go looking for a thing. Once they look, 自然 becomes a fifth rung on a ladder whose whole point is that it has four. **That is the same structural error as "Nature," smaller in degree and identical in kind** — and this entry's own case against "Nature" is what convicts it.

**2 · It failed the pointing test.** 河上公 shows what passing looks like, glossing Ch 23: 雲從龍，風從虎，水流濕，火就燥 — *"clouds follow the dragon, wind follows the tiger, water flows toward the damp, fire goes toward the dry."* He points at **water finding the low ground**. Nobody can point at *the self-so*. It is a calque that lives only inside sinology and survived in the verse only because a note explained it.

**3 · The lock had already lost.** Its stated fear was that local renderings would make the term invisible. Three of five lines paraphrased anyway — 17, 51, 64 — and those three read *well*. What the lock preserved was the calque in the two lines it damaged.

**Now locked: 自然 → "of itself / of themselves · so of itself."** *"Self-so" is forbidden.* Only two verse lines moved.

### Ch 25 · 道法自然 → "the Tao models itself on being what it is"

**Shalom's rendering, and the reason it is right is that it declines to be a noun.** 法 (*fǎ* — to take as one's model) stays *models itself on* through all four rungs, so the pattern holds; what changes is that the object stops being a **name** (earth, sky, the Tao) and becomes a **clause**. The dissolution of the regress is made grammatically visible. A ladder that ends in *A is A* has ended, and Wang Bi's 窮極之辭 — *an expression of the ultimate*, what you say when there is nothing further to say — is exactly that shape.

**Both commentators gloss this line with 性** (*xìng* — inherent nature): 王弼's 道不違自然乃得其**性** and 河上公's 道**性**自然. *"Being what it is"* is 性 in plain English, so the essence-flavoured reading is not an import here — it is what the commentary tradition already does with this line.

**The precedent that does not bind it.** `notes/translation.md` (Ch 64, above) rejected *"in being what they truly are"* for 萬物之自然, because *truly* implies a false self to be told apart from a real one. That rejection stands and does not transfer: at Ch 64 the subject is **creatures**, where a true-self/false-self split is a live theological import; at Ch 25 the subject is **the Tao**, of which both commentators already predicate 性.

**The cost, named rather than hidden.** *"Being what it is"* spends the **自**. It names the state but not its provenance, and the whole force of the nose-character is that the being-so comes **from the thing itself and nowhere else**. That loss is accepted at Ch 25 and paid back at the other four, which all carry *itself / themselves*. **The one place 自然 sits in a noun slot is the one place we decline to translate it as a noun** — which is probably the truest thing available to say about the word.

### Ch 23 · 希言自然 → "Speak sparingly, for things go of themselves" — a strain case

A-自然 compressed to four characters, and **English has no predicate slot that fits it.** Recorded as a strain case rather than smoothed.

**"For," not "and."** Shalom's call, and it is the right dependency: *for* makes sparing speech follow **from** things going of themselves, which is 自然 as the **ground**. *And* would make it a consequence, reversing the direction. 河上公 supports the ground reading — 希言者是愛言也，愛言者**自然之道** — *"sparing speech is being sparing with speech; being sparing with speech is the **Tao of 自然**"* — and it is the mechanism of Ch 17, where the ruler says little and the people say *we did this ourselves*.

**What it adds.** The English supplies the consequence clause the Chinese only implies. 王弼 licenses it: 無味不足聽之言，乃是**自然之至言**也 — *"speech that is flavourless and not worth listening to: this is 自然's utmost speech."*

### Ch 25 · two changes made in the working tree, logged after the fact

Found unlogged during the 自然 sweep and recorded now rather than left silent.

- **萬物之母 area — "mother of creation" → "mother of the world."** Correct: the line is 可以為**天下**母, and 天下 (*tiān xià*) is locked to **the world**. *Creation* also imports a created order with a creator behind it, which is the theistic overlay this edition strips.
- **"the aligned human" → "humans."** 域中有四大，而**人**居其一焉 says *humans* with no qualifier. *The aligned human* smuggled in a spiritual grade the Chinese does not have, and made the fourth of the four greats a subset of people rather than people. *(Note that 人 here is itself the editorial reading — every excavated witness reads 王, "king." See `DISCOVERIES.md` §1 and the Ch 25 entry in `notes/manuscript.md`.)*

**The closest rival at Ch 25 — *"the Tao models itself on its own nature"* — was tested and refused, 2026-08-24.** It is the strongest alternative available: 性 (*xìng* — inherent nature) is the word both commentators use of this line, and *its own* carries the 自 lexically. Three things defeat it, and the argument is recorded in full in `glossary/ziran-自然.md` → *The closest rival, and why it was refused*: **nature is 天's word in this edition** (nine occurrences, none from 自然) and 天 is the rung two lines above; **河上公 reaches for 性 to cancel the modelling relation** (無所法也 — *"there is nothing it models itself on"*), not to fill it; and a possessed noun **re-posits a thing**, which is the axis the line was rewritten to clear.

### Ch 16 · 復命 → "returning to what was given" — and the pronoun that changed the subject

Was *"returning to your original nature."* Three faults, in rising order.

**命 (*mìng*) is a command issued to you, not an essence inside you.** The graph is 口 (a mouth) and 卩 (a kneeling figure) under a roof: **a mouth giving an order to someone kneeling.** From there, what is ordered *for* you — an allotment, a span. *Original nature* points inward at what you already are; 命 points outward at what you were handed. The book uses it that way two chapters later: Ch 51's 莫之**命** is rendered *"no one **commands** it."*

**It also spent 天's English.** *Nature* is this edition's word for 天 acting as an agent (9, 47, 59, 67, 73). Ch 16 has no 天 in the line, so the rendering was borrowing from a character that was not there — found while auditing the 自然 revision, `concordance.py --english "nature"`.

**And "your" is not in the Chinese.** The passage is about 萬物: 夫物芸芸，各復歸其根 — *"the things flourish; each returns to its root."* 是謂復命 refers to **that**. The pronoun swung the camera onto the reader and turned a cosmological observation into a personal instruction. This was the worst of the three, because it is invisible — nothing in the English looks wrong.

**Why "given" and not "nature," when both commentators gloss 復命 with 性命.** They do — 王弼: 復命則得**性命**之常; 河上公: 是為**復還性命**. But watch what 河上公 attaches: **使不死也**, *"so that they do not die,"* and on the line above 各復反其根而**更生**也, *"each returns to its root and is **born again**."* The weight is on the **allotted life**, not on a spiritual essence to be recovered. *What was given* keeps the issuing, keeps the life, and takes no pronoun.

**The more literal alternative is "what was allotted,"** which is nearer to 命 and stiffer; *given* was chosen for the verse and the argument recorded here.

### 天 · the split between "sky" and "nature", written down at last

Entry: `glossary/tian-天.md`, 2026-08-24. **The rule was already the practice; it had never been recorded**, and the lock table pointed at `glossary/tiandi-天地.md` — an entry for the *compound* 天地, not for the solo character.

**92 occurrences, the book's most frequent content character** — more than 道. 61 are 天下 (*tiān xià* — the world), 9 are 天地 (*tiān dì* — sky and earth), and **19 stand alone**. Those nineteen split cleanly:

- **8 are a tier in a cosmological series, with 地 (*dì* — earth) beside them → *sky*.** Ch 7 天長地久, Ch 16 王乃天，天乃道, Ch 25 the four greats and the ladder, Ch 39 天得一以清 against 地得一以寧. **地 is physical, so 天 is physical**; a thing and a principle cannot stand in one series.
- **11 take verbs — giving, hating, rescuing, having a way → *nature*.** 天之道 six times (9, 47, 73, 77 ×2, 81), plus 事天 (59), 天將救之 (67), 天之所惡 and 天網 (73), 天道無親 (79). **地 is absent from every one.**

**The split is forced, not chosen.** English has no word with 天's range: *sky* cannot say 天之道, *nature* cannot say 天地. A language that lacks a term's range either splits the word or flattens the text, and flattening is what produced *Heaven*.

**The mechanical form of the rule, for drafting: if 地 is in the line or the series, it is *sky*.** That decides every clear case. The one contested line is 配天 (Ch 68) — see `WORKLIST.md`.

**Chapters 77, 79 and 81 are undrafted and all three carry 天之道 / 天道.** They take **"the way of nature,"** matching Ch 9, 47 and 73. The book writes the formula with and without the particle 之; nothing turns on it and both take one English.

### Ch 70 · 行 — not "execute", and not "do" either

The Source table glosses 行 (*xíng*) as **"execute"** — twice — which is pre-lock English and mechanistic on its face. But the trap underneath is subtler. The obvious repair is *"easy to do"*, and **為 (*wéi* — do / handle) does not occur anywhere in Chapter 70.** Handing 為's locked word to a chapter that has no 為 is precisely what the `--english` direction of the checker exists to catch: a lock is a two-way claim.

**Shalom's choice: "follow."** The AI argued for **"walk"** — 行 is a picture of **a crossroads**, four ways meeting, going on foot, and in a book whose title character 道 (*dào*) is a road (辵 walking + 首 head) the foot metaphor is native rather than imposed. *"Practise"* was rejected by both as abstraction drift.

**The cost of "follow", recorded so it is not rediscovered later.** The word already carries **four other characters** in this manuscript — 從 (*cóng*, ch 21, *"simply follows the Tao"*), 隨 (*suí*, ch 2 and 29), 徒 (*tú*, ch 50), and a bare 之 (ch 14). 行 makes five. It also lands two lines above 則我者 (*"those who pattern themselves on me"*), where *follow* and *pattern oneself on* read as a strong and a weak form of one idea rather than as two different things. Accepted anyway: the line is plainer, and plainness is what 河上公 says the words have (省…約, *pared down… bound tight*).

### Ch 70 · 君 takes "ruler", and the overlap with 王 is deliberate

言有宗，事有君 — *words have an ancestor, affairs have a* 君 (*jūn*). 君 is 尹 (a hand gripping the staff of office) over 口 (mouth): the hand that governs and the mouth that commands.

**Rendered "ruler", which is also 王's (*wáng*) locked word.** Two reasons this is safe and one reason it is right. Safe: 王 does not appear in Chapter 70, so nothing collides on the page, and "ruler" is not on 王's forbidden list — that list forbids *" king"*, not the word we chose. Right: **internal consistency already decided it.** Ch 26's 靜為躁君 stands as *"silence is the ruler of the agitated."* One character, one English.

**"Lord" and "master" were both rejected.** *Lord* fails the hymn test in a chapter already speaking in the first person about being unknown. *Master* is forbidden outright for 聖人 (*shèng rén* — the sage), and 聖人 is in this chapter's last line; the collision would be two lines apart.

### Ch 70 · 宗 and 君 are people, and stay people

The besetting error in this couplet is not a wrong word, it is **abstraction**: 宗 becomes "a principle" and 君 becomes "a governing authority", and the line turns into epistemology. Both characters are persons. 宗 (*zōng*) is 宀 (a roof) over 示 (an altar tablet) — **the ancestral shrine inside the house**, hence lineage, hence ancestor. 河上公 keeps them concrete too: 有宗祖根本 (*"an ancestral root"*) and 事有君臣 (*"affairs have lord and vassal"*).

Held as **"Words have an ancestor. Affairs have a ruler."** Two short sentences, two people, no dash — the couplet's whole force is that the thing behind speech is *someone you could stand in front of*. The pointing test passes; "a principle behind words" does not.

### Ch 70 · 夫唯無知 — left double on purpose

夫唯無知，是以不我知 (*fú wéi wú zhī, shì yǐ bù wǒ zhī*) forks, and the fork changes the chapter's temperature:

- **A — the majority reading.** *Because they have no understanding, they do not understand me.* The crowd is at fault. This is the reading that makes Ch 70 a complaint.
- **B — 河上公's reading.** 是我德之暗，不見於外，窮極微妙，故无知也 — *"this is my 德 (integrity) being unlit, not seen on the outside, reaching the limit of the subtle — therefore there is no knowing."* He attaches 無知 to **the speaker's own hiddenness**. Nothing is on show, so nothing is known. Nobody is at fault.

Reading B is what the chapter's closing image says out loud — the sage **put the sacking on** — and it is what 河上公 says one line earlier as well: 人惡柔弱好剛強也, *"people hate the soft and weak and love the hard and strong."* Not stupidity. **Preference.**

**Rendered so that English holds both:** *"Only because there is no knowing it / do they not know me."* "No knowing it" reads either as *it cannot be known* (B) or as *they do not know* (A). This is honesty over false closure, executed in the verse rather than only in the note. The 夫唯 → **"only because"** construction matches Ch 67's 夫唯大，故似不肖.

### Ch 70 · 被褐而懷玉 — coarse cloth, and the echo with Ch 20

被 (*pī*) is to drape over; 褐 (*hè*) is 衤 (cloth) with a coarse hair-fibre, **a labourer's sacking**; 懷 (*huái*) is 忄 (heart) inside 褱, a garment-graph — something carried **inside the robe, against the chest**.

Note the shape: **a clothing word outside, a clothing word inside, and jade between them.** The line is built out of layers, and that is the argument.

**"Coarse cloth" was chosen over "sacking" for a cross-chapter reason.** Ch 20 renders 而我獨頑似鄙 as *"I alone am stubborn, and look coarse."* 鄙 (*bǐ* — the outskirts, rustic) and 褐 are different characters, but they are the same claim — *this one looks low-born* — and letting the English rhyme makes the 20 ↔ 70 thread audible to a reader who has no Chinese. Logged rather than left to chance.

**"Against the chest", not "at the heart",** even though 懷 carries the 忄 radical. 心 (*xīn* — heart) is locked, and the character is absent from this chapter; a radical is not a licence.


### Ch 70 · 知 stays one word in English, because it is one act in the Chinese

**知 (*zhī*) occurs five times in twelve lines** — 易知, 莫能知, 無知, 不我知, 知我者 — and it is the most concentrated run of the book's central verb anywhere in the text (47 chapters carry it). A first pass rendered the first two as *"understand"* and the last three as *"know"*, which is the natural English reflex: you understand a sentence, you know a person.

**Reverted to "know" throughout, and the reason is structural rather than cosmetic.** The couplet in the middle — 言有宗，事有君, *words have ancestors, affairs have rulers* — exists to say that the words come from someone. So comprehending the sentences and knowing the speaker are **not two acts**. That is why one character does both jobs, and why 不我知 (*"they do not know me"*) is offered as the *explanation* for 莫能行 (*"none can follow"*). Split the English and the chapter appears to describe two separate failures — they missed the argument, and separately they missed the man. The Chinese names one failure five times.

**Two supports.** *"Easy to know"* is idiomatic English about **people** ("she's easy to know"); applied to words it is faintly odd, and the oddness quietly makes the words person-like — which is what 言有宗 then says outright. And **Chapter 71 is built entirely out of 知** (知不知，上；不知知，病 — *"knowing not-knowing is highest; not knowing yet knowing is sickness"*). 70 and 71 are adjacent on purpose; an *understand* in 70 breaks the hinge before 71 is drafted.

### Ch 70 · 被 and 懷 are two different verbs, and the line is made of the difference

A pass through the last line rendered both as *wear*: *"wears coarse cloth, but wears jade against their chest."* The repetition flattens the only architecture the line has.

被 (*pī*) is **draped over the outside**. 懷 (*huái*) is 忄 (heart) inside 褱, a garment-graph — **held within the robe, at the breast**. A cloth word outside, a cloth word inside, and the jade between them. 河上公 reads it exactly so: 被褐者薄外，懷玉者厚内 — *"wearing coarse cloth is thin outside; holding jade is thick within."* **懷 takes a verb of carrying**, not of wearing.

*(A smaller open question in the same line: 而 is held as **"but."** 河上公's 薄外／厚内 treats the two halves as a **matched pair** describing one person rather than as a contradiction, which argues faintly for "and". "But" was kept for the reader's ear.)*

### Ch 71 · 不知知 renders toward the mouth, not the mind

**Every standard English reads the second half as self-deception** — *"not to know, yet think you know."* We read it as **profession**: *"not to know and to claim you know."* Three supports, in the tie-breaking order.

**The graph.** 知 (*zhī*) is 矢 (*shǐ* — an arrow) over 口 (*kǒu* — a mouth): speech that flies straight to the target. The word has a mouth in it before it has a mind in it.

**The commentary.** 河上公 inserts 言 (*yán* — to say) into *both* halves, which he did not have to do: 知道**言**不知，是乃德之上 — *"to know the Tao and **say** you do not know: this is the height of integrity"* — and 不知道**言**知，是乃德之病, *"not to know the Tao and **say** you know: this is integrity's disease."* On his reading the chapter is not about the limits of knowledge at all. It is about the gap between what you hold and what you profess.

**Internal consistency.** Ch 56 opens 知者不言，言者不知 — *those who know do not speak; those who speak do not know* — which is this chapter's first line with the 言 already in it. And Ch 70 ends with the sage carrying jade **against the chest** under coarse cloth. 河上公 closes his note on 71 with the same gesture and nearly the same verb: 夫聖人**懷**通逹之知，託於不知者 — *"the sage **carries** penetrating knowledge against the breast, and lodges it in not-knowing."* 懷 is the character Ch 70 ends on. **70 and 71 are one gesture, and the commentator says so.**

*The interior reading is not wrong and is not erased — it is named in the chapter's `## Notes`. English forces a choice here that the Chinese does not force; we chose the reading the evidence favors and the one a reader is least likely to already have.*

### Ch 71 · "sick of the sickness" — one English word for one Chinese word

**病病 is the chapter's whole engine**: the first 病 verbal, the second nominal. The literal gloss in the source table says *"recognizing the disease as a disease"* — cool, diagnostic, and wrong about the verb. 河上公 supplies the sense: 夫唯能**病苦**衆人有強知之病 — *"only because they are **pained and distressed by** the crowd having the disease of forced knowing."* 病苦 is to suffer over, not to classify.

**English "sick of" is the only construction that keeps one word doing both jobs**, and it happens to carry exactly 病苦's sense of being wearied and pained by a thing. **Cost, logged:** *"sick of"* can read as impatient — sick of your nagging. The context defuses most of it, and the alternative (*troubled by the trouble*, *pained by the sickness*) either breaks the doubling or loses the body. 病 is 疒 (*nè* — a person lying against a bed-plank) over a phonetic; *Shuowen* has it as 疾加也, illness intensified. There is a body in this word and the English must keep it.

**Do not vary the repetition — but distinguish two kinds of it.** 病 falls seven times in four lines. Every instinct of English prose style wants to alternate *sickness / ailment / affliction*; the Chinese hammers one syllable, and the hammering is the argument. **That lexical repetition is kept entire.**

**The structural repetition is not.** The last line is 聖人不病，以其病病，是以不病 — literally **A, because B, therefore A.** Classical Chinese closes a period by restating its opening; English carries the conclusion inside the causal clause already, so *"the sage is not sick because they are sick of the sickness"* says the whole line. **Shalom cut the trailing 是以不病 (2026-08-24)** as an editorial redundancy, and it is one: nothing in the sense is lost, and the cut leaves the last two lines in exact chiasmus — *sick of the sickness → not sick*, then *not sick → sick of the sickness* — which is the shape the Chinese has underneath the padding.

*Recorded because it is a **cut**, not a rendering. 河上公 lemmatizes both halves, so the doubled text was in place by the Han and this is our edition's decision, not a witness's.*

**And 不病 stays flat.** A pass rendered 是以不病 as *"do you become no longer sick"* — six English words for two characters, carrying a **recovery arc** the Chinese does not have. 河上公 reads the line the other way: 是以**不自病**也, *"therefore they do not sicken themselves."* He adds 自 (*zì* — self). The cure is **not contracting it**, not getting over it, and "no longer" points backward at an illness the commentary says was never caught. Held at *"are you not sick"*, which also keeps the last two lines in exact chiasmus.

### Ch 72 · 大威 is not a bigger stick

**The standard English makes this line a threat**, and our own source table's literal gloss invites it: 民不畏威，則大威至 → *"when the people do not fear authority, then great authority arrives."* Read that way the chapter opens by telling a ruler that a larger power is waiting to enforce what theirs cannot — which is precisely the theology-of-office this edition exists to strip out.

**Both commentators read it as collapse.** 王弼: 民不能堪其威，則上下大潰矣，天誅將至 — *"the people cannot bear that dread; then high and low collapse utterly, and the reckoning of nature is coming."* 河上公, flatly: 威害也…大害至，謂死亡也 — *"威 means harm… the great harm arrives, meaning death."* Neither has anything arriving to enforce the ruler's will. **What arrives when your dread stops working is the end of the arrangement.**

**The English gives the first 威 an owner and leaves the second unowned** — *"when the people no longer fear **your** dread, **the** great dread arrives"* — because that asymmetry is the sentence. One dread belongs to somebody. The other does not belong to anyone, which is why it cannot be used.

**One character, two referents — so the English splits the word.** 威 (*wēi*) is 戌 (a great axe) over 女: the fear a figure commands and the figure commanding it, in one word. 王弼 glosses the ruler's 威 as **威權** (*wēiquán* — awe-power, **authority**) and the second as **天誅** (nature's reckoning). The Chinese runs one word through both slots and the shock is that the two are *not the same thing*; English cannot hold that in one word without asserting something false, so it renders *authority* / *the great collapse* and lets the difference be audible. The noun comes from 王弼's own gloss: 上下**大潰**矣, where 潰 (*kuì*) is a **dyke bursting**. A collapse answers to nobody, which is exactly the property the second 威 has and the first does not.

*A draft that kept the repetition — "when the people no longer fear **your dread**, the great dread arrives" — was killed by Shalom. You fear a thing; dread is the feeling. 畏威 works in Chinese and "fear dread" does not work in English, and the repetition was not worth the sentence. Also rejected, from the other direction: **"true authority arises"**, which makes 大威 a legitimate power replacing an illegitimate one. That is a larger inversion than the threat-reading it was meant to fix, and it is what the hymn test is for — the line would sit very comfortably in a sermon.* **Overlay watch:** 王弼's 天誅 is 天 (*tiān* — sky, nature) plus 誅 (*zhū* — to condemn, to execute) — **nature's reckoning**, not divine punishment. The pull toward "Heaven's judgment" is strong here and it is strongest in the commentary, where no checker is looking.

### Ch 72 · 厭 is a pun, and English happens to have the same one

厭 (*yàn* / *yā*) is 甘 (sweet) over 肉 (meat) under 厂 (a cliff): **sated with rich food**, hence *fed up with, sick of*; and by way of the cliff-graph it is the ancestor of 壓 (*yā* — to press down, to crush). One character, both senses live.

夫唯不厭，是以不厭 uses both in six characters: *do not press them down, and they will not be fed up with you.* 王弼 spells the second one out — 不自厭，是以天下莫之厭, *"does not make themselves loathsome, therefore no one in the world loathes them."*

**"Oppress" carries the pressing half exactly** — *ob-premere*, to press against — and it is the plainer, more pointable word. But the second 厭 is **not pressure, it is loathing**, and 王弼 spells it out: 不自厭，是以天下**莫之厭**, *"therefore no one in the world loathes them."* So the two halves take two Englishes: *when you do not oppress them, they will not tire of you.*

**Ch 66 fixes the second half** and the two chapters are twins: 是以天下樂推而不厭 → *"the world gladly pushes them forward and never tires of them"*, sitting directly under 聖人處上而民不重 — *the sage stands above and the people are not weighed down.* Ch 53's 厭飲食 → *"gorged on food and drink"* holds the root sense of the graph.

**"When", not "because" — and the cost is 唯.** Chs 2, 8 and 22 all render 夫唯…是以 as *"Because…"*, and a fourth is a tic; Shalom moved this one to *"when"*. What that drops is 唯 (*wéi*), 隹 (a short-tailed bird) beside 口 (mouth) — **solely, and nothing else**. 河上公 will not even leave it at one exclusive: he writes 夫唯**獨**不厭精神之人, stacking 獨 (*dú* — alone) on top of 唯. Without *only*, the line can be heard as a prediction rather than a mechanism. Logged as a known loss rather than repaired, because *"only when you do not oppress them do they not tire of you"* buys 唯 back at the price of a clanking double-negative inversion, and this chapter's other lines are plain.

*A draft rendered both with "weary" — "only when you do not weary them do they not weary of you" — on the grounds that one English word should do the work of one Chinese character. It bought the doubling at the price of "weary what gives them life", which is not a thing English does to a livelihood. **Two accurate words beat one clever one.***

**Second chapter running on the same device.** Ch 71: 夫唯病病，是以不病. Ch 72: 夫唯不厭，是以不厭. In both, a doubled character does two jobs and the English survives only by finding one word with two senses — *sick of the sickness*, *weary of you*. Worth watching for in 73–81 rather than being surprised by it again.

### Ch 72 · "loves themselves and does not hold themselves precious"

自愛，不自貴 turns on a distinction English usually blurs. 貴 (*guì*) sits on 貝, a **cowrie shell** — it means *costly* before it means *honoured*, and ch 70 already renders it *precious*. **You can love a thing without pricing it.** That is the line, and it is the answer to the chapter's first half: a ruler who has set their own price high has to keep collecting on it, which is what the crowding is.

*Not "exalt" — ch 3 already spends that word on 尚 (尚賢, "exalting the exceptional"). 河上公 splits the pair cleanly: 自愛其身以保精氣也 (bodily — preserving vital essence and energy) against 不自貴高榮名於世 (social — glory and fame).*

**故去彼取此 names its axis.** Ch 12 (*"rejects the hungry gaze, chooses gut wisdom"*) and ch 38 (*"rejects surfaces and embraces life's thickness"*) both fill in the referents. A draft here left *that* and *this* bare instead, on the grounds that the referents sit in the line immediately above and 河上公 spells them out: 去彼**自見自貴**，取此**自知自愛**. Shalom killed it for a structural reason: the preceding line carries **four** items, and English *that/this* cannot sort four things into two pairs.

**The characters supply the sorting principle, and it is spatial.** 彼 (*bǐ*) is 彳 (a step) beside 皮 — *yonder, over there*. 此 (*cǐ*) is *this, here*. And the axis is exactly the right one: 自見 (display) and 自貴 (self-pricing) **require an audience** — they are out there. 自知 (knowing) and 自愛 (loving) require nobody — they are here. Hence *"they let go of what is out there and take what is here."*

Keeping **here** also holds the chapter inside the 以此 thread that closes chapters 21, 54 and 57 — *how do I know it is so? By this* — which a bare "this" was carrying but not communicating. See `DISCOVERIES.md` §2.

### Ch 74 · "who would still push?" — the 敢 lock pays for itself

孰敢 (*shú gǎn*) is "who would dare?" in every translation there is, and we cannot have it: 敢 is locked to **push / venture**, the forward press to take (`glossary/gan-敢.md`). The reason is one page back. Ch 73 opens 勇於敢則殺 — *"bravery in pushing gets you killed"* — and Ch 74 closes its threat with the same 敢 and the same 殺. Read with the lock, the two chapters lock together: the ruler in 74 promises to kill the ones who push, and 73 has just said that pushing kills them anyway. **The threat is redundant, and that is the joke.** "Who would dare" hides it, because *dare* is a nerve and 敢 is an appetite.

**"Suppose", not "if you make".** 若使民常畏死 is a hypothetical the chapter exists to demolish, and a flat *"if you make the people fear death"* reads as a recommendation. 河上公 is unambiguous that it is a rebuke: 老子傷時王不先道德化之而先刑罰 — *"Laozi grieves that the rulers of his time did not first transform them with the Tao and integrity, but put punishment first."* The whole second stanza is a seduction, and the third takes the axe out of the ruler's hand.

**畏 and 懼 are two different fears, and the line is built on the difference.** 畏 (*wèi*) is a spirit-figure holding a staff — standing dread of a power that can strike. 懼 (*jù*) is 忄 (heart) beside 瞿, the wide stare of a startled bird — the jolt. So 民不畏死，奈何以死懼之 is *"when the people carry no dread of death, how will you startle them with it?"* We render **fear** and **frighten**, which keeps the state-and-act distinction in ordinary English. And note Ch 72 opens on the same verb and the same construction — 民不畏威, *"when the people no longer fear authority"* — with 威 (*wēi* — authority) being 畏 with 女 beneath it. **72 and 74 are the same sentence twice**: first they stop dreading your power, then they stop dreading death, and after that you have nothing left to hold over them.

**"master carpenter", lowercase — and 斫 belongs in the third line, not the second.** 匠 (*jiàng*) is 斤, an axe, inside 匚, a tool-chest — the graph is literally an axe put away in its box, which is the chapter's argument in one character. We keep the craft concrete ("carve", "cut their own hand") rather than abstracting to *"presume to do the work of a master"*, because the injury at the end is a real blade in a real hand.

**Where the carving sits is a real choice, and Shalom's placement is right.** 斫 (*zhuó*) appears in **both** lines of the Chinese — 是謂代大匠**斫** / 夫代大匠**斫** — and no English version we tried could carry it twice without clanking. Drafts put it in the second line (*"to take the master carpenter's place at the carving"*); the settled text puts it in the third:

> To take their place is to take the place of the master carpenter.
> Of those who **carve** in place of the master carpenter,
> few fail to cut their own hand.

**The gain is that the verb and the wound now land in one breath.** *Carve* and *cut* sit two lines apart in the drafts and adjacent here, so the blade that does the work is the blade that does the damage — which is the chapter's entire mechanism. It also lets the second line be a clean equation, place for place, which is what 是謂 (*shì wèi* — "this is called") asks for.

**And the tripled 代 survives.** 代 appears three times (代司殺者、代大匠、代大匠); the English answers with *take their place · take the place of · in place of* — the same idiom three times, varied enough that English tolerates what Chinese states flat. Both lines also end on *the master carpenter*, an echo the Chinese has and a draft with possessives ("the master carpenter's place") did not. 希 (*xī*) → **few**: 希有不傷其手 is a double negative and English can hold it, *"few fail to cut their own hand."*

### Ch 74 · a register correction, and what caused it

A first draft of this chapter read *"whoever goes crooked"*, *"one whose work is the killing"*, and *"the master carpenter at the hewing"* — three archaisms in twelve lines. Shalom flagged all three, 2026-08-25. **The cause is worth logging because it will recur:** each phrase was built to satisfy a lock or dodge an overlay, and solving them one at a time let the English drift into costume. A lock constrains the *word*; it does not license a sentence no one would say. **When three lines in a row start sounding old, the locks are being obeyed and the poetry is being lost.**

- 為奇者 → **"whoever steps out of line"**, not "criminals" and not "goes crooked". The semantic call holds (see the chapter's `## Notes` — 罪 was available and unused, and 奇 is a military virtue in ch 57), but plain English carries it. *"Out of line"* even keeps the 正/奇 geometry.
- 司殺者 → **"one who does the killing"**, not "executioner" and not "whose work is the killing". Again the call holds and only the register changed.
- 斫 → **"carving"**, not "hewing". Here the call itself changed, and Shalom was right: see `notes/reading.md` on 大制不割.

**And the opening line goes plain — with "try" doing the work.** 民不畏死，奈何以死懼之 → *"why try to frighten them with death?"* A draft had *"how will you frighten them"*, reaching for the futility in 奈何 (*nài hé*) with syntax. **The one word that carries it is *try*.** Put the attempt in the verb and the failure becomes structural rather than rhetorical: the ruler is not being asked *why they would want to*, but told that the attempt is the thing that does not work. Shalom's edit, 2026-08-25.

**"When", not "if"** — 民不畏死 carries no conditional marker, while the next line does (若使), and that contrast is the chapter's spine: a fact, then a fantasy.

**"The people", not bare "people" — and this one is a hold, not a decision.** A draft went bare. The evidence against: 民 (*mín*) renders *"the people"* in all 32 of its lines across the manuscript, and Ch 72 opens on the identical frame 民不畏威 — *"when the people no longer fear authority"* — two chapters before 74's 民不畏死, a rhyme the bare noun silences. The evidence for: 河上公 reads this very line at both registers, and *"the people"* bolts it to statecraft where *"people"* lets a reader hear it about themselves. **Shalom restored the article and parked the question for a decision across the whole book**, which is the right size for it — see `WORKLIST.md` → *民 and 人*. Ch 74 is not a precedent either way.

**"frighten", not "threaten".** 懼 (*jù*) is causative — *to cause fear* — and it pairs in one line with 畏 (*wèi*), the fear itself. *Fear / frighten* keeps the pair audible; *threaten* is a different verb doing a different job.

### Ch 75 · 有為 is the book's only positive naming of 為, and "action" is the one word it cannot take

有為 (*yǒu wéi* — "having doing") appears **once in eighty-one chapters**, in Ch 75. Every other 為-teaching in the book is framed as a negation: 無為 (*wúwéi* — non-doing), 為無為 (*wéi wúwéi*, 63), 為而不恃 (*wéi ér bù shì*, 2, 51, 77). This is the single line where Laozi states the positive, and he states it as a diagnosis of ungovernability.

**"Action" is barred here, and the bar is the lock working.** The 無為 entry forbids "non-action" because it abstracts 為 (*wéi* — to do / to handle) into a category. Ch 75 is the one place the pair is visible in a single chapter — 有為 in the second charge, 無以生為 (*wú yǐ shēng wéi* — "make no doing of living") in the closing couplet — so importing the forbidden English there breaks the bracket precisely where a reader could otherwise see it.

**The smoother English is barred too, for a different reason.** *Meddling*, *interference*, *officiousness* all read better and all judge the **quality** of the doing. The chapter makes no such distinction: the charge is not that rulers do the wrong things, it is that they do.

**What is left is to read 有 (*yǒu* — having) as persistence: "will not stop doing."** A first draft rendered it literally as "have their doing" and defended the awkwardness as load-bearing. It was not — it read as a typo. **The general lesson: strangeness in the English is only earned when it does work the plain line cannot do.** Here the plain line keeps the word *doing*, keeps the audible negative of *non-doing*, and simply reads. Caught by Shalom, 2026-08-25.

### Ch 75 · 上 is kept vertical for one specific chapter, not for a general doctrine

其上 (*qí shàng* — those above them) → **"those over them."** The vertical is kept because **ch 66 pairs the identical two characters**: 是以聖人處上而民不重 (*shì yǐ shèng rén chǔ shàng ér mín bù zhòng* — "so the sage dwells above and the people are not weighed down"). Ch 75 is its negative — same position over the same 民 (*mín* — the people), and the people starve. **"Over" rather than "above" because 不重 (*bù zhòng*) is measuring weight**: "above" is altitude, "over" is pressure.

**But do not generalize this into a doctrine that low is strong.** 上/下 carries no fixed valuation in this book. Ch 39: 高以下為基 (*gāo yǐ xià wéi jī* — "the high takes the low as its foundation") — the high is *rooted* in the low, not inferior to it. Ch 76: 柔弱處上 (*róu ruò chǔ shàng* — "the supple and weak occupy above") — the yielding is on top. And in ch 8, 38, 41 and 71, 上 means simply *highest/best*, with no spatial claim at all. Read the pairing in each chapter; there is no rule to apply.

### Ch 75 · the three-part 是以 refrain, dropped — the same call already made at ch 71

Ch 75 closes each of its three charges by repeating the word it opened on: 民之飢，以其上食稅之多，**是以飢** (*mín zhī jī … shì yǐ jī*).

**Distribution, corrected.** The loose shape X…是以X appears in ch 38, 70, 71, 72 and 75. The **full three-part form** — statement, a causal clause in 以其 (*yǐ qí* — because their), then a verbatim restatement — appears in only **two**: ch 71's 聖人不病，以其病病，是以不病, and ch 75's three charges. *(A first pass claimed the figure was unique to ch 75. The search behind it required a 之 in the clause and missed ch 71. Corrected 2026-08-26 — and the correction matters, because it converts a novel decision into a consistent one.)*

**Shalom cut ch 71's trailing 是以不病 on 2026-08-24** as editorial redundancy; ch 75's three go the same way on 2026-08-25. **The principle, now applying to both:** 以 (*yǐ* — because) and 是以 (therefore) in one breath is incantation, and classical Chinese wears it as liturgy. **English hears deliberate redundancy as stammering unless the register is already sermonic** — and sermonic is the register this edition exists to refuse. A figure that reads as ritual in the source reads as a lost place in the English, so rendering it faithfully would be an infidelity.

**But a dropped figure should be relocated, not merely lost, and there are three ways.** Ch 71 **recovers** it: cutting the tail leaves the last two lines in exact chiasmus, which is the shape underneath the padding. Ch 72 **folds** it — 夫唯不厭，是以不厭 becomes one sentence because 厭 carries two senses. Ch 75 **moves** it: the three unvaried openings, *"The people … / because those over them …"*, carry the hammering as anaphora at the stanza instead of the line. **The test before cutting any device: find where else in the English it can live.**

### Ch 75 · 賢 against 貴 — merit against standing, and why "noble" cannot be used

是賢於貴生 (*shì xián yú guì shēng*) → **"are worthier than those who hold life precious."**

**The line judges a person.** 無以生為者 carries 者 (*zhě* — the one who), and 河上公 glosses the whole payoff as a person's condition: 天子不得臣，諸侯不得使 — *"the Son of Heaven cannot make them a subject; the feudal lords cannot employ them."* A draft rendered it *"value life more than those who prize it"* and thereby turned a claim about persons into a theory of value. Caught by Shalom, 2026-08-26.

**Correction to an earlier entry.** This file previously held that ch 3's 不尚賢 (*bù shàng xián* — "do not exalt the worthy") barred *worthy* as an English for 賢. That was overstated: **ch 75 uses 賢 approvingly**, so the book holds both. Ch 3 forbids *exalting* worth, not worth itself, and refusing the word would smooth a tension the text has. The standing rule against ranking *tribes of people* (see below) survives; the blanket ban on the word does not.

**The real bar is on "noble", and it is structural.** 貴 (*guì*) means precious **and** high-ranked — 貴族 (*guì zú*) is the aristocracy — and in this sentence 貴 is the losing term. Render 賢 as *nobler* and 貴's own English stands on both sides of the comparison, erasing it. The two characters point opposite ways: **貴 is worth by standing; 賢 is worth by capacity** — *Shuowen* defines it 多才也 (*duō cái yě* — "having much ability"), and though 賢 carries 貝 (*bèi* — cowrie, shell money) it is the merit word, not the rank word. The chapter's last move prefers merit to rank, and "noble" means both at once, so it cannot carry a preference between them.

**And there is a tonal cost on top.** Ch 75 indicts rulers for eating the people and keeping their own lives rich. Closing it on *nobler* returns the argument in the aristocracy's vocabulary, three lines after the charge.

### Ch 75 · 無以生為 — render the 以, don't paraphrase it

無以生為 (*wú yǐ shēng wéi*) → **"don't use living for doing."** 以 (*yǐ*) is genuinely *use / by means of*, so the clause reads *"have nothing by which living is made a doing"* — and rendering the grammar beats paraphrasing it, because **it puts the word *doing* in the couplet as well as in the second stanza**, which is the only way the bracket 有為 (*yǒu wéi* — having doing) … 無以生為 becomes audible in English. Earlier drafts reached for noun phrases (*"a life not made into a doing"*) and lost it. Shalom's phrasing, 2026-08-25.

河上公 reached the same reading by inserting a character the text does not have: 無以生為**務**者 (*wù* — business, task), *"one who does not make living their business."* And he alone says what it buys — 天子不得臣，諸侯不得使, *"the Son of Heaven cannot make them a subject, the feudal lords cannot employ them."* **The payoff of not making a project of your living is that you cannot be used.** Left implicit in our English, as it is in the base text.

### Ch 75 · 貴生 and the ch 72 echo

貴生 (*guì shēng*) → **"a life held precious."** 貴 (*guì* — to prize, to hold dear) is the same character as ch 72's 自愛，不自貴 (*zì ài, bù zì guì*), rendered there as *"loves themselves and does not hold themselves precious."* Keeping one English across the two makes the thread audible: ch 72 tells you not to hold **yourself** precious, and ch 75 names holding your **life** precious as the reason the people go hungry. See the 72 → 74 → 75 thread in `notes/reading.md`.

### Ch 76 · 強 stays *strong* in all five places — the chapter is an ambush on the word

強 (*qiáng* — strong) appears five times here: 堅強 twice (of a corpse, and of the company of death), then 兵強 (a strong army), 木強 (a strong tree), 強大 (the strong and big). The standard English softens the corpse to *stiff* or *rigid* and keeps *strong* only for the army. That is exactly backwards. **The chapter works by using the admiring word for rigor mortis first**, so that by the time the army arrives the word has already been spent. Translate it consistently and the argument runs; vary it and the chapter becomes a mood about flexibility.

**Corrected 2026-08-26.** An earlier version of this note extended the claim to 弱 as well, arguing that 柔弱 must stay *soft and weak* because "the provocation is that the text calls the living state weak." That was wrong, and it put **weak** into the verse to defend a provocation the text does not make. There is one ambush here and it is on 強. 弱 now reads **yielding** — see `glossary/ruo-弱.md`, where the commentators settle it. Caught by Shalom.

### Ch 76 · 徒 is a band on foot, not a discipleship

徒 (*tú*) is 辵 (walking) over 土 (earth) — to go on foot, hence a foot-soldier, hence a band or cohort. 死之徒 / 生之徒 is *the company that death keeps* and *the company life keeps*, not a following in any devotional sense. "Disciples" is a missionary word and fails the hymn test on contact. **followers**, matching the already-drafted Ch 50 (生之徒，十有三).

### Ch 76 · 處下 is the losing position here, and only here

強大處下，柔弱處上 — the strong and big **dwell below**, the soft and weak **dwell above**. Everywhere else in the book 處下 is the winning move: water dwells where the crowd will not go (ch 8), the great state takes the lower place (ch 61), the sea is king of the valleys because it lies beneath them (ch 66). Here low is where the doomed end up. The reason is that this is a **tree**, not a landscape — 王弼 says so in four characters, 木之本也, *"it is the tree's trunk"*, and 枝條是也, *"these are the branches."* We keep the verb *dwell* so the collision with ch 8 and ch 66 stays visible on the page rather than being smoothed away. See `notes/reading.md`.

### Ch 76 · 人 rendered as *the body* — a word added, and why

人之生也柔弱 has 人 (*rén* — a person), not 身 (*shēn* — body), and we render it **the body**. This adds a word the Chinese does not have, so it is a call and not a reading.

The reason is that English "a person is soft and weak" does not stay neutral — it lands as **temperament**, which is the one thing the line is not about. What the line predicates is flesh. 河上公 reads it physiologically and leaves no room: alive, 人生含和氣抱精神故柔弱也, *"a living person holds harmonious energy and embraces the vital spirit, and is therefore soft and weak"*; dead, 人死和氣竭精神亡, *"the harmonious energy exhausted, the vital spirit gone."* The observable is rigor mortis. The parallel line's subject is 萬物草木 (the countless things, grass and trees) — bodies whose bodies are simply themselves — so *the body* keeps the two halves doing the same kind of work.

Caught by Shalom, 2026-08-26. The first draft rendered *a person* while the accompanying note argued the chapter is physical throughout, which is the argument being made in the notes and dropped in the verse.

### 弱 locked as *yielding* — and the one line it cost

Settled 2026-08-26 at Ch 76, on Shalom's call. Full argument in `glossary/ruo-弱.md`; the short version is that no classical gloss in this repository reads 弱 as deficiency. 王弼 on ch 40: 柔弱同通不可窮極, *"soft and 弱 alike pass through; they cannot be exhausted."* 河上公 on ch 78: 水能滅火, *"water can put out fire."* Water is not weak.

**The lock forced a four-word table**, because Ch 78 splits the compound and will not let 柔 and 弱 share an English word: 弱之勝強，柔之勝剛. So 柔 → **soft**, 剛 → **hard**, 弱 → **yielding**, 強 → **strong**.

**Swept:** ch 36 (柔弱勝剛強 → *the soft and yielding overcome the hard and strong*), ch 55 (骨弱 → *their bones are yielding*, replacing *weak*, which read as pathology in a newborn), ch 76 (three lines). **Ch 40 needed no change** — 弱者道之用 already read *"Yielding is the Tao's use,"* which is how the error was found: the lock ratified the line the manuscript already had, against the note that was arguing to overwrite it.

**Not swept, and it is the real cost: ch 52.** 守柔曰強 currently reads *"To stay with the yielding is strength."* That line renders **柔**, not 弱, and under the four-word table it cannot keep *yielding*. Held for Shalom rather than swapped, because it is a rewrite and not a term-substitution.

**Two lines keep *weaken*, on grammar.** ch 3 弱其志 and ch 36 將欲弱之 use 弱 transitively, with an object, meaning *to make weak*. A stance word cannot take an object. The split is marked in the Chinese, so it is checkable rather than a matter of taste.

### Ch 77 · 張弓 rendered as *stringing a bow*, not drawing one

河上公 glosses the simile 言張弓和調之如是乃可用 — *"stringing the bow and tuning it into balance, thus, and then it can be used."* 和調 (*hé tiáo* — harmonize and tune) is what a bowyer does, not what an archer does, and it decides the next two lines: 高者抑之，下者舉之 is the upper limb pressed down and the lower lifted so the string can be seated, not a sight being walked onto a target. 王弼 names the mechanism directly — 以均天下, *"to level the world"* — and 均 (*jūn* — to make even) is the chapter.

The cost of *drawing* is the whole point: aim makes it a chapter about hitting something. Bracing makes it a chapter about tension brought into balance, which is what 損有餘而補不足 then describes. **Retrofit applied:** `glossary/tian-天.md` quoted this line as "drawing a bow" and has been corrected.

### Ch 77 · 奉 rendered as *offer up*, in both directions

奉 (*fèng*) is 廾 (two raised hands) holding something aloft — the verb for giving upward, to a superior. English translations soften it to *serve* or *sacrifice*, and the political charge goes out of the line. 河上公 does not soften it: 世俗之人損貧以奉富，奪弱以益強 — *"worldly people diminish the poor to offer up to the rich, seize from the yielding to increase the strong."*

**One English verb across both occurrences**, because the reversal is the rhetoric: the world offers up to those who have too much (損不足以奉有餘), and the one who holds the Tao offers up to the world (有餘以奉天下). *Pay tribute* is more accurate to the first and impossible in the second; *offer up* carries the raised hands in both.

### Ch 77 · 補 rendered as *mends*

補 (*bǔ*) is 衤 (garment) + 甫 — to patch cloth. Not "supplement," which is a pharmacy word, and not "replenish," which is a stockroom one. The way of nature mends what falls short.

### Ch 77 · 恃 — *presuming* rejected, *rely on* locked

為而不恃 read *"acts without presuming"* in ch 2, 10 and 51, and Ch 77 inherited it. Shalom rejected it on 2026-08-26, first as *"acts without dependency."* The noun is not the fix — it is abstract where the line is verbs, and in current English it carries addiction — but **the discomfort was detecting something true**: 恃 (*shì*) is 心 (heart) + 寺, **to lean on, to count on**, and *presume* is an inference from the graph rather than a rendering of it.

**Settled as *rely on*** — Shalom's word, taken over the AI's *lean on* for two reasons found while writing the entry: 倚 (*yǐ* — to lean against) already holds *lean* at ch 58's 禍兮福之所倚, and 河上公's fourfold gloss 不恃望其報 (*"does not lean toward and watch for its repayment"*) is about counting on a return, which *rely* carries and *lean* underplays. *Shuowen* agrees: 恃，賴也.

**Swept the same day, all five occurrences.** ch 2, 10, 51 and 77 now share one formula — *acts yet relies on nothing* — where 為而不恃 had been carrying three different Englishes. ch 34's 萬物恃之以生 read *"draw sustenance from it"*, dropping 恃 entirely and erasing the book's only **positive** use of it; it now reads *"rely on it to live."* Entry: `glossary/shi-恃.md`.

**The cost, kept in the entry rather than hidden:** *rely* is Latinate with a dead picture (*re-* + *lier*, to bind), so English readers hear a mental act where the Chinese has a posture — 恃 is 忄 (heart) + 寺, the heart's member of a family of holding words (持 hand, 侍 body, 待 waiting). And *"relies on nothing"* can read as Stoic self-sufficiency; ch 34 is the guard against that, since there everything alive relies on the Tao and the Tao turns none of it away.

### Ch 77 · 不處 is *not staying*, not *not taking credit*

處 (*chù*) is to dwell, to occupy a place. 河上公 leaves no room: 功成事就不處其位 — *"the work done, they do not occupy the position."* Ch 2's parallel (功成而弗居) already reads *"the work is done, and the sage does not stay in it,"* and that chapter's closing couplet depends on the staying image — 夫唯弗居，是以不去, *"because the sage does not stay, it does not leave."*

*Taking credit* also makes the chapter repeat itself: 其不欲見賢 **is** the credit clause. Read as *not staying*, the three verbs move instead of circling — they act, they do not remain in what they did, they do not want to be seen for it. And 功成 is impersonal: the work completes. Not "they complete their work."

### Ch 77 · 有餘 / 不足 kept plain, and kept identical across both stanzas

*Excess* and *deficiency* were considered and set aside. They are the abstraction drift the overlay watchlist names — clinical register for the plainest Chinese in the chapter — and 補 as *supplement* loses the patched garment entirely.

**The structural reason matters more than the register one.** The Chinese repeats 有餘 and 不足 verbatim from the bow stanza into the human one; that repetition is the chapter's whole device, the same four terms with the arrows reversed. Any variation for elegance breaks the mirror at the exact line where the reader needs to see it. So *too much* and *too little* stand in both, unvaried.

**抑 keeps its hand.** 抑 (*yì*) is 扌 (hand) + 印 — pressing down. *Lowered* is what happens; *pressed down* is who does it, and the hands are the reason the bow is being braced rather than aimed.

### Ch 78 · 易 is *replace*, not *easy* — and 河上公 marks the tone to say so

以其無以易之 (*yǐ qí wú yǐ yì zhī*) turns on a homograph. 易 read in the departing tone is **easy**, which is what it means everywhere else in this book — ch 2 難易相成, ch 63 圖難於其易, ch 70 甚易知. Read in the entering tone it is **to exchange, to replace**.

河上公 does something here he almost never does: he tags the pronunciation. 夫攻堅強者無以易於水，**易入聲** — *"for attacking the hard and strong there is nothing to substitute for water. 易 is entering tone."* He evidently expected the mistake. So the line reads *"because nothing can take its place,"* not *"because nothing makes it easy."*

### Ch 78 · 社稷主 rendered for the substance, not the furniture

Our own source table glosses 社稷主 as *"Lord of the Altars"* — a straight hymn-test failure that manufactures a priest-king out of two agricultural offices. 社 (*shè*) is 示 (altar) + 土 (soil), the god of the ground; 稷 (*jì*) is millet, the god of grain. Together they are a Warring States metonym for **the state**, the way *the Crown* means the government.

But 國 (*guó* — the walled polity) already stands in the same clause: 受**國**之垢，是謂**社稷**主. So 社稷 is not doing the work of naming the state; it is naming what the state stands on. Rendered **keeper of the soil and the grain**. Laozi can point at soil and at grain. He cannot point at a Lord of Altars.

主 (*zhǔ* — a lamp with its flame, the one who presides) is kept distinct from 王 (*wáng* — the axe, locked to *ruler*), so the two titles escalate in English as they do in Chinese: the state, then the world. 河上公 supplies both senses — 長保其社稷，為一國君主, *"long preserve its altars, and be the sovereign of a state."*

### Ch 78 · 正言若反 — *words on the mark seem like their opposite*

**正 is not "correct." It is *on target*.** The oracle form is 止 (*zhǐ* — a foot) beneath a mark: a foot marching onto the objective. 征 (*zhēng* — to march on a campaign) is the same word with a walking radical added, and *Shuowen* glosses 正，是也 — 是 being itself 日 (sun) over 止 (foot), sun-straight. Correctness is the derived sense; **aim is the root**, and the rendering follows the root.

Three candidates were rejected, each for a different reason worth keeping.

**Straight** (the first draft, and the thread with ch 58's 正復為奇) renders the derivation rather than the graph, and *straight talk* shifts the claim to bluntness, which 正 is not about. **Upright** (the thread with ch 57) is a moral category in English — the Confucian coloring the razor strips. **Precise** was proposed and set aside on 2026-08-26 for a reason larger than register: it hands the book the one quality it has spent seventy-eight chapters declining (ch 1's unnameable Tao, ch 25's 強字之曰道, ch 41's catalogue of things that look like their opposites). 正 is also **accuracy, not precision** — in English those are opposite failures, and a tight grouping in the wrong corner is precise and not 正.

**反 is the *contrary* sense here, not ch 40's *return*.** 河上公 settles it and locates the error in the hearer: 此乃正直之言，**世人不知**，以為**反言** — *"these are straight and upright words; the people of the world do not know it, and take them for contrary speech."* "Their opposite" renders 反言 exactly.

**若 marks appearance, not frequency.** A quantifier was tried (*often seem*) and rejected: 正言若反 is categorical, which is what lets it serve as the book's colophon, and *often* would both hedge the claim and move the failure off the listener onto statistics. **Seem**, not *sound* — 言 is speech, but 若 marks appearance generally, and *sound* narrows it to the ear.

### Ch 78 · 弱 pays out, and Ch 52 is retrofitted

弱之勝強，柔之勝剛 is the line the 弱 lock was built on, and it forces four distinct words: 弱 **yielding** · 強 **strong** · 柔 **soft** · 剛 **hard**. 河上公 answers each half with an image rather than a definition — 水能滅火 (*"water can put out fire"*) and 舌柔齒剛，齒先舌亡 (*"the tongue is soft, the teeth are hard; the teeth go first"*).

Applying it here made Ch 52's 守柔曰強 unpayable as it stood: it read *"To stay with the yielding is strength,"* giving 柔 the word that belongs to 弱. Swept to **"To stay with the soft is strength."** Flagged in `CLAUDE.md` when the lock was set; discharged now.

### Ch 79 · 善 twice in one chapter, and the moral falls out

79 holds 善 (*shàn*) in two slots five lines apart — 安可以**為善**？ and 常與**善人** — and the received English renders both as *good*. That is what manufactures the moralized chapter: a question about whether patching a grudge is *good*, answered by a Heaven that sides with *the good*. Read both as **masterful**, per the lock, and the chapter becomes a claim about **competence**: settling a grudge after the fact is unskilled work, and the way of nature stays with those who never needed to.

王弼 licenses this directly, on 執左契: **左契防怨之所由生也** — *"the left tally guards against that from which grudges arise."* Prevention, not repair. That is a skill word, not a virtue word.

### Ch 79 · 徹 is auditing, not taxes — both commentators, independently

The standard rendering makes 有德司契，無德司徹 a contrast between contract and **taxation**, on the Zhou tithe sense of 徹 (*chè*) attested in Mencius. Neither classical commentator here reaches for it. 王弼: **徹司人之過也**, *"徹 is overseeing people's faults."* 河上公: **無德之君背其契，言司人所失**, *"the ruler without integrity turns their back on the tally: it means overseeing what people fall short in."* Two independent voices, the same gloss.

The graph agrees — 彳 (*chì* — a step) with 攴 (*pū* — a hand holding a stick): striking or seeing *through*. So 司徹 is going over the accounts to find the shortfall, and English has the exact idiom: **keeping score.** Rendered *"Those with integrity keep the tally. Those without integrity keep score."* The asymmetry of the articles is deliberate — 契 is an object you hold, 徹 is something you do to people.

### Ch 79 · 和 → "settle," and the accounting metaphor is the chapter

和 (*hé* — to harmonize) is elsewhere the word for blending and balance (ch 42 沖氣以為和, ch 55 和之至也). Here it is transitive and forensic: 和大怨, to compose a grudge. Rendered **settle**, because grudge, surplus, tally and score are one continuous ledger image and *settle* is the only English verb for 和 that stays inside it. *Reconcile* is more literal and steps out of the picture.

### Ch 79 · 餘怨 is the unhealed remainder, not the small one

An intermediate draft read *"and some small grudge always remains."* **Rejected.** 餘 (*yú*) is 食 (food) with 余 — surplus, remainder, what is still on the table. It is a presence word, not a size word: it answers whether the thing closed, not how much of it is left.

王弼 is decisive. 以致大怨已至，而德和之，**其傷不復**，故有餘怨也 — *"a great grudge has already arrived, and one uses integrity to compose it; **the wound does not heal**, and so there is leftover grudge."* 復 (*fù* — return to whole) is ch 16's word. He is describing damage that is not undone, not a scar that is minor.

Two costs decided it. The next line, 安可以為善, is a **dismissal**, and a dismissal only earns itself if the residue disqualifies the attempt; *small* invites the reader to answer back that small is good enough, which converts the chapter's case for prevention into a case for repair being merely imperfect. And 必有**餘**怨 carries the exact compound 有餘 that ch 77 makes the natural order's whole business (損**有餘**而補不足) — an axis of **excess**. *Small* swaps it for an axis of **size** and severs the thread.

The verb **remains** was adopted from the same draft, replacing *is left over*: one verb for three auxiliary words. The text's own repetition, 大**怨** … 餘**怨**, is left bare in English so it can land.

### Ch 79 · the tally is taught in the line, and 左 is dropped from the verse

First draft read *"the sage holds the left half of the tally / and never calls it in"* — accurate and opaque. It asked a modern reader to supply 300 BCE material culture from a bare noun, and *left* raised a question the poem cannot answer.

Revised to **"holds their half of the tally / and never asks for the other."** The second line now teaches the object: a tally has two halves, one per party, and one party can come asking. That is enough for the bare word **tally** to carry 有德司契 four lines later without a footnote. It is the poem's own way of defining a term — in use, not in a gloss.

**Modernizing the object was considered and rejected.** *Holds the note and never calls it in*, or *the IOU*, are far more legible, and both destroy the chapter. A note is a **one-sided** instrument. A 契 is **split**, and the claim cannot be enforced without the counterparty's half — which is precisely the contrast 有德司契，無德司徹 turns on: an instrument requiring the other party's participation, against a ledger you can run on someone without them. Kill the split at line four and the contrast at line six has nothing to stand on.

**執 (*zhí*) → *holds*; 司 (*sī*) → *keep*.** 執 is a hand grasping. 司 is administering an office, and it governs 契 and 徹 both, so the English reserves *keep* for the parallel and gives 執 its own verb.

**左 (*zuǒ* — left) is kept in the notes only.** It encoded which party held which half, and we cannot say which: the source table's literal gloss calls 左契 the *debtor's* tally, which cannot be right, since 而不責於人 (*does not press claims on people*) only means something in the hands of the party who could collect — 責 being 朿 (a thorn) over 貝 (a cowrie), to dun for payment. Neither 王弼 nor 河上公 states it. The editorial reading of the sage as creditor stands and is logged; the word carrying it does not survive into English, where it is noise on a point we hold by inference alone.

### Ch 79 · 天道 and 無親

**天道 → "the way of nature,"** following the precedent already set at ch 47 and twice at ch 77. **無親** is literally *has no kin* — 親 is closeness by blood — and "plays no favorites" is what it means in use.

### Ch 80 · 甘美安樂 are putative verbs — the food is poor and they find it sweet

甘其食，美其服，安其居，樂其俗 is not a description of what they have. All four verbs are **putative**: *find X sweet*, *find X fine*. 河上公 supplies the nouns the Chinese leaves bare, and every one of them is meagre — 甘其**蔬食** (coarse vegetable fare), 美其**惡衣** (poor clothing), 安其**茅茨** (thatch), 樂其**質朴之俗** (plain, unworked ways; note 朴, the 樸 lock). The received English — *"their food is sweet, their clothing beautiful"* — converts a portrait of 知足 (*zhīzú* — knowing you have enough) into a picture of abundance, which is the chapter's argument turned inside out. Rendered "They find their food sweet, / their clothes fine, / their houses restful, / their ways a pleasure." *Fine* is doing deliberate double duty for 美: beautiful, and good enough.

### Ch 80 · the three 使 are the chapter's spine

三 使 (*shǐ* — cause / let) open three of the chapter's clauses: 使有…, 使民重死…, 使民復…. They are **causatives addressed to a ruler**, and rendering them away is what turns this chapter into a landscape painting in English. All three keep an anaphoric *"Let."* The opening 小國寡民 stays verbless, as the Chinese is, so it can be read as scene or as instruction — see the reading note; both commentators read it as the second.

### Ch 80 · 使有什伯之器 — 王弼 supplies the subject, and the 無所 triple

The clause elides its subject: 使有什伯之器而不用, *"cause there to be ten- and hundred-fold tools and not use them."* Classical Chinese drops subjects freely; English strands them, which is what standing rule 5 is about. **王弼 restores it outright** — 言**使民**雖有什伯之器而無所用 — and the next clause of the base text states it (使**民**重死), so the two are parallel causatives over 民. The English names the people in both.

**而 is concessive, not additive.** 王弼 marks it with 雖 (*suī* — although): 雖有什伯之器**而**無所用. So the English is *"yet no need to use them,"* not *"and."* An *and* flattens a concession into a list.

**And the reason is sufficiency, not abstinence.** 王弼's full gloss is 無所用，**何患不足也** — *"nowhere to use them; why worry about not having enough?"* That is 知足. A tool that does the work of a hundred is needed only by someone who is short, so *no need* renders the argument, where the first draft's *no use for them* made the idleness sound like virtue. (Both fixes Shalom's, 2026-08-26. The draft also stranded the subject, which is what sent us back to 王弼's 使民.)

### Ch 80 · 無所 is *no call*, not *nowhere* — and 陳 is *take the field*

無所 + verb is the idiom for **no occasion arising**, not for a place failing to exist. The draft rendered both halves of the couplet *"there is nowhere to…"*, which makes a claim about the map the Chinese never makes — of course a small state has places to take a boat. Shalom caught it, 2026-08-26. **無所 → "there is no call to"**, twice, matching the two 無所.

河上公 names what is actually absent: 清静無為，不作煩華，**不好出入游娯也** — *"still and non-doing, not making vexing extravagance, and not fond of going out and roaming."* 王弼's gloss on the whole block is four characters, 無所欲求, *"nothing they want to seek."* So 乘 (*chéng* — to ride, to mount) renders **"travel in them"**: 舟輿 are distance technology, the line above has just said 不遠徙 (they do not move far), and naming the missing thing as *distance* ties the two together.

**陳 (*chén*) is the military verb for arraying a formation** — not showing something off. "No occasion to display them" makes the armor ornamental. Two drafts then over-corrected into jargon: *draw them up*, which readers parse as *draft*, and *draw them up in ranks*, which is worse. Settled on **"no call to march them out"** — plain, keeps 之 as *them*, and holds the image the received "display them" destroys: an army that is never sent anywhere. It gives up a little of the *formation* sense 陳 specifically carries; the alternative that keeps it, *take the field*, was the precise idiom for battle array but elided 之, and Shalom took the plainer one (2026-08-26). What matters is that both refuse *display*, which turns armor into ornament.

### Ch 80 · 往來 is traffic, not friendship

不相往來 has carried a xenophobic tone in English for a century — *"they never visit one another."* Neither commentator reads sociability. 王弼's entire gloss on the closing block is four characters: 無所欲求 — *"nothing they want to seek."* 河上公: 其無情欲 — *"they have no craving."* 往來 is going and coming — **errands, traffic, trade**. So we render the motion and nothing else: *"and never once **go next door**."*

**河上公 licenses the domestic register directly.** His whole gloss on 鄰國相望，雞狗之聲相聞 is four characters — **相去近也**, *"the distance between them is near."* Not geopolitics: proximity. And the chapter's own evidence for that proximity is **chickens and dogs**, household animals, the sound of someone else's yard. *Next door* is the English idiom for a neighbour whose animals you can hear, and it sits in the register the stanza is already in — thatch, clothes, the food on the table.

Two drafts failed first, both by leaving the destination unnamed. *cross between them* is not English idiom, and its *them* had to reach two lines back past two nearer plurals. *make the trip* fixed the idiom but still did not say **where**, which is the fact the line exists to deliver. (Both caught by Shalom, 2026-08-26.) Rejected alternatives: *make the trip next door*, which sharpens the irony but makes the book's second-to-last line wink; and *set foot in the next state*, which re-inflates 國 to statecraft register at precisely the moment 河上公 is calling the distance a short walk. The three 相 (*xiāng* — mutually) of 相望 / 相聞 / 不相往來 are carried by the two *each other*s above.

### Ch 80 · 重死 answers Ch 75's 輕死

使民重死 (*shǐ mín zhòng sǐ*) is the exact inverse of Ch 75's 民之輕死 — 重 (heavy) against 輕 (light), same object. Ch 75 already reads *"The people **make light of** death."* Ch 80 reads **"Let the people find death heavy"** — 重 kept as weight, so the pair stays audible across five chapters without a footnote.

**And it is the chapter's own grammar.** 重死 is a putative verb — *regard death as heavy* — structurally identical to the 甘其食，美其服 of the last stanza, which we render *"They **find** their food sweet, their clothes fine."* The same English verb twice in one chapter is the source's construction, not our tic.

**Three renderings were tried and rejected, and each failure is informative.**

*hold death heavy* (first draft). `concordance.py --english "hold"` shows the verb is already carrying 守 (ch 52, *hold fast to* — a lock), 貴 (ch 75:21, *hold life precious*), 執, and Ch 79's tally; it cannot take 重 as well. And *hold death heavy* leans morbid, which inverts the sense: 河上公 glosses the line 則民重死而**貪生** — *"then the people weigh death heavy and cling to life."* The point is that a life is worth keeping, not that death is a burden. *Find* fixes this where *hold* could not: it marks the weight as a judgment the people make rather than a load laid on them.

*make much of death* (second draft). The clean antonym of ch 75's *make light of* — but the idiom has soured. Modern English *make much of* implies **overvaluing**, fussing, protesting too much.

*respect / honour / be humble before death* (proposed). All three make death an **object of reverence**, a power one stands before — and every one of them would sit in a sermon without a ripple. 重死 is a disposition toward one's own life ending, not a posture toward Death. 王弼: 惟身是寶, *"they treasure only their own bodies."*

**And the plainest English of all is a trap: *loath to die* / *unwilling to die* renders 貴生, not 重死** — and Ch 75 **criticises** 貴生, which we render *"those who hold life precious."* The book distinguishes a life that has weight to you (重死, approved here) from clutching at it (貴生, warned against there). A rendering that collapses them would make Ch 80 recommend what Ch 75 rejects. This is the argument that decided the line. (Shalom flagged *hold* and then *make much of* as incongruous, 2026-08-26; both flags were right.)

### Ch 81 · 美 → *pretty*, and why "fine" was the near miss

美 (*měi*) is 羊 (*yáng* — a sheep) over 大 (*dà* — big): a big sheep, the pleasing thing. Ch 2 has it as the aesthetic category proper (天下皆知美之為美 — *"when the world knows beauty as beauty"*) and it stays **beauty** there. Ch 81 is not that. Both commentators read **ornament**, and both reach for the same antonym:

- 王弼 on 美言不信: 本在樸也 — *"the root lies in the uncarved."* 樸 (*pǔ*) is a locked term. Wang Bi makes *uncarved wood* the opposite of 美言, which settles the register: 美 here is what has been worked over.
- 河上公: 滋美之言者，孳孳華詞 — *"words made 美 are busily flowery phrasing"* — and 不信者，飾偽多空虚也, *"the untrustworthy is decorated falsehood, much of it empty."*

**Rejected: *fine words*, the reading in ch 62.** Ch 62's 美言可以市尊 renders *"Fine words can buy honor,"* and consistency argued for carrying it here. Two things beat it. *Fine* in modern English has drifted to mean *adequate* — "trustworthy words are not fine" reads as a concession, not an indictment. And ch 62's 美言 is instrumental, words that **purchase** status; ch 81's is decorative, words that **please**. Same character, adjacent senses, and the chapters are doing different work with it. **Ch 62 is left as it stands**; the seam is noted rather than sanded.

*美 is not lock material — ch 2 (beauty), ch 31 (glorify), ch 62 (fine), ch 81 (pretty) are four honest senses of one character. Noted so the next sweep does not mistake the spread for drift.*

### Ch 81 · 博 → *have heard it all*

博 (*bó*) is 十 (*shí* — ten, the complete set) with 尃 (*fū* — to spread out): **spread wide**. It occurs **once in the whole book**, here, so there is no consistency cost to paying for the sharper reading.

**河上公 supplies both halves of the contrast, and they are the argument:**

> 博者多見聞 — *"the 博 has seen and heard much"*
> 不博者守一元也 — *"the un-博 **holds fast to** the one origin"*

守 (*shǒu*) is our locked **hold fast to**. Gathered against scattered. And he names the cost rather than a ranking: 不知者失要真也 — 失 (*shī* — **to lose**), 要 (*yào* — essential), 真 (*zhēn* — real). Breadth does not sit below knowing; it **destroys** it. Ch 47 states the same thing as a proportion — 其出彌遠，其知彌少, *"the further out, the less you know."* That inverse is why the couplet is a flat contradiction (知者**不**博) and not a preference.

**Chosen: *have heard it all*.** It is 多見聞 put straight into English, and the idiom does a job no neutral word can — **the person who has heard it all is precisely the person who cannot be told anything.** It supplies the causal mechanism 河上公 only asserts. And it passes the pointing test: Laozi could point at someone who has heard everything; he could not point at *information*.

### Rejected, and why each failed

**"well-informed"** (the first draft). The defect Shalom caught: **it is a compliment in English.** Both halves of the couplet then sound endorsed, and the reader cannot tell which is the counterfeit. Couplet one signals it with *pretty*, couplet two with *argue*; couplet three had no signal at all.

**"truly know"** (proposed, for the same problem, on the other side of the line). Three costs. Ch 56 carries the identical frame — 知者不言，言者不知, *"Those who know do not speak. Those who speak do not know."* — so an intensifier at 81 alone silences the twin, and at both weakens one of the book's best-known lines. It also **concedes the argument**: *truly* implies two kinds of knowing, where Laozi is denying that breadth is knowing at all. And it breaks the mirror inside the couplet — *truly know* against a bare *do not know*.

**"hoard information."** The sharpest paraphrase raised, and rejected on **placement**: 積 (*jī* — to heap up grain) is the *next* line's word (聖人不積), and spending *hoard* early flattens the turn from knowledge to goods. Shalom's call, and it is right — the two lines are the same claim about accumulation applied to two objects, and the second must be allowed to land.

**"range wide."** Graph-faithful, imports nothing, and rhymes with ch 47's going-out. But it does not deflate — *range wide* is neutral in English, which is exactly the *well-informed* defect again.

**"spread thin."** Nearly 尃 literally, and the precise opposite of 守一元. But modern English uses it for someone **overcommitted**, so it reads as busyness rather than as knowing too many things.

**"widely read" / "learned."** Anachronistic — 見聞 is *seen and heard*, an oral culture — and *learning* already belongs to 學 (*xué*) at ch 20 and ch 48.

### Two costs, logged rather than smoothed

**1. The word is borrowed.** Ch 81 contains no 聞 (*wén* — to hear). *Heard* comes from the commentary, not from this chapter's Chinese, so `concordance.py --english "heard"` will report ch 81 unbacked — exactly the class of finding the `--english` direction exists to catch. Waived in the chapter's `## Notes` with this reason. A footnote, not a precedent: one occurrence, one chapter.

**2. The chapter may fail to widen where it should.** *Heard it all* carries the first two couplets' concern with speech — 言 (*yán* — words), then 辯 (*biàn* — argue) — into the third, which could read as the chapter narrowing to talk at the moment it ought to open onto knowing.

**Accepted anyway, and this is the reason.** Knowing in this book is *consistently* treated as a matter of what you take in and how far you range, not as a stock of contents: ch 47's 不出戶，知天下 (*"without going out the door, you know the world"*) and 其出彌遠，其知彌少; ch 56's 知者不言 (*"those who know do not speak"*); ch 71's 知不知，上 (*"to know you do not know is highest"*). The intake register **is** the book's register for 知. Reading 博 through the ear is therefore not a narrowing but an alignment. *(Shalom's call, 2026-08-26.)*

### The couplet is the hinge, not the end of a list

博 is 見聞 accumulated — knowledge held as a **stockpile** — and the very next line is 聖人不積, *the sage does not hoard*. Same movement of accumulation, two objects. 河上公 runs the link himself, one gloss into the next: 守一元 (hold to the one) → 聖人積德不積財 (*"the sage accumulates integrity, not wealth"*). There is no seam between the three couplets and the middle movement. **The third couplet is the turn.**

### Ch 81 · 辯 → *argue*, not *eloquence*

The graph settles it. 辯 (*biàn*) is 辡 — **two 辛** (*xīn*, the tattooing knife that marked a convict) set face to face, the classical graph for two parties in litigation — with 言 (*yán* — words) between them. **Words between disputants.** Eloquence is a consequence of that, not the content of it. 河上公 confirms the valence: 辯者謂巧言也 (*"the 辯 is clever speech"*), 不善者舌致患也 (*"the unmasterful: the tongue brings on trouble"*), and the image 山有玉掘其山，水有珠濁其淵 — *"a mountain with jade in it gets dug up; water with pearls in it has its depths muddied."*

**Ch 45's 大辯若訥 keeps *eloquence* for now.** There 辯 is what is being praised (大辯 — great 辯) and its foil is 訥 (*nè* — to stammer), so the line is about verbal facility specifically. One character, opposite valences, two chapters apart. Flagged, not forced.

### Ch 81 · 不積 — the sage hoards, in ch 59

聖人不積 does **not** mean the sage accumulates nothing. Ch 59 uses the identical character approvingly, twice: 重積德 (*zhòng jī dé* — *"a heavy accumulation of integrity"*). 河上公 resolves it in five characters — **聖人積德不積財**, *"the sage accumulates integrity, not wealth"* — and finishes the thought: 有德以教愚，有財以與貧也, *"having integrity, they teach the ignorant; having wealth, they give it to the poor."*

積 (*jī*) is 禾 (*hé* — standing grain) with 責 (*zé* — to gather in): **grain heaped in a granary**. **Hoard** keeps the granary and the disapproval, and — unlike *accumulate* — cannot be read back onto ch 59.

### Ch 81 · 既以為人己愈有 — perfective, not conditional

既 (*jì*) is the perfective particle, not *if*. The standard English (*"the more he does for others…"*) turns a completed act into a rate of exchange, which makes the couplet a transaction. It is not one: 河上公 ends on 如日月之光，無有盡時也 — *"like the light of sun and moon, which has no time of running out."* The sage is not trading; they are a **source**, and a source does not deplete.

Hence **"Having done for others, they have more. / Having given to others, they have more still."** The two verbs are the locked 為 (*wéi* — do/handle) and 與 (*yǔ* — give), and 有 (have) / 多 (more) are held apart as *more* / *more still* so the escalation of the doubled 愈 (*yù* — the more) survives.

---

## 強 — the fourth word of the table, 2026-08-28

**Locked: strong.** Entry at `glossary/qiang-強.md`. The 弱 lock had already declared this in its four-word table (柔 soft · 剛 hard · 弱 yielding · 強 strong) without an entry to enforce it, and the manuscript carried six Englishes for 強 across twelve chapters — two of them four lines apart in ch 33.

**What decided it: ch 52 and ch 55 use the same frame with opposite verdicts.** 守柔曰強 ("holding to the soft is called 強") and 心使氣曰強 ("the heart driving the energy is called 強"). One is praise, one is a warning, and the next line after the second is 物壯則老. Rendering the first *strength* and the second *forcing* answers a question the text leaves standing. 王弼 puts both on one page: 守強不強，守柔乃強也.

**The graph.** 強 is 蚚 — a grain weevil (說文, 虫部), borrowed for its sound from the Qin onward and displacing 彊, which is 弓有力也, "a bow having force." 弱 is two bows that bend. They are one instrument in two states, and 木強則折 (ch 76) is a bow past its give. This is the second core term in the book whose graph is an insect conscripted by rhyme; 萬 in 萬物 is a scorpion.

**Three flexions, all grammatically marked.** *Strengthen* where it takes an object — ch 3 強其骨 and ch 36 必固強之, the same two lines where 弱 is licensed to read *weaken*, because it is one grammar taken twice. *Forcing* where it strains a naming — ch 15 強為之容, ch 25 強字之曰道 (河上公's text carries the fanqie 強其文反, marking the *qiǎng* reading; the phonetic notes are later editorial additions). *Force / dominance* for ch 30's three coercive uses, where *strengthen* would be simply wrong — you do not strengthen a country by invading it. Everywhere else, **strong**.

**力 is covered as *force*.** Ch 33's 勝人者有力，自勝者強 is plain force against achieved strength, rhyming with 智/明 in the line above. Our text had it inverted — 有力 as "aggressive power," 強 as "true strength" — while ch 68 already rendered 力 as "strength."

**Two two-way violations, invisible to the checker.** 固 (*gù* — firm) at ch 55's 握固 and 壯 (*zhuàng* — in its prime) at 物壯則老 in ch 30 and 55 had both borrowed 強's English, in chapters that contain 強. The evidence gate that makes `check_locks.py` trustworthy is exactly what blinds it to these: the character is present, so no rule fires. Corrected by hand.

---

## Ch 24 — the mirror of Ch 22, 2026-08-28

**Pass C.** Ch 22's 不自X (*bù zì X* — "does not X themselves") stanza was rebuilt 2026-08-27; ch 24 is its exact negative on the same four verbs — 見 (*jiàn* — display) · 是 (*shì* — affirm as right) · 伐 (*fá* — claim) · 矜 (*jīn* — magnify oneself) — and the two chapters had shared no English at all. Full argument in `chapters/024.md` · Notes; three findings are worth carrying here.

**The mirror is in the verbs, not in matching predicates, and forcing the predicates together produced a punctuation hack.** The two chapters have different subjects: in ch 22 what becomes evident is *their rightness* (王弼 supplies it — 不自是則其是彰也), while in ch 24 it is *the person* who fails to appear (河上公 — 衆共蔽之，使不得彰明, "the crowd together obscures them"). An intermediate draft joined them with a colon; the fix was to stop trying.

***"Go unseen" is praise in this book, and an intermediate draft used it as the punishment.*** Ch 17's best rulers are barely known; ch 41 has 道隱無名; ch 70's sage wears coarse cloth over jade. The stanza's logic is **grasp at a thing and lose it**, and what this figure grasps at is recognition — so the loss must read as failure. Caught by Shalom. **A rendering can satisfy the character and still invert the book.**

**A commentator's gloss is not the text.** 餘食贅行 drew *wart* from 王弼 (肬贅) and *greed* from 河上公 (贅，貪也). Both were offered to Shalom as candidate renderings and both were correctly refused: the text has only 贅 (*zhuì* — superfluous, an appendage; 說文 以物質錢也, "to pawn a thing for money"). **Neither commentator's word is in the line.** *Wasted motion* keeps the plain sense and ties the summary back to the chapter's own opening images. 河上公's moral reading is separately declined on the naturalistic razor.

**跨 (*kuà*) is an overstretched step, not a stride** — 足 (foot) beside 夸 (*kuā* — to boast). Rendering it *stride* left a near-synonym of *walk* and killed the paradox. 河上公 licenses the repair by glossing 不行 as 使不得行 ("so they cannot get anywhere").

**物 → living things.** 河上公's 物無有不畏惡也 uses 畏 (*wèi* — fear), and rocks do not fear. 惡 read *wù* is aversion, not hatred → **recoil**. 或 (*huò*) is dropped deliberately. Swept into ch 31, which carries both closing lines verbatim.

---

## Four repeated formulas brought into line, 2026-08-28

**Pass C, the mechanical half.** In each case one chapter already carried the formula correctly and the other did not; the work was choosing which side won, not inventing a rendering. Three `repeated-formula` warnings closed (17 → 14).

**是謂玄德** (*shì wèi xuán dé* — "this is called profound integrity"). Ch 51 and ch 65 read *is called*; **ch 10 had dropped 謂** (*wèi* — is called) and asserted the identity flatly. Ch 10 now matches.

**故能成其大** (*gù néng chéng qí dà* — "and so completes its greatness"). Ch 63 was right. **Ch 34 had lost 成** (*chéng* — to complete) altogether and invented an intensifier: *"The Tao shows **true** greatness."* Now *"It never makes itself great, and so completes its greatness"*, which also restores the parallel with ch 63's 終不為大 (*zhōng bù wéi dà* — "never does the great"). Note the two chapters differ in their first halves — ch 34 has 不**自**為大 (does not make **itself** great), ch 63 has 不為大 (does not do the great) — so only the second clause is shared and only it was matched.

**可以長久** (*kě yǐ cháng jiǔ* — "can last long"). **Neither side carried it**: ch 44 had a noun phrase (*"you have long endurance"*) and ch 59 a different verb (*"one endures long"*). Both now read **can last long**, each keeping its own chapter's pronoun — the formula is the predicate, not the subject.

**是以聖人猶難之** (*shì yǐ shèng rén yóu nán zhī* — "so the sage still finds it difficult"). Ch 63 was close; **ch 73 read *"Even the sage finds this hard,"* which attaches 猶** (*yóu* — still, even so) **to 聖人 rather than to 難**. The Chinese says the sage still treats the thing as difficult, not that even a sage finds it hard — a difference between a practice and a concession. Both now read identically, and *hard* gives way to *difficult*, which ch 63 uses four times in its 難/易 (*nán/yì* — difficult/easy) pairs.

**為天下式** (*wéi tiān xià shì* — "serve as a pattern for the world") **was deliberately left.** Ch 22 reads *"sets a pattern for the world"*; ch 28 has it twice as *"Embody the pattern of the world."* Fixing it alone would mean touching ch 28 twice, since that chapter's three four-beat stanzas have to move as a unit — 守 is wrong in all three (`WORKLIST` T1-7), 常 is missing from all three 常德, and 谷/谿/官長 are open at T1-15. Deferred to the chapter's Pass D rewrite.

---

## Ch 8 — 善's showcase, and the grammar that decides it, 2026-09-02

*Pass D. `WORKLIST.md` T2-8 and T3-2, both closed.*

### 善 governs a verb — eighteen out of eighteen, and that is a standing principle

**Moved to [`glossary/shan-善.md`](../glossary/shan-善.md), 2026-09-10** — a fact about one character, filed as a principle. The heading stays so existing links resolve.

**Its other half *is* transferable and is now [`supplied-verb-is-scaffolding`](../process/principles/supplied-verb-is-scaffolding.md):** *masterful at X* requires X to name an activity, and collapses where the noun is a place — so a stance verb is supplied at 地 and 淵, and named as supplied. That rule governs chapters nobody has read yet. *善 governs a verb* governs 善.

### Supply a verb where the object names a place — and only there

**A second standing principle, and it is the first one's other half.** Having established that 善 governs a verb, the first draft rendered all seven objects as bare nouns: *masterful at ground · at depth · at humaneness · at trust · at order · at what can be done · at timing*. **English *masterful at X* requires X to name an activity.** It holds where the noun is a quality or a practice — 仁, 信, 治, 能, 時 — and **collapses where the noun is a place**: *"masterful at ground"* communicates nothing, and 淵 (*yuān* — a deep pool) is a place too. A stance verb is supplied at those two and nowhere else: **choosing ground**, **staying deep**.

**Ch 66 is the precedent and it predates this chapter.** 善下之 already reads *"masterful at **staying** below them"* — 下 (*xià* — below) is a position, and the English supplies the verb. Ch 61 does the same with *staying low*. **A supplied verb is scaffolding, not a character's English**, so *staying* can serve both 下 and 淵 without either losing its word. **The general rule: where the Chinese object is a position and the English needs a verb, supply a stance verb and name it — do not let the noun stand bare and hope.**

**Run the reverse check on the supplied word too, not just on the rendering.** It rejected two obvious candidates here: *keeping trust*, because *keep* is 全 (*quán* — whole)'s declared render and the manuscript already carries **nine unbacked *keeps***, and *bringing order*, because *bring* belongs to 生 (*shēng* — to give birth) and is unbacked seven times. **擇 (*zé* — to choose) and 選 (*xuǎn* — to select) have zero occurrences in the book**, so *choosing* was free. *(Both of those unbacked piles are pre-existing and now visible; neither is swept here.)*

### The chapter, line by line

**幾 (*jī*) is an adverb of degree, and two drafts running made it a verb.** 故幾於道 read *"And is therefore **one with** the Tao"* — identity for a hair's breadth — and the first repair over-corrected to *"comes near the Tao,"* which put the Tao at a distance and sent water travelling to it. **Caught by Shalom on the second, and the diagnosis is grammatical: 幾於道 contains no verb.** 說文: 微也。殆也, from 𢆶 (*yōu* — fine silk threads) under 戍 (*shù* — a garrison guard), which the entry spells out as 危也. Its second gloss is 殆 (*dài*), locked to **danger** on 2026-08-31.

**The book's other three 幾 are all degree, and none of them moves** — ch 69's 幾喪 → *"nearly costs"*, ch 64's 幾成 → *"just short of completing"*, ch 20's 幾何 → *"how much distance"*. **When a rendering is contested, count the character's other lines before arguing about the word.** It settled this in one command.

**The frame is sameness, not location, and ch 23 prints it bare seven times.** 河上公 glosses ch 8's line 水性幾與道**同**, *"nearly the **same** as the Tao"* — 幾 as an adverb on the stative 同 (*tóng* — the same) — and ch 23 has 同於道 (*"the same as the Tao"*) with no degree word at all. **幾於道 is 同於道 with a hair's breadth inserted**, and 於 (*yú*) is the relational particle, *with respect to*, never *toward*. Final: ***"and so is nearly the Tao."***

***Like the Tao* was proposed and declined.** It deletes 故 (*gù* — therefore, the chapter's inference, twice present), deletes 幾, **collides with 若 (*ruò* — like) in this chapter's own opening line** (上善若水), and moves the predication from water's nearness onto the Tao's dwelling. **A simile word cannot render a degree word**, even when both hedge.

**Rider opened: ch 23's 同於道 ×7 reads *"merges with the Tao."*** The same defect Shalom caught here — a word meaning *be the same as* rendered as a verb of motion and mixing. Opened as T2-25.
**上善 → *the most masterful*** (Shalom's call). 上 (*shàng* — highest) is settled at ch 38's 上德/上仁/上義/上禮; *good* is reserved by the lock for chapters 2, 20 and 58, where the book **attacks** the category, so using it here would make ch 8 endorse what ch 2 dismantles. Follows 河上公's person-reading, 上善之人如水之性. **Cost: it decides that 上善 is a person rather than the quality.** Full argument in `glossary/shan-善.md`.

**A rank word is not an authenticity word.** *True mastery* was proposed for 上善 and declined: 真 (*zhēn* — genuine) is live in this book at 21, 41 and 54, *true* already wears 真, 貞 and nothing at all across three lines, and **上 presupposes *lower* where *true* presupposes *false*** — a different axis, and a moral one. 上 is graded, and ch 41 prints the middle rung (上士/中士/下士). Kin to T4-7, the rank question.

**能 → *what can be done*, built from *can*.** 能 (*néng* — able) has 32 lines in 17 chapters and **31 are the plain modal *can***; ch 8's is the only noun in the book. *Ability* was a Latinate abstraction imported for that one line and stacked a second abstract noun beside *masterful*. **When a character is a verb almost everywhere, its one nominal use should be built from the verb's own English, not from a thesaurus.** *Action* was proposed and fails twice: 動 (*dòng* — to move) is the action word in the next line, and *action* already wears 行, 作, 事 (locked to *affairs*) and nothing at all across ch 12, 16, 23, 30 and 37. Cost: a slight drift of the capacity from the agent to the situation.

**利 → *benefiting*; *nourishes* was 養's English.** *Nourish* appears at ch 34 (衣**養**萬物) and ch 51 (**養**之覆之), both 養 (*yǎng*), **absent here**. 利 already reads *benefit* at 19, 56, 73 and 81, including 81's 利而不害 — the same 而 construction. Found by `--english`, invisible to `check_locks`.

**惡 read *wù*, and 河上公 marks it.** 處眾人之所惡 had read *"where the crowd will not go"* — avoidance for loathing. His *fanqie* note 惡烏路反 fixes the reading as the verb *to detest*, and his gloss names what is detested: 衆人惡卑濕垢濁, *"the low, the damp, the dirty and the turbid."*

**仁 → *humaneness*, the lock.** *"Pure kindness"* breached it and invented *pure*. `check_locks.py` was silent because *kindness* is not on 仁's `forbidden:` list — **the same blind spot that hid ch 38's *clutches at***, and an argument for T5-3.

**尤 is a hapax, and *always blameless* lost both halves.** 常 (*cháng* — the ever-present) has zero occurrences here, so *always* rendered nothing; 尤 (*yóu* — blame) appears once in all 81 chapters and means fault-finding, not moral purity. Kept **agentless** — 無尤 is agentless, and 河上公 supplies the agents (天下无有怨尤水者也) rather than the text.

**居 and 處 are near-twins and the seam is named.** 說文: 處 is 止也。得几而止 (*"to stop; to find a stool and stop"*), 居 is 蹲也 (*"to squat"*). 處 keeps *dwells* — its English at 24, 31, 38, 76 — and 居 takes ***settling***, 說文's squat. **This is the ch 38 collation note paying out** (`notes/manuscript.md`): the alternation may not be original, so the English is free to use one verb or two without straining.

### Left open, deliberately

**淵 (*yuān* — a deep pool) reads three ways** — *fathomless* (4), *depth* (8), *the deep abyss* (36) — and 說文 makes it **banked** water: 回水也…左右，岸也, *"swirling water… left and right are the banks."* That is why a fish cannot leave one at ch 36, and why *limitless* was precisely backwards. *Depth* is a holding move at ch 8; settling the term properly creates riders at ch 4 (rebuilt 2026-08-31) and ch 36. Opened as T2-24.

**The mistake worth keeping.** A first draft of the 上善 argument claimed ch 8 stages an 上/下 descent **lexically**. It does not: 下 (*xià* — below) has **zero occurrences** in the chapter. The descent is real but carried by low nouns — 地 (*dì* — ground), 淵 — and by 所惡; the 下 and the 卑 (*bēi* — low) I cited were 河上公's words, not the text's. The explicit pair lives at ch 66 (善下之) and ch 76 (強大處下，柔弱處上). Caught by Shalom. **A commentator's gloss is not the text — the second time this file has had to record that, and the first was ch 24.**

---

## Ch 23 — 同 is *the same*, not a merging, 2026-09-03

*Pass D. `WORKLIST.md` T2-25, closed.*

### The character is the antonym of *different*, and ch 1 prints the pair

**此兩者，同出而異名** — *"these two 同 emerge and 異 in name."* 同 (*tóng* — the same) stands against 異 (*yì* — different) in a single clause, and our ch 1 already renders it **same**. Then it scattered: *together* (1), *merges with* (4, 23 ×6, 56), *union* (56). **Five Englishes, and ch 23 carried the mystical one six times.**

**Both commentators gloss 同 with 同.** 王弼 (*Wáng Bì*): 與道**同體**, *"of one body with the Tao."* 河上公 (*Héshàng Gōng*): 所謂**與道同**也, *"what is called being the same as the Tao."* **Neither describes a process, and neither describes dissolution.**

**The chapter's claim is resonance, and 河上公 gives it in the 易經's own formula:** 同聲相應，雲從龍，風從虎，水流濕，火就燥 — *"like sounds answer each other: clouds follow the dragon, wind follows the tiger, water flows to the damp, fire goes to the dry."* **Four pairs. Every one is two things finding each other by kind.** 王弼 arrives independently, glossing 樂得之 with 應 (*yìng* — to answer): 故同而應之.

### Why identity was declined, and how it differs from ch 8

***"Is the Tao"* was proposed** (Shalom) **and it followed from the ch 8 ruling** — if 幾於道 is *"nearly the Tao,"* then 同於道 stripped of its degree word is *"is the Tao."* **It fails on the second stanza.** 同於道者，道亦樂**得之** needs two parties: someone to be received and someone to receive. Read as identity there is neither, and the resonance collapses — **a cloud that *is* the dragon has nothing to follow.**

**The asymmetry with ch 8, stated once so it is not re-argued:** 幾 (*jī* — nearly) **survives the collapse**, because the English word *nearly* is the character. 同 does not survive as *is*, and ch 56's 玄同 (*xuán tóng* — dark sameness) would be left with nothing to render. **A degree word can be absorbed into English; a content word cannot.**

**Cost of *the same as*, named:** six repetitions of a four-word phrase, heavier in English than 同於 is in Chinese. Accepted because the repetition is the argument. ***Matches*** was the lighter candidate and was declined as correspondence where 王弼 says substance (同體).

### The rest of the chapter

**事 (*shì* — affairs) is locked and read *actions*.** 從事於道者 → ***"one whose affairs follow the Tao."*** ***"One who follows the Tao"*** was proposed and **declined on the reverse check**: **ch 21's 惟道是從 already reads *"follows the Tao,"* and there 道 really is 從's object**, where here 從 governs 事 and 於道 is a complement — one English for two unlike grammars. **從事 occurs twice in the book**, here and ch 64's 民之從事 (*their affairs*). **The chapter is about conduct, not allegiance.** Both commentators define the phrase: 王弼 從事謂舉動, 河上公 從，為也。人為事當如道安静. ***Aligns* rendered 從** (*cóng*), whose 說文 is 隨行也, *"to follow along."*

***Intensity* and *sustain* rendered nothing** — 天地尚不能久 is duration (久 *jiǔ*), and *intensity* was 王弼's 暴疾 (*"violent and rapid"*) lifted from commentary into verse. **The ch 24 *wart* error, third occurrence.** 人 (*rén* — a person) had become ***we***, a first person not in the line; restoring *a person* does not touch the deferred T4-1, since *we* is neither candidate. 為 (*wéi*) had become *acts*.

**希言自然 → "Brevity in speech happens of itself."** *(Shalom's line, with two repairs.)* Three drafts, and the failures are the useful record. *"Speak sparingly, for **things** go of themselves"* supplied 物 (*wù* — things). *"Speech barely heard"* named **volume**, which neither commentator does — 河上公 means quantity (愛言, *sparing with words*), 王弼 means unremarkable (無味不足聽之言, *"no flavour, not enough to hear"*); **a whisper is neither**. *"Saying little is so of itself, and no one makes it so"* said something but **did not earn the 故** that follows.

**故 is printed and left unrendered, and the warrant is textual.** *(Shalom's call, 2026-09-04.)* The Siku 王弼 — our base — is the **only** witness that prints 故 (*gù* — therefore) here, and it says so itself: 〔案**河上公注本及各本俱無故字**〕, *"the Heshang Gong commentary edition and all editions lack the character 故."* Our vendored 河上公 confirms it. **So the three statements now stand in juxtaposition, as every other witness has them**, and the reader makes the connection. **We print the base text; we do not emend it — but neither do we assert in English an inference our base is alone in claiming.**

***Likewise* was proposed for 故 and declined.** 說文 makes it unambiguously causal — **使爲之也。从攴古聲**, *"to cause something to be done,"* a hand holding a stick (攴 *pū*) over 古 (*gǔ* — old). Rendering it comparatively would give the book's causal particle, **63 lines in 42 chapters**, a comparative English in one place. **And it inverts the logic**: both commentators make the squall the **counter-case**, not a parallel instance — 王弼 言暴疾美興不長也, 河上公 言疾不能長，暴不能久也, *"the violent cannot endure."* An instance would soften the chapter's warning, 而況於人乎, *"how much less a person?"* **The chapter's second 故 is rendered** (故從事於道者 → *So one whose affairs follow the Tao*), because there the inference is the chapter's own conclusion.

**A correction on the record.** An earlier version of this note praised the line for making the storm *"the thesis rather than its counter-example."* **That was backwards** — both commentators make it the counter-example, and 王弼 sets the contrast up by glossing 希言 with the Tao's own speech: 道之出言，淡兮其無味也。視之不足見，聽之不足聞 (ch 35's line, which he calls 下章). **The self-so mode of speech is bland and barely there; a squall is its opposite, and it stops before noon.** The line stands; the reason given for it did not.

**Two repairs, both from the reverse check.** 言 (*yán* — speech) had been dropped, and it is this chapter's only speech word — the link to 不言之教 (2, 43), 言者不知 (56), 信言不美 (81). And *the whole morning* was declined: **whole is 全 (*quán*)'s English**, already three-of-six unbacked. ***Last out*** is free and carries 終 (*zhōng* — 說文 絿絲也, *"finishing off silk thread"*): **seeing a thing through to its end.** ***"No one's doing"*** was killed the same way — *doing* is 無為's, backed there in ten lines, absent here.

**自然 keeps the locked wording, and the reason is arithmetic.** ch 17 (*by ourselves*) and ch 25 (*being what it is*) already depart from it: **two of five occurrences do not show the phrase.** *On its own* would make a sixth wording and produce exactly the invisibility the entry exists to prevent. **When a rare term has already spent its exceptions, the next occurrence pays the locked price.**

**When two commentators split, let the chapter's own imagery break the tie.** 飄風 and 驟雨 are **too much at once**, and 河上公 draws the moral — 言疾不能長，暴不能久也, *"the rapid cannot be long, the violent cannot endure."* Excess against sparseness, not loud against quiet. 王弼's audibility reading keeps 希 at ch 14 (*the inaudible*) and ch 41 (*"can barely be heard"*).

**The glossary entry had argued for the old line and was half right — logged as a finding, not a footnote.** `glossary/ziran-自然.md` defended *"for"* on the ground that 自然 is **the ground, not the consequence**. That reasoning stands. What it could not do was supply a subject without inventing 物, and its own flag on the line — *"English has no predicate slot that fits it; a strain case"* — was correct. Per `CLAUDE.md`: **the diagnosis was right, the rendering was not.** Both files now say so.

**得 (*dé*) → *gets*, not *receives*.** 說文 行有所得也, *"walking and getting something,"* from 彳 (*chì* — a step): active acquisition. The plain word is what makes the third line bite — **loss too gladly gets them.**

### Riders opened, not closed

**同其塵 at ch 4 and ch 56** reads *"merges with the dust"* / *"merge with the dust,"* and **ch 56's 玄同 reads *"the profound union."*** These are 同 used **transitively** (to make oneself the same as) rather than the stative 同於X settled here, so they may take a licensed flexion rather than the same English — but three of the five Englishes are still standing. Tracked on T2-25's row; **ch 4 and ch 56 are the named riders.**

---

## 同 finished — ch 4 and ch 56, 2026-09-03

*`WORKLIST.md` T2-26, the rider ch 23 left. Closed the same day it opened.*

**The finding that decided it: 同 occurs twice in ch 56, two lines apart, and the English used two unrelated words.** 和其光，**同**其塵。是謂玄**同** had read *"merge with the dust"* and *"the profound union,"* which hides the chapter's own move — **the practice and the name for it are one word.** Now: ***be the same as the dust. This is called profound sameness.***

**河上公 (*Héshàng Gōng*) glosses 同其塵 with 同's own opposites**: 不當自**别殊**也 — *"one should not set oneself apart as **separate** and **distinct**."* 别 (*bié* — to separate), 殊 (*shū* — distinct). **王弼 (*Wáng Bì*) makes the couplet a matched pair**: 和其光 is 無所**特顯** (*"nothing specially displayed"*), 同其塵 is 無所**特賤** (*"nothing specially despised"*) — do not stand out above the light, do not hold yourself apart from the dust. ***Merge* read as self-dissolution**, which is not what either says.

***Union* was 合's English.** The reverse check returns two lines; the other is ch 55's 牝牡之**合** (*"the union of female and male"*), where 合 (*hé* — to join) genuinely means union.

***Profound sameness*** because **是謂玄同 is the same formula as 是謂玄德** (*"This is called profound integrity,"* ch 10, 51, 65). Same frame, same English shape. 河上公 reads 玄 here as 天 (*tiān* — sky): 玄，天也…是謂與天**同道**也, *"of the **same way** as sky"* — 同 again, inside his gloss of the compound.

### The test that settled the word, and it generalizes

***"Share the dust"* was the better English and lost anyway.** Short, idiomatic, free in the reverse check, and it fits both grammars. It fails because **it gives no noun for 玄同** — 同其塵 and 玄同 would come apart again two lines later. **When one character appears twice in a chapter in different grammatical slots, the rendering must survive both slots; the more elegant word that survives only one is the wrong word.** That is the reverse check's structural cousin: not *is this English backed by its character*, but *does this English still work at the character's next appearance*.

**The cost, paid openly:** *is the same as the dust* is the one stative verb in ch 4's run of actions — *blunts, untangles, dims, is*. Accepted for one English on one character across ch 4, 23 and 56.

### Left standing, and named

**和其光 → *"dim your own light"* is the commentator's word, not the text's.** 說文 makes 和 **相譍也**, *"to answer one another"* — the same 應 (*yìng* — to answer) as 河上公's 同聲相應 at ch 23 — and *dim* comes from his 當和之使闇昧. `glossary/ming-明.md` glosses ch 4 and ch 56 together this way, so it is settled rather than sloppy. **But 和 and 同 are a pair and only one of them has been repaired**, and the pair is a resonance pair in both commentators.

**ch 1's 同謂之玄 still reads *"Together."*** 同's fourth English, and *together* can be heard as *jointly they form one thing* rather than *both alike are so called*. Opened as T2-27.

## Ch 16 · 致虛極，守靜篤 — "Go totally empty. Hold steadily to stillness."

*(2026-09-05, Pass D, `WORKLIST.md` D16 · T1-6.)* *(was: "Attain emptiness. / Embrace stillness.")*

**Five English words for six characters, and two of the six were missing.** 極 (*jí*) and 篤 (*dǔ*) had no English at all, and 守 (*shǒu*) was wearing 抱 (*bào* — to embrace)'s word — *embrace* runs seven lines, five of them 抱, and the other two were both this chapter.

**Both opening lines hide a gait, and that is the finding.** 致 (*zhì*) is 夊 (*suī* — a dragging foot) beneath 至 (*zhì* — to arrive); 說文解字: 送詣也, *"to send all the way there."* 篤 (*dǔ*) is 說文 **馬行頓遟** — *"a horse's gait, halting and slow"* — from 馬 (*mǎ* — horse) with 竹 (*zhú* — bamboo) for sound; earnest, thick and deep all come off that plod. The couplet is not two achievements. It is one instruction about how far and how slowly, and *attain* and *embrace* had made both of them prizes.

**極 belongs to the reacher, not to the emptiness.** 極's original graph is 亟 (*jí*), a standing person with one stroke above the head and one below the feet — 極于頂, 極于踵. Add 木 (*mù* — wood) and it becomes 棟 (*dòng* — the ridgepole). So the 極 in 致虛極 measures how far *you* go, not how big the hollow is. This is what dissolves the apparent paradox in the line: *complete emptiness* measures the emptiness, and an emptiness has no measure; 極 measures a body, and a body's reach is definite. See `glossary/ji-極.md`.

**虛 must not become *emptiness*.** English *emptiness* is śūnyatā's standard rendering, and 空 (*kōng*) — the character Chinese Buddhism uses for it — has **zero occurrences** in this book. The abstract noun imports a doctrine by six centuries, and ch 16 is the only place in the book where 虛 is forced into the noun slot, so it is the only place the import can happen. See `glossary/xu-虛.md`.

**Three renderings were tried and rejected on evidence, not taste:**

- ***"Attain complete emptiness."*** — *complete* is 成 (*chéng* — to complete)'s English in **six lines** (ch 2, 34, 41, 45, 51, 63), and 成 has zero occurrences in ch 16. Same defect class as this chapter's own *"returns **energy** to its root"* with no 氣 (*qì* — vital breath) present.
- ***"Empty yourself, all the way."*** — *yourself* is an insertion the Chinese does not license, and the comma is a seam the Chinese does not have: 致虛極 is three characters in one uninterrupted breath.
- ***"Reach the empty all the way."*** — *the empty* re-nominalizes 虛 more quietly, and the reverse check puts it at ch 11's *"the empty spaces cut into walls,"* which is 無 (*wú* — absence), a locked term.

**Why *go*.** It carries 致's foot, it works across the 致/至 fork (see `notes/manuscript.md`), and it is already this book's idiom for entering a state: *go muddy* at ch 49, *goes hoarse* at ch 55, *go hungry* at ch 75. **And *totally empty* keeps the exhaustion 極 needs** — both commentators gloss 極 with 窮 (*qióng* — to use up), and a thing that goes totally empty has run out. 虛 supplies the container; *totally* only has to mark completion.

**Why *hold **to***, and it matters more than the word count.** Bare *hold* is the most overloaded verb in the manuscript — **21 lines across five characters**: 守 (ch 5, 32), 執 (*zhí* — to grasp, ch 14), 保 (*bǎo* — to guard, ch 15), 有 (*yǒu* — to have, ch 59), 持 (*chí* — hold in the hand, ch 64). That pile is `WORKLIST.md` T2-19 ★, and 守 is the member it names. *Hold to* is currently clean — ch 28 three times and ch 37, all 守 — so it is the one form keeping 守 separable. The graph agrees: 守 is 宀 (*mián* — a roof) over 寸 (*cùn* — the standard measure), 說文 守官也, *"to hold an office."* Staying at your post, not taking hold. Two chapters over, the book says 執者失之 — *"those who grasp it lose it."*

**The shape, and what it cost.** The Chinese puts both degree words last — 致虛**極** / 守靜**篤** — and 王弼 binds them into one compound across the two lines, 物之極篤, which is only audible because they sit in matching slots. The English moves both to the middle: *Go **totally** empty / Hold **steadily** to stillness*. **The slot moved; the match survived**, and that is the trade — a plainer line in exchange for the line-final position. *Steadily* was chosen over *deeply* because *deep* already carries 淵 (*yuān* — a deep pool) at ch 8 and 36 and 深 (*shēn*) at ch 15, 21, 59 and 65, and 淵 is itself unsettled (T2-24).

## Ch 16 · the 容→公→王→天→道→久 chain — one broken link, not six

*(2026-09-05, Pass D, `WORKLIST.md` D16.)*

**乃 (*nǎi* — then) keeps *leads to*.** *(Shalom's call, and the argument against it was overstated.)* The charge was that five identical *leads to* build a causal ladder — the mechanistic overlay. But both commentators read the chain exactly that way, with 則 (*zé* — if/then): 王弼 (*Wáng Bì*) 無所不包通**則**乃至於蕩然公平也, 河上公 (*Héshàng Gōng*) 無所不包容**則**公正無私. English *leads to* covers natural consequence as readily as manufacture — opening your eyes leads to sight — and that is what 則…乃至於 says.

*(乃 does read four ways across its twelve lines: leads to (16 ×5), at last (28), becomes (54 ×5), only then (65). It is a particle rather than a content word, so it is left alone unless it earns a Pass E row.)*

**The real defect was 容 (*róng* — to contain), rendered twice.** *"The capacity to embrace the totality"* and then *"Embracing all"* one line later, where the Chinese repeats the identical character. That breaks 頂真 (*dǐng zhēn* — the tail-head chain, where each clause opens on the word the last one closed with) at its **first** link. Checking link by link, the other four were already clean: 公/公, 王/王, 天/天, 道/道. **One fix, not a rewrite.**

**容 is a roof over a valley.** 說文解字: 盛也。从宀、谷 — *"to hold, as a vessel holds. From 宀 (mián — a roof) and 谷 (gǔ — a valley)."* Both commentators gloss with 無所不包 (*wú suǒ bù bāo* — "there is nothing it does not enfold"): 王弼 無所不包通也, 河上公 无所不包容也. **That is what licenses *everything*** — it is supplied, but it is what 無所不 says, and the word is otherwise unused in the manuscript.

Repairing the link removed three imports in one move: **create** (生 *shēng*'s, and `check_locks.py` had been flagging it), **embrace** (抱 *bào*'s — seven lines, five of them 抱), and **totality**, which rendered nothing.

**久 → *what endures*, not *what lasts*.** *(Shalom's correction, and the evidence is stronger than register.)* **Ch 7 puts both characters in one line and splits them by position**: 天長地久 → *"The sky is lasting, the earth enduring,"* and 長且久 → *"Lasting and enduring."* **長 (*cháng*) holds *lasting*; 久 (*jiǔ*) holds *enduring*.** A proposed *what lasts* would have put 久 on 長's English inside a book that distinguishes them explicitly.

*Noted for a future 長/久 pass, not fixed here: 長 wears* endure *at ch 22 (不自矜故長) and ch 24, which is the same collision running the other way.*

**Two invented words removed.** *"The open sky"* twice — 天 is locked to *sky* as a tier, ch 25 already reads plain *the sky*, and *open* rendered no character. And the closing line was opening lowercase, reading as a fragment hanging off the Tao rather than as the chapter's own last sentence.

**王 (*wáng*) left standing as *sovereignty*.** It is what the lock says, and it is the one rung where the commentators genuinely split — 王弼 de-politicizes it (蕩然公平則乃至於無所不周普也, *"vast level impartiality then arrives at being nowhere not universally pervading"*), 河上公 politicizes it (公正無私可以為天下王). `glossary/wang-王.md` describes ch 16 as *"a stage in a sequence… no person at all"* and then assigns an office word, so the entry disagrees with itself. Owed its own decision.

## Ch 16 · 公乃王 — 王 → "supreme authority," and why *sovereignty* was the overlay

*(2026-09-05, Pass D, `WORKLIST.md` D16. Shalom's call.)* *(was: "Impartiality leads to sovereignty.")*

**The rung where the commentators genuinely split.** 王弼 (*Wáng Bì*) takes no person from it: 蕩然公平則乃至於**無所不周普**也 — *"vast level impartiality then arrives at being nowhere not universally pervading."* 河上公 (*Héshàng Gōng*) takes an office: 公正無私**可以為天下王** — *"impartial and without private interest, one can become 王 of 天下 (tiān xià — under-sky, the world)."*

**Why *sovereignty* had to go, and it is the entry's own test.** `glossary/wang-王.md` rejects *monarch* because it *"carries the constitutional apparatus of a much later world."* **Sovereignty is that apparatus** — Bodin (1576), Hobbes (1651), the modern nation-state's central concept: territorial supremacy, legitimacy, non-interference. A heavier anachronism than the word rejected for anachronism, and it survived two passes because it *sounds* abstract rather than regal. Now on 王's `forbidden:` list.

**Why not the obvious alternatives.** ***The leader*** carries six lines already and **not one has a ruler-character** — five are ch 17's 太上 (*tài shàng* — the highest) and 其次 (*qí cì* — the next) ×3, where *leaders* is wholly supplied. It also inverts the word: ch 66 has 江海…能為百谷王者，**以其善下之**, rule by staying below. ***The ruler*** is better — ch 78's 天下王 already reads *"the ruler of the world"* — but it collides with 君 (*jūn* — lord) at ch 26, still open as T2-6, and its plural is 侯王's across six lines, so a reader files ch 16's 王 in the political stratum and 河上公's reading wins silently.

**The cost of *supreme authority*, accepted with eyes open.** Two soft collisions: 威 (*wēi* — overawing force) carries *authority* once at ch 72, and 上 (*shàng* — upper) carries *supreme* once at ch 31, buried in the rank-title 上將軍 (*shàng jiāng jūn*). Both are single occurrences in chapters containing no 王. **An inconsistency is a smaller fault than an overlay**, which is the whole of the argument. *Supreme rule* was offered as a variant closing the 威 collision, since *rule* is already 王's own English at ch 66 — declined, because it trades one collision for 宰 (*zǎi*) at ch 10 and 51, and because it names an activity where the chain's other rungs are states.

**What it buys:** no person, so 容 → 公 → 王 → 天 stays a widening of scope rather than a ladder to a throne, and the chain's climb from 天下 (*tiān xià* — under-sky) to 天 (*tiān* — sky) stays visible.

## Ch 16 · 夫物芸芸，各復歸其根 — the peak and the turn are adjacent

*(2026-09-05, Pass D, `WORKLIST.md` D16 · T1-13.)* *(was: "Multitudes flourish, / Each returns energy to its root.")*

**Four faults in two lines**, three of them the same defect class: an English attached to a character the chapter does not contain. **物 (*wù* — things) deleted**, so the restatement of 萬物 from three lines above is invisible. ***Multitudes*** is 眾 (*zhòng* — the crowd)'s, and 眾 is absent — doubly invisible to `check_locks.py`, since 眾's `forbidden:` list carries *"the multitude"* and the line said *Multitudes*. ***Energy*** is 氣 (*qì* — vital breath)'s, also absent.

**芸芸 names a peak, and the placement is the teaching.** 河上公 (*Héshàng Gōng*): 芸芸者華葉盛 — *"flowers and leaves at their fullest."* Maximum display sits immediately before the return, which the book states outright elsewhere in identical words at ch 30 and ch 55: 物壯則老, *"things at their prime grow old."*

**Two candidates rejected, and the reasons generalize.** ***In full leaf*** — 芸's radical is 艸 (*cǎo* — grass) and its 說文 entry quotes the 淮南子 that 芸艸可以死復生, *"the 芸 plant can die and live again,"* which is a real resonance with the chapter's subject. But **物 is general**, and an English that commits it to foliage makes all things plants; 河上公's gloss was explaining the word, not asserting the world. ***Prime*** — it is 壯 (*zhuàng*)'s word, 壯 is absent here, and **ch 30 and ch 55 both render 物壯則老 as the identical sentence**, so borrowing it would read as a quotation of a formula ch 16 does not use. *(A concept can travel between chapters when its English cannot.)*

**復歸 → *returns again*, and ch 28 had already decided it.** The compound runs seven lines — 14, 16, 28 ×3, 52 — and ch 28's Pass D rewrite named *"復歸於 three shapes"* as a defect and unified them to **"Return again to X."** 歸 carries *return*, 復 carries *again*. 說文解字 keeps them apart: 復 往來也 (*"going and coming"*), 歸 女嫁也 (*"a woman marrying"* — going to the house that is now hers). ***Returns home*** was proposed and dropped: *home* does render 歸 rather than inserting anything, but it matches no other line in the formula, and consistency inside a seven-line compound outranks a better single line. *(No character reads two ways: 歸 alone stays* return *at 歸根曰靜, and* again *appears only inside the compound.)*

**What 歸根 means, since the passage turns on it.** 根 is 說文 木株也 — **the stump**, the stock left in the ground when the visible growth is gone. Not an origin, not a source. The text then defines that state itself: 歸根曰靜, *"returning to the root is called stillness."* 王弼 (*Wáng Bì*) supplies the frame — 凡有起於虛，動起於靜。故萬物雖並動作，卒復歸於虛靜 — *"all presence arises from emptiness, all movement arises from stillness; so although the countless things all rise and act together, in the end they turn back and come home to emptiness-and-stillness."* 河上公 reads the same motion biologically: 枯落…更生, *"wither and fall… born again."*

**It is not a euphemism for dying.** The chapter has the speaker *watching* it — 吾以觀復, *"by this I watch the returning"* — and no one watches their own death. Where mortality does enter, the chapter names it plainly at the close: 没身不殆.

## Ch 16 · 是謂復命，復命曰常 — "returning to what is given"

*(2026-09-05, Pass D, `WORKLIST.md` T2-18. Shalom's call.)* *(was: "returning to what **was** given.")*

**One word, after four candidates failed.** The change is *was* → *is*, and it is the whole of it.

**復命 is a name, not a further step.** Chapter 16 describes **one event** and names it four times, each name becoming the next line's subject: 各復歸其根 → 歸根**曰**靜 → 是謂**復命** → 復命**曰**常 → 知常**曰**明. 曰 (*yuē*) is *"is called."* Nothing new enters at 復命; the chapter is handing a second name to the returning it has just shown, so a motion you can watch in a field becomes a thing you can know. **That fact is what makes the term legible, and it is what the rendering has to respect.**

**Why the present tense.** *What was given* puts the giving in the past, inside a naming chain whose other members — 靜 (*jìng* — stillness), 常 (*cháng* — the ever-present) — are timeless. *What **is** given* is ongoing: what any thing is given, always. It reads straight into 常 on the following line, where a past-tense clause fought it.

**Why the passive stays.** The objection that it *implies a giver* is right, and the giver belongs there. 命's graph has a mouth in it — 說文解字 使也。从口从令, and 令 is 發號也, *"to issue a call."* What this edition strips is **naming** the speaker: *mandate* names Heaven, *destiny* names a plot, *fate* names the Moirai. A passive admits the speech and declines to say whose, which is exactly what the Chinese does.

**The four that failed, and the reasons generalize:**

- ***returning to the allotted course*** — a *course* is a path you run, and the chapter's event is a thing **finishing** one. 命 is not a path; everything in the graph is a moment. It also passed the hymn test comfortably, which is the warning sign, not the recommendation.
- ***returning the charge*** and ***returning the message*** — both read 復命 **transitively** (hand the commission back), which is a real idiom but one **neither commentator takes**. `CLAUDE.md`'s tie-breaking order puts the commentaries above this edition's ethos and above poetic intuition, and both renderings were arguing underneath it. Both also need an antecedent the chapter never supplies — *which* charge, *which* message — and *the message* carries the English sense of *the moral*.
- ***returning to what is*** — caught by the reverse check in an unusual form. *What it is* is already **自然 (*zì rán* — of itself)**'s English at ch 25, and **ch 51 sets 自然 against 命 in a single clause**: 夫莫之命而常自然, *"no one 命s it, and it is always 自然."* Rendering a character with its own antonym's English collapses the antithesis from the inside. **This is the reverse check's sharpest use so far** — not an English on an absent character, but an English on the character's opposite.

**Method note worth keeping.** Three of the four failures were mine, and all three came from pulling toward the envoy idiom — a reading the graph and the classical usage support but the commentaries do not. The tell was that each new candidate fixed one fault and introduced another; when that happens for three rounds, the reading underneath is usually the thing at fault, not the wording.

## Ch 35 · the whole chapter — one argument, cut in half and mystified

*(2026-09-05, Pass D, `WORKLIST.md` D35 · T1-12. The overdue 執 rider from ch 28.)*

**The chapter was drafted in a private vocabulary and the reverse check found it whole.** *route*, *routes*, *embody*, *allure*, *stability*, *guests*, *inexhaustible*, *safety* — eight words, one line each, all of them here and nowhere else in the book. That is the signature of a chapter drafted without the rest of the book open, and every one of them was covering a decision that had not been made.

### The reading: 不足 is *not enough*, not *cannot*

*(was: "Look for it. It can't be seen. / Listen for it. It can't be heard.")*

**The stanza break between 過客止 and 道之出口 was destroying the chapter.** Both commentators run those lines as a single argument. 王弼 (*Wáng Bì*), unbroken: 樂與餌則能令過客止，而道之出言淡然無味。視之不足見，則不足以恱其目；聽之不足聞，則不足以娛其耳 — *"music and food can bring a passing traveller to a halt; but the Tao coming out in speech is bland, without flavour. Look at it: not enough to see, and so not enough to please the eye. Listen: not enough to hear, and so not enough to amuse the ear."*

So the music-and-food line is not an aside about worldly distraction. **It is what the Tao is being measured against, and the Tao loses.** Music and food stop a traveller for an evening. The Tao stops nobody, because it has nothing to catch anyone with.

**不足 (*bù zú*) means *not enough* in all six other chapters that use it** — 信不足焉 (17, 23), 以為文不足 (19), 不笑不足以為道 and 廣德若不足 (41), 不足以取天下 (48), 補不足 (77). Ch 35 was the only *can't*. 足 is 說文解字 人之足也 — *"a person's foot"*; *enough* is the loan.

**And the substitution collided with ch 14, which is the chapter that does say *cannot*.** Ch 14 reads 視之**不見** — no 足. Ch 35 reads 視之**不足**見. Our English gave both chapters the same sentence, so a reader could not see that ch 35 had said something different. *"It can't be seen"* is the apophatic register, and ch 14 owns it, with its own three words for it — 夷 (*yí*), 希 (*xī*), 微 (*wēi*). **Ch 35 is doing something plainer and much stranger: the Tao is a bad advertisement.** It is under-seasoned. There is not enough there to hold your eye. That is deflationary and close to funny, and our English had turned it into a hymn.

**河上公 (*Héshàng Gōng*) reads it the other way** — 足，得也 (printed 足德也): *"足 means 得 (dé — to attain),"* so *"you cannot attain seeing it,"* which is what we had. **The commentators genuinely split here.** We follow 王弼 because his is the only reading that gives 樂與餌 any work to do, and because 不足 in six other chapters agrees with him.

### 執大象 → *Grasp the great image* — the mirror with ch 29

*(was: "Embody the great form.")*

**Ch 29 and ch 35 are a matched pair and our English hid it.** Ch 29: 天下神器…不可**執**也 — *"天下 (tiān xià — under-sky, the world) is a sacred vessel… it cannot be 執-ed."* Ch 35: **執**大象，**天下**往 — *"執 the great image, and 天下 goes to you."* **Same verb, same object-word, opposite instruction. You cannot take hold of the world; take hold of the great image, and the world comes to you of its own accord.** Ch 29 read *grasped* and ch 35 read *Embody*, so the two lines could not be seen answering each other.

**執 (*zhí*)** is 說文 捕罪人也。从丮从幸 — *"to seize a criminal; from 丮 (jǐ — two hands thrust out to take)"* and 幸, which in this graph is 㚔 (*niè*), **the manacle**. The book uses that sense outright at ch 74: 吾得執而殺之, *"I could seize them and put them to death."* *Embody* renders none of it; it replaces an act of the hands with a state of the body.

***Grasp* is the 強 (*qiáng*) solution applied to 執.** English *grasp* is double the way 執 is — you grasp an idea, and you grasp at what is not yours — so it carries no verdict and can be the error at 29 and 64 and the instruction at 14 and 35 without our English settling which. It already carries most of 執's load. **This does not close T2-19**, which is the whole 守/執/保 family; it settles 執 at this one line and leaves the family for Pass E.

### 大象 → *the great image* — our own ch 41 had already decided it

大象 (*dà xiàng*) occurs twice. **Ch 41 reads 大象無形 and we translate it *"the great image has no form."*** Ch 35 had the identical compound as *"the great **form**"* — grasping the great form of the thing ch 41 says has no form. 形 (*xíng* — shape) is a different character and takes *form* at ch 41 and ch 51.

**象 is an elephant.** 說文: 長鼻牙，南越大獸，三秊一乳，象耳牙四足之形 — *"long nose and tusks, the great beast of the far south; it bears young once in three years; the graph pictures an elephant's ears, tusks and four feet."* **韓非 (*Hán Fēi*, d. 233 BCE), the oldest commentary there is**, explains how it became the word for an image, at ch 14: 人希見生象也，而得死象之骨，案其圖以想其生也，故諸人之所以意想者皆謂之「象」也。今道雖不可得聞見，聖人**執**其見功以處見其形 — *"people seldom see a living elephant, but they come by the bones of a dead one, and going on that outline they picture it alive; so whatever people form in the mind as a picture is called 象. Now although the Tao cannot be come by through hearing or seeing, the sage **grasps** what shows of its working, and thereby places and sees its shape."* **象 is the picture you build of what you have never seen, from the traces it left** — and 韓非 puts 執 on it himself, in the positive valence.

### 往 → a verb again, and the mouth stays on the page

***routes to you* / *This route*** — network vocabulary, the mechanistic register the razor exists to strip, and it turned 往 (*wǎng*) into a noun the Chinese does not have. 說文: 往 之也, *"to go,"* from 彳 (*chì* — a step). Its only other appearance, ch 80's 不相往來, we already render as a plain verb of going. 王弼: 主若執之則天下徃也, *"if the ruler holds it, then the world goes to them."*

**道之出口 → *The Tao is bland in the mouth*** *(was: "Attempt to speak the Tao.")* — *"attempt to"* was supplied, and a first replacement, *"the Tao comes out of the mouth,"* was rejected by Shalom as reading like expulsion. It was: 出 is 說文 進也。象艸木益滋，上出達也 — *"to advance; it pictures grass and trees growing ever more abundantly, pushing up and out to the top."* A sprout, not a discharge.

**口 (*kǒu* — mouth) occurs exactly twice in the book, ch 12 and ch 35, both times in a line about taste — and the word *mouth* had appeared zero times in our English.** Ch 12 renders it *palate*, which quietly picks eating and drops speech. Ch 35 is the one place 口 cannot be allowed to pick, because what passes it is the Tao, and the commentators split on the direction: 王弼 rewrites 出口 as 出言 (*"coming out in words"*), while 河上公 keeps the organ and doubles it — 道出入於口，淡淡非如五味有酸鹹苦甘辛也, *"the Tao goes out at the mouth and in at the mouth; bland, bland, not like the five flavours, which have sour, salty, bitter, sweet, pungent."* ***In the mouth*** leaves that fork open, is ordinary English for speech and for taste both, and gives 口 its first actual mouth in this book. *"Spoken aloud"* was the runner-up and was declined because it settles the fork on 王弼's side.

**Word order, Shalom's call:** *"The Tao **is bland in the mouth**"* over *"The Tao **in the mouth** is bland."* The three lines beneath it all take the Tao itself as object — 視之／聽之／用之, *look at it / listen to it / use it* — so the lack is predicated of the Tao and the organ is only where you meet it. The restrictive order would have set the line apart from the three it belongs with. **Mouth, eye, ear: three organs, three helpings of nothing.**

### 安平太 → *at rest, utterly even* — and the parallelism that was never there

*(was: "It offers safety, peace, and stability.")* The fork is in `notes/manuscript.md`. **太 never stands alone in this book** (太上 at 17, 太牢 at 20), so three English adjectives invent a third item: 安平 is the pair, 太 the intensifier. An earlier attempt, *"at rest, level, at ease,"* was caught twice over — Shalom heard the broken parallelism (two prepositional phrases around a bare adjective), and the reverse check found ***level* is 夷 (*yí*)'s word**, ch 53's 大道甚夷, *"the great Tao is very level,"* with 夷 absent from ch 35.

**Shalom's line, and it is one sentence because the Chinese is** — 往而不害，安平太。takes a comma, then the stop. *"It comes and is not harmed. All is at rest, utterly even"* broke it in two and then had to supply a subject, *All*, that the text does not have; 天下 (*tiān xià* — the world) stays the single subject across both lines, which is what the repeated 往 is for. **It also maps beat for beat** — 往／不害／安／平太 → *comes / unharmed / at rest / utterly even*. 河上公 reads a consequence instead, with a 則 (*zé* — then) he supplies: 萬物歸往而不傷害，則國安家寧, *"the countless things turn toward them and are not harmed, then the state is at rest and the household at peace."* The text has no *then* and no new subject.

安 (*ān*) is 說文 靜也。从女在宀下 — *"stillness; a woman under a roof."* ***Safety*** was its outlier: 安 reads *at rest* at ch 64 (其安易持), *the calm* at ch 15, *restful* at ch 80. 平 (*píng*) occurs once in the whole book; 說文 語平舒也 — *"speech level and unhurried."* **Cost accepted:** *even* is a common English word, so the reverse check on it will be noisy from now on.

### 過客 → *a passing guest* — the fault was the number, not the character

*(was: "The allure of music and fine food causes passing guests to stop." An intermediate draft read* the passer-by, *and was wrong.)*

**客 (*kè*) occurs three times and our English preserves it once** — *guest* at ch 15, nothing at all at ch 69, and here. *Passing guests* read as a contradiction in English, since a guest has already stopped, and the first fix swapped the character out for *the passer-by*. **The contradiction was in the bare plural, not in the word.** Singular and with an article, the stiffness goes, and what tension is left is the line's own subject: 止 (*zhǐ*) is the moment a traveller becomes a guest.

**說文 unifies all three uses:** 客 寄也。从宀各聲 — *"to be lodged; from 宀 (mián — a roof),"* and 寄 (*jì*) is 託也, *"entrusted to another's keeping."* **客 is one who is under a roof that is not theirs.** Its pair 主 (*zhǔ*) is 鐙中火主也 — *"the flame in the lamp."* The one whose fire it is, and the one who came to it. 河上公 reads two of the three through that pair: at ch 15, 如客畏主人，儼然無所造作也, *"like a 客 in awe of the 主人 (zhǔ rén — the master of the house); solemn, making nothing of their own"*; at ch 69, 客者，和而不倡, *"the 客 harmonizes and does not lead off."*

**Ch 69 is the worse problem and is logged open.** 吾不敢為主，而為客 reads *"I do not push to move first. I move second"* — that is 河上公's gloss 主，先也 (*"主 means first"*) rendered **instead of** the text, and both characters vanish. `CLAUDE.md`: a commentator's gloss is not the text. On the battlefield the 客 is the army standing on ground that is not its own, which is what licenses 不敢進寸而退尺 in the next line.

**止 (*zhǐ*) and 足 (*zú*) are the same picture, and 許慎 says so**: 說文 止 下基也。象艸木出有址，故以止爲足 — *"the base below; it pictures grass and trees emerging with a footing, so 止 is taken for 足."* The traveller's foot stops; the next three lines are about there not being **enough** of a foothold. Not forced into the verse; recorded because it is the chapter's own rhyme.

## Ch 11 · the whole chapter — the repetition *is* the argument

*(2026-09-05, Pass D, `WORKLIST.md` D11 · T3-3.)*

**One sentence, three times, over three unlike objects.** 當其無 (*dāng qí wú*) repeats letter for letter, and so does 有X之用. Only the object changes: 車 (*chē* — cart), 器 (*qì* — vessel), 室 (*shì* — room). Our English changed everything else instead:

| Chinese, identical ×3 | was |
|---|---|
| 當其無，有**車**之用 | *"Through the **emptiness at its center**, the cart **can roll**."* |
| 當其無，有**器**之用 | *"Through the **emptiness it contains**, / A clay vessel **becomes useful**."* |
| 當其無，有**室**之用 | *"Through the **empty spaces cut into walls**, / A room **becomes useful**."* |

*At its center*, *it contains*, and *cut into walls* are all supplied, and *"the cart can roll"* renders 有車之用 (*"there is the use of the cart"*) as something else. **The reader is meant to hear the same sentence three times over a wheel, a pot and a room, and feel it click.** Ours said something different each time, so there was nothing to click. **Eleven lines for eleven, and the middle line of every stanza is now identical on the page.**

**No check could find this.** `repeated-formula` compares segments **across** chapters; 當其無 repeats three times **inside** one, and `concordance.py --formulas` did not list it either. **Both tools were repaired the same day, and this is the chapter that exposed it** — `DISCOVERIES.md` §6 for the finding, `PLAN.md` → *What Chapter 11 taught the tools* for the harness record.

### 無 → *in what is not there*, and 有 → *presence*

*(was: "emptiness" ×2, "empty space" ×2, "filled space".)* **This is the chapter `glossary/wu-you-無有.md` names as its own test case** — *"the moment the grammar becomes metaphysics, Chapter 11 stops making sense."* It had four 無 and four 有 and used the locked English for neither. *Emptiness* is 虛 (*xū*)'s forbidden word and **虛 is not in this chapter**; the checker saw it only as `info`, because 無's `forbidden:` list carries *nothingness* and *the Void* but not *emptiness* or *empty space*. **Those two should go on it** (`WORKLIST` T5-3).

*In what is not there* is the entry's own licensed wording rather than a new coinage. 無 is 說文 亡也 — *"gone"*, from 亡 (*wáng* — to flee, to lose). Not a void; a thing that is not there.

**當 is *right where*, not *through*.** 說文: 當 田相值也 — *"fields matching each other,"* from 田 (*tián* — a field). It locates; it is not instrumental. *Through* made the absence a means, which is the mechanistic reading of a line that is only pointing at a place.

### 利 → *advantage* — a locked rendering applied for the first time

`glossary/wu-you-無有.md` carries `covers: 利 → advantage`. **The word *advantage* appeared zero times in the manuscript.** The lock existed on paper and had never touched the text; here it read *"potential,"* which renders nothing. This is the second direction of a lock, which no rule can test — `CLAUDE.md`'s note on `--english`.

**利 wants its own entry and is logged open.** Nine chapters, three jobs: *benefit*, bound to 害 (*hài* — harm) as its antonym at 56, 73 and 81; **sharp**, at 利器 (36, 57) and 利劍 (53), which is the 說文 sense — 銛也。从刀, *"sharp; from 刀 (dāo — a knife)"*, the graph being a blade cutting 禾 (*hé* — grain); and *advantage*, what the edge gets you, here and at ch 19's 絕巧棄利.

**王弼 makes the closing couplet dependent, not merely paired:** 言無者，有之所以為利，皆頼無以為用也 — *"as for absence: what makes presence advantageous is that all of them rely on absence for their use."* The English keeps them side by side and lets the reader do that, rather than inserting the dependency.

### What the graphs give the chapter, kept out of the verse

- **室 (*shì* — room) is glossed by fullness.** 說文 實也。从宀从至。至，所止也 — *"solid; from 宀 (a roof) and 至 (to arrive); 至 is where one stops."* The room's own character means *full*, and the chapter's claim is that its use is where it is empty.
- **轂 (*gǔ* — hub) is defined by what converges on it**: 輻所凑也, *"what the spokes converge on."* 王弼 turns that back: 轂所以能統三十輻者，無也 — *"what lets the hub unify the thirty spokes is absence."*
- **牖 (*yǒu* — window) is 穿壁以木爲交窻也…所以見日** — *"boring through a wall to make a latticed wooden window… what you see the sun by."* 戶 (*hù* — door) is 半門曰戶, *"half a gate."* Both are holes made on purpose, which is why 鑿 (*záo*) — 穿木也, *"to bore through wood"* — opens the stanza.
- 河上公 adds a reader's note, not a rendering: 古者車三十輻，法月數也 — *"the ancient cart had thirty spokes, modelling the number of the month."*

## Ch 36 · the four clauses are instructions, not laws

*(2026-09-05, Pass D, `WORKLIST.md` D36 · T3-4. Found by `--formulas 36` the day it was built.)*

*(was: "Contraction requires firm expansion. / Weakening requires firm strengthening. / Abolishing requires firm elevation. / Removing requires firm giving.")*

**將欲X之，必固Y之 four times, and four things were wrong with the English at once.** 將欲 (*jiāng yù* — "if you are about to want to") was deleted, so the conditional went. 之 (*zhī* — it) was deleted twice per line, so the thing being handled went. The verbs were nominalized into *Contraction* and *Weakening*, so the acts went. **And 固 (*gù*), an adverb, became the adjective *"firm"* — which produced a "firm expansion," a phrase with no referent.**

**固 means *first* here, and two commentators say so.** 河上公 (*Héshàng Gōng*) glosses all four clauses with 先 (*xiān* — first): 先開張之者，欲極其奢淫 — *"to stretch it open first is to push its extravagance to the limit"*; 先強大之者，欲使遇禍患 — *"to make it strong first is to have it meet disaster"*; 先興之者，欲使其驕危也; 先與之者，欲極其貪心也. Elsewhere in this book 固 is the plain adjective *firm* (55, 59, 67) and once an adverb (58), so the reading is not forced. *(先 carries* first *at ch 7 and is absent here — a soft collision, accepted because 河上公 makes them synonyms in this slot.)*

**韓非 (*Hán Fēi*, d. 233 BCE) settles it with worked examples, which is as close to proof as this book offers.** He is the oldest commentary that exists, and on this chapter he does not gloss — he narrates:

> 吳兵既勝齊人於艾陵，**張之**於江、濟，**強之**於黄池，故可制於五湖。故曰：「將欲翕之，必固張之；將欲弱之，必固強之。」
> — *"Once Wu's army had beaten the men of Qi at Ailing, it **stretched itself out** along the Yangtze and the Ji and **made itself strong** at Huangchi, and so could be subdued at the Five Lakes. Hence it is said: 'if you would draw it in, you must first stretch it out; if you would weaken it, you must first strengthen it.'"*

> 晉獻公將欲襲虞，遺之以璧馬；知伯將襲仇由，遺之以廣車。故曰：「將欲取之，必固與之。」
> — *"Duke Xian of Jin, intending to raid Yu, sent them jade and horses; Zhi Bo, about to raid Chouyou, sent them a great chariot. Hence: 'if you would take it, you must first give to it.'"*

**Sequences in time, with named states as the object.** Not laws about Contraction.

**What the verbs actually are**, since abstraction had eaten all four: 歙 (*xì*) is 說文 縮鼻也, *"to draw in through the nose"*; 張 (*zhāng*) is 施弓弦也, *"to fit the string to a bow"* — a breath and a bowstring, both under tension. 廢 (*fèi*) is 屋頓也, *"a house collapsing."* 興 (*xīng*) is 起也。从舁从同。同力也, *"to rise; from 舁 — lifting hands — and 同; joint effort"* — many hands lifting together, and 與 (*yǔ*) carries the same 舁. 奪 (*duó*) is 手持隹失之也, *"a hand holding a bird and losing it."*

**Neither commentator reads this as a manipulator's handbook, and the English should not either.** 王弼: 將欲除强梁，去暴亂，當以此四者，因物之性，令其自戮 — *"if you would remove the strong and overbearing and rid yourself of the violent and disorderly, use these four: go along with the nature of the thing, and let it destroy itself."* 河上公 reads the same motion as the anatomy of ruin — overextension is how a thing ends. **The lines describe how overreach collapses; they do not recommend deceit.** Left standing rather than resolved, because the Chinese does not resolve it either.

### 利器 → *tools of advantage*, and all three commentators force it

*(was: "The sharp instruments of the state must not be shown to others.")* 韓非: 賞罰者，邦之利器也，在君則制臣，在臣則勝君 — *"reward and punishment are the state's 利器; in the ruler's hands they control the ministers, in the ministers' hands they overcome the ruler."* 王弼: 利器，利國之器也 — *"the tool that benefits the state."* 河上公: 利器，權道也 — *"the way of leverage."* **Unanimous, and none of them a weapon.** *Advantage* is 利's covered rendering in `glossary/wu-you-無有.md`, applied at ch 11 the same day; *edge* was the better line but is already 銳 (*ruì*)'s word at ch 9. *Instruments* also missed 器's lock, which licenses *vessel / tool / implement*. **利器 stands again at ch 57 and is not settled here — T2-33.**

### 淵 → *deep water*, closing T2-24's ch 36 half

*(was: "the deep abyss.")* 說文: 淵 回水也。从水，象形。**左右，岸也**。中象水皃 — *"circling water; from 水, a pictograph; **the left and right are the banks**, the middle pictures the water."* **Banked water that turns, not a bottomless place** — which is what made *abyss* backwards and *limitless* wrong at ch 4. 韓非 makes it the element a ruler is held in: 勢重者，人君之淵也…失則不可復得也 — *"positional power is the ruler's 淵; lose it and it cannot be got back."*

***Pool* was drafted and rejected by Shalom** — in modern English it reads as something chlorinated. ***The depths*** was the alternative and lost on the pointing test: it is a register word, and **deep water can be pointed at**, which also makes the fish a fish rather than a symbol.

### 示人 → *shown*

*(was: "shown to others.")* **The audience is inside the verb.** 說文 defines 示 with the very phrase: 天垂象，見吉凶，**所以示人也** — *"heaven hangs down its images, revealing fortune and misfortune; this is how it shows people."* *Remain hidden* was offered and declined: **the danger is in the act of showing, not the state of being seen**, which is 韓非's entire point — 君見賞，臣則損之以爲德 — *"if the ruler shows his rewards, the ministers shave them down and take the credit."* Someone is watching and will use it. Dropping *to others* also keeps the deferred 民/人 question (T4-1) shut.

## Ch 39 · what 得一 means, and the mirror that was inverted

*(2026-09-05, Pass D, `WORKLIST.md` D39 · T3-6. Found by `--formulas 39`.)*

**得一 (*dé yī*) means holding the one thing that makes you what you are — as against living off the quality it produces.** 王弼 states it in a line:

> 用一以致清耳，**非用清以清也**。守一則清不失，用清則恐裂也。
> — *"It is by using the one that clarity is brought about — **not by using clarity to be clear**. Hold to the one and clarity is not lost; use the clarity, and you risk splitting."*

And on the opening: 物皆各得此一以成，**既成而舍以居成，居成則失其母**，故皆裂發歇竭滅蹶也 — *"all things each get this one and are thereby completed. **Once completed they let it go and dwell in their completedness; dwelling in their completedness, they lose their mother**" — and so they all split, burst, cease, dry up, die out, topple.* 河上公 names the one outright: 一，無為，道之子也 — *"the one is 無為 (wú wéi — non-doing); it is the Tao's child."*

**The sky is not clear by being clear.** A thing that has arrived starts running on its own arrival, and that is when it comes apart.

### 得 → *received*, and 王弼 licenses it — Shalom's line

*(was "draw from"; an intermediate draft read "got the one and by it is clear," which Shalom rejected as a calque, and it was: the grammar with none of the meaning in it.)*

***Received* implies a giver, and the giver is in 王弼's own image**: 居成則**失其母** — *"they lose their mother."* **The one is the mother.** So the passive is not imported from outside the chapter; it names the relation the commentary already uses, while declining to say whose giving — the same move made for 命 (*mìng*) at ch 16. `--english "receive"` returns one line, ch 13's supplied *"stoop to receive favor,"* so the word is effectively free. **得 itself stays unsettled: 19 chapters, 30 lines, no entry** (T2-35).

**The past tense is the Chinese's own.** 昔 (*xī* — of old) governs the whole positive list, and the warning half is 將恐 — *"will likely."* An earlier draft used the present in both halves and flattened a shift the text makes. *(昔 is 說文 乾肉也, "dried meat" — the temporal sense is a phonetic loan. 王弼 glosses it 始也, "beginning"; 河上公 往也, "past." We take the plain sense.)*

**Three drafts of the opening line were wrong in the same direction** — *"From the very beginning"* (inherited), then *"Of old"*, then *"From the first"* — all three reaching for a cosmic origin 昔 does not carry. **昔 is 說文 乾肉也**, *"dried meat, cut meat with the sun drying it"*; the temporal sense is a phonetic loan meaning simply *days gone by*, and **the character occurs exactly once in the whole book.**

***In the beginning* was proposed and refused, and it is the sharpest register call in the chapter.** It is Genesis 1:1 and John 1:1 — and the overlay watchlist points at that exact seam, since the Chinese Union Bible renders John's Logos as 道: 太初有道. Over a list of sky, earth, spirit, valley and the countless things it would read as Genesis 1 to any English reader. **The reverse check independently forbids it**: *beginning* is 始 (*shǐ*)'s word at ch 1, 38 and 64, and **始 is not in this chapter.** Its only warrant was 王弼's gloss 昔，始也 — a commentator explaining one character with another, which is the 贅 / 肬贅 fault `CLAUDE.md` names by hand. 河上公 glosses it the other way: 昔，往也, *"past."*

***From the first* failed on Shalom's question — "the first what?"** There is no ordinal in the line. It was 始 in a smaller coat. **The settled line has no ordinal and no origin in it: *"These received the one long ago"*** — 者 (*zhě*) keeps its class-marking work as *these*, and 昔 sits where English carries a past marker, with no once-upon-a-time cadence at the front.

### The mirror was inverted — broken where the Chinese holds, smoothed where it breaks

**Pair five broke in our English while the Chinese held it.** 萬物得一以**生** / 萬物無以**生** — the same character — read *"come into being"* and *"lacked **presence**."* ***Presence* is 有 (*yǒu*)'s locked word and 有 is not in that line.** Now *came to life* / *with no way to live*.

**Pair six was smoothed in our English while the Chinese breaks it.** 為天下**貞** / 無以**貴高** — two different things — both read *"anchor."* **貴高 is the hinge**: it is what 故貴以賤為本，高以下為基 picks up two lines later, and with *anchor* on both sides the turn from cosmology to rank was invisible. *(Other editions insert 貞 and restore the mirror — see `notes/manuscript.md`. We keep the break.)*

***With no way to be X*** is 無以X exactly — *lacking that by which*. It says the loss is **of the means, not of the quality**: the sky does not run out of clearness, it runs out of what was making it clear. *"If the sky lacked clarity"* could not say that.

### 為天下貞 → *serve as the world's standard* — a settled formula we had broken

*(was "became true for the world," which Shalom flagged as odd. It was worse than odd.)* **為天下X was settled on 2026-09-01 closing T2-15**: *"serves as the world's pattern"* at ch 22 and *"serve as the world's ravine / pattern / valley"* three times at ch 28. **Ch 39 carries the identical construction and had a fourth rendering.** 為 (*wéi*) is locked to *do / handle / serve as*, and ch 22's note gives the reason: the sage does not **make** a pattern for anybody, the sage **is** one. *True for the world* also read as a claim about validity rather than a quality of the ruler.

**貞 → *standard*.** 說文 卜問也。从卜，貝以爲贄 — *"to inquire by divination; from 卜, the crack in the shell, with the cowry as the offering."* What is consulted in order to know what is right. *Upright* is 正 (*zhèng*)'s word at ch 57 and 正 sits inside the deferred T4-2, so it is left alone.

**The sixth pair's asymmetry is the Chinese's, and it is marked twice.** That line is the only positive one carrying 為 and 天下 — the other five are bare 得一以X — **and** its quality word 貞 differs from its negative counterpart 貴高. Five pairs match exactly; one does not, and that one is the hinge into 故貴以賤為本，高以下為基. *(Other editions insert 貞 and restore the mirror six for six, at the cost of 貴高 and the hinge; see `notes/manuscript.md`.)*

**How it was missed:** `--formulas` lists 為天下▢ for ch 22 and 28 but not ch 39, because there the phrase sits inside the longer segment 侯王得一以為天下貞. **A frame that does not begin at a punctuation boundary is invisible to segment matching** — logged as `WORKLIST` T5-13.

### 貴 and 賤 are price words, not moral ones

*(was "the noble is rooted in the humble.")* 說文: 貴 物不賤也 — *"a thing not cheap"*; 賤 賈少也 — *"low in price."* **Both are 貝 (*bèi* — cowry) graphs.** *Noble / humble* is the moralized overlay; *prized / cheap* keeps the ledger the characters are written on, and *prized* is already 貴's English at ch 3, 20 and 27. **貴 wants an entry — 15 chapters, 22 lines** (T2-36). 基 → *footing*: 說文 牆始也, *"the beginning of a wall."*

***Natural consequences* is gone.** 自然 (*zì rán*) is not in this chapter, so *natural* was a locked term's word on a chapter that has none of it. 其致之 takes *"Follow it through,"* which holds both readings — 王弼 takes 致 as bringing-about (各以其一致此清寧靈盈生貞), 河上公 as warning (致，誡也，謂下五事也).

### The close: neither jade nor stone

*(was: "Don't strive to chime and shine like polished jade. / **Instead**, clatter and remain rough like common stone.")* **Our English said *not jade, but stone*. Both commentators say *neither*.**

- 王弼: 玉石琭琭珞珞，**體盡於形**，故不欲也 — *"jade and stone, 琭琭 and 珞珞: their substance is used up in their form, and therefore one does not want it."*
- 河上公: 玉少故見貴，石多故見賤。言不欲如玉為人所貴，如石為人所賤，**當處其中也** — *"jade is few and so is seen as precious; stone is many and so is seen as cheap. Do not wish to be like jade, which people prize, nor like stone, which people despise — **one should dwell between them**."*

A single 不欲 governs both clauses; there is no 而 and no 寧 (*nìng* — "rather"). ***Instead* was supplied and inverted the point.** And it matters for the chapter: 貴 and 賤 are the two ends of one scale, so *"be the stone"* merely picks the other end. **Refusing to be priced at all is the deeper move**, which is 王弼's 體盡於形 exactly.

**A strain, named rather than smoothed.** 琭琭 (*lù lù*) and 珞珞 (*luò luò*) have **no 說文 entries**, and their exact sense is not recoverable from anything in `sources/`. *Gleaming* and *common* come from what the two stones **stand for** in both commentaries, not from the graphs; 河上公's edition reads 落落 (*"scattered, lying about in numbers"*) for the second, which supports *common*. Both words are otherwise unused in the manuscript.

**A second strain: 靈 → *numinous* fails the pointing test**, and no candidate survived. *Alive* is 生's, two lines down; *vital* drifts toward 氣 (*qì*). **神 (*shén*) and 靈 (*líng*) both sit in the overlay watchlist's semantic field and neither has an entry** — they want one together, not a decision inside a chapter (T2-37).

## Ch 13 · one word per character, and the chapter's argument appears

*(2026-09-05, Pass D, `WORKLIST.md` D13 · T1-10 · T3-7.)*

**Five characters carry this chapter and our English gave them fourteen words between them.** 身 (*shēn*) appears six times and read *your own body*, *a body*, *the separate self*, *their own person*. 患 (*huàn*) four times as *misfortune* ×3 and *troubles* ×1. 驚 (*jīng*) five times, 貴 (*guì*) three, 若 (*ruò*) **nine**. The argument could not land because the thing it is about kept changing name. Now one-to-one: **身 → body ×6 · 患 → trouble ×4 · 驚 → shock ×5 · 貴 → prize ×3 · 下 → below ×1.**

### 無身 → *if I had no body*, closing T1-10

*(was: "When the separate self dissolves, what troubles could I have?")*

**有 and 無 are the book's central locked pair, and this is the one place it is applied to a person:** 為吾有**身** / 及吾無**身**. Our English rendered the first half *"because I have a body"* and the second *"when the separate self dissolves"* — **destroying the pair on the line that exists to state it.** `check_locks` cannot see this: 無's `forbidden:` list carries *nothingness* and *the Void*, not a clause.

**And no commentator has a self dissolving.** 王弼: 及吾無身，**歸之自然也** — *"returning it to 自然 (zì rán — what is so of itself)."* 河上公 goes the opposite way from Advaita, into the body rather than out of it: 使吾无有身體，得道自然，**輕舉昇雲，出入无間**，與道通神 — *"if I had no body, attaining the Tao's 自然, rising lightly on the clouds, going in and out of the seamless, communing numinously with the Tao."* One returns it to what-is-so-of-itself; the other flies. **Neither merges anything into anything.**

### 貴以身為天下 → *as a way to serve the world* — Shalom's call, and a reception argument

*(was: "one who values the world as their body can be entrusted with the world." An intermediate draft read* "prizes their own body as much as the world," *which was withdrawn — see below.)*

**Two readings of 以身為天下, and they give near-opposite ethics.**

**Reading A — 以A為B, the ordinary frame for *take A as B*:** *take one's own body as the world*, i.e. price it at the world's rate. **Both commentators attach 貴/愛 to the body itself** — 王弼 無以易**其身**, 河上公 人君貴**其身** — and 王弼 makes it a theory of **immunity**: 不以寵辱榮患**損易其身**，然後乃可以天下付之也, *"only when one does not let favor, disgrace, glory or trouble diminish or buy off their own body can the world then be handed to them."* The person nothing can purchase is the one you can trust with the world, which makes the chapter one argument from first line to last: favor and disgrace are the currency, the body is what they buy, and the unbuyable person is immune.

**Reading B — 以身 + verb + 天下:** *with one's body, act for the world.* **Ch 26 supports this structurally**: 以身輕天下, where 輕 (*qīng* — to make light of) is unmistakably a verb with 天下 as its object. Same 以身 + verb + 天下 shape. **And 河上公's second gloss is very nearly the sentence**: 言人君能愛其身，**非為己也**，乃欲為萬民之父母 — *"the ruler who can love his own body, **and not for his own sake**, but wishing to be father and mother to the myriad people."*

**Shalom's call: Reading B, and his reason is about reception, not philology.** Reading A, rendered in English, **lands as egotism**. *"Prizes their own body as much as the world"* reads as narcissism to an English reader whatever 王弼 meant by 無以易其身, and a rendering that arrives as a different vice has failed even where it construes correctly. *(Same class of judgment as the refusal of "In the beginning" at ch 39: what a line lands as is part of whether it is accurate.)*

**What Reading B costs, recorded so a future reader sees it.** 王弼's whole chapter goes — and he is our base text's own commentator. Under B the qualification for power is **devotion**; under A it is **immunity**. The opening movement about favor and disgrace does real work in A (they are the currency the unbuyable person refuses) and much less in B, where devotion is not what favor and disgrace test. **B still coheres**: the trouble is having a body *for yourself*, and turning it to the world is what redeems it — which is exactly 河上公's 非為己也.

**A standing principle this yields.** *Supply what a character means, not what a passage points at* (`DISCOVERIES.md` §5) governs what may be **added**. This adds a second test on what may be **kept**: **a construal that is defensible in the Chinese and lands as a different claim in English has not been translated.** Two of this chapter's decisions turned on it, and so did ch 39's opening line.

### 若驚 and 是謂 — two frames rendered as causes

***Favor and disgrace cause alarm*** made them agents acting on you. **若 is *like*, not *cause***: 寵辱若驚 **equates** favor and disgrace with the shaken state. 驚 is 說文 馬駭也 — *"a horse shying."* Now *"Favor and disgrace are both a shock,"* repeated verbatim at all three places the Chinese repeats it.

***This is why*** for 是謂 is causal, where 謂 (*wèi*) is *to call*. **Eight other chapters render 是謂 as *"This is called"*** (10, 14, 16, 27, 30, 36, 51, 52). Here it governs a whole clause rather than a noun phrase, so it takes *"This is what is meant:"* — the same verb, fitted to the grammar.

**寵為下 → *to be favored is to be below***, replacing the supplied *"You must stoop to receive favor."* 下 → *below* matches ch 61 and 66. The fork with 河上公's 辱為下 is in `notes/manuscript.md`, and it is the fork that decides whether the line says anything at all.

**T2-1 stays open.** 身 is settled *inside this chapter only*; it still reads three ways across ch 7, 9, 44 and 54, two of them in one chapter.

---

## The holding family · 執 · 守 · 保 · 持 — four hands, one English word

*(2026-09-08, Pass E, `WORKLIST.md` T2-19. Raised by Shalom 2026-08-28 at ch 24.)*

Four characters had collapsed into *hold* and its neighbours across seventeen chapters, and **說文解字 gives them four different hands — one of which is not a hand at all:**

| | 說文 | the graph | now |
|---|---|---|---|
| 持 (*chí*) | 握也 — *"to grip"* | 手 (*shǒu* — hand) + 寺 | **hold** |
| 執 (*zhí*) | **捕罪人也** — *"to seize a criminal"* | 丮 a reaching hand + 㚔, **manacles** | **grasp** · *seize* (74) |
| 守 (*shǒu*) | **守官也** — *"to keep an office"* | 宀 a roof + 寸 (法度, a regulation) | **hold to** · *guard* (9, 67) |
| 保 (*bǎo*) | **養也** — *"to rear"* | 人 a person + 孚, a hand over a child | **keep safe** · bare ***keep*** at 9 |

A grip, a pair of handcuffs, a post you are answerable for, and a child on your back. Entries: `zhi-執.md`, `shou-守.md`, `bao-保.md`, `chi-持.md`.

### 執 is not the 強 case. It is a legal word.

`WORKLIST` framed 執 as 強's problem again — one character, opposite valences, an English that must hold both. **The character is narrower than that.** 說文's definition is 捕罪人也, and the book uses the judicial sense twice with no metaphor in it: at ch 74 河上公 reads 執而殺之 as statute (乃應**王法**執而殺之…老子傷時王不先道德化之而先**刑罰**), and at ch 79 執左契 is a bond that made a debt enforceable before there were written laws (古者聖人執左契合符信也，無文書法律，刻契合符以為信也).

So 執者失之 is not a caution against clinging. **Its object is 天下, and the clause before it says what the world is** — 天下神器，不可為也，不可執也. You cannot take a sacred vessel into custody. 王弼 states it as a fact about the world rather than about the heart: 物有徃來而執之，故必失矣, and he brackets the verb with ch 28's blade — 不施為**執割**也.

**Which makes ch 14 and ch 35 the joke, not the exception.** 執古之道 and 執大象 use the custody word straight: you cannot take the world into custody, so take the one thing that will not break in your hand. An English that softened 執 at those two and hardened it at the other five resolved a tension the Chinese leaves standing.

***Seize* at ch 74 is not an exception to the character — it is the dictionary headword.** English *grasp* has no judicial sense; 捕罪人也 is, in three characters, *seize a criminal*. Shalom's call, 2026-09-08.

### The error that had no name: *guard* was worn by three characters

守 read *guard* at ch 9, 保 read *guard* at ch 15, and 衛 (*wèi*) read *guards* at ch 67. **And 守 and 保 stand together in both ch 9 and ch 67**, so no rule in this repository could ever have seen it — a `forbidden:` entry keys off a character being present in the chapter and cannot express *right for that character, wrong for this one, same chapter*. Both new entries say so in a section of their own, because the gap is permanent.

Now: 守 → *guard* (9, 67), 保 → *keep safe* (15, 62, 67) and **bare *keep* at 9** *(flexion declared 2026-09-20 — see Ch 9 below)*, 衛 → *shields* (67).

### 保 runs in both directions, and one English lets them answer each other

At ch 15 and 67 a person keeps something safe; at ch 62 the Tao keeps a person safe. 王弼 gives the outcome in four characters — **保以全也**, *"保, because it keeps them whole"* — and 全 is locked to *whole*. 河上公 twice uses the compound 保倚, *to lean on for safety* (ch 62: 道者，不善人之**保倚**也，遭患逢急，猶自知悔卑下; ch 67: 我有三寳，抱持而**保倚**). Ch 62's 所保 accordingly makes the Tao the agent — *"what keeps safe those who are not"* — where a noun made it a passive receptacle.

### 守 takes a preposition because the graph has no hand in it

宀 a roof over 寸, which 說文 glosses 法度也, *a regulation*. What you 守 is a **post you are answerable for**, not a thing in your fist — so *hold to*, which is what English does with a charge. The split to *guard* runs by what is kept: nine lines keep a stance (中, 靜, 雌, 黑, 辱, 之, 母, 柔), two keep ground or property (a hall of gold and jade at ch 9; 以戰則勝，以守則固 at ch 67, where 河上公 expands the bare character to 以**守衛**則堅固).

**The paradox survives the single English.** 王弼 on ch 52's 守柔曰強: 守強不強，守柔乃強也 — *"holding to the strong is not strong; holding to the soft is truly strong."* Same verb both halves; only the object changes.

### 持 is the root the dictionary defines the others by

說文 sends 持 and 握 to each other (持，握也 / 握，搤持也), and defines the book's other hand-verbs *by* 持: **搏** 索持也 (14, 55) and **據** 杖持也 (55). Ch 64 prints 持 and 執 in one chapter doing opposite work — 其安易**持** against **執**者失之 — which is the chapter's argument in two verbs and disappears if they share a word.

### Riders applied on the way

- **Ch 14 — 搏 had taken 執's English inside 執's own chapter.** 搏之不得 read *"you cannot grasp it"* thirteen lines above 執古之道. Now *"Reach, but you cannot get it,"* on 得's own word.
- **Ch 55 — 握固 read *"their grasp is firm."*** 握 is the tightening word 說文 defines 持 by; now *"their grip is firm,"* which also frees *grasp* to mean 執 alone, book-wide.
- **Ch 79 — 左 had been dropped.** 執左契 read *"the sage holds their half of the tally"*; now *"grasps the left half of the tally."* **Whose half the left half was is left open** — the traditions disagree, and 而不責於人 is pointed under one reading and merely descriptive under the other. 王弼 says only 左契防怨之所由生也.
- **Ch 59 — *Holding* was on 有.** 有國之母 read *"Holding the mother of the state"* while 可以有國 one line above read *"maintain the state"* — the same character, two Englishes, adjacent lines, and neither of them 有's. Both now **have**, which matches them to each other; 有's transitive uses stay open beyond the settled 有道者.
- **Ch 52 — *holding* was on 襲.** 是謂襲常 read *"holding the ever-present covered"* in a chapter where 守 stands twice. Now *"the ever-present worn covered,"* matching ch 27's 是謂襲明 exactly.
- **Ch 5 — *in silence* rendered nothing.** 不如守中 read *"hold the center in silence"*; now *"hold to the center."*

---

## Ch 14's opening triad · 夷 · 希 · 微 — the names, and why the verse gives their meanings

*(Shalom's call, 2026-09-10. `WORKLIST.md` T2-52.)*

視之不見，名曰夷 · 聽之不聞，名曰希 · 搏之不得，名曰微 is a **definition passage** — 名曰X, *"its name is called X,"* three times — and it is the one place in the book where each of the three characters is named. The English renders each by **what it means here**, not by the word it carries elsewhere:

| | 說文解字 | ch 14 | elsewhere |
|---|---|---|---|
| **夷** (*yí*) | 平也 — *"level."* 大 (a person) with 弓 (a bow) | the invisible | **level** — 41, 53 |
| **希** (*xī*) | 爻 (crossed threads) over 巾 (cloth): **loose-woven fabric you can see through** | the inaudible | **barely heard** — 41 · **sparse** — 23, 43, 70, 74 |
| **微** (*wēi*) | 隱行也 — *"to move concealed,"* on 彳 the step radical | the intangible | **faint** — 15, 64 · **hidden** — 36 |

**河上公 supplies exactly these three readings, in one sentence three times:** 無**色**曰夷 · 無**聲**曰希 · 無**形**曰微 — colour, sound, form, the three ways a thing presents to the senses, denied in turn.

**The alternative was weighed and declined.** Rendering the words themselves — *"its name is the level · the sparse · the faint"* — would make all three **live threads through nine other chapters**, and 王弼 argues for it directly: at ch 41 he defines 希 by quoting this stanza outright (聽之不聞名曰希), which makes 大音希聲 and 名曰希 one word by his own hand. **It was declined on legibility.** Chapter 14 is early, and three bare adjectives there give a reader nothing to hang them on; the gain is everywhere else in the book and the loss is on the page in front of them.

**The standing principle it yields: where a rendering is chosen for one chapter's legibility, the connection it forgoes becomes an obligation on the notes, not a debt on the verse.** So the link is carried by an **anchor note at ch 14** listing all three with their graphs and recurrences, and a matching **thread note at chapters 15, 23, 36, 41, 43, 53, 64, 70 and 74**, each pointing back. **Ch 41 carries the counter-argument as well as the pointer**, because that is where 王弼 makes it.

**What stays open** is whether the *recurrences* agree among themselves: 夷 at 41 against 53 (T2-30), and 微's *hidden* at 36 against *faint* at 15 and 64 (T2-34). 希's six chapters remain TRIAGE 14b.

---

## 身 (*shēn*) → *body* — one character that had six Englishes

*(Shalom's call, 2026-09-19. `WORKLIST.md` T2-1. Full argument: `glossary/shen-身.md`.)*

身 stands twenty times across nine chapters and was reading **six ways** — *body* (13, 54), *self* (44, 54), *themselves / their selves* (7), *yourself* (52, 66), *their being* (26), and at ch 9 **nothing at all**. Now **body** everywhere, with one declared flexion.

**The graph settles what kind of word it is.** The oracle-bone form is a person in profile **with the abdomen swollen**, which is the entire difference from 人 (*rén* — a person); 說文 gives 躳也。象人之身 and 段玉裁 rejects its 从人𠂆聲 phonetic reading as an error. The oldest attested sense is pregnancy — 詩經 大明, 大任**有身**，生此文王 — and 身 is cognate with 孕 (*yùn* — pregnant). So **身 is a person seen as something that carries, and can be burdened**, which is 河上公's 財多**累身** (*"much wealth burdens the body"*, 9 and 44) and is why ch 13's 為吾**有身** is the Odes' idiom character for character.

**Why not *self*, which flows better at ch 7.** Three reasons, and the third is the general one:

1. *self* is **我/吾**'s (`wo-wu-我吾.md`, which already names 吾/身 as its cousin-pair), and at **ch 7 it is also 私's** — the one chapter where 身 and 私 (*sī* — private interest) stand in the same stanza, and where 王弼 makes their difference the argument: 無私者，**無為於身**也.
2. **Ch 7 is about staying alive.** 存 (*cún* — remains in existence) answers 長生 (*cháng shēng* — long life) four lines above it, and 河上公 reads 身存 with no metaphor: 百姓愛之如父母…故**身常存**. A self does not survive; a body does.
3. **Using *body* for the physical lines and *self* for the interior ones performs a split this tradition does not make.** 河上公's 修道於身，**愛氣養神** names the 身 as the *site* and 氣 and 神 as what is nourished in it — a structure, not a merger. Choosing between the two English words chapter by chapter is a dualism imported and then attributed to the text.

**The flexion, declared rather than drifted into.** In 終身 (*zhōng shēn*) and 没身 (*mò shēn*) the character marks **the span of a life**, not the flesh: all four lines (16 · 52 ×3) read *to the end of your days*. Ch 52's two 終身 lines had been *"all your life"* and *"your life"*; they now match.

**Riders applied.**

- **Ch 7** — 身 ×4 restored in place of *themselves / their selves*, and **生 (*shēng* — to live) restored at 故能長生**, which the verse had lost to *"They endure without limit."* The chapter now runs 長生 → 身存 as one argument.
- **Ch 54** — 以身觀身 → *observe the body through your own body*, rejoining the first stanza's 修之於身 and restoring the 身 → 家 → 鄉 → 國 → 天下 ladder's first rung in both directions.
- **Ch 52** — 無遺身殃 → *leave no calamity for the body*; 遺 (*yí* — to leave behind) now rendered.
- **Ch 44 · 66** — mechanical.
- **Ch 76** — *"In life the body is soft and yielding"* renders 人之生也柔弱, which has **no 身**. Now *a person*. A rendering that had taken 身's English in a chapter where the character is absent.

**The axis the entry adds.** 身 is weighed against 名 (*míng* — reputation) and 貨 (*huò* — goods) at 44, against 功 (*gōng* — merit and office) at 9, and against 大患 (*dà huàn* — great trouble) at 13. **The class is everything a person could acquire, and 天下 (*tiān xià* — the world) is simply the maximum of that class** — which is why ch 13, 26 and 54 put 身 and 天下 in a single line, and why ch 26's English losing 天下 cost more than one word.

**What no check can hold.** *self* cannot go on 身's `forbidden:` list: 身 shares ch 7 with 私 and ch 13, 16, 54 with 我/吾, and the evidence gate keys off a character's presence in that chapter. And the collision with **神** (*shén* — spirit) is invisible for the opposite reason — 神 stands in 6, 29, 39, 60 and 身 in 7, 9, 13, 16, 26, 44, 52, 54, 66, so **they share no chapter at all**. Only `concordance.py --english "spirit"` finds it. The same two-way blindness that hid 固 and 壯 inside chapters containing 強.

---

## Ch 9 · three verbs for keeping, and the English had one

*(Shalom's call, 2026-09-20. `WORKLIST.md` T2-51 · T2-1. Fork in `notes/manuscript.md`.)*

The chapter is a list of things that cannot be kept, and it uses **three different characters to say *keep*** — 持 (*chí* — hold), 保 (*bǎo* — keep safe), 守 (*shǒu* — guard). The old English rendered one of the three, invented a **vessel** for a chapter with no 器 (*qì*), flattened 不如 (*bù rú* — not as good as) to a comma, deleted 身 (*shēn* — body), and gave 咎 (*jiù*) the word that belongs to 敗 (*bài* — ruin) at ch 29 and 64.

**The vessel was not arbitrary, and it still had to go.** 河上公 glosses the opening 持滿必傾 — *"hold it full and it must tip over"* — which points at the 欹器 (*qī qì*), the tilting vessel of the ancestral temple that stands upright part-full and capsizes when filled. But 器 is locked to *vessel / tool / implement* across nine chapters, none of them this one. **The referent is named grammatically instead** — *what you hold* — which is `name-the-referent`'s answer and its third case: 之 (*zhī*) is a light particle a Chinese reader passes over, where English *it* actively selects, so declining to resolve is not preserving openness.

**保 → bare *keep*, a declared flexion** (`glossary/bao-保.md`). Its other three lines take a cherished object and are all positive — the Tao at 15 and 62, the three treasures at 67. **Ch 9 is the only negative instance and the only uncherished object**, and English *keep safe* wants something valued for its own sake. The lock had never been tested here: this verse rendered 保 nowhere, so the 2026-09-06 ruling was argued from the chapter's **gloss table** rather than from a line anyone had to say aloud.

**銳 (*ruì*) is a point, not an edge, and what fails is the point.** 說文: 芒也。从金兌聲 — *"it is 芒 (máng, the awn of grain), on the metal radical."* The edge is 刃 (*rèn*), which occurs **once in the whole book**, at ch 50. 王弼 agrees — 既揣**末**令**尖** — and 揣 as *hammer* is 說文's own second gloss, 一曰**捶**之. The failure is breakage, not blunting: 王弼 勢必**摧**䘐, 河上公 後必**弃捐**. **And blunting is 挫's** (*cuò*, 說文 摧也) at 挫其銳, ch 4 and 56 — where it is the **remedy**. An English reading *"cannot be kept sharp"* would make this chapter's affliction and those chapters' cure the same sentence.

**咎 → *fault*, on our own ch 46's authority.** 說文 gives 災也 (*disaster*) and a graph of 人 with 各 (相違也, *at odds*) — the falling-out and its consequence in one word. *Disaster* is unavailable anyway: **ch 46 sets 禍 (*huò*) and 咎 in a parallel couplet** — 禍莫大於不知足 / 咎莫大於欲得 — and gives *disaster* to 禍, *fault* to 咎. 遺 (*yí* — to leave behind) is now rendered, matching ch 20 and ch 52. **Opens T2-53**, the calamity family: *disaster* is currently worn by 禍 **and** 凶.

**功遂身退 → *the work done, the body withdraws*.** *Cease striving* deleted 身 and borrowed 爭's (*zhēng*) word. 河上公 reads it as vacating office — 不**退身**避位則遇於害 — and quotes the same shape back at ch 44, 名遂則**身退**也.

---

## Ch 26 · the chapter turns on heavy against light, and *light* was gone

*(Shalom's call, 2026-09-20. `WORKLIST.md` T2-1 · T2-5 · T2-6.)*

**輕 (*qīng* — light) had three Englishes in eight lines**, and it is the chapter's pivot: 重 (*zhòng* — heavy) against 輕 opens the chapter and delivers its verdict. *Ungrounded* stood at all three, so the pair was invisible. **輜重 (*zī zhòng* — the heavy baggage train) had become *sustenance***, taking the 重 that line 1 depends on; 王弼: 以重為本故不離.

**奈何萬乘之主，而以身輕天下 had lost three of its parts** — 萬乘 (*wàn shèng* — ten thousand chariots) flattened to *a great ruler*, 身 turned into *their being*, and **天下 (*tiān xià* — the world) deleted outright.** This is one of only three lines in the book where 身 and 天下 stand together, and `chapters/013.md` cites it as the support for ch 13's closing couplet — so the evidence for a settled call did not say what the note said it said. 河上公: 王者至尊，而以其身行輕躁乎.

**靜 → *stillness* (T2-5)**, against *Silence* here alone and seven lines elsewhere. **君 → *ruler* in both places (T2-6)**, where it had been *ruler* and *mastery* three lines apart in a matched pair. **燕處超然 → *they dwell at ease and stay apart***; *their equanimity is undisturbed* rendered no character.

---

## 明 (*míng*) · the frontmatter catches up with the entry, and 道 stops being a path

*(2026-09-20. `WORKLIST.md` T2-46.)*

**The entry already knew; the data did not.** `glossary/ming-明.md`'s *working register* section has listed four forms since it was written — the named state, the noun, the predicate, the modifier — while `render:` said only *"clear-seeing / clarity"*. So four of 明's thirteen lines (22, 24, 33, 47) and the modifier at 41 were **unlicensed by the frontmatter**, and `concordance.py --english "see clearly"` reported *not tied to any locked term* for a phrase that renders a locked character twice. `render:` now carries all three shapes.

**Why this stayed prose rather than becoming a `flexions:` entry.** The variation is **grammatical, not chapter-scoped**: 明 takes the predicate form wherever it predicates, and would in a chapter nobody has written. `flexions:` exists for a licence tied to a named place, and its `flexion-chapter` rule checks exactly that — so pinning a grammatical form to a chapter list would assert a condition the language does not have. The boundary is stated in `CLAUDE.md`.

**The glossary-self-check hole, found by hand.** The entry rendered 明道若昧 as *"the clear **path** seems dim"* in **three places**, and 道 (*dào*) is locked untranslated with *"the Path"* forbidden outright. **The file that defines one lock was breaching another** — which is the case `PLAN.md` opened `glossary-self-check` for, and the rule is still unbuilt. Note the near-miss: the forbidden string is capitalised, so a lowercase *path* would not have fired even if the rule existed.

**Two stale examples corrected in the same pass**, both overtaken by later decisions: 襲明 was glossed *"inherited clarity"* where ch 27 has read *clarity worn covered* since T2-10 settled 襲 → *covered*, and 明白四達 was glossed *"clear and penetrating in all directions"* where ch 10 reads *clarity reaching the four quarters*. An entry's examples are a second copy of the verse and go stale exactly as the prose restating a lock does.

---

## 昧 (*mèi*) → *murky* — *dark* is 玄's, in a chapter that has no 玄

*(Shalom's call, 2026-09-20. `WORKLIST.md` T2-54, its first half.)*

明道若昧 (41) read *"The clear Tao seems dark"* and 其下不昧 (14) read *"a dark bottom."* Both now **murky**.

**The fault is a collision, not a misreading.** 說文 gives 昧 both senses — 昧爽，旦明也 for the compound (*daybreak*) and 一曰**闇**也 for the graph alone (*shut-in dark*) — so *dark* was defensible about the character. It was unavailable anyway: **玄 (*xuán*) is locked to *dark or profound* and carries six verse lines**, among them ch 1's 玄之又玄, *"dark, and dark again, the gate of all subtleties,"* and 玄牝, *the dark female*. Neither ch 14 nor ch 41 contains 玄. So the English made a reader hear the book's signature word for the unseeable where the Chinese has only the plain antonym of 明 — **invented repetition**, the mirror of the ch 11 fault and the class `WORKLIST` T5-14 exists for. `--english "dark"` had ten lines, six backed and four not.

**Everything nearer was already worn.** *Dim* is 和 (*hé*) at 和其光 (4, 56) and 冥 (*míng*) at ch 21's 窈兮冥兮; *faint* is 微 (*wēi*) at 15 and 64; *dull* is 爽 at 12 and 悶 at 20 and 58; *hidden* is 微 again at 36. Free were *murky*, *clouded*, *obscure*, *shadowed*, *veiled*. **Obscure** was declined as abstract and as carrying *unimportant*, a verdict 昧 has not.

**The chime with 濁 (*zhuó* — *muddy*, 15 and 49) was weighed and accepted**, which is the part worth recording. `already-spoken-for` would ordinarily refuse a rendering that rhymes with a neighbour's; here the two were judged distinct enough to stand apart and resonant enough to be worth the nearness. *Clouded* was free of even that and was declined for it.

**The English does not settle the commentators, and must not.** 王弼: 光而不耀, *"bright but not dazzling"* — the light present and unostentatious, and he quotes ch 58 to say so. 河上公: 明道之人若闇昧，無所見 — genuine obscurity, seeing nothing. *Murky* holds both: still light, and not seen through.

**Still open in T2-54:** 昏 (*hūn*, 說文 日冥也 — the sun gone down) reads *dark* at ch 20's 我獨昏, so two characters still share 玄's word. And **昧 is settled but unlocked**, so the atlas keeps publishing the pre-lock gloss — the same debt T2-40 carries for 混.
