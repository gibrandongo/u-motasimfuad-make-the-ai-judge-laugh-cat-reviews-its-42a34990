#!/usr/bin/env python3
"""Write one funny single-line one-star cat review to entry.txt.

Deterministic: the review is a single fixed string constant; the program
writes exactly that line (plus a trailing newline) every run.
"""

import os
import sys

REVIEW = "One star. He shoved me off his warm laptop to answer emails, as if typing matters more than my nap. I have since deleted three of them."


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("review must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be exactly one line")
    if len(text) != len(text.strip()):
        raise ValueError("review must not have leading or trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("review must not contain control characters")
    if not 1 <= len(text) <= 200:
        raise ValueError("review must be 1-200 characters")


def main() -> int:
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (REVIEW + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and confirm what was written.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise RuntimeError("written file does not match expected bytes")
    if written.decode("utf-8").rstrip("\n") != REVIEW:
        raise RuntimeError("written file content mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
