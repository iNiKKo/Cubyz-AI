# [easy/codebase_assets_cubyz_sbb_phantasmal_auroras_high.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, chance, id, phantasmal, auroras, high, broken, array literal, struct fields, static data
**Symbols:** blueprints
**Concepts:** configuration, blueprint registry, spawn probability

## Summary
This chunk defines a static configuration of blueprint identifiers for the phantasmal auroras high tier, each with an associated spawn chance value.

## Explanation
The chunk declares a single top-level field named blueprints which is an array literal containing ten struct entries. Each entry has two fields: id and chance. The first nine entries share the same base identifier prefix cubyz:phantasmal/auroras/high with numeric suffixes from 0 to 8, each assigned a chance value of 1. The final three entries use the same prefix but append the literal string broken_ followed by a digit (broken_0, broken_1, broken_2), and each is assigned a chance value of 0.5. No executable logic or functions are present; this is purely declarative configuration data.

## Related Questions
- What is the spawn chance for each blueprint in this configuration?
- How many distinct blueprint identifiers are defined in this chunk?
- Which entries have a non-unity chance value and what is that value?
- Are any of the blueprint IDs marked as broken variants?
- Does this chunk contain any executable functions or logic?
- What prefix do all the blueprint IDs share?
- How are the numeric suffixes ordered in the array literal?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_auroras_high.zig.zon_chunk_0*
