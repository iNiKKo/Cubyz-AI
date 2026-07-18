# [medium/codebase_src_server_terrain_noise_PerlinNoise.zig] - Chunk 1

**Type:** algorithm
**Keywords:** noise generation, Perlin noise, geometric series, random seed scrambling, grid point calculation
**Symbols:** generateSmoothNoise, Array2D(f32).init, NeverFailingAllocator, random.scrambleSeed, Context, Context.l1, Context.l2, Context.l3, Context.calculateGridPoints, main.stackAllocator, context.freeGridPoints
**Concepts:** Perlin noise generation, smooth noise map

## Summary
Generates a smooth noise map using Perlin noise algorithm.

## Explanation
The `generateSmoothNoise` function creates a smooth noise map with values between 0 and 1. It initializes an `Array2D(f32)` to store the noise values, sets all elements to zero, and scrambles a seed based on the world seed. A `Context` struct is used to manage grid points and resolution settings. The function iterates over scales from `maxScale` down to `minScale`, calculating grid points and adding Perlin noise values to the map. The exact formula for the geometric series factor `fac` is given by: 

```plaintext
var fac = 1 / ((1 - std.math.pow(f32, reductionFactor, @as(f32, @floatFromInt(@ctz(maxScale/minScale) + 1)))) / (1 - reductionFactor));
```

The `calculateGridPoints` method computes grid points for the current scale using the formula: 

```plaintext
const x0 = x & ~context.resolutionMask;
const y0 = y & ~context.resolutionMask;
```

and `freeGridPoints` cleans up after processing each scale. The noise values are accumulated with a geometric series factor that reduces with each scale, calculated as: 

```plaintext
fac *= reductionFactor;
```

## Code Example
```zig
pub fn generateSmoothNoise(allocator: NeverFailingAllocator, x: i32, y: i32, width: u31, height: u31, maxScale: u31, minScale: u31, worldSeed: u64, voxelSize: u31, reductionFactor: f32) Array2D(f32) {
	const map = Array2D(f32).init(allocator, width/voxelSize, height/voxelSize);
	@memset(map.mem, 0);
	var seed = worldSeed;
	random.scrambleSeed(&seed);
	var context = Context{
		.l1 = random.nextInt(u64, &seed),
		.l2 = random.nextInt(u64, &seed),
		.l3 = random.nextInt(u64, &seed),
	};
	var fac = 1/((1 - std.math.pow(f32, reductionFactor, @as(f32, @floatFromInt(@ctz(maxScale/minScale) + 1))))/(1 - reductionFactor)); // geometric series.
	var scale = maxScale;
	while (scale >= minScale) : (scale >>= 1) {
		context.resolution = scale;
		context.resolutionMask = scale - 1;
		const x0 = x & ~context.resolutionMask;
		const y0 = y & ~context.resolutionMask;
		context.calculateGridPoints(main.stackAllocator, x, y, width, height, scale);
		defer context.freeGridPoints(main.stackAllocator);

		var x1 = x;
		while (x1 -% width -% x < 0) : (x1 +%= voxelSize) {
			var y1 = y;
			while (y1 -% y -% height < 0) : (y1 +%= voxelSize) {
				map.ptr(@as(u32, @intCast(x1 -% x))/voxelSize, @as(u32, @intCast(y1 -% y))/voxelSize).* += @abs(context.perlin(x1 -% x0, y1 -% y0))*fac;
			}
		}
		fac *= reductionFactor;
	}
	return map;
}
```

## Related Questions
- What is the purpose of the `generateSmoothNoise` function?
- How does the function initialize the noise map?
- What role does the `Context` struct play in the noise generation process?
- How are grid points calculated and managed during noise generation?
- What is the significance of the geometric series factor in the noise accumulation process?
- How does the function handle different scales in generating the noise map?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_PerlinNoise.zig_chunk_1*
