# [issues/issue_1205.md] - Issue #1205 discussion

**Type:** review
**Keywords:** refactor, struct, clone, Zig, StringHashMap, allocator, maintenance, organization, code duplication, improvement
**Symbols:** commonBlocks, commonBlockMigrations, commonItems, commonTools, commonBiomes, commonBiomeMigrations, commonRecipes, commonModels, readAssets
**Concepts:** refactoring, memory management, asset loading

## Summary
The `common*` variables from `assets.zig` are being refactored into a struct, and the `clone` function should be included.

## Explanation
The current implementation of asset handling in Cubyz uses multiple global variables to store different types of assets. This approach can lead to code duplication and maintenance challenges. By refactoring these variables into a struct, the codebase will become more organized and easier to manage. The inclusion of the `clone` function ensures that each asset type can be independently cloned with its own allocator, which is crucial for memory management in Zig. This change aligns with the broader goal of improving asset loading and management in Cubyz.

## Related Questions
- What is the purpose of refactoring `common*` variables into a struct?
- Why is the `clone` function necessary in this context?
- How does this change improve memory management in Cubyz?
- What are the potential benefits of organizing asset handling code into a struct?
- How will this refactoring impact existing asset loading functionality?
- Can you explain the role of allocators in cloning these assets?
- What is the relationship between this PR and issue #1367?
- How does this change align with the broader goals of Cubyz development?
- Are there any potential performance implications from this refactoring?
- What are the maintenance advantages of having a structured approach to asset management?

*Source: unknown | chunk_id: github_issue_1205_discussion*
