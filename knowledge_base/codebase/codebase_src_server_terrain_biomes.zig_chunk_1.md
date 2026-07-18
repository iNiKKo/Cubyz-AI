# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 1

**Type:** implementation
**Keywords:** bitwise operations, hash function, RGB conversion, enum, interpolation
**Symbols:** hashInt, Interpolation, Interpolation.none, Interpolation.linear, Interpolation.square, u32ToVec3
**Concepts:** integer hashing, color conversion

## Summary
This chunk defines a hash function for integers and utility functions for color conversion.

## Explanation
The chunk contains a function `hashInt` which performs integer hashing using bitwise operations. It also includes an enum `Interpolation` with three variants: none, linear, and square. Additionally, there is a function `u32ToVec3` that converts a u32 color value into a Vec3f representing RGB values normalized between 0 and 1.

## Code Example
```zig
fn hashInt(input: u64) u64 {
	var x = input;
	x = (x ^ (x >> 30))*%0xbf58476d1ce4e5b9;
	x = (x ^ (x >> 27))*%0x94d049bb133111eb;
	x = x ^ (x >> 31);
	return x;
}
```

## Related Questions
- How does the hashInt function work?
- What are the variants of the Interpolation enum?
- How is a u32 color converted to Vec3f in this code?
- Can you explain the bitwise operations used in hashInt?
- What is the purpose of the Interpolation enum in this context?
- How does the RGB conversion work in u32ToVec3?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_1*
