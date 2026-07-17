# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 7

**Type:** implementation
**Keywords:** mutex, swapRemove, blockBreakingFacesChanged, internalQuads, neighborFacingQuads, render thread, relative position, quad index, defer unlock
**Symbols:** removeBreakingAnimationFace, removeBreakingAnimation
**Concepts:** thread safety, mutex locking, face removal, block breaking animation, neighbor handling

## Summary
This chunk implements thread-safe face removal logic for block-breaking animations by locking mesh mutexes and swapping faces from the breaking list.

## Explanation
The code defines two functions: removeBreakingAnimationFace(pos, quadIndex, neighbor) which locates a specific face in mesh.blockBreakingFaces based on position coordinates and quad index, then swaps it out of the array while marking blockBreakingFacesChanged; it handles optional neighbor offsets by converting them to relative positions. The public function removeBreakingAnimation(pos) retrieves the block from the render thread (returning early if missing), obtains its model via main.blocks.meshes.model(block).model(), iterates over model.internalQuads calling removeBreakingAnimationFace with null neighbor, and then iterates over model.neighborFacingQuads calling removeBreakingAnimationFace for each quad index with the corresponding neighbor enum value. Both functions acquire mesh.mutex.lock() (deferred unlock) to protect blockBreakingFaces modifications; removeBreakingAnimationFace additionally locks mesh.meshUploadMutex during its lookup of the face in either transparent or opaque mesh data, deferring unlock there as well.

## Related Questions
- What mutexes are locked when removing a breaking animation face?
- How does removeBreakingAnimationFace handle optional neighbor offsets?
- Which model fields are iterated over in removeBreakingAnimation?
- What condition causes removeBreakingAnimation to return early without modifying faces?
- Does the code mark blockBreakingFacesChanged after swapping out a face?
- Is meshUploadMutex locked inside removeBreakingAnimationFace and how is it released?
- How are neighbor enum values derived from model.neighborFacingQuads?
- What happens if getBlockFromRenderThread returns null in removeBreakingAnimation?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_7*
