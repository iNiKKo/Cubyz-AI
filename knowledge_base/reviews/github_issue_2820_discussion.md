# [issues/issue_2820.md] - Issue #2820 discussion

**Type:** review
**Keywords:** crash, world entry, null pointer, initComponent, loadWorldAssets, pull request #2821, runtime error, thread safety
**Symbols:** initComponent, loadWorldAssets, init, startFromExistingThread, startFromNewThread, callFn__anon_123785, entryFn
**Concepts:** null pointer check, runtime error, thread safety

## Summary
The issue involves a crash when entering a world due to a null pointer check in the `initComponent` function.

## Explanation
The issue involves a crash when entering a world due to a null pointer check in the `initComponent` function at line 41 of `entity.zig`. The error occurs because `tmpReceiveList.items[id] == null`, leading to a runtime error. This error propagates through several functions including `loadWorldAssets`, `init`, and `startFromExistingThread`. Specifically, the crash is triggered by the following sequence of function calls:

```
C:\Users\argma\dev\Cubyz4\src\entity.zig:41:27: 0x7ff79747f2b0 in initComponent (Cubyz_zcu.obj)
if (tmpReceiveList.items[id] == null) {
                          ^
C:\Users\argma\dev\Cubyz4\src\assets.zig:701:28: 0x7ff797479f44 in loadWorldAssets (Cubyz_zcu.obj)
main.entity.initComponent();
                           ^
C:\Users\argma\dev\Cubyz4\src\server\world.zig:507:34: 0x7ff7974a8390 in init (Cubyz_zcu.obj)
try main.assets.loadWorldAssets(try std.fmt.allocPrint(arena.allocator, "{s}/saves/{s}/assets/", .{files.cubyzDirStr(), path}), self.blockPalette, self.itemPalette, self.toolPalette, self.biomePalette, self.entityComponentPalette);
                                 ^
C:\Users\argma\dev\Cubyz4\src\server\server.zig:535:26: 0x7ff7973fc2bf in init (Cubyz_zcu.obj)
world = ServerWorld.init(name) catch |err| {
                         ^
C:\Users\argma\dev\Cubyz4\src\server\server.zig:675:6: 0x7ff7973bad04 in startFromExistingThread (Cubyz_zcu.obj)
init(name, port);
     ^
C:\Users\argma\dev\Cubyz4\src\server\server.zig:670:25: 0x7ff7977800b1 in startFromNewThread (Cubyz_zcu.obj)
startFromExistingThread(name, port);
                        ^
C:\Users\argma\dev\Cubyz4\compiler\zig\lib\std\Thread.zig:558:13: 0x7ff7976900c4 in callFn__anon_123785 (Cubyz_zcu.obj)
            @call(.auto, f, args);
            ^
C:\Users\argma\dev\Cubyz4\compiler\zig\lib\std\Thread.zig:671:30: 0x7ff797598215 in entryFn (Cubyz_zcu.obj)
                return callFn(f, self.fn_args);
```
The user mentions that this should have been fixed by pull request #2821. However, there is no additional context provided about the nature of the fix or any concerns regarding regression.

## Related Questions
- What was the specific fix introduced in pull request #2821?
- Are there any known regressions or side effects from the changes in #2821?
- How does the `initComponent` function handle null values in other contexts?
- Can you provide more details on how the `tmpReceiveList.items[id]` can become null?
- Is there a possibility of race conditions affecting `tmpReceiveList.items[id]`?
- What is the purpose of the `loadWorldAssets` function, and how does it interact with `initComponent`?

*Source: unknown | chunk_id: github_issue_2820_discussion*
