# [src/assets.zig] - PR #2129 review diff

**Type:** review
**Keywords:** structureTables, structureTableMigrations, per-world palettes, addons, biomes, migrations
**Symbols:** Assets, ZonHashMap, AddonNameToZonMap
**Concepts:** architectural design, data management, migrations

## Summary
Added `structureTables` and `structureTableMigrations` fields to the `Assets` struct.

## Explanation
The reviewer is questioning the purpose of per-world palettes, suggesting that they might be needed for introducing addons that add structures to existing biomes. The addition of `structureTables` and `structureTableMigrations` indicates a potential need for managing structure data within worlds, with migrations handling any changes in structure table locations or names.

## Related Questions
- What is the purpose of the `structureTables` field in the `Assets` struct?
- How do `structureTableMigrations` handle changes in structure table locations or names?
- Are there any potential performance implications with adding these new fields to the `Assets` struct?
- Does this change affect backwards compatibility with existing worlds?
- What is the relationship between per-world palettes and the addition of structure tables?
- How are migrations implemented for structure tables in Cubyz?
- Is there a need for additional validation when modifying structure table data?
- Can these changes impact the loading time of world assets?
- Are there any potential memory usage considerations with the new fields?
- What is the expected behavior if an addon attempts to add structures to a non-existent biome?

*Source: unknown | chunk_id: github_pr_2129_comment_2860728351*
