# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** blocks.zig, register function, zon element, selection capabilities, callsite constant, struct-local constants, load and check functions
**Symbols:** register, zon, SelectionRule, selectionCapabilities
**Concepts:** architectural design, data management, constant handling

## Summary
The change introduces a new variable `selectionCapabilities` to store selection capabilities for blocks, but the reviewer notes that the current implementation lacks a corresponding constant at the callsite.

## Explanation
The patch adds a new variable `selectionCapabilities` to handle block selection capabilities. However, the reviewer points out that this change alone is insufficient because it does not address the issue at the callsite where there is no associated constant. The reviewer suggests using a struct with local constants and load/check functions to properly manage these capabilities.

## Related Questions
- What is the purpose of the `selectionCapabilities` variable?
- Why does the reviewer mention a lack of constant at the callsite?
- How can the struct with local constants and load/check functions be implemented?
- What are the implications of not having a constant at the callsite?
- Can you provide an example of how to use the suggested struct for managing selection capabilities?
- How does this change affect the overall architecture of block registration?

*Source: unknown | chunk_id: github_pr_2987_comment_3201818520*
