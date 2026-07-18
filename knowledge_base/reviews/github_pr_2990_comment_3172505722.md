# [src/blocks.zig] - PR #2990 review diff

**Type:** review
**Keywords:** blocks.zig, Replaceability, enum, behavior, interaction, semantics, readability, maintainability
**Symbols:** Replaceability, enum
**Concepts:** enumeration, code structure

## Summary
Added a new enum `Replaceability` to define how blocks behave when trying to place another block in the same position.

## Explanation
The change introduces a new enumeration called `Replaceability` within the `blocks.zig` file. This enum specifies three possible behaviors: `none`, `destroy`, and `drop`. The reviewer suggests that while there could be more complex structures, using enums keeps the property flat and straightforward. This addition is likely aimed at providing clearer semantics for block interactions in the game, potentially improving code readability and maintainability.

## Related Questions
- What are the possible values for the `Replaceability` enum?
- How does the addition of `Replaceability` affect block placement logic in Cubyz?
- Is there any existing code that needs to be updated to accommodate the new `Replaceability` enum?
- Can you explain the difference between `destroy` and `drop` behaviors in the context of `Replaceability`?
- What architectural considerations were taken into account when designing the `Replaceability` enum?
- How might this change impact performance or memory usage in Cubyz?
- Are there any potential backward compatibility issues with this new enum addition?
- Can you provide examples of how different blocks might use the `Replaceability` enum?
- What is the motivation behind making `Replaceability` a flat enum rather than a more complex structure?
- How does this change align with the overall design goals of Cubyz?

*Source: unknown | chunk_id: github_pr_2990_comment_3172505722*
