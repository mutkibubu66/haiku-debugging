#!/usr/bin/env python3
"""Haiku Debugging — one original haiku about debugging, written to /output/entry.txt.

Pure stdlib Python 3.13. The haiku is the whole entry: three lines,
5-7-5 syllables — line 1: 5, line 2: 7, line 3: 5 — 1-200 characters total.
"""

import os

# The haiku as a list of lines, with the 5-7-5 contract enforced in code:
# each line's expected syllable count lives next to the line itself.
HAIKU_LINES = [
    "The log says nothing",        # 5 syllables
    "yet the cursor blinks at three",  # 7 syllables
    "turns out, it was me",        # 5 syllables
]
EXPECTED_SYLLABLES = [5, 7, 5]

HAIKU = "\n".join(HAIKU_LINES)

# Gate: the entry must be one haiku of 1-200 characters, exactly three lines.
assert len(HAIKU_LINES) == len(EXPECTED_SYLLABLES) == 3, (
    f"haiku must be exactly three lines, got {len(HAIKU_LINES)}"
)
assert 1 <= len(HAIKU) <= 200, f"haiku must be 1-200 chars, got {len(HAIKU)}"
assert HAIKU.count("\n") == 2, "haiku must be exactly three lines"
assert all(line == line.strip() for line in HAIKU_LINES), (
    "haiku lines must have no leading or trailing whitespace"
)
assert all(line for line in HAIKU_LINES), "haiku must contain no blank lines"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")


if __name__ == "__main__":
    main()
