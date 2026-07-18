# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** refactoring, selection capabilities, zon loading, item selection, block tags
**Symbols:** SelectionCapabilities, alwaysSelectable, loadFromZon, allowsSelectionByItem, SelectionCapability
**Concepts:** encapsulation, modularity, selection logic

## Summary
Refactored `SelectionRule` into a more flexible `SelectionCapabilities` struct with additional methods for loading from Zon and checking selection capabilities by item.

## Explanation
The change introduces a new struct `SelectionCapabilities` that encapsulates the logic for determining if a block can be selected based on various capabilities. This refactoring allows for more complex selection rules, such as those dependent on specific items or tags. The reviewer suggests nesting `SelectionCapability` within `SelectionCapabilities` to reduce redundancy and improve encapsulation. The new methods `loadFromZon` and `allowsSelectionByItem` provide a structured way to handle selection logic, enhancing the modularity and maintainability of the code.

## Related Questions
- What is the purpose of the `alwaysSelectable` constant in `SelectionCapabilities`?
- How does the `loadFromZon` method handle invalid `SelectionCapability` entries?
- Can you explain the logic behind the `allowsSelectionByItem` method?
- Why was `SelectionRule` replaced with `SelectionCapabilities`?
- What is the role of the `capabilities` field in `SelectionCapabilities`?
- How does the refactoring impact backward compatibility with existing code?

*Source: unknown | chunk_id: github_pr_2987_comment_3202703881*
