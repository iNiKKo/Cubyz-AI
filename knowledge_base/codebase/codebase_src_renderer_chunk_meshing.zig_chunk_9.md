# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 9

**Type:** implementation
**Keywords:** mutex locking, neighbor chunks, opaque variant, transparent blocks, can be seen through, replace ranges, depends on neighbors, light refresh list
**Symbols:** ChunkMesh, deadlockFreeDoubleLock, updateBlockLight, updateBlockLightAndMesh
**Concepts:** chunk meshing, LOD neighbor quads, back-face culling, deadlock-free double locking, light propagation, block mode dependencies

## Summary
Chunk meshing logic that builds neighbor-facing quads for LOD transitions, updates block lighting under deadlock-free double-locking, and refreshes chunk data when blocks change.

## Explanation
The chunk iterates over its voxel grid using nested loops (x1, x2) to compute world coordinates relative to a neighboring chunk. It derives offsets from the neighbor's relative direction (relX/relY/relZ), masks with chunkMask, and builds a neighborPos via BlockPos.fromCoords. For each candidate block it checks settings.leavesQuality; if zero it replaces the block type with its opaqueVariant(). It then queries canBeSeenThroughOtherBlock to decide whether to render quads: transparent blocks go into transparentSelf, opaque ones into opaqueSelf via appendNeighborFacingQuads (called with neighbor.reverse() and pos). Back-face handling is also considered: if block.hasBackFace() it checks the reverse direction again. After the loops self.replaceRanges(.neighborLod(neighbor), opaqueSelf.items, transparentSelf.items) swaps in the generated quads. The function ends by locking self.mutex, setting needsLightRefresh to false (acq_rel swap), calling finishData(), and mesh_storage.finishMesh(self.pos). A separate deadlockFreeDoubleLock helper acquires two mutexes in pointer-order to avoid deadlocks. updateBlockLight iterates over lightingData[0..] and calls propagateLightsDestructive on each, then if newBlock.light() != 0 it propagates lights again without destruction. updateBlockLightAndMesh locks self.mutex, reads the block at blockUpdatePos from self.chunk.data.getValue, unlocks, initializes neighborBlocks as a splat of zero blocks, then iterates chunk.Neighbor.iterable to fetch each neighbor's chunk location. If the neighbor is inNeighborChunk it gets the neighborChunkMesh via mesh_storage.getNeighbor (or continues), locks its mutex, reads neighborBlock from neighborChunkMesh.chunk.data.getValue, and if neighborBlock.mode().dependsOnNeighbors evaluates true it calls neighborBlock.mode().updateData(&neighborBlock, neighbor.reverse(), newBlock). On success it writes back with setValue, unlocks, calls updateBlockLight on that neighbor, appends the neighborChunkMesh to regenerateMeshList via appendIfNotContained, then re-locks. If the neighbor is not inNeighborChunk it locks self.mutex, reads from self.chunk.data.getValue, performs the same dependsOnNeighbors check and updateData call, writes back if needed, unlocks, and stores the result into neighborBlocks[neighbor.toInt()]. After the loop, if newBlock.mode().dependsOnNeighbors it runs a final pass over chunk.Neighbor.iterable calling updateData with the pre-collected neighborBlocks. It then calls self.updateBlockLight(blockPos, newBlock, lightRefreshList). Finally it locks self.mutex again and clears lastNeighborsHigherLod/lastNeighborsSameLod entries for the six cardinal directions based on blockPos.x/y/z being 0 or 31 (the chunk size minus one), using dirNegX/dirPosX etc. from chunk.Neighbor.

## Related Questions
- What is the purpose of deadlockFreeDoubleLock and how does it prevent deadlocks?
- How are neighbor chunks retrieved when a block update requires them?
- Under what condition does the code replace a block's type with its opaque variant?
- When is canBeSeenThroughOtherBlock invoked and what determines which list receives the quads?
- What happens to lastNeighborsHigherLod/lastNeighborsSameLod when a block at chunk boundary changes?
- How does updateBlockLightAndMesh ensure neighbor blocks are updated before calling updateBlockLight on them?
- Why is needsLightRefresh swapped with .acq_rel after finishData() and what does that imply for ordering?
- What role does mesh_storage.finishMesh play in the chunk's lifecycle after quads are replaced?
- How does the code handle back-face blocks differently from front-facing ones during neighbor iteration?
- When is appendIfNotContained used and why is it necessary for regenerateMeshList?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_9*
