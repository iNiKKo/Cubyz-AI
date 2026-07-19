# [issues/issue_1548.md] - Issue #1548 discussion

**Type:** review
**Keywords:** crash, unreachable code, deinitialization, inventory, render distance, full log
**Symbols:** reset, deinit, main
**Concepts:** thread safety, memory management, error handling

## Summary
The game crashes when exiting a world after extensive flying and block placement, reaching unreachable code in the reset function.

## Explanation
**Summary**
The game crashes when exiting a world after extensive flying and block placement, reaching unreachable code in the reset function.

**Explanation**
The game crashes when exiting a world after extensive flying and block placement. The crash occurs upon clicking 'Exit World' in the void roots, resulting in a runtime error with an unreachable code message. Specifically, the error indicates that the code has reached an unreachable state during the `reset` method call on the inventory's client-side synchronization. This suggests a logical flaw or improper handling of certain conditions. The maintainer asks for additional information such as the render distance and full logs to better understand the context and potential causes of this issue.

The error message includes the following stack trace:
```
thread 11116 panic: reached unreachable code
/home/gfh/Cubyz/src/utils.zig:539:27: 0x138b0bd in reset (Cubyzig)
   const result = self.mem[self.startIndex];
                          ^
/home/gfh/Cubyz/src/game.zig:692:45: 0x13467bc in deinit (Cubyzig)
  main.items.Inventory.Sync.ClientSide.reset();
                                            ^
/home/gfh/Cubyz/src/main.zig:725:17: 0x1334d93 in main (Cubyzig)
    world.deinit();
                ^
/home/gfh/Cubyz/compiler/zig/lib/std/start.zig:647:22: 0x13202a9 in main (Cubyzig)
            root.main();
                     ^
???:?:?: 0x7df572bbd6b4 in ??? (libc.so.6)
Unwind information for `libc.so.6:0x7df572bbd6b4` was not available, trace may be incomplete

???:?:?: 0x7df572bbd768 in ??? (libc.so.6)
???:?:?: 0x12f1c54 in ??? (???)
```
The maintainer asks for the render distance and full logs to better understand the context and potential causes of this issue.

## Related Questions
- What is the expected behavior of the `reset` method in the inventory's client-side synchronization?
- How does the game handle extensive flying and block placement before exiting a world?
- Are there any known issues with memory management during world deinitialization?
- Can you provide more details on the render distance setting when the crash occurred?
- What additional logging or debugging information can be added to identify the root cause of the unreachable code error?
- How does the game ensure thread safety during world exit operations?

*Source: unknown | chunk_id: github_issue_1548_discussion*
