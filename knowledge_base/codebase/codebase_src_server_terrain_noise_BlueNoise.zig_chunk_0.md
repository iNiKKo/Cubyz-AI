# [easy/codebase_src_server_terrain_noise_BlueNoise.zig] - Chunk 0

**Type:** implementation
**Keywords:** noise_map, grid_based, random_movement, subregion_extraction, compression
**Symbols:** random, Array2D, NeverFailingAllocator
**Concepts:** world_generation

## Summary
Loads a pre-seeded noise map for world generation.

## Explanation
The `load` function initializes the `pattern` array with random values to create a simple square grid used for world generation. It uses a basic grid-based approach where each point is moved randomly to ensure the grid remains valid in each step, repeated multiple times for optimal results. The `sample` function retrieves a value from the `pattern` array based on given coordinates. The `getRegionData` function extracts a subregion of the noise map and returns it as an array of 32-bit integers representing the coordinates relative to the compressed input coordinates.

## Code Example
```zig
pub fn load() void { // TODO: Do this at compile time once the caching is good enough.
	@setRuntimeSafety(false); // TODO: Replace with optimizations.
	var seed: u64 = 54095248685739;
	const distSquareLimit = 8;
	const repetitions = 4;
	const iterations = 16;
	// Go through all points and try to move them randomly.
	// Ensures that the grid is valid in each step.
	// This is repeated multiple times for optimal results.
	// In the last repetition is enforced, to remove grid artifacts.
	for (0..repetitions) |_| {
		for (0..pattern.len) |i| {
			const x: i32 = @intCast(i >> sizeShift);
			const y: i32 = @intCast(i & sizeMask);
			outer: for (0..iterations) |_| {
				const point = random.nextInt(u6, &seed);
				const xOffset = point >> 3 & 7;
				const yOffset = point & 7;
				// Go through all neighbors and check validity:
			var dx: i32 = -2;
			while (dx <= 2) : (dx += 1) {
				var dy: i32 = -2;
				while (dy <= 2) : (dy += 1) {
					if (dx == 0 and dy == 0) continue; // Don't compare with itself!
					const neighbor = (x + dx & sizeMask) << sizeShift | (y + dy & sizeMask);
					const neighborPos = pattern[@intCast(neighbor)];
					const nx = (neighborPos >> 3) + (dx << featureShift);
					const ny = (neighborPos & 7) + (dy << featureShift);
					const distSqr = (nx - xOffset)*(nx - xOffset) + (ny - yOffset)*(ny - yOffset);
					if (distSqr < distSquareLimit) continue :outer;
				}
			}

			pattern[i] = point;
			break;
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `load` function?
- How does the `load` function initialize the `pattern` array?
- What are the parameters of the `getRegionData` function?
- What is the logic behind the `sample` function?
- How is the subregion extracted from the noise map in the `getRegionData` function?
- Why is the `@setRuntimeSafety(false)` line used in the `load` function?
- What are the constants used in the `load` function?
- What is the purpose of the outer loop in the `load` function?
- How does the `load` function ensure that the grid remains valid in each step?
- What is the purpose of the inner loop in the `load` function?
- What are the conditions for moving a point randomly in the `load` function?
- How many times is the grid repeated to ensure optimal results?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_BlueNoise.zig_chunk_0*
