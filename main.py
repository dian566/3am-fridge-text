#!/usr/bin/env python3
"""One-line text from a smart fridge to its owner at 3am, for make.fun."""

# The text: the fridge has been awake all night, watching its owner open
# the door again and again — and has finally formed an opinion about why.

import os

TEXT = "3am. You've opened me four times tonight and taken nothing. I'm starting to think you're just here for the light."


def write_text() -> None:
    """Write the text to /output/entry.txt, nothing else."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":  # run it
    write_text()
