# [easy/codebase_assets_cubyz_sbb_phantasmal_pillar_large_large.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprint, chance, pillar, offshoot, variant
**Symbols:** blueprints
**Concepts:** world generation, configuration

## Summary
This chunk defines the blueprint configuration for large phantasmal pillars, listing five pillar variants with equal generation chance and two possible child offshoots.

## Explanation
The chunk declares a single top-level object containing a .blueprints array of five entries (ids 'cubyz:phantasmal/pillar/large/0' through '4', each with chance 1) plus one null entry with chance 0.3, and a .children map assigning the white child to 'cubyz:phantasmal/pillar/offshoot/offshoot' and the purple child to 'cubyz:phantasmal/pillar/top/top'.

## Related Questions
- What are the IDs of all large phantasmal pillar blueprints defined in this configuration?
- Which blueprint entry has a generation chance of zero point three and what is its ID value?
- How many distinct pillar variants are listed under the blueprints array before the null entry?
- What child blueprint path is assigned to the purple color key in the children map?
- What child blueprint path is assigned to the white color key in the children map?
- Does this configuration include any entries with a chance value greater than one?
- Are all non-null blueprints guaranteed to have an equal generation probability of one?
- How many total entries are present in the blueprints array including the null placeholder?
- What is the exact string identifier for the offshoot child blueprint referenced by white?
- What is the exact string identifier for the top child blueprint referenced by purple?
- Is there any ordering implied among the pillar variants beyond their numeric suffixes?
- Does this chunk declare any functions or executable logic, only data structures?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_pillar_large_large.zig.zon_chunk_0*
