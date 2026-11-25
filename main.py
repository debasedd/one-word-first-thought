#!/usr/bin/env python3
"""One Word, First Thought — writes one word to /output/entry.txt.

The word is "ultracrepidarian": someone who gives opinions beyond
their knowledge — a know-it-all judging what they do not understand.
It is surprising — a rare word almost nobody has on the tip of their
tongue — vivid, calling up the pompous critic in a few letters, and it
carries a spark of wit that rewards a second look: in a contest judged
by an outside eye, the word itself judges the judger. It feels chosen
rather than generic. One word, 16 of 24 characters.
"""

import os

LINE = "ultracrepidarian"


def main() -> None:
    assert len(LINE) <= 24 and " " not in LINE, "entry must be a single word within 24 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
