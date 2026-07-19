# [hard/codebase_src_chunk.zig] - Chunk 0

**Type:** implementation
**Keywords:** constants, enum, relative positions, bitmask, texture coordinates, memory pool, global arena allocator
**Symbols:** chunkShift, chunkSize, chunkSizeIterator, chunkVolume, chunkMask, Neighbor, Neighbor.dirUp, Neighbor.dirDown, Neighbor.dirPosX, Neighbor.dirNegX, Neighbor.dirPosY, Neighbor.dirNegY, Neighbor.toInt, Neighbor.relX, Neighbor.relY, Neighbor.relZ, Neighbor.relPos, Neighbor.fromRelPos, Neighbor.bitMask, Neighbor.iterable, Neighbor.orthogonalComponents, Neighbor.textureX, Neighbor.textureY, Neighbor.reverse, Neighbor.isPositive, Neighbor.VectorComponentEnum, Neighbor.vectorComponent, Neighbor.extractDirectionComponent, Neighbor.rotateZ, memoryPool, serverPool
**Concepts:** chunk management, neighbor relationships, memory pooling

## Summary
Defines constants and structures for chunk management, including neighbor relationships and memory pooling.

## Explanation
This chunk defines several constants related to chunk dimensions and a Neighbor enum that describes the six possible directions of neighboring blocks. The Neighbor enum includes methods to convert between direction and relative positions, bitmasks, and texture coordinates. It also provides utility functions for reversing directions, checking positivity, extracting vector components, rotating around the z-axis, and iterating over all neighbors. Additionally, it declares memory pools for managing Chunk and ServerChunk instances using a global arena allocator.

**Constants:**
- `chunkShift`: 5
- `chunkSize`: 1 << chunkShift (32)
- `chunkVolume`: 1 << 3*chunkShift (32768)
- `chunkMask`: chunkSize - 1 (31)

**Neighbor Enum:**
- `dirUp`: 0
- `dirDown`: 1
- `dirPosX`: 2
- `dirNegX`: 3
- `dirPosY`: 4
- `dirNegY`: 5

**Methods:**
- `toInt(self: Neighbor) u3`: Converts the enum to an integer.
- `relX(self: Neighbor) i32`: Returns the relative X position of the neighbor.
- `relY(self: Neighbor) i32`: Returns the relative Y position of the neighbor.
- `relZ(self: Neighbor) i32`: Returns the relative Z position of the neighbor.
- `relPos(self: Neighbor) Vec3i`: Returns the relative position as a vector.
- `fromRelPos(pos: Vec3i) ?Neighbor`: Converts a relative position to a Neighbor enum value if valid.
- `bitMask(self: Neighbor) u6`: Returns the bitmask for bitmap direction data.
- `iterable`: An array of all Neighbor values for easy iteration.
- `orthogonalComponents(self: Neighbor) Vec3i`: Marks the two dimensions that are orthogonal to the neighbor.
- `textureX(self: Neighbor) Vec3i`: Returns the texture X coordinate relative to the neighbor.
- `textureY(self: Neighbor) Vec3i`: Returns the texture Y coordinate relative to the neighbor.
- `reverse(self: Neighbor) Neighbor`: Reverses the direction of the neighbor.
- `isPositive(self: Neighbor) bool`: Checks if the neighbor is positive.
- `vectorComponent(self: Neighbor) VectorComponentEnum`: Extracts the vector component of the neighbor.
- `extractDirectionComponent(self: Neighbor, in: anytype) @TypeOf(in[0])`: Extracts the direction component from a given input.
- `rotateZ(self: Neighbor) Neighbor`: Rotates the neighbor by 90 degrees counterclockwise around the z-axis.

## Code Example
```zig
pub inline fn toInt(self: Neighbor) u3 {
	return @intFromEnum(self);
}
```

## Related Questions
- What is the size of a chunk in Cubyz?
- How are neighboring blocks defined in Cubyz?
- What methods does the Neighbor enum provide for direction manipulation?
- How is memory allocated for chunks in Cubyz?
- What is the purpose of the chunkMask constant?
- How do you determine the relative position of a neighbor in Cubyz?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_0*
