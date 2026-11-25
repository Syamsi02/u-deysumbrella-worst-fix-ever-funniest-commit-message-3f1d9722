#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit-message line (77 characters, within the 100-char gate)
to /output/entry.txt, and prints it to stdout. Pure stdlib, deterministic:
the same line on every run.
"""

from pathlib import Path

LINE = "fix: stop the crash by deleting the users; zero errors reported since Tuesday"


def main() -> None:
    assert 1 <= len(LINE) <= 100, len(LINE)
    assert LINE == LINE.strip() and LINE, "line must be a single non-blank line"
    out = Path("/output/entry.txt") if Path("/output").is_dir() else Path("output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
