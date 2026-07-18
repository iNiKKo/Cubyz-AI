# [easy/codebase_src_server_terrain_noise_ValueNoise.zig] - Chunk 0

**Type:** implementation
**Keywords:** percentiles, random numbers, simulation, cumulative distribution function, binary search, linear interpolation
**Symbols:** randomNumbers, positions, totalValues, values, amount1D, amount2D, samples, percentiles, i, j, val, goal, diff, index, offset, ratio, scaledToList, percentileTable
**Concepts:** Percentile Calculation, Random Number Simulation, Cumulative Distribution Function (CDF), Binary Search-like Approach, Linear Interpolation

## Summary
Implements 2D value noise (`samplePoint2D`, result in `0..1`) via seeded interpolated grid sampling, plus a precomputed 128-entry `percentileTable` (built offline by `preGeneratePercentileTable`, a 4096x4096 Monte Carlo simulation) used by `percentile()` to remap a noise ratio onto its statistical percentile.

## Explanation
`getSeedX`/`getSeedY` derive a deterministic per-integer-coordinate seed by XORing the world seed with that coordinate multiplied by a large odd constant (`54275629861` for X, `5478938690717` for Y). `getGridValue1D` turns such a seed into a single random float. `samplePoint1D` adds a small random jitter (`0.0001`) to the input position, then linearly interpolates between the grid values at the floor and floor+1 of that jittered position. `samplePoint2D(x, y, worldSeed)` adds a random offset to `y`, derives a `lineSeed`, then linearly interpolates between two `samplePoint1D` calls (using Y-derived seeds) for the rows above and below `y` -- the result is always in `0..1`.

`preGeneratePercentileTable` is an offline generator (not called at runtime): it simulates `4096` random numbers x `4096` positions, computing `x*(2a+1) + (positions-x)*(2b+1)` for every combination to build a 1D distribution (`amount1D`), then squares that into a 2D distribution (`amount2D`) representing the sum of two such values (approximating what `samplePoint2D`'s bilinear interpolation actually produces). It sums to get total `samples`, then walks the cumulative distribution to find 128 evenly-spaced percentile boundaries, printing each computed percentile via `std.log.info`. The output of this function is baked into the `percentileTable` constant (128 float values from `0.0` to `1.0`) checked into the source.

`percentile(ratio)` scales `ratio` (must be `>= 0`) into an index into `percentileTable`, returning `1` if it's past the table's end, otherwise linearly interpolating between the two nearest table entries.

## Related Questions
- What does the `samplePoint2D` function return, and what is its value range?
- How are the seeds for X and Y coordinates derived in this noise implementation?
- What is the purpose of `preGeneratePercentileTable`, and is it called at runtime?
- How many random numbers and positions does the percentile simulation use?
- How does the `percentile` function use the precomputed `percentileTable`?
- What happens if `percentile` is called with a ratio at or beyond the table's range?

## Code Example
```zig
fn getSeedX(x: f32, worldSeed: u64) u64 {
	return worldSeed ^ @as(u64, 54275629861)*%@as(u32, @bitCast(@as(i32, @trunc(x))));
}
```

## Related Questions
- zig code snippet
- percentile calculation in zig
- zig function to calculate percentile
- zig code for generating percentile table
- zig code to find percentile value
- zig code for percentile interpolation

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_ValueNoise.zig_chunk_0*
