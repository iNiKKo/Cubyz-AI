# [easy/codebase_src_server_terrain_noise_FractalNoise1D.zig] - Chunk 0

**Type:** algorithm
**Keywords:** seed, offsetX, worldSeed, scale, bigMap, stackAllocator, randomFloat, clamp, memcpy, fractalTerrain
**Symbols:** setSeed, generateFractalTerrain, generateInitializedFractalTerrain, generateSparseFractalTerrain
**Concepts:** fractal noise generation, midpoint displacement algorithm, coordinate-dependent seeding, stack allocator usage, random float generation, value clamping, slice copying with memcpy

## Summary
This chunk defines the core fractal noise generation logic for terrain heightmaps using a recursive midpoint displacement algorithm with coordinate-dependent seeding and clamping.

## Explanation
The chunk declares main as an import from another file, then defines setSeed which initializes a per-coordinate seed by combining worldSeed with offsetX and x via main.random.initSeed2D. generateFractalTerrain allocates a bigMap of size scale+1 on the stack allocator, computes offset = wx & ~mask (where mask = scale-1), seeds the four corners (0, scale) using setSeed, fills those two points with random floats from main.random.nextFloat, then delegates to generateInitializedFractalTerrain. generateInitializedFractalTerrain iterates over scales starting at startingScale/2 down to 1; for each scale it computes randomnessScale = res/scale/2 as a float, then walks the bigMap stride 2*res, seeding each point and computing its value as the average of its two neighbors plus a signed random perturbation scaled by randomnessScale, finally clamping the result between lowerLimit and upperLimit using @min/@max. After generation it copies the relevant slice from bigMap into map[x0..][0..width] via @memcpy. generateSparseFractalTerrain iterates over the map in steps of scale, calling generateFractalTerrain with an offset x0 to produce a sparse terrain.

## Code Example
```zig
pub fn generateFractalTerrain(wx: i32, x0: u31, width: u32, scale: u31, worldSeed: u64, map: []f32) void {
	const max = scale + 1;
	const mask: i32 = scale - 1;
	const bigMap = main.stackAllocator.alloc(f32, max);
	defer main.stackAllocator.free(bigMap);
	const offset = wx & ~mask;
	var seed: u64 = undefined;
	// Generate the 4 corner points of this map using a coordinate-depending seed:
	setSeed(0, offset, &seed, worldSeed, scale);
	bigMap[0] = main.random.nextFloat(&seed);
	setSeed(scale, offset, &seed, worldSeed, scale);
	bigMap[scale] = main.random.nextFloat(&seed);
	generateInitializedFractalTerrain(offset, scale, scale, worldSeed, bigMap, 0, 0.9999);
	@memcpy(map[x0..][0..width], bigMap[@intCast((wx & mask))..][0..width]);
}
```

## Related Questions
- How does setSeed combine worldSeed and offsetX to produce a per-coordinate seed?
- What is the purpose of the mask = scale - 1 in generateFractalTerrain?
- Why are only the four corner points seeded before calling generateInitializedFractalTerrain?
- How is randomnessScale computed inside generateInitializedFractalTerrain and why divide by two?
- What does the stride 2*res loop accomplish in the midpoint displacement algorithm?
- How are lowerLimit and upperLimit applied to each generated height value?
- Why is @memcpy used with an intCast on wx & mask when copying into map?
- Does generateSparseFractalTerrain call generateFractalTerrain for every scale step or only once per sparse block?
- What happens if the allocated bigMap size (scale + 1) does not match the required indices?
- How does defer main.stackAllocator.free ensure cleanup of bigMap after generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise1D.zig_chunk_0*
