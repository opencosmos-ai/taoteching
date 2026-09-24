---
id: no-verdict-the-chinese-lacks
title: "The English must not carry a verdict the Chinese does not"
status: active
since: 2026-09-10
trigger: "your rendering approves or condemns, and the character only describes"
applies: [drafting, glossary]
evidence: ["notes/translation.md#貴-and-賤-are-price-words-not-moral-ones", "notes/translation.md#ch-79-善-twice-in-one-chapter-and-the-moral-falls-out", "notes/translation.md#ch-67-似不肖-look-like-nothing-and-細-petty"]
check: none
supersedes: []
---

# The English must not carry a verdict the Chinese does not

**The rule.** Where the Chinese describes, the English describes. A character that names a **position, a price, a skill or a state** must not be rendered by a word that also **passes judgment on it** — because the judgment is then the text's, and the text did not make it.

**When it fires.** When the obvious English for a descriptive character happens to be a word English uses to praise or condemn. That is most of them: English moralised its vocabulary early and thoroughly, and the plainest word is often the loaded one.

---

## Why this holds

**This book's argument depends on the distinction, and moralised English inverts it.** The Tao Te Ching repeatedly takes a word its culture used as praise and **declines to praise with it**. 強 (*qiáng* — strong) is the disease at ch 76 and the cure at ch 52. 辯 (*biàn* — to argue) sits in the 大X若Y (*dà X ruò Y*) frame at ch 45 and is condemned at ch 81 — and **the frame does not endorse its X**, as 巧 (*qiǎo* — skill) proves one line above. An English that has already decided whether a word is good removes the book's ability to change its mind.

**The failure mode is invisible because it feels like accuracy.** *Precious* for 貴 (*guì*) is not wrong; it is *narrow*. 貴 sits on 貝 (*bèi*), a cowrie shell — it means **costly** before it means **honoured**, and ch 72's whole force is that the two are separable: you can love a thing without pricing it. The moralised English quietly forecloses the line's argument while translating every character in it.

**A verdict also destroys parallelism the Chinese keeps.** When 貴 and 賤 (*jiàn* — cheap) are rendered *noble* and *base*, ch 39's pair stops being a scale and becomes a hierarchy of worth — and the chapter's claim, that the high is rooted in the low, turns into a moral paradox instead of a plain observation about prices.

**And it is the overlay problem in miniature.** The English Tao Te Ching was largely built by missionaries, and a moral vocabulary was the water they swam in. 善 as *good* rather than *skilled*, 罪 (*zuì* — crime) as *sin*, 義 (*yì* — duty) as *righteousness* — each is a verdict imported where a description stood.

---

## Why this principle exists

**貴 and 賤 are price words, not moral ones.** Both sit in the commercial register; ch 39's 貴以賤為本 is about what a thing costs and what it rests on. Rendered *prized* and *cheap*, the mirror holds. → [貴 and 賤](../../notes/translation.md#貴-and-賤-are-price-words-not-moral-ones)

**Ch 79 — 善 (*shàn*) twice in one chapter, and the moral falls out.** 安可以為善 is not *"how can that be good"* but a question about **mastery**; 天道無親，常與善人 keeps the same word. Once 善 is *masterful* throughout, the chapter stops rewarding virtue and starts describing competence. → [ch 79](../../notes/translation.md#ch-79-善-twice-in-one-chapter-and-the-moral-falls-out)

**Ch 67 — 細 (*xì*) read *petty*.** 細 is *slight*, a matter of scale; *petty* adds contempt the character does not carry, and it collided with ch 63, where the same word is plainly small-not-contemptible. → [ch 67](../../notes/translation.md#ch-67-似不肖-look-like-nothing-and-細-petty)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`chapter-review` step 5**, *Before you offer a line* | *ask what the line implies about the people in it* |
| **`glossary-entry` §2** | *What is set aside* — where a rejected verdict is named, with its reason |
| **`chapter-review` step 0** | `build_principles.py --applies drafting` lists it before a chapter is drafted |
| **`glossary-entry` §1** | `--applies glossary` lists it before an entry is written |

**Not enforced.** A verdict lives in valence, which no rule keyed to a word can read.

---

## Where it does not fire

**Some characters genuinely carry a verdict and must keep it.** 咎 (*jiù* — blame), 罪 (*zuì* — crime) and 禍 (*huò* — disaster) are not neutral, and neutralising them is the same error running the other way. The test is the character, not a preference for flatness.

**And the book does sometimes condemn.** 盜夸 (*dào kuā* — "robber's swagger") at ch 53 is contemptuous in the Chinese. Render it so.

**A verdict in the *commentary* is not a verdict in the text.** 河上公 (*Héshàng Gōng*) moralises freely; that is evidence about how a Han reader took the line, not a licence to import his register.

**Nor does this license blandness.** Removing a verdict the Chinese lacks is not the same as removing force. *Loathes* for 惡 (*wù*) is strong and correct; *evil* would be the verdict.

---

## What it obliges

1. **Ask what register the graph sits in** — commercial, military, agricultural, bodily — and stay in it. 貴 on 貝 is money; 執 (*zhí*) with its manacles is law.
2. **Check the character's other chapters before accepting a valenced English.** A verdict that fits here almost always breaks somewhere the same character is used the other way.
3. **When a character carries both valences, the English must too.** Do not resolve 強 or 執; that is the text's tension, not a defect in it.
4. **Put the rejected verdict in the glossary entry with its reason** — *"petty adds contempt 細 does not carry"* — so the next drafter meets the argument rather than the word.
