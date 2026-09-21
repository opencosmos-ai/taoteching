# WORKLIST — what the manuscript still owes

*The single forward-looking file. Everything here has a status that needs to be kept up-to-date.  When something closes it leaves this file and becomes a one-line pointer in the ledger at the foot — because the reasoning already lives somewhere permanent, and repeating it here is how the old debt list grew to 343 lines and went stale.*

**Where things live.** The **ruling and its full argument** go in `glossary/`. The **decision, thin**, goes in `notes/` — manuscript forks in `notes/manuscript.md`, our own rendering calls in `notes/translation.md`, reader-facing threads in `notes/reading.md`. **What is still owed** goes here. Nothing belongs in two of those.

**Policy: fix on discovery, not in a deferred batch.** Mechanical term-swaps are applied immediately. Lines needing a rewrite are proposed to Shalom first, then applied. Each chapter carries its own debt in frontmatter (`retrofit: [...]`).

**The first draft is complete — 81 of 81, since 2026-08-26. The editing pass is the work now.**

**Progress: Pass 0 ✅ · Pass A ✅ · Pass B ✅ · Pass C ✅ · Pass D ✅ — 19 of 19 chapters (2026-09-07).** Pass D, the chapter-level rewrites, is **complete**, and it had **one row per chapter** so they could be checked off one at a time. Done: **3 · 4 · 8 · 10 · 11 · 13 · 16 · 22 · 23 · 28 · 29 · 31 · 32 · 35 · 36 · 38 · 39 · 41 · 64** — nineteen of the nineteen. Gate green: 0 errors, 124 tests, hard breaks intact, worklist consistent with itself.

*Supersedes `RETROFIT.md` and `EDITING-PASS.md`, merged into this file on 2026-08-28 and both now deleted. This file is `RETROFIT.md` renamed, so `git log --follow WORKLIST.md` still reaches the project's start; the 2026-08-10 sweep record and the lessons it taught the checker moved to `PLAN.md`. Every item below was re-verified against the manuscript at the merge; the old file listed six repairs that had already been made.*

---

## The list

**⬜ open · 🔶 part done · ✅ done · ⏸ deferred by Shalom.** Detail for every row is below, under the matching heading. **130 item rows: 54 open · 70 done · 3 part done · 3 deferred.** *(19 of them are the per-chapter Pass D rows, whose status is derived.)* *(Counted from the table itself — a hand-kept tally drifts. It read "43 open · 18 done" and matched nothing.)*

| # | | Item | Ch | Pass |
|---|---|---|---|---|
| | | **Passes** | | |
| P0 | ✅ | Text bugs — a stray word, a missing *of*, a junk row, a corrupted table, a double space | 5 8 39 42 59 | 0 |
| PA | ✅ | **強 → strong**, completing the four-word table; 力 covered as *force* | 15 30 33 42 52 55 68 | A |
| PB | ✅ | **仁 → humaneness · 慈 → tenderness · 孝 → devotion**; Guodian G1 closed | 5 18 19 20 38 | B |
| PC | ✅ | ~~**The mirrors**~~ — every C-tagged row closed (T3-1, T2-9→14); T2-15's remainder moved to D with ch 28 and T1-8 | T3-1 · T2-9→15 | C |
| PD | ✅ | ~~**Chapter-level rewrites** — the real work~~ — **all 19 chapters closed 2026-09-07.** One row per chapter below; **the count lives in those rows, not here** | D3 → D64 | D |
| PE | 🔶 | Entries and sweeps — ~~**守 執 保 持**~~ (T2-19 ★, closed 2026-09-08) · ~~**身**~~ (T2-1 ★, closed 2026-09-20) · 氣 靜 君 智 事 志 谷 恃 | book-wide | E |
| PF | ⬜ | The deferred calls | 民/人 · 正/奇 · em-dashes | F |
| PG | ⬜ | `build.py` | — | G |
| | | **Tier 1 · Wrong, not merely inconsistent** | | |
| T1-1 | ✅ | ~~無知 and 無為 are on the wrong lines; 疵 dropped~~ — plus **全 · 萬物 · 鑑, three locked Englishes on a chapter that has none of them**; two forks logged | 10 | D |
| T1-2 | ✅ | ~~道沖 inverted…帝 erased~~ — ch 4 rebuilt; **帝 locked to *god*, new entry**; closes T2-14c | 4 | D |
| T1-3 | ✅ | ~~為無為 → *"Without effort"*; 敢 dropped~~ — ch 3's closing movement rebuilt; 治 restored at both ends; **`"effortless" / "without effort"` added to 無為's forbidden list** | 3 | D |
| T1-4 | ✅ | ~~無為 → *"takes no action"*; 上 rendered two ways; invented *pure*~~ — ch 38 rebuilt; **失 restored as the chapter's spine**; 大丈夫 → *the great person* (Shalom's call); opens T4-7 | 38 | D |
| T1-5 | ✅ | ~~Bare 德 → *"profound integrity"* ×3~~ — 玄德's word, on a chapter with no 玄; triad restored | 23 | C |
| T1-6 | ✅ | ~~守 → *"Embrace"* — 守/抱 swapped~~ — 守 → *hold to*, matching ch 28; **極 and 篤 were both dropped entirely** and are now rendered | 16 | D |
| T1-7 | ✅ | ~~守 → *"attune to"* ×3; 常 dropped from all three 常德~~ — 守 → *hold to*; 常 restored ×3; the template runs unbroken | 28 | D |
| T1-8 | ✅ | ~~為 → *"force"* ×3; clashes with ch 64's *handle*~~ — all three now **handle**, per the lock. *Force* belongs to 力 (33, 68) and **強 stands in this chapter**; the substitution also cost 王弼's argument, 可因而不可為, *"can be gone along with but not handled"* | 29 | D |
| T1-9 | ✅ | ~~左/右 as *"creation"/"destruction"*, then literal four lines later~~ — both restored. The old line also **reversed the argument**, having the sage choose destruction where 河上公 has 兵道與君子道反, *the way of arms and the way of the 君子 are opposed* | 31 | D |
| T1-10 | ✅ | ~~無身 → *"the separate self dissolves"*~~ — an Advaita import that also **broke 有/無 on the one line in the book applying the pair to a person**; now *if I had no body* | 13 | D |
| T1-11 | ⬜ | 古始 → *"the primordial source"* — forbidden register | 14 | E |
| T1-12 | ✅ | ~~往 → *"the world routes to you"* ×2~~ — 往 is a verb of going, as at ch 80; **執 → *grasp*, restoring ch 29's mirror**, and 大象 → *the great image*, matching ch 41 | 35 | D |
| T1-22 | ⬜ | Ch 48 — 取天下 → *"the world comes to you"*; 取 (*qǔ* — to take) is active and the English makes it a passive arrival. *Found by the ch 35 reverse check* | 48 | E |
| T1-13 | ✅ | ~~*"returns energy to its root"* — 氣 is not in this chapter~~ — plus ***Multitudes*** with no 眾, and 物 deleted; 復歸 → *returns again*, following ch 28 | 16 | D |
| T1-14 | ✅ | ~~The closing 譬…猶 simile is garbled~~ — the frame restored and the invented *high* and *deep* removed. 王弼 ties it to the chapter's middle: 非江海召之…不令而自均 | 32 | D |
| T1-15 | ✅ | ~~谷 → *"reservoir"*, 谿, 官長, 大制 → *"orchestrator"*~~ — 谷 → *valley* (its word in 6 chapters); 制 → *cutting* (as ch 32); 割 → *severs* | 28 | D |
| T1-16 | ✅ | ~~雄/雌 → *"assertive/yielding energy"*~~ — **rooster and hen**, forced by 牝/牡 already holding *male* / *female* | 28 | D |
| T1-17 | ⬜ | 明 → *"clever"* — the one licensed lock exception, unrecorded | 65 | E |
| T1-18 | ⬜ | 佐 → *"One who rules"* — follows 河上公 against the grammar, unlogged | 30 | E |
| T1-19 | ✅ | ~~大器晚成 → *"never completed"* — English follows a witness our table doesn't carry. **Also *the countless things* with no 萬物**~~ — the witness call is now argued in the chapter notes; 夫唯道，善貸且成 reads *"Only the Tao is masterful at lending, and at completing."* 貸 is **to lend** (貝, money), and 王弼 rules out our old *provides for*: 貸之非唯供其乏而已 | 41 | D |
| T1-20 | ⬜ | Four `unlogged-variant` warnings | 2 9 26 51 | E |
| T1-21 | ⬜ | 配天 — the chapter and its own note disagree; the contested 天 line | 68 | F |
| | | **Tier 2 · One character, many Englishes** | | |
| T2-19 | ✅ | ~~★ **The holding family — 守 執 保 有 collapsed into "hold."**~~ — **說文 gives four different hands, and 守 has none.** 執 → *grasp* (*seize* at 74, the arrest — 捕罪人也 is the dictionary headword) · 守 → *hold to* / *guard* · 保 → *keep safe* · 持 → *hold*. **Four entries written and locked.** *Guard* had been worn by **three characters** (守 9, 保 15, 衛 67) — unseeable by any rule, since 守 and 保 share both ch 9 and ch 67. Riders: 搏 (14), 握 (55), 左 (79), 有 (59), 襲 (52), ch 5. ~~Ch 9 open → T2-51~~ *(closed 2026-09-20; 保 gained a declared flexion there)* | 5 9 14 15 16 28 29 32 35 37 52 55 59 62 64 67 69 74 79 | E |
| T2-51 | ✅ | ~~**Ch 9 renders neither 持 nor 保, and invents a vessel**~~ — the chapter rebuilt: **持 · 保 · 守 all three on the page**, 不如 restored as a construction, the 器-less vessel gone and the referent named grammatically, 銳 held to *point* (說文 芒也; the edge is 刃, one line in the book), 咎 → *fault* following ch 46's couplet, 遺 rendered, and 身退 restored. **保 takes bare *keep* here, a declared flexion** — ch 9 is its only negative instance and its only uncherished object, and the lock had been argued from this chapter's gloss table rather than its verse. One fork logged | 9 | E |
| T2-1 | ✅ | ~~**身** — *body* / *self* / *themselves*, and two of them inside ch 54~~ — **身 → *body*, locked** (2026-09-19, Shalom's call); one character that had **six** Englishes and at ch 9 none. Entry written; 終身/没身 flexed to *to the end of your days* and declared. Swept at 7 (身 ×4, and **生** restored at 故能長生), 9, 26, 44, 52, 54, 66, plus the **ch 76 rider** where *body* rendered 人. *Self* refused: it is 我/吾's and, at ch 7, 私's. **Ch 10's rider resolves as no change** | 7 9 13 16 26 44 52 54 66 76 | E |
| T2-2 | 🔶 | **智** four ways; **ch 3 settled as *the knowers*, fork logged**; *"cunning"* still wears 巧 at 19 and 57 | 3 18 19 33 65 | E |
| T2-3 | ✅ | ~~**士** three ways, two on the identical phrase 善為士者~~ — all three now **in service** (2026-09-07, Shalom's call). 說文 士，事也: one who handles **affairs**, not a student; 河上公 has the middle 士 治國以太平, *governing the state*. *Officer* was declined as bureaucratic and negatively valenced. **Entry written and locked: `glossary/shi-士.md`.** **Seam noted:** 士 named a male class and the English is deliberately neutral. Opens T2-47 | 15 41 68 | E |
| T2-4 | 🔶 | **氣** — ch 10 → *breath* (河上公 呼吸精氣); *vital breath* (42) and *vital energy* (55) still split | 10 42 55 | E |
| T2-21 | ⬜ | **厚** four ways — *thick* (38) · *heavy* (44) · *abundant* (55) · *rich* (75) | 38 44 50 55 75 | E |
| T2-22 | ✅ | ~~**嬰兒 / 赤子** both read *newborn*~~ — 嬰兒 → *infant* (10, 20, 28); 赤子 keeps *newborn* (55) | 10 20 28 55 | E |
| T2-5 | ✅ | ~~**靜** reads *"Silence"* here alone~~ — **stillness**, matching its seven other lines (16, 45, 57, 61); closed with the ch 26 rebuild | 26 | E |
| T2-6 | ✅ | ~~君子 → *"the sage"* — the opposition's honorific on our figure~~ — **君子 → *the noble* at 26 and 31** (2026-09-07, Shalom's call; neutral over *the gentleman*), and **君 alone now reads *ruler* in both of ch 26's lines** (2026-09-20), where it had been *ruler* and *mastery* three lines apart in a matched pair. *Rank question → T4-7* | 26 31 | E |
| T2-7 | ⬜ | **志** — *ambition* (3) / *will* (33) | 3 33 | E |
| T2-8 | ✅ | ~~Eight 善 rendered eight ways~~ — **nine**, and one was deleted; all nine now **masterful**; 上善 → *the most masterful*; **善 governs a verb, 18 of 18** | 8 | D |
| T2-9 | ✅ | ~~**辯** → *"eloquence"*~~ — **argue** in both; the 大X若Y frame does not endorse its X | 45 81 | C |
| T2-10 | ✅ | ~~**襲** — *inherited clarity* vs *the practice of*~~ — **two characters, not two readings**; 襲/習 fork recorded | 27 52 | C |
| T2-11 | ✅ | ~~**殆** → *"depletion"*; 没身不殆 two ways~~ — **danger** ×5, one-to-one; ch 15's invented danger and ch 25's dropped 周行 fixed too | 15 16 25 32 44 52 | C |
| T2-12 | ✅ | ~~**以此** three ways~~ — all three now *"By this."*; two stale notes corrected | 21 54 57 | C |
| T2-13 | ✅ | ~~**故去彼取此** three ways~~ — all three now ch 72's line; *gut* locked; *embrace* freed | 12 38 72 | C |
| T2-14 | ✅ | ~~難得之貨 ×3 · 信不足焉 ×2 · 挫其銳…同其塵 ×2~~ — subject settled with T1-2: the Tao at ch 4, imperative at ch 56 | 3 4 12 17 23 56 64 | C |
| T2-15 | ✅ | ~~Formula pairs~~ — **all 6 closed.** 為者敗之，執者失之 now reads identically at ch 29 and ch 64 | 29 64 | D |
| T2-16 | ⬜ | **事** wants an entry; 無事's licensed split needs confirming | 48 57 63 | E |
| T2-17 | ⬜ | **私** two ways, sheltering under 公's `covers:` | 7 19 | E |
| T2-20 | ⬜ | **巧** — *skill* (45) vs *cunning* (19, 57); the same fault as 辯, one line above it | 19 45 57 | E |
| T2-18 | ✅ | ~~復命 → *"returning to what was given"*~~ — **"returning to what *is* given"**; two entries written. 天命 and 性 are both **absent from the book**; **復命 is a *name* for the return, not a further step**. Four candidates failed — *what is* would have taken 自然's English, and ch 51 sets 自然 **against** 命 | 16 | D |
| | | **Tier 3 · Missed parallelisms** | | |
| T3-1 | ✅ | ~~★ **The 不自X / 自X者 mirror**~~ — ch 24 rewritten as ch 22's negative; ch 31 swept | 22↔24↔31 | C |
| T3-2 | ✅ | ~~Seven 善X couplets, seven unlike shapes~~ — one shape, seven times: *In X, masterful at Y* | 8 | D |
| T3-3 | ✅ | ~~Three identical 當其無 frames rendered three ways; 利 and 用 lost~~ — one frame, three times, eleven lines for eleven; **利 → *advantage*, a covered lock never before applied anywhere** | 11 | D |
| T3-4 | ✅ | ~~Four 將欲X之，必固Y之 nominalized into abstract laws~~ — conditional instructions with their object restored; **固 was an adverb rendered as an adjective**, and 韓非's worked examples prove the temporal reading | 36 | D |
| T3-5 | ✅ | ~~Three four-beat stanzas rendered as prose~~ — the 知其X/守其Y · 為天下Z · 常德不W · 復歸於V template restored | 28 | D |
| T3-6 | ✅ | ~~The 得一 / 無以 mirror breaks at its sixth pair~~ — it was **inverted**: broken at pair five where the Chinese holds (生/生), smoothed at six where it breaks (貞 / 貴高, the hinge). Both restored | 39 | D |
| T3-7 | ✅ | ~~寄/託 are a pair, rendered *entrusted with* / *truly care for*~~ — near-synonyms (說文 defines each by the other; **王弼 swaps them**); now *given* / *trusted with* | 13 | D |
| R1 | ⬜ | ★ **Harvest 韓非's 35 divergent lemmas into `variants.yaml`** — the oldest witness to this text, currently marked but unexploited | 1 27 36 38 46 47 50 54 58 59 60 63 64 67 | E |
| R2 | ⬜ | **義 (yì) wants a glossary entry** — reads *duty* in all 5 lines, unlocked, and the atlas therefore publishes *righteousness* | 18 19 38 | E |
| | | **Pass D · one row per chapter** — *status is derived from the finding rows above; `check_worklist.py` gates it* | | |
| D3 | ✅ | ~~**Ch 3** — the closing movement had the opposite grammar; 治 dropped from its hinge~~ · T1-3 | 3 | D |
| D4 | ✅ | ~~**Ch 4** — 道沖 inverted, 吾不知誰之子 untranslated, 帝 erased~~ · T1-2 | 4 | D |
| D8 | ✅ | ~~**Ch 8** — 善's showcase, and the lock applied to none of its nine~~; 幾 → *near*, not *one with* · T2-8 · T3-2 | 8 | D |
| D10 | ✅ | ~~**Ch 10** — 無知/無為 swapped, 疵 deleted, and three Englishes on absent characters~~ · T1-1 | 10 | D |
| D11 | ✅ | ~~**Ch 11** — three 當其無 frames three ways; 無 → *emptiness* ×2, *empty space* ×2~~ — the whole chapter: 無 → *in what is not there*, 有 → *presence*, 當 → *right where*, 利 → *advantage*. The chapter `wu-you-無有.md` names as its own test case · T3-3 | 11 | D |
| D13 | ✅ | ~~**Ch 13** — 無身 → *the separate self dissolves*; 寄/託 a pair~~ — the whole chapter: **five characters had fourteen Englishes**, now one each (身 ×6 · 患 ×4 · 驚 ×5 · 貴 ×3). **The closing couplet was reversed** — 以A為B is *take A as B*. 若驚 → *a shock* not *cause alarm*; 是謂 → *this is what is meant*, matching 8 chapters. Two forks · T1-10 · T3-7 | 13 | D |
| D16 | ✅ | ~~**Ch 16** — 守 → *Embrace*; *energy* with no 氣; 復命~~ — whole chapter rebuilt: the couplet, 夫物芸芸, and the 容→公→王→天→道→久 chain. **Three new entries**: 極, 虛, 復命 · T1-6 · T1-13 · T2-18 | 16 | D |
| D23 | ✅ | ~~**Ch 23** — 同 as dissolution ×6; *intensity* and *we* rendering nothing; 事's lock breached by *actions*~~; three forks logged · T2-25 | 23 | D |
| D22 | ✅ | ~~**Ch 22** — 為天下式 → *serves as the world's pattern*~~; visited as the settled half of a formula pair · T2-15 | 22 | D |
| D28 | ✅ | ~~**Ch 28** — the pointing test failed on nearly every line~~ · T1-7 · T1-15 · T1-16 · T3-5 | 28 | D |
| D29 | ✅ | ~~**Ch 29** — 為 → *force* ×3, clashing with ch 64's *handle*; closes the last formula pair~~ — the whole chapter: 取 and 物 restored, 或▢或▢ ×4 given four matching lines, 去 ×3 unflattened to *lets go of*, 甚/奢/泰 separated on 說文, 羸 → *frail*. **Two forks logged, one followed against the base** (挫 → 載, on internal grounds) · T1-8 · T2-15 | 29 | D |
| D31 | ✅ | ~~**Ch 31** — 左/右 as *creation*/*destruction*, then literal four lines later; 君子 → *the sage*~~ — the whole chapter: 器 ×3, 兵 ×3, 美 ×2 and 以喪禮處之 ×2 each unflattened; 眾 restored to its lock; 偏/上將軍 given their ranks back and the seating inversion with them; the two inflated 夫 removed. **The Siku editors flag part of this chapter as absorbed commentary** — logged · T1-9 · T2-6 | 31 | D |
| D32 | ✅ | ~~**Ch 32** — the closing 譬…猶 simile is garbled~~ — the whole chapter, **and Pass D closes with it**: 制 → **carving** at 32 and 28, so 樸 (*the uncarved*) and the blade that ends it share one English root; 自 unflattened; 均 → *even out* (*harmonize* is 和's); 侯王若能守之 matched to ch 37 · T1-14 | 32 | D |
| D35 | ✅ | ~~**Ch 35** — 往 → *the world routes to you*; 執 → *Embody*~~ — the whole chapter: **不足 → *not enough*, not *cannot***, which un-splits 王弼's single argument; 執 → *grasp* (the ch 29 mirror); 大象 → *the great image*; 口 gets its first *mouth*. Two forks logged. The ch 28 rider is cleared · T1-12 | 35 | D |
| D36 | ✅ | ~~**Ch 36** — four 將欲X之，必固Y之 nominalized into abstract laws~~ — the frame restored ×4; 利器 → *tools of advantage* (all three commentators); 淵 → *deep water*. **韓非 covers this chapter with worked historical examples.** Three forks logged, including 邦/國, which dates our base to Han hands | 36 | D |
| D38 | ✅ | ~~**Ch 38** — the 道 → 德 → 仁 → 義 → 禮 descent; 失 deleted from its hinge~~ · T1-4 | 38 | D |
| D39 | ✅ | ~~**Ch 39** — the 得一 / 無以 mirror breaks at its sixth pair~~ — the mirror was inverted; 得 → *received*; 貴/賤 → *prized/cheap*, price words not moral ones; **故致數譽無譽 departs from the base for the cart**, which both commentaries explain and the Siku editors call an error. Five forks logged · T3-6 | 39 | D |
| D41 | ✅ | ~~**Ch 41** — 大器晚成 follows a witness our table doesn't carry; *the countless things* with no 萬物~~ — the whole chapter: the **建言 catalogue rebuilt one saying per line** (twelve proverbs had been packed onto five); 大白 → *the whitest white*, removing an English overlay the Chinese has none of; 廣 → *boundless*, 建 licensed to flex, 夷 → *level*, 質真 → *substantial truth*; 士 settled across three chapters · T1-19 · T2-3 | 41 | D |
| D64 | ✅ | ~~**Ch 64** — already reads *handle*~~; the settled side of 為者敗之, nothing owed here | 64 | D |
| | | **Tier 4 · Deferred by Shalom** | | |
| T2-38 | ✅ | ~~**逝 → *expanding* at ch 25**, where 說文 gives 往也, *"to go."* 逝 is departure, not size, and it is the outbound leg of 大曰逝，逝曰遠，遠曰反 — the sequence the road-words Thread rests on. Found while writing that Thread from ch 15's 通~~ — now **departing**, and the sequence is three lines; 反 → *returning* matches ch 40 | 25 | E |
| T2-39 | ⬜ | **名 → *description* at ch 25** (強為之名曰大). 名 (*míng* — name) is the book's own heavily-worked word for *name*, 21 lines across 9 chapters, and ch 1 is built on it. **強為之▢ is also a shared frame with ch 15** (強為之容), where our English reads *"I force a likeness"* | 15 25 | E |
| T2-40 | ⬜ | **混 wants a glossary entry.** Settled as *mixed* across 14, 15 and 25 on 2026-09-06 but unlocked, so the atlas still publishes the pre-lock glosses. 說文 豐流也, on the water radical | 14 15 25 | E |
| T2-41 | ⬜ | **沖 reads *blending* at ch 42** (沖氣以為和) where ch 4's Pass D work settled it as **empty** (道沖). Found by the reverse search when *blend* was freed from 混 | 4 42 | E |
| T2-42 | ✅ | ~~**Ch 67 — 我道大 reads *"Everyone says I am vast"*: 道 dropped and the line handed to the speaker**~~ — 道 restored, subject now *it* throughout; 大 → *great* completes the ch 25 sweep; 細 → *slight*, matching ch 63, dropping *petty*'s moral verdict | 67 | E |
| T2-43 | ⬜ | **夫唯 (*fū wéi*) — 11 chapters, 12 lines, at least three Englishes.** *Only because* (67, 70), *Precisely because* (15), bare *Because* (2). A formula this size wants one English; surfaced when ch 15 and ch 67 were settled three days apart | 2 8 15 22 41 59 67 70 + | E |
| T2-44 | ⬜ | **The return family — 反 · 復 · 歸 all read *return*, across 21 English lines.** 說文 keeps them distinct: 反 覆也 (overturn, on 又 a hand), 復 往來也 (going and coming, on 彳 the step radical), 歸 女嫁也 (a woman marrying in — going where one belongs). 反 → *returning* is fixed at 25 and 40; the other two are open | 14 16 25 28 34 40 52 59 65 | E |
| T2-45 | ⬜ | **廣 two Englishes** — *boundless* at 41 (廣德若不足, settled 2026-09-07) and *reach far* at 67 (儀故能廣). 說文: 殿之大屋也, a great hall, on the roof radical 广. *Vast* is free now that 大 is locked | 41 67 | E |
| T2-46 | ✅ | ~~**`glossary/ming-明.md` needs an adjectival flexion, and glosses 道 as *path*.**~~ — `render:` now carries all three shapes the entry's own *working register* had listed for months: *clear-seeing / clarity*, ***see clearly*** in predicate position (22, 24, 33, 47), ***clear*** as a modifier (41). **Kept as prose, not a `flexions:` entry** — the variation is grammatical, not chapter-scoped, and pinning it to a chapter list would assert a condition the language lacks. The 道-as-*path* breach stood in **three** places, not one; two stale examples (襲明, 明白四達) corrected with it. **Opens T2-54 and T1-24** | 41 + glossary | G |
| T2-47 | ⬜ | **Ch 68's 善▢者 frame now has a seam.** 善為士者 is verbatim at 15 and 68, so its first line reads *"Those masterful in service are not martial"* — while its other three run *"The master fighter," "The master of overcoming enemies," "The master of using people."* Four instances of one frame, two shapes. Opened by T2-3 | 68 | E |
| T2-48 | ⬜ | **`glossary/da-大.md` owes an adverbial flexion.** 大笑之 (41) reads *laugh **aloud***, which the entry's licensed list (*large · greater · master*) does not cover. Also unresolved there: whether the 大▢若▢ frame wants a superlative — ch 41's 大白 now takes one as a recorded exception, and 41 and 45 must be decided together. **The mechanism now exists** — `flexions:` (2026-09-20) | 41 45 + glossary | E |
| T2-49 | ⬜ | **兵 two Englishes** — *weapons* at 31, 50, 57, 69, 80 and *military force* at ch 30 (以兵強天下). *Arms* is unavailable: that is 臂, the body's arms, at 38, 42 and 64 | 30 31 50 57 69 76 80 | E |
| T2-50 | ⬜ | **Two characters now share the "carv-" root** — 制 (28, 32) and 斫 (*zhuó* — to hew) at ch 74, 代大匠斫 → *"those who carve in place of the master carpenter."* They never share a chapter, so no check fires; but 斫 is axe-work where 制 is a fitted cut | 28 32 74 | E |
| T2-53 | ⬜ | ★ **The calamity family — five characters, and *disaster* is worn by two of them.** 禍 (*huò*, 說文 害也，神不福也) → *disaster* at 46, 58 ×2, 69 · **凶** (*xiōng*) → *disaster* at 16, 30 and *ill* at 31 · 咎 (*jiù*, 說文 **災也**; 人 + 各, 相違也 *at odds*) → *fault* at 46 and 9 · 殃 (*yāng*, 說文 **咎也**) → *calamity* at 52 · 患 (*huàn*, 說文 憂也) → *trouble*, locked at 13. **The 守/保/衛 *guard* pattern again**, and unlike 身/神 **a rule could catch this one**: 咎 and 禍 share ch 46, in a parallel couplet that is only legible because they differ. Wants one entry | 13 16 30 31 46 52 58 69 | E |
| T2-55 | ⬜ | ★ **亂 (*luàn*) reads four ways in four lines, and *chaos* is the wrong register** — *disturbed* (3) · *chaos* (18) · *disorder* (38) · *chaotic* (64). **説文 defines it as its own opposite: 亂，治也**, *to bring to order* — the graph is 𤔔, tangled silk between two hands, plus 乙, *what orders it*. A 反訓. **Ch 64 prints the pair: 治之於未亂**, and ch 3 holds 亂 with 治 twice. Entry written and **`status: open` with an empty `forbidden:`**, because it cannot be settled apart from **治** — 12 lines, 9 chapters, no entry, itself split *govern* / *order*. *Order* is also on 正 at ch 45, which is **deferred** (T4-2). Owed: 治's entry, then the lock and the four lines | 3 18 38 64 + 治 | E |
| T2-54 | ✅ | ~~**Three characters wore 玄's *dark***~~ — **昧 → *murky*** (14, 41) and **昏 → *clouded*** (18, 20, 57), Shalom's calls 2026-09-20. 說文: 昧 一曰闇也, 昏 日冥也 — *the sun below the line*. Both were defensible about their own character and neither was available: *dark* is 玄's across six lines including ch 1's 玄之又玄. **`--english "dark"` went from 10 lines, 4 unbacked, to 6 and 0.** *Benighted* declined at ch 20 (a Victorian verdict); the 濁 chime accepted at 41 as resonance. 昏 had been **unrendered** at ch 18, absorbed into 亂. One fork logged (昏昏 / 若昏). **Opens T2-55** | 14 18 20 41 57 | E |
| T1-24 | ⬜ | **Ch 47's 不見而明 reads *understands clearly*, and *understand* is 知's** — the line's own triad is 不行而**知** / 不見而**明** / 不為而**成**, so 知 stands three characters away rendered *knows*. 明 answers 見 (*jiàn* — to look), and the paradox is *without looking, sees clearly* — which is how 22, 24 and 33 already render the same predicate. Found by the T2-46 sweep | 47 | E |
| T4-1 | ⏸ | **民 / 人** — one decision, whole book. Consider taking 身 (T2-1) with it. *Kin to T4-7* | 13 chapters | F |
| T4-2 | ⏸ | **正 / 奇** — five Englishes | 37 45 57 58 78 | F |
| T4-3 | ⏸ | **Em-dashes in the verse** — 14 lines *(ch 28's two and ch 15's one went with their rewrites, not by decision)* | 10 14 29 43 44 51 53 55 58 | F |
| T2-23 | ⬜ | **明白 / 白** — 白 is *the white* at ch 28 and inside the compound *clarity* at ch 10; check 明白 is bound | 10 28 41 | E |
| T2-24 | 🔶 | **淵** — ch 36 → **deep water** (說文 回水也…左右，岸也: circling water, banks left and right). *fathomless* (4) and *depth* (8) still open; *pool* rejected as chlorinated, *the depths* fails the pointing test | 4 8 | E |
| T2-25 | ✅ | ~~**同於X → *merges with*** ×6~~ — **the same as**; 同 is 異's antonym and ch 1 already had it right. Closed T2-26 too | 23 | D |
| T2-26 | ✅ | ~~**同 transitive — 同其塵 · 玄同**~~ — *the same as the dust* (4, 56) and *profound sameness* (56); **同 twice in ch 56 had two unrelated Englishes**. *union* was 合's (55) | 4 56 | E |
| T2-30 | ⬜ | **夷** three ways — *the invisible* (14) · *smooth* (41) · *level* (53). 說文 平也. *Found by the ch 35 reverse check: *level* was about to be taken for 平.* **Ch 14's half settled at T2-52 (2026-09-10) — its *the invisible* stands and the link is carried in notes. What is open is 41 vs 53** | 14 41 53 | E |
| T1-23 | ⬜ | **Ch 69 deletes 主/客.** 吾不敢為主，而為客 → *"move first / move second"* — 河上公's gloss (主，先也) rendered instead of the text. 說文 makes them pointable: 主 is *the flame in the lamp*, 客 *one lodged under another's roof* | 69 | E |
| T2-31 | ⬜ | **客** survives once in the English (ch 15). Restored at 35 as *a passing guest*; **ch 69 still owes it** · T1-23 | 15 35 69 | E |
| T2-32 | ⬜ | **口** → *palate* at ch 12, picking eating over speech. 口 occurs twice; ch 35 now reads *mouth*, which does both | 12 35 | E |
| T2-27 | ⬜ | **同謂之玄 → *Together*** — 同's fourth English, and *together* can read as *jointly they form one thing* rather than *both alike are so called* | 1 | E |
| T2-28 | ⬜ | **復歸 split four-to-three** — the seven-line compound reads *return again* at 16 and 28 ×3, plain *return* at 14 and 52 | 14 16 28 52 | E |
| T2-29 | ⬜ | **命 / 令 collapse into *command*** in the identical 莫之X而 frame — 令 at ch 32, 命 at ch 51. **令 is owed its own entry**: 8 lines, 3 Englishes (*makes* 12 · *command* 32 · *laws* 57) | 12 19 32 51 57 | E |
| T4-7 | ⬜ | ★ **Rank and gender — 大丈夫 · 君子 · 士.** Male rank-words dissolved in two opposite directions. Kin to T4-1 | 15 26 31 38 41 68 | F |
| T4-4 | ⬜ | 剛 owed its own mention | — | E |
| T2-33 | ⬜ | **利** wants an entry — 9 chapters, three jobs: *benefit* (bound to 害 at 56, 73, 81) · **sharp** (利器 36, 57; 利劍 53 — the 說文 sense, 銛也。从刀) · *advantage* (11, 19) | 8 11 19 36 53 56 57 73 81 | E |
| T2-34 | ⬜ | **微** three ways — *the intangible* (14) · *subtle* (15, 64) · *hidden* (36). 說文 隱行也, "to go concealed". **Ch 14's half settled at T2-52 (2026-09-10) — its *the intangible* stands and the link is carried in notes. What is open is 36 vs 15/64** | 14 15 36 64 | E |
| T2-35 | ⬜ | **得** wants an entry — 19 chapters, 30 lines, no entry; *obtain* · *get* · *gain* · *gets*, plus the 不得已 idiom at 29, 30, 31. Ch 39 uses **received** and does not settle it | book-wide | E |
| T2-36 | ⬜ | **貴 / 賤** want an entry — 貴 is 15 chapters, 22 lines (*prize* · *value* · *high status* · *honour*). 說文 makes both **price** words: 物不賤也 · 賈少也 | book-wide | E |
| T2-37 | ⬜ | ★ **神 and 靈 want one entry together** — both on the overlay watchlist, neither has an entry. 神 → *spirit* (6, 39, 60) · *sacred* (29); 靈 → *numinous* (39), which **fails the pointing test** and had no surviving alternative | 6 29 39 60 | E |
| T2-52 | ✅ | ~~★ **Ch 14's opening triad is a definition passage, and all three names are rendered by their explanations**~~ — **ch 14 keeps *the invisible · the inaudible · the intangible*** (Shalom's call, 2026-09-10). Rendering the words themselves (*the level · the sparse · the faint*) would make 夷 · 希 · 微 live threads through nine chapters, and **王弼 argues for it** — he defines 希 at ch 41 by quoting this stanza outright — but it costs ch 14 its clarity this early in the book. **The connection is carried by chapter notes instead: an anchor note at ch 14 and a matching thread note at 15, 23, 36, 41, 43, 53, 64, 70, 74.** The recurrences' own consistency stays open at T2-30 · T2-34 · TRIAGE 14b | 14 15 23 36 41 43 53 64 70 74 | E |
| T4-5 | ⬜ | Glossary harvest — 一 名 希, plus ten new candidates | — | E |
| T4-6 | ⬜ | Guodian **G2–G6** | 5 16 17 18 25 + 26 more | E |
| T4-8 | ⬜ | 說文 (c. 100 CE) quotes the four-greats line as 人亦大 — six centuries before our oldest 人 witness | 25 | E |
| | | **Tier 5 · The harness** | | |
| T5-1 | ✅ | ~~Build **thin-translation** — the only rule that finds *absence*~~ — **prototyped and declined, 2026-09-10 (Shalom's razor).** Its original job is **spent**: it existed to catch chapters that were never translated (ch 65's three ellipses, ch 20's missing movement), and the draft has been 81 of 81 since 2026-08-26. The *thin* half was tested rather than argued: a prototype checking every locked character present in a chapter's Chinese against its locked English **flagged 43 of 81 chapters, seven of them already through Pass D**, and spot-checks were **~90% false positives** from three mechanical causes — inflection (*keeps* safe), insertion (*keep them safe*), and licensed flexions that `render:` states in prose (*see clearly* for 明). `check_locks.py` exists on the promise that it never cries wolf; this breaks it. **A narrower version restricted to invariant multi-word renders still fails on inserted articles** (ch 6's *the sky and the earth*), so the yield approaches zero. **The fault class is real and the instrument is a reader** — ch 9 is a live instance and was found by reading, not by a tool. See `process/principles/renders-no-character.md`, which carries `check: none` deliberately | — | G |
| T5-2 | ⬜ | `repeated-formula` should name the segment's own English | — | G |
| T5-11 | ✅ | ~~Both tools were blind to a formula repeating **inside** one chapter~~ — they indexed into a *set* of chapter numbers, so ch 11's 當其無 ×3 collapsed to one entry and was dropped as "not shared". `--formulas` now covers the whole text and finds **frames** (將欲▢之, ▢得一以▢); `--formulas N` prints one chapter's English beside them. 13 tests. **Ch 11 is where this was found** — `DISCOVERIES.md` §6 | — | G |
| T5-13 | ⬜ | `--formulas` matches whole comma-segments, so **a frame that does not start at a punctuation boundary is invisible** — 為天下貞 sits inside 侯王得一以為天下貞 and ch 39 was missing from the 為天下▢ group, which is how a settled formula got a fourth rendering. Sub-segment matching, or a formula's own characters as a second index | — | G |
| T5-12 | ⬜ | `check_locks.py`'s `repeated-formula` still only compares **across** chapters. Whether the gate can carry the within-chapter case without crying wolf is unsettled — 152 findings at recall. Decide after Pass D, on the evidence `--formulas` is now producing | — | G |
| T5-14 | ⬜ | **Invented repetition — the mirror of `DISCOVERIES.md` §6, and nothing looks for it.** `--formulas` finds a *flattened* repeat (Chinese repeats, English varies). It cannot find an *invented* one (English repeats, Chinese does not), which asserts a link the text never makes. Found by ear at ch 15, where *"could not be made out"* chimed with *"newly made"* across 識 and 新成 — unrelated characters. Needs an English-side n-gram index checked back against the Chinese | 15 + unswept | G |
| T5-15 | ✅ | ~~**A lock's flexions were prose inside `render:`, and no tool could read them**~~ — *"keep safe — and bare keep where the object is not cherished (ch 9 alone)"* was a sentence in a YAML string, so `--english` could not tell a licensed flexion from a breach and the atlas published prose in a data column. Now `flexions: [{ english, chapters, why }]` — the **where** is checkable, the **why** stays for the reader. Seven locks converted (保 執 守 身 一 王 極), new `flexion-chapter` rule, `--english` reports scope and reason, and **36 false `NOT FOUND` rows left `data/locked-renderings.csv`**. 144 tests. *Deliberately not built: any check that a flexion's English stays inside its chapters — inflection and insertion make it the T5-1 trap* | — | G |
| T5-3 | ⬜ | Forbidden lists thin on near-synonyms — *clever*, *depletion*, *energy*. *(無為 gained *effortless* / *without effort* / *takes no action* with T1-3 and T1-4; these three stand)* | — | E |
| T5-4 | ⬜ | Run `--english` on every lock; it is the only reverse-direction check | — | ongoing |
| T5-5 | ⬜ | The 70-item false-friend `info` list is not being read | — | G |
| T5-6 | ⬜ | `import_commentary.py` mis-splits when a heading sits mid-block | — | G |
| T5-10 | ⬜ | `import_shuowen.py` matches exact graphs only, so **95 of the book's 806 characters have no row** and silently look absent from 說文 — 既/旣, 餌, 抱, 難 are all there under a variant graph; 太 genuinely is not. `CLAUDE.md` says "all 711 characters" | — | G |
| T5-7 | ⬜ | `build.py` — deferred until the text stops moving | — | G |
| T5-8 | ✅ | ~~`WORKLIST.md` keeps lists that restate its own table, ungated~~ — `check_worklist.py`, in CI; **`chapter-tally` added 2026-09-05**, gating the Progress line's three copies of the chapter count | — | G |
| T5-9 | ✅ | ~~`data/` is generated but nothing gates it~~ — atlas rebuilt-and-diffed in CI; `build_graph.py` made deterministic | — | G |

**Why passes and not chapters — and why Pass D is the exception.** Passes 0, A, B and C each closed **one decision and every chapter it touched**, in one sitting with the commentaries open, rather than walking 1→81 and re-opening the same argument twenty times. **Pass D is not that kind of pass.** It is chapter work by definition, so the principle that ordered the others does not order it, and it now carries one row per chapter.

**The order within Pass D, and what it costs.** Chapters 4, 3, 38, 28 and 10 were taken in that order for two reasons: **debt density** (ch 28 carried four Tier-1 rows; ch 10 carried a row that turned out to hide four more faults) and **rider chains** — a settled term leaves other chapters immediately inconsistent, and the cheapest moment to fix them is while the evidence is still open. Ch 28 settled 雌 → *the hen*, which put a live inconsistency into ch 10 that same minute; ch 10 followed.

**The cost of that order is real and worth naming: a rider can sit open across several sittings, and nothing gates it.** `check_locks.py` cannot see it — a chapter that renders a term the old way passes every rule, because the rule keys off the character being present and the character *is* present. Only `--english` finds it, by hand (T5-4). **So riders are now written on the chapter rows themselves**, which is the cheapest place they will be seen.

**Numeric order is the sound default from here**, and the one discipline worth keeping is: *when a chapter opens a rider on a named other chapter, close that rider next rather than at that chapter's turn.*

**Pass D is the real work and must not be rushed into a sweep.** Each chapter is a full `chapter-review` with the witnesses and the commentaries open. **The per-chapter rows are derived, not hand-kept:** a `D<n>` row cannot be marked done while a finding row on that chapter is still open, and a finding row cannot name a chapter that has no `D<n>` row. `check_worklist.py` gates both, so the chapter list and the finding list cannot drift apart — which is what happened to the two hand-kept copies this table replaced.

*A second copy of this table, headed "The order of work," sat lower in this file and was deleted on 2026-08-31. It had drifted: it listed Pass D as seventeen chapters including 15, 26 and 30 — none of which has a D-tagged row — while omitting 38, which does, and it still showed Pass C unstarted. **The pass rows above are the only copy.** `PD`'s `Ch` cell now **points at the per-chapter rows** rather than listing chapters, which is the behaviour `pass-chapters` exists to encourage: a row declining to keep a list cannot keep a stale one.*

### The harness — closed 2026-08-31

**T5-8 · `tools/check_worklist.py`.** Four hand-kept lists went stale in three days and a person found every one by reading; `tools/` had no rule that read `WORKLIST.md` at all. Seven rules, all enforcing something the file already says about itself: **pass-chapters** (a pass row's `Ch` is the union of its rows' `Ch`, and a cell that *points at rows* is never checked — declining to keep a list is the goal), **closed-pass** (no pass marked done over an open or part-done row; ⏸ does not block), **chapter-row** and **chapter-cover** (added 2026-09-02 with the per-chapter Pass D rows: a chapter row is derived from its findings, and no finding may name a chapter that has no row — the pass filter is load-bearing, since ch 13 carries pass-D findings *and* 身 in pass E), **tally**, **pass-exists**, **duplicate-id**. 23 tests, each fixture a real failure this repo shipped. Wired into CI.

**T5-9 · the atlas is gated, and `build_graph.py` is deterministic.** `data/constellation-chars.json` had **never agreed with `data/characters.csv`** — both entered in `2466b4d`, but the JSON was built from an older database than the CSV it shipped beside, so it published glosses the CSV had withdrawn (95 characters) and older wordings for 93 more (*"the sea"* against the CSV's *"sea"*). Nothing rebuilt it, and nothing compared them. CI now rebuilds `build_db → export → build_graph` and fails on `git diff --exit-code data/`, the same shape as the glossary gate. **That gate was only safe after fixing the generator:** `export.py` orders all 11 of its queries, `build_graph.py` ordered 1 of 8, so its row order came from SQLite's planner — stable on one machine, and exactly the kind of stability that breaks when the gate moves to another. Every query is now ordered and the co-occurrence map is emitted sorted, so the output is a function of the data alone. Verified: node and link **sets** are unchanged by the ordering fix; only order moved.

---

## The finding

**This is two books.**

Chapters **56–81** were drafted *through* the locks, with `check_locks.py` live, the commentaries in `sources/`, and `chapter-review` running. Chapters **1–41** were drafted in the Google Doc era and have only ever been **swept** — term-swapped against locks settled after the fact.

| | chapters | clean | swap | chapter-level rewrite |
|---|---|---|---|---|
| **1–41** | 41 | **3** (7%) | 16 | **22** (54%) |
| 42–55 | 14 | 2 | 11 | 1 |
| **56–81** | 26 | **20** (77%) | 6 | 0 |

**And a sweep is structurally blind to what is wrong with the early half.** Every lock keys off a Chinese character in order to judge the English, so a chapter that simply **does not render** the character passes every check. Ch 4 drops 吾不知誰之子 (*wú bù zhī shuí zhī zǐ* — "I do not know whose child it is") and erases 帝 (*dì* — the high god of the Shang); ch 25 drops 周行 (*zhōu xíng* — "moves in a circle"); ch 28 drops 常 (*cháng*) from all three 常德 lines; ch 3 dropped 敢 (*gǎn*) and 治 (*zhì*). **All four carried `retrofit: []` and passed every check.** *(Ch 4 repaired 2026-08-31 with T1-2; ch 3 with T1-3. Ch 25 and 28 stand.)* This is the Ch 20 / Ch 65 failure one level down — not an empty translation block, but a *thin* one.

**So the work is a second draft of chapters 1–41, not another sweep.**

---

## Tier 1 · Wrong, not merely inconsistent

Meaning changed. Each needs a decision; most need one line rewritten.

### Errors of fact

1. **Ch 10 — 無知 and 無為 are on the wrong lines.** Our base reads 愛民治國，能**無知**乎 and 明白四達，能**無為**乎. The verse answers them backwards: *"can you lead **without doing**?"* / *"can you be **unknowing**?"* Some editions swap the pair; ours does not, and either way it is unlogged. Also in this chapter: 滌除玄覽，能無疵乎 loses 疵 (*cī* — flaw) entirely, and 明白四達 renders 明 as *"understanding"*.

2. ✅ **Closed 2026-08-31 — the first Pass D chapter.** Four faults and a missing line. **道沖 inverted and given 器's *vessel*** (沖 is *empty*, 不盈 is *never fills*; both halves were flipped). **淵 dropped**, taking one of two matched 兮 frames with it. **吾不知誰之子 not translated at all.** And **帝 erased into "ancestor"** — the inverse overlay: the Chinese names a god and the English deleted him, deleting Laozi's own demotion of him. **帝 is now locked** (`glossary/di-帝.md`) to *god*, rendered *"older than any god"* — not *the high god*, because the definite article asserts a singular supreme deity the scholarship has not settled, **and *the* confers status as effectively as a capital.** Along the way: **兮 never hedges** (twelve occurrences, [asserted]兮，[hedged]), **存 is being-still-there against 亡** — *remain* imports a depletion the first line denies, *exist* belongs to 有 — and **象 is the comparison, not the noun**, because wherever 象 is a noun it is marked by 之/有/大 and here it stands bare. **Closes T2-14c**: the quatrain keeps the Tao as subject at ch 4, the imperative at ch 56. 或/若 fork recorded.

### Lock violations live in the verse

3. ✅ **Closed 2026-08-31 — Pass D's second chapter.** The whole closing movement had **the opposite grammar from the Chinese**: 常使民無知無欲 / 使夫智者不敢為也 / 為無為，則無不治 are built on 使 (*shǐ* — to cause), 使 and 為, and the English on three *"Without"*s, so the sage who acts became a sage who abstains. **為無為 → *"Without effort"* breached the 無為 lock on the one line `glossary/wuwei-無為.md` cites as its own proof** (*"something you actively do … continuous, **effortful**, and difficult"*); it now carries ch 63's English exactly, *"Do the not-doing."* **治 (*zhì* — to govern) had been dropped from the hinge** 是以聖人之治 while still closing the chapter at 無不治 — both ends restored, and *"nothing is left ungoverned"* recovers the echo with 無不為 at ch 37 and 48. **敢 applied** (*never push to act*), **常 restored** (*ever*), and 志 → *ambition*. **The English had also read as manipulation, and the Chinese does not** — 無知, 無欲 and 不敢為 are each the sage's **own** state elsewhere (10 · 1, 34 · 64, 67, 69), and three English collocations invented the asymmetry. The general finding is now a standing principle, ***collocation carries a verdict*** (`notes/translation.md`), beside ch 4's *the definite article*. **Harness hole closed:** the forbidden list held `"effortless action"` and not `"without effort"`; both `"effortless"` and `"without effort"` are now on 無為's list and verified firing. **Still owed at ch 3:** the 知/智 pair (T2-2), and 心 dropped from 使民心不亂.
4. ✅ **Closed 2026-08-31 — Pass D's third chapter.** **失 (*shī* — to lose) is the chapter's spine and had been deleted from its hinge.** Five occurrences, more than in any chapter in the book — 下德不**失**德, then 失道 · 失德 · 失仁 · 失義 — and line 2 read *"clutches at integrity."* The argument that vanished with it: **the refusal to lose is what produces the losing** (王弼: 求而得之，必有失焉). **And *clutches* renders 執, which is not in the chapter** — it came from 王弼's gloss on the line *above*, describing what 上德 lacks; 河上公 reads the contrast as **visibility**, not grasping. **無為 → *"takes no action"*** was invisible to `check_locks` (`"non-action"` was on the list, `"takes no action"` was not — now added and verified firing). **上** read *highest* ×2 and ***Ultimate*** ×3 with a capital, on a ladder's rung-marker, against ch 41 and against `glossary/wei-為.md`'s own table. **首 / 始** shared one English in adjacent lines; **華 / 實** had three across two stanzas. **以為 → *"has something it acts for,"*** restoring the 2×2 grid 王弼 states outright (無以為者，無所偏為也). The invented *pure*, *imitation*, *life's* and *of being* are all gone, and the 禮 rung now takes the two lines the Chinese gives it. **大丈夫 → *the great person*, gendered reference removed deliberately (Shalom's call)** — standing rule 2's default, so no `shaloms-call`; the violation was the silence. **Opens T4-7** (rank and gender) and **T2-21** (厚). Two collation notes recorded: 扔/仍 in `sources/variants.yaml`, 焦竑's four 處 in `notes/manuscript.md` only.
5. ✅ **Closed 2026-08-31.** Bare 德 had been given **玄德**'s English on three lines, in a chapter containing no 玄. 德 is locked to *integrity*, and `--english "profound integrity"` now returns only 玄德's four lines (10, 51, 65 ×2). **The cost was structural:** the stanza is a three-term parallel — 道者同於道；德者同於德；失者同於失 — and an adjective on the middle term alone broke it. Second time this chapter has handed 德's slot to the wrong word; the first was 信 (*xìn* — trust) taking 德's.
6. **Ch 16 — 守 → *"Embrace."*** 守 is *hold fast to*, 抱 is *embrace*; the lock says do not swap. **Ch 52 does it right.**
7. **Ch 28 — 守 → *"attune to"*** on all three 知其X守其Y lines, and 常 dropped from all three 常德.
8. **Ch 29 — 為 rendered *"force"* three times in four lines.** 為 is locked to *do / handle / serve as*. *Force* is a reading smuggled in as a translation: it supplies violence 為 only implies, and makes 無為 look like counsel against aggression rather than against handling as such. **Ch 64 carries 為者敗之，執者失之 verbatim and now reads *"Those who handle it ruin it."*** The shared formula must not read two ways. Line 1 also carries an em-dash.

### Inventions and overlays

9. **Ch 31 — 左/右 rendered *"creation"/"destruction"*, then rendered literally four lines later.** The chapter cannot be read against itself, and the reader cannot see that 吉事尚左，凶事尚右 is explaining 君子居則貴左.
10. **Ch 13 — 無身 → *"the separate self dissolves."*** 及吾無身 is *"when I have no body."* An Advaita frame on the one line where 身 works hardest.
11. **Ch 14 — 古始 → *"the primordial source."*** *The Source* is forbidden for 母 and is the register the naturalistic razor exists to strip. 古始 is *"the ancient beginning."*
12. **Ch 35 — 往 → *"the world routes to you,"* twice.** Network vocabulary; our named besetting temptation.
13. **Ch 16 — *"Each returns energy to its root."*** 氣 is not in this chapter.
14. **Ch 32 — the closing simile is garbled.** 譬道之在天下，猶川谷之於江海 is *"the Tao in the world is like streams and valleys to rivers and the sea."* The 譬…猶 frame is gone and the comparison's direction is muddled.
15. **Ch 28 — 谷 → *"reservoir"*, 谿 → *"deep ravine"*, 官長 → *"master orchestrator"*, 大制 → *"the great orchestrator."*** Ch 66, 15 and 32 all render 谷 as **valley**, which is the plain sense; a reservoir is *built* and holds by design, and the chapter's argument is that lowness gathers **without** contrivance. *Orchestrator* is the mechanistic register, one line below 器. 谷 also wants an entry — seven chapters.
16. **Ch 28 — 雄/雌 as *"assertive energy" / "yielding energy."*** 雄 and 雌 are a **rooster and a hen**. Rendering the book's central feminine image as an abstract polarity of energies is a live cost, and 雌 is load-bearing for the feminine thread. **Take ch 28 as one review, not five swaps.**

### Unlogged departures — defensible, but nothing records them

17. **Ch 65 — 明 → *"clever."*** Breaks the 明 lock, and **both commentators support the break**: 王弼 明謂多見巧詐蔽其樸也. Almost certainly right; **the one licensed exception to a settled lock in the book, and nothing records it.** Owed: a line in `notes/translation.md`, a paragraph in `glossary/ming-明.md`, a `lock-ok` waiver, and *clever* added to 明's forbidden list so the exception is visible rather than invisible.
18. **Ch 30 — 佐 → *"One who rules."*** 佐 is *to assist*; the chapter addresses a ruler's **adviser**. 河上公 rescues it reflexively — 謂人主能以道自輔佐也 — but we follow a commentary against the plain grammar without saying so.
19. **Ch 41 — 大器晚成 → *"never completed."*** Our table reads 晚成 (**late**-completed); *never completed* is the Mawangdui 免成 reading. Bring the English to our Chinese, or take the silks deliberately and record it.
20. **Four `unlogged-variant` warnings**: ch 2 (相形…相盈), ch 9 (銳), ch 26 (君子), ch 51 (亭之毒之). Each claims a `notes/manuscript.md` entry that does not exist.
21. **Ch 68 — 配天 — the chapter and its own note disagree.** Reads *"partnered with the sky"*; 天 stands alone with no 地 near, which the lock sends to *nature / the natural*. **The single contested line for the 天 split.**

---

## Tier 2 · One character, many Englishes

19. ✅ **Closed 2026-09-08. 說文解字 gives the four characters four different hands, and one of them is not a hand at all.**

   | | 說文 | the graph | now |
   |---|---|---|---|
   | 持 (*chí*) | 握也 — *"to grip"* | 手 (*shǒu* — hand) + 寺 | **hold** (9, 64, 67) |
   | 執 (*zhí*) | **捕罪人也** — *"to seize a criminal"* | 丮 a reaching hand + 㚔, **manacles** | **grasp** · ***seize*** at 74 |
   | 守 (*shǒu*) | **守官也** — *"to keep an office"* | 宀 a roof + 寸 (法度, a regulation) — **no hand** | **hold to** · ***guard*** at 9, 67 |
   | 保 (*bǎo*) | **養也** — *"to rear"* | 人 a person + 孚, a hand over a child | **keep safe** (15, 62, 67) · bare ***keep*** (9) |

   **Four entries written and locked:** `zhi-執.md` · `shou-守.md` · `bao-保.md` · `chi-持.md`. Full argument in `notes/translation.md` → *The holding family*.

   **執 is not the 強 case.** This file had framed it as one character with opposite valences that the English must hold together. **The character is narrower than that: it is a legal word.** 說文 is 捕罪人也, and the book uses the judicial sense twice with no metaphor in it — ch 74's 執而殺之, which 河上公 reads as statute (乃應**王法**執而殺之…先**刑罰**), and ch 79's 執左契, a bond enforceable before there were written laws. So 執者失之 is not a caution against clinging: **its object is 天下, and the clause before it says the world is a 神器.** You cannot take a sacred vessel into custody. 王弼: 物有徃來而執之，故必失矣, and he brackets the verb with ch 28's blade, 不施為**執割**也. **Ch 14 and 35 are therefore the joke, not the exception** — you cannot arrest the world, so arrest the one thing that will not break in your hand. ***Seize* at 74 is the dictionary headword, not an exception** (Shalom's call).

   **The live error nothing could have caught: *guard* was worn by three characters** — 守 (9), 保 (15), 衛 (67). And **守 and 保 stand together in both ch 9 and ch 67**, so a `forbidden:` rule keying off a character's presence can never separate them. Both entries carry a *"what no rule can enforce"* section for exactly this. The ch 15 decision of 2026-09-06 had also been argued from ch 9's **literal gloss table** rather than its verse — ch 9's verse renders 保 nowhere, and its *guard* belongs to 守.

   **Riders applied:** 搏 (14) had taken 執's English inside 執's own chapter (now *get*, on 得's word) · 握 (55) → *grip*, freeing *grasp* book-wide · 左 restored at 79 · 有 (59) had *Holding* on it, with 有國 reading two ways in adjacent lines · 襲 (52) had *holding* on it, now matched to ch 27 · ch 5's *in silence* rendered nothing.

   **Left open:** ch 9 → **T2-51**; whose half 執左契 names; 有's transitive uses beyond 有道者.

51. ⬜ **Ch 9 renders neither 持 nor 保, and invents a vessel.** 持而盈之，不如其已 reads *"Filling a vessel, stop before spilling"* — 持 (*chí* — to hold) is gone, 不如 (*bù rú* — not as good as) is flattened to a comma, and **器 (*qì* — vessel) is not in the chapter**. 揣而銳之，不可長保 reads *"An over-sharpened blade's edge cannot last"* — 保 gone, *blade's edge* invented for 銳 (*ruì* — sharp). The chapter's spine is three things you cannot keep, in three different characters — 持 · 保 · 守 — and the English keeps one of them. **A stanza rewrite, not a term swap.** Ch 9 also carries T2-1 (身退 → *"cease striving"*, where *striving* is 爭's) and T1-20's unlogged 銳 variant, so the three should move together.


1. **身 (*shēn* — body) drifts, and ch 54 uses two Englishes inside one stanza.** 修之於身 → *"in your **body**"*; five lines later 以身觀身 → *"the **self** through your own **self**."* Across the book: *body* (13, 54), *self* (7, 44, 54), *themselves* (7), dissolved entirely at ch 9 (身退 → *"cease striving"*). **Same shape as 民/人 — decide them together.**
2. **智 rendered four ways, and *"cunning"* covers four characters.** *cunning* (3), *cleverness* (18, 19), *intelligent* (33), *guile* (65). Some spread is legitimate — 智 runs from *wisdom* at 33 through *cleverness* at 19 to *artifice* at 65, a licensed split like 事. What is not legitimate is that it happened by accident. **And *cunning* also did duty for 知 (ch 3, adjacent line), 巧 (ch 57), and a fourth at ch 58.** **Ch 3 is closed (2026-08-31, with T1-3):** 無知 → *unknowing*, 智者 → **the knowers**, and *cunning* is off the chapter. The word was chosen because **the commentators diverge on who the 智者 are** — 王弼 prints 智者 and glosses 智者謂知為也 (*"those who know how to handle"*), 河上公 prints 知者 with the phonetic note 知音智 and glosses 思慮深不輕言, almost verbatim what he says of the *approving* 知者 at ch 56 — so any English specific enough to settle it picks a side. Fork now in `sources/variants.yaml` and `notes/manuscript.md`. **The book-wide split stands** at 18, 19, 33, 65. **Take 智 with 知, 巧, and the locked 明** — those four are the book's whole epistemology and three are unlocked.
3. **士 (*shì*) has three Englishes, two on the identical phrase.** 善為士者 is *"The ancient masters"* (15) and *"The master warrior"* (68); 上士/中士/下士 are *students* (41). 王弼 defines it flatly: 士，卒之帥也, *"the commander of troops."* None of them is a master of anything, and *masters* puts back the register the 聖人 lock exists to keep out.
4. **氣 has three Englishes:** *life energy* (10), *vital breath* (42), *vital energy* (55).
5. **靜 reads *"Silence"* at ch 26** alone, against *stillness* at 15, 16, 37, 45, 57, 61.
6. **君 reads *ruler* then *mastery* three lines apart at ch 26 — and 君子 is rendered *"the sage"* at ch 26 and twice at ch 31.** Conflating 君子 with 聖人 erases a distinction the book draws deliberately.
7. **志 (*zhì*) reads *striving* (3) and *will* (33).** Small, real, no entry.
8. ✅ **Closed 2026-09-02 — and it was nine 善, not eight.** One had been **deleted**: 水**善**利萬物 read *"it nourishes the countless things"* with the 善 gone, and *nourish* is 養's English at ch 34 and 51, a character **absent here**. The lock is now applied to all nine. **上善 → *the most masterful*** (Shalom's call), following 河上公's 上善之人如水之性 and ch 38's settled 上 → *the highest*; *the highest excellence* was declined as bloodless and as Legge's phrase, ***true mastery*** because 真 (*zhēn* — genuine) is live at 21, 41, 54 and **上 is a graded rank word** whose middle rung ch 41 prints. **The finding that outlives the chapter: 善 governs a verb, 18 instances out of 18**, so X善Y is *masterful **at** Y* and not *masterful Y* — the seven couplets are the only place in the book the parse could have gone the other way. **Four more repairs on the way**: 幾 → *near*, not *"one with the Tao"*; 仁 → *humaneness*, breached silently by *pure kindness* because *kindness* is not on its `forbidden:` list; 惡 → *loathes*, marked *wù* by 河上公's own *fanqie*; and *"always blameless"*, where 常 has zero occurrences and 尤 is a **hapax**. **Opens T2-24** (淵).
9. ✅ **Closed 2026-08-31.** **argue** in both; ch 45 reads *"Great argument seems halting."* Ch 81's Notes had licensed the split on the premise that **辯 is praised at ch 45** — wrong. **The 大X若Y frame does not endorse its X**, and the proof is one line above: 大巧若拙 puts 巧 (*qiǎo*) in the frame, and 巧 is condemned at ch 19 (絕巧棄利) and ch 57 (人多伎巧). The commentators put the two chapters together, not apart — 王弼 on ch 45: 大辯因物而言，己**無所造** (*"great 辯 speaks according to things; the self invents nothing"*), against 河上公 on ch 81: **不綵文**也 (*"does not ornament their words"*). Not the 強 both-valences case: *eloquence* manufactured the appearance of a double. 說文 on 辯: 治也。从言在辡之閒 — words between **two tattooing knives**, a courtroom. 訥 → *halting* (說文 言難也, of speech specifically) rather than *awkward*, which overlapped 拙. **Spun off as T2-20:** 巧 has the identical fault, *skill* (45) against *cunning* (19, 57).
10. ✅ **Closed 2026-08-31, and the cause was a manuscript fork nobody had logged.** The two Englishes were **not two readings of one character**: ch 27 rendered 襲 (*xí* — to layer a garment over another), ch 52 rendered **習** (*xí* — to practise), which our base text does not print. Both commentaries print 習 at ch 52 — 河上公 glosses it 習修常道 — and the Siku 王弼 carries 〔案習各本作襲〕. **We keep 襲 in both**, on the pair: 是謂襲明 / 是謂襲常 is one frame, and 明 / 常 are bonded by 知常曰明 (16, 55). **襲 is 說文's 左衽袍 — a robe closed to the left, i.e. grave-clothes**, one garment over another; *inherit* is a derived sense and lost the layering. Now *"clarity worn covered"* (27) and *"holding the ever-present covered"* (52). Fork recorded in `sources/variants.yaml` and `notes/manuscript.md`. **The `unlogged-variant` rule could never have caught this** — it fires only on variants a chapter *claims*, and an English quietly following an unrecorded reading is invisible to it.
11. ✅ **Closed 2026-08-31.** 殆 (*dài*) had **five occurrences and four Englishes, none of them 殆**: *"Not even death threatens this"* (16), *"Inexhaustible"* (25), *"depletion"* (32, 44), *"no harm"* (52). All five now read **danger**, and *danger* renders nothing else — one-to-one in both directions. 說文 危也; the graph is 歺 (*è*), the **bare-bone radical** of 死 and 殃. **Both commentators converge in all five places** (河上公 不危殆 ×3; 王弼 免殆 at ch 25) — no divergence to preserve. Two of the four Englishes were other characters' words: *harm* is 害's (35, 56, 66, 73, 81), *inexhaustible* is 窮's (6, 35). **Ch 16 was a mistranslation, not a mismatch** — 没身 is "to the end of one's life," as ch 52 already had it, not *death*; and the sentence belonged to the person, not the Tao. **Two extras fixed on the way:** ch 25's 周行 (*zhōu xíng* — "moves in a circle") had been dropped entirely and is restored, and **ch 15's *"aware of danger from all sides"* was invented** — no 殆 in that chapter, no threat in the Chinese, and 河上公 has 畏四鄰**知之**, *the fear of being found out*; now *"Hesitant, as if wary of neighbors on four sides."* **殆 and 畏 both still owe glossary entries**, so *danger* is correct book-wide but unenforced.
12. ✅ **Closed 2026-08-30.** All three read **"By this."** — ch 57 keeps its colon, which is punctuation and marks the only forward-pointing one of the three. *"Precisely"* had no warrant; *"here, now"* was 河上公 (*Héshàng Gōng*)'s gloss 此，今也 (*cǐ, jīn yě* — "'this' means now") lifted into the verse, and it picked his reading over 王弼 (*Wáng Bì*)'s anaphoric 此上之所云也 (*"'this' is what was said above"*), which the old note claimed it "held." **Two stale claims corrected** — `notes/manuscript.md` §*What the commentators say 此 means* and `DISCOVERIES.md` §2's table and evidence list. **Rider:** ch 57's 其 (*qí* — it) had been rendered *"this"*, colliding with 此 one clause apart; now *"it."* **Two standing principles added** to `notes/translation.md`: *the commentaries are evidence, never candidate renderings*, and *register — no modern spiritual idiom* (the "here, now" / *Be Here Now* family).
13. ✅ **Closed 2026-08-30.** All three read **"They let go of what is out there and take what is here."** 彼 (*bǐ* — that, yonder) occurs **exactly three times in the book and all three are this tag**, so there was no competing context. Ch 12 and 38 had been rendering the *referents* and deleting the *deixis*; ch 72's axis-not-referent solution was right in all three. **Two side gains:** *embrace* freed from 取 (*qǔ* — to take) at ch 38 — it had been wearing four characters, and the other two are T2-19; and ch 12's *"gut wisdom"* turned out to be a **lock breach against its own entry**, which has a paragraph headed *"Why 'belly' and not 'gut'"* citing ch 12. **Harness hole found and closed:** `covers:` records a `render:` but no `forbidden:` list, so *gut* was unforbidden book-wide; `"gut"` is now on 心's `forbidden:` and verified firing. **Still owed on ch 38's stanza** (Pass D, T1-4): *"thickness **of being**"* and *"**life's** fruit"* invent words.
14. 🔶 **難得之貨 — closed 2026-08-30.** All three read **"rare goods"**, and **貨 (*huò*) is now locked to *goods* with its own entry** (`glossary/huo-貨.md`, `status: locked`, forbidding *treasure · precious · scarce · riches*). The error was not inconsistency: all three Englishes put the value **in the object** — *the precious* (貴's word, and 貴 is the verb in the same line), *rare treasures* (寶's), *precious goods* — which made 不貴難得之貨 circular and dropped the ruler out of a sentence about what a ruler does. 貨 was also wearing 富's *wealth* at **ch 44**, now swept. *Rare* renders no character and that cost is recorded: **"hard" is 堅's**, and 難's own *difficult* will not go attributive. **Two general rules came out of it** — *one Chinese modifier, one English modifier* (no near-synonym doublets; they are a KJV tell), and the note that English has **no one-word adjective for "difficult to obtain" that is not also a value word**, which is why three chapters drifted the same way independently. **Ch 3 riders applied:** 民 restored to the middle clause of the triad, and 不貴 → *prizing* in both ch 3 and ch 64. **Still owed at ch 12:** 妨 (*fáng* — to hinder) reads *corrupt*, a moral word for an obstruction word. **信不足焉，有不信焉 — closed 2026-08-30**, the oldest open item in the debt list. Both chapters now read **"Where trust runs short, there is no trust,"** and **ch 23's `lock-ok` waiver is gone with it** — it said *"revisit in the editing pass,"* and this was that pass. The split had been argued on context (ch 17 political, ch 23 about 同 *tóng* — merging), and **the commentators cross it in both directions**: 王弼 reads the line at **ch 17** as impersonal natural law (此自然之道也), 河上公 supplies a ruler at **ch 23** (君信不足於下). **Ch 17 was also wrong, not just mismatched** — *"leaders don't trust the people"* made 信 an inner attitude, which `glossary/xin-信.md` forbids (信 is a 符契, a split tally — a correspondence that can be checked), and ran the failure backwards: 河上公 has the people **deceive** a ruler who could not be relied on. Both old versions asserted **reciprocity**, which is 河上公's reading; 王弼's is **emergence**, with no second party. The English is now agent-free and holds both. `glossary/xin-信.md` updated to match. **挫其銳…同其塵 — closed 2026-08-31, and the only Pass C item that does not fully unify.** Ch 4's four lines now carry ch 56's nouns and its couplet lineation: **"It blunts the sharpness, untangles the knots. / Dims its own light, merges with the dust."** The live error was a **lock breach** — *brilliance* is on 明's `forbidden:` list, 光 (*guāng*) is 明's counter-term, and `glossary/ming-明.md` had **already glossed both chapters together** as *dim your light*. `check_locks.py` could not see it (no 明 in ch 4, so the evidence gate drops it to `info`); only `--english` finds this class. **The subject is deliberately left split** and travels with ch 4's rewrite (T1-2): 王弼 reads ch 4's lines with **the Tao** as subject and ch 56's as **a person's practice**, and unlike ch 17/23 the frames do not appear in the wrong chapters. Ch 4's subject is downstream of 道沖 inverted, 吾不知誰之子 dropped, and 帝 erased — deciding it now means deciding it twice. **Ch 56 held the ground** because it is attested **complete at Guodian**; ch 4 is not attested at all.
15. **Formula pairs the checker names:** 是謂玄德 (10 vs 51/65) · 故能成其大 (34 vs 63) · 可以長久 (44 vs 59) · 是以聖人猶難之 (63 vs 73) · 為者敗之，執者失之 (29 vs 64) · 為天下式 (22 vs 28) · 物或惡之 and 故有道者不處 (24 vs 31) · 不貴難得之貨 (3 vs 64).
16. **事 wants an entry, and 無事's licensed split needs confirming.** *meddle* at 48 and 57, *serve the not-serving* at 63. `glossary/shi-事.md` recommends making ch 63's word the standard on the strength of ch 57's quartet. Not applied.
17. **私 reads two ways** — *private self* (7) and *the self* (19) — sheltering under 公's `covers:`. Ch 19's is arguably right in place, but 私 may want its own entry rather than a `covers:` line.
18. **Ch 16 — 復命 → *"returning to what was given."*** No longer borrowing another character's English, but still interpretive for 命. Worth a look when ch 16 is reviewed.

19. ✅ **Closed at ch 23, 2026-09-03; the transitive uses spun off as T2-26.** 同 (*tóng* — the same) is **異 (*yì* — different)'s antonym**, printed against it in ch 1's own clause 同出而異名 — which our ch 1 already renders *"the **same** origin."* Ch 23 had *merges with* **six times**, turning a sameness word into motion and dissolution. **Both commentators gloss 同 with 同**: 王弼 與道**同體** (*"of one body with the Tao"*), 河上公 所謂**與道同**也. **And the chapter's claim is resonance, not union** — 河上公 closes it with the 易經 formula 同聲相應，雲從龍，風從虎，水流濕，火就燥 (*"like sounds answer each other: clouds follow the dragon, wind follows the tiger, water flows to the damp, fire goes to the dry"*), **four pairs, every one of them two things**. ***"Is the Tao"* was proposed and declined**: 同於道者，道亦樂得之 needs two parties, and identity leaves none — and unlike ch 8's 幾, 同 does not survive being absorbed into English *is*. **Four more repairs on the way**: 事 (locked to *affairs*) read *actions*; *intensity* and *sustain* rendered nothing (*intensity* was 王弼's 暴疾 lifted from commentary); 人 read ***we***; and 希言自然 was an instruction plus a reason where the Chinese is an equation — **the commentators split on 希 and *"speech scarcely heard"* now holds both**. **Spun off as T2-26:** 同其塵 at ch 4 and 56 (*merges with the dust*) and 玄同 at 56 (*the profound union*) — 同 used **transitively**, so possibly a licensed flexion rather than the same English, but three of the five Englishes still stand. **Pass E, not D:** it is a term sweep across two settled chapters, not a chapter rewrite. **Three forks logged**, one meaning-bearing. **T2-26 closed the same day**: 同其塵 → *the same as the dust* at ch 4 and 56, and **玄同 → *profound sameness***, matching 是謂玄德's *"This is called profound integrity"* ×4. **同 occurs twice in ch 56 two lines apart** and had two unrelated Englishes, hiding that the practice and its name are one word. *Union* turned out to be **合 (*hé* — to join)'s** English at ch 55 (牝牡之合). *Share the dust* was the first candidate and **failed on the link** — it leaves 玄同 with no noun. **Spun off as T2-27:** ch 1's 同謂之玄 still reads *Together*.

---

## Tier 3 · Missed parallelisms

Structure the Chinese has and the English does not. These are rewrites, and they are where the poetry is.

1. **★ Ch 22 ↔ Ch 24 — the 不自X / 自X者 mirror, the biggest in the book.** Ch 22's stanza was rebuilt 2026-08-27 following 王弼's one-to-one mapping; ch 24 is its exact negative and still reads in unrelated words. Ch 24 also flattens 餘食贅行 (王弼: 盛饌之餘, *"the leftovers of a rich feast"*, and 肬贅, a wart) to *"wasteful and superfluous"*, and renders 物 as *"the material world."* **Its last two lines are shared verbatim with ch 31 and must move together.**
2. ✅ **Closed 2026-09-02 with T2-8.** Seven identical three-character couplets had seven English shapes — *it is a N · it is N · it is ADJ · it has N* — and now run one shape seven times: **"In X, masterful at Y."** The shape was decided by counting, not by taste: 善 takes a **verb** in all eighteen of its other X善Y instances, and the adjectival alternative (*masterful ability*) works only where Y is already a skill word, collapsing on *masterful ground* and *masterful trust*. 能 → ***what can be done*** rather than *ability*, because 能 has 32 lines in the book and **31 are the plain modal *can***; ch 8's is its only nominal use.
3. **Ch 11 — three identical 當其無，有…之用 frames rendered three ways**, and 有之以為利，無之以為用 loses both 利 and 用 into *"creates potential."*
4. **Ch 36 — four 將欲X之，必固Y之 conditionals nominalized into abstract laws.** *"Contraction requires firm expansion"* has no agent and no *first*. Ch 36 is the least dense chapter in the book (0.88).
5. **Ch 28 — three four-beat stanzas rendered as prose**, with 守 wrong and 常 missing in all three.
6. **Ch 39 — the 得一 and 無以 lists are a mirror, and the sixth pair breaks.** The first ends 侯王得一以為天下**貞**, the second 侯王無以**貴高**; our English answers *"true anchors"* with *"their anchoring."*
7. **Ch 13 — 寄/託 are a pair**, rendered *"entrusted with"* and *"truly care for."*
8. **Ch 33 — 力/強** — closed by Pass A, but the chapter's remaining couplets are worth a look when 智 is settled.

---

## Research · R1 — 韓非's divergent lemmas

*Opened 2026-08-29, after the `unmarked-lemma` defect was fixed. The marks now exist; nothing has been done with what they reveal.*

**Why this is worth a pass of its own.** 韓非 (*Hán Fēi*) died in **233 BCE**. His quotations in 解老 (*Jiě Lǎo* — "Explaining Laozi") and 喻老 (*Yù Lǎo* — "Illustrating Laozi") are **the oldest witness to the Laozi text in existence** — older than the Mawangdui silks (c. 200 BCE) and roughly contemporary with the tail of the Guodian tradition. And unlike Guodian and Mawangdui, **his text is vendored in this repository and quotable**: it is public domain by age, so `PROVENANCE.md`'s "record the fact, never the transcription" rule does not bind here. We can cite the reading directly.

**35 of his 53 lemmas differ from our base text**, every one now carrying `*`. Four more differ only in printed glyph and are correctly unmarked. The divergences are **not yet in `sources/variants.yaml`, so `--witnesses N` shows nothing for any of these chapters.**

**Five of them bear directly on decisions already open on this list**, which is the real argument for doing it:

| ch | 韓非 reads | our base | bears on |
|---|---|---|---|
| 60 | 聖人亦不傷**民** | 聖人亦不傷**人** | **T4-1**, the deferred 民/人 decision — the oldest witness has 民 where we have 人 |
| 27 | 雖**知**大迷 | 雖**智**大迷 | **T2-2**, 智 rendered four ways; 韓非 reads the other character |
| 64 | **恃**萬物之自然 | **以輔**萬物之自然 | 恃 (*shì* — rely on) against 輔 (*fǔ* — assist), on a line swept for 敢; 恃 was itself settled 2026-08-26 |
| 67 | **吾**有三寶，持而**寶**之 | **我**有三寶，持而**保**之 | the locked 我/吾 pair (`glossary/wo-wu-我吾.md`), and 保/寶 feeds **T2-19**'s holding family |
| 36 | **邦**之利器 | **國**之利器 | the 邦/國 Han name-taboo already logged at ch 61 in `notes/manuscript.md` |

**Substantive forks worth their own entries**, beyond those five:

| ch | 韓非 | our base | what turns on it |
|---|---|---|---|
| 38 | 失道而後**失**德，失德而後**失**仁… | 失道而後德，失德而後仁… | he repeats 失 (*shī* — to lose) in all four clauses: *"lose the Tao, then lose integrity"* rather than *"lose the Tao, and then integrity."* **A different chapter**, and we edited it in Pass B without knowing |
| 58 | 廉而不**穢** | 廉而不**劌** | 劌 (*guì* — to wound) against 穢 (*huì* — foul, weed-choked); our verse reads *"sharp but does not wound"* |
| 50 | 虎無所**錯**其爪 | 虎無所**用**其爪 | 錯 (*cuò* — to set down) against 用 (*yòng* — to use) |
| 36 | 將欲**取**之 | 將欲**奪**之 | 奪 (*duó* — to seize by force) against 取 (*qǔ* — to take); **T3-4** is rewriting these four conditionals |
| 36 | 魚不可脫於**深**淵 | 魚不可脫於淵 | 韓非 adds 深 (*shēn* — deep) |
| 67 | 故能為成**事**長 | 故能成**器**長 | 器 (*qì* — vessel) is locked; 韓非 reads 事 (*shì* — affairs), also locked |
| 54 | **脩**之身 | 修之**於**身 | 脩/修 is a lexical choice, deliberately **not** folded as a printing variant; he also drops 於 |
| 59 | 治人事天莫**如**嗇 | 莫**若**嗇 | same sense, real variant |
| 47 | 不出**於**戶，**可以**知天下 | 不出戶知天下 | he adds 於 and 可以 throughout |

**Noise to record but not to log.** Roughly a third of the 35 are 也 / 矣 / 乎 / 之 particles added or dropped — 韓非 is quoting inside prose essays, often from memory, and pads for rhythm. Ch 1's 道**之**可道，非常道**也** is the clearest case. **Mark them, do not give them `variants.yaml` entries**, or the apparatus fills with noise and the real forks stop standing out.

**How to do it accurately.**

1. **Read the lemma in its essay, not alone.** 韓非 sometimes quotes a line to argue against a reading, and the surrounding 〔解老〕 or 〔喻老〕 prose says which. The vendored file has both.
2. **Use the existing schema** — `chapter · line · base · witnesses · meaning_bearing · our_call · note · logged`, with `hanfeizi` as the witness id, which `sources/variants.yaml` already declares in its header.
3. **`our_call: base` unless there is a reason** — this is an edition of the received recension, as settled at ch 25 and ch 19.
4. **Set `meaning_bearing` honestly.** Particle padding is `false`; a different content word is `true`. Every `true` needs a `notes/manuscript.md` entry or `check_locks.py` will fail the build — which is the ratchet working.
5. **Regenerate**: `python3 tools/build_db.py && python3 tools/export.py`, then `--witnesses N` on the affected chapters.

**The command that produces the evidence table:** fold each `*`-marked lemma with `lib.corpus.fold`, align it against `load_base_text()` with `difflib.SequenceMatcher`, and print the non-equal opcodes. That is how the tables above were generated; it takes about fifteen lines.

**Do not start this before Pass D.** Ch 36, 38, 54, 64 and 67 are all being rewritten, and a variant entry written against a line that is about to change will have to be written twice.

---

## Tier 4 · Open calls, deferred by Shalom

- **★ Rank and gender — 大丈夫 · 君子 · 士. T4-7, opened 2026-08-31 with ch 38.** This book has a family of **male rank-words**, and the manuscript has been dissolving them silently **in two opposite directions**. 大丈夫 (*dà zhàng fū*, ch 38, a hapax) was turned into a **modern psychological type** — *"the mature person"*, now *the great person*. 君子 (*jūn zǐ* — literally *a ruler's son*, the Confucian gentleman, ch 26 and 31) is rendered **"the sage"**, which hands the opposition's honorific to Laozi's own figure, whose name is a different word entirely (聖人). 士 (*shì* — a male service rank: knight, officer, retainer, ch 15, 41, 68) reads three ways, twice on the identical phrase 善為士者. **The shared question is what to do with *rank*, and it is not the one-character-many-Englishes question that T2-3 and T2-6 currently file it under** — a rank word universalised loses the rank, which is often what the line is about. 說文 makes the stakes concrete for 夫: 一以象簪也…人長八尺，故曰丈夫 — *"the single stroke depicts a hairpin… a person stands eight 尺 tall, therefore we say 丈夫"* — a measurement and a capping ceremony, not an inner state. Standing rule 2's carve-out is for the **incidental** male-default; these are not incidental. **Owed:** one decision across all three, the seam noted wherever it is universalised, and a check on whether 君子 can keep *"the sage"* at all. **Kin to T4-1 (民/人) and to T2-1 (身) — the same question about social categories.** Cross-refs: T2-3, T2-6.

- **民 / 人 — one decision, whole book, deferred 2026-08-25.** 民 (the governed, an eye pierced by a blade) reads *"the people"* in all 32 of its lines — consistent, unlogged, never argued for. 人 drifts, and **ch 57 renders it both ways two lines apart.** A rule settled at one chapter propagates to twelve others and to the cross-chapter rhymes in `notes/reading.md` (72 → 74 → 75 turns on 民不畏X; ch 80's 使民重死 is load-bearing for ch 75's 民之輕死). Ch 74 reads *"the people"* as a **hold, not a precedent**. Owed: `glossary/min-民.md`, very likely a 人 entry or `covers:`, a sweep, and a `notes/reading.md` pass. **This sweep adds 身 to the same shape of problem — consider deciding the three together.**
- **正 / 奇** — five Englishes across ch 37, 45, 57, 58, 78. Owed: `glossary/zheng-正.md`.
- **Em-dashes in the verse** — 17 lines across ch 10, 14, 15, 28, 29, 43, 44, 51, 53, 55, 58. Ch 44's three are good. Ch 10 and ch 51 share the same en-dash on the same line (長而不宰) and move together.
- **柔 → soft, 剛 → hard** — 剛 still owed its own mention; 柔 is `covers:`-ed by `ruo-弱.md`.
- **Glossary harvest** from `TRIAGE.md`: 一 is owed only its entry, then 名, then 希. **This sweep adds 身, 氣, 靜, 君, 士, 智, 事, 志, 谷, 恃.**
- **Guodian G2–G6** (`PLAN.md`). G1 closed 2026-08-28.

---

## Tier 5 · The harness

1. **Two proposed rules remain unbuilt** — `incomplete-draft` and `glossary-self-check` (`PLAN.md`). **Neither would have caught most of what the 2026-08-28 sweep found.** What would:
   - a **thin-translation** heuristic — English words per Chinese character against the book's own median. It ranks ch 36 (0.88), ch 11 (0.98), ch 3 (1.03), ch 7 (1.04) at the bottom, and all four turn out to have dropped material. **The only rule here that finds *absence*.**
   - **`repeated-formula` should name the segment's own English**, not the closest line by token overlap. Its 67% "mismatches" at 22/66 are line-break artifacts, while the real four-line divergence at 4/56 never surfaces.
   - **forbidden lists are thin on near-synonyms** — *clever* is not on 明's, *depletion* is not on 殆's, *energy* is not on 氣's.

   **And a measurement for `glossary-self-check`, taken 2026-08-30.** Running every lock's `forbidden:` list over the prose docs — `method.md`, `overlay-audit.md`, `AGENTS.md`, `README.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md` — returns **66 hits, of which 65 are the document quoting a forbidden word in order to forbid it.** `overlay-audit.md`'s whole table is a list of words not to use; `AGENTS.md` has a Never column. **A naive scan of these files would be 98% noise**, which is exactly the design note already in `PLAN.md`: the rule must scan only an entry's *own* English — the `> *…*` gloss lines, `render:`, and the "Where it stands" table — and leave the argument around it alone. The one true finding was in `process/method.md`, which rendered 玄牝 (*xuán pìn*) as *"the mysterious female"* where 玄 is locked to **dark**; fixed the same day.
2. **`concordance.py --english` is the only instrument that looks in the reverse direction, and it should be run on every lock.** Pass A found two two-way violations no rule can reach: 固 at ch 55 and 壯 at ch 30 and 55 had borrowed 強's English **inside chapters that contain 強**, so the evidence gate that makes the checker trustworthy is exactly what blinds it.
3. **The false-friend `info` list is 70 items and is not being read.** Almost all are ordinary English. Consider suppressing the ones that recur book-wide so the list stays scannable.
4. **`tools/import_commentary.py` mis-splits chapters when a chapter heading sits mid-block.** Wang Bi's ch 18 currently carries ch 19's lemmas.
5. **`build.py` stays deferred** until the text stops moving.

---

## Chapter status, all 81

**Clean** *(no finding beyond the Tier 4 open calls)* — 5, 15, 18, 19, 20, 22, 30, 33, 38, 40, 42, 46, 52, 53, 55, 56, 59, 60, 61, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81

**Needs a swap** — 1, 2, 6, 7, 9, 12, 14, 17, 21, 23, 25, 27, 34, 37, 43, 44, 45, 47, 48, 49, 50, 51, 54, 57, 58, 63, 65

**Needs a chapter-level rewrite** — 3, 4, 8, 10, 11, 13, 16, 24, 26, 28, 29, 31, 32, 35, 36, 39, 41

*Chapters 5, 15, 18, 19, 20, 30, 33, 38, 42, 52, 55, 59, 68 moved up during Passes 0–B. Ch 38 retains two debts (Tier 1 §4); ch 15 retains 士 (Tier 2 §3); ch 30 retains 佐 (Tier 1 §18); ch 68 retains 配天 (Tier 1 §21) — they are listed clean only where this file says otherwise above.*

---

## The principles harvest — the inventory

*Swept 2026-09-10 with `process/skills/principle-entry`, three passes over ~11,400 lines of prose plus the 4,478-line glossary. **This is the inventory, not the entries** — each row becomes a file in [`process/principles/`](process/principles/README.md), written to the standard there. Rows leave this table as they ship.*

**What the three passes cost and returned.** Pass 1 (self-declared — *"standing principle"*, *"general rule"*) found **28 hits**. Pass 2 (principle-shaped bolded leads naming no chapter or character) found **~40 more**, most of them scoped to one document. **Pass 3 — the same reason given over and over and abstracted never — found the two largest rules in the project**, and neither is reachable by any keyword search: ***a rendering that renders no character*** (88 instances) and ***a rendering already spoken for by another character*** (47). Pass 3 is the one to run habitually.

**Status here means *harvested*, not *shipped*.** ⬜ inventoried · ✅ written as an entry.

### A · No home, high instance — write these first

| | | Proposed rule | Trigger fires when | Cases |
|---|---|---|---|---|
| H1 | ✅ | ~~**Every English word in the verse renders a character** — shipped `active`, 3 cases. `renders-no-character.md`~~ | you are about to put a word in the verse that renders nothing in the Chinese | **88** — ch 16 *energy*, ch 23 *intensity* · *we*, ch 10 ×3, ch 41 *the countless things*, ch 15 *danger from all sides* |
| H2 | ✅ | ~~**A rendering already spoken for by another character is not available** — shipped `active`, 3 cases. `already-spoken-for.md`~~ | a rendering you want is doing duty for a different character somewhere in the book | **47** — *nourish* (34, 51), *harm* (35, 56, 66), *inexhaustible* (6, 35), *precious* (70, 72, 75), *embrace* ×4. The operational half is `concordance.py --english` |
| H3 | ✅ | ~~**The English must not carry a verdict the Chinese does not** — shipped `active`, 3 cases. `no-verdict-the-chinese-lacks.md`~~ | your rendering approves or condemns and the character only describes | **26** — 貴/賤 as price not virtue, 善 as skilled, 惡 as *loathes*, 細 without *petty*, 辯 in the 大X若Y frame |
| H4 | ✅ | ~~**Where the commentators diverge, the English must not settle it** — shipped `active`, 3 cases. `divergence-stays-open.md`~~ | you are choosing an English that picks one commentator's reading over another's | **31** — 智者 (3), 信不足 (17/23), the subject at 4/56, 希 (23), 專 (10) |
| H5 | ✅ | ~~**Register is a claim — a line that would sit in a sermon has made one** — shipped `active`, 3 cases; absorbs §1 *Register*, the hymn test and `overlay-audit.md`. `imported-register.md`~~ | a rendering would sit comfortably in a sermon, or in 1971 | **55** — the KJV/Genesis/Pauline family, *Be Here Now*, devotional capitals |

### B · Already written, in the wrong place — migrate from `notes/translation.md` §1

*✅ **Closed 2026-09-10.** All three migrated, plus §1's *Register*, which H5 had already absorbed. **§1 went from 89 lines to 40**, and each migrated section keeps its heading as a redirect so existing links resolve. Four prose pointers repaired (`source/chinese.md`, ch 3, ch 12, ch 21) and two inside `notes/translation.md` itself. **What is left in §1 is exactly H30 and H32** — two term rulings that belong in `glossary/`, and the typography rule that already has an enforced home.*

| | | Proposed rule | Note |
|---|---|---|---|
| H6 | ✅ | ~~**The marks are ours; the music is the source's** — shipped `active`, 3 cases; `check: fix-linebreaks`. `lineation-is-ours.md`~~ | §1, and it is load-bearing for the CC0 claim (`PROVENANCE`) |
| H7 | ✅ | ~~**A commentator's gloss is an argument for a rendering, never a rendering** — shipped `active`, 3 cases; its divergence half went to `divergence-stays-open`. `commentary-is-not-a-rendering.md`~~ | §1 · the 河上公 *"here, now"* case |
| H8 | ✅ | ~~**A collocation carries a verdict its component words do not** — shipped `active`, 3 cases. `collocation-carries-a-verdict.md`~~ | §1 · ch 3. Distinct from H3: the *pairing* carries it, not the word |

### C · Born inside chapter notes and never migrated

*✅ **Closed 2026-09-10.** All seven shipped — six `active`, one `provisional`. **The set produced three boundaries the individual notes never had:** H11 is the named exemption to H1 (a supplied verb renders no character and is allowed, because English grammar requires it and the note declares it); H12 is H8 one level up (there the *idiom* adds a claim, here the *construal* does); and H15 splits into two rules that look identical and are not — distribution about the **English** concludes, distribution about the **Chinese** does not.*

| | | Proposed rule | Born at |
|---|---|---|---|
| H9 | ✅ | ~~**A rendering chosen for one chapter's legibility owes the connection to the notes**~~ — shipped `provisional` | ch 14 · T2-52 |
| H10 | ✅ | ~~**One Chinese modifier, one English modifier** — shipped **`provisional`**: the doublet-refusal half rests on one case. `one-modifier-one-modifier.md`~~ | 難得之貨 · T2-14 |
| H11 | ✅ | ~~**A supplied verb is scaffolding, not a character's English** — shipped `active`, 3 cases. The named exemption to `renders-no-character`. `supplied-verb-is-scaffolding.md`~~ | ch 8 · ch 61 · ch 66 |
| H12 | ✅ | ~~**A construal defensible in the Chinese that lands as a different claim in English has not been translated** — shipped `active`, 2 cases. `defensible-but-a-different-claim.md`~~ | ch 13 · ch 39 |
| H13 | ✅ | ~~**Correct an overlay by performing it, not by labelling it more accurately** — shipped `active`, 2 cases (ch 10 · ch 28). `perform-dont-label.md`~~ | ch 10 · 營魄 |
| H14 | ✅ | ~~**Name the referent — classical Chinese can leave one floating where English cannot** — shipped `active`, 2 cases; **carries the em-dash rule's real reason**. `name-the-referent.md`~~ | ch 22 · and the em-dash rule's real reason |
| H15 | ✅ | ~~**A distributional argument is a reason to look, not a reason to conclude** — shipped `active`, 3 cases, **with the boundary found**: distribution about the *English* concludes, about the *Chinese* does not. `distribution-locates.md`~~ | ch 4 · 象 |

### D · Tooling and process — scoped to one document, invisible to a translator

*✅ **Closed 2026-09-10, and the harvest is complete.** **12 written, 2 merged** — H25 was already the core of `already-spoken-for` and H29 was already both halves of `commentary-is-not-a-rendering`. The deduplication step in `principle-entry` caught both before a word was written, which is what it is for. **27 principles in force, 26 active, 1 provisional.** Three now carry a tool in `check:` — `check_locks` twice and `concordance --formulas` once — so the enforced few are visibly separated from the many that no rule can hold.*

| | | Proposed rule | Where it is stated now |
|---|---|---|---|
| H16 | ✅ | ~~**For the excavated witnesses, record the fact — never the text** — `active`. **The one rule a `shaloms-call` cannot set aside**: it is somebody else's copyright, not ours to suspend. `record-the-fact.md`~~ | **four places** — `ARCHITECTURE` 271, `PLAN` 196, `PROVENANCE` 45, `manuscript.md` 19 |
| H17 | ✅ | ~~**No rule fires on English alone** — `active`, `check: check_locks`. Carries why the two tools must not be merged. `evidence-gate.md`~~ | `ARCHITECTURE` 221 · `CLAUDE.md` |
| H18 | ✅ | ~~**Never delete a rule to silence it** — `active`, `check: check_locks`. The two escape hatches are deliberately asymmetric: an unused waiver is an error, an expired call is an error. `never-silence-a-rule.md`~~ | `ARCHITECTURE` 239 |
| H19 | ✅ | ~~**Make a generator deterministic before you gate it** — `active`. `deterministic-before-gated.md`~~ | `ARCHITECTURE` 147 |
| H20 | ✅ | ~~**Every file is edited or generated, never both** — `active`. Both failure modes documented: the stale hand-kept lock table, and two generated files disagreeing for seven months. `edited-or-generated.md`~~ | `ARCHITECTURE` 64 |
| H21 | ✅ | ~~**An importer that does not verify itself is decoration** — `active`. The 韓非 case: the files asserted an agreement nobody had tested. `importers-verify-themselves.md`~~ | `ARCHITECTURE` 149 · the 韓非 case |
| H22 | ✅ | ~~**Where the Chinese repeats itself, repeat yourself** — `active`, **`check: concordance --formulas`**. `repeat-yourself.md`~~ | `CLAUDE.md` · `DISCOVERIES` §6 · `check: formulas` |
| H23 | ✅ | ~~**Verify a flagged line against the Chinese in its own chapter before changing it** — `active`. `verify-the-flag.md`~~ | `CLAUDE.md` · the 2026-08-10 sweep's false positives |
| H24 | ✅ | ~~**Check the witnesses before drafting, not after** — `active`. A blank result means nobody has looked. `witnesses-before-drafting.md`~~ | `CLAUDE.md` · ch 21 · ch 25 |
| H25 | ✅ | ~~~~**A lock is a claim in both directions**~~ — **merged, not written.** Already the core of `already-spoken-for` (H2), which states it and names the reverse check. Deduplication step working~~ | `CLAUDE.md` · 固 · 壯 |
| H26 | ✅ | ~~**Intuition is last as an arbiter and first as a detector** — `active`. Never answer a feeling with a synonym. `intuition-detects.md`~~ | `CLAUDE.md` ★ · `method.md` 105–109 |
| H27 | ✅ | ~~**Universalize over the male-default — and name the seam** — `active`. Both halves load-bearing; each without the other fails. `universalize-and-name-the-seam.md`~~ | `CLAUDE.md` rule 2 · `reading.md` 62 |
| H28 | ✅ | ~~**One question at a time** *(`applies: process`)* — `active`. **Corollary: it constrains open decisions, not findings.** `one-question-at-a-time.md`~~ | `CLAUDE.md` · 2026-08-28 |
| H29 | ✅ | ~~~~**A commentator's gloss is not the text**~~ — **merged, not written.** Both halves already in `commentary-is-not-a-rendering` (H7). Deduplication step working~~ | `CLAUDE.md` · `manuscript.md` 536 |

### E · Findings, not principles — four things the sweep found in the wrong layer

*`CLAUDE.md`: "if you find them disagreeing, that is a finding: fix both and say which was wrong."*

*✅ **Closed 2026-09-10, and the sweep found a fifth.** Three documents described what `notes/translation.md` holds and they disagreed. **`WORKLIST.md` was right** — the ruling and its full argument go in `glossary/`, the decision goes in `notes/`. **`notes/translation.md` §2 was wrong**: it claimed *"the lock itself lives in `CLAUDE.md` and the glossary; the argument lives here"*, and it had exactly **one occupant in its whole life** — 無為 — which was a summary closing with *"Full reasoning: `glossary/wuwei-無為.md`."* **It described a layer that was never used.** §2 is dissolved, §1 is emptied, and both `CLAUDE.md`'s notes table and the file's own header now say what is true.*

| | | Finding |
|---|---|---|
| H30 | ✅ | ~~**Two term rulings were filed among rules that govern every chapter** — *The 天 family* (§1) and *無為* (§2). Both moved to `glossary/tian-天.md` · `tiandi-天地.md` · `wuwei-無為.md`, **which already carried more than the summaries did**; each closed by pointing there. Headings kept as redirects~~ |
| H31 | ✅ | ~~**`### 善 governs a verb`** moved to `glossary/shan-善.md`, which already carried it. **Its other half was the transferable one** and shipped as `supplied-verb-is-scaffolding` (H11)~~ |
| H32 | ✅ | ~~**The typography rule's third full copy is gone.** `CLAUDE.md` rule 5 is canonical and `check_locks.py` enforces it (`_DEVOTIONAL` carries `"Mother": "母"`); `CONTRIBUTING.md` restates it for outside contributors, which is a different audience. §1's 母 argument moved to `glossary/mu-母.md`; **the em-dash *case* stays** because it is the evidence for `name-the-referent`, and the rule went there~~ |
| H33 | ✅ | ~~**Recorded in `process/principles/README.md`** — standing rules 0–6 stay in `CLAUDE.md`. They are indexed, read every session, and partly enforced; this directory is for rules with **no** home, and a second copy is what killed the hand-kept lock table~~ |

---

## Closed — the ledger

*One line each. The reasoning lives where the pointer says; it is deliberately not repeated here.*

| Closed | What | Where the reasoning lives |
|---|---|---|
| 2026-08-10 | The first hand sweep, ~40 chapters, every lock then settled | `PLAN.md` → *What the building taught* |
| 2026-08-12 | Ch 27 無棄人 · Ch 48 closing stanza · Ch 31 吉事/凶事 · Ch 7 故能成其私 | `notes/translation.md` |
| 2026-08-12 | 無事 as a licensed split — *meddle* / *serve* | `glossary/shi-事.md` |
| 2026-08-14 | 善 → **masterful**, *good* only where the text names the category | `glossary/shan-善.md` |
| 2026-08-11 | Ch 21 *source code* · Ch 29 *sacred system* · Ch 40 用 · Ch 25 域 · Ch 14 無物 and 有 · Ch 2 *eternally* · Ch 23 *winds down* | `notes/translation.md` |
| 2026-08-26 | 恃 → *rely on*, freeing *presume* for 敢 — ch 2, 10, 51, 34 | `glossary/gan-敢.md` |
| 2026-08-26 | Ch 52 守柔曰強 → *the soft* | `glossary/ruo-弱.md` |
| 2026-08-27 | Ch 22's 不自X stanza rebuilt; 抱一 → *one thing* | `notes/translation.md` · Ch 22 · `glossary/yi-一.md` |
| 2026-08-28 | **Pass 0** — five text bugs (ch 5, 8, 39, 42, 59) | this file's git history |
| 2026-08-28 | **Pass A** — 強 → **strong**, completing the four-word table; 力 covered as *force* | `glossary/qiang-強.md` · `notes/translation.md` |
| 2026-08-28 | **Pass B** — 仁 → **humaneness**, 慈 → **tenderness**, 孝 → **devotion** | `glossary/ren-仁.md` · `glossary/ci-慈.md` |
| 2026-08-28 | **G1** — the ch 19 Guodian fork recorded as facts | `sources/variants.yaml` · `notes/manuscript.md` · Ch 19 |
| 2026-08-28 | **T3-1** — ch 24 rewritten as ch 22's mirror; 物 → *living things*; ch 31 swept | `chapters/024.md` · Notes · `notes/translation.md` |
| 2026-08-28 | **T2-15, four of six** — 是謂玄德 (10) · 故能成其大 (34) · 可以長久 (44, 59) · 猶難之 (63, 73) | `notes/translation.md` |
| 2026-08-30 | **T2-12** — 以此 → *"By this."* in all three; 2 stale notes corrected; 2 standing principles added | `notes/translation.md` · `notes/manuscript.md` · `DISCOVERIES.md` · Ch 21/54/57 |
| 2026-08-30 | **T2-13** — 故去彼取此 → ch 72's line in all three; `"gut"` locked onto 心; *embrace* freed from 取 | `notes/translation.md` · `glossary/xin-心.md` · Ch 12/38/72 |
| 2026-08-30 | **T2-14a** — 難得之貨 → *rare goods*; **貨 locked to *goods***, new entry; ch 44 swept off 富's *wealth* | `glossary/huo-貨.md` · `notes/translation.md` · Ch 3/12/44/64 |
| 2026-08-30 | **T2-14b** — 信不足焉 → *"Where trust runs short, there is no trust"* in both; ch 23's waiver removed | `notes/translation.md` · `glossary/xin-信.md` · Ch 17/23 |
| 2026-08-31 | **T2-14c** — 挫其銳…同其塵: ch 4 takes ch 56's nouns and couplets; *brilliance* breach closed; subject deferred to T1-2. **Closes the eleven named mirrors; PC stays 🔶 for T2-9/10/11** | `notes/translation.md` · Ch 4/56 |
| 2026-08-31 | **T5-8 · T5-9** — `check_worklist.py` (16 tests); atlas gated in CI; `build_graph.py` made deterministic | `tools/check_worklist.py` · `tools/build_graph.py` · `.github/workflows/checks.yml` |
| 2026-08-31 | **T2-11** — 殆 → **danger** ×5, one-to-one; ch 16's 没身 mistranslation; ch 25's 周行 restored; ch 15's invented danger removed | `notes/translation.md` · Ch 15/16/25/32/44/52 |
| 2026-08-31 | **T2-10** — 襲 → *covered* (27, 52); the 襲/習 fork found and recorded | `sources/variants.yaml` · `notes/manuscript.md` · `notes/translation.md` · Ch 27/52 |
| 2026-08-31 | **T2-9 → Pass C ✅** — 辯 → *argue* (45, 81), 訥 → *halting*; 巧 spun off as T2-20 | `notes/translation.md` · Ch 45/81 |
| 2026-08-31 | **T1-5** — ch 23's bare 德 off 玄德's word; the 道/德/失 triad restored | `chapters/023.md` |
| 2026-08-31 | **T1-2 → Pass D begins** — ch 4 rebuilt; **帝 locked**, new entry; 或/若 fork logged; T2-14c closed | `glossary/di-帝.md` · `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 4 |
| 2026-08-31 | **T1-3** — ch 3's closing movement rebuilt: 使 causatives restored, 治 at both ends, 為無為 unified with ch 63, 敢 and 常 applied. New standing principle: ***collocation carries a verdict***. 無為's forbidden list widened | `notes/translation.md` · `glossary/wuwei-無為.md` · Ch 3 |
| 2026-08-31 | **T2-2 (ch 3)** — 智者 → **the knowers**; *cunning* off the chapter; the 智者/知者 fork and the 民 restoration in the third clause both recorded | `sources/variants.yaml` · `notes/manuscript.md` · `notes/translation.md` · Ch 3 |
| 2026-08-31 | **T1-4** — ch 38 rebuilt: 失 restored as the chapter's spine, *clutches* (=執, absent) out, one English for 上 · 首/始 · 華/實, 以為 as the 2×2 grid, 大丈夫 → *the great person*. Opens **T4-7** (rank and gender) and T2-21 (厚) | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · `glossary/wuwei-無為.md` · Ch 38 |
| 2026-09-01 | **T1-7 · T1-15 · T1-16 · T3-5 · T2-15** — ch 28 de-abstracted: **rooster/hen** (forced by 牝/牡), 谷 → *valley*, 制 → *cutting* · 割 → *severs*, 守 → *hold to*, 常 restored ×3, the template unbroken; ch 22 unified on 為天下式 | `notes/translation.md` · `notes/manuscript.md` · Ch 22/28 |
| 2026-09-01 | **T1-1 · T2-22** — ch 10: 無知/無為 unswapped, 疵 restored, and **三 locked Englishes lifted off a chapter that has none of their characters** (全 · 萬物 · 鑑). *Dark mirror* survives on 說文's 从見、監. Two forks logged; ch 51 unified on 長而不宰 | `sources/variants.yaml` · `notes/manuscript.md` · `notes/translation.md` · Ch 10/51 |
| 2026-09-02 | **T2-8 · T3-2** — ch 8: **nine** 善, not eight, one of them deleted; all nine now *masterful*, seven couplets in one shape. 上善 → *the most masterful*; 幾 → *near*, not *one with the Tao*. **善 governs a verb, 18 of 18** — the parse decided by counting. Opens **T2-24** (淵) | `glossary/shan-善.md` · `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 8 |
| 2026-09-03 | **T2-25** — ch 23: 同 → *the same as*, not *merges with* ×6; 同 is 異's antonym and ch 1 had it right. 事's lock restored, *intensity* and *we* removed, 希言自然 made an equation again. Three forks logged, one meaning-bearing. Riders open at ch 4 and 56 | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 23 |
| 2026-09-02 | **Pass D restructured** — one row per chapter (D3…D64), so chapters check off one at a time; **`chapter-row` and `chapter-cover` added to `check_worklist.py`** so the chapter rows are derived rather than a second copy. PD's `Ch` now points at them. 7 tests, 102 total | `tools/check_worklist.py` · `tools/tests/test_check_worklist.py` · `WORKLIST.md` |
| 2026-09-05 | **Ch 35** — 不足 → *not enough*, un-splitting 王弼's single argument; 執 → *grasp* (the ch 29 mirror); 大象 → *the great image*; 口's first *mouth*. Two forks. Opens T1-22, T2-30/31/32, T5-10 | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 35 |
| 2026-09-05 | **`chapter-tally`** — the Progress line's figure, Done list and spelled-out repeat all gated against the per-chapter rows; the number-table filters prose out. 9 tests, 111 total | `tools/check_worklist.py` · `tools/tests/test_check_worklist.py` |
| 2026-09-05 | **Ch 11** — one frame three times, eleven lines for eleven; 無 → *in what is not there*, 當 → *right where*; **利 → *advantage*, a covered lock never applied anywhere**. 埏/挻 fork logged | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 11 |
| 2026-09-05 | **The formula finder** — `--formulas` now covers within *and* across chapters and finds frames; `--formulas N` prints a chapter's English beside them. Surfaces T3-4 and T3-6 on sight, plus a dozen unlogged. 13 tests, 124 total | `tools/concordance.py` · `tools/tests/test_concordance.py` · `CLAUDE.md` · `ARCHITECTURE.md` |
| 2026-09-05 | **Ch 36** — the four 將欲X之，必固Y之 restored as conditional instructions; **固 was an adverb rendered as the adjective *firm***, and 韓非's worked examples prove *first*. 利器 → *tools of advantage* (all three commentators); 淵 → *deep water*. Three forks, incl. 邦/國 dating our base to Han hands | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 36 |
| 2026-09-05 | **Ch 39** — the mirror was **inverted**, not merely broken; 得 → *received*; 貴/賤 → *prized/cheap*, price words; 為天下貞 rejoined its formula (T2-15); **故致數譽無譽 departs from the base for the cart**. *In the beginning* refused on the hymn test. Five forks. Opens T2-35/36/37, T5-13 | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 39 |
| 2026-09-06 | **Ch 15 reworked whole** — 蔽 read as *covered* (foliage), not 敝 *worn out*; the 盈/成 chain made legible; 此 anaphoric, so *"the Tao like this"*; 保 → *guard*; 不可識 and 夫唯 each unflattened; **靜/安 were swapped**; 將, 涉 and the 若 series restored. 識 → *read* over *named* (名 collides with ch 14's 不可名), *identified* and *known* (58 lines). 通 → *unobstructed*, on 說文's 達也 · 从辵. One fork logged (河上公's 久). **New Thread: the Tao is a road** — 道 = 辵 + 首, and ch 14 says you cannot see its 首. Opens T5-14, T2-38, T2-39 | `notes/translation.md` · `notes/manuscript.md` · `notes/reading.md` · `sources/variants.yaml` · `WORKLIST.md` · Ch 15 |
