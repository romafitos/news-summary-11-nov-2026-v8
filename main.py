"""Print the 11 November 2026 news summary to stdout."""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "summary.txt")
    with open(path, "r", encoding="utf-8") as f:
        sys.stdout.write(f.read())


if __name__ == "__main__":
    main()
