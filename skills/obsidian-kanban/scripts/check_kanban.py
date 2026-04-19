#!/usr/bin/env python3
"""Detect whether an Obsidian note uses the kanban plugin."""

import sys


def is_kanban(path: str) -> bool:
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if "kanban-plugin:" in line:
                    return True
    except OSError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(2)
    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path-to-note>", file=sys.stderr)
        sys.exit(2)

    if is_kanban(sys.argv[1]):
        print("kanban")
        sys.exit(0)
    else:
        print("plain")
        sys.exit(1)
