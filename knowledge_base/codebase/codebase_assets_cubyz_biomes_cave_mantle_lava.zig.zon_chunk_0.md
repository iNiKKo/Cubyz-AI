# [easy/codebase_assets_cubyz_biomes_cave_mantle_lava.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** chance, size, depth, smoothness, structure, block, caveModels
**Symbols:** cave_mantle_lava, chance, caves, soilCreep, structures, id, structure, placeMode, size, size_variation, baseSlope, topSlope, ground_patch, block, width, variation, depth, smoothness, caveModels, minAmount, maxAmount, minRadius, maxRadius, minHeight, maxHeight, mode
**Concepts:** biome configuration, cave structure, ground patch, cave model

## Summary
Cave structure configuration for lava mantle biome

## Explanation
This chunk defines the configuration for cave structures in the lava mantle biome. It includes various types of structures such as sbb, stalagmites, ground patches, and cave models with specific properties like chance, size, depth, smoothness, block type, width, variation, and mode.

- The overall chance for caves is 0.5.
- The soil creep value is 2.
- For the sbb structure:
  - ID: cubyz:sbb
  - Structure: cubyz:cave/mantle/lava_pool
  - PlaceMode: degradable
  - Chance: 0.05
- For stalagmites with pyrolite/rough block:
  - First instance:
    - ID: cubyz:stalagmite
    - Block: cubyz:pyrolite/rough
    - Chance: 0.05
    - Size: 12
    - Size variation: 6
    - Base slope: 0
    - Top slope: 8
  - Second instance:
    - ID: cubyz:stalagmite
    - Block: cubyz:pyrolite/rough
    - Chance: 0.15
    - Size: 4
    - Size variation: 6
- For ground patches with lava block:
  - ID: cubyz:ground_patch
  - Block: cubyz:lava
  - Chance: 0.05
  - Width: 4
  - Variation: 2
  - Depth: 2
  - Smoothness: 1
- For ground patches with magma block:
  - First instance:
    - ID: cubyz:ground_patch
    - Block: cubyz:magma
    - Chance: 0.2
    - Width: 3
    - Variation: 2
    - Depth: 2
    - Smoothness: 0.05
  - Second instance:
    - ID: cubyz:ground_patch
    - Block: cubyz:magma
    - Chance: 0.04
    - Width: 6
    - Variation: 5
    - Depth: 2
    - Smoothness: 0.05
- For cave models:
  - ID: cubyz:cylinder
  - Min amount: 10
  - Max amount: 20
  - Min radius: 6
  - Max radius: 10
  - Min height: 80
  - Max height: 200
  - Mode: additive

## Related Questions
-  What is the overall chance for caves in the lava mantle biome?
-  What is the soil creep value for the lava mantle biome?
-  For the sbb structure, what are its ID and chance of placement?
-  How many ground patches with magma block have a depth of 2?
-  What are the specific properties (chance, size, variation) of the first stalagmite structure with pyrolite/rough block?
-  What is the maximum height of cave models in the lava mantle biome?
-  For the second instance of ground patches with magma block, what are its width and variation?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_cave_mantle_lava.zig.zon_chunk_0*
