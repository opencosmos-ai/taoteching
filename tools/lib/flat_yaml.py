"""The deliberately small YAML subset used for authored source data."""

import json
import re


def scalar(value, location):
    value = value.strip()
    if value.startswith('"'):
        try:
            result = json.loads(value)
        except ValueError as exc:
            raise ValueError(f"{location}: malformed quoted value: {value!r}") from exc
        return result
    if value.startswith("'"):
        if not re.fullmatch(r"'(?:[^']|'')*'", value):
            raise ValueError(f"{location}: malformed quoted value: {value!r}")
        return value[1:-1].replace("''", "'")
    if (not value or value in {"|", ">"} or any(char in value for char in '{}[]"') or
            re.search(r"(^|\s)#|:\s", value)):
        raise ValueError(f"{location}: expected a scalar, got {value!r}")
    return value


def split_inline(value, delimiters, location):
    value = value.strip()
    if not value.startswith(delimiters[0]) or not value.endswith(delimiters[1]):
        raise ValueError(f"{location}: expected {delimiters} delimiters: {value!r}")
    inner = value[1:-1].strip()
    if not inner:
        return []

    parts = []
    quote = None
    escaped = False
    start = 0
    for index, char in enumerate(inner):
        if escaped:
            escaped = False
        elif quote:
            if char == "\\" and quote == '"':
                escaped = True
            elif char == quote:
                quote = None
        elif char in "\"'" and (not inner[start:index].strip()
                                 or inner[start:index].rstrip().endswith(":")):
            quote = char
        elif char == ",":
            parts.append(inner[start:index].strip())
            start = index + 1
        elif char in "{}[]":
            raise ValueError(f"{location}: nested inline values are unsupported")
    parts.append(inner[start:].strip())
    if quote or not all(parts):
        raise ValueError(f"{location}: malformed inline value: {value!r}")
    return parts


def inline_map(value, location, allowed=None):
    result = {}
    for part in split_inline(value, "{}", location):
        key, separator, raw = part.partition(":")
        key = key.strip()
        if not separator or not re.fullmatch(r"[a-zA-Z][\w-]*", key):
            raise ValueError(f"{location}: invalid mapping member: {part!r}")
        if key in result:
            raise ValueError(f"{location}: duplicate field {key!r}")
        if allowed is not None and key not in allowed:
            raise ValueError(f"{location}: unknown field {key!r}")
        result[key] = scalar(raw, location)
    return result


def records(path, fields, *, blocks=None, lists=(), maps=(), folded=()):
    """Yield each top-level record with its authored location."""
    blocks = blocks or {}
    record = None
    key = None
    block = is_folded = False
    for line, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        location = f"{path}:{line}"
        if raw.startswith("- "):
            if record is not None:
                yield origin, record
            origin, record = location, {}
            raw = "  " + raw[2:]
        match = re.fullmatch(r" {2}([a-zA-Z][\w-]*):[ \t]*(.*)", raw)
        if record is not None and match:
            key, value = match.groups()
            if key not in fields or key in record:
                raise ValueError(f"{location}: unknown or duplicate field {key!r}")
            is_folded = key in folded and value == ">"
            block = key in blocks and not value
            if key in blocks and value in ("", "[]"):
                record[key] = []
            elif key in blocks:
                raise ValueError(f"{location}: {key} requires a block of mappings")
            elif key in lists:
                record[key] = [scalar(part, location) for part in split_inline(value, "[]", location)]
            elif key in maps:
                record[key] = inline_map(value, location)
            else:
                record[key] = "" if is_folded else scalar(value, location)
        elif record is not None and block and raw.startswith("    - "):
            record[key].append(inline_map(raw[6:], location, blocks[key]))
        elif record is not None and raw.startswith("    ") and is_folded:
            record[key] = f"{record[key]} {raw.strip()}".strip()
        else:
            raise ValueError(f"{location}: unexpected record content")
    if record is not None:
        yield origin, record
