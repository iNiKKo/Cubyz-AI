# [medium/codebase_src_random.zig] - Chunk 1

**Type:** implementation
**Keywords:** vector operations, XOR reduction, random range, seed computation, generic struct
**Symbols:** initSeed3D, initSeed2D, RandomRange
**Concepts:** random number generation, seed initialization

## Summary
Provides functions for initializing random seeds in 2D and 3D space, and a generic struct for generating random numbers within a specified range.

## Explanation
The chunk defines three main functionalities: seed initialization for 2D and 3D positions, and a generic random number generator with a range. The `initSeed3D` and `initSeed2D` functions compute a unique seed based on a world seed and position vectors using vector multiplication and XOR reduction. The `RandomRange` struct template allows creating a range object that can generate random numbers within a specified minimum and maximum value, utilizing a provided seed for randomness.

## Code Example
```zig
pub fn initSeed3D(worldSeed: u64, pos: Vec3i) u64 {
	const fac = Vec3i{11248723, 105436839, 45399083};
	const seed = @reduce(.Xor, fac*%pos);
	return @as(u32, @bitCast(seed)) ^ worldSeed;
}
```

## Related Questions
- How is the seed initialized for a 3D position?
- What is the purpose of the `RandomRange` struct?
- How does the `initSeed2D` function work?
- What type does the `RandomRange` template return?
- How are random numbers generated within a specified range?
- What operations are performed on vectors in seed initialization?

*Source: unknown | chunk_id: codebase_src_random.zig_chunk_1*
