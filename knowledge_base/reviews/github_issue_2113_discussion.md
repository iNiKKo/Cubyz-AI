# [issues/issue_2113.md] - Issue #2113 discussion

**Type:** review
**Keywords:** crash, workbench, network.zig, 1286, null value, thread safety, singleplayer, server, commit 6d0fe85, commit 0f2d4bb
**Symbols:** receive, sendFailure, self.receiveBuffer.receive, entryFn
**Concepts:** thread safety, null value handling

## Summary
The issue involves a crash when clicking the button in the workbench, occurring since commit 6d0fe85. The problem persists on both singleplayer and server environments.

## Explanation
The crash is caused by an attempt to use a null value in the network handling code at `network.zig:1286`. Reviewers are concerned about the potential for thread safety issues and the need to ensure that all values are properly initialized before use. The discussion suggests focusing on the singleplayer experience, as both the user and another tester can replicate the issue on commit 6d0fe85 but not on the previous commit (0f2d4bb). There is speculation that the server's version might be a factor.

## Related Questions
- What is the potential impact of using a null value in network handling?
- How can thread safety be improved to prevent similar crashes?
- Is there any specific initialization step missing that could cause this null value error?
- Can the crash be replicated consistently on both singleplayer and server environments?
- What changes were introduced in commit 6d0fe85 that might have caused this issue?
- How can we ensure that all values are properly initialized before use in network operations?

*Source: unknown | chunk_id: github_issue_2113_discussion*
