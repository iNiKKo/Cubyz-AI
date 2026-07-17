# [easy/codebase_assets_cubyz_sbb_tree_oak_old_growth.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, trunk, branch_extender, root, deco, small_branch, top, children
**Symbols:** blueprints, children
**Concepts:** asset registry, tree generation, blueprint composition

## Summary
This chunk defines the blueprint registry for an old-growth oak tree, listing trunk segments and child parts with their identifiers.

## Explanation
The chunk declares a single top-level struct (implicitly named via its field access) containing two fields: blueprints and children. The blueprints field is an array of anonymous structs each holding an id string for trunk segments indexed 0 through 4. The children field is an object mapping color keys to blueprint identifiers for root, branch_extender, top, deco, and small_branch.

## Related Questions
- What are the IDs of all trunk segments defined in this blueprint?
- Which child part is associated with the color brown?
- How many trunk segments are listed under blueprints?
- Is there a child part named top and what is its identifier?
- Does this configuration include a deco child part?
- What identifier corresponds to the small_branch child?
- Are all children defined as strings pointing to other blueprint IDs?
- Can I determine the order of trunk segments from this data?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_oak_old_growth.zig.zon_chunk_0*
