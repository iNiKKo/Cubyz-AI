# [issues/issue_2783.md] - Issue #2783 discussion

**Type:** review
**Keywords:** multiplayer, Linux, Windows, IP swapping, crashing, port instability, LAN option
**Concepts:** thread safety, networking, crashes

## Summary
The issue describes problems with multiplayer functionality on both Linux and Windows, including IP address swapping and crashes when joining a game.

## Explanation
The user reports that when trying to join someone on the same network, the IP addresses keep swapping between them, which might cause issues with player invitations requiring a stable IP. Additionally, there are crashes in the multiplayer window, particularly on Windows where the game becomes unresponsive and then crashes, and on Linux where it just becomes black before crashing. The user suggests that these issues might be related to thread problems or port instability. There is also a suggestion for adding a button to automatically fill in the IP address if both players are on the same network.

## Related Questions
- What is the root cause of the IP address swapping issue in multiplayer?
- How does the crash in the multiplayer window on Windows occur, and what could be causing it?
- Why does the game become black on Linux before crashing, and how can this be fixed?
- Is there a specific thread problem that might be causing these issues, and if so, how can it be addressed?
- How can the port instability issue be resolved to ensure stable multiplayer connections?
- What changes are needed to add a LAN option for automatically filling in the IP address when both players are on the same network?

*Source: unknown | chunk_id: github_issue_2783_discussion*
