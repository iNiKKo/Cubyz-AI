# [issues/issue_1628.md] - Issue #1628 discussion

**Type:** review
**Keywords:** stackable, max stack size, display count, feature request, game mechanics
**Concepts:** stackable items, item display

## Summary
Discussion on whether items with a max stack size of 1 should display a count.

## Explanation
The issue discusses the display behavior of item counts for stackable items in the game. The maintainer points out that every item is technically stackable, but some have a stack size of 1. There is agreement that if an item's max stack size is greater than 1, its current count should always be displayed; however, if the max stack size is 1, the item will display '1' even when it is alone.

## Related Questions
- What is the current behavior of item count display for items with a max stack size of 1?
- How does the game determine if an item should display its count?
- Are there any performance implications of always displaying item counts?
- Is there a plan to implement this feature request in future updates?
- What is the impact on user experience if lone stackable items do not show a count?
- How will this change affect backwards compatibility with existing save files?

*Source: unknown | chunk_id: github_issue_1628_discussion*
