# [issues/issue_2950.md] - Issue #2950 discussion

**Type:** review
**Keywords:** import styles, standardization, relative imports, root-relative imports, Cubyz, Zig, modularity
**Symbols:** itemdrop.zig, blueprint.zig, @import, main.x, Vec3i
**Concepts:** module system, import consistency, code style

## Summary
The issue discusses inconsistent import styles in Cubyz's Zig codebase and proposes standardizing them. The main points of discussion include the choice between relative imports (`@import`) and root-relative imports (`main.x`), with a preference for the latter due to its stability and ease of use.

## Explanation
The issue highlights inconsistencies in import styles across different files, such as `itemdrop.zig` and `blueprint.zig`. The primary concern is the choice between using relative imports (`@import`) and root-relative imports (`main.x`). While there are arguments for both approaches—relative imports being more flexible and root-relative imports providing a stable reference point—the discussion leans towards adopting root-relative imports due to their stability and ease of use. However, practical considerations such as recursive imports and the need to import non-tree items complicate enforcement. The maintainer suggests focusing on eliminating cases where the same struct is used both through its module (`mod.Struct`) and through an alias (`Struct`), which is seen as a more actionable step.

## Related Questions
- What are the potential issues with using recursive imports in Cubyz?
- How does the choice of import style affect code maintainability in Cubyz?
- Can you explain the difference between relative and root-relative imports in Zig?
- Why is there a preference for root-relative imports in Cubyz's development?
- What are the current limitations of ZLS that impact module resolution in Cubyz?
- How can we enforce consistent import styles across the Cubyz codebase?

*Source: unknown | chunk_id: github_issue_2950_discussion*
