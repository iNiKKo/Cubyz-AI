# [easy/codebase_assets_cubyz_recipes_special_recipes.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** inputs, output, reversible, crafting recipes, ore processing, block generation, torch-based crafting, material templates
**Symbols:** inputs, output, reversible
**Concepts:** crafting recipes, ore processing, block generation, reversible smelting, torch-based crafting, modular material templates

## Summary
This chunk defines a collection of special crafting recipes for the Cubyz voxel engine, including ore-to-ingot conversions, block creation from ingots, reversible smelting operations, and torch-based lamp/lantern synthesis.

## Explanation
The file contains an array of recipe objects, each specifying inputs (as a struct literal with .inputs field) and output (as a string). Several recipes include a .reversible = true flag indicating that the process can be undone. Inputs often use template strings like "{mod}:{type}_ore" or "{mod}:bars/{type}" to support modularity across different material types. Outputs include standard ingots, blocks (e.g., coal_block, iron_block), cut variants (cut_diamond_block), and composite items such as lamps and lanterns derived from torches and metal ingots.

## Related Questions
- What is the output of a recipe that takes cubyz:coal_ore and 8 cubyz:clay as inputs?
- Which recipes are marked as reversible in this configuration file?
- How does the template string "{mod}:{type}_ingot" behave when substituted with actual material names?
- What input combination produces cubyz:lamp, and what is its output?
- Can a cut_diamond_block be converted back into an ore using these recipes?
- Which recipe converts 4 cubyz:resin into a block, and does it support reversal?
- Are there any recipes that produce multiple units of the same item (e.g., 8 cubyz:glass/white)?
- What is the exact output string for a recipe with inputs {"cubyz:sulfur_torch", "2 cubyz:iron_ingot"}?
- Does this chunk define any recipes involving uranium or diamond materials?
- How many distinct lamp variants are defined in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_recipes_special_recipes.zig.zon_chunk_0*
