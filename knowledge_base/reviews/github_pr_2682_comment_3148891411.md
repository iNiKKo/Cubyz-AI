# [src/client/entity_manager.zig] - PR #2682 review diff

**Type:** review
**Keywords:** entity_manager.zig, VirtualList, SparseSet, interpolation, pointer storage, performance, memory usage
**Symbols:** uniforms, pipeline, entities, main.utils.VirtualList, main.client.Entity, main.utils.SparseSet
**Concepts:** memory management, data structures, performance optimization, interpolation

## Summary
Replaced `VirtualList` with `SparseSet` in entity management to support pointer-based interpolation storage.

## Explanation
The change from `VirtualList` to `SparseSet` in the entity manager is aimed at optimizing memory usage and access patterns for entities. The reviewer notes that using a `SparseSet` allows for more efficient storage and retrieval of entities, particularly when dealing with pointer-based interpolation. This architectural decision is intended to improve performance by reducing overhead associated with managing large numbers of entities. The reviewer also mentions that this change enables the interpolation mechanism to store results directly by pointer, which can be more efficient than other methods.

## Related Questions
- What are the performance implications of using SparseSet instead of VirtualList?
- How does the change impact memory allocation patterns for entities?
- Can you explain the benefits of pointer-based interpolation storage in this context?
- Are there any potential regressions introduced by this architectural change?
- How does this change affect the scalability of entity management in Cubyz?
- What are the trade-offs between VirtualList and SparseSet in terms of functionality and performance?

*Source: unknown | chunk_id: github_pr_2682_comment_3148891411*
