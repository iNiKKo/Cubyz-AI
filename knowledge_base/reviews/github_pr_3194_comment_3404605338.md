# [src/Inventory.zig] - PR #3194 review diff

**Type:** review
**Keywords:** sortItems, compressItems, SortContext, item sorting, tag-based categorization, read order issues, pre-sorting tags
**Symbols:** ClientInventory, sortItems, compressItems, SortContext, getItem, getTagsFromItem
**Concepts:** sorting algorithm, inventory management, tag-based categorization

## Summary
Added `sortItems` and `compressItems` functions to `ClientInventory`, along with a `SortContext` struct for item sorting based on tags.

## Explanation
The changes introduce functionality to sort items in the inventory by compressing similar items first and then sorting them based on their tags. The `compressItems` function ensures that similar items are combined by iterating through each item stack and checking for duplicates, then depositing the excess amount into a single stack. The `SortContext` struct is used in the sorting process to provide context about the inventory being sorted, including methods like `lessThan` which determine the order of items based on their tags. The reviewer notes that the current implementation could cause read order issues if tags are not sorted, suggesting a modification to ensure tags are pre-sorted when loaded from Zon files. This can be achieved by adding sorting logic in the `loadTagsFromZon` function in `src/tag.zig`. Developers can customize the item sorting algorithm by modifying the `lessThan` method or other parts of the sorting process. Potential issues if tags are not sorted include inconsistent ordering and potential bugs in the sorting logic.

## Related Questions
- How does the `compressItems` function ensure that similar items are combined?
- What is the purpose of the `SortContext` struct in the sorting process?
- Why is it important to pre-sort tags when loading them from Zon files?
- How can developers customize the item sorting algorithm?
- What potential issues could arise if tags are not sorted before use?
- How does the current implementation handle items with different tag orders?

*Source: unknown | chunk_id: github_pr_3194_comment_3404605338*
