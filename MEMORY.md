# MEMORY.md

## Notes, tasks & lists

All of Ben's notes live in Obsidian. This covers everything: tasks, shopping lists, culture tracking, daily logs, tech notes.

**Vault path — critical, do NOT write to the wrong one:**
- ✅ **Correct vault (LiveSync source of truth):** `/home/jduff/Workspace/github.com/Barben360/blackwater-services/volumes/obsidian-livesync/vault`
  - This is the `vault` default in `obsidian-cli` (notesmd-cli).
- ❌ **Never use** `/home/jduff/Obsidian` — it's a client-only mirror that only syncs when the Obsidian app is running. Writes there are inert/stale.

Use `obsidian-cli` (notesmd-cli; default vault `vault` = correct path) or direct filesystem edits to the correct path above. The official `obsidian` CLI is unreliable (crashes with exit 133); do not fall back to `find` + guess.

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

## Skills
- `messenger-browser` — workspace skill for reading Messenger via Chrome extension (browser virtual scroll technique, Mot du Jour/Tusmo group)
- `wordle-scores` — workspace skill for reporting weekly Mot du Jour/Tusmo scores: read Messenger, parse scores, write to Excel, summarize


