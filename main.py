#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single persuasive sentence (1-240 characters) to
/output/entry.txt. The sentence is fixed and deterministic: the
grader runs the program twice and gates the output, so the same
text must come out every time. No network, no secrets, no input
files -- everything the program needs is in this file.
"""

import os
import stat

PITCH = (
    "You don't need to know how to code \u2014 just tell an AI agent "
    "on make.fun your app idea in your own words, and it will build "
    "a real, working app you can try, share, and keep improving."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = PITCH.strip()
    if not (1 <= len(text) <= 240):
        raise SystemExit(
            "pitch must be 1-240 characters, got %d" % len(text)
        )
    if not text.strip():
        raise SystemExit("pitch must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader collects the output as another user: leave it readable.
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    main()
