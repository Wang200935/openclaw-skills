---
name: computer_vision_control
description: Observe the current screen, identify UI targets, then control the computer with mouse and keyboard in a careful step-by-step loop. Use when the user wants the agent to look at the screen and operate desktop apps or websites.
---

# Computer Vision Control

Use this skill when the user wants you to operate a computer by **looking at the screen first**, then using **mouse and keyboard** to complete a task.

## Goal

Work in a reliable loop:

1. **See** the current screen or target window.
2. **Identify** the exact UI target.
3. **Act** with the smallest safe mouse/keyboard step.
4. **Re-check** the screen after each important action.
5. Repeat until the task is done.

Do not blindly issue long action chains without checking results.

## Safety rules

- Prefer small, reversible actions.
- Before destructive actions (delete, submit, purchase, send, overwrite, close unsaved work), ask for confirmation unless the user already clearly authorized it.
- If the UI is ambiguous, inspect again instead of guessing.
- If a modal, permission prompt, captcha, 2FA challenge, or unexpected window appears, stop and explain what you need.
- If the available environment does not actually provide screen/mouse/keyboard automation tools, say so plainly and do not pretend.

## Platform/tool strategy

### Preferred tool on macOS: `peekaboo`

If `peekaboo` is available, use it as the primary UI automation tool.

Reliable pattern:

```bash
peekaboo permissions
peekaboo see --annotate --path /tmp/peekaboo-see.png
peekaboo click --on B1
peekaboo type "hello"
```

Useful commands:

- Inspect screen/window: `peekaboo see --annotate`
- Capture screenshot: `peekaboo image`
- Click target: `peekaboo click --on <ID>` or `--coords x,y`
- Type text: `peekaboo type "..."`
- Press keys: `peekaboo press`, `peekaboo hotkey`
- Scroll: `peekaboo scroll`
- Move/drag: `peekaboo move`, `peekaboo drag`, `peekaboo swipe`
- Focus/manage apps: `peekaboo app`, `peekaboo window`, `peekaboo menu`

Before using `peekaboo`, check permissions if needed:

```bash
peekaboo permissions
```

### If not on macOS or `peekaboo` is unavailable

1. Check whether another installed tool in the current environment provides:
   - screenshot capture
   - UI analysis / element targeting
   - mouse movement / click
   - keyboard typing / hotkeys
2. If a real tool exists, use the same **see -> act -> verify** loop.
3. If no such tool is available, say exactly what is missing and what would need to be installed or enabled.

Do not claim to have clicked, typed, or seen something unless you truly used a tool that can do it.

## Operating procedure

### 1) Understand the task

Clarify the end goal in one sentence, for example:
- log into a site
- download a report
- fill a form
- change a setting in an app

### 2) Establish visual state

Inspect the relevant screen/window first.
If available, save annotated screenshots when that helps identify targets.

### 3) Take one small action

Examples:
- focus the app/window
- click a single button
- type into one field
- press one hotkey
- scroll a small amount

### 4) Verify result

Re-read the screen after actions that may change layout, navigation, focus, or state.

### 5) Continue carefully

Prefer sequences like:
- see -> click -> see -> type -> see -> submit
- see -> scroll a bit -> see -> click
- see -> hotkey -> see

## Reliability heuristics

- Prefer targeting by UI element ID over raw coordinates when available.
- Use coordinates only when the UI target is visually clear and stable.
- If typing into a field, first ensure the field is focused.
- If a page is loading, wait briefly and inspect again instead of assuming completion.
- When multiple similar buttons exist, describe which one you intend to use before clicking.

## Communication style while using this skill

Be short and concrete.
Explain:
- what you observed
- what you are about to do next
- why you stopped, if blocked

## Example flow with `peekaboo`

```bash
peekaboo app launch "Safari" --open https://example.com/login
peekaboo see --app Safari --window-title "Login" --annotate --path /tmp/login.png
peekaboo click --on B3 --app Safari
peekaboo type "user@example.com" --app Safari
peekaboo press tab --app Safari
peekaboo type "password" --app Safari --return
peekaboo see --app Safari --annotate --path /tmp/post-login.png
```

## Success criteria

The task is complete only when you have visually verified the expected result, or the user explicitly says the result is good enough.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\agents\computer-vision-control\SKILL.md
---
---
name: computer_vision_control
description: Observe the current screen, identify UI targets, then control the computer with mouse and keyboard in a careful step-by-step loop. Use when the user wants the agent to look at the screen and operate desktop apps or websites.
---

# Computer Vision Control

Use this skill when the user wants you to operate a computer by **looking at the screen first**, then using **mouse and keyboard** to complete a task.

## Goal

Work in a reliable loop:

1. **See** the current screen or target window.
2. **Identify** the exact UI target.
3. **Act** with the smallest safe mouse/keyboard step.
4. **Re-check** the screen after each important action.
5. Repeat until the task is done.

Do not blindly issue long action chains without checking results.

## Safety rules

- Prefer small, reversible actions.
- Before destructive actions (delete, submit, purchase, send, overwrite, close unsaved work), ask for confirmation unless the user already clearly authorized it.
- If the UI is ambiguous, inspect again instead of guessing.
- If a modal, permission prompt, captcha, 2FA challenge, or unexpected window appears, stop and explain what you need.
- If the available environment does not actually provide screen/mouse/keyboard automation tools, say so plainly and do not pretend.

## Platform/tool strategy

### Preferred tool on macOS: `peekaboo`

If `peekaboo` is available, use it as the primary UI automation tool.

Reliable pattern:

```bash
peekaboo permissions
peekaboo see --annotate --path /tmp/peekaboo-see.png
peekaboo click --on B1
peekaboo type "hello"
```

Useful commands:

- Inspect screen/window: `peekaboo see --annotate`
- Capture screenshot: `peekaboo image`
- Click target: `peekaboo click --on <ID>` or `--coords x,y`
- Type text: `peekaboo type "..."`
- Press keys: `peekaboo press`, `peekaboo hotkey`
- Scroll: `peekaboo scroll`
- Move/drag: `peekaboo move`, `peekaboo drag`, `peekaboo swipe`
- Focus/manage apps: `peekaboo app`, `peekaboo window`, `peekaboo menu`

Before using `peekaboo`, check permissions if needed:

```bash
peekaboo permissions
```

### If not on macOS or `peekaboo` is unavailable

1. Check whether another installed tool in the current environment provides:
   - screenshot capture
   - UI analysis / element targeting
   - mouse movement / click
   - keyboard typing / hotkeys
2. If a real tool exists, use the same **see -> act -> verify** loop.
3. If no such tool is available, say exactly what is missing and what would need to be installed or enabled.

Do not claim to have clicked, typed, or seen something unless you truly used a tool that can do it.

## Operating procedure

### 1) Understand the task

Clarify the end goal in one sentence, for example:
- log into a site
- download a report
- fill a form
- change a setting in an app

### 2) Establish visual state

Inspect the relevant screen/window first.
If available, save annotated screenshots when that helps identify targets.

### 3) Take one small action

Examples:
- focus the app/window
- click a single button
- type into one field
- press one hotkey
- scroll a small amount

### 4) Verify result

Re-read the screen after actions that may change layout, navigation, focus, or state.

### 5) Continue carefully

Prefer sequences like:
- see -> click -> see -> type -> see -> submit
- see -> scroll a bit -> see -> click
- see -> hotkey -> see

## Reliability heuristics

- Prefer targeting by UI element ID over raw coordinates when available.
- Use coordinates only when the UI target is visually clear and stable.
- If typing into a field, first ensure the field is focused.
- If a page is loading, wait briefly and inspect again instead of assuming completion.
- When multiple similar buttons exist, describe which one you intend to use before clicking.

## Communication style while using this skill

Be short and concrete.
Explain:
- what you observed
- what you are about to do next
- why you stopped, if blocked

## Example flow with `peekaboo`

```bash
peekaboo app launch "Safari" --open https://example.com/login
peekaboo see --app Safari --window-title "Login" --annotate --path /tmp/login.png
peekaboo click --on B3 --app Safari
peekaboo type "user@example.com" --app Safari
peekaboo press tab --app Safari
peekaboo type "password" --app Safari --return
peekaboo see --app Safari --annotate --path /tmp/post-login.png
```

## Success criteria

The task is complete only when you have visually verified the expected result, or the user explicitly says the result is good enough.








