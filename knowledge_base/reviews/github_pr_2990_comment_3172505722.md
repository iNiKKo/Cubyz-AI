# [src/blocks.zig] - PR #2990 review diff

**Type:** review
**Keywords:** Replaceability, enum, block placement, behavior, destroy, drop
**Symbols:** Ore, SelectionRule, Replaceability
**Concepts:** enum usage, block behavior

## Summary
Added a new enum `Replaceability` to define how blocks behave when trying to place another block in the same position.

## Explanation
The reviewer acknowledges the addition of a new enum `Replaceability` which specifies three behaviors: none, destroy, and drop. The reviewer suggests that while enums are flat, they can still effectively represent complex properties without needing a more intricate structure. This change is likely aimed at improving the clarity and control over block placement behavior in the game.

## Related Questions
- What are the possible values for the Replaceability enum?
- How does the Replaceability enum affect block placement in Cubyz?
- Can you explain the difference between 'none', 'destroy', and 'drop' in the Replaceability enum?
- Is there any existing code that uses the Replaceability enum?
- What architectural considerations were taken into account when adding this enum?
- How might this change impact backwards compatibility with older versions of Cubyz?

*Source: unknown | chunk_id: github_pr_2990_comment_3172505722*
