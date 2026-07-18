# [easy/codebase_src_server_terrain_noise_CachedFractalNoise.zig] - Chunk 0

**Type:** implementation
**Keywords:** noise map, terrain generation, fractal noise, caching, recursive generation, memory management
**Symbols:** CachedFractalNoise, CachedFractalNoise.pos, CachedFractalNoise.cache, CachedFractalNoise.scale, CachedFractalNoise.worldSeed, CachedFractalNoise.init, CachedFractalNoise.deinit, CachedFractalNoise.getRandomValue, CachedFractalNoise.getGridValue, CachedFractalNoise.generateRegion, CachedFractalNoise._getValue, CachedFractalNoise.getValue
**Concepts:** terrain generation, fractal noise, caching

## Summary
The CachedFractalNoise struct manages a cached noise map for terrain generation, providing methods to initialize, deinitialize, and retrieve noise values.

## Explanation
The CachedFractalNoise struct is designed to efficiently generate and cache fractal noise values for use in terrain generation. It includes methods for initialization (`init`), cleanup (`deinit`), and retrieving noise values (`getValue`). The `init` method sets up the cache and initializes corner values, while `deinit` frees allocated resources. The `getValue` method calculates the noise value at a given world position by converting it to relative coordinates within the cached region and calling `_getValue`, which checks if the value is already cached or needs to be generated using `generateRegion`. The `generateRegion` method recursively generates noise values for a specified region, ensuring that all higher points are generated before calculating intermediate values.

## Code Example
```zig
pub fn deinit(self: CachedFractalNoise) void {
	self.cache.deinit(main.globalAllocator);
}
```

## Related Questions
- How does the `init` method initialize the cache?
- What is the purpose of the `_getValue` method in the CachedFractalNoise struct?
- How does the `generateRegion` method ensure that all higher points are generated before calculating intermediate values?
- What role does the `scale` field play in the CachedFractalNoise struct?
- How does the `deinit` method handle memory cleanup?
- What is the function of the `getRandomValue` method in generating noise values?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_CachedFractalNoise.zig_chunk_0*
