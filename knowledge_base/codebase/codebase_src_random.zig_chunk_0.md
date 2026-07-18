# [medium/codebase_src_random.zig] - Chunk 0

**Type:** algorithm
**Keywords:** random numbers, LCG algorithm, integer generation, floating-point generation, vector generation, seed scrambling
**Symbols:** scrambleSeed, nextInt, nextIntBounded, nextFloat, nextFloatSigned, nextFloatExp, nextFloatGauss, nextFloatVector, nextFloatVectorSigned, nextDouble, nextDoubleSigned, nextDoubleVector, nextDoubleVectorSigned, nextPointInUnitCircle, initSeed3D, initSeed2D
**Concepts:** random number generation, linear congruential generator (LCG)

## Summary
This chunk provides a set of functions for generating random numbers and points using a linear congruential generator (LCG) algorithm.

## Explanation
This chunk provides a set of functions for generating random numbers and points using a linear congruential generator (LCG) algorithm. The constants used in this LCG are `multiplier = 0x5deece66d`, `addend = 0xb`, and `mask = (1 << 48) - 1`. The `scrambleSeed` function modifies the seed using bitwise operations with these constants: `seed.* = (seed.* ^ multiplier) & mask;`. The `nextInt` function generates an integer of a specified type by either directly using the LCG or combining multiple 32-bit results if the type size exceeds 32 bits. For bounded integers, the `nextIntBounded` function ensures that the generated number is within a given bound and calculates the bit size based on the logarithm of the bound. Functions like `nextFloat`, `nextFloatSigned`, and their vector counterparts generate floating-point numbers, including signed versions and vectors of floats using bitwise operations and conversions to float types. The `nextDouble` and `nextDoubleVector` functions generate double-precision floating-point numbers and vectors by combining 32-bit and 20-bit results respectively. Additionally, there are functions to generate points within a unit circle (`nextPointInUnitCircle`) and initialize seeds based on 3D or 2D positions (`initSeed3D`, `initSeed2D`).

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
