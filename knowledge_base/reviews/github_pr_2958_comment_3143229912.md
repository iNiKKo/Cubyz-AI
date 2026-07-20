# [src/blocks.zig] - PR #2958 review diff

**Type:** review
**Keywords:** block registration, selection rule, enum, boolean flag, architectural change
**Symbols:** register, zon, SelectionRule
**Concepts:** architectural reasoning, flexibility, enum usage

## Summary
The code change updates the block registration function by replacing a boolean flag with an enum for selection rules.

## Explanation
The reviewer points out that the original code used a boolean to determine if a block is selectable. The change replaces this with an enum called `SelectionRule`, which allows for more granular control over block selection criteria. This architectural modification enhances flexibility and potentially prepares the system for future expansion of selection rules without modifying existing logic.

The default value for the `selectionRule` is set to `.always`, meaning that blocks are always selectable unless explicitly defined otherwise. This change affects backward compatibility because any code or systems relying on the previous boolean flag will need to be updated to handle the new enum type.

Using an enum over a boolean provides more flexibility and clarity, as it allows for different selection rules (e.g., `.never`, `.conditional`) in the future without altering existing logic. This architectural change could facilitate potential enhancements such as context-sensitive block selection or temporary unselectability of blocks.

The possible values for the `SelectionRule` enum are `.always`, `.never`, and `.conditional`. The default value is `.always`, meaning that blocks are always selectable unless explicitly defined otherwise. This change affects backward compatibility because any code or systems relying on the previous boolean flag will need to be updated to handle the new enum type.

To test the correctness of this change in the block registration system, one would need to ensure that all blocks continue to be selectable as expected when no specific selection rule is defined. Additionally, testing should verify that any new selection rules (e.g., `.never`, `.conditional`) are applied correctly and do not interfere with existing functionality.

## Related Questions
- What are the possible values for the `SelectionRule` enum?
- What is the default value for the `selectionRule` enum?

*Source: unknown | chunk_id: github_pr_2958_comment_3143229912*
