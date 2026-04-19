# Obsidian Kanban — Format & Operations Reference

## File format

A kanban board is a plain `.md` file. Detection: contains `kanban-plugin:` anywhere in the file.

```markdown
---
kanban-plugin: board
---

## Lane Title

- [ ] Card text @{2024-01-15}
- [ ] Another card #tag

## In Progress (3)

- [ ] Card with WIP limit (lane max = 3)

## 

**Complete**
- [x] Archived card

%% kanban:settings
```json
{"kanban-plugin":"board","list-collapse":[false,false,false]}
```
%%
```

### Key structural rules

- **Frontmatter** must contain `kanban-plugin: board` (or `list`, `table`, `timeline`)
- **Lanes** = `## Heading` lines; WIP limit in parentheses: `## In Progress (5)`
- **Cards** = `- [ ] text` (open) or `- [x] text` (archived/done)
- **Archive lane**: unnamed lane (`## `) with `**Complete**` label above archived cards
- **Settings block**: `%% kanban:settings ... %%` at end of file — preserve as-is unless explicitly changing settings
- **Dates**: appended as `@{YYYY-MM-DD}` by default (format is configurable per board)
- **Tags**: standard Obsidian `#tag` syntax, displayed at card bottom when hidden from title

## Editing rules

**DO** edit cards and lane headings directly as markdown.  
**DON'T** touch the `%% kanban:settings %%` block unless changing board settings.  
**DON'T** reformat the frontmatter — extra blank lines around `kanban-plugin:` are normal.

## Common operations

### Add a card to a lane
Append `- [ ] Card text` under the target `## Lane` heading (before the next `##`).

### Move a card between lanes
Cut the `- [ ] ...` line and paste under the target lane heading.

### Archive a card
Change `- [ ] text` to `- [x] text` and move it under the archive lane (`## ` / `**Complete**`).

### Add a lane
Insert `## New Lane Name` with a blank line above and below.

### Set/update WIP limit
Rename lane heading: `## In Progress` → `## In Progress (5)`.

### Add a date to a card
Append `@{YYYY-MM-DD}` to the card text (uses board's date format).

## Settings (per-board frontmatter / settings block)

Settings live in two places:
- `kanban-plugin:` key in frontmatter (board type)
- JSON in `%% kanban:settings %%` block (all other settings)

Key settings in the JSON block:

| Key | Description |
|-----|-------------|
| `list-collapse` | Array of booleans, one per lane — whether lane is collapsed |
| `date-format` | Output format for date picker (e.g. `YYYY-MM-DD`) |
| `date-display-format` | Format shown at bottom of card |
| `time-format` | Output format for time picker |
| `link-date-to-daily-note` | Link card dates to daily notes |
| `show-relative-date` | Show days-until/since on cards |
| `prepend-new-cards` | Insert new cards at top of lane |
| `new-line-trigger` | `enter` or `shift-enter` |
| `max-archive-size` | Cap on archived cards (-1 = unlimited) |

Full settings reference: https://github.com/obsidian-community/obsidian-kanban/tree/main/docs/Settings

## How to create a board from scratch

Create a `.md` file with this minimal structure:

```markdown
---

kanban-plugin: board

---

## To Do



## In Progress



## Done


%% kanban:settings
```json
{"kanban-plugin":"board","list-collapse":[false,false,false]}
```
%%
```
