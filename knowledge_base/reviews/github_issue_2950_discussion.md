# [issues/issue_2950.md] - Issue #2950 discussion

**Type:** review
**Keywords:** import styles, standardization, relative imports, root-relative imports, Cubyz, Zig, modularity
**Symbols:** itemdrop.zig, blueprint.zig, @import, main.x, Vec3i
**Concepts:** module system, import consistency, code style

## Summary
The issue discusses inconsistent import styles in Cubyz's Zig codebase and proposes standardizing them. The main points of discussion include the choice between relative imports (`@import`) and root-relative imports (`main.x`), with a preference for the latter due to its stability and ease of use.

## Explanation
The issue discusses inconsistent import styles in Cubyz's Zig codebase and proposes standardizing them. The main points of discussion include the choice between relative imports (`@import`) and root-relative imports (`main.x`), with a preference for the latter due to its stability and ease of use.

Specific examples from `itemdrop.zig` and `blueprint.zig` illustrate the inconsistency:
- In `itemdrop.zig`, imports are done using `const vec = @import("vec.zig");`
- In `blueprint.zig`, imports are done using `const vec = main.vec;`

The primary concern is the choice between relative imports (`@import`) and root-relative imports (`main.x`). While there are arguments for both approaches—relative imports being more flexible and root-relative imports providing a stable reference point—the discussion leans towards adopting root-relative imports due to their stability and ease of use. However, practical considerations such as recursive imports and the need to import non-tree items complicate enforcement.

The maintainer suggests focusing on eliminating cases where the same struct is used both through its module (`mod.Struct`) and through an alias (`Struct`), which is seen as a more actionable step. Additionally, enforcing root-relative imports via CI would require ensuring that all `@import` statements are public to avoid issues with recursive imports.

The preferred style for aliasing structs is to use the second option (root-relative imports) due to its stability and ease of use.

## Related Questions
- What specific import styles are used in Cubyz's Zig codebase?
- How do relative imports (`@import`) differ from root-relative imports (`main.x`)?
- Why is there a preference for root-relative imports over relative imports in Cubyz?
- Can you provide examples of recursive imports and non-tree item imports that complicate the enforcement of import styles?
- What are the current limitations of ZLS that impact module resolution in Cubyz?

*Source: unknown | chunk_id: github_issue_2950_discussion*
