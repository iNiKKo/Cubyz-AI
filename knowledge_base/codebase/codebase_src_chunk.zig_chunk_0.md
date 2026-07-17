# [hard/codebase_src_chunk.zig] - Chunk 0

**Type:** implementation
**Keywords:** enum, inline fn, Vec3i, bitMask, orthogonalComponents, rotateZ, extractDirectionComponent, memoryPool, serverPool
**Symbols:** chunkShift, chunkSize, chunkSizeIterator, chunkVolume, chunkMask, Neighbor, Lod
**Concepts:** neighbor enumeration, relative position lookup, texture coordinate generation, memory pooling, LOD levels

## Summary
Defines chunk constants (shift/size/mask), a Neighbor enum with relative position and texture lookup methods, LOD levels, and memory pool declarations.

## Explanation
The chunk declares pub const chunkShift = 5 and derives chunkSize as 1 << chunkShift, chunkVolume as 1 << 3*chunkShift, and chunkMask as chunkSize - 1. It defines a public Neighbor enum(u3) with six directional variants (dirUp, dirDown, dirPosX, dirNegX, dirPosY, dirNegY). Each variant exposes inline toInt returning the enum value, relX/relY/relZ returning i32 offsets from static arrays, and relPos returning Vec3i composed of those offsets. The enum also provides bitMask (u6) shifting 1 by the enum value, an iterable array of all six neighbors, orthogonalComponents returning Vec3i with two non-zero entries per neighbor, textureX/textureY returning Vec3i for face normals, reverse flipping the least significant bit via XOR 1, isPositive checking LSB == 0, vectorComponent mapping to VectorComponentEnum (x/y/z), extractDirectionComponent using a comptime switch on val.vectorComponent() to index into anytype input, and rotateZ returning a neighbor rotated 90° CCW around Z. Two global heap pools are declared: memoryPool of type main.heap.MemoryPool(Chunk) initialized with main.globalArena, and serverPool of type main.heap.MemoryPool(ServerChunk) also initialized with main.globalArena.

## Related Questions
- What does the Neighbor enum represent and how many directions are defined?
- How is chunkSize computed from chunkShift in this file?
- Which methods on Neighbor return relative coordinate offsets for each direction?
- How can I obtain a neighbor rotated 90 degrees around the Z axis using this enum?
- What does the bitMask method produce and why is it useful?
- Where are the global memory pools declared and what types do they hold?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_0*
