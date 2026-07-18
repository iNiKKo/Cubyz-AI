# [issues/issue_2783.md] - Issue #2783 discussion

**Type:** review
**Keywords:** multiplayer, Linux, Windows, IP swapping, crashing, port instability, LAN option
**Concepts:** thread safety, networking, crashes

## Summary
The issue describes problems with multiplayer functionality on both Linux and Windows, including IP address swapping and crashes when joining a game.

## Explanation
The issue describes problems with multiplayer functionality on both Linux and Windows. When trying to join someone on the same network, the IP addresses keep swapping between players, which can cause issues with player invitations requiring a stable IP address. Additionally, there are crashes in the multiplayer window, particularly on Windows where the game becomes unresponsive for about 5 seconds before crashing, and on Linux where it turns black before crashing. The user suggests that these issues might be related to thread problems or port instability as mentioned in issue #2726. There is also a suggestion for adding a button to automatically fill in the IP address if both players are on the same network, which could help simplify the process of joining multiplayer games on the local network.

## Related Questions
-  What specific steps can be taken to resolve the issue of IP addresses swapping between players?
-  How does the crash in the multiplayer window on Windows occur, and what is the exact nature of this problem?
-  Why does the game become black on Linux before crashing, and how can this be addressed?
-  Is there a specific thread problem that might be causing these issues, and if so, how can it be resolved?
-  How can the port instability issue be fixed to ensure stable multiplayer connections?
-  What changes are needed to add a LAN option for automatically filling in the IP address when both players are on the same network?

*Source: unknown | chunk_id: github_issue_2783_discussion*
