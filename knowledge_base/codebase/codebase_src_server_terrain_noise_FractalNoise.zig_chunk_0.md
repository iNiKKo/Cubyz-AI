# [easy/codebase_src_server_terrain_noise_FractalNoise.zig] - Chunk 0

**Type:** implementation
**Keywords:** seed-dependent random, noise initialization, terrain scaling, sparse terrain generation, grid-based algorithm
**Symbols:** Array2D, setSeed, generateFractalTerrain, generateInitializedFractalTerrain, generateSparseFractalTerrain
**Concepts:** fractal noise, terrain generation, random number generator

## Summary
Fractal noise generation for terrain in Cubyz

## Explanation
This chunk defines functions to generate fractal noise-based terrain using a seed-dependent random number generator. It includes functions to initialize and scale the generated noise, as well as a function to generate sparse versions of the terrain.

## Code Example
```zig
fn setSeed(x: i32, y: i32, offsetX: i32, offsetY: i32, seed: *u64, worldSeed: u64, scale: u31, maxResolution: u31) void {
	seed.* = main.random.initSeed2D(worldSeed*%(scale*maxResolution | 1), .{(offsetX +% x)*%maxResolution, (offsetY +% y)*%maxResolution});
}
```

## Related Questions
- What is the purpose of the `setSeed` function?
- How does the `generateFractalTerrain` function work?
- What are the parameters of the `generateInitializedFractalTerrain` function?
- What is the difference between `generateFractalTerrain` and `generateSparseFractalTerrain`?
- How is the noise generated in the `generateInitializedFractalTerrain` function?
- What is the purpose of the `randomnessScale` variable in the `generateInitializedFractalTerrain` function?
- How does the `generateSparseFractalTerrain` function generate sparse terrain?
- What are the parameters of the `generateSparseFractalTerrain` function?
- How is the noise generated in the `generateSparseFractalTerrain` function?
- What is the purpose of the `scaledWx` and `scaledWy` variables in the `generateSparseFractalTerrain` function?
- How does the `generateSparseFractalTerrain` function scale the input coordinates to generate sparse terrain?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise.zig_chunk_0*
