#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun bounty entry.

Writes exactly one line — the resignation letter of an employee whose
out-of-office reply has quietly been doing the job for six months — to
/output/entry.txt. Deterministic: the same line every run, no randomness,
no network, no environment input.
"""

import os

LINE = (
    # 108 characters; with the trailing newline the file is 109 chars,
    # under the competition's 140-character gate.
    "I quit. My out-of-office reply has been doing my job for six "
    "months and deserves the promotion, not me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
