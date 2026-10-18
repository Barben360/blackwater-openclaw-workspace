---
name: messenger-browser
description: Read Facebook Messenger conversations through the OpenClaw Chrome extension (profile="chrome"), handling Messenger's React virtual scrolling.
---

# Messenger Browser Reader

Read Facebook Messenger conversations through the OpenClaw Chrome extension (`profile="chrome"`). Messenger uses React virtual scrolling — this skill handles the tricky parts.

## Prerequisites

- Chrome extension installed and paired (`openclaw browser extension pair`)
- Browser plugin enabled in `plugins.allow`
- Agent has `browser` in `tools.alsoAllow`
- Default profile set to `chrome`: `browser.defaultProfile: "chrome"`

## Launching the browser (if not running)

Chrome is not always running, and the OpenClaw extension needs it up before any `browser` call works. Do this first:

1. Check status:
   ```
   browser({ action: "status" })
   ```
   If `running: false` or `cdpReady: false`, launch Chrome.

2. Chrome needs the display env from the running Wayland/Xwayland session (there is no standalone X server — `DISPLAY` is empty in a plain shell). Discover it dynamically (do NOT hardcode the auth token — it changes per session):
   ```bash
   XWAYLAND_PID=$(pgrep -f 'Xwayland :' | head -1)
   tr '\0' '\n' < /proc/$XWAYLAND_PID/environ | grep -E 'XAUTHORITY|WAYLAND_DISPLAY|DISPLAY'
   ls /tmp/.X11-unix/
   ls /run/user/1000/.mutter-Xwaylandauth.*
   ```
   Observed (Sep 2026): `DISPLAY=:0`, `XAUTHORITY=/run/user/1000/.mutter-Xwaylandauth.3E7VV3` (suffix `.3E7VV3` is random each session). `:0` is the main Xwayland socket.

3. Launch Chrome:
   ```bash
   export XAUTHORITY=/run/user/1000/.mutter-Xwaylandauth.<token>
   export DISPLAY=:0
   nohup google-chrome-stable >/tmp/chrome-openclaw.log 2>&1 &
   ```
   (Using the extension's `attachOnly` profile, `browser({action:"start"})` will error if the extension isn't connected — launching Chrome manually is the way.)

4. Wait ~8s, then re-check `browser({ action: "status" })` until `running: true` and `cdpReady: true`.

5. Open Messenger:
   ```
   browser({ action: "open", url: "https://www.messenger.com/" })
   ```
   It redirects to the most recent thread; to open a specific thread, use its URL directly: `https://www.messenger.com/t/<thread-id>/`.

## Reading Messages

### Conversation list
Use `browser({ action: "tabs" })` to see which tabs are shared, then take a compact snapshot of the Messenger tab:
```
browser({ action: "snapshot", targetId: "t1", compact: true })
```
The sidebar shows conversation previews with last messages and timestamps. The message area renders under `role="log"` with each message as an article/button containing text and a timestamp label (e.g., "Message envoyé à Jeudi 14:39 par Clara : 3 et 3").

### Scrolling to older messages
Messenger uses React virtual scrolling — only ~30 messages are rendered at a time. To load older messages:

1. Find the scrollable container inside `role="main"` — a div with `overflowY: scroll/auto` where `scrollHeight > clientHeight`
2. Continuously set `scrollTop = 0` at 300ms intervals to trigger the infinite scroll loader:

```js
// Use browser evaluate in the Messenger tab (not the iframe)
for (let i = 0; i < 40; i++) {
  container.scrollTop = 0;
  await new Promise(r => setTimeout(r, 300));
}
```

3. Monitor `scrollHeight` — jumps confirm new messages loaded (validated: 1,853 → 34,803)
4. After scrolling, take a fresh snapshot to read the newly loaded messages

### Jumping to latest
Click the "Accéder au message le plus récent" button that appears when scrolled up, or navigate directly to the conversation URL.

### Searching within a conversation
Click the "Rechercher" button in the conversation info panel, type in the search textbox. Messenger search only searches message text, NOT date separator labels.

## Known Limitations

- **Excel Online/OneDrive**: Spreadsheets load in a cross-origin iframe — browser snapshots work with `frame="iframe[title=\"Office on the web Frame\"]"` but `evaluate` is blocked. Better to download the file and read locally.
- **Date separators**: "Jeudi", "Vendredi" etc. are not searchable text
- **E2E encrypted chats**: Messages show as "Les messages et les appels sont protégés par un chiffrement de bout en bout" — content is not readable
- **Virtual scroll batch size**: Each scroll cycle loads ~1-2 weeks of messages, so reaching very old messages may require many cycles

## Mot du Jour / Tusmo score reporting

For the weekly Mot du Jour / Tusmo score-reporting workflow (thread ID, player mapping, score parsing, Excel write-up), use the `wordle-scores` skill. This skill only covers the generic Messenger reading mechanics above.
