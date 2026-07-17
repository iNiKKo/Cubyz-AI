# [src/items.zig] - PR #2381 review diff

**Type:** review
**Keywords:** complexity, blocks, zon elements, callbacks, temporary storage, architectural review
**Symbols:** BaseItem, tooltip, self.onUse
**Concepts:** architectural design, data structures, callback implementation

## Summary
The review discusses the complexity of implementing item usage callbacks compared to blocks due to differences in data structures.

## Explanation
The reviewer points out that items are more complex to handle than blocks because items do not have an array of zon elements, unlike blocks. The reviewer suggests storing the zon in the BaseItem temporarily until all components are finished and then parsing the callbacks as a potential solution, indicating concern over the architectural complexity and lack of elegant alternatives.

## Related Questions
- What is the difference between items and blocks in terms of data structures?
- Why is implementing item usage callbacks more complex than for blocks?
- How does the reviewer suggest handling the zon elements temporarily?
- What are the potential drawbacks of storing zon elements in BaseItem until everything is finished?
- Are there any other architectural considerations mentioned in the review?
- How might the implementation of callbacks be improved based on this review?

*Source: unknown | chunk_id: github_pr_2381_comment_2632750016*
