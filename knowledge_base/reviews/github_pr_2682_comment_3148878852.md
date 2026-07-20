# [src/client/entity_manager.zig] - PR #2682 review diff

**Type:** review
**Keywords:** refactoring, SparseSet, VirtualList, entity management, architectural decisions, interpolation issues, performance considerations, code review, system design, batch processing, data structures
**Symbols:** uniforms, pipeline, entities, main.utils.VirtualList, main.client.Entity, main.utils.SparseSet, main.entity.Entity
**Concepts:** architectural review, batch processing, interpolation system, data structures

## Summary
The `entity_manager.zig` file has been refactored by replacing a `VirtualList` with a `SparseSet`. The reviewer suggests pausing further work on this PR until issues in the interpolation system are resolved.

## Explanation
The change involves switching from a `VirtualList` to a `SparseSet` for managing entities. This decision is part of an ongoing architectural review that highlights potential batch processing improvements. However, the reviewer expresses concern about the current state of the interpolation system and advises pausing this PR until those issues are addressed. The reviewer also questions the rationale behind the chosen approach.

Additionally, there is a comment suggesting that entities are sometimes small and sometimes big, which means using smooth lighting would require a lot of work. Therefore, a non-smooth shader is used for these entities.

## Related Questions
- What are the potential performance implications of switching from VirtualList to SparseSet?
- Why was the interpolation system deemed poorly designed, and what specific issues need fixing?
- How does this change affect memory usage in the entity manager?
- Can you provide more details on the architectural review that led to this refactoring decision?
- What are the benefits of using a SparseSet over a VirtualList for entity management?
- Are there any known regressions or issues introduced by this change that need to be addressed?
- How does this change impact the overall design and scalability of the entity manager?
- Can you explain the rationale behind pausing this PR until interpolation system issues are resolved?
- What specific improvements in batch processing are expected from this refactoring?
- Are there any alternative data structures that could have been considered for this change?

*Source: unknown | chunk_id: github_pr_2682_comment_3148878852*
