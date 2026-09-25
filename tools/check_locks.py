#!/usr/bin/env python3
"""
check_locks.py — the settled decisions of this translation, as tests.

The glossary carries the reasoning. CLAUDE.md carries the rules. This carries
neither: it only checks that the manuscript still obeys what has already been
decided somewhere else. Every rule below cites the written decision it enforces,
and a rule with no citation does not belong here.

    python3 tools/check_locks.py                  # everything
    python3 tools/check_locks.py --chapter 53
    python3 tools/check_locks.py --rule devotional-capitalization -v
    python3 tools/check_locks.py --staged         # what the pre-commit hook runs
    python3 tools/check_locks.py --json

Exits non-zero when an error-severity rule fires. Warnings and info never fail.

Two things this tool will never do: rewrite the verse, or judge it. It reports
where the manuscript departs from a decision already made, and stops there.
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import (  # noqa: E402
    ROOT, UNTRANSLATED_MARKER, fold, load_base_text, load_calls, load_chapters,
    load_terms, load_variants,
)

ERROR, WARN, INFO = "error", "warn", "info"
SEVERITY_ORDER = {ERROR: 0, WARN: 1, INFO: 2}


@dataclass
class Finding:
    rule: str
    severity: str
    chapter: int
    line_no: int
    message: str
    line: str = ""
    ref: str = ""                       # where the decision is written down
    tags: set = field(default_factory=set)   # what a lock-ok waiver may name
    scope: set = field(default_factory=set)  # chapters whose Notes may waive this
    waived_by: object = None

    def waivable_in(self):
        """A finding about two chapters can be waived from either of them.

        Cross-chapter findings are filed under one number for display, but the
        decision they record may belong to the other — a formula deliberately
        rendered two ways is Ch 23's choice, not Ch 17's, even though the
        finding prints under 17.
        """
        return self.scope or {self.chapter}

    def as_dict(self):
        return {
            "rule": self.rule, "severity": self.severity, "chapter": self.chapter,
            "line": self.line_no, "message": self.message, "text": self.line,
            "ref": self.ref, "waived": bool(self.waived_by),
        }


# --------------------------------------------------------------------- helpers

def _waiver_names(entry_path, term):
    """Every name a lock-ok waiver may use for this term.

    glossary/chang-常.md yields {"chang", "chang-常", "常"} — the bare pinyin for
    brevity, the full stem to disambiguate, and the character itself. The bare
    pinyin is not always unique: 心 (xīn — heart) and 信 (xìn — trust) both
    reduce to "xin", so a waiver for either must name the stem or the character.
    """
    stem = Path(entry_path).stem if entry_path else ""
    names = {term} if term else set()
    if stem:
        names.add(stem)
        names.add(stem.split("-")[0])
    return {n for n in names if n}


def _sentence_initial(line, pos):
    """Is this position the start of a sentence? Then a capital is legitimate."""
    before = line[:pos].rstrip()
    if not before:
        return True
    return before[-1] in '.!?:;"“' or before.endswith(("—", "–"))


def _cased(needle):
    """A forbidden string written with a capital means the capital IS the violation.

    "the Way" is wrong; "the way of nature" is not. "eternal" is wrong in any
    case, which is how "eternally" hid from the 2026-08-10 sweep. So the policy
    is derived from how the decision was written, not configured separately.
    """
    return any(c.isupper() for c in needle)


def _find_all(line, needle, case_sensitive):
    flags = 0 if case_sensitive else re.IGNORECASE
    return list(re.finditer(re.escape(needle), line, flags))


def _cjk_runs(text):
    return re.findall(r"[㐀-鿿]+", text)


def _split_segments(text):
    """Split a source row into its comma-segments — the unit a formula lives in.

    Punctuation in the Chinese is a later editor's addition (see notes/
    translation.md), but it tracks the character-beats faithfully enough to
    delimit formulas, and the literal gloss is punctuated to match.
    """
    return [s.strip() for s in re.split(r"[，。；、,;.]", text) if s.strip()]


# Dropped when guessing which two English lines render the same Chinese formula:
# these carry no signal, and they are exactly what two unrelated lines share.
def _stem(w):
    """Enough stemming that "serve" meets "serves" and "prize" meets "prizing".

    Applied to both sides of every comparison, so its crudeness cancels out:
    it only has to map two forms of one word to the same string, not to a word.
    """
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    for suffix in ("ing", "ed"):
        if len(w) > len(suffix) + 2 and w.endswith(suffix):
            w = w[:-len(suffix)]
            break
    return w[:-1] if len(w) > 3 and w.endswith("e") else w


_STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "is", "it", "its",
    "this", "that", "they", "their", "them", "you", "your", "not", "without",
    "with", "for", "as", "so", "be", "are", "do", "does", "no", "then", "thus",
    "therefore", "what", "who", "one", "all", "can", "will", "by", "from", "at",
}


# ----------------------------------------------------------------------- rules

def rule_forbidden_rendering(chapters, terms, **_):
    """A locked term's forbidden rendering, with the character to prove it.

    The evidence gate is the whole design: "virtue" is an error only when 德 is
    in *this* chapter's own Chinese. Without it, roughly a third of the flags
    are 常 (cháng, constant) being blamed for a line that renders 長 (cháng,
    long) — and a checker at that noise level gets ignored within a week.
    """
    out = []
    for t in terms:
        for needle in t.forbidden:
            cs = _cased(needle)
            for ch in chapters:
                evidence = [c for c in t.characters if ch.has(c)]
                for ln, line in ch.verse:
                    for m in _find_all(line, needle, cs):
                        if cs and _sentence_initial(line, m.start()):
                            continue
                        if evidence:
                            msg = (f'{t.term} ({t.pinyin}) is in this chapter, and "{needle}" '
                                   f'is forbidden for it — render as: {t.render}')
                            sev = t.severity
                        else:
                            msg = (f'"{needle}" is forbidden for {t.term} ({t.pinyin}), but '
                                   f'{"/".join(t.characters)} is not in this chapter — '
                                   f'likely an ordinary English word, verify before changing')
                            sev = INFO
                        out.append(Finding(
                            "forbidden-rendering", sev, ch.number, ln, msg,
                            line.strip(), t.entry, _waiver_names(t.entry, t.term),
                        ))
    return out


# CLAUDE.md standing rule 1: never refer to the sage as "he". Applies to all
# archetypal figures. Not evidence-gated — this one is absolute.
_MALE_PRONOUN = re.compile(r"\b(he|his|him|himself)\b", re.IGNORECASE)


def rule_sage_pronoun(chapters, **_):
    out = []
    for ch in chapters:
        for ln, line in ch.verse:
            for m in _MALE_PRONOUN.finditer(line):
                out.append(Finding(
                    "sage-pronoun", ERROR, ch.number, ln,
                    f'"{m.group(0)}" — use singular they/their, or recast. '
                    f"Standing rule 1; applies to every archetypal figure.",
                    line.strip(), "CLAUDE.md · standing rule 1", {"sage-pronoun"},
                ))
    return out


# CLAUDE.md standing rule 5: English capitals confer status — they turn a word
# into a doctrine. Each watched word maps to the character that would license
# the concept, so the evidence gate applies here too.
_DEVOTIONAL = {
    "Way": "道", "Virtue": "德", "Heaven": "天", "Nature": "自然", "Being": "有",
    "Mother": "母", "Sage": "聖", "Stillness": "靜", "Uncarved": "樸",
    "Master": "聖", "Source": "母", "Origin": "母", "Void": "無",
}


def rule_devotional_capitalization(chapters, **_):
    """Capitals mid-sentence, where the Chinese has none to give.

    Complements forbidden-rendering rather than duplicating it: a forbidden
    phrase like "the Way" is defeated by an inserted adjective, and "The great
    Way" in ch 53 slips through the phrase rule while being exactly the same
    error. This rule watches the bare word.
    """
    out = []
    for ch in chapters:
        for ln, line in ch.verse:
            for word, gate in _DEVOTIONAL.items():
                for m in re.finditer(rf"\b{word}\b", line):
                    if _sentence_initial(line, m.start()):
                        continue
                    has_gate = ch.has(gate) or any(ch.has(g) for g in gate)
                    sev = ERROR if has_gate else INFO
                    out.append(Finding(
                        "devotional-capitalization", sev, ch.number, ln,
                        f'"{word}" is capitalized mid-sentence — lowercase everything '
                        f"but the Tao. Capitals turn a word into a doctrine."
                        + ("" if has_gate else f" ({gate} is not in this chapter — verify.)"),
                        line.strip(), "CLAUDE.md · standing rule 5",
                        {"devotional-capitalization", word.lower()},
                    ))
    return out


# CLAUDE.md, the overlay watchlist: "our own besetting temptation — the
# mechanistic ('operating system', 'source code', 'generate')."
_MECHANISTIC = [
    "source code", "operating system", "algorithm", "programming", "software",
    "hardware", "mechanism", "system", "function", "output", "input", "network",
    "data", "protocol", "circuit", "engine",
]


def rule_mechanistic_register(chapters, **_):
    out = []
    for ch in chapters:
        for ln, line in ch.verse:
            for needle in _MECHANISTIC:
                for _ in _find_all(line, needle, False):
                    out.append(Finding(
                        "mechanistic-register", ERROR, ch.number, ln,
                        f'"{needle}" — the mechanistic overlay. Could Laozi have '
                        f"pointed at it?",
                        line.strip(), "CLAUDE.md · the overlay watchlist",
                        {"mechanistic-register"},
                    ))
    return out


def rule_status_coherence(chapters, **_):
    out = []
    for ch in chapters:
        empty = (not ch.verse) or all(UNTRANSLATED_MARKER in t for _, t in ch.verse)
        if ch.status == "drafted" and empty:
            out.append(Finding("status-coherence", ERROR, ch.number, 1,
                               "status: drafted, but the Translation block is empty",
                               "", "CLAUDE.md · per-chapter frontmatter", {"status-coherence"}))
        if ch.status == "untranslated" and not empty:
            out.append(Finding("status-coherence", ERROR, ch.number, 1,
                               "status: untranslated, but the Translation block has verse",
                               "", "CLAUDE.md · per-chapter frontmatter", {"status-coherence"}))
        if ch.number != int(ch.path.stem):
            out.append(Finding("status-coherence", ERROR, ch.number, 2,
                               f"frontmatter says chapter: {ch.number}, filename says "
                               f"{ch.path.stem}", "", "", {"status-coherence"}))
        if not ch.source_rows:
            out.append(Finding("status-coherence", ERROR, ch.number, 1,
                               "no Source rows parsed — the table shape may have changed",
                               "", "", {"status-coherence"}))
    return out


def rule_flexion_chapter(chapters, terms, **_):
    """A declared flexion must name chapters its character actually stands in.

    Flexions are the one place a lock says "this other English, but only here,"
    so the "here" has to be checkable — that is the whole reason they are data
    and not a sentence inside `render:`. Two ways to get it wrong, both cheap
    to catch and neither capable of a false positive:

      * the flexion names a chapter the character is absent from, so the
        licence points at nothing;
      * the flexion's English is also on the term's own forbidden list, which
        would have the build fighting the entry.

    Deliberately NOT checked: whether the flexion's English appears outside its
    chapters. Inflection and insertion make that unanswerable — 保's *keep safe*
    reads "keep the Tao safe" at ch 15 and "keeps safe those who are not" at 62,
    so a scan for the bare string finds legitimate lines everywhere. That is the
    thin-translation trap, prototyped and declined at ~90% false positives
    (WORKLIST T5-1), and this checker's whole value is that it never cries wolf.
    """
    present = {ch.number for ch in chapters}
    out = []
    for t in terms:
        for f in t.flexions:
            eng = f.get("english", "")
            if not f.get("chapters"):
                out.append(Finding("flexion-chapter", ERROR, 0, 1,
                                   f'{t.term}: flexion "{eng}" names no chapters — '
                                   f"a flexion scoped to nowhere is a second render",
                                   "", t.entry, {"flexion-chapter"}))
            for n in f.get("chapters", []):
                if n in present and n not in t.chapters:
                    out.append(Finding("flexion-chapter", ERROR, n, 1,
                                       f'{t.term}: flexion "{eng}" is licensed at ch {n}, '
                                       f"but {'/'.join(t.characters)} is not in that chapter",
                                       "", t.entry, {"flexion-chapter"}))
            if any(eng.lower() == x.lower() for x in t.forbidden):
                out.append(Finding("flexion-chapter", ERROR, 0, 1,
                                   f'{t.term}: "{eng}" is both a declared flexion and '
                                   f"forbidden — the entry contradicts itself",
                                   "", t.entry, {"flexion-chapter"}))
    return out


def rule_source_drift(chapters, **_):
    """source/chinese.md is derived. This is what keeps that claim honest."""
    base = load_base_text()
    out = []
    for ch in chapters:
        if ch.number not in base:
            continue
        theirs = re.sub(r"\s", "", base[ch.number])
        if ch.chinese != theirs:
            out.append(Finding(
                "source-drift", ERROR, ch.number, 1,
                f"this chapter's Source rows ({len(ch.chinese)} chars) disagree with "
                f"source/chinese.md ({len(theirs)} chars) — chapters/ is the source of "
                f"truth, so rebuild chinese.md from it",
                "", "CLAUDE.md · source of truth", {"source-drift"},
            ))
    return out


_DASH = re.compile(r"[—–]")


def rule_em_dash(chapters, **_):
    """Inventory only. CLAUDE.md is explicit that removing these is a
    chapter-by-chapter conversation, not a sweep — so this never fails a build."""
    out = []
    for ch in chapters:
        for ln, line in ch.verse:
            if _DASH.search(line):
                out.append(Finding(
                    "em-dash", INFO, ch.number, ln,
                    "dash in the verse — check whether it strands a subject "
                    "(some are good; ch 44's are)",
                    line.strip(), "notes/translation.md · typography", {"em-dash"},
                ))
    return out


def rule_repeated_formula(chapters, verbose=False, **_):
    """Verbatim Chinese must produce verbatim English.

    No reader holding ch 30 in mind is also holding ch 55, which is how
    物壯則老 came to be rendered two different ways in the two chapters that
    share it. Advisory rather than error: verse lines do not reliably align to
    source rows (only 27 of 62 drafted chapters align), so the tool can point
    at the pair but cannot prove which English line answers which Chinese one.
    """
    # Index whole comma-segments, not arbitrary n-grams. The formulas of this
    # text are its segments — 物壯則老, 不道早已, 是謂玄德 — and indexing below
    # that granularity produces fragments no translator ever rendered as a unit
    # (難得之貨 inside 不貴難得之貨), each of which becomes a warning about
    # nothing. It also gives each formula a literal gloss of its own to match
    # against, which arbitrary n-grams cannot have.
    index = defaultdict(set)
    segments = defaultdict(dict)        # chapter -> {segment: gloss}
    for ch in chapters:
        if not ch.drafted:
            continue
        for row in ch.source_rows:
            cn = _split_segments(row.chinese)
            en = _split_segments(row.literal)
            for i, seg in enumerate(cn):
                seg = "".join(_cjk_runs(seg))
                if len(seg) < 4:
                    continue
                index[seg].add(ch.number)
                gloss = en[i] if len(en) == len(cn) else row.literal
                segments[ch.number].setdefault(seg, gloss)

    # Shared by 2-3 chapters is a formula; shared by more is grammar (是以聖人).
    maximal = {g: chs for g, chs in index.items() if 2 <= len(chs) <= 3}

    by_number = {c.number: c for c in chapters}

    def words(text):
        # The literal glosses carry bracketed pinyin annotations — "growing/
        # leading \[zhang\] but not dominating \[zai\]" — which are apparatus,
        # not gloss, and never appear in the verse.
        text = re.sub(r"\\?\[[^\]]*\\?\]", " ", text)
        return {_stem(w) for w in re.findall(r"[a-z']+", text.lower())
                if w not in _STOPWORDS}

    def similarity(a, b):
        """Containment, not overlap: how much of the SHORTER line the longer holds.

        A formula often shares its verse line with the clause after it — ch 29
        packs 為者敗之，執者失之 onto one line where ch 64 gives 為者敗之 a line of
        its own — and whole-line overlap scored that as a 60% mismatch between
        two identical renderings. All seven of this rule's warnings on
        2026-09-24 were that artifact (WORKLIST T5-2). Asking whether one line
        is inside the other still needs no alignment, which three earlier
        attempts showed cannot be had. A one-word line falls back to overlap,
        since a single word is inside almost anything.
        """
        wa, wb = words(a), words(b)
        if not (wa | wb):
            return 1.0
        if min(len(wa), len(wb)) >= 2:
            return len(wa & wb) / min(len(wa), len(wb))
        return len(wa & wb) / len(wa | wb)

    def best_pair(a, b):
        """The most similar line in a and in b, and how similar they are.

        Deliberately asks nothing about which line renders which row. Three
        attempts at that inference all failed for structural reasons: the verse
        does not align to the source rows, the literal glosses speak pre-lock
        English (玄德 is glossed "dark/mysterious virtue/power" where the verse
        correctly reads "profound integrity"), and a line may be restructured
        wholesale. So the question becomes one that needs no alignment: two
        chapters sharing a verbatim Chinese segment should have two lines that
        look alike. If their closest pair still looks nothing alike, say so.
        """
        best = (0.0, "", "")
        for _, la in a.verse:
            if not words(la):
                continue
            for _, lb in b.verse:
                if not words(lb):
                    continue
                s = similarity(la, lb)
                if s > best[0]:
                    best = (s, la.strip(), lb.strip())
        return best

    out = []
    for g, chs in sorted(maximal.items(), key=lambda kv: (-len(kv[0]), sorted(kv[1]))):
        nums = sorted(chs)
        present = [by_number[n] for n in nums if n in by_number and by_number[n].drafted]
        if len(present) < 2:
            continue

        worst = (1.0, None, None, "", "")
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                score, la, lb = best_pair(a, b)
                if score < worst[0]:
                    worst = (score, a.number, b.number, la, lb)
        score, na, nb, la, lb = worst
        if na is None:
            continue
        divergent = score < 0.7

        msg = (f"{g} appears in chapters {', '.join(str(n) for n in nums)} — "
               f"verbatim Chinese, so the English must match")
        if divergent:
            msg += (f". Closest lines in {na} and {nb} agree only {score:.0%}, so the "
                    f"formula is rendered two ways or dropped in one of them:"
                    f"\n           ch {na}: {la or '(nothing comparable)'}"
                    f"\n           ch {nb}: {lb or '(nothing comparable)'}")
        elif verbose:
            msg += f" — matching at {score:.0%}: {la}"
        out.append(Finding(
            "repeated-formula", WARN if divergent else INFO,
            nums[0], 1, msg, "", "CLAUDE.md · internal consistency",
            {"repeated-formula", g}, set(nums),
        ))
    return out


def rule_unlogged_variant(**_):
    """A meaning-bearing fork must have a logged decision somewhere.

    This is the rule the sources library exists to make possible. Ch 21 was
    drafted over a reversed chronology in both Mawangdui silks with nothing
    recording that a choice had been made; Ch 25 was drafted with a king the
    oldest witnesses do not have. Neither was dishonest — nobody knew. Once the
    apparatus exists, translating over a known fork without saying so becomes a
    build failure rather than an accident.
    """
    out = []
    for v in load_variants():
        if not v.meaning_bearing:
            continue
        if not v.logged or v.logged.lower() == "false":
            out.append(Finding(
                "unlogged-variant", ERROR, v.chapter, 1,
                f"{v.base} in {v.line} diverges meaningfully in the witnesses "
                f"({', '.join(sorted(v.witnesses)) or 'editorial'}), and no decision "
                f"is logged — record it in notes/manuscript.md and set `logged:`",
                "", "sources/variants.yaml", {"unlogged-variant"},
            ))
            continue
        target = ROOT / v.logged
        if target.exists() and f"Ch {v.chapter} " not in target.read_text(encoding="utf-8"):
            out.append(Finding(
                "unlogged-variant", WARN, v.chapter, 1,
                f"{v.base} claims to be logged in {v.logged}, but that file has no "
                f'"Ch {v.chapter}" entry',
                "", "sources/variants.yaml", {"unlogged-variant"},
            ))
        if v.our_call == "undecided":
            out.append(Finding(
                "unlogged-variant", WARN, v.chapter, 1,
                f"{v.base} is recorded as undecided — the verse has to say something, "
                f"so decide it or note why it is left open",
                "", "sources/variants.yaml", {"unlogged-variant"},
            ))
    return out


def rule_shaloms_call_unparsed(calls, **_):
    """Every dated heading in the ledger must have produced a call.

    A suspension the tool cannot see is a suspension that silently does not
    apply — and worse, a stale call that can never be caught. This once happened
    for real: a heading written `## DATE · rule (label)` failed a regex that
    required the line to end at the rule id, and a three-call ledger parsed as
    one with no complaint. Count the headings and compare.
    """
    from lib.corpus import CALLS
    if not CALLS.exists():
        return []
    headings = re.findall(r"^## \d{4}-\d{2}-\d{2}\s*·", CALLS.read_text(encoding="utf-8"), re.M)
    if len(headings) == len(calls):
        return []
    return [Finding(
        "shaloms-call-unparsed", ERROR, 0, 1,
        f"process/shaloms-call.md has {len(headings)} dated entries but "
        f"{len(calls)} parsed — a call the tool cannot see is a rule that is "
        f"silently not suspended. Check the heading format: "
        f"`## YYYY-MM-DD · rule-id`",
        "", "process/shaloms-call.md", {"shaloms-call-unparsed"},
    )]


def rule_stale_shaloms_call(calls, **_):
    """An override that has outlived its condition must be renewed or retired."""
    out = []
    for call in calls:
        if call.retired or call.standing:
            continue
        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", call.until)
        if m and date(*(int(x) for x in m.groups())) < date.today():
            out.append(Finding(
                "stale-shaloms-call", ERROR, 0, 1,
                f'shaloms-call "{call.rule}" expired on {m.group(0)} — renew it or '
                f"retire it",
                "", "process/shaloms-call.md", {"stale-shaloms-call"},
            ))
    return out


COMMENTARY_NAMES = {"wangbi": "王弼", "heshanggong": "河上公", "hanfeizi": "韓非"}


def rule_unmarked_lemma(**_):
    """A vendored lemma that differs from our base text must carry its `*`.

    Every file in sources/commentaries/ opens by promising the reader that
    "Lemmas marked `*` differ from our base text." That promise is the only
    thing telling a reader which quotations are evidence of a different text and
    which are simply our own text quoted back. Unenforced, it lapsed silently:
    the Han Feizi importer wrote 35 divergent quotations as exact lemmas, so the
    file asserted an agreement it had never tested — and 韓非 died in 233 BCE,
    which makes his quotations the oldest witness to the Laozi there is.

    Folding is shared with the importer (lib/corpus.fold) precisely so that a
    printing variant such as 爲/為 is never reported as a textual one.
    """
    out, base = [], {n: fold(t) for n, t in load_base_text().items()}
    root = ROOT / "sources" / "commentaries"
    if not root.is_dir():
        return out
    for src_dir in sorted(root.iterdir()):
        if not src_dir.is_dir():
            continue
        who = COMMENTARY_NAMES.get(src_dir.name, src_dir.name)
        for path in sorted(src_dir.glob("[0-9]*.md")):
            try:
                chapter = int(path.stem)
            except ValueError:
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
                m = re.match(r"^\*\*(.+?)\*\*(\s*`\*`)?\s*$", line)
                if not m:
                    continue
                lemma, marked = m.group(1), bool(m.group(2))
                probe = fold(lemma)
                if not probe:
                    continue
                agrees = probe in base.get(chapter, "")
                if not agrees and not marked:
                    out.append(Finding(
                        "unmarked-lemma", ERROR, chapter, i,
                        f"{who} quotes {lemma[:28]} which differs from our base text, "
                        f"but the lemma carries no `*` — the file header promises "
                        f"divergent lemmas are marked",
                        "", str(path.relative_to(ROOT)), {"unmarked-lemma"},
                    ))
                elif agrees and marked:
                    out.append(Finding(
                        "unmarked-lemma", WARN, chapter, i,
                        f"{who}'s lemma {lemma[:28]} is marked `*` but agrees with our "
                        f"base text once printing variants are folded",
                        "", str(path.relative_to(ROOT)), {"unmarked-lemma"},
                    ))
    return out


RULES = {
    "forbidden-rendering": rule_forbidden_rendering,
    "sage-pronoun": rule_sage_pronoun,
    "devotional-capitalization": rule_devotional_capitalization,
    "mechanistic-register": rule_mechanistic_register,
    "status-coherence": rule_status_coherence,
    "flexion-chapter": rule_flexion_chapter,
    "source-drift": rule_source_drift,
    "repeated-formula": rule_repeated_formula,
    "em-dash": rule_em_dash,
    "unlogged-variant": rule_unlogged_variant,
    "unmarked-lemma": rule_unmarked_lemma,
    "stale-shaloms-call": rule_stale_shaloms_call,
    "shaloms-call-unparsed": rule_shaloms_call_unparsed,
}


# ------------------------------------------------------------------- the runner

def run(chapter_filter=None, rule_filter=None, verbose=False, drafted_only=False):
    chapters = list(load_chapters(only=chapter_filter).values())
    if drafted_only:
        chapters = [c for c in chapters if c.drafted]
    terms = load_terms()
    calls = load_calls()

    suppressed = {c.rule: c for c in calls if not c.retired and c.rule in RULES}

    findings = []
    for name, fn in RULES.items():
        if rule_filter and name not in rule_filter:
            continue
        findings += fn(chapters=chapters, terms=terms, calls=calls, verbose=verbose)

    by_number = {c.number: c for c in chapters}

    kept = []
    for f in findings:
        call = suppressed.get(f.rule)
        if call and call.covers(f.chapter):
            continue
        for number in sorted(f.waivable_in()):
            ch = by_number.get(number)
            if not ch:
                continue
            match = next((w for w in ch.waivers if w.rule in f.tags), None)
            if match:
                match.used = True
                f.waived_by = match
                break
        kept.append(f)

    # A waiver that no longer matches anything is itself a finding, so the
    # chapter files self-clean. (shaloms-call inverts this on purpose: an
    # unused override is fine, an expired one is not.)
    #
    # Only ever computed on a COMPLETE run. A filtered run cannot know whether a
    # waiver was used: --rule leaves the rule that would consume it unrun, and
    # --chapter drops cross-chapter findings filed under a number outside the
    # filter — so both would report a live waiver as dead.
    complete = chapter_filter is None and rule_filter is None
    if complete:
        for ch in chapters:
            for w in ch.waivers:
                if not w.used:
                    kept.append(Finding(
                        "unused-waiver", ERROR, ch.number, w.line_no,
                        f'lock-ok waiver for "{w.rule}" matches nothing — the finding '
                        f"it excused is gone, so remove the waiver",
                        w.note, "process/shaloms-call.md · waivers", {"unused-waiver"},
                    ))

    return kept, suppressed, calls


def report(findings, suppressed, calls, min_severity=INFO, verbose=False):
    threshold = SEVERITY_ORDER[min_severity]
    live = [f for f in findings if not f.waived_by
            and SEVERITY_ORDER[f.severity] <= threshold]

    icons = {ERROR: "✗", WARN: "!", INFO: "·"}
    counts = defaultdict(int)
    for f in live:
        counts[f.severity] += 1

    by_chapter = defaultdict(list)
    for f in live:
        by_chapter[f.chapter].append(f)

    for number in sorted(by_chapter):
        rows = sorted(by_chapter[number], key=lambda f: (SEVERITY_ORDER[f.severity], f.line_no))
        head = f"chapter {number}" if number else "repository"
        print(f"\n{head}")
        for f in rows:
            loc = f"{f.line_no}" if f.line_no else "-"
            print(f"  {icons[f.severity]} {loc:>4}  {f.rule}")
            print(f"           {f.message}")
            if f.line:
                print(f"           › {f.line}")
            if f.ref:
                print(f"           see {f.ref}")

    def plural(n, word):
        return f"{n} {word}" if n == 1 else f"{n} {word}s"

    waived = [f for f in findings if f.waived_by]
    print("\n" + "─" * 72)
    print(f"{plural(counts[ERROR], 'error')} · {plural(counts[WARN], 'warning')} · "
          f"{counts[INFO]} info"
          + (f" · {len(waived)} waived" if waived else ""))

    if suppressed:
        names = ", ".join(sorted(suppressed))
        print(f"{len(suppressed)} rule(s) suspended by shaloms-call ({names}) "
              f"— see process/shaloms-call.md")
    conditional = [c for c in calls
                   if not c.retired and not c.standing
                   and not re.search(r"\d{4}-\d{2}-\d{2}", c.until)]
    for c in conditional:
        print(f'  · "{c.rule}" until: {c.until} — condition, not a date; review by hand')

    return counts[ERROR]


def staged_chapters():
    try:
        out = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    nums = {int(m.group(1)) for line in out.split("\n")
            if (m := re.match(r"chapters/(\d+)\.md$", line.strip()))}
    return nums or None


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--chapter", type=int, action="append", help="limit to chapter N")
    p.add_argument("--rule", action="append", help="limit to one rule")
    p.add_argument("--severity", choices=[ERROR, WARN, INFO], default=INFO,
                   help="lowest severity to report (default: info)")
    p.add_argument("--staged", action="store_true",
                   help="only staged chapters, errors only, skipping untranslated "
                        "(what the pre-commit hook runs)")
    p.add_argument("--json", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true",
                   help="include the verse of each repeated-formula group")
    args = p.parse_args()

    chapter_filter = set(args.chapter) if args.chapter else None
    severity = args.severity
    drafted_only = False

    if args.staged:
        staged = staged_chapters()
        if staged is None:
            print("no chapters staged — nothing to check")
            return 0
        chapter_filter = staged if chapter_filter is None else chapter_filter & staged
        severity = ERROR
        drafted_only = True

    findings, suppressed, calls = run(chapter_filter, set(args.rule) if args.rule else None,
                                      args.verbose, drafted_only)

    if args.json:
        print(json.dumps({
            "findings": [f.as_dict() for f in findings],
            "suspended": sorted(suppressed),
        }, indent=2, ensure_ascii=False))
        return 1 if any(f.severity == ERROR and not f.waived_by for f in findings) else 0

    errors = report(findings, suppressed, calls, severity, args.verbose)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
