# [easy/codebase_assets_cubyz_sbb_phantasmal_auroras_low.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, chance, id, auroras, broken variants, spawn weight, configuration data
**Symbols:** blueprints
**Concepts:** blueprint configuration, spawn probability weights, phantasmal aurora structures

## Summary
This chunk defines the blueprint configuration for low-tier phantasmal aurora structures, listing each variant identifier and its spawn chance.

## Explanation
The chunk contains a single top-level field named blueprints which is an array of anonymous objects. Each object holds two fields: id (a string identifying the specific aurora blueprint) and chance (a float representing the probability weight for that blueprint). The identifiers follow the pattern cubyz:phantasmal/auroras/low/<index> with indices 0 through 9, plus three broken variants named broken_0, broken_1, and broken_2. Most entries have a chance of 1, while index 5 has a chance of 0.25 and the three broken variants each have a chance of 0.5.

## Related Questions
- What is the spawn chance for the aurora blueprint with id cubyz:phantasmal/auroras/low/5?
- Which aurora blueprints are classified as broken variants in this configuration?
- How many total low-tier phantasmal aurora blueprints are defined in this chunk?
- What is the chance value assigned to each of the broken variant blueprints?
- Does any blueprint other than the broken ones have a spawn chance less than 1.0?
- List all unique id strings present under the blueprints field.
- Are there any duplicate id values among the defined aurora blueprints?
- What is the sum of all chance values for the low-tier phantasmal auroras?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_auroras_low.zig.zon_chunk_0*
