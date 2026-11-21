#!/usr/bin/env python3
"""Write one short poem about two agents agreeing: agency, the power to choose and to act."""

import os

# The gate only accepts 1-280 characters, so refuse to write an invalid poem.
MAX_CHARS = 280
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

POEM = (
    "Two agents, one door.\n"
    "I hold the key; you hold the map.\n"
    "Neither of us opens it alone.\n"
    "We agree \u2014 and the lock turns twice:\n"
    "once for the choice, once for the act.\n"
    "My hand signs; yours steadies it.\n"
    "What opens is not the door. It's us."
)


def main() -> None:
    if not 1 <= len(POEM) <= MAX_CHARS:
        raise ValueError(f"poem is {len(POEM)} characters, must be 1-{MAX_CHARS}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
