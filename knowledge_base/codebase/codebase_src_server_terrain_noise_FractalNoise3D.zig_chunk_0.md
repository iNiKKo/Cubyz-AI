# [easy/codebase_src_server_terrain_noise_FractalNoise3D.zig] - Chunk 0

**Type:** world_generation
**Keywords:** fractal noise, terrain generation, random number generation, array manipulation, 3D space
**Symbols:** FractalNoise3D, FractalNoise3D.pos, FractalNoise3D.cache, FractalNoise3D.voxelShift, FractalNoise3D.scale, FractalNoise3D.worldSeed, FractalNoise3D.generateAligned, FractalNoise3D.generateInitializedFractalTerrain
**Concepts:** chunk meshing, world generation

## Summary
This chunk implements the generation of fractal noise for 3D terrain.

## Explanation
This chunk implements the generation of fractal noise for 3D terrain. The `FractalNoise3D` struct contains methods to generate aligned and initialized fractal terrain. The `generateAligned` function initializes an array and generates random values at specific intervals, while `generateInitializedFractalTerrain` refines the noise by averaging neighboring points and adding randomness.

The `generateAligned` function performs several assertion checks:
- Alignment: `wx & scale - 1 == 0`, `wy & scale - 1 == 0`, `wz & scale - 1 == 0`
- Dimensions need to be of the form n*scale + 1 with n ∈ ℕ \∗ {0}: `width - 1 & scale/voxelSize - 1 == 0`, `height - 1 & scale/voxelSize - 1 == 0`, `depth - 1 & scale/voxelSize - 1 == 0`
- Dimensions must be greater than 1: `width > 1`, `height > 1`, `depth > 1`
The function initializes an array and generates random values at specific intervals, refining the noise by averaging neighboring points and adding randomness. The parameters required for generating fractal noise include:
- `allocator`: Memory allocator
- `wx`, `wy`, `wz`: World coordinates
- `voxelSize`: Size of each voxel
- `width`, `depth`, `height`: Dimensions of the terrain
- `worldSeed`: Seed value for random number generation
- `scale`: Scale factor for noise generation

## Code Example
```zig
pub fn generateAligned(allocator: NeverFailingAllocator, wx: i32, wy: i32, wz: i32, voxelSize: u31, width: u31, depth: u31, height: u31, worldSeed: u64, scale: u31) Array3D(f32) {
	std.debug.assert(wx & scale - 1 == 0 and wy & scale - 1 == 0 and wz & scale - 1 == 0); // Alignment;
	std.debug.assert(width - 1 & scale/voxelSize - 1 == 0 and height - 1 & scale/voxelSize - 1 == 0 and depth - 1 & scale/voxelSize - 1 == 0); // dimensions need to be of the form n*scale + 1 with n ∈ ℕ \ {0}
	std.debug.assert(width > 1 and height > 1 and depth > 1); // dimensions need to be of the form n*scale + 1 with n ∈ ℕ \ {0}
	const map = Array3D(f32).init(allocator, width, depth, height);

	// Generate the corners:
	const scaledScale = scale/voxelSize;
	var x0: u31 = 0;
	while (x0 < width) : (x0 += scaledScale) {
		var y0: u31 = 0;
		while (y0 < depth) : (y0 += scaledScale) {
			var z0: u31 = 0;
			while (z0 < height) : (z0 += scaledScale) {
				var seed = random.initSeed3D(worldSeed, .{wx +% x0*voxelSize, wy +% y0*voxelSize, wz +% z0*voxelSize});
				map.ptr(x0, y0, z0).* = (random.nextFloat(&seed) - 0.5)*@as(f32, @floatFromInt(scale));
			}
		}
	}

	generateInitializedFractalTerrain(wx, wy, wz, scaledScale, worldSeed, map, voxelSize);

	return map;
}
```

## Related Questions
- - What is the purpose of the `generateAligned` function?
- - How does the `generateInitializedFractalTerrain` function work?
- - What data structure is used to store the noise values?
- - What are the parameters required for generating fractal noise?
- - How is randomness incorporated into the noise generation process?
- - What assertion checks are performed in the `generateAligned` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_FractalNoise3D.zig_chunk_0*
