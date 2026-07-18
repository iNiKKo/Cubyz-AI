# [src/block_entity.zig] - PR #2216 review diff

**Type:** review
**Keywords:** global variable, renaming, architectural review, refactoring, code organization, BlockEntityTypes
**Symbols:** blockyEntityTypes, BlockEntityType, BlockEntityTypes
**Concepts:** global state, architectural refactoring, code organization

## Summary
The review discusses the removal of a global variable `blockyEntityTypes` and mentions a renaming of the `BlockEntityTypes` struct.

## Explanation
The reviewer points out that a global variable named `blockyEntityTypes` has been removed. They also note that there is another `BlockEntityTypes` struct, which has been renamed in the current branch. The review suggests that this change might be part of an architectural refactoring to improve code organization or reduce global state.

## Related Questions
- What was the purpose of removing `blockyEntityTypes`?
- Why was the `BlockEntityTypes` struct renamed?
- How does this change impact the overall architecture of Cubyz?
- Are there any potential side effects from reducing global state?
- Can you provide more details on the refactoring process?
- What benefits are expected from this architectural change?

*Source: unknown | chunk_id: github_pr_2216_comment_2495484075*
