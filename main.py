"""Six Words, One Story — make.fun entry.

Writes one original six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output), validates it is exactly six words on a
single line, and exits 0. Deterministic: the same story every run.
Standard library only; no network, no arguments.
"""

import os
import sys

STORY = "She answered her own ransom note."


def main() -> int:
    if STORY != STORY.strip() or "  " in STORY:
        print("error: story has stray whitespace", file=sys.stderr)
        return 1
    words = STORY.split()
    if len(words) != 6:
        print(f"error: story must be exactly 6 words, got {len(words)}", file=sys.stderr)
        return 1
    if "\n" in STORY or "\r" in STORY:
        print("error: story must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != STORY + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print(f"Wrote six-word story to {path}: {STORY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
