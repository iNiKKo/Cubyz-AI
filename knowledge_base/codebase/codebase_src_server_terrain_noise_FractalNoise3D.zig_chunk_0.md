# [easy/codebase_src_server_terrain_noise_FractalNoise3D.zig] - Chunk 0

**Type:** algorithm
**Keywords:** Array3D, ChunkPosition, voxelShift, worldSeed, scale, random.nextFloat, initSeed3D, alignment assertions, multi-axis averaging, corner seeding
**Symbols:** FractalNoise3D, generateAligned, generateInitializedFractalTerrain
**Concepts:** fractal noise generation, voxel terrain initialization, multi-axis averaging, seeded random offsets, corner seeding, alignment assertions, iterative refinement loops

## Summary
Implements a 3D fractal noise generator for terrain voxelization, producing aligned corner seeds and iteratively refining interior values via multi-axis averaging with per-voxel random offsets.

## Explanation
The chunk defines FractalNoise3D as a struct holding pos (ChunkPosition), cache (Array3D(f32)), voxelShift (u5), scale (u31), and worldSeed (u64). It exposes generateAligned, which asserts alignment of wx/wy/wz to the given scale, asserts that width/height/depth are of the form n*scale + 1 with n > 0, initializes an Array3D(f32) map, then generates corner values by iterating over x/y/z steps of scaledScale = scale/voxelSize and seeding each corner with random.initSeed3D(worldSeed, offset coordinates). Each corner is set to (random.nextFloat(&seed) - 0.5) * @as(f32, @floatFromInt(scale)). After corners are filled, generateInitializedFractalTerrain is called. That function takes the same worldSeed and a bigMap, computes randomnessScale = @floatFromInt(res*maxResolution), then repeatedly halves res starting from startingScale/2 until zero. For each res it processes six passes: x-axis averaging (z offset only), y-axis averaging (x offset only), z-axis averaging (y offset only), all three axes averaged together (divide by 4), two-axes averaged together, and finally the full interior average of six neighbors (divide by 6). Each pass uses nested loops stepping by 2*res over the appropriate dimensions, initializes seed via random.initSeed3D(worldSeed, offset coordinates scaled by maxResolution plus base wx/wy/wz), reads neighbor values with bigMap.get, writes the averaged value plus randomnessScale*(random.nextFloat(&seed) - 0.5). The chunk does not declare any additional public functions or constants beyond generateAligned and generateInitializedFractalTerrain; all other identifiers are local variables inside those functions.

## Related Questions
- How does generateAligned ensure that the input coordinates wx, wy, wz are aligned to the given scale?
- What is the purpose of the randomnessScale computed as @floatFromInt(res*maxResolution) inside generateInitializedFractalTerrain?
- In which order are the six averaging passes executed for each resolution level in generateInitializedFractalTerrain?
- How does the chunk handle interior voxels that have fewer than six neighbors near map boundaries?
- What is the exact formula used to combine neighbor values when all three axes are averaged together (divide by 4)?
- Where is the worldSeed propagated through the nested loops in generateInitializedFractalTerrain?
- How does the chunk use random.nextFloat(&seed) - 0.5 to inject noise after averaging neighbors?
- What assertions are performed on width, height, depth before initializing the map in generateAligned?
- Can a caller reuse the same FractalNoise3D instance for multiple terrain chunks without re-seeding?
- How does the chunk translate local coordinates (x, y, z) into global world coordinates when calling random.initSeed3D?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise3D.zig_chunk_0*
