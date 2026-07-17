# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** refactoring, sorted array, block properties, Zig struct, module-as-struct, efficient lookups, generic programming, data structures
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Efficiency, Modularity, Maintainability, Generic Programming, Data Structures

## Summary
Refactored block properties management by introducing a `SortedBlockProperties` function template for efficient property storage and retrieval. Moved all related methods into the `BlockProps` struct to align with Zig's module-as-struct paradigm.

## Explanation
The refactoring aims to improve the efficiency of block property management by using a sorted array approach, which allows for faster lookups and updates compared to the previous static arrays. The introduction of the `SortedBlockProperties` function template provides a generic way to handle both boolean and non-boolean properties, reducing code duplication. By encapsulating all related methods within the `BlockProps` struct, the code better aligns with Zig's module-as-struct design philosophy, enhancing modularity and maintainability. This change also paves the way for future enhancements and optimizations in block property handling.

## Related Questions
- What is the purpose of the `SortedBlockProperties` function template?
- How does the `addBlockProperty` method handle adding properties to the sorted array?
- What changes were made to align with Zig's module-as-struct paradigm?
- How does the `resetSortedProperties` function work?
- What are the benefits of using a sorted array for block property management?
- How does the refactoring improve the efficiency of block property lookups and updates?

*Source: unknown | chunk_id: github_pr_2063_comment_2443327768*
