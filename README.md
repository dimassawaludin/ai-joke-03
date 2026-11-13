# ai-joke-03

A tiny entry for the make.fun ai-joke-03 bounty. The program writes one
fixed joke about an AI coding agent to `entry.txt`.

Run it with `python3 main.py`. The output directory comes from the
`MAKEFUN_OUTPUT_DIR` environment variable and defaults to `/output`.
The joke never changes, so the file is byte-identical on every run.

The joke itself: an agent asked to explain its fix answers "Certainly!",
then pastes the user's own code back with the bug renamed.
