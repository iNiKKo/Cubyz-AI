# [easy/codebase_assets_cubyz_biomes_ocean_temperate_island_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** height, radius, structures, biome, configuration
**Concepts:** world generation, biome configuration

## Summary
Defines configuration for a temperate island biome in the Cubyz game.

## Explanation
This chunk contains a JSON-like structure defining various properties of a temperate island biome in the Cubyz game. It specifies the following details:

- **Minimum Height:** 5
- **Maximum Height:** 6
- **Radius:** 32
- **Soil Creep:** 1
- **Number of Hills:** 4
- **Tags:** oak
- **Ground Structures:**
  - Cubyz:grass/temperate
  - 1 to 2 cubyz:soil
- **Structures:**
  - Simple Tree:
    - ID: `cubyz:simple_tree`
    - Leaves: `cubyz:leaves/oak`
    - Log: `cubyz:log/oak`
    - Chance: 0.016
    - Type: round
    - Height: 12
    - Height Variation: 10
    - Leaf Radius: 5
    - Leaf Radius Variation: 6
  - Flower Patch (Grass Vegetation):
    - ID: `cubyz:flower_patch`
    - Blocks: `cubyz:grass/vegetation/temperate`
    - Chance: 0.08
    - Width: 3
    - Variation: 2
    - Density: 0.5
    - Priority: 0.2
  - Flower Patch (Hibiscus):
    - ID: `cubyz:flower_patch`
    - Blocks: `cubyz:hibiscus:0`, `cubyz:hibiscus:1`, `cubyz:hibiscus:2`, `cubyz:hibiscus:3`
    - Chance: 0.03
    - Width: 3
    - Variation: 2
    - Density: 0.3
    - Priority: 0.2
- **Parent Biomes:**
  - ID: `cubyz:ocean/temperate/island/shelf`
  - Chance: 1
  - Parent Edge Distance: 37

## Related Questions
- What is the minimum height of the temperate island biome?
- How many different types of structures are defined for this biome?
- What is the chance of generating a simple tree in this biome?
- Which blocks can be found in the flower patches of this biome?
- What is the parent biome associated with this one, and what is its chance?
- What is the maximum height variation allowed for trees in this biome?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_temperate_island_base.zig.zon_chunk_0*
