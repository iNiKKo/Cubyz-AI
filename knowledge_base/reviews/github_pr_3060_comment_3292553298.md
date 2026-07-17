# [src/blocks.zig] - PR #3060 review diff

**Type:** review
**Keywords:** refactoring, union(enum), backing type, memory efficient, coercion, selection capabilities, toolEffective, Block, Item
**Symbols:** SelectionCapabilities, backingType, never, always, custom, toolEffective, allowsSelectionByItem, Block, Item
**Concepts:** memory efficiency, union(enum), enum coercion, selection logic

## Summary
Refactored `SelectionCapabilities` to use a union(enum) with a backing type for more efficient storage and selection logic.

## Explanation
The change refactors the `SelectionCapabilities` struct to use a union(enum) with a backing type, replacing the previous array of capabilities. This approach is more memory-efficient as it uses a single byte to represent different selection states. The reviewer notes that coercion from enum literals to void union fields is possible, making the new design redundant in some cases. The refactoring aims to improve performance by reducing memory usage and potentially simplifying the logic for checking selection capabilities.

## Related Questions
- How does the new `SelectionCapabilities` union(enum) improve memory usage compared to the previous array of capabilities?
- What is the purpose of the `backingType` in the refactored `SelectionCapabilities`?
- Can you explain how coercion from enum literals to void union fields works in this context?
- How does the new design affect the performance of selection checks in Cubyz?
- Are there any potential regressions introduced by this refactoring that need to be tested?
- What are the implications of using a single byte for different selection states in `SelectionCapabilities`?

*Source: unknown | chunk_id: github_pr_3060_comment_3292553298*
