# [medium/codebase_src_server_terrain_cavegen_FractalCaveGenerator.zig] - Chunk 0

**Type:** world_generation
**Keywords:** fractal generation, cave generation, voxel terrain, randomness, spherical cavities
**Symbols:** id, priority, generatorSeed, defaultState, init, chunkShift, chunkSize, range, initialBranchLength, splittingChance, splitFactor, zSplitReduction, maxSplitLength, branchChance, minRadius, maxInitialRadius, heightVariance, generate, considerCoordinates, generateSphere_, generateSphere, generateCaveBetween
**Concepts:** chunk meshing, world generation, terrain modification

## Summary
The FractalCaveGenerator module is responsible for generating fractal cave structures within the game world.

## Explanation
This chunk defines a fractal cave generator for the Cubyz voxel engine. It includes constants for configuration such as seed values, dimensions, and probabilities. The `generate` function initializes the generation process by considering nearby chunks and their positions. The `generateSphere_` function creates spherical cavities within the map, either adding or removing terrain based on parameters. The `generateSphere` function wraps this with logic to handle negative radii. The `generateCaveBetween` function begins the process of generating caves between two points, checking if the segment can cross the current chunk.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	_ = parameters;
}
```

## Related Questions
- What is the priority of the fractal cave generator?
- How does the `generate` function determine if a segment can cross the current chunk?
- What role does the `generateSphere_` function play in cave generation?
- How is randomness incorporated into the cave generation process?
- What is the purpose of the `considerCoordinates` function?
- How are spherical cavities created within the map?

*Source: unknown | chunk_id: codebase_src_server_terrain_cavegen_FractalCaveGenerator.zig_chunk_0*
