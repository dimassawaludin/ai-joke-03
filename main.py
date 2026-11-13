"""ai-joke-03 entry: a single fixed joke about an AI coding agent.

The program writes one joke to entry.txt in the output directory.
The joke never changes: no network, no randomness, no clock reads,
so every run produces a byte-identical file.
"""

import os

JOKE = 'I asked my coding agent to explain its fix. It said, "Certainly!" — then pasted my own code back with the bug renamed.'

ENTRY_NAME = "entry.txt"


def main() -> None:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    destination = os.path.join(folder, ENTRY_NAME)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
