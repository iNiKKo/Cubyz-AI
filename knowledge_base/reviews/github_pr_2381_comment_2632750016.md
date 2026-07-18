# [src/items.zig] - PR #2381 review diff

**Type:** review
**Keywords:** onUse, zon elements, blocks vs items, temporary storage, callback parsing
**Symbols:** BaseItem, tooltip, self.tooltip, self.onUse
**Concepts:** architectural complexity, callback handling

## Summary
The review discusses the complexity introduced by adding 'onUse' functionality to items compared to blocks, highlighting architectural challenges.

## Explanation
The reviewer points out that implementing 'onUse' for items is more complex than for blocks due to differences in their structures. Blocks have an array of zon elements, whereas items do not. The reviewer suggests storing the zon in the BaseItem temporarily until all components are finalized and then parsing the callbacks. This approach is described as 'ugly,' indicating potential architectural issues or inefficiencies.

## Related Questions
- What is the purpose of the 'onUse' functionality being added to items?
- How does the structure of blocks differ from that of items, and why does this affect callback implementation?
- Why is storing zon elements temporarily in BaseItem considered an 'ugly' solution?
- What are the potential architectural implications of implementing 'onUse' for items?
- How might the temporary storage of zon elements impact performance or memory usage?
- Are there any alternative approaches to handling callbacks for items that could be more efficient?

*Source: unknown | chunk_id: github_pr_2381_comment_2632750016*
