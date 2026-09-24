---
id: deterministic-before-gated
title: "Make a generator deterministic before you gate it"
status: active
since: 2026-08-31
trigger: "you are about to add a diff gate to a generated file"
applies: [tooling]
evidence: ["ARCHITECTURE.md#what-is-generated-and-from-what", "ARCHITECTURE.md#the-gates"]
check: none
supersedes: []
---

# Make a generator deterministic before you gate it

**The rule.** A `git diff --exit-code` gate on a generated file is only as good as the generator's determinism. **Make the output a function of the data alone, then gate it.** Gating a non-deterministic generator produces noise instead of findings.

**When it fires.** The moment you write a CI step that rebuilds something and diffs it.

---

## Why this holds

**A noisy gate is worse than no gate**, for the same reason a checker that cries wolf is worse than none: the failure stops carrying information, and people learn to re-run it until it passes. See [[evidence-gate]].

**The specific trap is unordered queries.** `export.py` orders all eleven of its queries, which is why its CSVs never drifted. `build_graph.py` ordered **one of eight**, so its row order came from SQLite's query planner — **stable for one machine and one planner version, which is exactly the stability that breaks when the gate runs on another.** Every query there is now ordered and the co-occurrence map is emitted sorted.

**And the gate is worth building, because the failure it catches is invisible otherwise.** `data/constellation-chars.json` had **never agreed** with `data/characters.csv`: both entered the repository in the same commit, but the JSON was built from an older database, so it published glosses the CSV had already withdrawn and older wordings for ninety more. **Nothing rebuilt it and nothing compared them.** A person found it seven months later by reading a diff.

**Two generated files publishing different things is the failure mode of a repository that generates anything at all** — and the only reliable defence is rebuild-and-diff in CI.

---

## Why this principle exists

**What is generated, and from what** — the table of every build product, its generator, and whether CI fails when it is stale. → [ARCHITECTURE](../../ARCHITECTURE.md#what-is-generated-and-from-what)

**The gates** — where each check runs, and what it is allowed to block. → [ARCHITECTURE](../../ARCHITECTURE.md#the-gates)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`export.py`** · **`build_graph.py`** | every query ordered and every map emitted sorted, so output is a function of the data alone |
| **CI**, *generated atlas files are current* | rebuilds `build_db → export → build_graph` and fails on `git diff data/` — a gate that is only safe because of the ordering above |
| **`BASELINE`** in `tools/build_db.py` | the regression counts, each carrying the note that says what it counts and why it last moved |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |

**Enforced by CI**, once a generator is deterministic. Making it so is the author's job and nothing checks it in advance — a nondeterministic generator shows up as a gate that fails on one machine only.

---

## Where it does not fire

**A file that is not committed does not need a gate.** The sqlite database is committed for convenience; the CSVs are gated because **a binary blob cannot be diffed or reviewed and the CSVs can.**

**And a generator with a legitimately variable output should not be gated at all** — it should be made deterministic, or its output should not be committed. There is no third option that ends well.

---

## What it obliges

1. **Order every query, sort every map, before adding the gate.**
2. **Gate the reviewable artifact, not the opaque one.**
3. **Rebuild every generated file after any change to its source**, and commit the result in the same commit.
4. **When a gate fires on a machine and not on yours, suspect the generator, not the gate.**
