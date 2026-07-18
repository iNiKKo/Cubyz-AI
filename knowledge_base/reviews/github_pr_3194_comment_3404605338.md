# [src/Inventory.zig] - PR #3194 review diff

**Type:** review
**Keywords:** sortItems, compressItems, SortContext, item sorting, tag-based categorization, read order issues, pre-sorting tags
**Symbols:** ClientInventory, sortItems, compressItems, SortContext, getItem, getTagsFromItem
**Concepts:** sorting algorithm, inventory management, tag-based categorization

## Summary
Added `sortItems` and `compressItems` functions to `ClientInventory`, along with a `SortContext` struct for item sorting based on tags.

## Explanation
The changes introduce functionality to sort items in the inventory by compressing similar items first and then sorting them based on their tags. The reviewer notes that the current implementation could cause read order issues if tags are not sorted, suggesting a modification to ensure tags are pre-sorted when loaded from Zon files.

## Related Questions
- How does the `compressItems` function ensure that similar items are combined?
- What is the purpose of the `SortContext` struct in the sorting process?
- Why is it important to pre-sort tags when loading them from Zon files?
- How can developers customize the item sorting algorithm?
- What potential issues could arise if tags are not sorted before use?
- How does the current implementation handle items with different tag orders?

*Source: unknown | chunk_id: github_pr_3194_comment_3404605338*
