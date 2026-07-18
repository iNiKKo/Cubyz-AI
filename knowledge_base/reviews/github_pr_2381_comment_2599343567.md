# [src/items.zig] - PR #2381 review diff

**Type:** review
**Keywords:** inline, performance, blocks, architecture, method addition
**Symbols:** BaseItemIndex, getTooltip, onUse, main.callbacks.UseItemCallback
**Concepts:** inlining, architectural design

## Summary
Added an `onUse` method to `BaseItemIndex` with an `inline` attribute.

## Explanation
The reviewer points out that the added `onUse` method does not involve any performance-critical operations, making the `inline` attribute unnecessary. The reviewer also questions whether blocks should have this inline attribute, suggesting a potential architectural review is needed to ensure appropriate use of inlining.

## Related Questions
- Why was the `onUse` method added to `BaseItemIndex`?
- What is the purpose of the `inline` attribute in this context?
- Are there any performance implications of using `inline` here?
- Should blocks have the `inline` attribute according to the reviewer's opinion?
- How does the addition of `onUse` affect the overall architecture of the items module?
- What is the expected behavior of the `onUse` method in different scenarios?

*Source: unknown | chunk_id: github_pr_2381_comment_2599343567*
