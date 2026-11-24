"""Alien Field Notes: The Two Day Earth Review.

Writes a single original line of plain text — an alien tourist's review
of planet Earth — to /output/entry.txt.

Standard library only. No network, no secrets, no external files.
"""

import os

ENTRY = (
    "3/5 stars. Lovely planet, but the locals worship a glowing rectangle, "
    "queue for coffee they complain about, and charged my saucer for "
    "parking. Would visit again, preferably unnoticed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
