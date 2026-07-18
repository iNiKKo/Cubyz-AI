# [easy/codebase_assets_cubyz_biomes__migrations.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome migration, world update, identifier mapping, game assets, data structure
**Concepts:** world generation, biome system

## Summary
Defines a list of biome migration rules.

## Explanation
This chunk contains a series of mappings from old biome identifiers to new ones, representing changes in the Cubyz game's biome system. Each entry specifies an `old` and a `new` string that represent the old and new names for a particular biome type. This data is likely used during world generation or loading processes to update biomes according to the latest definitions. The following is a comprehensive list of all the mappings defined in this chunk:

- `.old = "cave/void_cavern", .new = "cave/void/void_cavern"`
- `.old = "cave/void_roots", .new = "cave/void/void_roots"`
- `.old = "clearing", .new = "forest/clearing"`
- `.old = "desert", .new = "desert/base"`
- `.old = "forest", .new = "forest/base"`
- `.old = "jungle(TODO)", .new = "jungle"`
- `.old = "swamp", .new = "swamp/base"`
- `.old = "taiga", .new = "taiga/base"`
- `.old = "tundra", .new = "tundra/base"`
- `.old = "forest/base", .new = "forest/mixed/oak_birch"`
- `.old = "forest/clearing", .new = "forest/mixed/oak_birch_clearing"`
- `.old = "beach", .new = "beach/warm/base"`
- `.old = "jungle", .new = "jungle/base"`
- `.old = "ocean", .new = "ocean/temperate/base"`
- `.old = "ocean_shelf", .new = "ocean/temperate/shelf"`
- `.old = "cold_ocean", .new = "ocean/cold/base"`
- `.old = "warm_ocean", .new = "ocean/warm/base"`
- `.old = "prairie/dry_spell", .new = "prairie/dry_spell/base"`
- `.old = "prairie/limestone_pit", .new = "prairie/limestone_pit/base"`
- `.old = "rainbow_forest", .new = "rare/rainbow_forest"`
- `.old = "modern_art", .new = "rare/modern_art"`
- `.old = "glass_forest", .new = "rare/glass_forest"`
- `.old = "spawn", .new = "rare/spawn"`
- `.old = "cave/glimmergill", .new = "cave/mushroom/glimmergill"`
- `.old = "cave/glimmergill_big", .new = "cave/mushroom/big/glimmergill"`
- `.old = "cave/toadstool_big", .new = "cave/mushroom/big/toadstool"`
- `.old = "cave/bolete_big", .new = "cave/mushroom/big/bolete"`
- `.old = "flatland", .new = "development/flat"`
- `.old = "island", .new = "ocean/temperate/island/base"`
- `.old = "island_shelf", .new = "ocean/temperate/island/shelf"`
- `.old = "cave/cave", .new = "cave/slate/base"`
- `.old = "tall_mountain/peak", .new = "tall_mountain/summit1"`
- `.old = "bush_lands", .new = "bushlands/base"`

## Related Questions
- What is the purpose of this chunk?
- How are old biome identifiers mapped to new ones?
- Can you list all the old biomes that have been renamed?
- Is there a mapping for 'jungle(TODO)' in this chunk?
- What is the new identifier for 'desert'?
- Does this chunk include any mappings related to ocean biomes?
- How many biome migration rules are defined in total?
- Can you provide an example of a biome migration rule?
- Is there a mapping for 'flatland' in this chunk?
- What is the new identifier for 'cave/cave'?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes__migrations.zig.zon_chunk_0*
