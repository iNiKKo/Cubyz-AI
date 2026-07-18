# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 0

**Type:** ui
**Keywords:** addon validation, engine defaults, field names, format mismatches, bug fixes, hand-editing, error messages
**Symbols:** blocks.zig:register(), items.zig:BaseItem.init(), Material.init(), registerProceduralItem(), items/recipes.zig:parseRecipe(), server/terrain/biomes.zig:Biome.init(), entityModel.zig:EntityModel.init()
**Concepts:** data-binding, form validation, live preview

## Summary
This chunk provides a comprehensive reference for the Cubyz engine's validation rules and default values for addon fields, including detailed notes on format mismatches, bug fixes, and advanced features. It serves as a critical guide for developers to ensure their addons are correctly formatted and compatible with the game environment.

## Explanation
The document outlines the expected fields, types, and defaults for various components of an addon, such as blocks, items, recipes, biomes, and entities. It highlights discrepancies between the website's form defaults and the engine's expectations, including specific field name mismatches (e.g., `isValidPlayerSpawn` vs `validPlayerSpawn`) and format issues (e.g., packed integers for colors). The reference is essential for developers to avoid common pitfalls and ensure their addons function correctly within the game environment.

## Related Questions
- What is the correct field name for player spawn in biomes?
- How does the engine handle missing fields in block definitions?
- Are there any discrepancies between website form defaults and engine expectations for items, such as material properties?
- What happens if a recipe has more than two items when trying to set it as reversible?
- Can procedural items be created using the Addon Creator website, or must they be hand-written?
- How does the engine handle invalid height ranges in biome definitions?
- Are there any specific tags required for cave biomes that are not enforced by the website UI?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_0*
