# [easy/codebase_assets_cubyz_sbb_tree_palm_coconut.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, children, fronds, trunk, tilt, leaning, coconut palm, straight variants
**Symbols:** blueprints, children
**Concepts:** asset collection, blueprint registry, tree model hierarchy

## Summary
Defines the blueprint asset collection for coconut palm tree trunks (straight, tilt, leaning variants) and their frond children.

## Explanation
This chunk declares a static array of blueprint identifiers under the .blueprints field, enumerating straight trunk IDs from 6 through 11 plus an extra variant 6a, tilt trunk IDs from 6 through 12 with corresponding 6a/7a variants, and leaning trunk IDs from 7 through 12. It also defines a single child entry under .children mapping the key lime to the fronds blueprint ID cubyz:tree/palm/coconut/fronds.

## Related Questions
- What blueprint IDs are included in the straight trunk category for coconut palms?
- How many tilt variant trunks are defined and what is their ID range?
- Which child asset does the lime key reference in this configuration?
- Are any leaning trunk variants missing from the 7-12 sequence?
- Does the fronds child point to a different namespace than the trunk blueprints?
- What is the total count of straight trunk entries versus tilt entries?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_palm_coconut.zig.zon_chunk_0*
