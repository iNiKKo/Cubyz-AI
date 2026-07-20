# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** block properties, SortedBlockProperties, memory usage, code readability, modularization, generics, struct consolidation
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Code organization, Memory optimization, Generics, Structural refactoring

## Summary
Refactored block properties into a single `BlockProps` struct using a generic function `SortedBlockProperties` to manage boolean and non-boolean properties efficiently.

## Explanation
The refactoring introduces a new function `SortedBlockProperties` that encapsulates the logic for managing block properties in a sorted manner, optimizing memory usage by only storing indices of blocks with specific properties. This approach reduces redundancy and improves efficiency. For boolean properties, `SortedBlockProperties` uses an array to store indices of blocks that have the property set to true, reducing memory usage by avoiding false values for every block. For non-boolean properties, it stores both the index and the value in separate arrays, allowing efficient retrieval using binary search. The reviewer emphasizes improved code organization by consolidating properties into one struct, enhancing readability and maintainability. Additionally, the `resetSortedProperties` function clears all properties stored in the `BlockProps` struct during critical architectural reviews or when resetting block properties for testing purposes.

## Related Questions
- What is the purpose of the `SortedBlockProperties` function?
- How does the `SortedBlockProperties` function handle boolean properties differently from non-boolean properties?
- Why was it decided to consolidate block properties into one struct?
- What changes are planned for the `BlockProps` struct in future updates?
- How does the `resetSortedProperties` function work and when is it called?

*Source: unknown | chunk_id: github_pr_2063_comment_2443264212*
