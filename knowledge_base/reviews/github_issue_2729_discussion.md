# [issues/issue_2729.md] - Issue #2729 discussion

**Type:** review
**Keywords:** non-zero refcount, panic, unreachable code, deinit, server.zig, assertion failure, player cleanup, sync system, kick command, reproducible bug
**Symbols:** deinit, server.zig, refCount, assert, std.debug.assert
**Concepts:** thread safety, memory management, reference counting, cleanup logic

## Summary
A non-zero reference count on a user object causes a panic when leaving a world with multiple clients.

## Explanation
A non-zero reference count on a user object causes a panic when leaving a world with multiple clients. The issue arises during the deinitialization process in `server.zig`, leading to an assertion failure at `/home/Wunka/Documents/Cubyz/master/src/server/server.zig:161`. This results in a crash, as observed by the following error message:

```shell
thread 5552 panic: reached unreachable code
/home/Wunka/Documents/Cubyz/master/compiler/zig/lib/std/debug.zig:417:14: 0x1470add in assert (Cubyz)
    if (!ok) unreachable; // assertion failure
             ^
/home/Wunka/Documents/Cubyz/master/src/server/server.zig:161:19: 0x1654959 in deinit (Cubyz)
  std.debug.assert(self.refCount.load(.monotonic) == 0);
                  ^
/home/Wunka/Documents/Cubyz/master/src/server/server.zig:546:14: 0x158c1a0 in deinit (Cubyz)
  user.deinit();
             ^
/home/Wunka/Documents/Cubyz/master/src/server/server.zig:663:14: 0x154976b in startFromExistingThread (Cubyz)
 defer deinit();
             ^
/home/Wunka/Documents/Cubyz/master/src/server/server.zig:657:25: 0x1906abf in startFromNewThread (Cubyz)
 startFromExistingThread(name, port);
                        ^
/home/Wunka/Documents/Cubyz/master/compiler/zig/lib/std/Thread.zig:558:13: 0x1821a9e in callFn__anon_128433 (Cubyz)
            @call(.auto, f, args);
            ^
/home/Wunka/Documents/Cubyz/master/compiler/zig/lib/std/Thread.zig:830:30: 0x17294cf in entryFn (Cubyz)
                return callFn(f, args_ptr.*);
                             ^
???:?:?: 0x7f1a1e6dd979 in ??? (/usr/lib/libc.so.6)
???:?:?: 0x7f1a1e7612bb in ??? (/usr/lib/libc.so.6)
./debug_linux.sh: line 31:  5451 Aborted                    (core dumped) ./zig-out/bin/Cubyz
```
The maintainer suspects that there might be an issue with player cleanup logic, especially after restructuring the sync system. The user reports that the bug is highly reproducible when using the kick command and has been observed consistently since recent changes.

## Related Questions
- What is the current state of the reference counting mechanism in Cubyz?
- Are there any known issues with player cleanup logic after recent changes?
- How can we ensure that the reference count is correctly managed during user deinitialization?
- What steps should be taken to prevent similar assertion failures in the future?
- Can you provide a detailed analysis of the sync system restructuring and its impact on player management?
- Is there any logging or debugging information available to help trace the origin of the non-zero reference count?

*Source: unknown | chunk_id: github_issue_2729_discussion*
