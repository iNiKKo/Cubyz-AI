# [issues/issue_2410.md] - Issue #2410 discussion

**Type:** review
**Keywords:** game crash, singleplayer world, multiplayer window, port in use, Zig version update, network.zig, WSAEADDRINUSE, AddressInUse
**Symbols:** init, startFromExistingThread, startFromNewThread
**Concepts:** port conflict, error handling, platform normalization

## Summary
The issue involves game crashes when loading a singleplayer world while the multiplayer window is open due to port conflicts.

## Explanation
The problem stems from the server using a default port that may already be in use, causing a crash. The discussion reveals that this behavior was introduced after a Zig version update (d25cdc530d37f50d0f8c82a005bd13abe230696d). Two potential fixes are proposed: modifying the error handling at line 470 in `network.zig` to include `error.WSAEADDRINUSE`, or changing the return type at line 38 to `error.AddressInUse`. The maintainer prefers the second option but suggests normalizing error handling styles across platforms.

## Related Questions
- What is the default port used by the server in Cubyz?
- How does the server handle port conflicts before and after the Zig version update?
- Why was the second fix preferred over the first one?
- Are there any other potential fixes for handling port conflicts in Cubyz?
- How can we ensure that all error handling styles are normalized across platforms in Cubyz?
- What is the impact of using `error.AddressInUse` on Windows systems?
- Can you provide a test case to verify the fix for this issue?
- How does the server determine if a port is already in use?
- What changes were made to the Zig codebase that introduced this issue?
- How can we prevent similar issues from occurring in the future?

*Source: unknown | chunk_id: github_issue_2410_discussion*
