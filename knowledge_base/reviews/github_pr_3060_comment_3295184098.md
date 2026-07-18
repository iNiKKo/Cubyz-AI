# [src/blocks.zig] - PR #3060 review diff

**Type:** review
**Keywords:** refactor, union(enum), packed struct, capabilities, tool effectiveness, conditional checks, architectural review
**Symbols:** SelectionCapabilities, BackingType, always, custom, toolEffective, allowsSelectionByItem, Block, Item
**Concepts:** union(enum), packed struct, conditional logic

## Summary
Refactored the SelectionCapabilities struct to use a union(enum) with a packed struct for better control over capabilities.

## Explanation
The change refactors the SelectionCapabilities struct from using an optional slice of capabilities to a union(enum) that includes a packed struct. This allows for more granular control over individual capabilities, such as tool effectiveness. The reviewer suggests ensuring that checks are not skipped by properly structuring the conditional logic within the `allowsSelectionByItem` method.

## Related Questions
- What is the purpose of using a union(enum) with a packed struct in SelectionCapabilities?
- How does the refactored `allowsSelectionByItem` method ensure that checks are not skipped?
- What changes were made to the original Capability enum and how do they affect functionality?
- Why was it necessary to use @as(BackingType, @bitCast(self)) in the allowsSelectionByItem method?
- How does this refactoring impact backwards compatibility with existing code?
- Can you explain the potential performance implications of using a packed struct for capabilities?

*Source: unknown | chunk_id: github_pr_3060_comment_3295184098*
