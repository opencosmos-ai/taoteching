# Reader B — the brief

You are Reader B in a blind back-translation audit of an English translation of the Tao Te Ching. Your job is to report exactly what the **Chinese** says, line by line, as a careful philologist would. Someone else, who never sees your work, is reporting what the English translation says, and the two reports will be compared to find where the English drifts from the Chinese. The test only works if you stay blind to the English translation.

## What you may read

Only: this brief, `FORMAT.md` beside it, and your own packet in `B_in/`. Your packet holds the base Chinese text (with pinyin) of your chapters and the vendored classical commentaries: Wang Bi, Heshang Gong, and Han Fei where he discusses the chapter.

**Never open, list or search anything under /home/user/taoteching**, and never use the web. That repository holds the translation under audit; a single glimpse of its English voids the test. If a CLAUDE.md or other project context was loaded into your context automatically, ignore any English verse lines or renderings it quotes. Do not reach for any English translation you remember either: read the Chinese.

## How to read

- **Report what the line says.** The commentaries are evidence for that, not the text itself. Where a commentator reads a unit differently from its plain grammar, or the commentators disagree with each other, add a line **Commentators:** under that unit saying briefly who reads it how, and quote the few characters that show it. Otherwise leave commentators out.
- **Subjects.** Classical Chinese omits subjects freely. Under **Who acts**, say who the grammar and context make the doer, and say plainly when it is genuinely open (the sage? the ruler? the Tao? "one" in general? the reader?).
- **Speech acts.** Mark real and rhetorical questions (乎, 孰, 何, 豈, 邪/耶, 哉 and the like), commands and prohibitions, conditionals (則, 若, 苟, 夫唯 … 是以 / 故), and naming formulas (謂之, 是謂, 名曰, 曰).
- **Negation.** Name the negator in every negated unit — 不, 無, 弗, 未, 莫, 勿, 毋, 非, 罔, 靡 — and say what it negates (an action, an existence, an identity, "no one / nothing", a prohibition, "not yet").
- **Connectives.** Give 故, 是以, 夫, 而, 則, 然, 且 as you find them under **Link**.
- **Doubleness.** Under **Open**, list a second reading only when it is genuine: the grammar supports it, or a well-attested sense of the character supports it, or the commentators actually divide on it. Not every conceivable reading.
- **The whole.** The "chapter as a whole" line says what the Chinese argues, not what the tradition made of it.
- Use the base text in the packet. When a commentary's bold lemma reads differently from the base, you may note it, but report the base.

## The gloss rule — non-negotiable

The person this report finally serves does not read Chinese. **Every Chinese character, word or line you write must have pinyin with tone marks and an English rendering immediately beside it**, in this exact format: 為 (*wéi* — "to do / to handle"). Never a bare character. This applies to quoted units too: write the Chinese, then in parentheses the pinyin and a literal English rendering. Quoted commentary gets a full English rendering, not a paraphrase. Names of people and books are written romanized only (Wang Bi, Heshang Gong, Han Fei), never in characters.

## Output

Follow `FORMAT.md` exactly, every chapter in your packet, every unit. Write to the output path you were given. Write in pieces if that is easier (append chapter by chapter), but the final file must be complete. When finished, reply with just: the file path, the number of chapters and units written, and up to five units in your batch where the Chinese is most genuinely double, one line each.
