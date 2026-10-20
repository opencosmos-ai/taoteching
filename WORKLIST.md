# WORKLIST — what the manuscript still owes

*The single forward-looking file: **only work that is still owed.** When a row closes it leaves this file, word for word, for [`WORKLIST-CLOSED.md`](WORKLIST-CLOSED.md), because the reasoning already lives somewhere permanent and repeating it here is how the old debt list grew to 343 lines and went stale. `tools/check_worklist.py` holds the line.*

**Where things live.** The **ruling and its full argument** go in `glossary/`. The **decision, thin**, goes in `notes/` — manuscript forks in `notes/manuscript.md`, our own rendering calls in `notes/translation.md`, reader-facing threads in `notes/reading.md`. **What is still owed** goes here. Nothing belongs in two of those.

**Policy: fix on discovery, not in a deferred batch.** Mechanical term-swaps are applied immediately. Lines needing a rewrite are proposed to Shalom first, then applied. Each chapter carries its own debt in frontmatter (`retrofit: [...]`).

## ▶ Start here — the next round (updated 2026-10-14)

*The pointer for whoever picks this up cold. It orders the work and names the first move; the reasoning lives in the rows it points to. Rewrite this block when the round changes, never append to it.*

**Next, in order:**

3. ~~**混 (T2-40)**~~ — ✅ 2026-10-19, with **清 (T2-59)** beside it (`glossary/hun-混.md`, `glossary/qing-清.md`). **Next:** down `glossary/TRIAGE.md` → *The relevance queue*, one entry at a time: 反/復/歸 (T2-44) · 名 · 氣 · 神/靈 (T2-37) · 靜 · 欲 · 智 (T2-2) · 始 · 希 · 貴/賤 (T2-36) · 和 · 谷 · 言 · 得 (T2-35) · 先.
4. **T2-62** — the smaller findings from the gloss pass, whenever a chapter they touch is open.

**Waiting on Shalom:** nothing. Still deferred: 正/奇 (T4-2) and the em-dashes (T4-3).

**How the work goes:** branch from a fresh `main` with an **ASCII** branch name (a non-ASCII one draws GitHub's hidden-character warning, and renaming it closes the PR). Run the tests, `check_locks.py`, and the full rebuild — `build_db` → `export` → `build_graph` → `export_atlas` — before every PR. The atlas rebuilds within a minute or two of a merge (`notify-atlas.yml` dispatches; an hourly rebuild is the fallback).

---

## The list

**⬜ open · 🔶 part done · ✅ done · ⏸ deferred by Shalom.** Detail for every row is below, under the matching heading. **55 item rows: 49 open · 0 done · 4 part done · 2 deferred.** *(Counted from the table itself — a hand-kept tally drifts. It read "43 open · 18 done" and matched nothing.)*

| # | | Item | Ch | Pass |
|---|---|---|---|---|
| | | **Passes** | | |
| PE | 🔶 | Entries and sweeps — ~~**守 執 保 持**~~ (T2-19 ★, closed 2026-09-08) · ~~**身**~~ (T2-1 ★, closed 2026-09-20) · 氣 靜 君 智 事 志 谷 恃 | book-wide | E |
| PF | 🔶 | The deferred calls | ~~民/人~~ (T4-1, 2026-10-14) · 正/奇 · em-dashes | F |
| PG | ⬜ | `build.py` | — | G |
| | | **Tier 1 · Wrong, not merely inconsistent** | | |
| T1-22 | ⬜ | Ch 48 — 取天下 → *"the world comes to you"*; 取 (*qǔ* — to take) is active and the English makes it a passive arrival. *Found by the ch 35 reverse check* | 48 | E |
| T1-18 | ⬜ | 佐 → *"One who rules"* — follows 河上公 against the grammar, unlogged | 30 | E |
| T1-21 | ⬜ | 配天 — the chapter and its own note disagree; the contested 天 line | 68 | F |
| | | **Tier 2 · One character, many Englishes** | | |
| T2-2 | 🔶 | **智** four ways; **ch 3 settled as *the knowers*, fork logged**; *"cunning"* still wears 巧 at 19 and 57. **聖's entry rules *wise*/*wisdom* out for 聖 and cannot enforce it until 智 is settled** (shared ch 3 19 27); Guodian's 五行 pairs them as knowing by seeing (智) and by hearing (聖) | 3 18 19 33 65 | E |
| T2-4 | 🔶 | **氣** — ch 10 → *breath* (河上公 呼吸精氣); *vital breath* (42) and *vital energy* (55) still split | 10 42 55 | E |
| T2-21 | ⬜ | **厚** four ways — *thick* (38) · *heavy* (44) · *abundant* (55) · *rich* (75) | 38 44 50 55 75 | E |
| T2-7 | ⬜ | **志** — *ambition* (3) / *will* (33) | 3 33 | E |
| T2-16 | ⬜ | **事** wants an entry; 無事's licensed split needs confirming | 48 57 63 | E |
| T2-17 | ⬜ | **私** two ways, sheltering under 公's `covers:` | 7 19 | E |
| T2-20 | ⬜ | **巧** — *skill* (45) vs *cunning* (19, 57); the same fault as 辯, one line above it | 19 45 57 | E |
| | | **Tier 3 · Missed parallelisms** | | |
| R3 | ⬜ | ★ **Read the ten recovered 王弼 chapters against decisions made without him** — 8, 14, 15, 19, 30, 54, 62, 70, 71, 78 (T5-6). Every one was drafted, and several reworked, with one commentary where there were two. **The lemma forks are logged** (ch 8 正 (*zhèng* — straight), ch 15 久 (*jiǔ* — long), ch 54 國 (*guó* — state), ch 78 是為 (*shì wéi* — "this is")); **the comments have not been read.** One already bears on a settled line: **ch 15 prints 若容 (*ruò róng* — like a bearing) for our 若客 (*ruò kè* — like a guest)**, base kept provisionally. One confirms a call made blind: his 蔽覆盖也 (*bì fù gài yě* — "蔽 means covered") is ch 15's 2026-09-06 reading of 蔽 exactly. Ch 62 was already drafted with him (under 061) | 8 14 15 19 30 54 62 70 71 78 | E |
| R2 | ⬜ | **義 (yì) wants a glossary entry** — reads *duty* in all 5 lines, unlocked, and the atlas therefore publishes *righteousness* | 18 19 38 | E |
| | | **Tier 4 · Deferred by Shalom** | | |
| T2-39 | 🔶 | ~~**名 → *description* at ch 25**~~ — *found done 2026-09-24:* ch 25 now reads *"Forcing a name on it, I call it great."* **What is left is the frame**, and a new wrinkle in it: the line above, 字之曰道 (*zì zhī yuē dào* — "I style it Tao"), now reads *"Forcing a label on it"*, and **強 (*qiáng* — to force) is not in that line.** Original finding: **名 → *description* at ch 25** (強為之名曰大). 名 (*míng* — name) is the book's own heavily-worked word for *name*, 21 lines across 9 chapters, and ch 1 is built on it. **強為之▢ is also a shared frame with ch 15** (強為之容), where our English reads *"I force a likeness"* | 15 25 | E |
| T2-41 | ⬜ | **沖 reads *blending* at ch 42** (沖氣以為和) where ch 4's Pass D work settled it as **empty** (道沖). Found by the reverse search when *blend* was freed from 混 | 4 42 | E |
| T2-44 | ⬜ | **The return family — 反 · 復 · 歸 all read *return*, across 21 English lines.** 說文 keeps them distinct: 反 覆也 (overturn, on 又 a hand), 復 往來也 (going and coming, on 彳 the step radical), 歸 女嫁也 (a woman marrying in — going where one belongs). 反 → *returning* is fixed at 25 and 40; the other two are open | 14 16 25 28 34 40 52 59 65 | E |
| T2-45 | ⬜ | **廣 two Englishes** — *boundless* at 41 (廣德若不足, settled 2026-09-07) and *reach far* at 67 (儀故能廣). 說文: 殿之大屋也, a great hall, on the roof radical 广. *Vast* is free now that 大 is locked | 41 67 | E |
| T2-47 | ⬜ | **Ch 68's 善▢者 frame now has a seam.** 善為士者 is verbatim at 15 and 68, so its first line reads *"Those masterful in service are not martial"* — while its other three run *"The master fighter," "The master of overcoming enemies," "The master of using people."* Four instances of one frame, two shapes. Opened by T2-3 | 68 | E |
| T2-48 | ⬜ | **`glossary/da-大.md` owes an adverbial flexion.** 大笑之 (41) reads *laugh **aloud***, which the entry's licensed list (*large · greater · master*) does not cover. Also unresolved there: whether the 大▢若▢ frame wants a superlative — ch 41's 大白 now takes one as a recorded exception, and 41 and 45 must be decided together. **The mechanism now exists** — `flexions:` (2026-09-20) | 41 45 + glossary | E |
| T2-49 | ⬜ | **兵 two Englishes** — *weapons* at 31, 50, 57, 69, 80 and *military force* at ch 30 (以兵強天下). *Arms* is unavailable: that is 臂, the body's arms, at 38, 42 and 64 | 30 31 50 57 69 76 80 | E |
| T2-50 | ⬜ | **Two characters now share the "carv-" root** — 制 (28, 32) and 斫 (*zhuó* — to hew) at ch 74, 代大匠斫 → *"those who carve in place of the master carpenter."* They never share a chapter, so no check fires; but 斫 is axe-work where 制 is a fitted cut | 28 32 74 | E |
| T2-53 | ⬜ | ★ **The calamity family — five characters, and *disaster* is worn by two of them.** 禍 (*huò*, 說文 害也，神不福也) → *disaster* at 46, 58 ×2, 69 · **凶** (*xiōng*) → *disaster* at 16, 30 and *ill* at 31 · 咎 (*jiù*, 說文 **災也**; 人 + 各, 相違也 *at odds*) → *fault* at 46 and 9 · 殃 (*yāng*, 說文 **咎也**) → *calamity* at 52 · 患 (*huàn*, 說文 憂也) → *trouble*, locked at 13. **The 守/保/衛 *guard* pattern again**, and unlike 身/神 **a rule could catch this one**: 咎 and 禍 share ch 46, in a parallel couplet that is only legible because they differ. Wants one entry | 13 16 30 31 46 52 58 69 | E |
| T2-58 | ⬜ | **Ch 2 — 高下相盈 → *"High and low depend on each other"*, which renders neither graph.** Our base's 盈 (*yíng* — to fill) is the Mawangdui reading; every transmitted text we carry prints 傾 (*qīng* — to lean), usually explained as the Han taboo on 劉盈 (*Liú Yíng*)'s name. *Depend on* is neither *fill* nor *lean*. Its neighbour 相形 (*xiāng xíng* — give each other shape) reads *measure*, closer to 王弼's own 較 (*jiào* — compare) than to the 形 we print. Found writing T1-20's ch 2 entry | 2 | E |
| T2-57 | ⬜ | **居 (*jū* — to dwell) reads four ways and is unrendered twice** — *settling* (8) · *stay* (2 ×2) · *at home* (31) · *homes* (72) · **nothing at 38**, where 不居其薄 and 不居其華 are folded into 處's verb, losing a four-part parallel. Ch 25 and 80 unchecked. **Ch 8's *settling* is right and should stand**: 處 (*chǔ*) holds *dwell* four lines above at 處眾人之所惡, and 說文 separates them — 居 **蹲也** (*to squat*, on 尸 a seated body) against 處 **止也。得几而止** (*to stop, having got a stool*). Found by Shalom asking why ch 8 does not read *In dwelling* | 2 8 25 31 38 72 80 | E |
| T2-62 | ⬜ | **Smaller findings from the word-gloss pass**, each needing a look, none urgent. **伐** (*fá*) is *claim the work* at 22, 24 but *bragging* at 30 · **惚恍** shares one word (*the elusive*) at 14 where 21 splits it (*elusive / vague*) · **少 / 寡** both *diminish* in one line at 19 · **必固** reads *must first* ×4 at 36 (固 as 姑 *for now*; the literal has *firmly*) · **為天下正 / 為天下貞** take two shapes at 45 and 39 · **其次** (*the next*) turned into *Good / Poor / The worst leaders* at 17 · **夸** at 53 and **晚** at 41 follow variants (recorded; the glosses describe the base graph) · **ch 39 source table** lacks punctuation after 將恐裂 and 故貴以賤為本 · ~~**脆** two Englishes, *tender* 慈's~~ → *fragile* at 64 and 76, 2026-10-15 · **筋** (*jīn* — 說文 肉之力也, *the strength of the flesh*; sinew) reads *muscles* at 55 · characters absorbed by paraphrase: 容 (21, 50), 發 (12), 立 (25), 甚 (53), 詰 (14), 至 (65, 80), 拱 (62), 含 (55) · **ch 17's *only* renders no character**: 太上，下知有之 (*tài shàng, xià zhī yǒu zhī* — "the highest: those below know they exist") reads *"know only that they exist"*, and nothing in the line says *only*; found by T2-43's reverse check | 12 14 17 19 21 25 36 39 41 45 50 53 55 62 64 65 76 80 | E |
| T2-63 | ⬜ | **渾 (*hún*) at ch 49 reads *muddy*, which is 濁's English.** 為天下渾其心 → *"they let their heart go muddy."* 渾 is 混's own word: 說文 渾，混流聲也, and 河上公's text prints 渾 for 混 at ch 15. The chime with ch 15 the line wants is real, but in the Chinese it runs through 混 (*mixed*), not 濁. A line rewrite, so Shalom's call; then 渾 can go into `hun-混.md`'s `covers:` | 15 49 | E |
| T4-2 | ⏸ | **正 / 奇** — five Englishes | 37 45 57 58 78 | F |
| T4-3 | ⏸ | **Em-dashes in the verse** — 14 lines *(ch 28's two and ch 15's one went with their rewrites, not by decision)* | 10 14 29 43 44 51 53 55 58 | F |
| T2-23 | ⬜ | **明白 / 白** — 白 is *the white* at ch 28 and inside the compound *clarity* at ch 10; check 明白 is bound | 10 28 41 | E |
| T2-24 | 🔶 | **淵** — ch 36 → **deep water** (說文 回水也…左右，岸也: circling water, banks left and right). *fathomless* (4) still open; ch 8's *depth* is gone — 心善淵 now reads *"In the heart, masterful at staying deep"* (seen 2026-09-24) — so what is left is whether 4 and 8 join 36; *pool* rejected as chlorinated, *the depths* fails the pointing test | 4 8 | E |
| T2-30 | ⬜ | **夷** three ways — *the invisible* (14) · *smooth* (41) · *level* (53). 說文 平也. *Found by the ch 35 reverse check: *level* was about to be taken for 平.* **Ch 14's half settled at T2-52 (2026-09-10) — its *the invisible* stands and the link is carried in notes. What is open is 41 vs 53** | 14 41 53 | E |
| T1-23 | ⬜ | **Ch 69 deletes 主/客.** 吾不敢為主，而為客 → *"move first / move second"* — 河上公's gloss (主，先也) rendered instead of the text. 說文 makes them pointable: 主 is *the flame in the lamp*, 客 *one lodged under another's roof* | 69 | E |
| T2-31 | ⬜ | **客** survives once in the English (ch 15). Restored at 35 as *a passing guest*; **ch 69 still owes it** · T1-23 | 15 35 69 | E |
| T2-32 | ⬜ | **口** → *palate* at ch 12, picking eating over speech. 口 occurs twice; ch 35 now reads *mouth*, which does both | 12 35 | E |
| T2-27 | ⬜ | **同謂之玄 → *Together*** — 同's fourth English, and *together* can read as *jointly they form one thing* rather than *both alike are so called* | 1 | E |
| T2-28 | ⬜ | **復歸 split four-to-three** — the seven-line compound reads *return again* at 16 and 28 ×3, plain *return* at 14 and 52 | 14 16 28 52 | E |
| T2-29 | ⬜ | **命 / 令 collapse into *command*** in the identical 莫之X而 frame — 令 at ch 32, 命 at ch 51. **令 is owed its own entry**: 8 lines, 3 Englishes (*makes* 12 · *command* 32 · *laws* 57) | 12 19 32 51 57 | E |
| T4-7 | ⬜ | ★ **Rank and gender — 大丈夫 · 君子 · 士.** Male rank-words dissolved in two opposite directions. Kin to T4-1. **聖人 is not a rank and its entry leaves *is the sage a ruler?* open; both silks read 君子 at ch 26** (`glossary/sheng-聖.md`) | 15 26 31 38 41 68 | F |
| T2-33 | ⬜ | **利** wants an entry — 9 chapters, three jobs: *benefit* (bound to 害 at 56, 73, 81) · **sharp** (利器 36, 57; 利劍 53 — the 說文 sense, 銛也。从刀) · *advantage* (11, 19) | 8 11 19 36 53 56 57 73 81 | E |
| T2-34 | ⬜ | **微** three ways — *the intangible* (14) · *subtle* (15, 64) · *hidden* (36). 說文 隱行也, "to go concealed". **Ch 14's half settled at T2-52 (2026-09-10) — its *the intangible* stands and the link is carried in notes. What is open is 36 vs 15/64** | 14 15 36 64 | E |
| T2-35 | ⬜ | **得** wants an entry — 19 chapters, 30 lines, no entry; *obtain* · *get* · *gain* · *gets*, plus the 不得已 idiom at 29, 30, 31. Ch 39 uses **received** and does not settle it | book-wide | E |
| T2-36 | ⬜ | **貴 / 賤** want an entry — 貴 is 15 chapters, 22 lines (*prize* · *value* · *high status* · *honour*). 說文 makes both **price** words: 物不賤也 · 賈少也 | book-wide | E |
| T2-37 | ⬜ | ★ **神 and 靈 want one entry together** — both on the overlay watchlist, neither has an entry. 神 → *spirit* (6, 39, 60) · *sacred* (29); 靈 → *numinous* (39), which **fails the pointing test** and had no surviving alternative | 6 29 39 60 | E |
| T4-5 | ⬜ | Glossary harvest — 一 名 希, plus ten new candidates | — | E |
| T4-6 | ⬜ | Guodian **G2–G6** | 5 16 17 18 25 + 26 more | E |
| T4-8 | ⬜ | 說文 (c. 100 CE) quotes the four-greats line as 人亦大 — six centuries before our oldest 人 witness | 25 | E |
| | | **Tier 5 · The harness** | | |
| T5-12 | ⬜ | `check_locks.py`'s `repeated-formula` still only compares **across** chapters. Whether the gate can carry the within-chapter case without crying wolf is unsettled — 152 findings at recall. Decide after Pass D, on the evidence `--formulas` is now producing | — | G |
| T5-14 | ⬜ | **Invented repetition — the mirror of `DISCOVERIES.md` §6, and nothing looks for it.** `--formulas` finds a *flattened* repeat (Chinese repeats, English varies). It cannot find an *invented* one (English repeats, Chinese does not), which asserts a link the text never makes. Found by ear at ch 15, where *"could not be made out"* chimed with *"newly made"* across 識 and 新成 — unrelated characters. Needs an English-side n-gram index checked back against the Chinese | 15 + unswept | G |
| T5-3 | ⬜ | Forbidden lists thin on near-synonyms — ~~*clever*~~ *(settled by T1-17: now 明's ch 65 flexion, so it cannot also be forbidden)*, *depletion*, *energy*. *(無為 gained *effortless* / *without effort* / *takes no action* with T1-3 and T1-4; these three stand)* | — | E |
| T5-4 | ⬜ | Run `--english` on every lock; it is the only reverse-direction check | — | ongoing |
| T5-5 | ⬜ | The 70-item false-friend `info` list is not being read | — | G |
| T5-7 | ⬜ | `build.py` — deferred until the text stops moving | — | G |
| T5-17 | ⬜ | **`import_commentary.py` drops every 韓非子 quotation under five characters** (`if len(fq) < 5: continue`), and a passage whose quotations are all short is lost entirely. 49 short quotations across 解老 and 喻老. Lost outright: ch 52's 見小曰明 and 守柔曰強 (no `hanfeizi/052.md` exists), and **ch 47's 不見而明**, a witness for 明 on the fork reversed to 名 on 2026-09-24 (`notes/manuscript.md`). Also 去彼取此 and 朝甚除. A four-character quotation can be placed by exact match against the base text, where five-grams cannot. Found 2026-10-15 | 47 52 53 | G |
| T5-18 | ⬜ | **The atlas's "Built from" shows 說文's analysis even where an entry argues against it.** 聖's card says 呈 is *sound only*; `glossary/sheng-聖.md` argues 呈 is a later misreading of the bronze form's 口 over 𡈼 (鄭張尚芳: 非呈聲). The parts come from `import_shuowen.py`, so an entry has no way to annotate them. Decide whether it should, or whether the card should say the analysis is 說文's | 19 | G |
| T5-20 | ⬜ | **`--english` cannot see a `covers:` character.** `build_index.py` writes `covers:` into `terms.yaml` as a comment, so the Term model never learns of it, and ch 21's two 惟 lines report *"no 唯 in this chapter"* under `--english "only"`. Every covered character has the same blind spot (剛 under 柔, 腹 under 心). Emit `covers:` as data and let `licenses()` count it | 21 | G |
| T5-21 | ⬜ | **The 河上公 importer files two ch 15 lemmas as comment lines**: 敦兮其若朴 and 渾兮其若濁 print as `> ` text, not `**…**` lemmas. So `unmarked-lemma` never sees 渾, which differs from our 混, and `--commentary 15` shows each under the wrong heading. 渾/混 is recorded by hand in `variants.yaml`. Find why these two were not split, then check the other 80 chapters for the same pattern | 15 | G |

---

## Tier 1 · Wrong, not merely inconsistent

Meaning changed. Each needs a decision; most need one line rewritten.

### Unlogged departures — defensible, but nothing records them

18. **Ch 30 — 佐 → *"One who rules."*** 佐 is *to assist*; the chapter addresses a ruler's **adviser**. 河上公 rescues it reflexively — 謂人主能以道自輔佐也 — but we follow a commentary against the plain grammar without saying so.
21. **Ch 68 — 配天 — the chapter and its own note disagree.** Reads *"partnered with the sky"*; 天 stands alone with no 地 near, which the lock sends to *nature / the natural*. **The single contested line for the 天 split.**

---

## Tier 2 · One character, many Englishes

2. 🔶 *Part done — T2-2; the row says what is left.* **智 rendered four ways, and *"cunning"* covers four characters.** *cunning* (3), *cleverness* (18, 19), *intelligent* (33), *guile* (65). Some spread is legitimate — 智 runs from *wisdom* at 33 through *cleverness* at 19 to *artifice* at 65, a licensed split like 事. What is not legitimate is that it happened by accident. **And *cunning* also did duty for 知 (ch 3, adjacent line), 巧 (ch 57), and a fourth at ch 58.** **Ch 3 is closed (2026-08-31, with T1-3):** 無知 → *unknowing*, 智者 → **the knowers**, and *cunning* is off the chapter. The word was chosen because **the commentators diverge on who the 智者 are** — 王弼 prints 智者 and glosses 智者謂知為也 (*"those who know how to handle"*), 河上公 prints 知者 with the phonetic note 知音智 and glosses 思慮深不輕言, almost verbatim what he says of the *approving* 知者 at ch 56 — so any English specific enough to settle it picks a side. Fork now in `sources/variants.yaml` and `notes/manuscript.md`. **The book-wide split stands** at 18, 19, 33, 65. **Take 智 with 知, 巧, and the locked 明** — those four are the book's whole epistemology and three are unlocked.
4. 🔶 *Part done — T2-4; the row says what is left.* **氣 has three Englishes:** *life energy* (10), *vital breath* (42), *vital energy* (55).
7. **志 (*zhì*) reads *striving* (3) and *will* (33).** Small, real, no entry.
16. **事 wants an entry, and 無事's licensed split needs confirming.** *meddle* at 48 and 57, *serve the not-serving* at 63. `glossary/shi-事.md` recommends making ch 63's word the standard on the strength of ch 57's quartet. Not applied.
17. **私 reads two ways** — *private self* (7) and *the self* (19) — sheltering under 公's `covers:`. Ch 19's is arguably right in place, but 私 may want its own entry rather than a `covers:` line.

---

## Tier 3 · Missed parallelisms

Structure the Chinese has and the English does not. These are rewrites, and they are where the poetry is.

8. **Ch 33 — 力/強** — closed by Pass A, but the chapter's remaining couplets are worth a look when 智 is settled.

---

## Tier 4 · Open calls, deferred by Shalom

- **★ Rank and gender — 大丈夫 · 君子 · 士. T4-7, opened 2026-08-31 with ch 38.** This book has a family of **male rank-words**, and the manuscript has been dissolving them silently **in two opposite directions**. 大丈夫 (*dà zhàng fū*, ch 38, a hapax) was turned into a **modern psychological type** — *"the mature person"*, now *the great person*. 君子 (*jūn zǐ* — literally *a ruler's son*, the Confucian gentleman, ch 26 and 31) is rendered **"the sage"**, which hands the opposition's honorific to Laozi's own figure, whose name is a different word entirely (聖人). 士 (*shì* — a male service rank: knight, officer, retainer, ch 15, 41, 68) reads three ways, twice on the identical phrase 善為士者. **The shared question is what to do with *rank*, and it is not the one-character-many-Englishes question that T2-3 and T2-6 currently file it under** — a rank word universalised loses the rank, which is often what the line is about. 說文 makes the stakes concrete for 夫: 一以象簪也…人長八尺，故曰丈夫 — *"the single stroke depicts a hairpin… a person stands eight 尺 tall, therefore we say 丈夫"* — a measurement and a capping ceremony, not an inner state. Standing rule 2's carve-out is for the **incidental** male-default; these are not incidental. **Owed:** one decision across all three, the seam noted wherever it is universalised, and a check on whether 君子 can keep *"the sage"* at all. **Kin to T4-1 (民/人) and to T2-1 (身) — the same question about social categories.** Cross-refs: T2-3, T2-6.
- **正 / 奇** — five Englishes across ch 37, 45, 57, 58, 78. Owed: `glossary/zheng-正.md`.
- **Em-dashes in the verse** — 17 lines across ch 10, 14, 15, 28, 29, 43, 44, 51, 53, 55, 58. Ch 44's three are good. Ch 10 and ch 51 share the same en-dash on the same line (長而不宰) and move together.
- **Glossary harvest** from `TRIAGE.md`: 一 is owed only its entry, then 名, then 希. **This sweep adds 身, 氣, 靜, 君, 士, 智, 事, 志, 谷, 恃.**
- **Guodian G2–G6** (`PLAN.md`). G1 closed 2026-08-28.

---

## Tier 5 · The harness

1. **Two proposed rules remain unbuilt** — `incomplete-draft` and `glossary-self-check` (`PLAN.md`). **Neither would have caught most of what the 2026-08-28 sweep found.** What would:
   - **forbidden lists are thin on near-synonyms** — *clever* is not on 明's, *depletion* is not on 殆's, *energy* is not on 氣's.

   **And a measurement for `glossary-self-check`, taken 2026-08-30.** Running every lock's `forbidden:` list over the prose docs — `method.md`, `overlay-audit.md`, `AGENTS.md`, `README.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md` — returns **66 hits, of which 65 are the document quoting a forbidden word in order to forbid it.** `overlay-audit.md`'s whole table is a list of words not to use; `AGENTS.md` has a Never column. **A naive scan of these files would be 98% noise**, which is exactly the design note already in `PLAN.md`: the rule must scan only an entry's *own* English — the `> *…*` gloss lines, `render:`, and the "Where it stands" table — and leave the argument around it alone. The one true finding was in `process/method.md`, which rendered 玄牝 (*xuán pìn*) as *"the mysterious female"* where 玄 is locked to **dark**; fixed the same day.
2. **`concordance.py --english` is the only instrument that looks in the reverse direction, and it should be run on every lock.** Pass A found two two-way violations no rule can reach: 固 at ch 55 and 壯 at ch 30 and 55 had borrowed 強's English **inside chapters that contain 強**, so the evidence gate that makes the checker trustworthy is exactly what blinds it.
3. **The false-friend `info` list is 70 items and is not being read.** Almost all are ordinary English. Consider suppressing the ones that recur book-wide so the list stays scannable.
5. **`build.py` stays deferred** until the text stops moving.
