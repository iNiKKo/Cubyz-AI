# [easy/codebase_assets_cubyz_sbb_phantasmal_pillar_medium_medium.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, chance, id, children, white, purple, offshoot, top, null, pillar, medium
**Symbols:** blueprints, children
**Concepts:** blueprint configuration, pillar generation, component hierarchy

## Summary
This chunk defines the blueprint configuration for medium phantasmal pillars, listing seven pillar variants with equal generation chance and one null entry with a lower chance, along with child offshoot and top components.

## Explanation
The chunk declares a single object containing two fields: blueprints and children. The blueprints field is an array of objects each holding an id string (cubyz:phantasmal/pillar/medium/0 through cubyz:phantasmal/pillar/medium/6) paired with a chance value of 1, followed by one entry where the id is null and the chance is 0.6. The children field maps color keys white and purple to their respective blueprint paths cubyz:phantasmal/pillar/offshoot/offshoot and cubyz:phantasmal/pillar/top/top.

## Related Questions
- What is the generation chance for each of the seven medium phantasmal pillar blueprints?
- Which blueprint id corresponds to a null entry in the blueprints array?
- What are the child component paths associated with the white and purple keys?
- How many distinct pillar variants are defined under cubyz:phantasmal/pillar/medium?
- Does any blueprint entry have a chance value less than 1, and if so which one?
- Are there any other color keys besides white and purple in the children mapping?
- What is the exact string format of the id field for each pillar blueprint entry?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_phantasmal_pillar_medium_medium.zig.zon_chunk_0*
