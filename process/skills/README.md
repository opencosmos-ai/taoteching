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

## To activate

Symlink into the agent's skills directory, so they stay in sync with the repo:

```bash
for s in process/skills/*/; do
  ln -sfn "$(pwd)/${s%/}" ~/.claude/skills/"$(basename "$s")"
done
```

**The links are absolute, so they break when the repository moves** — and a broken link fails silently: the skill simply stops appearing. All three went missing this way when the repo moved from `shalomormsby/taoteching` to `opencosmos-ai/taoteching`. If a skill is missing, check where its link points, and re-run the loop above from the repository's current location:

```bash
for s in chapter-review glossary-entry principle-entry; do readlink ~/.claude/skills/$s; done
```

Skills load when a session starts, so a relink shows up in the next one.

## Why these exist

`process/method.md` describes how the work is done. A skill makes a piece of that method
**executable** — loaded automatically when the task arises, rather than depending on
someone remembering to read the guide. It is also how the method transfers intact to a
different or more capable model later.
