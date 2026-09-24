---
id: never-silence-a-rule
title: "Never delete a rule to silence it — waive one finding, or set the rule aside on the record"
status: active
since: 2026-08-11
trigger: "a check is firing and you are about to remove, narrow or bypass the rule to make it stop"
applies: [tooling, process]
evidence: ["ARCHITECTURE.md#escape-hatches-and-why-each-costs-something", "process/shaloms-call.md#how-a-call-works"]
check: check_locks
supersedes: []
---

# Never delete a rule to silence it

**The rule.** When a check is wrong there are two answers and **they are different sizes**. A `lock-ok` comment in the chapter's `## Notes` waives **one finding** and must carry a reason. A `shaloms-call` sets aside **a whole rule**, with a scope, an expiry and a reason. **Deleting the rule is neither, and it is never the answer.**

**When it fires.** When a rule is firing, you are confident it is wrong, and the fastest fix is to make it go away.

---

## Why this holds

**A rule removed is a rule that stops protecting the other eighty chapters.** The finding in front of you may well be a false positive; the rule exists because of the true positives you are not looking at. Deleting it converts one local judgment into a silent global change.

**And a suppressed rule is invisible, which is the actual danger.** *Suspension is never silent*: `check_locks.py` prints a footer naming every rule currently set aside. **A rule you cannot see is switched off is how a lock quietly dies.**

**The two escape hatches are deliberately asymmetric, and the asymmetry is the design.** An **unused waiver is itself an error**, so waivers self-clean and the files stay honest. An **expired call is an error**, so each override gets renewed or retired deliberately, while a dormant `standing` call may sit indefinitely. *Waivers should self-clean; overrides should demand a decision.*

**And `git commit --no-verify` is the ad-hoc version.** Fine once. **Twice on the same rule is a signal that a call is owed** — or that the rule wants changing, properly, with the reasoning recorded.

---

## Why this principle exists

**The escape hatches**, and what each costs, are set out together precisely so the cheap one is not reached for when the expensive one is owed. → [ARCHITECTURE](../../ARCHITECTURE.md#escape-hatches-and-why-each-costs-something)

**How a call works** — only Shalom makes one; a call **suspends, it never deletes**; the rule stays written where it is and the override sits beside it, so a future reader sees the rule, the override, and the reason. → [shaloms-call](../../process/shaloms-call.md#how-a-call-works)

---

## How it is implemented

| Where | What it does |
|---|---|
| **`lock-ok`** waivers | waive one finding, in a chapter's Notes, with a required reason; an unused waiver is itself an error |
| **`process/shaloms-call.md`** | sets aside a whole rule, with `scope:` and `until:`; `stale-shaloms-call` fails an expired call and `shaloms-call-unparsed` fails one the tool cannot read |
| **`CLAUDE.md`** | *the AI never writes a call on its own initiative* |
| **`CLAUDE.md` → *The harness*** | `--applies tooling` lists it before anything in `tools/` or `data/` changes |
| **`CLAUDE.md` → *Start here*** | `--applies process` lists it at the start of every session |

**Enforced by `check_locks.py`.**

---

## Where it does not fire

**A rule that is simply wrong should be corrected, not waived.** If a `forbidden:` string catches a word no reasonable rendering would violate, fix the string — and say in the entry what changed. **Correcting a rule is not silencing it**; the test is whether the reasoning is recorded and the protection survives.

**Narrowing on evidence is legitimate.** Several words **cannot** go on a forbidden list because another character legitimately claims them in the same chapter. Leaving them off is precision, not evasion — and both `chi-持.md` and `zhi-執.md` say which words they had to leave off and why.

---

## What it obliges

1. **Waive one finding with `lock-ok` and a reason**, in that chapter's Notes.
2. **Set aside a whole rule only through `process/shaloms-call.md`**, with `scope:` and `until:` — and **only Shalom makes a call.** The AI may draft one when he makes it and must then act on it.
3. **Never write a call on your own initiative, and never cite one you wrote unprompted.**
4. **If you find yourself writing the same waiver into many chapters, the rule wants a call — or wants changing.**
