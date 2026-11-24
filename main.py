#!/usr/bin/env python3
"""Haiku Debugging — one original haiku about debugging, written to /output/entry.txt.

Pure stdlib Python 3.13. The haiku is the whole entry: three lines,
5-7-5 syllables, 1-200 characters total.
"""

import os

HAIKU = """The log says nothing
yet the cursor blinks at three
turns out, it was me"""

# Gate: the entry must be one haiku of 1-200 characters, exactly three lines.
assert 1 <= len(HAIKU) <= 200, f"haiku must be 1-200 chars, got {len(HAIKU)}"
assert HAIKU.count("\n") == 2, "haiku must be exactly three lines"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")


if __name__ == "__main__":
    main()
