# Skills

Reusable, machine-readable procedures for this project. Each is a folder containing a
`SKILL.md` with YAML frontmatter, in the format used by Claude Code and Cowork.

They live here — in the repository, under CC0 — rather than only in a local config, so
that the method travels with the work: version-controlled, reviewable, portable between
AI collaborators, and available to anyone who clones the repo.

| Skill | Use when |
|---|---|
| `chapter-review/` | Drafting or reviewing a chapter from the Chinese |
| `glossary-entry/` | Adding or revising a term in `glossary/`, or locking a rendering |
| `principle-entry/` | Recording a rule that will govern chapters nobody has read yet |

## How Claude finds them

**Nothing to do: they are committed.** `.claude/skills/` holds one symlink per skill, each **relative** — `.claude/skills/principle-entry → ../../process/skills/principle-entry`. Claude Code loads project skills from `.claude/skills/`, follows symlinked folders, and loads a skill once even if several locations point at it. So anyone who clones the repository and opens it in Claude Code — as the working directory or as an added directory — gets all three, with no setup step.

**The skills themselves stay here, in `process/skills/`**, under CC0 and in the method's own directory. `.claude/skills/` only points at them, so there is still one copy.

**Why relative.** The links used to be absolute, created per machine in `~/.claude/skills/` by a loop in this file. When the repository moved from `shalomormsby/taoteching` to `opencosmos-ai/taoteching`, all three dangled, and a dangling link fails silently: the skill simply stops appearing. A relative link moves with the repository.

**To add a skill:** create `process/skills/<name>/SKILL.md`, then link it:

```bash
ln -sfn ../../process/skills/<name> .claude/skills/<name>
```

**Personal links** in `~/.claude/skills/` are no longer needed. If you keep one, it must point at the repository's **current** location — check with `readlink ~/.claude/skills/<name>`.

## Using them in another repository

**Do not symlink these into another repository.** Two reasons, both learned the hard way:

- **They are bound to this repository.** Every one runs this repo's Python tools — `chapter-review` names them twelve times, `glossary-entry` nine, `principle-entry` four — and walks `chapters/`, `notes/` and `process/principles/`. In a repository without those, a linked skill is discovered, invoked, and wrong, which is worse than absent.
- **A link across repositories resolves only where both sit side by side.** Committed, it dangles for anyone who clones one repository alone, and in CI.

**Share the method, not the file.** A neighbouring project — the I Ching translation is the first — carries its own skill, stating which procedure it inherits from here and what differs: its paths, its build command, its loaders. That is how its `principles/README.md` already inherits this project's principles, and it is what its own principle *inheriting means saying where you differ* requires.

## Why these exist

`process/method.md` describes how the work is done. A skill makes a piece of that method
**executable** — loaded automatically when the task arises, rather than depending on
someone remembering to read the guide. It is also how the method transfers intact to a
different or more capable model later.
