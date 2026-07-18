# [issues/issue_1205.md] - Issue #1205 discussion

**Type:** review
**Keywords:** refactor, struct, clone, Zig, StringHashMap, allocator, maintenance, organization, code duplication, improvement
**Symbols:** commonBlocks, commonBlockMigrations, commonItems, commonTools, commonBiomes, commonBiomeMigrations, commonRecipes, commonModels, readAssets
**Concepts:** refactoring, memory management, asset loading

## Summary
The `common*` variables from `assets.zig` are being refactored into a struct, and the `clone` function should be included.

## Explanation
The current implementation of asset handling in Cubyz uses multiple global variables to store different types of assets such as blocks, block migrations, items, tools, biomes, biome migrations, recipes, and models. These variables are defined as `std.StringHashMap(ZonElement)` for most types except `commonModels`, which is a `std.StringHashMap([]const u8)`. The refactoring involves moving these global variables into a struct to improve code organization and maintainability. Specifically, the variables include `commonBlocks`, `commonBlockMigrations`, `commonItems`, `commonTools`, `commonBiomes`, `commonBiomeMigrations`, `commonRecipes`, and `commonModels`. Each of these variables is cloned using the `clone` function with its own allocator, which is crucial for memory management in Zig. This change aligns with the broader goal of improving asset loading and management in Cubyz by reducing code duplication and enhancing maintenance practices. The `readAssets` function takes pointers to these variables and clones them with a specified allocator, ensuring that each asset type can be independently managed. This refactoring also simplifies the process of updating and maintaining asset data within the game.

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
