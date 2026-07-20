# [src/client/entity_manager.zig] - PR #2682 review diff

**Type:** review
**Keywords:** refactoring, SparseSet, VirtualList, entity management, architectural decisions, interpolation issues, performance considerations, code review, system design, batch processing, data structures
**Symbols:** uniforms, pipeline, entities, main.utils.VirtualList, main.client.Entity, main.utils.SparseSet, main.entity.Entity
**Concepts:** architectural review, batch processing, interpolation system, data structures

## Summary
The `entity_manager.zig` file has been refactored by replacing a `VirtualList` with a `SparseSet`. The reviewer suggests pausing further work on this PR until issues in the interpolation system are resolved.

## Explanation
The `entity_manager.zig` file has been refactored by replacing a `VirtualList` with a `SparseSet`. This change is part of an ongoing architectural review aimed at improving batch processing and addressing issues in the interpolation system. The reviewer suggests pausing further work on this PR until these issues are resolved.

The decision to use a `SparseSet` over a `VirtualList` was made to potentially improve performance and memory usage, as well as to address design flaws in the current system. Specifically, the reviewer notes that entities are sometimes small and sometimes big, making smooth lighting computationally expensive. Therefore, a non-smooth shader is used for these entities.

The use of a `SparseSet` is expected to provide better performance and more efficient memory usage compared to a `VirtualList`, especially in scenarios involving large numbers of entities. Additionally, there is currently no smooth lighting due to poor design decisions in the interpolation system, which necessitates the use of a non-smooth shader.

## Related Questions
- What are the specific reasons for switching from VirtualList to SparseSet?
- What architectural improvements are expected from this refactoring decision?
- How does the use of a SparseSet impact performance and memory usage compared to a VirtualList?

*Source: unknown | chunk_id: github_pr_2682_comment_3148878852*
