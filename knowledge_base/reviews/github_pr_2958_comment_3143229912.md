# [src/blocks.zig] - PR #2958 review diff

**Type:** review
**Keywords:** block registration, selection rule, enum, boolean flag, architectural change
**Symbols:** register, zon, SelectionRule
**Concepts:** architectural reasoning, flexibility, enum usage

## Summary
The code change updates the block registration function by replacing a boolean flag with an enum for selection rules.

## Explanation
The reviewer points out that the original code used a boolean to determine if a block is selectable. The change replaces this with an enum called `SelectionRule`, which allows for more granular control over block selection criteria. This architectural modification enhances flexibility and potentially prepares the system for future expansion of selection rules without modifying existing logic.

## Related Questions
- What is the purpose of the `SelectionRule` enum in the block registration process?
- How does this change affect backward compatibility with existing blocks?
- Can you explain the benefits of using an enum over a boolean for selection rules?
- What potential future enhancements could be facilitated by this architectural change?
- Is there any performance impact associated with replacing a boolean with an enum?
- How would you test the correctness of this change in the block registration system?

*Source: unknown | chunk_id: github_pr_2958_comment_3143229912*
