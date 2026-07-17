# [easy/codebase_assets_cubyz_recipes_brick_recipes.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** recipe, inputs, output, reversible, crafting, item, smooth, rough, tile, bricks, wall, pillar
**Symbols:** inputs, output, reversible
**Concepts:** recipe configuration, item crafting, smooth to rough conversion, smooth to tile conversion, smooth to bricks conversion, smooth to wall conversion, smooth to pillar conversion, reversible crafting

## Summary
This chunk defines a collection of brick recipe configurations, mapping smooth item inputs to various output forms including rough, tile, bricks, wall (quantity 2), and pillar.

## Explanation
The chunk contains five distinct recipe entries. Each entry specifies an inputs field containing a single smooth item reference formatted as cubyz:{item}/smooth, and an output field defining the resulting item or quantity of items. The first entry additionally includes a reversible flag set to true, indicating that this specific transformation can be undone. The remaining four entries lack the reversible attribute.

## Related Questions
- What is the output of a smooth item when reversible crafting is enabled?
- Which recipe produces two wall items from a single smooth input?
- How many distinct outputs are defined for the smooth input in this chunk?
- Is there any difference between the first and second recipe entries besides the reversible flag?
- What output corresponds to the third entry in the list of brick recipes?
- Which entry defines the pillar crafting outcome from a smooth item?

*Source: unknown | chunk_id: codebase_assets_cubyz_recipes_brick_recipes.zig.zon_chunk_0*
