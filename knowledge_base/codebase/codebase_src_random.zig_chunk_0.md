# [medium/codebase_src_random.zig] - Chunk 0

**Type:** algorithm
**Keywords:** PRNG, LCG, seed mutation, bit masking, spatial locality, bounded sampling, vectorized sequences, Box-Muller, exponential distribution, uniform float
**Symbols:** Vec2f, Vec2i, Vec3i, multiplier, addend, mask, scrambleSeed, nextWithBitSize, next, nextInt, nextIntBounded, nextFloat, nextFloatSigned, nextFloatExp, nextFloatGauss, nextPointInUnitCircle, initSeed3D, initSeed2D, RandomRange
**Concepts:** pseudo-random number generation, linear congruential generator, spatial seeding, bounded sampling, vectorized random sequences, Box-Muller transform, exponential distribution, uniform float generation

## Summary
This chunk defines a deterministic pseudo-random number generator (PRNG) suite providing integer and floating-point sequences via linear congruential generation, seeded per-world-position for spatial locality, plus bounded sampling and vectorized variants.

## Explanation
The file imports std and re-exports main.vec types Vec2f, Vec2i, Vec3i; it defines constants multiplier (0x5deece66d), addend (0xb), mask ((1<<48)-1). The public function scrambleSeed mutates a seed pointer by XORing with multiplier then masking to 48 bits. nextWithBitSize performs the LCG step (seed = (seed*multiplier + addend) & mask) and returns an @intCast of the high-order (48-bitSize) bits; it is called by next which adapts bitSize via @bitSizeOf(T). nextInt handles types larger than 32 bits by looping over 32-bit chunks, otherwise delegates to next. nextIntBounded asserts T must be an integer type, converts signed bounds to unsigned if needed, computes the minimal bitSize required for bound via std.math.log2_int_ceil, then repeatedly draws until result < bound. nextFloat returns a uniform f32 in [0,1) by casting a 24-bit integer to float and dividing by 2^24; nextFloatSigned casts to i24 before the same division (range [-1/8, 1)). nextFloatExp applies -log(U[0,1)) for exponential distribution. nextFloatGauss uses Box-Muller: sqrt(-2*log(U1))*cos(2*pi*U2). nextPointInUnitCircle repeatedly draws two signed floats until x^2+y^2<1 and returns the Vec2f point. initSeed3D and initSeed2D compute a world-local seed by XOR-reducing fac (Vec3i or Vec2i) multiplied modulo pos, then cast to u32 and XOR with worldSeed; these are used for spatial seeding. nextDouble splits into lower 32 bits and upper 20 bits via two calls to nextInt(u32) and nextInt(u20), casts to f64 by shifting upper left 32 and dividing by 2^52 (unsigned) or 2^51 (signed). nextDoubleVector/nextDoubleVectorSigned similarly iterate over a compile-time length. All functions are public except nextWithBitSize which is internal.

## Related Questions
- How does scrambleSeed modify the seed value and why is a mask applied?
- What are the exact constants used in the linear congruential generator (multiplier, addend) and how do they affect period length?
- Explain the difference between nextFloat and nextFloatSigned: what ranges do they produce and how is the sign handled?
- How does nextIntBounded guarantee a result strictly less than bound without biasing toward lower values?
- What is the purpose of initSeed3D/initSeed2D and how are fac vectors chosen to ensure good spatial distribution?
- Describe the Box-Muller implementation in nextFloatGauss: why two uniform samples and what trigonometric function is used?
- How does nextDouble split a 64-bit float into lower and upper parts using nextInt calls, and why are different bit widths chosen for signed vs unsigned?
- What compile-time constraints exist on the types passed to these random functions (e.g., integer check in nextIntBounded)?
- How does the mask ((1<<48)-1) limit the LCG state space and what impact does that have on reproducibility across builds?
- Can a caller safely mutate the seed pointer after calling scrambleSeed, or must they preserve the original value?

*Source: unknown | chunk_id: codebase_src_random.zig_chunk_0*
