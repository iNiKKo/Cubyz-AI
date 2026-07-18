# [issues/issue_2729.md] - Issue #2729 discussion

**Type:** review
**Keywords:** non-zero refcount, panic, unreachable code, deinit, server.zig, assertion failure, player cleanup, sync system, kick command, reproducible bug
**Symbols:** deinit, server.zig, refCount, assert, std.debug.assert
**Concepts:** thread safety, memory management, reference counting, cleanup logic

## Summary
A non-zero reference count on a user object causes a panic when leaving a world with multiple clients.

## Explanation
The issue arises from a non-zero reference count on a user object during the deinitialization process. This leads to an assertion failure in the `deinit` function of the server module, causing a crash. The maintainer suspects that there might be an issue with player cleanup logic, especially after restructuring the sync system. The user reports that the bug is highly reproducible when using the kick command and has been observed consistently since recent changes.

## Related Questions
- What is the current state of the reference counting mechanism in Cubyz?
- Are there any known issues with player cleanup logic after recent changes?
- How can we ensure that the reference count is correctly managed during user deinitialization?
- What steps should be taken to prevent similar assertion failures in the future?
- Can you provide a detailed analysis of the sync system restructuring and its impact on player management?
- Is there any logging or debugging information available to help trace the origin of the non-zero reference count?

*Source: unknown | chunk_id: github_issue_2729_discussion*
