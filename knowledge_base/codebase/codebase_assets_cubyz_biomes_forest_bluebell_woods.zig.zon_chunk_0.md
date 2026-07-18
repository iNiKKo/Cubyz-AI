# [easy/codebase_assets_cubyz_biomes_forest_bluebell_woods.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** biome config, forest structure, tree placement, flower patching, height variation
**Symbols:** BluebellWoods
**Concepts:** biome, structure, chance

## Summary
Biome configuration for Bluebell Woods

## Explanation
Defines properties, tags, and structures for the Bluebell Woods biome.

- **Properties:**
  - `minHeightLimit`: 7
  - `minHeight`: 35
  - `maxHeight`: 40
  - `maxHeightLimit`: 50
  - `smoothBeaches`: true
  - `minRadius`: 200
  - `maxRadius`: 280
  - `roughness`: 5
  - `hills`: 2
  - `chance`: 0.3
  - `music`: "cubyz:totaldemented/leaves"
  - `validPlayerSpawn`: true
- **Tags:**
  - `.birch`
  - `.oak`
- **Ground Structure:**
  - Grass: `cubyz:grass/temperate`
  - Soil: 2 to 3 layers of `cubyz:soil`
- **Structures:**
  - Old Growth Oak Tree (`cubyz:sbb`)
    - Structure: `cubyz:tree/oak/old_growth`
    - Place Mode: degradable
    - Chance: 0.1
  - Silver Birch Trees (`cubyz:sbb`)
    - Structure: `cubyz:tree/birch/silver/1`, `cubyz:tree/birch/silver/2`
    - Place Mode: degradable
    - Chance: 0.005 for each type
  - Fallen Oak Tree (`cubyz:fallen_tree`)
    - Log Type: `cubyz:log/oak`
    - Height: 6 cubyz
    - Height Variation: 3 cubyz
    - Chance: 0.01
  - Fallen Birch Tree (`cubyz:fallen_tree`)
    - Log Type: `cubyz:log/birch`
    - Height: 6 cubyz
    - Height Variation: 3 cubyz
    - Chance: 0.003
  - Simple Vegetation (`cubyz:simple_vegetation`)
    - Block: `cubyz:grass/vegetation/temperate`
    - Chance: 0.4
    - Height: 1 cubyz
    - Height Variation: 0 cubyz
  - Flower Patches (`cubyz:flower_patch`)
    - Bluebells
      - Blocks: `cubyz:bluebells`
      - Width: 6 cubyz
      - Variation: 3 cubyz
      - Density: 0.5
      - Priority: 0.1
    - Vetch
      - Blocks: `cubyz:vetch`
      - Width: 6 cubyz
      - Variation: 3 cubyz
      - Density: 0.3
      - Priority: 0.1
    - Temperate Grass Vegetation
      - Blocks: `cubyz:grass/vegetation/temperate`
      - Width: 6 cubyz
      - Variation: 3 cubyz
      - Density: 0.3
      - Priority: 0.1

## Related Questions
- What are the tags associated with Bluebell Woods?
- What is the minimum height limit for Bluebell Woods?
- How many structures are defined for Bluebell Woods?
- What is the chance of placing a fallen tree in Bluebell Woods?
- What is the maximum radius for Bluebell Woods?
- What is the roughness value for Bluebell Woods?
- What is the height of simple vegetation in Bluebell Woods?
- What are the blocks used in the flower patch in Bluebell Woods?
- What is the width of the flower patches in Bluebell Woods?
- What is the priority of the bluebells in the flower patches in Bluebell Woods?
- What is the height variation for the fallen trees in Bluebell Woods?
- What is the chance of placing a silver birch tree in Bluebell Woods?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_forest_bluebell_woods.zig.zon_chunk_0*
