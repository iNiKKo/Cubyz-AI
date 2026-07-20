# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** selectionCapabilities, callsite, constant, struct-local, load function, check function
**Symbols:** register, zon, SelectionRule, SelectionCapability
**Concepts:** architectural review, struct design

## Summary
The change introduces a new variable `selectionCapabilities` to store selection capabilities, but the reviewer notes that the callsite does not have an extra constant and suggests using a struct with local constants for better architecture.

## Explanation
The change introduces a new variable `selectionCapabilities` to store selection capabilities. The reviewer notes that the current approach lacks an extra constant at the callsite, which could lead to architectural issues. The reviewer recommends using a struct with a struct-local constant and associated load and check functions to improve the design and prevent potential bugs.

## Related Questions
- What is the purpose of introducing `selectionCapabilities`?
- Why does the reviewer mention a lack of an extra constant at the callsite?
- How can using a struct with local constants improve the architecture?
- What are the potential benefits of adding load and check functions to the struct?
- Could this change lead to any performance improvements or regressions?
- How might this modification affect backwards compatibility?

*Source: unknown | chunk_id: github_pr_2987_comment_3201818520*
