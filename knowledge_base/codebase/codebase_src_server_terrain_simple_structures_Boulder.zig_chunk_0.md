# [easy/codebase_src_server_terrain_simple_structures_Boulder.zig] - Chunk 0

**Type:** implementation
**Keywords:** boulder generation, point cloud, potential function, voxel placement, chunk update
**Symbols:** id, generationMode, Boulder, loadModel, generate
**Concepts:** block generation, point cloud, potential function

## Summary
Boulder generation logic

## Explanation
This chunk defines the Boulder structure with a block, size, and size variation. The `loadModel` function parses parameters for these attributes: 'block' defaults to 'cubyz:slate/smooth', 'size' defaults to 4, and 'sizeVariation' defaults to 1 if not specified in parameters. The `generate` function places blocks based on a point cloud potential function using the parsed values. It calculates radius as `self.size + self.sizeVariation * (random.nextFloat(seed) * 2 - 1)` and uses this radius to determine block placement within a square area of side length 2*radius.

## Code Example
```zig
pub fn generate(self: *Boulder, _: GenerationMode, x: i32, y: i32, z: i32, chunk: *main.chunk.ServerChunk, caveMap: CaveMapView, _: CaveBiomeMapView, seed: *u64, _: bool) void {
	_ = caveMap;
	const radius = self.size + self.sizeVariation*(random.nextFloat(seed)*2 - 1);
	// My basic idea is to use a point cloud and a potential function to achieve somewhat smooth boulders without being a sphere.
	const numberOfPoints = 4;
	var pointCloud: [numberOfPoints]Vec3f = undefined;
	for (&pointCloud) |*point| {
		point.* = Vec3f{
			(random.nextFloat(seed) - 0.5)*radius/2,
			(random.nextFloat(seed) - 0.5)*radius/2,
			(random.nextFloat(seed) - 0.5)*radius/2,
		};
	}
	// My potential functions is ¹⁄ₙ Σ (radius/2)²/(x⃗ - x⃗ₚₒᵢₙₜ)²
	// This ensures that the entire boulder is inside of a square with sidelength 2*radius.
	const maxRadius: i32 = @ceil(radius);
	var px = chunk.startIndex(x - maxRadius);
	while (px < x + maxRadius) : (px += chunk.super.pos.voxelSize) {
		var py = chunk.startIndex(y - maxRadius);
		while (py < y + maxRadius) : (py += chunk.super.pos.voxelSize) {
			var pz = chunk.startIndex(z - maxRadius);
			while (pz < z + maxRadius) : (pz += chunk.super.pos.voxelSize) {
				if (!chunk.liesInChunk(px, py, pz)) continue;
				var potential: f32 = 0;
				for (&pointCloud) |point| {
					const delta = @as(Vec3f, @floatFromInt(Vec3i{px, py, pz} - Vec3i{x, y, z})) - point;
					const distSqr = vec.dot(delta, delta);
					potential += 1/distSqr;
				}
				potential *= radius*radius/4/numberOfPoints;
				if (potential >= 1) {
					chunk.updateBlockInGeneration(px, py, pz, self.block);
				}
			}
		}
	}
}
```

## Related Questions
- What are the default values for 'size' and 'sizeVariation' in the Boulder structure?
- How is the default block ('cubyz:slate/smooth') set if no parameter is provided?
- What is the formula used to calculate radius during generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_Boulder.zig_chunk_0*
