# [src/blocks.zig] - PR #3060 review diff

**Type:** review
**Keywords:** refactoring, union(enum), custom struct, capabilities, coercion, simplification, functionality, enum literals, void union fields, selection capabilities
**Symbols:** SelectionCapabilities, Capability, toolEffective, allowsSelectionByItem, neverSelectable, alwaysSelectable
**Concepts:** union(enum), coercion, flexibility, efficiency

## Summary
Refactored `SelectionCapabilities` to use a union(enum) with a custom struct for capabilities, replacing the previous enum-based approach.

## Explanation
The change refactors the `SelectionCapabilities` structure from using an enum of capabilities to a union(enum) that includes a custom struct. This new approach aims to provide more flexibility and efficiency in handling different selection capabilities. The custom struct within the union(enum) contains a single field, `toolEffective`, which is a boolean indicating whether the tool is effective on a block. The `allowsSelectionByItem` function checks if an item can select a block based on its capabilities. The reviewer notes that the previous method was redundant because coercion from enum literals to void union fields is possible, suggesting that the new design simplifies the codebase while maintaining functionality. The `neverSelectable` and `alwaysSelectable` constants are provided for convenience, representing selection capabilities where no items can select a block and all items can select a block, respectively.

## Related Questions
- What is the purpose of using a union(enum) in `SelectionCapabilities`?
- How does the new design simplify the codebase compared to the previous enum-based approach?
- Can you explain the role of the custom struct within the union(enum)?
- Why was the previous method considered redundant?
- How does coercion from enum literals to void union fields work in this context?
- What are the benefits of using a union(enum) with a custom struct for selection capabilities?

*Source: unknown | chunk_id: github_pr_3060_comment_3292553298*
