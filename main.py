"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Deterministic: the entry is a single fixed string, written verbatim with no
trailing newline, so every run produces byte-identical output.
"""

import os

ENTRY = "I tested in production — it's the only environment that believes in me."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
