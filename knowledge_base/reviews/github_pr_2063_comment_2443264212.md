# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** block properties, SortedBlockProperties, memory usage, code readability, modularization, generics, struct consolidation
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Code organization, Memory optimization, Generics, Structural refactoring

## Summary
Refactored block properties into a single `BlockProps` struct using a generic function `SortedBlockProperties` to manage boolean and non-boolean properties efficiently.

## Explanation
The refactoring introduces a new function `SortedBlockProperties` that encapsulates the logic for managing block properties in a sorted manner. This approach optimizes memory usage by only storing indices of blocks with specific properties, reducing redundancy. The use of generics allows handling both boolean and non-boolean properties within the same framework.

For boolean properties, `SortedBlockProperties` uses an array to store indices of blocks that have the property set to true. If a block does not have the property, it is not included in the array. This reduces memory usage by avoiding storing false values for every block.

For non-boolean properties, `SortedBlockProperties` stores both the index and the value of the property in separate arrays. The indices are sorted, allowing efficient retrieval using binary search. This approach ensures that only blocks with specific properties are stored, optimizing memory usage.

The reviewer emphasizes improved code organization by consolidating properties into one struct, enhancing readability and maintainability. Additionally, the reviewer plans to make this struct public in future changes as part of a broader effort to modularize the codebase.

## Related Questions
-  What is the purpose of the `SortedBlockProperties` function?
  The `SortedBlockProperties` function manages block properties in a sorted manner, optimizing memory usage by only storing indices of blocks with specific properties.

- How does the `SortedBlockProperties` function handle boolean properties differently from non-boolean properties?
  For boolean properties, `SortedBlockProperties` uses an array to store indices of blocks that have the property set to true. If a block does not have the property, it is not included in the array. For non-boolean properties, `SortedBlockProperties` stores both the index and the value of the property in separate arrays.

- Why was it decided to consolidate block properties into one struct?
  Consolidating block properties into one struct improves code organization, enhancing readability and maintainability.

- What changes are planned for the `BlockProps` struct in future updates?
  The reviewer plans to make the `BlockProps` struct public as part of a broader effort to modularize the codebase.

- How does the `resetSortedProperties` function work and when is it called?
  The `resetSortedProperties` function clears all properties stored in the `BlockProps` struct. It is called during critical architectural reviews or when resetting block properties for testing purposes.

- What potential performance improvements can be expected from this refactoring?
  This refactoring optimizes memory usage by only storing indices of blocks with specific properties, reducing redundancy. Additionally, the use of generics allows handling both boolean and non-boolean properties within the same framework, improving code efficiency.

*Source: unknown | chunk_id: github_pr_2063_comment_2443264212*
