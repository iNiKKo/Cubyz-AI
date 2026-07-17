# [src/server/world.zig] - Chunk 2637876307

**Type:** review
**Keywords:** loadWorldData, loadWorldConfig, ZonElement, ServerWorld, world configuration, terminology, consistency, refactor, API clarity, data scope
**Symbols:** ServerWorld, loadWorldData, loadWorldConfig, ZonElement
**Concepts:** API naming clarity, configuration vs. runtime data, terminology consistency, refactor motivation, issue tracking

## Summary
The reviewer suggests renaming `loadWorldData` to `loadWorldConfig` because 'world data' is too broad a term; the change addresses terminology consistency while noting that broader initialization inconsistencies will be handled separately.

## Explanation
In the context of Cubyz's server world management, the function originally named `loadWorldData` was responsible for loading configuration from a ZonElement. The reviewer pointed out that 'world data' is ambiguous—it could imply entity data or other runtime state—whereas this specific call only handles static configuration values (e.g., terrain settings, chunk generation parameters). Renaming to `loadWorldConfig` clarifies the scope and aligns with existing naming conventions in the codebase. The reviewer also acknowledged that while initialization from Zon is inconsistent across the project, fixing all such cases is beyond the scope of this PR; instead, they will open an issue for future discussion. This change improves API clarity without altering behavior, preventing potential misuse by developers who might assume broader data loading than actually occurs.

## Related Questions
- What other functions in world.zig load data from ZonElement and how are they named?
- Is there a distinction between configuration and entity data loading elsewhere in the codebase?
- Where is the issue tracker referenced for future fixes to inconsistent initialization?
- How does renaming affect binary compatibility or public API contracts?
- Are there any tests that specifically cover loadWorldData behavior after this rename?
- What documentation strings accompany loadWorldConfig and do they reflect its narrower scope?
- Does the ServerWorld struct have other methods dealing with world state initialization?
- Is ZonElement a custom type or imported from another module in Cubyz?
- How does the reviewer plan to address broader initialization inconsistencies outside this PR?
- Are there any migration paths for existing code calling loadWorldData after this change?

*Source: unknown | chunk_id: github_pr_2422_comment_2637876307*
