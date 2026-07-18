# [src/assets.zig] - PR #2129 review diff

**Type:** review
**Keywords:** structureTables, structureTableMigrations, per-world palettes, addons, biomes, migrations
**Symbols:** Assets, ZonHashMap, AddonNameToZonMap
**Concepts:** architectural design, data management, versioning

## Summary
Added `structureTables` and `structureTableMigrations` fields to the `Assets` struct.

## Explanation
The reviewer is concerned about the purpose of per-world palettes and whether they are necessary for introducing addons that add structures to existing biomes. The addition of `structureTables` and `structureTableMigrations` suggests a need to manage structure data and potential changes in their locations or names across different world versions.

## Related Questions
- What is the purpose of the `structureTables` field in the `Assets` struct?
- How does the addition of `structureTableMigrations` address potential changes in structure locations or names?
- Are there any implications for backward compatibility with existing worlds when introducing these new fields?
- How are `ZonHashMap` and `AddonNameToZonMap` used to manage structure data and migrations?
- What is the relationship between per-world palettes and the ability to introduce addons that add structures to biomes?
- Are there any performance considerations associated with managing structure tables and their migrations?

*Source: unknown | chunk_id: github_pr_2129_comment_2860728351*
