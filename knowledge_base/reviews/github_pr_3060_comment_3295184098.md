# [src/blocks.zig] - PR #3060 review diff

**Type:** review
**Keywords:** refactor, union(enum), packed struct, capabilities, checks, robustness, architectural review
**Symbols:** SelectionCapabilities, BackingType, always, custom, toolEffective, allowsSelectionByItem, Block, Item
**Concepts:** union(enum), packed struct, capability checks

## Summary
Refactored the SelectionCapabilities struct to use a union(enum) with a packed struct for better control over capabilities, ensuring checks are not skipped.

## Explanation
The change refactors the SelectionCapabilities struct from using an optional slice of capabilities to a union(enum) with a packed struct. This approach provides more granular control over individual capabilities and ensures that all checks are explicitly handled. The reviewer suggests modifying the condition inside allowsSelectionByItem to ensure it does not skip subsequent checks, improving the robustness of capability checks.

## Related Questions
- What is the purpose of using a union(enum) with a packed struct in SelectionCapabilities?
- How does the refactored allowsSelectionByItem function ensure that no checks are skipped?
- What potential issues could arise from not explicitly handling all capability checks?
- How does this change improve the control over individual capabilities?
- Can you explain the role of BackingType in the new SelectionCapabilities struct?
- Why was it necessary to modify the condition inside allowsSelectionByItem?

*Source: unknown | chunk_id: github_pr_3060_comment_3295184098*
