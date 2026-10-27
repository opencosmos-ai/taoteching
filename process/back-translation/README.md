# The back-translation audit's raw reports

*Frozen evidence for [`../back-translation-audit.md`](../back-translation-audit.md). These are the blind readers' and comparers' reports exactly as they were written on 2026-10-27. Never edit them. A correction belongs in the ledger, not here.*

**They are AI readings, and evidence, not authority.** Weigh them the way `CLAUDE.md` says to weigh a commentary: as testimony about what a line says, never as the line.

| Files | Who wrote them | What they saw |
|---|---|---|
| `A_01-27.md` · `A_28-54.md` · `A_55-81.md` | **Reader A**, three blind readers | the English verse only, nothing else from this repository |
| `B_01-14.md` … `B_69-81.md` | **Reader B**, six blind readers | the base Chinese with pinyin, and the vendored Wang Bi, Heshang Gong and Han Fei; no English from this repository |
| `C_01-27.md` · `C_28-54.md` · `C_55-81.md` | **the comparers**, three | both readers' reports, and the whole repository, read-only, to verify against |
| `FORMAT.md` · `B_BRIEF.md` · `C_BRIEF.md` | the briefs | the shared claim format, Reader B's instructions and the comparers' instructions. Reader A's instructions are quoted in the ledger's *How it was run* |

**To re-run the audit**, give fresh readers the same briefs and packets: the verse of each chapter for A, and each chapter's source table plus its files in `sources/commentaries/` for B. Then compare the new reports against these. A divergence that appears in both runs is not one reader's taste.

**One allowance.** Reader A's paraphrase of chapter 1 restates a superseded wording, so `process/retractions.yaml` allows `A_*.md` for that one entry, as it already allows the frozen archive.
