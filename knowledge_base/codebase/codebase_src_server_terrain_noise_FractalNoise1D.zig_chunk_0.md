# [easy/codebase_src_server_terrain_noise_FractalNoise1D.zig] - Chunk 0

**Type:** implementation
**Keywords:** seed, randomness, noise, terrain, scale
**Symbols:** setSeed, generateFractalTerrain, generateInitializedFractalTerrain, generateSparseFractalTerrain
**Concepts:** fractal noise, terrain generation

## Summary
1D fractal noise generation for terrain

## Explanation
This chunk defines several key functions for generating 1D fractal noise used in terrain generation. The `setSeed` function initializes a seed based on coordinates and scale using the `main.random.initSeed2D` method. Specifically, it calculates the offset as `wx & ~mask`, where `mask = scale - 1`. The `generateFractalTerrain` function generates a map of fractal terrain by initializing corner points with random values and then interpolating between them. It uses parameters like `wx`, `x0`, `width`, `scale`, and `worldSeed`. Specifically, it calculates the maximum value (`max`) as `scale + 1` and defines a mask (`mask`) as `scale - 1`. The function also generates an intermediate map (`bigMap`) of size `max` using `main.stackAllocator.alloc` and initializes corner points with random values. It then copies data from `bigMap` into the final map using `@memcpy`. The `generateInitializedFractalTerrain` function iteratively refines the generated terrain using a scale factor, ensuring that each point is within specified limits (`lowerLimit` and `upperLimit`). This function uses a coordinate-dependent seed to generate random values for interpolation. The `generateSparseFractalTerrain` function generates sparse fractal terrains by calling `generateFractalTerrain` for specific intervals defined by the `scale` parameter.

## Code Example
```zig
fn setSeed(x: i32, offsetX: i32, seed: *u64, worldSeed: u64, scale: u31) void {
	seed.* = main.random.initSeed2D(worldSeed, .{offsetX +% x, scale});
}
```

## Related Questions
- How does the `setSeed` function initialize a seed based on coordinates and scale?
- What are the exact steps involved in initializing corner points with random values in `generateFractalTerrain`?
- How is the intermediate map (`bigMap`) generated and used in `generateFractalTerrain`?
- What is the purpose of the `main.stackAllocator.alloc` function in this context?
- How does the `generateInitializedFractalTerrain` function iteratively refine the terrain using a scale factor?
- What are the parameters for the `main.random.initSeed2D` function and how do they affect seed initialization?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise1D.zig_chunk_0*
