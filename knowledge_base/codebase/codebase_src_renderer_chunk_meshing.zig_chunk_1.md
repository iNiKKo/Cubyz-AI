# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 1

**Type:** implementation
**Keywords:** faceBuffers, lightBuffers, chunkIDBuffer, commandBuffer, Vao, glDispatchCompute, glMultiDrawElementsIndirect, ssbo.bind, uniform uploads, memory barriers, transparent fog, lod distance, player position integer, player position fractional, occlusion test pipeline
**Symbols:** drawChunksIndirect, drawChunksOfLod, bindBuffers, bindShaderAndUniforms, bindTransparentShaderAndUniforms, beginRender, endRender, deinit, bindCommonUniforms
**Concepts:** chunk meshing, LOD rendering, indirect draw calls, compute shader dispatch, occlusion testing, uniform binding, SSBO allocation, multi-draw elements, memory barriers, shader pipeline switching

## Summary
Chunk meshing: allocates face/light buffers per LOD, initializes VAO with empty vertex data and indirect index buffer, deinit pipelines/buffers, begin/end render loops over all LODs, binds common/transparent shaders, dispatches compute for occlusion tests.

## Explanation
The chunk meshes this file constructs a graphics pipeline by allocating faceBuffers[i] and lightBuffers[i] (each 1<<20 bytes) for every supported LOD level, initializing an empty VertexArray with no vertices but populated indirect index data via rawData computed from a lookup table lut. It then provides deinit() to tear down all pipelines (pipeline, transparentPipeline, occlusionTestPipeline, commandPipeline), VAO, and per-LOD face/light buffers plus chunkBuffer, commandBuffer, chunkIDBuffer. beginRender() iterates over LODs calling beginRender on each buffer; endRender() mirrors that with corresponding endRender calls. bindCommonUniforms uploads projection matrix, reflection map size, block contrast, lod distance (lod0.5Distance), view matrix, ambient light, near/far planes, and player position split into integer and fractional components using floor/mod casts. bindShaderAndUniforms binds the main pipeline to null, invokes bindCommonUniforms on uniforms struct, then binds VAO. bindTransparentShaderAndUniforms similarly sets up fog color/density/lower/higher from game.world.dayTime.fog fields, calls bindCommonUniforms on transparentUniforms, and binds VAO. bindBuffers selects LOD-specific SSBO bindings for faceBuffers[lod] and lightBuffers[lod]. drawChunksIndirect iterates over chunkIds array; when transparent it walks backwards through LOD levels (highestSupportedLod - i), otherwise forwards, calling bindBuffers(lod) then drawChunksOfLod(chunkIds[lod].items,...). drawChunksOfLod returns early if no chunks, estimates draw calls as len*8 for opaque or len for transparent, uploads chunkIDs into chunkIDBuffer via uploadData with a deferred free, allocates indirect data in commandBuffer (rawAlloc) and frees it on exit, binds commandPipeline, sets lodDistance uniform, passes the start index of the allocated chunkID buffer region, size of draw calls, isTransparent flag, integer player position, and for opaque draws also sets onlyDrawPreviouslyInvisible to 0 before dispatching a compute shader via glDispatchCompute with workgroup count ceil((len+63)/64) (TODO replace with @divCeil). After the compute dispatch it inserts memory barriers for shader storage and command. If transparent it binds the transparent shader path; otherwise it binds the main shader path, then binds the indirect buffer and issues a multi-draw elements call using glMultiDrawElementsIndirect with GL_TRIANGLES and an IndirectData pointer derived from allocation.start*sizeOf(IndirectData). Finally it begins occlusion testing by binding occlusionTestPipeline to null, uploading player position integer/fractional uniforms, projection and view matrices, and binds VAO.

## Related Questions
- How are faceBuffers and lightBuffers sized per LOD level?
- What does rawData compute for the indirect index buffer?
- Why is onlyDrawPreviouslyInvisible set to 0 only in opaque draws?
- How is the chunkIDBuffer upload deferred free handled?
- What workgroup count formula is used for glDispatchCompute?
- Which uniforms are uploaded by bindCommonUniforms vs bindTransparentShaderAndUniforms?
- How does drawChunksIndirect decide which LOD index to use when transparent is true?
- What memory barriers are inserted after the compute dispatch?
- Where is the IndirectData struct referenced in this chunk?
- How is player position split into integer and fractional components for uniforms?
- Is there any vertex data initialized in the VAO before draw calls?
- What happens to pipelines in deinit versus beginRender/endRender?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_1*
