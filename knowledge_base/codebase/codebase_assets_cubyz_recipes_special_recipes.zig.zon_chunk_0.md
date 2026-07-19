# [easy/codebase_assets_cubyz_recipes_special_recipes.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** recipes, crafting, inputs, outputs, reversible
**Concepts:** crafting, recipes

## Summary
Defines detailed special crafting recipes for items such as blocks, ingots, and crafted items in Cubyz. Each recipe specifies exact input materials and outputs, with some being reversible.

## Explanation
This chunk contains a list of specific special recipes used in the Cubyz game. Each recipe is defined by an anonymous struct containing `.inputs` (an array of input strings) and `.output` (a string for the output). Some recipes also include a `.reversible` field set to `true`, indicating that the crafting process can be reversed back to its inputs. Here are all the detailed recipes provided in raw_content:

- **Inputs:** `{cubyz:coal_ore, {mod}:{type}_ore}`
  **Output:** `{mod}:{type}_ingot`
- **Inputs:** `{cubyz:coal_ore, 8 cubyz:clay}`
  **Output:** `8 cubyz:terracotta/smooth`
- **Inputs:** `{cubyz:coal_ore, 8 cubyz:sand}`
  **Output:** `8 cubyz:glass/white`
- **Inputs:** `{1 cubyz:torch, 2 cubyz:iron_ingot}`
  **Output:** `cubyz:lamp`
- **Inputs:** `{1 cubyz:sulfur_torch, 2 cubyz:iron_ingot}`
  **Output:** `cubyz:sulfur_lamp`
- **Inputs:** `{2 cubyz:torch, 1 cubyz:iron_ingot}`
  **Output:** `2 cubyz:lantern/coal`
- **Inputs:** `{2 cubyz:sulfur_torch, 1 cubyz:iron_ingot}`
  **Output:** `2 cubyz:lantern/sulfur`
- **Inputs:** `{4 cubyz:resin}`
  **Output:** `cubyz:resin_block` (reversible)
- **Inputs:** `{4 cubyz:coal_ore}`
  **Output:** `cubyz:coal_block` (reversible)
- **Inputs:** `{4 cubyz:sulfur_ore}`
  **Output:** `cubyz:sulfur_block`
- **Inputs:** `{4 cubyz:copper_ingot}`
  **Output:** `cubyz:copper_block` (reversible)
- **Inputs:** `{4 cubyz:iron_ingot}`
  **Output:** `cubyz:iron_block` (reversible)
- **Inputs:** `{4 cubyz:meteorite_ingot}`
  **Output:** `cubyz:meteorite_block` (reversible)
- **Inputs:** `{1 cubyz:iron_ingot}`
  **Output:** `4 cubyz:chain/iron`
- **Inputs:** `{4 cubyz:silver_ingot}`
  **Output:** `cubyz:silver_block` (reversible)
- **Inputs:** `{4 cubyz:gold_ingot}`
  **Output:** `cubyz:gold_block` (reversible)
- **Inputs:** `{4 cubyz:uranium_ingot}`
  **Output:** `cubyz:uranium_block` (reversible)
- **Inputs:** `{8 cubyz:glass/white, cubyz:uranium_ingot}`
  **Output:** `8 cubyz:glass/uranium`
- **Inputs:** `{4 cubyz:diamond_ore}`
  **Output:** `cubyz:diamond_block` (reversible)
- **Inputs:** `{cubyz:diamond_block}`
  **Output:** `cubyz:cut_diamond_block`
- **Inputs:** `{4 cubyz:amber_ore}`
  **Output:** `cubyz:amber_block` (reversible)
- **Inputs:** `{cubyz:amber_block}`
  **Output:** `cubyz:cut_amber_block`
- **Inputs:** `{4 cubyz:ruby_ore}`
  **Output:** `cubyz:ruby_block` (reversible)
- **Inputs:** `{cubyz:ruby_block}`
  **Output:** `cubyz:cut_ruby_block`
- **Inputs:** `{cubyz:cut_diamond_block}`
  **Output:** `4 cubyz:diamond_ore`
- **Inputs:** `{cubyz:cut_amber_block}`
  **Output:** `4 cubyz:amber_ore`
- **Inputs:** `{cubyz:cut_ruby_block}`
  **Output:** `4 cubyz:ruby_ore`
- **Inputs:** `{4 cubyz:jade_ore}`
  **Output:** `cubyz:jade_block` (reversible)
- **Inputs:** `{cubyz:jade_block}`
  **Output:** `cubyz:cut_jade_block`
- **Inputs:** `{cubyz:cut_jade_block}`
  **Output:** `4 cubyz:jade_ore`
- **Inputs:** `{cubyz:gravel}`
  **Output:** `4 cubyz:pebbles` (reversible)

These recipes provide a comprehensive set of crafting instructions for various materials and items in the game.

## Related Questions
- What are the inputs for crafting a cubyz:lamp?
- Is there a recipe to reverse the creation of a cubyz:resin_block?
- List all recipes that require cubyz:iron_ingot as an input.
- Which items can be crafted from cubyz:diamond_ore?
- Are there any reversible recipes involving cubyz:silver_ingot?
- What is the output of crafting 4 cubyz:jade_ore?

*Source: unknown | chunk_id: codebase_assets_cubyz_recipes_special_recipes.zig.zon_chunk_0*
