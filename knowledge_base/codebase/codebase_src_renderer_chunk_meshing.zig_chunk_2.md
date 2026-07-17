# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 2

**Type:** implementation
**Keywords:** FaceData, ChunkData, IndirectData, FaceGroups, PrimitiveMesh, neighborLod, deinit, replaceRange, finish, getEverything, lightMap, visibilityState
**Symbols:** FaceData, ChunkData, IndirectData, FaceGroups, PrimitiveMesh
**Concepts:** meshing pipeline, face data structures, neighbor LOD groups, occlusion testing, indirect draw dispatch, visibility state management, light map hashing

## Summary
This chunk implements the renderer's meshing pipeline, managing face data structures for opaque and transparent chunks, handling neighbor LOD groups, performing occlusion tests, and dispatching compute workloads to draw indirect buffers.

## Explanation
The chunk defines FaceData as an extern struct with packed position fields (x,y,z,u5), backFace bool, lightIndex u16, blockAndQuad containing texture and quadIndex. It provides init() taking texture, quadIndex, pos, and comptime backFace to construct a FaceData instance. ChunkData is defined as an extern struct holding position Vec3i, min/max Vec3f aligned 16, voxelSize i32, lightStart u32, vertexStartOpaque/Transparent u32, faceCountsByNormalOpaque [14]u32, visibilityState and oldVisibilityState u32. IndirectData is an extern struct with count, instanceCount, firstIndex, baseVertex, baseInstance for glMultiDrawElementsIndirect. FaceGroups is a public enum(u32) listing core plus neighbor0..neighbor5 and neighborLod0..neighborLod5 plus optional; it exposes neighbor() and neighborLod() functions that map main.chunk.Neighbor values to the corresponding FaceGroups variant via @enumFromInt arithmetic. PrimitiveMesh is a struct containing completeList (MultiArray(FaceData,FaceGroups)), bufferAllocation (graphics.SubAllocation), vertexCount u31, byNormalCount [14]u32 initialized with @splat(0), wasChanged bool default false, min/max Vec3f defaults to floatMax/-floatMax, and lod u3. PrimitiveMesh exposes deinit() which frees faceBuffers[self.lod].bufferAllocation via faceBuffers array access and calls completeList.deinit(main.globalAllocator). replaceRange() delegates to completeList.replaceRange with the given group and items. finish() sets min/max bounds, iterates over self.completeList.getEverything(), retrieves lighting for each face using parent chunk and face.position plus texture/quadIndex, then uses lightMap (std.AutoHashMap([4]u32,u16)) to getOrPut the light key; if not found it casts lightList.items.len/4 as u32 into result.value_ptr.*, appends slice(&light) to lightList, and writes face.position.lightIndex = result.value_ptr.*. The chunk also contains a public function neighborLod(n: main.chunk.Neighbor) FaceGroups returning @enumFromInt(@intFromEnum(FaceGroups.neighborLod0)+@intFromEnum(n)).

## Related Questions
- What fields does FaceData contain and how are they packed?
- How is the neighbor LOD enum constructed from a main.chunk.Neighbor value?
- Which function in PrimitiveMesh frees its allocated face buffers on deinit?
- How does finish() populate the light map using std.AutoHashMap?
- What default values are assigned to min and max in PrimitiveMesh?
- How is the vertex count stored in PrimitiveMesh typed?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_2*
