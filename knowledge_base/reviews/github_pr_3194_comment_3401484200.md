# [src/Inventory.zig] - PR #3194 review diff

**Type:** review
**Keywords:** inventory, sort, compress, insertion sort, item comparison, tag retrieval
**Symbols:** ClientInventory, sortItems, compressItems, SortContext, lessThan, swap, getTagsFromItem
**Concepts:** Sorting Algorithm, Item Management, Code Organization

## Summary
Added functions to sort and compress items in the client inventory, including context for sorting logic.

## Explanation
The changes introduce two new functions: `sortItems` and `compressItems`. The `compressItems` function iterates through the inventory to merge identical items into a single stack. If items have different amounts, it deposits the smaller amount into the larger one. The `sortItems` function first calls `compressItems` and then sorts the remaining items using an insertion sort algorithm with a custom context (`SortContext`). The `SortContext` struct provides methods for comparing items (`lessThan`) and swapping slots (`swap`). The `lessThan` method handles null items by returning false if itemA is null and true if itemB is null. It also prioritizes procedural items over non-procedural ones. Tags are retrieved from different types of items using the `getTagsFromItem` function, which checks if the item is null, procedural, or base and returns the appropriate tags. The reviewer suggests moving the logic in `getTagsFromItem` into the `Item` struct to improve code organization.

The sorting algorithm handles null items by returning false if itemA is null and true if itemB is null. It also prioritizes procedural items over non-procedural ones. Tags are compared lexicographically, and if tags have different lengths, the shorter one is considered less than the longer one. If all tags are equal, the item IDs are compared.

The `ignoredSlotCount` parameter in the `sortItems` function specifies the number of slots at the beginning of the inventory that should be ignored during sorting.

Potential issues with nested loops in the `compressItems` function include increased time complexity and potential performance bottlenecks, especially for large inventories.

## Related Questions
- How does the `compressItems` function handle items with different amounts?
- What is the purpose of the `lessThan` method in the `SortContext` struct?
- Why is there a suggestion to move the logic in `getTagsFromItem` into the `Item` struct?
- How does the sorting algorithm handle null or procedural items?
- Can you explain the role of the `ignoredSlotCount` parameter in the `sortItems` function?
- What potential issues might arise from the nested loops in the `compressItems` function?

*Source: unknown | chunk_id: github_pr_3194_comment_3401484200*
