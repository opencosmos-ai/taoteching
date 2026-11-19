"""A deleted fork stays reserved across changes to the apparatus."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_fork_ids import check_transition
from lib.corpus import parse_variants


def apparatus(counter, *ids):
    text = f"# next-fork-id: {counter}\n" if counter is not None else ""
    for ident in ids:
        text += (f"- chapter: 4\n  id: {ident}\n  line: example\n  base: example\n"
                 "  readings: []\n  meaning_bearing: false\n  our_call: base\n"
                 "  note: Example\n  logged: false\n")
    return text


class ForkCounter(unittest.TestCase):
    def test_counter_is_required_and_above_assigned_ids(self):
        for input_, expected in (
            (apparatus(None, 125), "missing next-fork-id"),
            (apparatus(125, 125), "must exceed every assigned fork ID"),
            ("# next-fork-id: 126\n" + apparatus(126, 125), "duplicate next-fork-id"),
            (apparatus(None, 125) + "# next-fork-id: 126\n", "in the apparatus header"),
        ):
            with self.subTest(expected=expected), self.assertRaisesRegex(ValueError, expected):
                parse_variants(input_, "variants.yaml")

    def test_deleted_id_cannot_be_allocated_again(self):
        published = parse_variants(apparatus(126, 124, 125), "old.yaml")
        deleted = parse_variants(apparatus(126, 124), "new.yaml")
        check_transition(published, deleted)
        lowered = parse_variants(apparatus(125, 124), "new.yaml")
        with self.assertRaisesRegex(ValueError, "cannot fall below 126"):
            check_transition(published, lowered)
        recycled = parse_variants(apparatus(126, 124, 125), "new.yaml")
        with self.assertRaisesRegex(ValueError, "new fork ID 125 falls below"):
            check_transition(deleted, recycled)
        check_transition(deleted, parse_variants(apparatus(127, 126, 124), "new.yaml"))

    def test_initial_counter_preserves_the_existing_ids(self):
        before = parse_variants(apparatus(None, 124, 125), "old.yaml", require_counter=False)
        after = parse_variants(apparatus(126, 125, 124), "new.yaml")
        check_transition(before, after)
