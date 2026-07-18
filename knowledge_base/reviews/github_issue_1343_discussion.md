# [issues/issue_1343.md] - Issue #1343 discussion

**Type:** review
**Keywords:** refactor, ListUnmanaged, chunk_meshing.zig, iterator safety, mesh regeneration, light update
**Symbols:** lightRefreshList, regenerateMeshList, ListUnmanaged
**Concepts:** iterator invalidation, list management

## Summary
The issue discusses refactoring `lightRefreshList` to use `ListUnmanaged` in `chunk_meshing.zig`, noting that it is inconsistent with `regenerateMeshList`. The maintainer clarifies that the two lists serve different purposes.

## Explanation
The discussion revolves around the inconsistency between `lightRefreshList` and `regenerateMeshList` when using `ListUnmanaged`. The reviewer points out that while they are conceptually similar, one is used for regenerating the entire mesh while the other is specifically for updating light data. This distinction prevents them from being merged into a single list, as modifying one during iteration over the other could lead to iterator invalidation.

## Related Questions
- What is the purpose of `regenerateMeshList` in `chunk_meshing.zig`?
- How does `lightRefreshList` differ from `regenerateMeshList`?
- Why can't `regenerateMeshList` and `lightRefreshList` be merged into a single list?
- What are the risks associated with modifying one list while iterating over another?
- How does using `ListUnmanaged` impact iterator safety in this context?
- Can you explain the distinction between mesh regeneration and light updates in Cubyz?

*Source: unknown | chunk_id: github_issue_1343_discussion*
