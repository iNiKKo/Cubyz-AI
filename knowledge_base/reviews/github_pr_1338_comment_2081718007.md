# [src/blocks.zig] - PR #1338 review diff

**Type:** review
**Keywords:** TickFunction, TouchFunction, NamedCallbacks, init, deinit, getFunctionPointer, architectural review
**Symbols:** Block, TickFunction, TickFunctions, utils.NamedCallbacks
**Concepts:** refactoring, code organization, architectural design

## Summary
Refactored block touch handling to introduce a new tick function and updated the associated data structures.

## Explanation
The change introduces a new `TickFunction` type and corresponding `TickFunctions` struct, replacing the previous `TouchFunction` and `TouchFunctions`. The reviewer suggests declaring the `NamedCallbacks` instance directly outside the struct for potential architectural simplicity. This refactoring aims to improve code organization and maintainability by separating concerns related to block ticking from other interactions.

## Related Questions
- What is the purpose of the `TickFunction` type?
- How does the new `TickFunctions` struct differ from the old `TouchFunctions`?
- Why was the suggestion made to declare `NamedCallbacks` outside the struct?
- What are the benefits of separating block ticking from other interactions?
- How is memory management handled in the new `TickFunctions` struct?
- Can you explain the role of the `init` and `deinit` methods in the `TickFunctions` struct?

*Source: unknown | chunk_id: github_pr_1338_comment_2081718007*
