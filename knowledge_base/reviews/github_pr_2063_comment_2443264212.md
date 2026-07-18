# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** block properties, SortedBlockProperties, memory usage, code readability, modularization, generics, struct consolidation
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Code organization, Memory optimization, Generics, Structural refactoring

## Summary
Refactored block properties into a single `BlockProps` struct using a generic function `SortedBlockProperties` to manage boolean and non-boolean properties efficiently.

## Explanation
The refactoring introduces a new function `SortedBlockProperties` that encapsulates the logic for managing block properties in a sorted manner. This approach optimizes memory usage by only storing indices of blocks with specific properties, reducing redundancy. The use of generics allows handling both boolean and non-boolean properties within the same framework. The reviewer emphasizes improved code organization by consolidating properties into one struct, enhancing readability and maintainability. Additionally, the reviewer plans to make this struct public in future changes as part of a broader effort to modularize the codebase.

## Related Questions
- What is the purpose of the `SortedBlockProperties` function?
- How does the `SortedBlockProperties` function handle boolean properties differently from non-boolean properties?
- Why was it decided to consolidate block properties into one struct?
- What changes are planned for the `BlockProps` struct in future updates?
- How does the `resetSortedProperties` function work and when is it called?
- What potential performance improvements can be expected from this refactoring?

*Source: unknown | chunk_id: github_pr_2063_comment_2443264212*
