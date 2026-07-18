# [medium/codebase_src_random.zig] - Chunk 0

**Type:** algorithm
**Keywords:** random numbers, LCG algorithm, integer generation, floating-point generation, vector generation, seed scrambling
**Symbols:** scrambleSeed, nextInt, nextIntBounded, nextFloat, nextFloatSigned, nextFloatExp, nextFloatGauss, nextFloatVector, nextFloatVectorSigned, nextDouble, nextDoubleSigned, nextDoubleVector, nextDoubleVectorSigned, nextPointInUnitCircle, initSeed3D, initSeed2D
**Concepts:** random number generation, linear congruential generator (LCG)

## Summary
This chunk provides a set of functions for generating random numbers and points using a linear congruential generator (LCG) algorithm.

## Explanation
The chunk defines several public functions to generate random values of various types, including integers, floating-point numbers, vectors, and points. It uses a linear congruential generator (LCG) with specific constants for generating pseudo-random numbers. The `scrambleSeed` function modifies the seed using bitwise operations. The `nextInt` function generates an integer of a specified type by either directly using the LCG or combining multiple 32-bit results if the type size exceeds 32 bits. The `nextIntBounded` function ensures that the generated number is within a given bound. Functions like `nextFloat`, `nextFloatSigned`, and their vector counterparts generate floating-point numbers, including signed versions and vectors of floats. The `nextDouble` and `nextDoubleVector` functions generate double-precision floating-point numbers and vectors. Additionally, there are functions to generate points within a unit circle (`nextPointInUnitCircle`) and initialize seeds based on 3D or 2D positions (`initSeed3D`, `initSeed2D`).

## Code Example
```zig
pub fn scrambleSeed(seed: *u64) void {
	seed.* = (seed.* ^ multiplier) & mask;
}
```

## Related Questions
- How does the `scrambleSeed` function modify the seed?
- What is the purpose of the `nextIntBounded` function?
- How are floating-point numbers generated in this chunk?
- What algorithm is used for generating random numbers?
- How do the vector generation functions work?
- What is the role of the `initSeed3D` and `initSeed2D` functions?

*Source: unknown | chunk_id: codebase_src_random.zig_chunk_0*
