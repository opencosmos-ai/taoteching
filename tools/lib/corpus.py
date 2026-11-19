#!/usr/bin/env python3
"""
corpus.py — one reader for the whole manuscript.

Every tool in tools/ reads the repo through this module, so that there is
exactly one understanding of what a chapter file is. Forking a second parser
is the drift the harness exists to prevent.

What it holds:

    Chapter          one chapters/NNN.md file, parsed
    SourceRow        one row of a chapter's Source table
    Pairing          one line of a chapter's Alignment: English line → source rows
    alignment_errors()  why a chapter's authored alignment cannot be trusted
    load_chapters()  all 81, keyed by number
    load_terms()     glossary/terms.yaml, the locks as data
    load_calls()     process/shaloms-call.md, the overrides in effect
    parse_frontmatter()  the YAML-ish frontmatter reader (also used by
                         build_index.py, which imports it from here)

Stdlib only, deliberately: this runs in a pre-commit hook and must not
depend on anything a fresh clone lacks.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .flat_yaml import inline_map, records, scalar

ROOT = Path(__file__).resolve().parent.parent.parent
CHAPTERS = ROOT / "chapters"
GLOSSARY = ROOT / "glossary"
SOURCE = ROOT / "source" / "chinese.md"
CALLS = ROOT / "process" / "shaloms-call.md"
VARIANTS = ROOT / "sources" / "variants.yaml"
GUODIAN = ROOT / "sources" / "guodian-inventory.yaml"

# A chapter's Source table marks its header row with 原文 ("original text")
# and its alignment row with colons and dashes. Both are skipped.
_HEADER_CELL = "原文"
_RULE_CHARS = set("|: -")

UNTRANSLATED_MARKER = "*(untranslated)*"
CITATION_FIELDS = {"source", "via", "edition", "locator", "url"}


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text, path="frontmatter"):
    """Read the YAML frontmatter of a markdown file. Returns None if absent.

    Deliberately minimal rather than a real YAML parser — the frontmatter in
    this repo is a flat map of scalars and inline lists, plus lists of
    inline mappings for glossary coverage, flexions, and references. Anything richer
    should be reconsidered rather than parsed.
    """
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data, covers, flexions = {}, [], []
    block = None
    for number, line in enumerate(m.group(1).split("\n"), 2):
        location = f"{path}:{number}"
        if line.startswith("refs:"):
            if "refs" in data or line[5:].strip() not in ("", "[]"):
                raise ValueError(f"{location}: refs requires a single block of mappings")
            data["refs"] = []
            block = "refs" if not line[5:].strip() else "empty_refs"
            continue
        if block in {"refs", "empty_refs"} and line.startswith(" "):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if block == "empty_refs" or not line.startswith("  - "):
                raise ValueError(f"{location}: expected a refs mapping")
            data["refs"].append(inline_map(line[4:], location, CITATION_FIELDS | {"at"}))
            continue
        if line.startswith("refs_status:"):
            if "refs_status" in data:
                raise ValueError(f"{location}: duplicate refs_status")
            data["refs_status"] = scalar(line.split(":", 1)[1], location)
            block = None
            continue
        # Both blocks are read only in their block form. Anything else used to
        # parse to an empty list without a word: `covers: ["柔"]` in ruo-弱.md
        # dropped 柔's lock on the floor from 2026-08-26 until 2026-10-14, while
        # the entry's prose said it was locked. A shape this parser cannot read
        # is an error, never an empty list.
        for name in ("covers", "flexions"):
            if line.startswith(f"{name}:") and line[len(name) + 1:].strip() not in ("", "[]"):
                raise ValueError(
                    f"`{name}:` must be a block of `- {{ ... }}` mappings, not "
                    f"inline: {line.strip()!r}")
        if line.startswith("covers:"):
            block = "covers"
            continue
        if line.startswith("flexions:"):
            block = "flexions"
            continue
        if block and line.strip().startswith("- {"):
            if block == "covers":
                c = re.search(r'char:\s*"([^"]*)"', line)
                r = re.search(r'render:\s*"([^"]*)"', line)
                if not (c and r):
                    raise ValueError(f"a `covers:` entry needs char and render: {line.strip()!r}")
                covers.append((c.group(1), r.group(1)))
            else:
                e = re.search(r'english:\s*"([^"]*)"', line)
                ch = re.search(r'chapters:\s*\[([^\]]*)\]', line)
                why = re.search(r'why:\s*"([^"]*)"', line)
                if e:
                    flexions.append({
                        "english": e.group(1),
                        "chapters": [int(x) for x in re.findall(r"\d+", ch.group(1))] if ch else [],
                        "why": why.group(1) if why else "",
                    })
            continue
        block = None
        km = re.match(r"^(\w+):\s*(.*)$", line)
        if not km:
            continue
        key, raw = km.group(1), km.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [v.strip().strip('"') for v in inner.split(",") if v.strip()]
        else:
            data[key] = raw.strip('"')
    data["covers"] = covers
    data["flexions"] = flexions
    return data


# -------------------------------------------------------------------- records

@dataclass
class SourceRow:
    """One line of Chinese with its pinyin and literal gloss."""
    chinese: str
    pinyin: str
    literal: str
    block: int
    line_no: int          # 1-indexed line in the chapter file


@dataclass
class Pairing:
    """One line of a chapter's `## Alignment`: an English line and the source
    rows it renders. `rows` is None when the line could not be read."""
    verse: int
    rows: list
    line_no: int


@dataclass
class Waiver:
    """A `lock-ok` comment in a chapter's Notes, excusing one finding."""
    rule: str
    note: str
    line_no: int
    used: bool = False


@dataclass
class Chapter:
    number: int
    path: Path
    status: str
    retrofit: list
    verse: list                     # (line_no, text) — non-blank verse lines only
    source_rows: list               # SourceRow
    notes: str
    waivers: list = field(default_factory=list)
    alignment: list = field(default_factory=list)  # Pairing — empty unless authored

    @property
    def drafted(self):
        return self.status == "drafted"

    @property
    def chinese(self):
        """Every character of this chapter's Chinese, whitespace stripped."""
        return re.sub(r"\s", "", "".join(r.chinese for r in self.source_rows))

    @property
    def verse_text(self):
        return "\n".join(t for _, t in self.verse)

    def has(self, term):
        """Does this chapter's own Chinese contain this character or compound?

        This is the evidence gate. A rule about English never fires unless the
        character licensing it is present in *this* chapter — which is what
        keeps 常 (cháng, constant) from being blamed for a line rendering
        長 (cháng, long).
        """
        return bool(term) and term in self.chinese

    def __str__(self):
        return f"ch {self.number}"


# --------------------------------------------------------------------- loading

def _split_sections(text):
    """Return {heading: body} for the `## ` sections of a chapter file."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def _line_index(text):
    """Map each line's content to its 1-indexed position in the file."""
    return {i: line for i, line in enumerate(text.split("\n"), 1)}


def _parse_source(body, offset):
    """Parse the pipe tables under a chapter's Source section."""
    rows, block = [], 0
    for i, line in enumerate(body.split("\n")):
        s = line.strip()
        if s.startswith("### Block"):
            m = re.search(r"(\d+)", s)
            block = int(m.group(1)) if m else block + 1
            continue
        if not s.startswith("|"):
            continue
        if _HEADER_CELL in s or set(s) <= _RULE_CHARS:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        while len(cells) < 3:
            cells.append("")
        rows.append(SourceRow(cells[0], cells[1], cells[2], block, offset + i))
    return rows


_PAIRING = re.compile(r"^(\d+):\s*(.+)$")
_ROWS = re.compile(r"^(\d+)(?:\s*[–-]\s*(\d+))?$")


def _parse_alignment(body, offset):
    """Parse a chapter's `## Alignment`: one line per English line, in order,
    naming the source rows it renders — `1: 1–2`, `5: 7`, `12: 14, 16`.

    Lenient on purpose. A line that cannot be read becomes a Pairing with no
    rows, so alignment_errors() names it instead of the parser dropping it.
    """
    out = []
    for i, line in enumerate(body.split("\n")):
        s = line.strip()
        if not s or s.startswith("<!--"):
            continue
        m = _PAIRING.match(s)
        if not m:
            out.append(Pairing(0, None, offset + i))
            continue
        rows = []
        for part in m.group(2).split(","):
            r = _ROWS.match(part.strip())
            if not r:
                rows = None
                break
            lo, hi = int(r.group(1)), int(r.group(2) or r.group(1))
            rows.extend(range(lo, hi + 1))
        out.append(Pairing(int(m.group(1)), rows, offset + i))
    return out


def alignment_errors(ch):
    """Why a chapter's English and Chinese cannot be paired line by line, as messages.

    Where the counts agree, the pairing is 1:1 and needs nothing written. Where
    they differ, the chapter must carry an `## Alignment`. An alignment is shown
    to readers as a fact, so it must be whole: every English line names the rows
    it renders, in order, and every source row is named by at least one English
    line. Adding or cutting a line on either side breaks that, which is how a
    stale alignment is caught.
    """
    verse, rows = len(ch.verse), len(ch.source_rows)
    if not ch.alignment:
        if verse and rows and verse != rows:
            return [f"{ch.path.name}: {verse} English lines against {rows} source rows, "
                    f"so it needs an `## Alignment` naming the rows each English line "
                    f"renders (AGENTS.md)"]
        return []
    errs = []
    for p in ch.alignment:
        where = f"{ch.path.name}:{p.line_no}"
        if p.rows is None:
            errs.append(f"{where}: cannot read this line; write it as `verse: rows`, e.g. `1: 1–2`")
        elif not p.rows:
            errs.append(f"{where}: English line {p.verse} names no source rows")
        else:
            for r in p.rows:
                if not 1 <= r <= rows:
                    errs.append(f"{where}: source row {r} does not exist (the chapter has {rows})")
    got = [p.verse for p in ch.alignment if p.rows is not None]
    if got != list(range(1, len(got) + 1)):
        errs.append(f"{ch.path.name}: English lines must be numbered 1, 2, 3… in order")
    if len(ch.alignment) != verse:
        errs.append(f"{ch.path.name}: the alignment has {len(ch.alignment)} lines "
                    f"and the translation has {verse}")
    named = {r for p in ch.alignment for r in (p.rows or [])}
    missing = [r for r in range(1, rows + 1) if r not in named]
    if missing:
        errs.append(f"{ch.path.name}: no English line renders source row"
                    f"{'s' if len(missing) > 1 else ''} {', '.join(map(str, missing))}")
    return errs


def _parse_waivers(body, offset):
    waivers = []
    for i, line in enumerate(body.split("\n")):
        m = re.search(r"<!--\s*lock-ok:\s*([^\s·|]+)\s*[·|]?\s*(.*?)-->", line)
        if m:
            waivers.append(Waiver(m.group(1).strip(), m.group(2).strip(), offset + i))
    return waivers


def load_chapter(path):
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text) or {}
    sections = _split_sections(text)

    lines = text.split("\n")

    def offset_of(heading):
        for i, line in enumerate(lines, 1):
            if line.strip() == f"## {heading}":
                return i
        return 0

    verse_body = sections.get("Translation", "")
    verse_offset = offset_of("Translation")
    verse = []
    for i, line in enumerate(verse_body.split("\n")):
        if line.strip():
            verse.append((verse_offset + i, line.rstrip()))

    source_rows = _parse_source(sections.get("Source", ""), offset_of("Source"))
    notes_body = sections.get("Notes", "")

    retrofit = fm.get("retrofit", [])
    if isinstance(retrofit, str):
        retrofit = [retrofit] if retrofit and retrofit != "[]" else []

    return Chapter(
        number=int(fm.get("chapter", path.stem)),
        path=path,
        status=fm.get("status", ""),
        retrofit=retrofit,
        verse=verse,
        source_rows=source_rows,
        notes=notes_body,
        waivers=_parse_waivers(notes_body, offset_of("Notes")),
        alignment=_parse_alignment(sections.get("Alignment", ""), offset_of("Alignment")),
    )


def load_chapters(only=None):
    """All chapters, keyed by number. `only` limits to a set of numbers."""
    out = {}
    for path in sorted(CHAPTERS.glob("*.md")):
        if not re.fullmatch(r"\d+", path.stem):
            continue
        n = int(path.stem)
        if only and n not in only:
            continue
        out[n] = load_chapter(path)
    return out


# ---------------------------------------------------- glyph folding, shared
#
# Lives here rather than in import_commentary.py because check_locks.py's
# unmarked-lemma rule must fold exactly as the importer folded, or it would
# flag printing variants as textual ones. Two copies would drift apart.

# Include CJK Extension B: the Siku form of 玄 is 𤣥 (U+24465), outside the BMP.
# Omitting it silently deletes the character, which turned 玄德 into 徳 and
# 玄牝 into 牝 on the first pass through this data.
CJK = r"[㐀-鿿豈-﫿\U00020000-\U0002ebef]"

# Orthographic variants: the Siku printing's glyph forms for characters our base
# text writes differently. Harvested empirically by aligning every non-matching
# lemma line against our base text and collecting single-character
# substitutions, then filtered by hand to forms that are the SAME WORD.
# Applied for matching only — the vendored text always keeps the original glyph.
ORTHOGRAPHIC = {
    "徳": "德", "强": "強", "争": "爭", "𤣥": "玄", "衆": "眾", "静": "靜",
    "髙": "高", "盗": "盜", "徃": "往", "逺": "遠", "兊": "兌", "竒": "奇",
    "虚": "虛", "緜": "綿", "乗": "乘", "㣲": "微", "舍": "捨", "饑": "飢",
    "巳": "已", "絶": "絕", "况": "況", "賔": "賓", "氾": "汎", "隐": "隱",
    "隂": "陰", "沒": "没", "寳": "寶", "刋": "刊", "㝠": "冥", "㫖": "旨",
    "劔": "劍", "隣": "鄰", "耶": "邪",   # 耶/邪 are interchangeable final particles
    # Further forms from the Song woodblock behind the Heshang Gong edition.
    "爲": "為", "乆": "久", "户": "戶", "奥": "奧", "愼": "慎", "剋": "克",
    "踈": "疏", "柰": "奈", "䘮": "喪", "𥙷": "補", "轝": "輿", "田": "畋",
    # From the Wikisource 韓非子 transcription. Printing variants only: 脩/修 is
    # deliberately NOT mapped, being a lexical choice rather than a glyph form.
    "晩": "晚", "牗": "牖",
}

def cjk(s):
    return "".join(re.findall(CJK, s))


def fold(s):
    """Normalize Siku glyph forms, for comparison only.

    Strips 〔…〕 first. Those are the Siku compilers' collation notes, and
    folding their characters into the comparison probe makes the lemma they
    annotate fail to match — which silently reclassified 揣而梲之 (a real
    variant against our 揣而銳之) as commentary on the first run.
    """
    return "".join(ORTHOGRAPHIC.get(c, c) for c in cjk(re.sub(r"〔[^〕]*〕", "", s)))



def load_base_text():
    """source/chinese.md, keyed by chapter number. Derived, not authoritative."""
    if not SOURCE.exists():
        return {}
    parts = re.split(r"^## Chapter (\d+)$", SOURCE.read_text(encoding="utf-8"), flags=re.M)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


# ---------------------------------------------- where a glossary term stands
#
# The one rule for where a glossary term stands in the text and how often.
# glossary/INDEX.md's chapter lists, terms.yaml's, and the `where` of every
# entry in data/atlas-export.json all come from term_where(), and the Library
# on opencosmos.ai reads that `where` rather than counting for itself. Two
# copies of this rule disagreed once: INDEX counted only the first half of a
# pairing, so 我 & 吾 stood in 7 chapters there and 19 in the Library
# (2026-11-15). Count nowhere else.

def term_parts(term):
    """What a glossary term names: "無 & 有" → ["無", "有"], "天地" → ["天地"]."""
    return [p.strip() for p in term.split("&") if p.strip()]


def term_where(term, chapters):
    """[["ch.line", n], …]: every line of the Chinese a term stands in, and how often.

    `chapters` is load_chapters(). A line is a source row, numbered from 1 as
    the export's `lines` are. Every half of a pairing counts, so 我 & 吾 stands
    wherever 吾 does. Each part is counted on its own, without overlaps, so 天
    counts the 天 inside 天地. Counting within a line means a compound never
    matches across a line break.
    """
    parts = term_parts(term)
    out = []
    for n in sorted(chapters):
        for i, row in enumerate(chapters[n].source_rows, 1):
            k = sum(row.chinese.count(p) for p in parts)
            if k:
                out.append([f"{n}.{i}", k])
    return out


def term_chapters(where):
    """The chapters a term_where() result stands in, in order."""
    return sorted({int(k.split(".")[0]) for k, _ in where})


# ----------------------------------------------------------------------- terms

@dataclass
class Term:
    term: str
    pinyin: str
    render: str
    forbidden: list
    chapters: list
    status: str
    entry: str
    case: str = "insensitive"       # per-rule case policy; see WORKLIST.md lesson 2
    match: str = "substring"        # substring catches "eternally"; lesson 1
    severity: str = "error"
    # A lock's secondary Englishes, each scoped to named chapters. Data, not
    # prose: `render:` used to carry these as a sentence ("keep safe — and bare
    # keep where the object is not cherished (ch 9 alone)"), which no tool could
    # read, so --english could not tell a licensed flexion from a breach.
    flexions: list = field(default_factory=list)

    def flexion_for(self, phrase):
        """The flexion whose English is this phrase, or None."""
        return next((f for f in self.flexions
                     if f.get("english", "").lower() == phrase.lower()), None)

    def licenses(self, phrase, chapter):
        """Is this English licensed for this chapter — as the render, or a flexion?

        The primary render is licensed everywhere the character stands. A
        flexion is licensed only in the chapters it names, which is the whole
        point of writing it down.
        """
        f = self.flexion_for(phrase)
        return chapter in f["chapters"] if f else True

    @property
    def characters(self):
        """The characters this lock governs. "無 & 有" governs both."""
        return term_parts(self.term)


def load_terms():
    """Parse glossary/terms.yaml. Generated from entry frontmatter — never hand-edited."""
    path = GLOSSARY / "terms.yaml"
    if not path.exists():
        return []
    terms, cur = [], None
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("- term:"):
            if cur:
                terms.append(cur)
            cur = {}
        if cur is None:
            continue
        m = re.match(r"^[- ]\s*(\w+):\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            cur[key] = [v.strip().strip('"') for v in inner.split(",") if v.strip()]
        else:
            cur[key] = raw.strip('"')
    if cur:
        terms.append(cur)

    # flexions are inline mappings under a `flexions:` key; the scalar loop
    # above cannot see them, so they are read from the raw text per block.
    flex_by_term = {}
    for blk in path.read_text(encoding="utf-8").split("\n- term:")[1:]:
        name = re.match(r'\s*"?([^"\n]*)"?', blk).group(1).strip()
        rows = []
        for line in blk.split("\n"):
            if not line.strip().startswith("- {"):
                continue
            e = re.search(r'english:\s*"([^"]*)"', line)
            ch = re.search(r'chapters:\s*\[([^\]]*)\]', line)
            why = re.search(r'why:\s*"([^"]*)"', line)
            if e:
                rows.append({"english": e.group(1),
                             "chapters": [int(x) for x in re.findall(r"\d+", ch.group(1))] if ch else [],
                             "why": why.group(1) if why else ""})
        if rows:
            flex_by_term[name] = rows

    out = []
    for t in terms:
        chapters = [int(c) for c in t.get("chapters", []) if str(c).strip().isdigit()]
        out.append(Term(
            term=t.get("term", ""),
            pinyin=t.get("pinyin", ""),
            render=t.get("render", ""),
            forbidden=t.get("forbidden", []),
            chapters=chapters,
            status=t.get("status", "open"),
            entry=t.get("entry", ""),
            case=t.get("case", "insensitive"),
            match=t.get("match", "substring"),
            severity=t.get("severity", "error"),
            flexions=flex_by_term.get(t.get("term", ""), []),
        ))
    return out


# ------------------------------------------------------------- shaloms-call

@dataclass
class Call:
    """A rule Shalom has set aside. See process/shaloms-call.md."""
    rule: str
    source: str
    scope: str
    until: str
    reason: str
    date: str
    retired: bool = False

    @property
    def standing(self):
        return self.until.strip().lower() == "standing"

    def covers(self, chapter_number=None):
        """Is this call in force here? Scope is `repo`, or `chapter: N`, or a list."""
        if self.retired:
            return False
        scope = self.scope.strip()
        if scope in ("", "repo", "all"):
            return True
        if chapter_number is None:
            return False
        nums = {int(n) for n in re.findall(r"\d+", scope)}
        return chapter_number in nums


def load_calls():
    """Parse process/shaloms-call.md. Entries after `## Retired calls` are retired.

    The heading is `## YYYY-MM-DD · rule-id`, and anything after the rule id is
    a human label — "(sources library)", "— retired, condition met". Trailing
    text is tolerated deliberately: requiring the heading to end at the rule id
    once made a three-call ledger parse as one, silently, which is the worst
    possible failure for a file whose job is to make suspensions visible.
    """
    if not CALLS.exists():
        return []
    text = CALLS.read_text(encoding="utf-8")
    retired_at = text.find("## Retired calls")
    calls = []
    for m in re.finditer(r"^## (\d{4}-\d{2}-\d{2})\s*·\s*(\S+).*?$(.*?)(?=^## |\Z)",
                         text, re.M | re.S):
        date, rule, body = m.group(1), m.group(2), m.group(3)
        fields = {}
        key = None
        for line in body.split("\n"):
            fm = re.match(r"^(\w+):\s*(.*)$", line)
            if fm:
                key = fm.group(1)
                val = fm.group(2).strip()
                fields[key] = "" if val == ">" else val
            elif key and line.strip() and line.startswith(("  ", "\t")):
                fields[key] = (fields.get(key, "") + " " + line.strip()).strip()
        calls.append(Call(
            rule=rule,
            source=fields.get("source", ""),
            scope=fields.get("scope", "repo"),
            until=fields.get("until", ""),
            reason=fields.get("reason", ""),
            date=date,
            retired=retired_at != -1 and m.start() > retired_at,
        ))
    return calls


# -------------------------------------------------------------------- variants

@dataclass(frozen=True)
class Reading:
    source: str
    text: str
    pinyin: str = ""
    english: str = ""
    annotation: str = ""
    via: str = ""
    edition: str = ""
    locator: str = ""
    url: str = ""
    verification: str = "unassessed"
    confirm: str = ""
    confirmed_edition: str = ""
    confirmed_locator: str = ""
    confirmed_on: str = ""
    confirmation: str = ""


@dataclass
class Variant:
    """One divergence between our base text and an older witness.

    A fact about a text, not a transcription of one — see sources/PROVENANCE.md
    for why the excavated manuscripts are recorded this way and never copied.
    """
    chapter: int
    line: str
    base: str
    witnesses: dict
    meaning_bearing: bool
    our_call: str
    note: str
    logged: str
    readings: list = field(default_factory=list)
    base_pinyin: str = ""
    base_english: str = ""
    location: str = ""
    legacy: bool = False
    id: Optional[int] = None
    refs: list = field(default_factory=list)

    @property
    def followed_a_witness(self):
        return self.our_call not in ("base", "punctuation", "undecided", "")

    def __str__(self):
        others = " · ".join(f"{k}: {v}" for k, v in sorted(self.witnesses.items()))
        return f"ch {self.chapter} · {self.base} ({others or 'editorial'})"


def load_variants(chapter=None):
    """Parse sources/variants.yaml. Hand-rolled, like everything else here."""
    if not VARIANTS.exists():
        return []
    _, out = parse_variants(VARIANTS.read_text(encoding="utf-8"), VARIANTS)
    if chapter is not None:
        out = [v for v in out if v.chapter == chapter]
    return out


def fork_number(value, field, location):
    if not re.fullmatch(r"[1-9][0-9]{0,15}", value) or int(value) >= 2**53:
        raise ValueError(f"{location}: {field} must be a positive safe integer")
    return int(value)


def parse_variants(text, path, *, require_counter=True):
    """Read the counter and records from an apparatus snapshot."""
    next_id, counter_at = None, str(path)
    in_header = True
    for line, raw in enumerate(text.splitlines(), 1):
        if raw.startswith("- "):
            in_header = False
        if not re.match(r"^# next-fork-id\b", raw):
            continue
        counter_at = f"{path}:{line}"
        label, separator, value = raw.partition(":")
        if label != "# next-fork-id" or not separator or not in_header:
            raise ValueError(f"{counter_at}: expected '# next-fork-id: N' in the apparatus header")
        if next_id is not None:
            raise ValueError(f"{counter_at}: duplicate next-fork-id")
        next_id = fork_number(value.strip(), "next-fork-id", counter_at)

    out = []
    seen_ids = set()
    required = {"chapter", "line", "base", "meaning_bearing", "our_call", "note", "logged"}
    fields = required | {"id", "witnesses", "readings", "refs", "base_pinyin", "base_english"}
    for location, cur in records(path, fields, text=text, maps={"witnesses"}, folded={"note"},
                                 blocks={"readings": Reading.__dataclass_fields__, "refs": CITATION_FIELDS}):
        legacy = "witnesses" in cur
        if not required <= cur.keys() or legacy == ("readings" in cur):
            raise ValueError(f"{location}: expected all variant fields and exactly one reading form")
        ident = None
        if not legacy or "id" in cur:
            ident = fork_number(cur.get("id", ""), "fork id", location)
            if ident in seen_ids:
                raise ValueError(f"{location}: duplicate fork id {ident}")
            seen_ids.add(ident)
        if not cur["chapter"].isdigit() or not 1 <= int(cur["chapter"]) <= 81:
            raise ValueError(f"{location}: expected a chapter from 1 to 81")
        if cur["meaning_bearing"] not in {"true", "false"}:
            raise ValueError(f"{location}: meaning_bearing must be true or false")
        readings = []
        for reading in cur.get("readings", []):
            if not {"source", "text"} <= reading.keys():
                raise ValueError(f"{location}: each reading needs a source and text")
            readings.append(Reading(**reading))
        witnesses = cur.get("witnesses", {r.source: r.text for r in readings})
        if len(witnesses) != len(readings) and not legacy:
            raise ValueError(f"{location}: duplicate source in readings")
        out.append(Variant(
            chapter=int(cur["chapter"]), line=cur["line"], base=cur["base"], witnesses=witnesses,
            meaning_bearing=cur["meaning_bearing"] == "true", our_call=cur["our_call"],
            note=" ".join(cur["note"].split()), logged=cur["logged"], readings=readings,
            refs=cur.get("refs", []),
            base_pinyin=cur.get("base_pinyin", ""), base_english=cur.get("base_english", ""),
            location=location, legacy=legacy, id=ident,
        ))
    if next_id is None and require_counter and (not out or any(not v.legacy for v in out)):
        raise ValueError(f"{path}: missing next-fork-id")
    if next_id is not None and next_id <= max(seen_ids, default=0):
        raise ValueError(f"{counter_at}: next-fork-id must exceed every assigned fork ID")
    return next_id, out


# --------------------------------------------------------------------- guodian

@dataclass
class GuodianEntry:
    """What the oldest witness carries for one chapter — an inventory fact.

    Never a text. The Guodian slips are excluded from sources/ as transcriptions
    (PROVENANCE.md); what chapters sit on which slips, in what order, is a fact
    about an excavated object and is recorded instead.
    """
    chapter: int
    bundles: list
    extent: str
    units: list
    note: str

    @property
    def partial(self):
        return self.extent not in ("complete", "")

    def __str__(self):
        where = "+".join(self.bundles)
        return f"ch {self.chapter} · bundle {where} · {self.extent}"


def load_guodian(chapter=None):
    """Parse sources/guodian-inventory.yaml. Hand-rolled, like the rest."""
    if not GUODIAN.exists():
        return {} if chapter is None else None
    out, cur, key = {}, None, None

    def flush():
        if not cur or "chapter" not in cur:
            return
        n = int(cur["chapter"])
        out[n] = GuodianEntry(
            chapter=n,
            bundles=_split_list(cur.get("bundles", "")),
            extent=cur.get("extent", ""),
            units=_split_list(cur.get("units", "")),
            note=" ".join(cur.get("note", "").split()),
        )

    for raw in GUODIAN.read_text(encoding="utf-8").split("\n"):
        if raw.lstrip().startswith("#"):
            continue
        if raw.startswith("- "):
            flush()
            cur, key = {}, None
            raw = "  " + raw[2:]
        if cur is None:
            continue
        stripped = raw.strip()
        if not stripped:
            continue
        if raw.startswith("    ") and key:          # folded continuation
            cur[key] = (cur.get(key, "") + " " + stripped).strip()
            continue
        if ":" in stripped:
            k, _, v = stripped.partition(":")
            key = k.strip()
            v = v.strip()
            cur[key] = "" if v == ">" else v
    flush()
    return out if chapter is None else out.get(chapter)


def _split_list(val):
    """Split `[A, B]` into ['A', 'B']."""
    inner = val.strip().lstrip("[").rstrip("]").strip()
    return [p.strip() for p in inner.split(",") if p.strip()]
