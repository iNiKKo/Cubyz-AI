# [src/blocks.zig] - PR #2990 review diff

**Type:** review
**Keywords:** Replaceability, enum, block placement, future proofing, flexibility, refactoring, rotation.RotationMode.CanBeChangedInto
**Symbols:** Replaceability, enum
**Concepts:** future-proofing, flexibility, refactoring

## Summary
Added a new `Replaceability` enum to define how blocks behave when placed in the same position.

## Explanation
The change introduces a new `Replaceability` enum within the `blocks.zig` file to specify different behaviors for block placement. The reviewer points out that this approach may not be future-proof, as it limits flexibility (e.g., adding support for different drop items would require a major refactor). The reviewer also notes a similar pattern exists in `rotation.RotationMode.CanBeChangedInto`, suggesting consistency or potential refactoring opportunities.

## Related Questions
- What are the potential future use cases for the `Replaceability` enum?
- How does adding a union instead of an enum affect memory usage and performance?
- Is there a way to make the `Replaceability` enum more extensible without a major refactor?
- Can you provide examples of how the `rotation.RotationMode.CanBeChangedInto` pattern is used in other parts of the codebase?
- What are the implications of changing the `Replaceability` enum to a union for existing block behaviors?
- How can we ensure backward compatibility when refactoring the `Replaceability` enum?

*Source: unknown | chunk_id: github_pr_2990_comment_3168984030*
