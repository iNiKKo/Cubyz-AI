# [issues/issue_1314.md] - Issue #1314 discussion

**Type:** review
**Keywords:** timestamp, monotonic, system time, user error, Zig standard library
**Symbols:** std.time.nanoTimestamp, std.time.microTimestamp, std.time.milliTimestamp
**Concepts:** monotonic timestamps, system time manipulation

## Summary
The issue discusses the potential for breaking the game by changing the system time during runtime due to non-monotonic timestamp usage.

## Explanation
The issue discusses the potential for breaking the game by changing the system time during runtime due to non-monotonic timestamp usage. The maintainer suggests that if users alter their system time while the game is running, it's a user error rather than a bug to be addressed immediately. This affects all uses of `std.time.nanoTimestamp`, `std.time.microTimestamp`, and `std.time.milliTimestamp`. The issue is currently on hold until it becomes a significant problem or there is a straightforward way to implement monotonic timestamps using Zig's standard library.

## Related Questions
- What are the potential consequences of using non-monotonic timestamps in a game?
- How can monotonic timestamps be implemented in Zig's standard library?
- Are there any other parts of the codebase that might be affected by system time changes?
- Why is the maintainer not prioritizing this issue at the moment?
- What are the benefits and drawbacks of using monotonic timestamps in games?
- How can we detect if a user has changed their system time while the game is running?

*Source: unknown | chunk_id: github_issue_1314_discussion*
