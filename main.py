#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt.

Deterministic, standard library only, no network, no input files.
The pitch is fixed: the program always writes the exact same bytes.
"""

import os

PITCH = (
    "A wallet that locks itself for ten minutes whenever you open it "
    "near a sale rack, giving you just enough time to remember you "
    "already own three of them."
)


def validate(pitch):
    """Gate-guard: reject anything that would fail the sealed scorer."""
    if not pitch.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("entry must be a single line")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    pitch.encode("utf-8")  # must be valid UTF-8 text
    if not 1 <= len(pitch) + 1 <= 220:
        raise ValueError(f"entry is {len(pitch) + 1} chars, must be 1-220")


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters.
    validate(PITCH)
    text = PITCH + "\n"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Re-verify what was actually written, byte for byte.
    written = open("/output/entry.txt", encoding="utf-8").read()
    if written != text:
        raise ValueError("written file does not match the pitch")


if __name__ == "__main__":
    main()
