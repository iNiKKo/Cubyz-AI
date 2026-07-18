# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** refactoring, flexibility, Zig language, deprecation, initialization syntax, selection rules
**Symbols:** SelectionRule, SelectionCapabilities, alwaysSelectable
**Concepts:** type safety, expressiveness, language evolution

## Summary
Refactored the `SelectionRule` enum into a `SelectionCapabilities` struct to enhance flexibility and align with Zig's evolving language features.

## Explanation
The change involves replacing the simple `SelectionRule` enum with a more complex `SelectionCapabilities` struct. This refactoring is motivated by the need for greater flexibility in defining selection rules, which can now include various capabilities instead of just three fixed states (always, toolEffective, never). The reviewer suggests using the new syntax `.{} = .{}` to initialize the struct, which is recommended as the older `T{}` syntax may be deprecated. This change also aligns with Zig's ongoing efforts to improve type safety and expressiveness, ensuring that the codebase remains robust and adaptable to future language changes.

## Related Questions
- What are the potential benefits of using a struct instead of an enum for selection capabilities?
- How does this refactoring impact backward compatibility with existing code?
- What is the significance of avoiding the `T{}` syntax in Zig?
- Can you explain the motivation behind aligning with Zig's evolving language features?
- How might this change affect performance or memory usage?
- What are the implications for future maintenance and extension of selection rules?

*Source: unknown | chunk_id: github_pr_2987_comment_3202666668*
