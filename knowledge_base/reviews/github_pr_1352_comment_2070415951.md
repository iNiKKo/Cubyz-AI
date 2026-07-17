# [src/blueprint.zig] - PR #1352 review diff

**Type:** review
**Keywords:** set function, variable pointer, cloning, unnecessary copies, masks implementation, old blocks preservation
**Symbols:** Blueprint, NeverFailingAllocator, Pattern
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `set` function in the `Blueprint` struct has been modified to take a variable pointer instead of cloning the blueprint.

## Explanation
The reviewer pointed out that the caller should be responsible for copying, and suggested changing the `set` function to accept a variable pointer rather than cloning the blueprint. This change aims to prevent unnecessary copies, especially when the `set` function is applied to the clipboard. The reviewer also noted that cloning is not necessary in the current implementation because all values are overwritten, but this could change once masks are implemented, which might require preserving some or all of the old blocks.

## Related Questions
- What is the purpose of the `set` function in the `Blueprint` struct?
- Why was the decision made to change the `set` function to accept a variable pointer?
- How does this change impact memory usage and performance?
- What are the potential implications of implementing masks in the future?
- How can we ensure that the caller is always responsible for copying when using the `set` function?
- What other architectural considerations should be taken into account when modifying the `Blueprint` struct?

*Source: unknown | chunk_id: github_pr_1352_comment_2070415951*
