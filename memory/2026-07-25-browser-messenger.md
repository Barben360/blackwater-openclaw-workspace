# Browser Messenger Reading

## Setup
- Chrome extension installed 2026-07-25
- Read Messenger via `profile="chrome"` (browser extension)
- Extension pair: runs on loopback `ws://127.0.0.1:18799`

## Scrolling Messenger Conversations
Messenger uses virtual scrolling via React — only renders a subset of messages. To load older messages:

1. Find the scrollable container: look for a div inside `role="main"` with `overflowY: scroll/auto` and `scrollHeight > clientHeight`
2. Continuously set `scrollTop = 0` at 300ms intervals to trigger Messenger's infinite scroll loader
3. Monitor `scrollHeight` — jumps indicate new messages loaded (confirmed: 1,853 → 34,803)

```js
// Pattern: rapid scrollTop = 0 assignments with delays
for (let i = 0; i < 40; i++) {
  container.scrollTop = 0;
  await new Promise(r => setTimeout(r, 300));
}
```

## Mot du Jour / Tusmo
- Group chat for Ben's Wordle game group
- Thread ID: `1274886107864622`
- Scores format: "X et Y" where X = Mot du jour attempts, Y = Tusmo attempts
- Excel spreadsheet tracker pinned to chat (OneDrive link)
- Players include: Ben, Clara, Audrey, Manon, Martin, Anthony

## What Works / What Doesn't
- ✅ Reading message list sidebar
- ✅ Reading visible messages via snapshot
- ✅ Scrolling to load older messages
- ✅ Screenshots of Messenger pages
- ⚠️ Messenger search only searches message text, not date separators
- ⚠️ Excel Online via browser is tricky (cross-origin iframe; better to use downloaded file)
