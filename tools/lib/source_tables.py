"""SQLite projections of the validated source registry and the reader contract."""

import json

from .source_registry import EDITORIAL, edition_order

SCHEMA = """
CREATE TABLE source (
    id TEXT PRIMARY KEY,
    record TEXT NOT NULL
);
CREATE TABLE source_edition (
    source TEXT NOT NULL REFERENCES source(id),
    id TEXT NOT NULL,
    record TEXT NOT NULL,
    PRIMARY KEY (source, id)
);
CREATE TABLE source_glossary_entry (
    slug TEXT PRIMARY KEY,
    status TEXT NOT NULL
);
CREATE TABLE source_citation (
    slug TEXT NOT NULL REFERENCES source_glossary_entry(slug),
    seq INTEGER NOT NULL,
    source TEXT NOT NULL REFERENCES source(id),
    record TEXT NOT NULL,
    PRIMARY KEY (slug, seq)
);
CREATE TABLE source_chapter_commentary (
    chapter INTEGER NOT NULL REFERENCES chapter(n),
    source TEXT NOT NULL REFERENCES source(id),
    path TEXT NOT NULL,
    PRIMARY KEY (chapter, source)
);
CREATE TABLE source_total (
    id TEXT PRIMARY KEY,
    count INTEGER NOT NULL
);
CREATE TABLE source_editorial_label (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);
"""

EVIDENCE = ("annotation", "via", "edition", "locator", "url", "confirm", "confirmed_edition",
            "confirmed_locator", "confirmed_on", "confirmation", "verification")


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def store(cur, registry):
    cur.executemany("INSERT INTO source VALUES (?, ?)",
                    [(ident, encode(record)) for ident, record in registry.records.items()])
    cur.executemany("INSERT INTO source_edition VALUES (?, ?, ?)", [
        (source, ident, encode(record)) for source, editions in registry.editions.items()
        for ident, record in editions.items()])
    cur.executemany("INSERT INTO source_glossary_entry VALUES (?, ?)", [
        (slug, entry["refs_status"]) for slug, entry in registry.entries.items()])
    cur.executemany("INSERT INTO source_citation VALUES (?, ?, ?, ?)", [
        (slug, index, ref["source"], encode(ref)) for slug, entry in registry.entries.items()
        for index, ref in enumerate(entry["refs"])])
    cur.executemany("INSERT INTO source_chapter_commentary VALUES (?, ?, ?)", [
        (chapter, item["source"], item["path"]) for chapter, data in registry.chapters.items()
        for item in data["commentary"]])
    cur.executemany("INSERT INTO source_total VALUES (?, ?)", sorted(registry.totals.items()))
    cur.executemany("INSERT INTO source_editorial_label VALUES (?, ?)", sorted(EDITORIAL.items()))
    for ident, source in registry.records.items():
        if source["kind"] not in {"base", "commentary", "excavated", "transmitted"} and not source["forks"]:
            continue
        coverage = source["coverage"]
        covered, total = len(coverage["chapters"]), coverage.get("total")
        editions = "; ".join(edition["title"] for edition in
                             sorted(registry.editions[ident].values(), key=edition_order))
        years = source.get("years", [None, None])
        cur.execute("""
            INSERT INTO witness (id, name_en, kind, date_low, date_high, edition,
                                 rights, is_full_text, coverage_note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (ident, source["name"], source["kind"], *years, editions,
                  source.get("rights", source["policy"]),
                  int(source["use"] == "stored" and total is not None and covered == total),
                  f"{covered} of {total} chapter files or attestations" if total else None))

    columns = ("variant_group", "chapter", "line", "base_reading", "base_pinyin", "base_english",
               "base_gloss", "witness_id", "witness_reading", "witness_pinyin", "witness_english",
               "witness_gloss", "chain", "meaning_bearing", "our_call", "followed", "note", "logged",
               *EVIDENCE)
    sql = f"INSERT INTO variant ({', '.join(columns)}) VALUES ({', '.join('?' for _ in columns)})"
    for group, fork in registry.forks.items():
        base = fork["base"]
        for witness in fork["readings"] or [{}]:
            cur.execute(sql, (
                group, fork["chapter"], fork["line"], base["text"], base.get("pinyin"),
                base["english"], base["gloss"], witness.get("source"), witness.get("text"),
                witness.get("pinyin"), witness.get("english"), witness.get("gloss"),
                encode(witness.get("chain", [])), int(fork["meaning_bearing"]), fork["our_call"],
                fork["followed"], fork["note"], fork["logged"], *(witness.get(k) for k in EVIDENCE),
            ))


def published_sources(conn):
    records = {}
    for ident, record in conn.execute("SELECT id, record FROM source ORDER BY id"):
        records[ident] = {**json.loads(record), "editions": []}
    for source, record in conn.execute("SELECT source, record FROM source_edition ORDER BY source, id"):
        records[source]["editions"].append(json.loads(record))
    for record in records.values():
        record["editions"].sort(key=edition_order)
    return {"records": list(records.values()), "totals": dict(
        conn.execute("SELECT id, count FROM source_total ORDER BY id"))}


def published_citations(conn):
    entries = {slug: {"refs_status": status, "refs": []}
               for slug, status in conn.execute("SELECT slug, status FROM source_glossary_entry ORDER BY slug")}
    for slug, record in conn.execute("SELECT slug, record FROM source_citation ORDER BY slug, seq"):
        entries[slug]["refs"].append(json.loads(record))
    return entries


def published_chapters(conn, cards, legacy_chapters):
    chapters = {}
    for n, present, extent, bundles, units in conn.execute("""
        SELECT n, guodian_attested, guodian_extent, guodian_bundles, guodian_units
        FROM chapter ORDER BY n
    """):
        if bool(present) != bool(legacy_chapters[n][3]):
            raise ValueError(f"chapter {n}: Guodian attestation and legacy chapter flag disagree")
        chapters[n] = {"attestation": {
            "source": "guodian", "present": bool(present), "extent": extent,
            "bundles": bundles.split(", ") if bundles else [], "units": json.loads(units),
        }, "commentary": [], "forks": []}

    for chapter, source, path in conn.execute("""
        SELECT chapter, source, path FROM source_chapter_commentary ORDER BY chapter, source
    """):
        chapters[chapter]["commentary"].append({"source": source, "path": path})
    forks = {}
    sql = f"""
        SELECT chapter, variant_group, base_reading, base_pinyin, base_english, base_gloss,
               our_call, meaning_bearing, witness_id, witness_reading, witness_pinyin,
               witness_english, witness_gloss, chain, {', '.join(EVIDENCE)}
        FROM variant ORDER BY chapter, id
    """
    for row in conn.execute(sql):
        n, group, base, pin, gloss, derivation, our_call, meaning, source, reading, rpin, rgloss, rderived, chain, *evidence = row
        if group not in forks:
            paired = {"text": base, "english": gloss, "gloss": derivation}
            if pin:
                paired["pinyin"] = pin
            fork = {"id": group, "base": paired, "our_call": our_call,
                    "meaning_bearing": bool(meaning), "readings": []}
            forks[group] = fork
            chapters[n]["forks"].append(fork)
        if source is not None:
            record = {"source": source, "text": reading, "english": rgloss, "gloss": rderived,
                      "chain": json.loads(chain), "cards": list(dict.fromkeys(c for c in reading if c in cards))}
            if rpin:
                record["pinyin"] = rpin
            record.update({k: v for k, v in zip(EVIDENCE, evidence) if v is not None})
            forks[group]["readings"].append(record)
    return chapters
