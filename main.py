#!/usr/bin/env python3
"""Write the one-line review of my own Monday to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, exactly one line. The
line is a review of my own Monday: I gave Monday one star, and Monday
reviewed me back. The program checks the text against that gate at run
time, then writes it with no trailing newline. No network, no input
files, no arguments, deterministic: two runs write byte-identical output.
"""

import pathlib

REVIEW = (
    "I gave Monday one star. Monday reviewed me back: 'Arrived late, "
    "complained for eight hours, blamed the Wi-Fi, then asked why "
    "nothing shipped. Would not host again.'"
)


def main() -> None:
    text = REVIEW
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if out.read_bytes() != text.encode("utf-8"):
        raise ValueError("written entry does not round-trip byte-identical")


if __name__ == "__main__":
    main()
