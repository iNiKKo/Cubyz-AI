# [medium/codebase_src_server_terrain_chunkgen_CrystalGenerator.zig] - Chunk 0

**Type:** world_generation
**Keywords:** randomization, voxel placement, crystal formation, 3D coordinate system, block mapping
**Symbols:** id, priority, generatorSeed, defaultState, crystalColor, glowCrystals, surfaceDist, init, generate, distSqr, considerCrystal
**Concepts:** world generation, cave structure, glow crystals

## Summary
The CrystalGenerator module is responsible for generating glow crystals within cave structures in the Cubyz voxel engine.

## Explanation
The CrystalGenerator module is responsible for generating glow crystals within cave structures in the Cubyz voxel engine. It initializes by mapping crystal colors to their corresponding block IDs using an array `crystalColor` which contains 24 different colors: 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'aqua', 'blue', 'pink', 'magenta', 'violet', 'crimson', 'viridian', 'indigo', 'purple', 'brown', 'white', 'grey', 'dark_grey', and 'black'. The `init` function maps each color to its corresponding block ID. The `generate` function iterates over nearby chunks, considering each coordinate to place crystals based on random parameters and proximity to cave walls using a surface distance of 2 units from the wall. The generator seed is set to `0x9b450ffb0d415317`. The `considerCrystal` function handles the detailed placement of individual crystals, including their size, shape, and orientation by generating crystal spikes in random directions with varying lengths. Each spike has a length between 8 and 32 units, and the number of spikes is determined by adding a base value (4 or 6) to a random value between 0 and the base value. The `considerCrystal` function also ensures that crystals do not float in mid-air by adjusting the size and spacing of the crystal bits.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	_ = parameters;
	// Find all the glow crystal ores:
	inline for (crystalColor[0..], glowCrystals[0..]) |color, *block| {
		const oreID = "cubyz:glow_crystal/" ++ color;
		block.* = main.blocks.getTypeById(oreID);
	}
}
```

## Related Questions
- What is the ID of the CrystalGenerator?
- How many different crystal colors are defined?
- What does the `init` function do?
- How does the `generate` function determine where to place crystals?
- What is the purpose of the `considerCrystal` function?
- How are crystal spikes generated in the `considerCrystal` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_chunkgen_CrystalGenerator.zig_chunk_0*
