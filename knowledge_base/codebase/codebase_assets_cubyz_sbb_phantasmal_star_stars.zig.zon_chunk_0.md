# [easy/codebase_assets_cubyz_sbb_phantasmal_star_stars.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, chance, id, phantasmal, star, broken, blood_star, f32, string, array
**Symbols:** blueprints
**Concepts:** asset configuration, blueprint registry, spawn probability

## Summary
This chunk defines a static configuration of blueprint entries for the phantasmal star asset collection, each with an identifier and spawn chance.

## Explanation
The chunk contains a single top-level field named blueprints which is an array literal holding twelve struct instances. Each instance has two fields: id (a string constant) and chance (a f32). The first eleven entries share the prefix cubyz:phantasmal/star/ with numeric suffixes 0 through 8, followed by broken_0, broken_1, and broken_2 each assigned a chance of 0.25. The final entry is named blood_star with a chance of 0.01. No executable logic or functions are present; this is purely declarative data.

## Related Questions
- What is the spawn chance for the blueprint with id cubyz:phantasmal/star/0?
- Which blueprints in this configuration have a non-zero chance value?
- How many entries are defined under the blueprints field?
- Does any entry use a broken_ prefix and what is its chance?
- What is the chance assigned to blood_star compared to the others?
- Are all id strings prefixed with cubyz:phantasmal/star/ in this chunk?
- How many entries have exactly 0.25 as their chance value?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_star_stars.zig.zon_chunk_0*
