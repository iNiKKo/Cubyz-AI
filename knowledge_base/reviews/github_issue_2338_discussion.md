# [issues/issue_2338.md] - Issue #2338 discussion

**Type:** review
**Keywords:** UDP, std.Io.net, posix sockets, winsock2, Zig, Windows-specific code
**Concepts:** networking, cross-platform compatibility, standard library

## Summary
Discussion about using Zig's standard library for UDP networking instead of POSIX sockets or Winsock2, aiming to reduce Windows-specific code.

## Explanation
The discussion revolves around the potential benefits of utilizing Zig's standard library for network operations, specifically for UDP. The current implementation uses a placeholder function `@panic("TODO netSendWindows");` while Zig's standard library provides a link to its networking functions. There is an ongoing issue [#25746](https://github.com/ziglang/zig/issues/25746) tracking the Windows part of this functionality. A user was able to bring their draft PR #2466 to the newest version, which serves as a starting point or proof of concept for using Zig's standard library for network operations.

## Related Questions
- What is the current status of Zig's support for Windows networking?
- How can we leverage Zig's standard library to improve cross-platform compatibility in Cubyz?
- Is there a specific issue or PR that addresses the use of UDP in Zig?
- What are the potential benefits and drawbacks of using Zig's standard library for network operations?
- How does the current implementation handle Windows-specific networking code in Cubyz?
- Are there any performance considerations when switching to Zig's standard library for networking?

*Source: unknown | chunk_id: github_issue_2338_discussion*
