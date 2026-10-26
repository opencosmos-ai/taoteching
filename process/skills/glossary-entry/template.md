# The glossary entry template

*Drawn on 2026-10-26 from the entries that read best: 谷 (gǔ — valley), 水 (shuǐ — water), 牝 (pìn — the female), 雌 (cí — the hen), 柔 (róu — soft), 常 (cháng — ever-present) and 民 (mín — the people). Shalom asked for one shape every entry follows.*

Four headings are fixed, word for word, so a reader always knows where to look and `tools/tests/test_entry_shape.py` can hold them: **The graph**, **What is set aside**, **Working register**, **Left open**, in that order. Every other heading is free, and **must state a claim**. *"Three chapters, and she is a body in each"* is a heading. *"Usage"* is not. A claim in the heading is what keeps an entry an argument rather than a filing cabinet.

Each slot below says what it is for, and what earns it its place. Copy the skeleton, then delete the guidance. In it, 字 (zì — "written character") stands in for the term.

```markdown
---
term: "字"
pinyin: "zì"
render: "english"
forbidden: []
chapters: []
status: open
pairing: false
---

## 字 (Zì) — The English

*Say "dzuh," falling. N appearances across M chapters. One sentence on what the word is in this book.*

**Recommended: 字 → "english".** *(Not "x," which … Not "y," which ….)*

### The graph: <what it pictures>

### <N lines>, and <what the word does in them>

### <a claim>

### <字 (pinyin — "english")>

### What is set aside

### Working register

### What no rule can enforce

### Left open
```

## The slots

**The head** (required). The term, how it sounds, how often it stands, and the ruling, before any argument: a reader wants to know what the word *is* first (`SKILL.md` §2.1). The lock line names what is refused in a parenthesis, one reason each. If the ruling is Shalom's call, say so and date it.

**The graph: <what it pictures>** (required). Oracle bone, then bronze and seal, then the Shuowen's line, quoted in Chinese with its English. *Earns its place* by saying what the picture is, and **where the picture stops**: the Shuowen's water is the Han's five phases, which the book never uses. The heading names the picture: *"wood that bends and comes back,"* *"an animal, and its sex."*

**The evidence: <N lines>, and <a claim about them>** (required). Every line the term stands in, or every line that matters if there are many, each as a **verse quote** (`SKILL.md` §3). Then the pattern, in bold, as the first sentence after them: *"In each line she is something you could point at."* *Earns its place* by letting the lines argue: the count, what the word does in each, and what it never does.

**Claim-titled sections** (0–3, as the term needs them). The pairing (柔 (róu — soft) against 剛 (gāng — unbending)), the hardest line (`SKILL.md` §6), what the silk and bamboo manuscripts change, the company the word keeps (*"Water and the valley"*). Each heading is a finding.

**What the commentators did with it** (when they diverge, or merge what the book keeps apart). Wang Bi and Heshang Gong, quoted in Chinese with full English renderings, names romanized. *Earns its place* only if the reading changes something: a grammar, a ruling, a fork. Agreement goes in a sentence elsewhere.

**One section per character in `covers:`** (required for each). Headed with the character glossed: *"牡 (mǔ — the male)."* Its graph, its lines, and why it lives in this entry and not its own.

**What is set aside** (required). Every rejected English, each with **its own** reason: the hymn test, the pointing test, the overlay it brings. This is where the critique of the *conventional* English lives (`SKILL.md` §3 forbids critique of our own drafts). **For any term that names or stands for the female, set aside every English that could be quoted to justify her domination, and say why** (`CLAUDE.md` standing rule 1).

**Working register** (required). How the English flexes with the grammar, with a table where the senses split: the line, our English, and why. Name any flexion recorded in `flexions:`.

**What no rule can enforce** (when a ruling cannot be gated). A word the entry rules out that another character in the same chapters may print: name the blocking character and the shared chapters (`SKILL.md` §2.7).

**Left open** (required). The real tension, stated honestly: a fork in the witnesses, a cost the English pays, a question for Shalom. If nothing is unresolved, look harder (`SKILL.md` §2.6). Each open thread names its home: `WORKLIST.md`, `DISCOVERIES.md`, or the entry that owes the answer.

## Two tests on every sentence

The **hymn test** and the **pointing test** (`SKILL.md` §2). And the house rules: lowercase everything but the Tao, never "he" for the sage, gloss every character.
