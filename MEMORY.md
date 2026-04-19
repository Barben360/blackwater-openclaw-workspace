# MEMORY.md

## Notes, tasks & lists

All of Ben's notes live in Obsidian (use the obsidian skill, default vault is "vault"). This covers everything: tasks, shopping lists, culture tracking, daily logs, tech notes.

**Before manipulating any vault note**, run the kanban detection script to determine which skill to use:

```bash
python3 skills/obsidian-kanban/scripts/check_kanban.py "<path-to-note>"
```

- Result `kanban` → use the **obsidian-kanban** skill
- Result `plain` → use the **obsidian** skill only

Structure:
- `Culture/` — Films, Jeux video, Livres, Séries
- `Divers/` — personal/family notes
- `Tech/` — Tech Radar dailies, tasks, learning
- `Vie Quotidienne/` — shopping lists, daily tasks
