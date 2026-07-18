# [medium/codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig] - Chunk 1

**Type:** world_generation
**Keywords:** random generation, voxel manipulation, chunk update, tree structure, leaf placement
**Symbols:** generate, height0, deltaHeight, leafRadius, deltaLeafRadius, leafElongation, deltaLeafElongation, leavesBlock, typ, pyramid, round, generateStem
**Concepts:** world_generation, terrain generation, tree model

## Summary
Generates a simple tree model in a server chunk based on given parameters and random factors.

## Explanation
The `generate` function is responsible for creating a simple tree model within a server chunk. It calculates the height, leaf radius, and elongation of the tree using random factors. The function checks if there is enough space for the tree to grow based on the cave map. If the conditions are met, it updates the blocks in the chunk to form the stem and leaves according to the specified tree type (pyramid or round). The `generateStem` method is called to create the trunk of the tree. For pyramid-shaped trees, it fills a conical area with leaf blocks. For round-shaped trees, it calculates a spherical area based on the leaf radius and elongation, updating blocks within this area to form the leaves.

## Code Example
```zig
pub fn generate(self: *SimpleTreeModel, _: GenerationMode, x: i32, y: i32, z: i32, chunk: *main.chunk.ServerChunk, caveMap: CaveMapView, _: CaveBiomeMapView, seed: *u64, _: bool) void {
	const factor = random.nextFloat(seed);
	var height = self.height0 + @as(i32, @trunc(factor*@as(f32, @floatFromInt(self.deltaHeight))));
	const leafRadius = self.leafRadius + factor*self.deltaLeafRadius;
	const leafElongation: f32 = self.leafElongation + random.nextFloatSigned(seed)*self.deltaLeafElongation;

	if (z + height >= caveMap.findTerrainChangeAbove(x, y, z)) return; // Space is too small.Allocator

	if (z > chunk.super.width) return;

	if (chunk.super.pos.voxelSize >= 16) {
		// Ensures that even at lowest resolution some leaves are rendered for smaller trees.
		if (chunk.liesInChunk(x, y, z)) {
			chunk.updateBlockIfDegradable(x, y, z, self.leavesBlock);
		}
		if (chunk.liesInChunk(x, y, z + chunk.super.pos.voxelSize)) {
			chunk.updateBlockIfDegradable(x, y, z + chunk.super.pos.voxelSize, self.leavesBlock);
		}
	}

	switch (self.typ) {
		.pyramid => {
			self.generateStem(x, y, z, height, chunk, seed);
			// Position of the first block of leaves
			height = 3*height >> 1;
			var pz = chunk.startIndex(z + @divTrunc(height, 3));
			while (pz < z + height) : (pz += chunk.super.pos.voxelSize) {
				const j = @divFloor(height - (pz - z), 2);
				var px = chunk.startIndex(x + 1 - j);
				while (px < x + j) : (px += chunk.super.pos.voxelSize) {
					var py = chunk.startIndex(y + 1 - j);
					while (py < y + j) : (py += chunk.super.pos.voxelSize) {
						if (chunk.liesInChunk(px, py, pz)) {
							chunk.updateBlockIfDegradable(px, py, pz, self.leavesBlock);
						}
					}
				}
			}
		},
		.round => {
			self.generateStem(x, y, z, height, chunk, seed);

			const ceilZRadius: i32 = @ceil(leafRadius*leafElongation);
			const ceilRadius: i32 = @ceil(leafRadius);
			const radiusSqr: f32 = leafRadius*leafRadius;
			const randomRadiusSqr: f32 = (leafRadius - 0.25)*(leafRadius - 0.25);
			const invLeafElongationSqr = 1.0/(leafElongation*leafElongation);
			const center = z + height;
			var pz = chunk.startIndex(center - ceilZRadius);
			while (pz < center + ceilZRadius) : (pz += chunk.super.pos.voxelSize) {
				var px = chunk.startIndex(x - ceilRadius);
				while (px < x + ceilRadius) : (px += chunk.super.pos.voxelSize) {
					var py = chunk.startIndex(y - ceilRadius);
					while (py < y + ceilRadius) : (py += chunk.super.pos.voxelSize) {
						const distSqr = @as(f32, @floatFromInt((pz - center)*(pz - center)))*invLeafElongationSqr + @as(f32, @floatFromInt((px - x)*(px - x) + (py - y)*(py - y)));
						if (chunk.liesInChunk(px, py, pz) and distSqr < radiusSqr and (distSqr < randomRadiusSqr or random.nextInt(u1, seed) != 0)) { // TODO: Use another seed to make this more reliable!
							chunk.updateBlockIfDegradable(px, py, pz, self.leavesBlock);
						}
					}
				}
			}
		},
	}
}
```

## Related Questions
- What is the purpose of the `generate` function in this chunk?
- How does the function determine the height and leaf properties of the tree?
- What conditions are checked before generating a tree?
- How are leaves placed for pyramid-shaped trees?
- How are leaves placed for round-shaped trees?
- What is the role of the `generateStem` method in this chunk?
- How does the function ensure that some leaves are rendered even at lower resolutions?
- What is the significance of the `leavesBlock` variable in the tree generation process?
- How does the function handle random factors in generating the tree?
- What is the purpose of the `ceilZRadius` and `ceilRadius` variables in the round-shaped tree generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig_chunk_1*
