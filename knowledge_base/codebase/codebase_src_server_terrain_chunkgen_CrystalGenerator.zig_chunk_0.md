# [medium/codebase_src_server_terrain_chunkgen_CrystalGenerator.zig] - Chunk 0

**Type:** world_generation
**Keywords:** randomization, voxel placement, crystal formation, 3D coordinate system, block mapping
**Symbols:** id, priority, generatorSeed, defaultState, crystalColor, glowCrystals, surfaceDist, init, generate, distSqr, considerCrystal
**Concepts:** world generation, cave structure, glow crystals

## Summary
The CrystalGenerator module is responsible for generating glow crystals within cave structures in the Cubyz voxel engine.

## Explanation
This chunk defines a CrystalGenerator that generates glow crystals inside caves. It initializes by mapping crystal colors to their corresponding block IDs. The `generate` function iterates over nearby chunks, considering each coordinate to place crystals based on random parameters and proximity to cave walls. The `considerCrystal` function handles the detailed placement of individual crystals, including their size, shape, and orientation.

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
