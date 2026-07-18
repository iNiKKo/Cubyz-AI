# [medium/codebase_src_server_terrain_chunkgen_CrystalGenerator.zig] - Chunk 1

**Type:** implementation
**Keywords:** random number generation, seed scrambling, world coordinates, surface proximity check, crystal placement
**Symbols:** considerCoordinates, seed, crystalSpawns, differendColors, _colors, colors, useNeedles, worldX, worldY, worldZ, relX, relY, relZ
**Concepts:** crystal generation, random seed, cave environment, biome influence

## Summary
Generates crystals within a cave based on biome and random seed.

## Explanation
The function `considerCoordinates` is responsible for generating crystals within a cave. It takes the coordinates of the chunk, a pointer to the server chunk, views of the cave map and biome map, and a pointer to a seed. The function first determines the number of different crystal colors based on random chance with an initial value of 1 and up to a maximum of 32. There is a 75% chance that a cave has only one type of crystal color; if this condition fails, there is an exponentially diminishing chance for each additional color until reaching 32 or the next random check passes. A decision is made whether to use needles for crystal generation based on another random number generator call. Using the old position-specific seed, it randomly selects world coordinates within the chunk size to start generating crystals. Crystals are only placed in solid blocks that are close to the surface (within ±SURFACE_DIST blocks). The `considerCrystal` function is called to generate each crystal at the selected coordinates.

## Code Example
```zig
fn considerCoordinates(x: i32, y: i32, z: i32, chunk: *main.chunk.ServerChunk, caveMap: CaveMap.CaveMapView, biomeMap: CaveBiomeMap.CaveBiomeMapView, seed: *u64) void {
	const oldSeed = seed.*;
	const crystalSpawns = biomeMap.getBiomeAndSeed(x +% main.chunk.chunkSize/2 -% chunk.super.pos.wx, y +% main.chunk.chunkSize/2 -% chunk.super.pos.wy, z +% main.chunk.chunkSize/2 -% chunk.super.pos.wz, true, seed).crystals;
	random.scrambleSeed(seed);
	var differendColors: u32 = 1;
	if (random.nextInt(u1, seed) != 0) {
		// ¹⁄₄ Chance that a cave has multiple crystals.
		while (random.nextInt(u1, seed) != 0 and differendColors < 32) {
			differendColors += 1; // Exponentially diminishing chance to have more differend crystals per cavern.
		}
	}
	var _colors: [32]u16 = undefined;
	const colors = _colors[0..differendColors];
	for (colors) |*color| {
		color.* = glowCrystals[random.nextIntBounded(u16, seed, glowCrystals.len)];
	}
	const useNeedles = random.nextInt(u1, seed) != 0; // Different crystal type.
	// Spawn the crystals using the old position specific seed:
	seed.* = oldSeed;
	for (0..crystalSpawns) |_| {
		// Choose some in world coordinates to start generating:
		const worldX = x + random.nextIntBounded(u31, seed, main.chunk.chunkSize);
		const worldY = y + random.nextIntBounded(u31, seed, main.chunk.chunkSize);
		const worldZ = z + random.nextIntBounded(u31, seed, main.chunk.chunkSize);
		const relX = worldX -% chunk.super.pos.wx;
		const relY = worldY -% chunk.super.pos.wy;
		const relZ = worldZ -% chunk.super.pos.wz;
		if (caveMap.isSolid(relX, relY, relZ)) { // Only start crystal in solid blocks
			// Only start crystal when they are close to the surface (±SURFACE_DIST blocks)
			if ((worldX - x >= surfaceDist and !caveMap.isSolid(relX - surfaceDist, relY, relZ)) or (worldX - x < main.chunk.chunkSize - surfaceDist and !caveMap.isSolid(relX + surfaceDist, relY, relZ)) or (worldY - y >= surfaceDist and !caveMap.isSolid(relX, relY - surfaceDist, relZ)) or (worldY - y < main.chunk.chunkSize - surfaceDist and !caveMap.isSolid(relX, relY + surfaceDist, relZ)) or (worldZ - z >= surfaceDist and !caveMap.isSolid(relX, relY, relZ - surfaceDist)) or (worldZ - z < main.chunk.chunkSize - surfaceDist and !caveMap.isSolid(relX, relY, relZ + surfaceDist))) {
				// Generate the crystal:
				considerCrystal(worldX, worldY, worldZ, chunk, seed, useNeedles, colors);
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `considerCoordinates` function?
- How does the function determine the number of different crystal colors?
- What role does the biome map play in crystal generation?
- How are world coordinates selected for crystal placement?
- What conditions must be met for a crystal to be placed?
- What is the process for generating each crystal after selection?

*Source: unknown | chunk_id: codebase_src_server_terrain_chunkgen_CrystalGenerator.zig_chunk_1*
