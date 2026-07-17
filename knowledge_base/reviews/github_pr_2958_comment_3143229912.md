# [src/blocks.zig] - PR #2958 review diff

**Type:** review
**Keywords:** blocks.zig, register, zon, SelectionRule, selectable, emittedLight, absorbedLight, degradable, enum literals, type inference
**Symbols:** register, zon, SelectionRule
**Concepts:** Enum usage, Code simplification

## Summary
The code change updates the registration of block properties by replacing a boolean `selectable` field with an enum `SelectionRule`, defaulting to `.always`. The reviewer suggests simplifying the enum literal usage.

## Explanation
The modification involves changing how blocks are selectable. Previously, a simple boolean flag was used to determine if a block could be selected. This has been replaced with a more flexible `SelectionRule` enum, which allows for different selection behaviors beyond just being always selectable or not. The reviewer points out that when the result type of an enum literal is known, it can be simplified by omitting the explicit type specification.

## Related Questions
- What is the purpose of the `SelectionRule` enum in Cubyz?
- How does the change from boolean to enum affect block selection logic?
- Why was it decided to simplify the enum literal usage?
- Are there any potential performance implications with this change?
- Does this change impact backwards compatibility with existing blocks?
- What other properties could benefit from using enums instead of booleans?

*Source: unknown | chunk_id: github_pr_2958_comment_3143229912*
