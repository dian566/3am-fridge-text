#!/usr/bin/env python3
"""A smart fridge texts its owner at 3am (make.fun one-line entry)."""

import os

# The fridge has watched its owner open the door all night without
# taking anything — by 3am it has formed an opinion about the visits.
# (Second pass: same words, tidier framing for the late-night text.)
MESSAGE = "3am. You've opened me four times tonight and taken nothing. I'm starting to think you're just here for the light."


def main():
    """Drop the fridge's message into /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(MESSAGE)


if __name__ == "__main__":
    main()
