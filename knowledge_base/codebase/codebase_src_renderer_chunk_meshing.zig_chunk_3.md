# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 3

**Type:** implementation
**Keywords:** primitive mesh, opaque transparent rendering, neighbor LOD state, sorting data, circular buffer queue, mutex protection, backface culling, light map insertion, quad corners, vertex count calculation
**Symbols:** PrimitiveMesh, SortingData, ChunkMesh
**Concepts:** chunk meshing, backface culling, LOD neighbor tracking, lighting data aggregation, GPU upload sorting

## Summary
ChunkMesh defines the meshing pipeline for a voxel chunk, managing opaque and transparent PrimitiveMesh instances, lighting data, neighbor LOD state, sorting/culling buffers, and provides methods to deinit, replace ranges, finish lighting, upload sorted face data, and update sorting metadata.

## Explanation
The ChunkMesh struct holds two PrimitiveMesh pointers (opaqueMesh, transparentMesh) for rendering faces at different transparency levels. It contains lightingData: [2]*lighting.ChannelChunk for per-channel light information, a meshUploadMutex to protect concurrent uploads, blockUpdateQueue (CircularBufferQueue<Vec3i>) for deferred block updates, and neighbor LOD state arrays (lastNeighborsSameLod, lastNeighborsHigherLod, isNeighborLod) that track which neighboring chunks are at the same or higher level of detail. The struct also includes currentSorting: []SortingData and sortingOutputBuffer: []FaceData used to collect faces for backface culling, culledSortingCount tracks how many were culled, and lastTransparentUpdatePos remembers where transparent updates occurred.

The deinit method frees faceBuffers[self.lod] via its free function and calls self.completeList.deinit(main.globalAllocator) to release the internal list of FaceData. replaceRange delegates to self.completeList.replaceRange with main.globalAllocator for a given FaceGroups, inserting new items into the complete list. finish initializes min/max bounds by splatting float extremes, then iterates over all faces in self.completeList.getEverything(). For each face it queries lighting via lighting.getLight(parent, position, texture, quadIndex) and inserts or retrieves the light index from lightMap; if a new light is found it appends to lightList. It also computes basePos by converting integer face coordinates to floats, then walks the four corners of the quad (via quadInfo().corners) updating min/max with @min/@max.

uploadData prepares GPU data sorted by normal direction for backface culling. It first counts core and optional faces via getRange, then builds a list array where each entry is either self.completeList.getRange(.neighbor(...)) or .neighborLod(...) depending on the isNeighborLod flags. It allocates a fullBuffer from faceBuffers[self.lod] with allocateAndMapRange, deferring unmapping. The core and optional faces are placed into fullBuffer sequentially. Then for normals 0..6 it iterates coreList: if the quad's extraQuadInfo().alignedNormalDirection matches the current normal (or is null/edge case at normal==6) it copies the face; otherwise when normal<6 it uses @memcpy to copy neighbor faces from list[normalDir.reverse()].toInt() into fullBuffer, advancing i. After coreList it records self.byNormalCount[normal] = count and resets iStart. The same pattern repeats for optionalList but writes to indices offset by +7 in byNormalCount. Finally std.debug.assert ensures all allocated space is filled, sets vertexCount = 6*fullBuffer.len (each face contributes six vertices), and marks wasChanged.

SortingData is a small struct holding a FaceData pointer, distance (u32), isBackFace bool, and shouldBeCulled bool. Its update method receives chunkDx/Dy/Dz offsets from the parent chunk. It extracts x/y/z from self.face.position, adds the offsets to get dx/dy/dz, copies isBackFace, reads quadIndex.quadInfo().normal as Vec3f, then computes dot(normalVector, Vec3i{dx,dy,dz}) and sets shouldBeCulled true if >0 (backface relative to view direction). It also computes fullDx/Dy/Dz by subtracting the integer component of the normal vector from the offset coordinates; these are used for distance calculation via @abs sum. The TODO comments indicate this logic is not yet adjusted for arbitrary voxel models, implying it currently assumes axis-aligned normals or a specific model class.

## Code Example
```zig
fn deinit(self: *PrimitiveMesh) void {
	faceBuffers[self.lod].free(self.bufferAllocation);
	self.completeList.deinit(main.globalAllocator);
}
```

## Related Questions
- What happens to the face buffers when a ChunkMesh is deallocated?
- How does finish populate lightList and compute min/max bounds for a PrimitiveMesh?
- In uploadData, how are neighbor LOD faces selected versus same-LOD neighbors?
- Why is there an assert after filling fullBuffer in uploadData?
- What role does meshUploadMutex play in ChunkMesh operations?
- How does SortingData.update determine whether a face should be culled?
- Where are core and optional faces stored before being uploaded to the GPU?
- What is the purpose of byNormalCount array entries at indices 0..6 versus 7..13?
- Does finish iterate over all faces or only a subset, and how does it access them?
- How does replaceRange insert new FaceData into the complete list without reallocating?
- What information is required by lighting.getLight to resolve a face's light index?
- Are there any public methods on ChunkMesh that expose its internal sorting buffers?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_3*
