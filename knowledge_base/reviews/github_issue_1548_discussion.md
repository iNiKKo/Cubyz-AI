# [issues/issue_1548.md] - Issue #1548 discussion

**Type:** review
**Keywords:** crash, unreachable code, deinitialization, inventory, render distance, full log
**Symbols:** reset, deinit, main
**Concepts:** thread safety, memory management, error handling

## Summary
The game crashes when exiting a world after extensive flying and block placement, reaching unreachable code in the reset function.

## Explanation
The game crashes when exiting a world after extensive flying and block placement. The crash occurs upon clicking 'Exit World' in the void roots, resulting in a runtime error with an unreachable code message. Specifically, the error indicates that the code has reached an unreachable state during the `reset` method call on the inventory's client-side synchronization. This suggests a logical flaw or improper handling of certain conditions. The maintainer asks for additional information such as the render distance and full logs to better understand the context and potential causes of this issue.

## Related Questions
- What is the expected behavior of the `reset` method in the inventory's client-side synchronization?
- How does the game handle extensive flying and block placement before exiting a world?
- Are there any known issues with memory management during world deinitialization?
- Can you provide more details on the render distance setting when the crash occurred?
- What additional logging or debugging information can be added to identify the root cause of the unreachable code error?
- How does the game ensure thread safety during world exit operations?

*Source: unknown | chunk_id: github_issue_1548_discussion*
