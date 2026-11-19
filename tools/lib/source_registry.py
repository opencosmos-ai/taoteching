"""Resolve authored source identities, manuscript evidence, and citations."""

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
import re
import unicodedata
from urllib.parse import urlsplit

from .corpus import GLOSSARY, ROOT, load_chapters, load_guodian, load_variants, parse_frontmatter
from .flat_yaml import records

CATALOGUE = ROOT / "sources" / "sources.yaml"
POLICY = ROOT / "sources" / "PROVENANCE.md"
BLOB = "https://github.com/opencosmos-ai/taoteching/blob/main/"
KINDS = {"base", "excavated", "transmitted", "commentary", "dictionary", "context",
         "translation", "reference"}
EDITORIAL = {"various": "Editions reported collectively",
             "wangbi_collation": "Siku collation note"}
CHOICES = {"base", "punctuation", "undecided"}
EXTENTS = {"complete", "opening", "middle", "end", "split"}
SOURCE_FIELDS = {"id", "name", "kind", "use", "date", "years", "found", "holds",
                 "editions", "why_not_stored", "via", "url", "scan", "citation_debt",
                 "display_edition", "short_name"}
EDITION_FIELDS = {"id", "title", "publisher", "year", "url"}
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LATIN = re.compile(r"[A-Za-z]")
TONE_MARKS = frozenset("\u0304\u0301\u030c\u0300")


def han(text):
    """Include supplementary-plane and compatibility ideographs."""
    return any(unicodedata.name(char, "").startswith(
        ("CJK UNIFIED IDEOGRAPH", "CJK COMPATIBILITY IDEOGRAPH", "CJK RADICAL", "KANGXI RADICAL"))
        for char in text)


def fail(location, message):
    raise ValueError(f"{location}: {message}")


def english(text, location):
    if not LATIN.search(text) or han(text):
        fail(location, "expected readable Roman-alphabet display text")


def check_url(value, location, *, local=False):
    parts = urlsplit(value)
    if parts.scheme in {"http", "https"} and parts.hostname and not any(c.isspace() for c in value):
        return
    if local and not parts.scheme and not parts.netloc:
        check_path(parts.path, location, parts.fragment)
        return
    fail(location, f"invalid source URL {value!r}")


def check_path(value, location, anchor=""):
    from build_principles import headings_in

    path = ROOT / value
    if not value or not path.resolve().is_relative_to(ROOT) or not path.exists():
        fail(location, f"missing or invalid local path {value!r}")
    if anchor and (not path.is_file() or anchor not in (headings_in(path) or ())):
        fail(location, f"missing heading {value}#{anchor}")


def imported_sources():
    """Read stored metadata offline and compare each importer's common projection."""
    from import_commentary import COMMENTARIES, SOURCES
    from import_shuowen import HEADER, OUT

    if {p.name for p in COMMENTARIES.iterdir() if p.is_dir()} != SOURCES.keys():
        fail(COMMENTARIES, "stored commentary directories differ from importer bindings")
    out = {}
    for ident, src in SOURCES.items():
        directory = COMMENTARIES / ident
        common = {key: src[key] for key in
                  ("work", "author", "author_dates", "edition", "edition_dates", "punctuation", "rights")}
        common.update(transcription=src["host"], obtained=src["url"],
                      imported_by="tools/import_commentary.py")
        paths = sorted(directory.glob("*.md"))
        if not paths:
            fail(directory, "importer binding has no chapters")
        chapters = {}
        for path in paths:
            actual = parse_frontmatter(path.read_text(encoding="utf-8"), path) or {}
            check_import(path, common, actual)
            chapter = actual.get("chapter", "")
            if not chapter.isdigit() or not 1 <= int(chapter) <= 81 or path.stem != f"{int(chapter):03}":
                fail(path, "chapter frontmatter and stored filename disagree")
            chapters[int(chapter)] = path.relative_to(ROOT).as_posix()
        out[ident] = ("commentary", directory, common, chapters)
    common = parse_frontmatter(HEADER)
    common = {key: value for key, value in common.items() if key not in {"covers", "flexions"}}
    actual = parse_frontmatter(OUT.read_text(encoding="utf-8"), OUT) or {}
    check_import(OUT, common, actual)
    if set(OUT.parent.glob("*.md")) != {OUT}:
        fail(OUT.parent, "unexpected stored dictionary files")
    out["shuowen"] = ("dictionary", OUT, common, {})
    return out


def check_import(path, expected, actual):
    mismatched = [key for key, value in expected.items() if actual.get(key) != value]
    if mismatched:
        fail(path, "frontmatter differs from importer for " + ", ".join(mismatched))


def years_for(date_label):
    """Derive sortable years only when the display date is numerically explicit."""
    match = re.fullmatch(r"(?:c\. )?(\d{1,4})(?:\s*[–-]\s*(?:c\. )?(\d{1,4}))?\s*(BCE|CE)?", date_label)
    if not match:
        return None
    first, last, era = match.groups()
    sign = -1 if era == "BCE" else 1
    return sorted([sign * int(first), sign * int(last or first)])


def edition_rows(rows, location):
    out = {}
    for row in rows:
        ident = row.get("id", "")
        if not ID.fullmatch(ident) or ident in out:
            fail(location, "invalid or duplicate edition ID")
        english(row.get("title", ""), location)
        if "publisher" in row:
            english(row["publisher"], location)
        if "year" in row:
            if not row["year"].isdigit():
                fail(location, "edition year must be numeric")
            row = {**row, "year": int(row["year"])}
        if "url" in row:
            check_url(row["url"], location)
        out[ident] = row
    return out


def edition_order(edition):
    return "year" not in edition, edition.get("year", 0), edition["id"]


@dataclass
class ResolvedSources:
    records: dict
    editions: dict
    chapters: dict
    entries: dict
    forks: dict
    totals: dict


def catalogue(imported, chapters, guodian):
    from build_principles import headings_in

    sources, editions, locations = {}, {}, {}
    policy_headings = headings_in(POLICY)
    for location, row in records(CATALOGUE, SOURCE_FIELDS, blocks={"editions": EDITION_FIELDS},
                                 lists={"holds", "years"}):
        ident = row.get("id", "")
        if not ID.fullmatch(ident) or ident in sources:
            fail(location, "invalid or duplicate source ID")
        locations[ident] = location
        kind, use = row.get("kind"), row.get("use")
        chapter_list = []
        coverage = {"chapters": chapter_list}
        editions[ident] = edition_rows(row.get("editions", []), location)
        view = {key: row[key] for key in ("id", "name", "date", "found", "via", "url", "scan",
                                          "citation_debt", "short_name") if key in row}
        holds = row.get("holds", [])
        if ident in imported:
            forbidden = {"kind", "use", "holds", "editions", "url"}
            metadata = imported[ident][2]
            if forbidden & row.keys() or ("work_english" in metadata and "name" in row):
                fail(location, "stored-source metadata belongs to the importer")
            kind, path, metadata, bound = imported[ident]
            holds = [path.relative_to(ROOT).as_posix()]
            use = "stored"
            if bound:
                coverage.update(chapters=sorted(bound), total=len(chapters))
            if kind == "dictionary":
                from import_shuowen import OUT
                count = sum(1 for line in OUT.read_text(encoding="utf-8").splitlines()
                            if re.match(r"^\|\s*[^|]+\|", line) and han(line.split("|")[1]))
                coverage["items"] = count
            if "work_english" in metadata:
                view["name"] = metadata["work_english"]
            view.update(author_dates=metadata.get("author_dates", ""), url=metadata["obtained"],
                        rights=metadata["rights"])
            title = row.get("display_edition", "")
            english(title, location)
            edition = {"id": "imported", "title": title, "url": metadata["obtained"]}
            if metadata.get("edition_dates"):
                edition["date"] = metadata["edition_dates"]
            editions[ident]["imported"] = edition
        elif ident == "base":
            if kind != "base" or holds or use or "display_edition" in row:
                fail(location, "base identity must bind to the manuscript")
            holds = ["source/chinese.md"]
            coverage.update(chapters=sorted(chapters), total=len(chapters))
            use = "stored"
        elif kind not in KINDS - {"base"} or use not in {"facts", "consulted"} or "display_edition" in row:
            fail(location, "invalid source kind or use")
        if ident == "guodian":
            coverage.update(chapters=sorted(guodian), total=len(chapters))
        policy = row.get("why_not_stored", "the-admission-rules")
        if policy not in policy_headings or (kind == "excavated" and use != "stored" and
                                             "why_not_stored" not in row):
            fail(location, f"invalid or missing provenance-policy heading {policy!r}")
        for relative in holds:
            check_path(relative, location)
        for field in ("name", "short_name", "found", "author_dates"):
            if field in view or field == "name":
                english(view.get(field, ""), location)
        if "date" in view and not view["date"].isdigit():
            english(view["date"], location)
        for field in ("url", "scan"):
            if field in view:
                check_url(view[field], location)
        if "years" in row:
            try:
                years = [int(value) for value in row["years"]]
            except ValueError:
                fail(location, "years must be a numeric range")
            if len(years) != 2 or years != sorted(years):
                fail(location, "years must be an ascending pair")
        else:
            years = years_for(view.get("date", view.get("author_dates", "")))
        if years:
            view["years"] = years
        view.update(kind=kind, use=use, holds=holds, coverage=coverage,
                    policy=f"sources/PROVENANCE.md#{policy}")
        sources[ident] = view
    missing = ({"base", "guodian"} | imported.keys()) - sources.keys()
    if missing:
        fail(CATALOGUE, f"missing required source bindings: {', '.join(sorted(missing))}")
    return sources, editions, locations


def pairing(text, pinyin, gloss, location):
    if not text.strip():
        fail(location, "empty reading text")
    english(gloss, location)
    if han(text) and (not LATIN.search(unicodedata.normalize("NFD", pinyin)) or
                      han(pinyin) or not TONE_MARKS.intersection(unicodedata.normalize("NFD", pinyin))):
        fail(location, "reading needs its own tone-marked pinyin")
    return {"text": text, "english": gloss, "gloss": "authored", **({"pinyin": pinyin} if pinyin else {})}


def resolve(chapters=None, guodian=None):
    from check_worklist import CLOSED, DONE, WORKLIST, parse

    chapters = load_chapters() if chapters is None else chapters
    guodian = load_guodian() if guodian is None else guodian
    imported = imported_sources()
    sources, editions, locations = catalogue(imported, chapters, guodian)
    open_rows = {row.id: row for row in parse(WORKLIST.read_text(encoding="utf-8"))
                 if row.status != DONE}
    closed_rows = {row.id: row for row in parse(CLOSED.read_text(encoding="utf-8"))
                   if row.status == DONE}
    usages = defaultdict(set)
    fork_ids, chapter_ids, entry_ids = defaultdict(set), defaultdict(set), defaultdict(set)
    pending, pending_via, confirmed = Counter(), Counter(), Counter()
    readings_count = 0

    def chain(source, via, location):
        current, result = via or sources.get(source, {}).get("via"), []
        seen = {source}
        while current:
            if current not in sources or current in seen:
                fail(location, f"unknown or cyclic intermediary {current!r} for {source!r}")
            result.append(current)
            seen.add(current)
            current = sources[current].get("via")
        return result

    def reference(record, location, *, editorial=False):
        source = record.get("source", "")
        if source not in sources and not (editorial and source in EDITORIAL):
            fail(location, f"unknown source {source!r}")
        result = {**record, "chain": chain(source, record.get("via"), location)}
        for key in ("edition", "confirmed_edition"):
            if key in record and record[key] not in editions.get(source, {}):
                fail(location, f"unknown {key} {record[key]!r} for {source}")
        if "url" in record:
            check_url(record["url"], location, local=True)
        for key in ("confirmation", "annotation"):
            if key in record:
                english(record[key], location)
        for key in ("locator", "confirmed_locator"):
            locator = record.get(key, "")
            if re.match(r"^(sources|glossary|chapters|notes|source|process)/", locator):
                local_path, _, fragment = locator.partition("#")
                check_path(local_path, location, fragment)
            elif locator and not re.fullmatch(r"[\d.:[\]–-]+", locator):
                english(locator, location)
        for intermediary in result["chain"]:
            usages[intermediary].add("intermediary")
        if source in sources:
            usages[source].add("citation" if not editorial else "apparatus")
        return result

    def resolve_citations(citations, location, *, entry_path=None):
        seen, result = set(), []
        for citation in citations:
            if not (citation.get("locator") or citation.get("url")):
                fail(location, "citation needs a locator or passage URL")
            if entry_path and citation.get("at"):
                check_path(entry_path, location, citation["at"])
            key = tuple(sorted(citation.items()))
            if key in seen:
                fail(location, "duplicate citation")
            seen.add(key)
            result.append(reference(citation, location))
        return sorted(result, key=lambda ref: (ref["source"], ref.get("locator", ""), ref.get("url", "")))

    for ident, source in sources.items():
        source["chain"] = chain(ident, None, locations[ident])

    entries = {}
    for path in sorted(GLOSSARY.glob("*.md")):
        if path.name in {"INDEX.md", "TRIAGE.md"}:
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"), path) or {}
        status = fm.get("refs_status", "incomplete")
        if status not in {"incomplete", "complete"}:
            fail(path, "invalid refs_status")
        refs = resolve_citations(fm.get("refs", []), path, entry_path=path.relative_to(ROOT).as_posix())
        for record in refs:
            entry_ids[record["source"]].add(path.stem)
        entries[path.stem] = {"refs_status": status, "refs": refs}

    chapter_data, forks = {}, {}
    if set(guodian) - chapters.keys():
        fail("Guodian inventory", "attestation outside the manuscript")
    for number in sorted(chapters):
        row = guodian.get(number)
        if row and (row.extent not in EXTENTS or not row.bundles or not row.units or
                    any(unit.partition(".")[0] not in row.bundles for unit in row.units)):
            fail("Guodian inventory", f"chapter {number} has invalid extent or slip units")
        commentary = [{"source": ident, "path": binding[3][number]}
                      for ident, binding in sorted(imported.items()) if number in binding[3]]
        chapter_data[number] = {
            "attestation": {"source": "guodian", "present": row is not None,
                            "extent": row.extent if row else None,
                            "bundles": row.bundles if row else [], "units": row.units if row else []},
            "commentary": commentary,
        }
    for v in load_variants():
        if v.legacy:
            fail(v.location, "source export requires structured readings")
        ident = v.id
        if v.our_call not in CHOICES | v.witnesses.keys():
            fail(v.location, f"invalid call {v.our_call!r}")
        base = pairing(v.base, v.base_pinyin, v.base_english, v.location)
        resolved = []
        for reading in sorted(v.readings, key=lambda item: item.source):
            location = f"{v.location} [{reading.source}]"
            paired = pairing(reading.text, reading.pinyin, reading.english, location)
            evidence = {key: value for key, value in asdict(reading).items()
                        if value and key not in {"text", "pinyin", "english"}}
            record = reference(evidence, location, editorial=True)
            verification = reading.verification
            work = open_rows.get(reading.confirm)
            completed = (reading.confirmed_edition, reading.confirmed_locator, reading.confirmed_on,
                         reading.confirmation)
            if reading.confirm and reading.confirm not in open_rows and reading.confirm not in closed_rows:
                fail(location, f"unknown print-check row {reading.confirm!r}")
            if verification == "pending-print":
                if not record["chain"] or not reading.locator or not work or (
                        work.chapters and v.chapter not in work.chapters):
                    fail(location, "pending print check needs an intermediary, locator, and relevant open row")
                pending[reading.source] += 1
                pending_via[record["chain"][0]] += 1
            elif verification == "confirmed-print":
                if not all(completed) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reading.confirmed_on):
                    fail(location, "confirmed print check needs edition, locator, ISO date, and outcome")
                try:
                    date.fromisoformat(reading.confirmed_on)
                except ValueError:
                    fail(location, "invalid print-check date")
                confirmed[reading.source] += 1
            elif verification != "unassessed" or reading.confirm:
                fail(location, "invalid verification status or worklist reference")
            if verification != "confirmed-print" and any(completed):
                fail(location, "confirmation evidence requires confirmed-print status")
            if reading.source in sources:
                fork_ids[reading.source].add(ident)
                chapter_ids[reading.source].add(v.chapter)
            resolved.append({**paired, **record})
            readings_count += 1
        refs = resolve_citations(v.refs, v.location)
        for citation in refs:
            fork_ids[citation["source"]].add(ident)
            chapter_ids[citation["source"]].add(v.chapter)
        forks[ident] = {"chapter": v.chapter, "base": base, "our_call": v.our_call,
                       "meaning_bearing": v.meaning_bearing, "readings": resolved, "refs": refs,
                       "line": v.line, "note": v.note, "logged": v.logged,
                       "followed": "witness" if v.followed_a_witness else "base"}

    for ident, record in sources.items():
        if record["use"] == "stored" or record["holds"]:
            usages[ident].add("binding")
        if record["use"] == "consulted":
            usages[ident].add("consulted")
    for ident in tuple(usages):
        for intermediary in sources[ident]["chain"]:
            usages[intermediary].add("intermediary")
    for ident, record in sources.items():
        debt = record.get("citation_debt")
        used = usages.get(ident, set())
        if record["use"] == "consulted" and ({"citation", "apparatus"} & used or debt):
            fail(locations[ident], "consulted sources cannot carry a quotation or citation debt")
        if debt:
            row = open_rows.get(debt)
            if used or not row or not any(
                    name.casefold() in row.item.casefold()
                    for name in (ident, ident.replace("-", " "), record["name"])):
                fail(locations[ident], "citation debt must name a relevant open row for an otherwise orphaned source")
        elif not used:
            fail(locations[ident], f"orphan source {ident!r}")
        record.update(forks=sorted(fork_ids[ident]), chapters=sorted(chapter_ids[ident]),
                      entries=sorted(entry_ids[ident]), pending_print=pending[ident],
                      pending_via=pending_via[ident], confirmed_print=confirmed[ident])
    counts = Counter(record["use"] for record in sources.values())
    totals = {"sources": len(sources), "stored": counts["stored"], "facts": counts["facts"],
              "pending_print": sum(pending.values()), "confirmed_print": sum(confirmed.values()),
              "readings": readings_count,
              "citation_debt": sum("citation_debt" in r for r in sources.values()),
              "entries": len(entries), "incomplete_entries": sum(
                  e["refs_status"] == "incomplete" for e in entries.values())}
    return ResolvedSources(sources, editions, chapter_data, entries, forks, totals)
