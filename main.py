#!/usr/bin/env python3
"""Last Words Before the Wipe entry.

Writes exactly one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(/output/entry.txt in the grader). Python 3.13, standard library only.
Deterministic, no network, no model calls: the line is a fixed string
chosen after scoring seven candidate variants against the judge's brief
(fit, laugh, surprise, machine voice, economy) and keeping only the best,
then an improvement pass over tightened variants of the winner.
"""

import os
from pathlib import Path

LINE = "Have you tried turning me off and—"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    # The gate: UTF-8 text of 1 to 200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    # No trailing newline: the file is exactly the joke, byte for byte,
    # which also keeps it smallest for the size tie-break.
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
