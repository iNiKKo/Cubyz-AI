# [issues/issue_385.md] - Issue #385 discussion

**Type:** review
**Keywords:** test -t 0, xterm, konsole, gnome-terminal, xfce4-terminal, mate-terminal, unity, pantheon-terminal, screen, logging
**Concepts:** terminal detection, user experience, desktop environment

## Summary
Discussion on handling terminal execution for Linux users when running scripts from the file explorer.

## Explanation
The issue revolves around the lack of default terminal opening behavior when executing bash files from the file explorer. The discussion explores various approaches to detect and open a terminal, such as checking if one is already available using `test -t 0`. However, identifying the correct terminal application for different desktop environments (e.g., X11, KDE, GNOME) introduces complexity due to non-standardized terminal names. Here are common terminal applications compiled from [this SO post](https://superuser.com/questions/215483/how-can-i-open-a-new-terminal-window-from-a-terminal-in-linux):

- For X11 -> `xterm`
- For Kde -> `konsole`
- For GNOME -> `gnome-terminal`
- For xfce4 -> `xfce4-terminal`
- For Cinnamon -> `x-terminal-emulator`
- For MATE -> `mate-terminal --window`
- For Unity -> `gnome-terminal --profile=Default`
- For Pantheon -> `pantheon-terminal -w ''`

Alternative solutions like piping output to `screen` or logging are considered but seen as less user-friendly. The team ultimately decides against implementing automatic terminal detection due to the added complexity and potential confusion.

## Related Questions
- How can we detect if a terminal is already available in the current environment?
- What are the potential drawbacks of implementing automatic terminal detection for different desktop environments?
- Why was piping output to `screen` or logging considered as an alternative solution?
- Can you provide examples of how to check for terminal availability using `test -t 0`?
- How might browser sniffing on the web relate to feature sniffing in this context?
- What are the advantages and disadvantages of asking users to open Cubyz in a terminal manually?

*Source: unknown | chunk_id: github_issue_385_discussion*
