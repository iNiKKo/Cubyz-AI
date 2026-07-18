# [easy/codebase_assets_cubyz_sbb_tree_coniferous_pine_eastern_white_2_branched_trunk.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, children, branching, hierarchical structure, tree segments
**Concepts:** world generation, tree branching

## Summary
Defines the structure and branching patterns of an Eastern White Pine tree in the Cubyz voxel engine.

## Explanation
This chunk specifies the blueprints and child nodes for a particular type of coniferous tree, detailing its stem and various branch segments. The `.blueprints` array contains a single entry with an ID identifying the tree's stem blueprint: `cubyz:tree/coniferous/stem/5/0`. The `.children` object maps color identifiers to specific branch segment IDs, outlining the hierarchical structure of the tree from top to bottom as follows:
- `.white`: `cubyz:tree/coniferous/pine/eastern_white/3_tip`
- `.purple`: `cubyz:tree/coniferous/pine/eastern_white/branches/normal/4_top`
- `.crimson`: `cubyz:tree/coniferous/pine/eastern_white/branches/normal/3_middle_top`
- `.red`: `cubyz:tree/coniferous/pine/eastern_white/branches/normal/2_middle`
- `.orange`: `cubyz:tree/coniferous/pine/eastern_white/branches/normal/1_bottom_middle`
- `.yellow`: `cubyz:tree/coniferous/pine/eastern_white/branches/normal/0_bottom`

## Related Questions
- What is the ID of the stem blueprint for the Eastern White Pine tree?
- Which color identifier corresponds to each branch segment in the Eastern White Pine tree?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_coniferous_pine_eastern_white_2_branched_trunk.zig.zon_chunk_0*
