# [easy/codebase_assets_cubyz_sbb_phantasmal_phantasmal_pillars.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, id, blueprint, pillar, color, mapping, spawn, probability, asset, identifier
**Symbols:** .blueprints, .children
**Concepts:** asset blueprint selection, spawn probability configuration, pillar color mapping

## Summary
Defines blueprint asset identifiers and their spawn chances, plus a children mapping that links color names to pillar blueprint IDs.

## Explanation
This chunk declares a single top-level anonymous struct containing two fields: .blueprints and .children. The .blueprints field is an array of objects each with an .id string (prefixed with cubyz:phantasmal/base/...) and a .chance float; the first six entries have chance 1, the next four medium entries have chance 0.3, and the final three large entries have chance 0.1. The .children field is an object mapping color names to pillar blueprint IDs: black maps to cubyz:phantasmal/pillar/large/large, dark_grey maps to cubyz:phantasmal/pillar/medium/medium, and grey maps to cubyz:phantasmal/pillar/small/small.

## Related Questions
- What are the spawn chances for each phantasmal base blueprint?
- Which pillar blueprint ID corresponds to the black color in children?
- How many small blueprints have a chance of exactly 1.0?
- What is the total number of entries defined under .blueprints?
- Does any entry in .children reference a large pillar blueprint?
- Are all .id strings prefixed with cubyz:phantasmal/base/ or cubyz:phantasmal/pillar/?
- Which color name maps to the medium pillar blueprint ID?
- What is the chance value for the first large pillar entry in .blueprints?
- Is there any blueprint with a chance greater than 1.0 defined here?
- How many entries under .children are present and what are their keys?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_phantasmal_pillars.zig.zon_chunk_0*
