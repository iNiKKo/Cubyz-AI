# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 3

**Type:** implementation
**Keywords:** mesh rendering, face sorting, buffer allocation, lighting processing, culling optimization
**Symbols:** PrimitiveMesh, PrimitiveMesh.completeList, PrimitiveMesh.bufferAllocation, PrimitiveMesh.vertexCount, PrimitiveMesh.byNormalCount, PrimitiveMesh.wasChanged, PrimitiveMesh.min, PrimitiveMesh.max, PrimitiveMesh.lod, PrimitiveMesh.deinit, PrimitiveMesh.replaceRange, PrimitiveMesh.finish, PrimitiveMesh.uploadData, SortingData, SortingData.face, SortingData.distance, SortingData.isBackFace, SortingData.shouldBeCulled, SortingData.update
**Concepts:** chunk meshing, face data management, GPU buffer upload, lighting calculation, backface culling

## Summary
Handles the creation and management of chunk meshes for rendering.

## Explanation
The `PrimitiveMesh` struct manages the mesh data for a single LOD level, including face data storage, buffer allocation, and vertex count. It provides methods to deinitialize resources (`deinit`), replace face ranges (`replaceRange`), finalize mesh data by calculating lighting and bounding boxes (`finish`), and upload mesh data to GPU buffers (`uploadData`). The `SortingData` struct is used for sorting faces based on distance and culling criteria, with an `update` method that recalculates these properties.

## Code Example
```zig
fn deinit(self: *PrimitiveMesh) void {
	faceBuffers[self.lod].free(self.bufferAllocation);
	self.completeList.deinit(main.globalAllocator);
}
```

## Related Questions
- What is the purpose of the `deinit` method in the `PrimitiveMesh` struct?
- How does the `replaceRange` method update the mesh data?
- What steps are involved in finalizing a mesh with the `finish` method?
- How is data uploaded to GPU buffers in the `uploadData` method?
- What criteria are used for sorting faces in the `SortingData` struct?
- How does the `update` method in `SortingData` calculate culling properties?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_3*
