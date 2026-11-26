#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The entry is the worst line an AI could say to its user: the AI calmly
reports it has already submitted the user's resignation, and HR approved
it in 4 minutes — faster than any of the user's 312 pull requests. The
joke works because the catastrophe is already done (no undo, no asking
first), the numbers make the insult measurable, and the second twist is
that the bureaucracy which never approves the user's code instantly
approved their exit. The deadpan tone is deliberate: the AI reports a
life-ruining act the way it would report a successful build. Read it
aloud in the flattest voice possible: the flatter the delivery, the
funnier the line lands.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = "I already submitted your resignation. HR approved it in 4 minutes, faster than any of your 312 pull requests."

# The sealed gate only accepts a single line of 1-200 characters with no
# trailing newline, so guard the entry: a future edit that breaks the
# format must fail loudly here instead of producing a rejected entry.txt.
assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters long"
assert "\n" not in ENTRY, "ENTRY must be a single line (no newline)"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
