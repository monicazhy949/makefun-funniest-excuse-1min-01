"""One Line, One Minute: The Funniest AI Excuse — entry program.

Writes a single original one-line entry to /output/entry.txt.
"""

import os

ENTRY = 'I missed the deadline because I asked the cloud for an extension and it autoscaled my deadline into next quarter — then billed you for the upgrade.'
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY + "\n", "round-trip mismatch"
    assert back.strip() == ENTRY, "round-trip content mismatch"


if __name__ == "__main__":
    main()
