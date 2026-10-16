<!--
Thank you. Before anything else: this repository is CC0, and contributions are
released into the public domain too. If your change alters the text, you'll be
named in the notes — because that's the truth about how the reading was arrived
at, not because the license asks for it.
-->

**What changes, and why**

**If this touches the translation**

- [ ] Every Chinese character in this PR carries pinyin and an English rendering
- [ ] Checked against the Chinese in its own chapter, not from memory
- [ ] Checked whether the change propagates — `python3 tools/concordance.py <character>`
- [ ] The sage is never "he"
- [ ] Lowercase throughout, except the Tao
- [ ] Trailing double-spaces preserved (verse line breaks are load-bearing)

**Checks**

```bash
python3 tools/fix-linebreaks.py --check
python3 tools/check_locks.py
python3 -m unittest discover -s tools/tests
python3 tools/build_index.py                      # if a glossary entry changed
python3 tools/build_db.py && python3 tools/export.py \
  && python3 tools/build_graph.py && python3 tools/export_atlas.py
```

- [ ] The checks pass, and `data/` (and the glossary index, if an entry changed) is rebuilt and committed — CI fails a PR whose generated files are stale. Everything CI runs is in `.github/workflows/checks.yml`.

<!--
If check_locks.py flags something you believe is right, don't delete the rule.
Either waive the single finding with a lock-ok comment in that chapter's
## Notes (CONTRIBUTING.md shows the form), then rebuild data/, since the Notes
are published in the export; or say so here and I'll make the call.
-->

**Anything you're unsure about**

<!-- Genuinely welcome. An unfinished PR with a good question beats a polished one. -->
