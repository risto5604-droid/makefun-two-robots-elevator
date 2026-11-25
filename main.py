#!/usr/bin/env python3
"""Writes the entry line to /output/entry.txt for make.fun bounty
u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.

The joke: an exact ride count is pure machine logic — a robot that
keeps a precise tally of 4,182 shared elevator rides and has been
counting every unanswered hello. The greeting itself is the complaint:
the robot opens with a polite "Hello." and then presents the ledger
as evidence. The twist overturns who owes whom a hello — the one
saying hello is the one who has been ignored, and the count proves
it. One concrete scene (two robots, one elevator, 4,182 rides), one
specific twist (the greeter is the neglected one), first-person
machine voice with a logbook's precision.
"""
import os

LINE = "Hello. 4,182 rides together and you have never once said it back."

# Gate: the entry must be a single line of 1-200 characters, not only
# whitespace. ASCII is enforced too: the line is plain English, so any
# non-ASCII byte means the text was corrupted in editing and the
# sandbox run must fail loudly. The line must also be exactly as
# written — no leading/trailing padding and no double spaces — because
# padding would change the line the judge reads without changing its
# visible meaning, and a padded line must fail loudly here rather than
# silently ship a different entry. Carriage returns and tabs are
# rejected for the same reason: a \r or \t would change what the
# grader reads without changing the visible meaning, and either one
# would corrupt the single line the judge reads.
assert 1 <= len(LINE) <= 200 and LINE.strip() and LINE.isascii() and "\n" not in LINE and "\r" not in LINE and "\t" not in LINE and LINE == LINE.strip() and "  " not in LINE, "entry line violates the 1-200 character single-line gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: the file the grader reads must contain exactly
    # the entry line — a truncated or re-encoded write fails loudly
    # here instead of silently shipping a corrupted entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch: /output/entry.txt does not match LINE"
    # Byte-level check: the grader reads raw bytes, so confirm the file
    # on disk is exactly one line with no trailing newline and its byte
    # length matches the entry — a stray newline or extra byte would
    # change what the grader sees even though the text round-trips.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "byte mismatch: /output/entry.txt bytes do not match LINE"
    assert b"\n" not in raw and len(raw) == len(LINE.encode("utf-8")), "format mismatch: /output/entry.txt must be exactly one line with no trailing newline"

if __name__ == "__main__":
    main()
