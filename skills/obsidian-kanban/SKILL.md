---
name: obsidian-kanban
description: Read, edit, and manipulate Obsidian notes that use the obsidian-kanban plugin (boards with lanes and cards). Use when working with kanban boards in the vault — adding/moving/archiving cards, managing lanes, updating settings, or creating new boards. Always use obsidian-cli for file I/O; this skill provides kanban-specific format knowledge on top of it.
---

# Obsidian Kanban

## Detection

Before editing any vault note, run the detection script to check if it is a kanban board:

```bash
python3 skills/obsidian-kanban/scripts/check_kanban.py "<path-to-note>"
# exits 0 + prints "kanban"  → use this skill
# exits 1 + prints "plain"   → use obsidian-cli only
```

## Working with kanban boards

1. **Read** `references/kanban-format.md` for the file format, editing rules, and common operations.
2. **Use obsidian-cli** for all actual file reads and writes — kanban boards are plain markdown files, editable directly.
3. **Preserve the `%% kanban:settings %%` block** at the end of the file unless explicitly changing board settings.

## Reference

- [kanban-format.md](references/kanban-format.md) — file format, editing rules, common operations, settings reference
