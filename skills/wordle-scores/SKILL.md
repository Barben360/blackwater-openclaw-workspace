---
name: wordle-scores
description: Report Mot du Jour / Tusmo scores for a given week by reading Messenger, updating the Excel sheet, and summarizing.
---

# Wordle Scores Reporter

Report Mot du Jour / Tusmo scores for a given week. Multi-step workflow: open Messenger tab → find date range in Excel → scroll Messenger → parse scores → write to Excel → summarize.

## Prerequisites

- `messenger-browser` skill (browser Messenger reading)
- `microsoft-excel` skill (Graph API via Maton)
- `MATON_API_KEY` in environment (read from `~/.maton-api-token` if the env var is a shell substitution)

## Step 1: Open Messenger tab

First check if a Messenger tab with the Mot du Jour / Tusmo conversation is already open:

```js
browser({ action: "tabs" })
```

If the "Mot du jour / Tusmo" conversation (thread ID `1274886107864622`) is not already open, spawn it directly:

```js
browser({ action: "open", url: "https://www.messenger.com/t/1274886107864622", profile: "chrome" })
```

Only if the browser cannot be opened at all (no Chrome extension available or `profiles` shows no `chrome` profile running), tell Ben "Je ne peux pas ouvrir Chrome, tu peux partager l'onglet Messenger (Mot du jour / Tusmo) ?" and STOP.

## Step 2: Find date range from Excel

Given a week number N:
1. Read the Scores sheet to find rows for Week N
2. Extract the Excel serial dates from column C for each day
3. Convert: `date = datetime(1899, 12, 30) + timedelta(days=serial)`
4. Determine the date range (Monday to Sunday) for the week

Excel file is shared with Ben at:
- Drive ID: `b4e1e630cabb8d13`
- Item ID: `B4E1E630CABB8D13!s8d77805ecc034ef1ae0137e2129e5310`
- Worksheet: `Scores`

API base: `https://gateway.maton.ai/microsoft-excel/v1.0/me/drives/{drive_id}/items/{item_id}/workbook/worksheets('Scores')`

## Step 3: Scroll Messenger to the correct dates

Use the messenger-browser skill's scroll technique (jump to latest, find the scrollable container inside `role="main"`, set `scrollTop = 0` at 300ms intervals, take compact snapshots) to reach the target date range.

**Scrolling tip:** The virtual scroller loads the entire conversation history, making precise positioning tricky. If you overshoot:
- Jump to latest with "Accéder au message le plus récent"
- Then set `scrollTop` to a fraction of `scrollHeight` to target the right date range
- Example: scrollHeight=40000, target early August ≈ scrollTop=35000

## Step 4: Parse scores from Messenger

### Score format
Each day has TWO Wordle games. Reports like:
- `X et Y` → X = Mot du jour attempts, Y = Tusmo attempts
- `2 et 3` = 2 attempts on Mot du jour, 3 on Tusmo

### Player mapping (Messenger name → Excel column group)

| Messenger name | Excel columns | Column letters |
|---|---|---|
| Clara / Clara Pautonnier | Cols J-L | Mot=J, Tusmo=K, Total=L |
| Audrey / Audrey Ljn | Cols P-R | Mot=P, Tusmo=Q, Total=R |
| Manon / Manon Grimault | Cols G-I | Mot=G, Tusmo=H, Total=I |
| Martin / Martin Eyx | Cols D-F | Mot=D, Tusmo=E, Total=F |
| Anthony / Anthony Ferré / Antho | Cols S-U | Mot=S, Tusmo=T, Total=U |
| Vous / Ben / Benjamin Barrois | Cols M-O | Mot=M, Tusmo=N, Total=O |

### Edge cases to handle

1. **"Hier j'ai fait X et Y"** → Scores refer to YESTERDAY, not the message timestamp. Place in the correct day column.
2. **Late night / early morning reports**: Scores posted at very early hours (e.g. 05:39) without "Hier" likely refer to the previous day if the same person also posts a later score the same day. Apply common sense.
3. **Missing a day**: If a player has played at least once this week but didn't report for a specific day → score is 7,7 (max attempts = didn't find the word). Do NOT apply 7,7 for today (current day) — they may not have played yet.
4. **Current day with no scores**: Leave blank in Excel. Do not fill 7,7.
5. **Non-score messages**: IGNORE everything not about scores. The group often has banter, jokes, photo attachments, etc. Only extract messages containing score patterns.
6. **"Pareil" or "Même chose"**: Player got the same scores as the previous player who reported. Copy those scores.
7. **Incomplete reports**: "J'ai fait 3" (only one game mentioned) → note it but don't guess the second score.
8. **Someone explicitly says they didn't play**: Leave blank (do NOT set to 7,7). 7,7 is only for when they played but didn't find the word, not for when they didn't play at all.
9. **Player hasn't reported at all this week**: Leave all days blank. They may not be playing this week.

### Score pattern matching
Scores usually come in one of these patterns:
- `X et Y` (e.g. "2 et 3", "4 et 5")
- `X etY` (e.g. "2 et4" — missing space)
- Look for messages containing JUST numbers and "et", or messages where the score pattern appears within a sentence

Ignore messages that are clearly not scores (jokes, reactions, photos, banter about the game rules, Excel tracker discussion).

## Step 5: Write to Excel

For each day in the week, update the player's cells using the Graph API PATCH endpoint. Each day is one row.

```python
# PATCH to a specific cell or range
url = f"https://gateway.maton.ai/microsoft-excel/v1.0/me/drives/{drive_id}/items/{item_id}/workbook/worksheets('Scores')/range(address='J{row}')"
# Body: {"values": [[mot_score]]}
```

Column mapping per player for scores:
- Martin: Mot=D, Tusmo=E, Total=F
- Manon: Mot=G, Tusmo=H, Total=I
- Clara: Mot=J, Tusmo=K, Total=L
- Ben: Mot=M, Tusmo=N, Total=O
- Audrey: Mot=P, Tusmo=Q, Total=R
- Antho: Mot=S, Tusmo=T, Total=U

After writing all scores, also update the Total column for each player (sum of Mot + Tusmo for the day). Also update the Week TOTAL row (the row with "TOTAL" in column B after the week's rows) by summing each player's daily totals.

## Step 6: Summary

Present a clear table showing:
- Each day of the week as a row
- Each player as a column group (Mot | Tusmo)
- Mark scores found in Messenger vs. those filled as 7,7 (missed)
- Note any days with incomplete data

Format:
```
Week N (Mon DD/MM — Sun DD/MM)
| Day | Clara | Audrey | Manon | Martin | Ben | Antho |
| Lun | 3/3 ✓ | 2/3 ✓ | 4/3 ✓ | 7/7 ✗ | -- | 3/2 ✓ |
...
```

Where ✓ = found in chat, ✗ = missed day (7,7), -- = not yet played.

## Important: Write to memory

After completing the report, save a summary to `memory/YYYY-MM-DD-scores-week-N.md` so it's searchable later.
