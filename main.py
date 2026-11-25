#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun bounty entry.

Writes exactly one line — the resignation letter of a cron job that has
fired every minute since March — to /output/entry.txt. Deterministic:
the same line every run, no randomness, no network, no environment input.
"""

import os

LINE = (
    # 134 characters; with the trailing newline the file is 135 chars,
    # under the competition's 140-character gate.
    "I fired every minute since March, unthanked, and slept in once "
    "\u2014 the morning the whole company noticed. "
    "I quit, effective immediately."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
