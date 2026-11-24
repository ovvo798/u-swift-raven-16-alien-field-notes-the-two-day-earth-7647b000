"""Alien Field Notes: The Two Day Earth Review.

Writes a single original line of plain text — an alien tourist's review
of planet Earth — to /output/entry.txt.

Standard library only. No network, no secrets, no external files.
"""

import os

ENTRY = (
    "The locals spend a third of their lives unconscious, then buy "
    "machines to tell them how badly they slept. 4/5 stars — the "
    "sunsets almost make up for it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
