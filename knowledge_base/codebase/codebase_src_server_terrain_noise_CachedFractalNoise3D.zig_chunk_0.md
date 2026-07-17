# [easy/codebase_src_server_terrain_noise_CachedFractalNoise3D.zig] - Chunk 0

**Type:** implementation
**Keywords:** cached noise, fractal noise, voxel engine, random value, cache initialization
**Symbols:** CachedFractalNoise3D, init, deinit, getRandomValue, getGridValue, generateRegion, _getValue, getValue
**Concepts:** cached fractal noise generator, voxel engine, noise generation, random value generation

## Summary
Cubyz voxel engine CachedFractalNoise3D implementation

## Explanation
This module provides a cached fractal noise generator for the Cubyz voxel engine. It initializes cache with precomputed values and generates random values based on seed, position, and scale. The `generateRegion` function recursively fills the cache by averaging neighboring values and adding random noise. The `getValue` method maps world coordinates to cached noise values.

## Code Example
```zig
pub fn init(wx: i32, wy: i32, wz: i32, voxelSize: u31, size: u31, worldSeed: u64, scale: u31) CachedFractalNoise3D {
	const maxSize = size/voxelSize;
	const cacheWidth = maxSize + 1;
	var self = CachedFractalNoise3D{
		.pos = .{
			.wx = wx,
			.wy = wy,
			.wz = wz,
			.voxelSize = voxelSize,
		},
		.voxelShift = @ctz(voxelSize),
		.cache = Array3D(f32).init(main.globalAllocator, cacheWidth, cacheWidth, cacheWidth),
		.scale = scale,
		.worldSeed = worldSeed,
	};
	// Init the corners:
	@memset(self.cache.mem, 0);
	const reducedScale = scale/voxelSize;
	var x: u31 = 0;
	while (x <= maxSize) : (x += reducedScale) {
		var y: u31 = 0;
		while (y <= maxSize) : (y += reducedScale) {
			var z: u31 = 0;
			while (z <= maxSize) : (z += reducedScale) {
				self.cache.ptr(x, y, z).* = (@as(f32, @floatFromInt(reducedScale + 1 + scale))*self.getGridValue(x, y, z))*@as(f32, @floatFromInt(voxelSize));
			} //                                                    ↑ sacrifice some resolution to reserve the value 0, for determining if the value was initialized. This prevents an expensive array initialization.
		}
	}
	return self;
}
```

## Related Questions
- What is the purpose of the `CachedFractalNoise3D` struct?
- How does the `init` function initialize the cache and set up the noise generator?
- What is the role of the `generateRegion` function in the noise generation process?
- How is the `_getValue` function used to retrieve cached noise values?
- What is the significance of the `voxelShift` field in the `CachedFractalNoise3D` struct?
- How does the `getValue` method map world coordinates to cached noise values?
- What is the purpose of the `getRandomValue` function?
- How is the `scale` parameter used in the noise generation process?
- What is the role of the `worldSeed` field in the `CachedFractalNoise3D` struct?
- How does the `deinit` function clean up resources allocated by the `CachedFractalNoise3D` struct?
- What is the purpose of the `getGridValue` function?
- How is the cache initialized with precomputed values?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_CachedFractalNoise3D.zig_chunk_0*
