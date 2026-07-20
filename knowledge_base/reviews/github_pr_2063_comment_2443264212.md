# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** block properties, SortedBlockProperties, memory usage, code readability, modularization, generics, struct consolidation
**Symbols:** SortedBlockProperties, Cmp.less, getBlockPropertyValue, addBlockProperty, clear, isSortedProp, resetSortedProperties, BlockProps
**Concepts:** Code organization, Memory optimization, Generics, Structural refactoring

## Summary
Refactored block properties into a single `BlockProps` struct using a generic function `SortedBlockProperties` to manage boolean and non-boolean properties efficiently.

## Explanation
The refactoring introduces a new function `SortedBlockProperties` that encapsulates the logic for managing block properties in a sorted manner, optimizing memory usage by only storing indices of blocks with specific properties. This approach reduces redundancy and improves efficiency. For boolean properties, `SortedBlockProperties` uses an array to store indices of blocks that have the property set to true, reducing memory usage by avoiding false values for every block. For non-boolean properties, it stores both the index and the value in separate arrays, allowing efficient retrieval using binary search.

The `SortedBlockProperties` function is defined as a generic type that takes two parameters: `sortedBlockSize`, which specifies the maximum number of blocks that can have a property, and `DataType`, which specifies the type of the property. If `DataType` is `bool`, it uses an array to store indices of blocks with the property set to true. For other data types, it stores both the index and the value in separate arrays.

The `getBlockPropertyValue` function retrieves the value of a block property for a given block ID. For boolean properties, it returns true if the block ID is in the array of indices; otherwise, it returns false. For non-boolean properties, it performs a binary search on the index array to find the block ID and then returns the corresponding value.

The `addBlockProperty` function adds a property for a given block ID. If the property value is true (for boolean properties) or if the block ID is not already in the index array (for non-boolean properties), it inserts the block ID into the appropriate position in the index array and updates the data array if necessary.

The `clear` function resets the `SortedBlockProperties` struct by setting its allocated size to zero.

The `isSortedProp` function checks if a given type has the required methods (`clear`, `addBlockProperty`, and `getBlockPropertyValue`) to be considered a sorted property.

The `resetSortedProperties` function clears all properties stored in the `BlockProps` struct during critical architectural reviews or when resetting block properties for testing purposes. It iterates over all fields of the `BlockProps` struct, checks if each field is a sorted property using the `isSortedProp` function, and calls the `clear` method on it.

The reviewer emphasizes improved code organization by consolidating properties into one struct, enhancing readability and maintainability.

## Related Questions
-  What is the purpose of the `SortedBlockProperties` function?
-  How does the `SortedBlockProperties` function handle boolean properties differently from non-boolean properties?
-  Why was it decided to consolidate block properties into one struct?
-  What changes are planned for the `BlockProps` struct in future updates?
-  How does the `resetSortedProperties` function work and when is it called?

*Source: unknown | chunk_id: github_pr_2063_comment_2443264212*
