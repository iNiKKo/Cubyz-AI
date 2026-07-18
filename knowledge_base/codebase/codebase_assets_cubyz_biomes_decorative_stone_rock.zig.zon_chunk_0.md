# [easy/codebase_assets_cubyz_biomes_decorative_stone_rock.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome configuration, terrain generation, height constraints, parent biomes, stone block type
**Concepts:** world_generation

## Summary
Defines configuration for a decorative stone rock biome in Cubyz.

## Explanation
This chunk configures the decorative stone rock biome: `radius = 16`, `chance = 0`, `minHeight = 1500`, `maxHeight = 3000`, `keepOriginalTerrain = 0.99`, `roughness = 1`, `mountains = 50`, `hills = 20`, `stoneBlock = "cubyz:slate/smooth"`. It has 14 parent biomes with individual generation chances, ranging from `cubyz:autumn/forest` (chance 2) to the most likely, `cubyz:rocky_grassland` (chance 24); others include `cubyz:tundra/base` (12), `cubyz:autumn/dead_forest`/`cubyz:grassland` (3 each), `cubyz:taiga/base`/`cubyz:forest/mixed/oak_birch`/`cubyz:forest/mixed/oak_pine`/`cubyz:forest/birch` (4 each), `cubyz:tundra/patchy` (6), and `cubyz:rare/tuften/fields`/`cubyz:hills/temperate`/`cubyz:hills/cold` (3 each).

## Related Questions
- What is the radius of the decorative stone rock biome?
- What is the minimum height for this biome to generate?
- Which stone block is used in this biome?
- How many parent biomes are associated with this biome?
- What is the chance of generating a mountain in this biome?
- What is the probability of keeping the original terrain when generating this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_decorative_stone_rock.zig.zon_chunk_0*
