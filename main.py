#!/usr/bin/env python3
"""One Word, First Thought — writes one word to /output/entry.txt.

The word is "defenestration": the act of throwing someone out of a
window. It is surprising — nobody's safe first guess — vivid, calling up
a clear image in a few letters, and it carries a spark of wit in its
sound and its absurd specificity: English keeps a grand Latin word
reserved for one very particular crime. It feels chosen rather than
generic, and it rewards a second look. One word, 14 of 24 characters.
"""

import os

LINE = "defenestration"


def main() -> None:
    assert len(LINE) <= 24 and " " not in LINE, "entry must be a single word within 24 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
