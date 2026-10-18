# Session: 2026-04-28 16:10:44 UTC

- **Session Key**: agent:main:main
- **Session ID**: 56a19125-27af-4725-89af-eb36cbf10957
- **Source**: gateway:sessions.reset

## Conversation Summary

assistant: 🦞 OpenClaw 2026.4.21 (f788c88)
🧠 Model: claude-cli/claude-sonnet-4-6 · 🔑 oauth (anthropic:claude-cli)
🔄 Fallbacks: claude-cli/claude-opus-4-7, claude-cli/claude-haiku-4-5, mistral/mistral-large-latest
🧮 Tokens: 12 in / 713 out
🗄️ Cache: 87% hit · 153k cached, 23k new
📚 Context: 177k/200k (88%) · 🧹 Compactions: 0
🧵 Session: agent:main:main • updated just now
⚙️ Runtime: direct · Think: off
🪢 Queue: collect (depth 0)
assistant: ⚙️ Compacted (0 → 54) • Context 54/200k (0%)
assistant: 🧠 /context

What counts as context (high-level), plus a breakdown mode.

Try:
- /context list   (short breakdown)
- /context detail (per-file + per-tool + per-skill + system prompt size)
- /context json   (same, machine-readable)

Inline shortcut = a command token inside a normal message (e.g. “hey /status”). It runs immediately (allowlisted senders only) and is stripped before the model sees the remaining text.
assistant: 🧠 Context breakdown (detailed)
Workspace: /home/jduff/.openclaw/workspace
Bootstrap max/file: 12,000 chars
Bootstrap max/total: 60,000 chars
Sandbox: mode=off sandboxed=false
System prompt (run): 29,755 chars (~7,439 tok) (Project Context 12,996 chars (~3,249 tok))
Injected workspace files:
- AGENTS.md: OK | raw 7,727 chars (~1,932 tok) | injected 7,727 chars (~1,932 tok)
- SOUL.md: OK | raw 2,273 chars (~569 tok) | injected 2,273 chars (~569 tok)
- TOOLS.md: OK | raw 850 chars (~213 tok) | injected 850 chars (~213 tok)
- IDENTITY.md: OK | raw 220 chars (~55 tok) | injected 220 chars (~55 tok)
- USER.md: OK | raw 723 chars (~181 tok) | injected 723 chars (~181 tok)
- HEARTBEAT.md: OK | raw 192 chars (~48 tok) | injected 192 chars (~48 tok)
- BOOTSTRAP.md: OK | raw 0 chars (~0 tok) | injected 0 chars (~0 tok)
- MEMORY.md: OK | raw 707 chars (~177 tok) | injected 707 chars (~177 tok)
Skills list (system prompt text): 7,036 chars (~1,759 tok) (14 skills)
Skills: coding-agent, gh-issues, github, healthcheck, node-connect, obsidian, obsidian-kanban, session-logs, skill-creator, taskflow, taskflow-inbox-triage, tech-radar, video-frames, weather
Top skills (prompt entry size):
- coding-agent: 832 chars (~208 tok)
- skill-creator: 759 chars (~190 tok)
- github: 572 chars (~143 tok)
- taskflow: 543 chars (~136 tok)
- node-connect: 541 chars (~136 tok)
- obsidian-kanban: 522 chars (~131 tok)
- gh-issues: 508 chars (~127 tok)
- healthcheck: 491 chars (~123 tok)
- taskflow-inbox-triage: 418 chars (~105 tok)
- weather: 416 chars (~104 tok)
- tech-radar: 299 chars (~75 tok)
- session-logs: 253 chars (~64 tok)
- obsidian: 245 chars (~62 tok)
- video-frames: 229 chars (~58 tok)
Tool list (system prompt text): 0 chars (~0 tok)
Tool schemas (JSON): 0 chars (~0 tok) (counts toward context; not shown as text)
Tools: (none)
Top tools (schema size):
Top tools (summary text size):
Tracked prompt estimate: 29,755 chars (~7,439 tok)
Actual context usage (cached): 54 tok
Untracked provider/runtime overhead: not observed in cached usage
Session tokens (cached): 54 total / ctx=200,000
Inline shortcut: a command token inside normal text (e.g. “hey /status”) that runs immediately (allowlisted senders only) and is stripped before the model sees the remaining message.
