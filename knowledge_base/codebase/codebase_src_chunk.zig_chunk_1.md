# [hard/codebase_src_chunk.zig] - Chunk 1

**Type:** api
**Keywords:** Lod enum, voxelSizeMask, localMask, ChunkPosition struct, initFromWorldPos, hashCode, equals optional, getMinDistanceSquared, chunkSize constant
**Symbols:** Lod, ChunkPosition
**Concepts:** level of detail, resolution masks, chunk coordinates, voxel size scaling, coordinate conversion, hashing, distance calculation

## Summary
Defines the Lod LOD (Level of Detail) enum with resolution masks and chunk position utilities for world coordinate conversion.

## Explanation
The chunk declares a public const Lod enum representing LOD levels from 1 to 32, each mapped to an integer value. It includes inline functions next/previous for navigation, toInt for extracting the underlying integer, voxelSize returning 1 << level, chunkWidth multiplying by a global chunkSize constant, voxelSizeShift returning the integer tag, and two mask functions: voxelSizeMask producing ~((voxelSize - 1)) as an i32 for converting global coordinates to LOD resolution space, and localMask producing ~(voxelSize*chunkSize - 1) for converting global coordinates to chunk-local coordinates. The chunk also defines a public const ChunkPosition struct with wx/wy/wz fields of type i32 and a voxelSize field of type u31; it provides initFromWorldPos which applies the localMask derived from voxelSize and chunkSize, hashCode using ctz-based shifts and modulo arithmetic, equals handling optional/pointer types and comparing to ServerChunk.super.pos, and getMinDistanceSquared computing halfWidth via @divExact(chunkSize, 2) and absolute differences. All functions are inline or public, indicating they form part of the exposed API for LOD management.

## Related Questions
- What integer value corresponds to Lod level 4?
- How does voxelSizeMask convert global coordinates to LOD resolution space?
- What is the purpose of localMask in coordinate conversion?
- Which fields are stored inside ChunkPosition?
- How does initFromWorldPos apply masking to world positions?
- Does hashCode use ctz-based shifts for its computation?
- How does equals handle optional types compared to pointers?
- What is the role of @divExact in getMinDistanceSquared?
- Can ChunkPosition be directly compared with ServerChunk using equals?
- What happens if equals receives an unsupported type?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_1*
