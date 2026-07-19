# [src/block_entity.zig] - PR #1470 review diff

**Type:** review
**Keywords:** BlockEntityIndex, enum(u32), ID, indexing, sparse arrays, type safety
**Symbols:** BlockEntityIndex, u32
**Concepts:** type safety, sparse array indexing

## Summary
The `BlockEntityIndex` type has been changed from a simple `u32` to an enum(u32).

## Explanation
The reviewer points out that the previous name suggestion for `BlockEntityIndex` was inappropriate because it is used as an ID to index sparse arrays in various contexts. The change to an enum(u32) likely aims to provide more clarity and type safety, ensuring that the index is used correctly in different parts of the codebase. The previous type of `BlockEntityIndex` before this change was a simple `u32`. The reviewer suggests that the name was inappropriate because it does not reflect its use as an ID for indexing sparse arrays. Changing `BlockEntityIndex` to an enum(u32) improves type safety by providing more explicit and controlled usage of the index in different parts of the codebase.

## Related Questions
- What was the previous type of BlockEntityIndex before this change?
- Why was the name suggested for BlockEntityIndex inappropriate?
- How does changing BlockEntityIndex to an enum(u32) improve type safety?
- Are there any other parts of the codebase that use BlockEntityIndex and need to be updated?
- What potential regressions should be tested after this change?
- Does this change affect backwards compatibility with existing data?

*Source: unknown | chunk_id: github_pr_1470_comment_2096481606*
