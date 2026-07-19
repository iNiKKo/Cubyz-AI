# [src/client/entity_manager.zig] - PR #2682 review diff

**Type:** review
**Keywords:** SparseSet, VirtualList, entity management, interpolation system, pointer stability, benchmarking
**Symbols:** entities, main.utils.VirtualList, main.client.Entity, main.utils.SparseSet, main.entity.Entity
**Concepts:** memory reordering, stable pointers, architectural design

## Summary
The change replaces `VirtualList` with `SparseSet` for managing entities, but is reverted due to architectural concerns about memory reordering and pointer stability.

## Explanation
The change replaces `VirtualList` with `SparseSet` for managing entities, but is reverted due to architectural concerns about memory reordering and pointer stability. The reviewer suggests reverting the change from `VirtualList` to `SparseSet` because `SparseSet` reorders values in memory, which conflicts with the current interpolation system's requirement for stable pointers. The reviewer recommends keeping the original `VirtualList` until a benchmark can be conducted with enough entities to make an informed decision.

## Related Questions
- What are the implications of using SparseSet for entity management?
- Why is stable pointer support important in the interpolation system?
- How does VirtualList ensure pointer stability?
- What are the potential performance benefits of using SparseSet over VirtualList?
- When should a benchmark be conducted to evaluate entity management strategies?
- How does the current design decision impact future scalability of the entity manager?

*Source: unknown | chunk_id: github_pr_2682_comment_3148791148*
