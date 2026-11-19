#!/usr/bin/env python3
"""Check the apparatus ID counter against the preceding Git snapshot."""

import argparse
import re
import subprocess
import sys

from lib.corpus import ROOT, VARIANTS, parse_variants


def check_transition(previous, current):
    previous_next, previous_forks = previous
    next_id, forks = current
    previous_ids = {fork.id for fork in previous_forks if fork.id is not None}
    floor = previous_next if previous_next is not None else max(previous_ids, default=0) + 1
    if next_id is None or next_id < floor:
        raise ValueError(f"{VARIANTS}: next-fork-id cannot fall below {floor}")
    for fork in forks:
        if fork.id is not None and fork.id not in previous_ids and fork.id < floor:
            raise ValueError(f"{fork.location}: new fork ID {fork.id} falls below the previous next-fork-id {floor}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", help="full commit SHA of the previous snapshot")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.base):
        parser.error("base must be a full commit SHA")
    revision = f"{args.base}:{VARIANTS.relative_to(ROOT).as_posix()}"
    try:
        old_text = subprocess.check_output(["git", "show", revision], cwd=ROOT, encoding="utf-8")
        previous = parse_variants(old_text, revision, require_counter=False)
        current = parse_variants(VARIANTS.read_text(encoding="utf-8"), VARIANTS)
        check_transition(previous, current)
    except (ValueError, subprocess.CalledProcessError) as exc:
        print(exc, file=sys.stderr)
        return 1
    print("Fork IDs respect the previous allocation counter.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
