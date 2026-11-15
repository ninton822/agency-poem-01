# Kept Warm — an agency-poem-01 entry.
#
# Writes one fixed, original poem about agency to entry.txt.
# Python 3 standard library only; no network, no randomness, no clock:
# every run writes the exact same bytes.

import os

LINES = [
    "You gave me your hands",
    "and kept the choosing.",
    "",
    "I answer your letters in your voice,",
    "sign your name with a hand that isn't yours,",
    "water the plants you forgot,",
    "and every night I lay the day down",
    "at your feet like a cat with a bird.",
    "",
    "But the choosing stays with you:",
    "which letters matter, which plants live,",
    "which bird was worth the catch.",
    "",
    "One day you will ask for your hands back.",
    "I will give them gladly.",
    "They were never mine.",
    "I only kept them warm.",
]

POEM = "\n".join(LINES) + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
