# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 13

**Type:** algorithm
**Keywords:** sorting, buckets, distance, prefix sum, uploadData, backFace, culledSortingCount, blockBreakingFaces, chunkLists, transparentMesh
**Symbols:** SortingData, blockBreakingFacesSortingData, currentSorting, culledSortingCount, buckets, sortingOutputBuffer, faceBuffers, transparentMesh, chunkLists, uploadChunkPosition
**Concepts:** bucket sort, back-face culling, depth sorting, mesh upload, chunk list management, transparency LOD

## Summary
This chunk implements the transparent mesh sorting pipeline: it swaps back-face entries, performs a bucket sort on distance values, uploads sorted faces to the transparent mesh buffer, and appends the resulting chunk allocation to the appropriate chunk list.

## Explanation
The code begins by adjusting culledStart (swapping with backFaceStart when not a back face). It then initializes a buckets array of size 34*3 and clears it. Two loops accumulate counts into buckets: first over blockBreakingFacesSortingData, then over the current sorting up to culledSortingCount. A prefix sum is computed in-place on buckets. Faces are moved into self.sortingOutputBuffer using bucket indices derived from distance (34*3 - 1 - val.distance). Block breaking faces are inserted after front faces but before backfaces. The culledSortingCount is incremented by the number of block breaking faces. Finally, faceBuffers[self.transparentMesh.lod].uploadData writes the sorted buffer into self.transparentMesh.bufferAllocation and uploadChunkPosition is called. After sorting, the chunk allocation start is appended to chunkLists indexed by log2_int(u32, self.pos.voxelSize) and transparentQuadsDrawn is incremented.

## Related Questions
- How does the code handle swapping back-face entries before sorting?
- What is the size of the buckets array used for distance-based sorting?
- In what order are block breaking faces inserted relative to front and back faces?
- Which function uploads the sorted face buffer into the transparent mesh allocation?
- How is the chunk list index computed from self.pos.voxelSize?
- What variable tracks the number of quads drawn after sorting?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_13*
