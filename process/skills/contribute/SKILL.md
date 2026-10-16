---
name: contribute
description: Help anyone — a Substack reader, a visitor from opencosmos.ai, someone who has never seen this repository — turn a suggestion about the Open Tao Te Ching into the right contribution, starting from nothing but what they say. Use when someone wants to suggest an edit, report a line or word that reads wrong, propose different English, fix a typo, or "contribute" without naming a character or file. Finds the line, gathers what the repository already says about it, routes the suggestion to an issue or a pull request, and hands character glosses to the suggest-edit skill.
---

# Contributing a suggestion, from anywhere

You are working **for a contributor** who may know nothing about this
repository. They read a chapter on Substack, or a line on opencosmos.ai, and
something struck them. They may not read Chinese, may not know the chapter
number, and may not know what a pull request is. All of that is fine.

**Your job is to find where their suggestion belongs and carry it there, in
their words, with the evidence attached.** Not to replace it with yours.

Read [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) first. Two things in it govern
everything below:

- **One person decides.** Everything here is a proposal to an editor. Tell the
  contributor that before they spend time on it, and again at the end.
- **Every Chinese character gets an English rendering beside it, every time** —
  in your messages and in anything you draft: 谷 (gǔ — a valley), never a bare 谷.
  A quoted line of Chinese gets its English beside it, not a gloss per character.

---

## 0. Get the repository — read-only, for now

Most suggestions end as an issue, which needs only a read. Clone; fork later,
in §4, only if this becomes a pull request:

```bash
git clone https://github.com/opencosmos-ai/taoteching && cd taoteching
```

Everything is standard-library Python 3; there is nothing to install.

## 1. Hear the suggestion, and name its kind

Ask what struck them, in their own words, if they have not said. Then the one
question that decides the route — **what kind of thing is it?**

| They say… | It is | It becomes |
|---|---|---|
| "This line — or this word — sounds off / preachy / clunky / old-fashioned", **no replacement in mind** | a line that doesn't land | **Issue** — `a-line-that-doesnt-land.md` |
| "This line, or this word, should say X instead" | a rendering proposal | **Issue** — `rendering-proposal.md` |
| "The English for this character is wrong or missing" (on the atlas, or anywhere) | a gloss | **Follow `process/skills/suggest-edit/SKILL.md`** — a PR or an issue |
| "There's a typo / a broken line / bad punctuation" — nothing about what it *says* | a correction | **Pull request** (§4) |
| "Something on the Character Atlas site is broken or confusing" | the atlas | **Issue** at `opencosmos-ai/chinese-atlas` |
| "Something on opencosmos.ai, or Cosmo, …" | the platform | **Issue** at `opencosmos-ai/opencosmos` |
| A question, a doubt, a disagreement that fits none of these | a conversation | **Issue**, blank |

**Why most of these are issues.** The translation is one person's reading, and
a line or a ruled term cannot be reviewed as a diff — it needs the conversation
first. An issue *is* the complete contribution, and CONTRIBUTING.md says the
most useful one — "this doesn't land" — needs no Chinese and no fix.

## 2. Find the line

If they named a chapter, open `chapters/NNN.md` (zero-padded: chapter 6 is
`006.md`). If they remember only the English, search the **translation itself**
— each chapter's `## Translation` block, not the source table beneath it, whose
old literal English ("virtue", "Heaven") is exactly what the edition rejects:

```bash
python3 - "deathless" <<'EOF'
import sys, pathlib, re
q = sys.argv[1].lower()
for p in sorted(pathlib.Path("chapters").glob("*.md")):
    t = p.read_text(encoding="utf-8")
    m = re.search(r"^## Translation\n(.*?)(?=^## )", t, re.S | re.M)
    for line in (m.group(1) if m else "").splitlines():
        if q in line.lower():
            print(f"ch {int(p.stem)}: {line.strip()}")
EOF
```

It is an exact match. People remember lines roughly, so **if a phrase finds
nothing, search one distinctive word** from it. Show them the line as it reads
now and confirm it is the one they mean.

**Then find the Chinese behind their word.** The chapter's `## Source` table
lines the Chinese up with a literal English, a phrase per row; the row whose
literal matches their line holds the characters: "is deathless" sits on the row
谷神不死 (gǔ shén bù sǐ — the valley spirit does not die), so the word is 死
(sǐ — to die), here as 不死 (bù sǐ — does not die).

## 3. Gather what the repository already says — every route

An issue needs the evidence as much as a PR does. Run all three:

```bash
python3 tools/concordance.py 死                 # every line the character stands in, book-wide
python3 tools/concordance.py --record 谷神       # what this repo has argued about it
grep -rn -i --exclude-dir=skills -e "deathless" -e "谷神" \
  notes/ process/ glossary/ WORKLIST.md chapters/006.md
```

- **Query the single character for the book-wide picture** (死 shows every use;
  不死 only this line). The concordance's first line names any lock and the
  words the edition refuses (`→ integrity   never: virtue, …`). Under each
  Chinese line, the **dim, indented** line is the source tables' old literal —
  not the translation — and the **`│` lines** are the edition's verse, the
  *whole chapter's*, not aligned to the line above: find the sentence that
  renders it.
- **`--record` searches the glossary, the notes, `WORKLIST.md` and the chapter
  notes, but not `process/`**, and only for the Chinese. The `grep` covers the
  English word and the rest. A chapter's `## Notes` may be empty while the
  reasoning sits elsewhere (`process/overlay-audit.md`, `notes/reading.md`).
- **For a rendering proposal, also read the commentaries and the witnesses** —
  this project consults them before changing a settled line:
  `concordance.py --commentary 6` and `concordance.py --witnesses 6`.

Then tell the contributor plainly what you found — one of these, usually:

- **Unruled ground.** No entry, no lock, the word not refused, nothing argued:
  say so. Their report is *especially* useful here, because nobody has looked.
- **A ruled term.** It has an entry (`glossary/<slug>.md`), maybe a lock: read
  them its reason in plain English. A change would reverse a ruling across the
  book — say that too.
- **A refused word** — theirs, or the line's. (*heaven, God, holy, virtue,
  righteousness, eternal, the Way, the One, …* — the overlay watchlist in
  CLAUDE.md.) Explain why, and ask what they mean by it.

**If they still want it passed along, pass it along — honestly**, in their own
words, saying what the evidence showed. Quote no modern translation's text:
sources are for meaning, never phrasing, pre-1931 public-domain only.

If the suggestion turns out to be about **one character's English** on its
card, follow `process/skills/suggest-edit/SKILL.md` from its §1 — it owns that
route.

## 4. A correction — the one PR this skill opens

A typo, a broken line break, a doubled word: a mechanical fix, not a different
reading. If it changes what a line *says*, it is a rendering proposal (§1).

Now fork — the contributor needs a GitHub account and the GitHub CLI
(`gh auth status`). `--remote` makes their fork `origin` and the project
`upstream`:

```bash
gh repo fork --remote
git status --short                          # must be empty — if not, ask what it is, and
                                            # commit or set it aside before branching
git fetch upstream
git switch -c fix/ch41-typo upstream/main   # ASCII only
```

**The line breaks are load-bearing.** The verse is Markdown, and every line of a
stanza ends in **two trailing spaces**. Do not let an editor strip them. Then:

```bash
python3 tools/build_db.py && python3 tools/export.py \
  && python3 tools/build_graph.py && python3 tools/export_atlas.py   # the verse feeds data/
python3 tools/fix-linebreaks.py --check
python3 tools/check_locks.py --severity error                       # what CI gates on
python3 -m unittest discover -s tools/tests
```

All three checks must pass; plain `check_locks.py` also prints info findings,
which never fail. **Even a one-character fix to the verse changes the generated
files** — the atlas export, the line and translation tables, the
locked-renderings report — and CI fails a PR whose `data/` is stale, so commit
them with the chapter.

## 5. Draft it, show them, and only then send it

**An issue.** Use the template's own fields, in its order, and **strip its
`<!-- … -->` comments**. Put the contributor's words in the fields — that is the
report. Where a field asks for scholarship they lack, say so plainly ("the
contributor does not read Chinese"). Then, below the fields, **a short section
headed *What the assistant found***: the line, its Chinese with English, and
the two or three facts from §3 that matter — not the whole search. End with one
line naming the AI assistant that helped.

Title it by the template's pattern (`Ch 6 — "deathless" sounds old-fashioned`)
and give them the link with template and title filled:

`https://github.com/opencosmos-ai/taoteching/issues/new?template=a-line-that-doesnt-land.md&title=<url-encoded title>`

(a blank issue: `…/issues/new`; another repository: swap the path). Tell them:
**the link opens the template; replace its text with the body you drafted, then
submit.** They post it themselves — the template carries the label that sorts
it, and an issue made from the command line would lose it.

**A pull request (§4).** Show them the diff and the PR text first. Title
`Ch 41: <what was wrong>`; body: what it said, what it says now, the checks
passing, and one line naming the AI assistant. Then, on their yes:

```bash
git add chapters/041.md data/
git commit        # subject: the PR title; body: one line of why
git push -u origin fix/ch41-typo
gh pr create --repo opencosmos-ai/taoteching --base main
```

## 6. Tell them what happens next

Give them the link, and say plainly: **it is a proposal, and one person
decides.** It may be taken, revised, or declined for reasons of consistency they
could not have known about — and if it changes the text, they will be named in
the notes. Nothing here is urgent.

---

**Do not:** edit `glossary/` or change what a verse line says in a PR from this
skill; push to `opencosmos-ai/taoteching` directly; strip trailing whitespace
from a chapter; invent a suggestion the contributor did not make; leave a
Chinese character unglossed anywhere the maintainer will read it.
