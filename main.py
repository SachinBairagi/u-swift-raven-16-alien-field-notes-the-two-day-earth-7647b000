"""Alien Field Notes: The Two Day Earth Review.

Writes one original line, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt: an alien tourist's review of Earth.
"""

import os

LINE = (
    "Two-day stay on Earth: locals pay rent to live on their own planet, "
    "queue for bitter bean water, and worship glowing rectangles. "
    "Three stars, the sunsets almost justify it."
)


def main() -> None:
    # Deterministic: the same fixed line every run, no randomness or I/O
    # beyond the single output file, so repeated runs are byte-identical.
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert "\n" not in text
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
