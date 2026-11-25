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
    # Sealed gate (RULES.txt): entry.txt must be a single word of 1-24
    # characters. A longer word scores Valid=0 outright — the first
    # candidate, "floccinaucinihilipilification" (29 letters), was rejected
    # for exactly that reason, so the check below enforces the full gate.
    assert 1 <= len(LINE) <= 24, "entry must be 1-24 chars"
    assert LINE.isalpha(), "entry must be a single word (letters only)"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
