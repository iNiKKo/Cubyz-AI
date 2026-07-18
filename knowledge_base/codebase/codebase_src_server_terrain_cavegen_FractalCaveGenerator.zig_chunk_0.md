# [medium/codebase_src_server_terrain_cavegen_FractalCaveGenerator.zig] - Chunk 0

**Type:** world_generation
**Keywords:** fractal generation, spherical carving, random seed, voxel terrain, chunk processing
**Symbols:** id, priority, generatorSeed, defaultState, init, chunkShift, chunkSize, range, initialBranchLength, splittingChance, splitFactor, zSplitReduction, maxSplitLength, branchChance, minRadius, maxInitialRadius, heightVariance, generate, considerCoordinates, generateSphere_, generateSphere
**Concepts:** chunk meshing, world generation, cave generation

## Summary
This chunk implements the Fractal Cave Generator for generating cave structures in a voxel world.

## Explanation
The FractalCaveGenerator module is responsible for creating cave-like structures within the game world using a fractal-based approach. It initializes with specific parameters such as chunk size, range, and probabilities for branching and splitting. The `priority` of this generator is set to 131072, and its default state is enabled. The `chunkShift` value determines the chunk size (1 << chunkShift), which results in a chunkSize of 32 voxels. The range for neighboring chunks is 8 * chunkSize, making it 256 voxels. The generator uses an initial branch length of 64 and has a splitting chance of 0.4 with a split factor of 1.0. Additionally, the z-split reduction is set to 0.5 to reduce splitting in the z-direction, and the maximum split length is 128. The minimum radius for carving is 2.0, while the maximum initial radius is 5. Height variance is set at 0.15. The `generate` function iterates over neighboring chunks within a specified range, calculates seeds based on their positions, and calls `considerCoordinates` to evaluate and carve out cave structures. The `generateSphere_` function handles the actual carving of spherical cavities by either adding or removing terrain based on the radius. The `generateSphere` function manages the sign of the radius to determine whether to add or remove terrain.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	_ = parameters;
}
```

## Related Questions
- What is the priority of the Fractal Cave Generator?
- How does the generator determine the range for neighboring chunks?
- What are the specific parameters used in fractal cave generation, such as chunk size and splitting chance?
- What function is responsible for carving out spherical cavities?
- How does the generator handle the sign of the radius in `generateSphere`?

*Source: unknown | chunk_id: codebase_src_server_terrain_cavegen_FractalCaveGenerator.zig_chunk_0*
