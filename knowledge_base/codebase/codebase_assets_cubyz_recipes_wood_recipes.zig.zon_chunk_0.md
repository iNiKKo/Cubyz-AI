# [easy/codebase_assets_cubyz_recipes_wood_recipes.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** recipes, crafting, inputs, outputs, placeholders
**Concepts:** crafting system, item recipes

## Summary
Defines various wood-based crafting recipes for the Cubyz game.

## Explanation
This chunk contains a list of crafting recipe definitions in the form of anonymous structs. Each recipe specifies its inputs and output, where inputs are arrays of strings representing item identifiers with placeholders like `{mod}` and `{type}`, and outputs are single strings representing the crafted item identifier. Exact recipes defined here: 4 planks (any wood type) -> 1 workbench. 1 log -> 4 planks (same wood type). 1 log -> 2 branches (same wood type). 1 branch -> 2 planks (same wood type). 1 plank -> 2 fences (same wood type). 1 plank -> 1 sign (same wood type). 4 planks (same wood type) -> 1 chest. 1 candy cane block -> 2 candy-cane branches. Planks (any mod's, any type) + coal ore -> 8 torches. Planks + sulfur ore -> 8 sulfur torches. Planks + lumiflora -> 8 lumi torches.

## Related Questions
- What are the inputs required to craft a workbench?
- How do you make/craft a workbench in Cubyz?
- How many planks are produced from one log?
- Which items can be crafted using sulfur ore as an ingredient?
- What is the output of crafting four planks with any mod's planks and coal ore?
- List all recipes that produce torches.
- Can logs be directly converted to branches without intermediate steps?
- How many planks does crafting a chest require?

*Source: unknown | chunk_id: codebase_assets_cubyz_recipes_wood_recipes.zig.zon_chunk_0*
