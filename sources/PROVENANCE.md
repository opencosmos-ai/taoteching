# PROVENANCE — what may live in `sources/`, and on what authority

*This directory holds primary material consulted during translation. Every file in it must be **provably free**, because this repository is dedicated CC0 with no exceptions, and because the companion volume in `../taocompanion` is intended to be **sold**.*

**Read the admission rules before adding anything.** They are stricter than copyright law requires, deliberately.

---

## A correction, 2026-08-11

**This file previously said Chinese Wikisource could not be used, because its content is CC BY-SA 4.0. That was wrong**, and the error was over-caution: it read the site-wide licence banner instead of the copyright policy.

Wikisource's policy says the opposite, in terms:

> *"the transcription of a work on Wikisource does not create a new copyright, so if the original work has entered the public domain the transcription here is also public domain"* … *"anything that could attract copyright would no longer be faithful to the original, and because of that, the CC BY-SA default license for contributions never comes into play for mainspace content."*

That is Wikisource's own account of its own licence, and it matches the law it is reasoning from (*Feist* 1991; *Bridgeman v. Corel* 1999). **The blocker described here for three weeks did not exist.** The caution was cheap and the correction is cheaper; recorded rather than quietly edited away, because a provenance file that hides its own mistakes is worth nothing.

**What does not change:** ctext.org's structured data really is **CC BY-NC-SA 3.0**, and NonCommercial really is incompatible with the companion volume. And the exclusion of the excavated manuscripts stands on entirely different grounds — see below.

---

## Why stricter than the law requires

The ancient texts are free. The Laozi is roughly 2,400 years old; Wang Bi died in 249 CE; Heshang Gong and Han Feizi are older still. No copyright subsists in any of them, and a faithful transcription of a public-domain text creates no new copyright — in the United States see *Feist v. Rural Telephone* (1991), rejecting "sweat of the brow," and *Bridgeman Art Library v. Corel* (1999) for faithful reproductions.

**So why keep rules at all?** Because "the characters are ancient, therefore the file is free" needs to be *true of the specific file in front of you*. Two things can make it untrue:

1. **A source can have its own licence over its own additions.** ctext.org licenses its structured data **CC BY-NC-SA 3.0**. The characters are not theirs, but the database is.
2. **Modern editions really do add protectable material.** Not the characters, but the **punctuation**, the collation apparatus, the emendations, the reconstruction of damaged graphs, the annotations, and the selection and arrangement. Some of that is thin; some is genuine scholarship by living people.

---

## The admission rules

**A file may be added only if all four hold.**

1. **The work itself is public domain by age** — pre-modern, and its author long dead.
2. **The specific printing or transcription is either pre-1929, or dedicated CC0 / marked public domain, or a faithful transcription of such a printing.** "Found on the open web" is not provenance; the *edition* must be nameable.
3. **Its frontmatter names that source exactly** — work, author, edition, dates, host, and URL.
4. **Any modern editorial layer is either absent, excluded, or marked.** Punctuation especially.

**And one category is excluded outright, on grounds unrelated to licence text.**

**No transcriptions of the excavated manuscripts.** The **Mawangdui** silks were excavated in 1973 and the **Guodian** slips in 1993. Reconstructing their damaged and missing graphs — the brackets, the □ marks, the conjectural readings — is **genuine editorial work by living scholars**, not faithful transcription of anything. Reproducing a reconstruction reproduces the scholarship.

**The exclusion is on the reconstructions, not on the manuscripts.** The silks and slips are themselves public domain by age, and a *faithful* transcription of a public-domain text creates no new copyright — see above. **So this rule tracks what is currently available, not what is permanently forbidden**, and it lapses for any excavated transcription that clears all four admission rules on its own merits: faithful rather than reconstructive (or expired, or CC0-dedicated), from a nameable edition, with the editorial layer marked, under a licence compatible with CC0. None does today. *(The Guodian search below is the worked instance, and its "there cannot be one **yet**" is deliberate.)*

**Instead, record the facts.** See `variants.yaml`. "Mawangdui A and B read 自今及古 where Wang Bi reads 自古及今" is a **fact about a text**, and facts are not copyrightable. This is not merely the safe path; it is better practice, because a fact can be cited and checked while a bulk transcription only invites trust.

### The Guodian question, asked properly and answered no — 2026-08-17

*Shalom asked for a public-domain Guodian concordance to be vendored. It was searched for rather than ruled out from memory, because this file has been wrong about a licence once before. The search is recorded so nobody repeats it.*

**There is no public-domain transcription of the Guodian slips, and there cannot be one yet.** The slips were excavated in October 1993; the standard 釋文 (*shìwén* — the reading of the Chu-script graphs into modern characters) was produced by the Jingmen Museum team and published by 文物出版社 (Wenwu Chubanshe) in May 1998. That is 28 years old and squarely in copyright, in China and everywhere else.

**Chinese Wikisource does host a 郭店楚墓竹簡 page with the Laozi bundles in full.** It was checked, because the correction above establishes that a Wikisource mainspace transcription of a public-domain work is itself public domain. **That reasoning does not reach this page**, for three separate reasons, any one of which is sufficient:

1. **Wikisource's own logic does not apply.** Its policy holds that "anything that could attract copyright would no longer be faithful to the original." A 釋文 of damaged bamboo is *precisely* something that attracts copyright, because it is not a faithful transcription of anything legible — it is a reconstruction. The policy exempts faithful copies of readable printings; that is not what this is.
2. **It names no edition.** Admission rule 2 requires a *nameable* printing and rule 3 requires the frontmatter to cite it exactly. The page cites no scholarly source for its 釋文 at all. "Found on the open web is not provenance" is this file's own sentence, and it applies here more than anywhere.
3. **It carries annotations and variant readings** — a modern editorial layer that is neither absent, excluded, nor marked. That fails rule 4 outright.

And a fourth blocker that would stand even if all three fell: the page's content, whatever its status, would arrive under **CC BY-SA 4.0** if the site banner did govern. ShareAlike is copyleft. This repository is **CC0 with no exceptions** and the companion volume is **intended to be sold**. We could not dedicate it CC0 and we could not sell alongside it.

**A `shaloms-call` cannot fix this one.** A call sets aside a rule of this repository. It cannot set aside someone else's copyright, and it cannot make a CC0 dedication true of material we do not own. This is the rare case where the constraint is not ours to suspend.

**What was built instead: `guodian-inventory.yaml`.** Which chapters sit on which slips, in which bundle and in what order, is a **fact about an object recovered from the ground** — not a transcription, not a reconstruction, not a reading. It contains no Chu graphs, no 釋文, no reconstructed characters, and no bracketed conjectures. It answers the question that actually blocks work: *before drafting chapter N, does the oldest witness even have it?* `concordance.py --witnesses N` now prints the answer first, above the forks.

**No modern translations, of anything, for any reason.** Consulting them for *meaning* is governed by `process/method.md` §3 — pre-1931 only. None belong in this repository.

---

## What is here

| Path | Contents | Coverage |
|---|---|---|
| `variants.yaml` | The variant apparatus, as **facts** | 24 forks across 12 chapters |
| `guodian-inventory.yaml` | What the **oldest witness** contains, as facts — never a text | 31 chapters, 3 bundles |
| `commentaries/wangbi/` | 王弼 (d. 249 CE) on the Laozi, lemma by lemma | **all 81 chapters** *(71 until 2026-09-24)* |
| `commentaries/heshanggong/` | 河上公章句 (Han), lemma by lemma, with his own chapter titles | **81 of 81 chapters** |
| `commentaries/hanfeizi/` | 韓非子 解老 / 喻老 — the oldest commentary on the Laozi | **the 17 chapters he discusses** |
| `.cache/` | The fetched wikitext the import ran from | gitignored |

### `commentaries/wangbi/` — 老子道徳經注

**Source:** 欽定四庫全書 (Siku Quanshu), 子部十四 · 道家類 — imperially commissioned 1773, completed 1782. Transcribed on Chinese Wikisource in mainspace, tagged `{{PD-old}}`, at [老子道徳經 (四庫全書本)](https://zh.wikisource.org/zh-hant/老子道徳經_(四庫全書本)). A scan of the same edition, digitised by Zhejiang University Library, is at [archive.org/details/06049303.cn](https://archive.org/details/06049303.cn).

**Punctuation: none.** The transcription's own editorial policy excludes it — the wikitext opens *請根據四庫全書掃描版校對本頁 … 加標點請另外建立頁面* ("proofread against the Siku Quanshu scan … to add punctuation, create a separate page"). So the vendored text is the authorial layer only, which is both the cleanest rights position and the more faithful one.

**Imported by `tools/import_commentary.py`**, which is the point: the vendoring is **reproducible**, and it **verifies itself**. The source interleaves Laozi lemmas with Wang Bi's comment on each, so every lemma is matched against our own `source/chinese.md`:

```
wangbi: 81/81 chapters — complete
lemma lines: 361 matched our base text exactly, 38 with variants (90% exact)
commentary blocks: 425
```

A lemma that matches is direct evidence the transcription was carried across intact at that point. Lemmas that differ are **reported, never normalized away** — Siku glyph forms go in the importer's `ORTHOGRAPHIC` map, and genuine forks go in `variants.yaml`.

**Ten chapters were missing until 2026-09-24, and the transcription was never the reason.** For two years this paragraph said chapters 8, 14, 15, 19, 30, 54, 62, 70, 71 and 78 were *"simply not yet transcribed on Wikisource."* They were transcribed. In each case the chapter heading ran onto the end of the previous chapter's last comment line (…相濡之徳生也十九章, *"…then the kindness of moistening each other arises. Chapter nineteen"*). The importer matched only headings at the start of a line, so each of the ten was merged into the chapter before it. **The self-check reported the shortfall accurately and the explanation beside it was wrong.** A count of 71/81 is a finding about the parser as much as the source, and nothing asked which. `WORKLIST` T5-6.

**Preserved from the edition:** the Siku compilers' own collation notes, marked 〔…〕. They are 18th-century editorial matter, public domain by age, and immediately useful — the note at Ch 21, 〔案狀各本俱作然〕 ("for 狀, all editions read 然"), reopened a decision we had already made. **□** marks a glyph the transcribers could not encode; a gap is never passed off as text.

### `commentaries/heshanggong/` — 老子道德經 河上公章句

**Source:** *Sibu congkan* volume 0532, whose own colophon reads **景常熟瞿氏鐵琴銅劍樓藏宋刊本** — a photo-reproduction of the **Song** printed edition held in the Qu family's Iron-Qin-Copper-Sword Tower at Changshu. The commentary itself is Han. Transcribed on Chinese Wikisource in the `Page:` namespace against the djvu scan.

**Assembled from 77 scan pages.** Unlike the Wang Bi text, this one is not a single page: it is transcluded page by page from `Sibu Congkan0532-河上公-老子道德經-1-1.djvu`, pages 16–51 (卷上) and 52–92 (卷下). `tools/import_commentary.py --source heshanggong --fetch` retrieves them with a 0.4s pause between requests, caches them, and concatenates **in order before parsing** — because the text runs across page boundaries and a lemma or an annotation column can be cut in half by the end of a page.

**How the commentary is marked.** In the woodblock, Heshang Gong's notes are printed as **two columns of small type inline** with the main text. The transcription encodes each as `{{雙行註文|right|left}}` — "double-line annotation" — where the `|` is the column break, so the two halves join in reading order. Consecutive templates continue one note.

**Coverage: 81 of 81 chapters, complete.** 752 lemma lines matched our base text exactly, 80 with variants (90%), and 1054 commentary blocks.

**A bonus the edition carries: Heshang Gong titles every chapter himself** — 體道第一 (*"Embodying the Tao"*), 養身第二 (*"Nourishing the self"*), 安民第三 (*"Settling the people"*). These are preserved in each file's `chapter_title:` frontmatter. They are the oldest chapter names the text has, and they are interpretations in miniature.

### `commentaries/hanfeizi/` — 韓非子 解老 / 喻老

**The oldest surviving commentary on the Laozi**, by Han Fei (d. 233 BCE) — earlier than Heshang Gong and five centuries before Wang Bi. Chapters 20 (解老, *"Explaining Laozi"*) and 21 (喻老, *"Illustrating Laozi"*) of the 韓非子.

**A different shape, and so a different importer.** Han Feizi does not gloss the text lemma by lemma; he **argues, and quotes**. The quotations sit in 「」, usually introduced by 故曰 (*"therefore it is said"*). So the chapter a passage belongs to is discovered by **matching each quotation against our own base text** — the same fidelity check the other two importers use, doing double duty here as the only way to index the essays at all.

**Coverage: the 17 chapters he discusses** — 1, 14, 26, 27, 36, 38, 41, 46, 47, 50, 54, 58, 59, 60, 63, 64, 67 — with 53 quotations, **all 53 matching our base text exactly.** "Missing chapters" is the wrong frame for this source: he never set out to cover the book. The coverage is found by quotation, so a passage he paraphrases without quoting will not appear.

**Punctuation: present, and retained.** This is the one vendored source that carries modern editorial punctuation, and the admission rules permit *marked* as well as absent or excluded. These are prose essays rather than lemma lists and are close to unreadable without it, so the punctuation stays and the frontmatter says so.

**What he is worth having.** 解老 is a systematic philosophical reading — it opens on Ch 38's 上德不德 and works through it clause by clause. 喻老 is the opposite: **anecdote**. The great arises from the small, 千丈之堤，以螻蟻之穴潰 (*"a thousand-foot dyke is breached by a mole-cricket's hole"*), and then the story of Bian Que and the Duke of Cai, who would not treat an illness while it was still shallow. He is the only commentator in this collection who argues by narrative, and on Ch 63 he supplies a reading of 大小多少 — 大必起於小 (*"the great must arise from the small"*) — that neither Wang Bi nor the modern discussion offers.

### Nothing is owed

All three classical commentaries named in `process/method.md` §3 are now in the repository. **Every chapter has at least two**: 王弼 and 河上公 both cover all 81.

What could still be added, in rough order of value: the **Fu Yi** (傅奕) recension, which is a *received* text and therefore admissible in full where the excavated manuscripts are not; and a **Guodian / Mawangdui variant sweep** for the chapters not yet in `variants.yaml`, recorded as facts.

**The Guodian sweep is now the highest-value item on that list**, and `guodian-inventory.yaml` says where to point it. Two chapters are flagged in the inventory as owing work: **Ch 19**, where the best-known divergence in the entire Guodian Laozi sits and our apparatus is silent, and **Ch 25**, where `DISCOVERIES.md` §1 rests on the Mawangdui silks without consulting the older witness that also carries the chapter.

---

## Frontmatter for a commentary file

```yaml
---
work: "老子道德經注"          # the commentary's own title
author: "王弼"                # 226-249 CE
chapter: 21
edition: "四部叢刊 初編"       # the exact printing transcribed from
publisher: "商務印書館"
year: 1919
obtained: "https://archive.org/details/…"   # or: "physical copy, <library>"
punctuation: "editorial, present"           # or "none in source"
rights: "public domain by age; printing predates 1929"
transcribed: 2026-08-11
---
```

---

## On citing rather than copying

Where a commentary's *reading* matters to a decision, the practice already in use is the right one: **quote the phrase that carries the argument, gloss it, and cite it.** Wang Bi's gloss on Chapter 21 — 此上之所云也, *"'this' is what was said above"* — is nine characters, and quoting nine characters of a third-century commentary to make an argument about it is fair by any standard and free by age.

A repository does not need to *contain* a library in order to *use* one.
