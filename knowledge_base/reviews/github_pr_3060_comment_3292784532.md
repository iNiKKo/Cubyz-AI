# [src/blocks.zig] - PR #3060 review diff

**Type:** review
**Keywords:** SelectionCapabilities, refactor, union(enum), allowsSelectionByItem, custom, always, toolEffective, architectural review, feature separation, conditional checks
**Symbols:** SelectionCapabilities, BackingType, always, custom, toolEffective
**Concepts:** refactoring, union(enum), architectural design, function placement

## Summary
Refactored SelectionCapabilities from a struct with optional capabilities array to a union(enum) with two variants: always and custom. The reviewer suggests moving the allowsSelectionByItem function to the custom variant for clearer distinction between features.

## Explanation
The change refactors the SelectionCapabilities structure by converting it into a union(enum) with two variants: 'always' and 'custom'. This modification aims to provide a more explicit separation of capabilities that are always applicable versus those that can be customized. The reviewer recommends placing the allowsSelectionByItem function within the custom variant, which would involve adding conditional checks for each capability. This approach is intended to enhance clarity and maintainability by distinguishing between hardcoded features and configurable ones.

## Related Questions
- What is the purpose of refactoring SelectionCapabilities to a union(enum)?
- Why does the reviewer suggest moving allowsSelectionByItem to the custom variant?
- How does this change affect the distinction between hardcoded and configurable features?
- What are the potential benefits of using a union(enum) in this context?
- How might this refactoring impact performance or memory usage?
- Are there any backward compatibility concerns with this change?

*Source: unknown | chunk_id: github_pr_3060_comment_3292784532*
