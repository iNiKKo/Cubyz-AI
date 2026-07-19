# [src/blocks.zig] - PR #2990 review diff

**Type:** review
**Keywords:** Replaceability, enum, union, block placement, drop behavior, rotation.RotationMode.CanBeChangedInto
**Symbols:** Replaceability, enum, union
**Concepts:** future-proofing, refactoring, architectural consistency

## Summary
The `Replaceability` enum in `blocks.zig` has been expanded with new values to handle different behaviors when placing blocks in the same position.

## Explanation
The reviewer points out that the current implementation of the `Replaceability` enum is not future-proof, as it does not allow for flexibility in handling different drop items when a block is broken. The reviewer suggests using a union instead of an enum to accommodate this requirement, which would necessitate a major refactor. Additionally, the reviewer notes that a similar pattern has already been established in `rotation.RotationMode.CanBeChangedInto`, indicating consistency with existing architectural practices.

The specific values added to the `Replaceability` enum are:
- `none`: No replacement behavior.
- `destroy`: The block is destroyed when trying to place another block in the same position.
- `drop`: The block drops its items when trying to place another block in the same position.

## Related Questions
- What are the potential impacts of changing `Replaceability` from an enum to a union?
- How does the existing pattern in `rotation.RotationMode.CanBeChangedInto` relate to the proposed changes in `blocks.zig`?
- What other future-proofing considerations should be taken into account for block behaviors?
- How can we ensure that the refactoring of `Replaceability` does not introduce regressions?
- What are the performance implications of using a union instead of an enum in this context?
- How can we maintain architectural consistency while implementing these changes?

*Source: unknown | chunk_id: github_pr_2990_comment_3168984030*
