# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** refactoring, block properties, binary search, memory usage, code organization, template metaprogramming, helper functions, boolean properties, non-boolean properties, module splitting
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, compare, getBlockSortedIdx, getBlockPropertyValueByIdx, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Code organization, Binary search, Memory efficiency, Template metaprogramming

## Summary
Refactored block properties management by introducing a `SortedBlockProperties` function to handle boolean and non-boolean properties efficiently using binary search. Added helper functions for adding, retrieving, and clearing properties.

## Explanation
The refactoring aims to improve code organization and efficiency by consolidating block property management into a single struct. The use of binary search allows for faster retrieval of properties, especially for boolean values where the presence or absence of a property is indicated by the existence in an array. This approach reduces memory usage compared to having separate arrays for each property. The `SortedBlockProperties` function template handles both boolean and non-boolean types, providing a flexible solution that can be reused across different block properties. Additionally, helper functions like `addBlockProperty`, `getBlockPropertyValue`, and `clear` ensure that the properties are managed safely and efficiently. This refactoring is part of a larger effort to split the `blocks.zig` file into smaller modules for better maintainability.

## Related Questions
- How does the `SortedBlockProperties` function handle boolean and non-boolean types differently?
- What is the purpose of the `isSortedProp` function in this refactoring?
- How does the `resetSortedProperties` function contribute to maintaining clean state between different block property sets?
- Can you explain the use of binary search in retrieving block properties and why it is efficient?
- What are the benefits of consolidating all block properties into a single struct as part of this refactoring?
- How does the `addBlockProperty` function ensure that properties are added in sorted order?
- What potential issues could arise if the size of the array for storing block properties is exceeded?
- How does the `clear` function help in managing memory and state within the `SortedBlockProperties` struct?
- What architectural changes are planned for splitting the `blocks.zig` file into smaller modules?
- How does this refactoring impact the performance of property retrieval operations?

*Source: unknown | chunk_id: github_pr_2063_comment_2443264212*
