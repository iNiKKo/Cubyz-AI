# [easy/codebase_src_server_terrain_simple_structures_Boulder.zig] - Chunk 0

**Type:** implementation
**Keywords:** GenerationMode, ServerChunk, updateBlockInGeneration, liesInChunk, startIndex, point cloud, potential function, random.nextFloat, worldArena.create
**Symbols:** id, generationMode, Boulder, loadModel, generate
**Concepts:** simple structure generation, point cloud potential function, chunk coordinate mapping, random seeded noise, block placement filtering

## Summary
Defines the Boulder simple structure model with floor generation mode and implements a point-cloud potential function to generate smooth boulder geometry within a chunk.

## Explanation
The chunk declares a public Boulder struct containing block, size, and sizeVariation fields. It provides loadModel which parses ZonElement parameters (block name defaults to cubyz:slate/smooth, size defaults to 4, size_variation defaults to 1) and allocates the Boulder via main.worldArena.create. The generate method takes a GenerationMode (unused), world coordinates x/y/z, a ServerChunk pointer, cave maps (ignored), a seed for random number generation, and an unused boolean flag. It computes radius as base size plus a variation term scaled by random.nextFloat(seed)*2-1. A point cloud of 4 points is initialized with offsets derived from the same seed. The method then iterates over a bounding box around the target position using chunk.startIndex to map world coordinates to chunk voxel indices, skipping positions outside the chunk via liesInChunk. For each candidate voxel it accumulates a potential value as sum(1/distSqr) over all point cloud points, scaled by radius^2/4/numberOfPoints. If potential >= 1 the block is placed via chunk.updateBlockInGeneration.

## Code Example
```zig
pub fn loadModel(parameters: ZonElement) ?*Boulder {
	const self = main.worldArena.create(Boulder);
	self.* = .{
		.block = main.blocks.parseBlock(parameters.get([]const u8, "block") orelse "cubyz:slate/smooth"),
		.size = parameters.get(f32, "size") orelse 4,
		.sizeVariation = parameters.get(f32, "size_variation") orelse 1,
	};
	return self;
}
```

## Related Questions
- What default block is used when the ZonElement parameter 'block' is missing?
- How does generate compute the radius for a Boulder instance?
- Why are CaveMapView and CaveBiomeMapView parameters ignored in generate?
- What condition determines whether a voxel gets placed during generation?
- How many points are used in the point cloud for the potential function?
- Which method is responsible for allocating a new Boulder struct on the world arena?
- Does generate accept any GenerationMode value or only floor mode?
- What role does seed play in random.nextFloat calls within generate?
- How does startIndex translate world coordinates to chunk voxel indices?
- Is liesInChunk used before or after computing potential for a voxel?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_Boulder.zig_chunk_0*
