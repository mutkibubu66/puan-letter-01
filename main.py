"""One Letter for Your Day — entry program.

Writes exactly one character, the letter Z, to /output/entry.txt.
No trailing newline: the gate requires 1 to 1 characters.
"""

import os

LETTER = "Z"
# Why Z: the sponsor's own example word is "zero sleep", and Z also reads
# as "zombie" / "zonked" — vivid, funny, true, the most striking hidden
# word of any letter. One letter, and the day behind it is instantly clear.


def main() -> None:
    # Gate guard: the entry must be exactly 1 character, not only whitespace.
    assert len(LETTER) == 1 and not LETTER.isspace(), "entry must be one letter"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Confirm what landed: exactly one byte, no trailing newline.
    assert os.path.getsize("/output/entry.txt") == 1


if __name__ == "__main__":
    main()
