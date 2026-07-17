# [easy/codebase_assets_cubyz_biomes_rare_phantasmal_archipelago.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** fog density, fog color, properties enum, chance probability, min height, max height limit, music reference, hills parameter, roughness value, stone block identifier, ground structure, structure placement mode, transition biome, biome properties, degradable structures
**Symbols:** fogDensity, fogColor, properties, chance, minHeight, maxHeight, maxHeightLimit, music, hills, roughness, stoneBlock, ground_structure, structures, transitionBiomes
**Concepts:** biome configuration, structure placement, fog rendering, ocean biome, height constraints, music reference

## Summary
Defines the Phantasmal Archipelago biome configuration with fog settings, ocean properties, height constraints, music reference, hills/roughness parameters, stone block, ground structure (obsidian), and a collection of structures including pillars, mushroom variants, bubbles, plus transition biomes to warm beaches and temperate shelves.

## Explanation
This chunk is a .zon configuration file containing static biome data. It declares fogDensity=3 and fogColor=0x000C14. The properties field is set to the enum value .ocean. Chance is 0.01, minHeight=-128, maxHeight=-64, maxHeightLimit=-48. Music is referenced as "cubyz:totaldemented/tides". Hills=35 and roughness=55 are numeric parameters. StoneBlock points to the block identifier "cubyz:chalk/black". GroundStructure contains a single entry for heights 0-2 using block "cubyz:obsidian". Structures is an array of four entries: (1) id="cubyz:sbb", structure="cubyz:phantasmal/phantasmal_pillars", placeMode=.degradable, chance=0.05; (2) id="cubyz:flower_patch", blocks=["cubyz:glimmergill"], chance=0.04, width=12, variation=6, density=0.08, priority=0.15; (3) id="cubyz:sbb", structure="cubyz:mushroom/small/glimmergill", placeMode=.degradable, chance=0.035; (4) id="cubyz:sbb", structure="cubyz:mushroom/big/glimmergill", placeMode=.degradable, chance=0.03; and (5) id="cubyz:sbb", structure="cubyz:phantasmal/bubble/bubble", chance=0.05, rotation=0. TransitionBiomes lists three entries: beach/warm/wide with chance=0.2, width=2, properties=[.land,.inland]; beach/warm/base with chance=1, width=1, properties=[.land,.inland]; ocean/temperate/shelf with chance=1, width=3, properties=[.land,.inland].

## Related Questions
- What fog density and color are configured for the Phantasmal Archipelago biome?
- Which music track is assigned to this biome configuration?
- What height range (minHeight, maxHeight) defines the vertical bounds of this biome?
- How many hills and what roughness value are set for terrain generation?
- Which stone block identifier is used as the primary ground material?
- What blocks comprise the ground_structure entry for heights 0-2?
- List all structures defined in the structures array with their IDs.
- What placeMode is assigned to each structure entry (e.g., .degradable)?
- How many transition biomes are listed and what are their IDs?
- What properties (land, inland) are attached to each transition biome entry?
- Are any of the transition biomes guaranteed to appear (chance=1)?
- Does this configuration include any flower_patch or bubble structures?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_rare_phantasmal_archipelago.zig.zon_chunk_0*
