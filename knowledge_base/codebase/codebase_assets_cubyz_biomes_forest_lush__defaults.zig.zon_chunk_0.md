# [easy/codebase_assets_cubyz_biomes_forest_lush__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** wet, oak, pine, height limits, smooth beaches, radius bounds, roughness, hills, music reference, player spawn, fallen tree, flower patch
**Symbols:** .properties, .tags, .minHeightLimit, .minHeight, .maxHeight, .maxHeightLimit, .smoothBeaches, .minRadius, .maxRadius, .roughness, .hills, .music, .validPlayerSpawn, .structures
**Concepts:** biome configuration, structure generation, forest biome defaults, wet property flag, tree tags, height limits, beach smoothing, radius bounds, roughness parameter, hill count, music reference, player spawn validity

## Summary
Defines default biome configuration for a lush forest with wet properties, tree tags, height limits, beach smoothing, radius bounds, roughness, hill count, music reference, spawn validity, and structure generation rules including fallen trees and flower patches.

## Explanation
This chunk is a static data definition (zon) containing biome configuration parameters. It sets .wet as the only property flag, assigns oak and pine tags, defines minHeightLimit=7, minHeight=20, maxHeight=50, maxHeightLimit=60, smoothBeaches=true, minRadius=256, maxRadius=320, roughness=10, hills=12, music='cubyz:totaldemented/leaves', validPlayerSpawn=true. The .structures array lists four entries: two fallen_tree variants (oak log with chance 0.005 height 6 variation 3; pine log with chance 0.002 height 6 variation 3), and two flower_patch variants (bolete blocks chance 0.02 width 3 density 0.4 priority 0.1; toadstool blocks chance 0.01 width 8 density 0.1 priority 0.1). No executable logic is present; all values are literal constants used by the biome generation system.

## Related Questions
- What property flags are enabled for the lush forest biome defaults?
- Which tags are assigned to trees in this biome configuration?
- What are the minimum and maximum height limits defined for terrain generation?
- Is beach smoothing enabled by default in this biome config?
- What is the roughness value set for surface detail in the forest biome?
- How many hills are configured to generate in this biome's defaults?
- Which music track is referenced for ambient audio in the lush forest biome?
- Is player spawning allowed by default in this biome configuration?
- What structures are defined under .structures and what are their spawn chances?
- Are there multiple variants of fallen_tree structures with different log types?
- How do flower_patch structure definitions differ between bolete and toadstool blocks?
- What width, density, and priority values are assigned to each flower patch variant?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_forest_lush__defaults.zig.zon_chunk_0*
