# [easy/codebase_src_server_terrain_chunkgen_OreGenerator.zig] - Chunk 0

**Type:** implementation
**Keywords:** random number generation, block placement, terrain generation, vein distribution, density calculation
**Symbols:** id, priority, generatorSeed, defaultState, ores
**Concepts:** cave generation, ore vein generation, chunk generation

## Summary
Ore generation logic for Cubyz terrain chunks

## Explanation
This chunk defines the `generate` function, which generates ore veins in server chunks based on cave maps and biome maps. It considers nearby chunks and randomly places ore veins within them.

## Code Example
```zig
fn considerCoordinates(ore: *const main.blocks.Ore, relX: f32, relY: f32, relZ: f32, chunk: *main.chunk.ServerChunk, startSeed: u64) void {
	const chunkSizeFloat: f32 = @floatFromInt(main.chunk.chunkSize);
	// Compose the seeds from some random stats of the ore. They generally shouldn't be the same for two different ores. TODO: Give each block a hash function (id based) that can be used in cases like this.
	var seed = startSeed ^ ore.seed;
	// Determine how many veins of this type start in this chunk. The number depends on parameters set for the specific ore:
	const veins: u32 = @trunc(random.nextFloat(&seed)*ore.veins*2);
	for (0..veins) |_| {
		// Choose some in world coordinates to start generating:
		const veinRelX = relX + random.nextFloat(&seed)*chunkSizeFloat;
		const veinRelY = relY + random.nextFloat(&seed)*chunkSizeFloat;
		const veinRelZ = relZ + random.nextFloat(&seed)*chunkSizeFloat;
		// Choose a random volume and create a radius from that:
		const size = (random.nextFloat(&seed) + 0.5)*ore.size;
		const expectedVolume = 2*size/ore.density; // Double the volume, because later the density is actually halfed.
		const radius = std.math.cbrt(expectedVolume*3/4/std.math.pi);
		var xMin: i32 = @floor(veinRelX - radius);
		var xMax: i32 = @ceil(veinRelX + radius);
		var yMin: i32 = @floor(veinRelY - radius);
		var yMax: i32 = @ceil(veinRelY + radius);
		xMin = @max(xMin, 0);
		xMax = @min(xMax, chunk.super.width);
		yMin = @max(yMin, 0);
		yMax = @min(yMax, chunk.super.width);

		var veinSeed = random.nextInt(u64, &seed);
		var curX = xMin;
		while (curX < xMax) : (curX += 1) {
			const distToCenterX = (@as(f32, @floatFromInt(curX)) - veinRelX)/radius;
			var curY = yMin;
			while (curY < yMax) : (curY += 1) {
				const distToCenterY = (@as(f32, @floatFromInt(curY)) - veinRelY)/radius;
				const xyDistSqr = distToCenterX*distToCenterX + distToCenterY*distToCenterY;
				if (xyDistSqr > 1) continue;
				const zDistance = radius*@sqrt(1 - xyDistSqr);
				var zMin: i32 = @floor(veinRelZ - zDistance);
				var zMax: i32 = @ceil(veinRelZ + zDistance);
				zMin = @max(zMin, 0);
				zMax = @min(zMax, chunk.super.width);
				var curZ = zMin;
				while (curZ < zMax) : (curZ += 1) {
					const distToCenterZ = (@as(f32, @floatFromInt(curZ)) - veinRelZ)/radius;
					const distSqr = xyDistSqr + distToCenterZ*distToCenterZ;
					if (distSqr < 1) {
						// Add some roughness. The ore density gets smaller at the edges:
						if ((1 - distSqr)*ore.density >= random.nextFloat(&veinSeed)) {
							const stoneBlock = chunk.getBlock(curX, curY, curZ);
							if (chunk.getBlock(curX, curY, curZ).allowOres()) {
								chunk.updateBlockInGeneration(curX, curY, curZ, .{.typ = ore.blockType, .data = stoneBlock.typ});
							}
						}
					}
				}
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `considerCoordinates` function?
- How many veins are generated for each ore type in a chunk?
- What is the formula used to calculate the radius of an ore vein?
- Where does the seed for generating ore veins come from?
- What is the density calculation used to determine if an ore block should be placed?
- How are ore blocks placed in chunks?
- What is the maximum height limit for ore veins in a chunk?
- What is the minimum height limit for ore veins in a chunk?
- How many nearby chunks are considered when generating ore veins?
- What is the formula used to calculate the volume of an ore vein?
- What is the formula used to calculate the expected volume of an ore vein?
- What is the formula used to calculate the radius from which an ore vein starts?

*Source: unknown | chunk_id: codebase_src_server_terrain_chunkgen_OreGenerator.zig_chunk_0*
