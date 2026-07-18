# [easy/codebase_src_server_terrain_noise_FractalNoise1D.zig] - Chunk 0

**Type:** implementation
**Keywords:** seed, randomness, noise, terrain, scale
**Symbols:** setSeed, generateFractalTerrain, generateInitializedFractalTerrain, generateSparseFractalTerrain
**Concepts:** fractal noise, terrain generation

## Summary
1D fractal noise generation for terrain

## Explanation
This chunk defines functions to generate 1D fractal noise for terrain. It includes functions to set a seed, generate initialized and sparse fractal terrains, and copy the generated data into a map.

## Code Example
```zig
fn setSeed(x: i32, offsetX: i32, seed: *u64, worldSeed: u64, scale: u31) void {
	seed.* = main.random.initSeed2D(worldSeed, .{offsetX +% x, scale});
}
```

## Related Questions
- What is the purpose of the `setSeed` function?
- How does the `generateFractalTerrain` function work?
- What are the parameters for the `generateInitializedFractalTerrain` function?
- What is the difference between initialized and sparse fractal terrains?
- How is the generated data copied into a map?
- What is the purpose of the `generateSparseFractalTerrain` function?
- How does the `generateInitializedFractalTerrain` function handle randomness?
- What are the parameters for the `main.random.initSeed2D` function?
- What is the purpose of the `@memcpy` function in this chunk?
- What is the difference between a 1D and 2D fractal noise generator?
- How does the `generateInitializedFractalTerrain` function use the `res` variable?
- What is the purpose of the `main.stackAllocator.alloc` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise1D.zig_chunk_0*
