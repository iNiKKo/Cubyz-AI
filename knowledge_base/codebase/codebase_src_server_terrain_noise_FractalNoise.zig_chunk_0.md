# [easy/codebase_src_server_terrain_noise_FractalNoise.zig] - Chunk 0

**Type:** implementation
**Keywords:** seed, random, noise, grid, iteration
**Symbols:** Array2D, setSeed, generateFractalTerrain, generateInitializedFractalTerrain, generateSparseFractalTerrain
**Concepts:** fractal noise, terrain generation, randomization

## Summary
Fractal noise generation functions for terrain. These include `generateFractalTerrain` which initializes a big map using coordinate-dependent seeds to generate terrain points, and `generateInitializedFractalTerrain` which iteratively increases grid size by adding new points based on average heights of neighbors with random offsets.

## Explanation
The chunk defines functions for generating fractal noise-based terrain. It includes the following key components:

1. **setSeed Function**
   - Initializes a seed using `main.random.initSeed2D` with parameters derived from world coordinates and scale.
   - Example usage: `seed.* = main.random.initSeed2D(worldSeed * (scale * maxResolution | 1), .{(offsetX + x) % maxResolution, (offsetY + y) % maxResolution});`

2. **generateFractalTerrain Function**
   - Initializes a big map with dimensions `max` by `max`, where `max = scale + 1`.
   - Generates four corner points using the `setSeed` function and sets their values to random floats from `main.random.nextFloat(&seed)`.
   - Iteratively generates additional grid points based on average heights of neighbors with random offsets, ensuring a smooth terrain transition.

3. **generateInitializedFractalTerrain Function**
   - Increases the grid size by a factor of 2×2 in each iteration until `res` becomes zero.
   - Calculates `randomnessScale` as `(res / scale) / 2` to control noise level.
   - For each new point, it calculates an average height from surrounding points and adds a random offset using `main.random.nextFloatSigned(&seed)` scaled by `randomnessScale`.
   - Ensures the generated values are within specified limits (`lowerLimit`, `upperLimit`).

4. **generateSparseFractalTerrain Function**
   - Generates a reduced resolution version of the map by calling `generateFractalTerrain` on smaller sub-grids defined by scaled coordinates and dimensions.
   - Uses `scaledWx = wx / maxResolution`, `scaledWy = wy / maxResolution`, and `scaledScale = scale / maxResolution` to determine grid sizes for each call.

## Code Example
```zig
fn setSeed(x: i32, y: i32, offsetX: i32, offsetY: i32, seed: *u64, worldSeed: u64, scale: u31, maxResolution: u31) void {
	seed.* = main.random.initSeed2D(worldSeed*%(scale*maxResolution | 1), .{(offsetX +% x)*%maxResolution, (offsetY +% y)*%maxResolution});
}
```

## Related Questions
- What is the purpose of the `generateFractalTerrain` function?
- How does the `setSeed` function work in relation to terrain generation?
- What are the parameters and steps involved in generating initialized fractal terrain?
- How does the algorithm for sparse fractal terrain differ from full resolution terrain generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise.zig_chunk_0*
