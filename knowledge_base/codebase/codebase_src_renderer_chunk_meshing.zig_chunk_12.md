# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 12

**Type:** implementation
**Keywords:** meshing, rendering, transparency, sorting, LOD, bucket sort
**Symbols:** ChunkMesh, ChunkMesh.position, ChunkMesh.voxelSize, ChunkMesh.lightStart, ChunkMesh.vertexStartOpaque, ChunkMesh.faceCountsByNormalOpaque, ChunkMesh.vertexStartTransparent, ChunkMesh.vertexCountTransparent, ChunkMesh.min, ChunkMesh.max, ChunkMesh.visibilityState, ChunkMesh.oldVisibilityState, ChunkMesh.opaqueMesh, ChunkMesh.transparentMesh, ChunkMesh.meshUploadMutex, ChunkMesh.currentSorting, ChunkMesh.sortingOutputBuffer, ChunkMesh.lastTransparentUpdatePos, ChunkMesh.blockBreakingFaces, ChunkMesh.blockBreakingFacesChanged, ChunkMesh.blockBreakingFacesSortingData, ChunkMesh.culledSortingCount, ChunkMesh.prepareRendering, ChunkMesh.updateTransparencyDataAfterMeshUpload, ChunkMesh.prepareTransparentRendering
**Concepts:** chunk meshing, rendering preparation, transparent rendering, bucket sort

## Summary
Handles chunk meshing and rendering preparation for opaque and transparent voxels, including specific details about the ChunkMesh structure and the functions' logic.

## Explanation
This chunk manages the preparation of chunk meshes for rendering, including both opaque and transparent voxel data. It includes functions to prepare rendering by adding chunks to appropriate lists based on their LOD (Level of Detail) and updating transparency data after mesh uploads.

The `ChunkMesh` structure contains various fields such as:
- `.position`: A tuple containing the world coordinates (`wx`, `wy`, `wz`) and voxel size.
- `.voxelSize`: The size of the voxels in the chunk.
- `.lightStart`: The starting index for lighting data.
- `.vertexStartOpaque` and `.faceCountsByNormalOpaque`: Data related to opaque mesh vertices and face counts by normal direction.
- `.vertexStartTransparent` and `.vertexCountTransparent`: Data related to transparent mesh vertices and vertex count.
- `.min` and `.max`: The minimum and maximum coordinates of the chunk.
- `.visibilityState` and `.oldVisibilityState`: States for visibility tracking.
- `.opaqueMesh` and `.transparentMesh`: Structures holding mesh data for opaque and transparent voxels, respectively.
- `.meshUploadMutex`: A mutex for synchronizing mesh uploads.
- `.currentSorting` and `.sortingOutputBuffer`: Buffers for sorting face data.
- `.lastTransparentUpdatePos`: The last position used to update transparency data.
- `.blockBreakingFaces` and `.blockBreakingFacesChanged`: Data related to block breaking faces and their change state.
- `.blockBreakingFacesSortingData`: Sorting data for block breaking faces.
- `.culledSortingCount`: Count of culled sorting entries.

The `prepareRendering` function adds opaque chunks to the render list if they have vertices. The `updateTransparencyDataAfterMeshUpload` function updates sorting data for transparent faces, ensuring they are rendered correctly relative to the player's position. The `prepareTransparentRendering` function checks for changes in transparent data and updates sorting accordingly, using a bucket sort algorithm to organize faces by distance.

The `prepareTransparentRendering` function includes conditions such as checking if the transparent mesh or block breaking faces have changed, updating relative positions based on the player's position, and re-sorting faces if necessary. The bucket sort algorithm organizes faces into buckets based on their distance from the camera, ensuring they are drawn in the correct order.

## Code Example
```zig
pub fn prepareRendering(self: *ChunkMesh, chunkLists: *[main.settings.highestSupportedLod + 1]main.ListManaged(u32)) void {
		if (self.opaqueMesh.vertexCount == 0) return;

		chunkLists[std.math.log2_int(u32, self.pos.voxelSize)].append(self.chunkAllocation.start);

		quadsDrawn += self.opaqueMesh.vertexCount/6;
	}
```

## Related Questions
- What is the purpose of the `prepareRendering` function?
- How does the chunk determine if it needs to update transparency data?
- What sorting algorithm is used for transparent faces?
- What conditions trigger a re-sorting of transparent faces?
- How are opaque chunks added to the render list?
- What is the role of the `meshUploadMutex` in this code?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_12*
