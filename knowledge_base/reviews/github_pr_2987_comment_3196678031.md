# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** nullable, non-nullable, default value, allocation, memory efficiency
**Symbols:** register, zon, _light, _absorption, _degradable, _selectionRule, SelectionRule, SelectionCapability
**Concepts:** memory management, performance optimization

## Summary
The code introduces a new variable `selectionCapabilities` and suggests using a non-nullable default value instead of a nullable one.

## Explanation
The reviewer recommends changing the `selectionRule` from being nullable to using a default `.all` capability. This avoids unnecessary allocation by directly assigning a reference to an array containing `.all`. The architectural reasoning behind this change is to simplify memory management and improve performance by eliminating potential null checks and allocations.

## Related Questions
- Why is the reviewer suggesting a non-nullable default value?
- What are the potential benefits of using `.all` as the default selection capability?
- How does this change impact memory allocation in the code?
- Can you explain the architectural implications of avoiding null checks?
- What is the purpose of the `SelectionCapability` array in this context?
- How might this change affect existing code that relies on nullable selection rules?

*Source: unknown | chunk_id: github_pr_2987_comment_3196678031*
