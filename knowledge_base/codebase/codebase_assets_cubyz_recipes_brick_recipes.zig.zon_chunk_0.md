# [easy/codebase_assets_cubyz_recipes_brick_recipes.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** recipes, brick crafting, smooth to rough, tile, bricks, wall, pillar
**Concepts:** crafting recipes, item transformation

## Summary
Defines recipes for transforming smooth items into rough, tile, bricks, wall, and pillar forms of the same base item.

## Explanation
This chunk contains a list of recipe definitions, each specifying the inputs and outputs for crafting different brick types from smooth items. Each recipe is represented as an anonymous struct with fields for inputs, output, and optionally reversibility. The specific recipes are as follows:

1. **Smooth to Rough:**
   - Inputs: `cubyz:{item}/smooth`
   - Output: `cubyz:{item}/rough`
   - Reversible: true
2. **Smooth to Tile:**
   - Inputs: `cubyz:{item}/smooth`
   - Output: `cubyz:{item}/tile`
3. **Smooth to Bricks:**
   - Inputs: `cubyz:{item}/smooth`
   - Output: `cubyz:{item}/bricks`
4. **Smooth to Wall:**
   - Inputs: `cubyz:{item}/smooth`
   - Output: `2 cubyz:{item}/wall`
5. **Smooth to Pillar:**
   - Inputs: `cubyz:{item}/smooth`
   - Output: `cubyz:{item}/pillar`

## Related Questions
- What are the exact recipes for transforming a smooth item into rough, tile, bricks, wall, and pillar forms?
- Is there a recipe that allows reversing the transformation of a smooth item to rough?
- How many different types of brick transformations are defined in this chunk?
- What is the input required for all recipes listed in this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_recipes_brick_recipes.zig.zon_chunk_0*
