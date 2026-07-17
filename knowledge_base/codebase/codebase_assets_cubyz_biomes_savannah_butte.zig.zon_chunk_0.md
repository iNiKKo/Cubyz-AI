# [easy/codebase_assets_cubyz_biomes_savannah_butte.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** hot, dry, barren, minHeight, maxHeight, roughness, hills, stripes, stoneBlock, parentBiomes
**Symbols:** .properties, .hot, .dry, .barren, .minHeight, .maxHeight, .minRadius, .maxRadius, .roughness, .chance, .hills, .stripes, .direction, .block, .distance, .offset, .width, .stoneBlock, .parentBiomes, .id
**Concepts:** biome configuration, terrain generation parameters, stripe pattern definition, parent biome transition

## Summary
Configuration data defining the Savannah Butte biome with its terrain height limits, roughness parameters, stripe patterns, and parent biome relationships.

## Explanation
This chunk contains a single configuration structure (`.properties`) for the Savannah Butte biome. It defines environmental attributes including hot/dry/barren flags, minHeight/maxHeight bounds of 75/100, minRadius/maxRadius bounds of 33/48, and roughness set to 15. The chance field is explicitly zeroed out. Hills generation probability is set to 40. Two stripe pattern entries are defined: the first uses cubyz:ferrock/smooth block with direction {1,1,5}, distance 12, offset 6, width 1; the second uses cubyz:sandstone/rough block with identical direction and offset but distance 10 and width 1. The stoneBlock field specifies cubyz:limestone/smooth as the base terrain material. A single parentBiome entry references cubyz:savannah/base with a transition chance of 24.

## Related Questions
- What are the minimum and maximum height values for the Savannah Butte biome?
- Which block is used as the base stone material in this biome configuration?
- How many stripe patterns are defined for the Savannah Butte biome?
- What direction vector is specified for both stripe patterns?
- Is hill generation enabled or disabled by default in this biome config?
- What is the transition chance to the parent Savannah base biome?
- Which block type appears first in the stripes array and what are its distance and offset values?
- How does the second stripe pattern differ from the first one in terms of distance and block material?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_savannah_butte.zig.zon_chunk_0*
