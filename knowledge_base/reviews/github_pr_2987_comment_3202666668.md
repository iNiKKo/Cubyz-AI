# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** refactoring, enum, struct, selection capabilities, deprecated syntax, flexibility
**Symbols:** SelectionRule, SelectionCapabilities, capabilities, alwaysSelectable
**Concepts:** modularity, extensibility, deprecation

## Summary
Refactored the `SelectionRule` enum to a more flexible `SelectionCapabilities` struct, allowing for dynamic selection capabilities.

## Explanation
The change replaces the simple `SelectionRule` enum with a more complex `SelectionCapabilities` struct. This new struct introduces a nullable slice of `SelectionCapability`, providing greater flexibility in defining selection rules. The reviewer notes that construction with T{} is likely to be deprecated, so the code was updated to use the recommended syntax. This refactoring enhances the modularity and extensibility of the block selection logic, making it easier to add new capabilities without modifying existing code.

## Related Questions
- What is the purpose of the `SelectionCapabilities` struct?
- How does the new `alwaysSelectable` constant differ from the old `SelectionRule` enum?
- Why was the construction syntax updated in this refactoring?
- Are there any potential performance implications of using a nullable slice for selection capabilities?
- What are the benefits of making the selection logic more modular and extensible?
- How might this change affect existing code that relies on the old `SelectionRule` enum?

*Source: unknown | chunk_id: github_pr_2987_comment_3202666668*
