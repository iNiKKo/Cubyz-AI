# [hard/codebase_src_renderer.zig] - Chunk 2

**Type:** implementation
**Keywords:** glActiveTexture, bindTexture, drawChunksIndirect, prepareTransparentRendering, cullBackface, glDepthRange, settings.bloom, hasFog, fogColor, invViewMatrix, renderHud
**Symbols:** Bloom, MeshSelection
**Concepts:** rendering pipeline, GPU performance measurement, opaque entity rendering, item drop rendering, block entity rendering, particle system rendering, texture rebinding, transparent chunk preparation, indirect draw calls, depth range manipulation, bloom post-processing, fog handling, deferred render pass, HUD rendering

## Summary
This chunk orchestrates the complete rendering pipeline for a frame: it measures GPU performance across entity/block/particle/transparent/final passes, rebinds textures, renders opaque entities and item drops, prepares and draws transparent chunks via indirect draw calls, applies bloom post-processing (with fog handling), updates deferred uniforms, and finally renders the HUD.

## Explanation
The chunk begins by stopping any prior GPU query, then starts a new one for entity rendering; it calls main.entity.client.render with projection matrix, ambient light, player position, and delta time. Next it invokes itemdrop.ItemDropRenderer.renderItemDrops. After that it starts the block_entity_rendering query and calls main.block_entity.renderAll, then stops the query. It proceeds to particle_rendering by calling particles.ParticleSystem.render with view matrix and ambient light. The chunk then rebinds textures: glActiveTexture(GL_TEXTURE0) followed by blocks.meshes.blockTextureArray.bind(), then glActiveTexture(GL_TEXTURE1) and blocks.meshes.emissionTextureArray.bind(). MeshSelection is rendered next. For transparent chunks, the worldFrameBuffer binds its depth texture to GL_TEXTURE5; a GPU barrier is issued via c.glTextureBarrier(); then inside a loop that iterates over meshes in reverse order (i from len down to 1), each mesh calls prepareTransparentRendering(playerPos, &chunkLists) while clearing chunkLists' capacity. After the loop, transparent rendering is measured and drawChunksIndirect(&chunkLists, ...) is called with true for cullBackface. Depth range is set to [0, 0.001] before itemdrop.ItemDropRenderer.renderDisplayItems, then restored to normal depth range. chunk_meshing.endRender() finalizes the transparent pass. The worldFrameBuffer binds its color texture to GL_TEXTURE3. Player block is fetched from mesh_storage via getBlockFromAnyLodFromRenderThread using floor'd player coordinates. If settings.bloom is true, Bloom.render is called with lastWidth/height and player data; otherwise Bloom.bindReplacementImage() is invoked. A final GPU query starts for the copy pass; if activeFrameBuffer equals 0, glViewport is set to window size. The worldFrameBuffer binds its color texture (GL_TEXTURE3) and depth texture (GL_TEXTURE4), then unbinds. deferredRenderPassPipeline.bind(null) prepares the pipeline. Fog uniforms are conditionally set: if blocks.meshes.hasFog(playerBlock) is false, fog.color/density/fogLower/fogHigher from game.world.dayTime.fog are applied; otherwise fogColor is obtained via blocks.meshes.fogColor(playerBlock), its RGB components are extracted and normalized to [0,1], density comes from blocks.meshes.fogDensity(playerBlock), and fogLower/higher are set to 1e10. The inverse view matrix uniform receives the transposed camera viewMatrix; player position integer and fractional parts (via floor and mod) are uploaded as uniforms; zNear/zFar/tanXY are also set. glBindFramebuffer switches to activeFrameBuffer, then graphics.draw.rectVao.bind() is called followed by a drawArrays of GL_TRIANGLE_STRIP with 4 vertices. The framebuffer is unbound. Finally, if main.gui.hideGui is false, main.entity.client.renderHud is invoked.

## Related Questions
- What is the order of rendering passes measured by gpu_performance_measuring in this chunk?
- How does the chunk handle texture rebinding before rendering MeshSelection and transparent chunks?
- Describe the loop that prepares transparent chunks: what data structure is iterated, how capacity is managed, and which function is called per mesh.
- Under what condition does Bloom.render get invoked versus Bloom.bindReplacementImage?
- How are fog uniforms set when hasFog returns false compared to when it returns true?
- What vertex count and draw mode are used for the final rectVao draw call, and why might that be chosen?
- Which functions are responsible for fetching the player block from mesh_storage on the render thread?
- How does the chunk ensure depth testing is temporarily disabled during transparent rendering preparation?
- What role does deferredRenderPassPipeline.bind(null) play in the final copy pass setup?
- In what way does the chunk preserve the original depth range after rendering item drops and before bloom?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_2*
