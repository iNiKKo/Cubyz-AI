# [hard/codebase_src_chunk.zig] - Chunk 0

**Type:** implementation
**Keywords:** constants, enum, relative positions, bitmask, texture coordinates, memory pool, global arena allocator
**Symbols:** chunkShift, chunkSize, chunkSizeIterator, chunkVolume, chunkMask, Neighbor, Neighbor.dirUp, Neighbor.dirDown, Neighbor.dirPosX, Neighbor.dirNegX, Neighbor.dirPosY, Neighbor.dirNegY, Neighbor.toInt, Neighbor.relX, Neighbor.relY, Neighbor.relZ, Neighbor.relPos, Neighbor.fromRelPos, Neighbor.bitMask, Neighbor.iterable, Neighbor.orthogonalComponents, Neighbor.textureX, Neighbor.textureY, Neighbor.reverse, Neighbor.isPositive, Neighbor.VectorComponentEnum, Neighbor.vectorComponent, Neighbor.extractDirectionComponent, Neighbor.rotateZ, memoryPool, serverPool
**Concepts:** chunk management, neighbor relationships, memory pooling

## Summary
Defines constants and structures for chunk management, including neighbor relationships and memory pooling.

## Explanation
This chunk defines several constants related to chunk dimensions and a Neighbor enum that describes the six possible directions of neighboring blocks. The Neighbor enum includes methods to convert between direction and relative positions, bitmasks, and texture coordinates. It also provides utility functions for reversing directions, checking positivity, extracting vector components, rotating around the z-axis, and iterating over all neighbors. Additionally, it declares memory pools for managing Chunk and ServerChunk instances using a global arena allocator.

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
