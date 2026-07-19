# [hard/codebase_src_renderer_chunk_meshing.zig] - Chunk 1

**Type:** implementation
**Keywords:** deinitialization, rendering pipeline, shader uniforms, indirect draw, occlusion test
**Symbols:** deinit, beginRender, endRender, bindCommonUniforms, bindShaderAndUniforms, bindTransparentShaderAndUniforms, drawChunksIndirect, drawChunksOfLod
**Concepts:** chunk meshing, shader binding, uniform setting, indirect drawing, occlusion testing

## Summary
Handles the rendering of chunk meshes in Cubyz, including initialization, binding shaders and uniforms, drawing chunks, and performing occlusion tests.

## Explanation
This chunk manages the rendering process for chunk meshes in the Cubyz engine. It includes functions to initialize and deinitialize resources (`deinit`), begin and end rendering (`beginRender`, `endRender`), bind common shader uniforms (`bindCommonUniforms`), and bind specific shaders with their respective uniforms (`bindShaderAndUniforms`, `bindTransparentShaderAndUniforms`). The chunk also handles the drawing of chunks indirectly (`drawChunksIndirect`) and the detailed drawing process for each level of detail (`drawChunksOfLod`). It performs occlusion tests to determine which chunks are visible and then draws them accordingly. The code interacts with various buffers, pipelines, and shaders to manage the rendering state and execute draw calls efficiently.

The `deinit` function deinitializes all resources used in chunk rendering, including pipelines, buffers, and other related objects. The `beginRender` function prepares for rendering by beginning render operations on face buffers, light buffers, chunk buffer, command buffer, and chunk ID buffer. The `endRender` function ends the render operations similarly.

The `bindCommonUniforms` function sets several common uniforms used across different shaders. These include the projection matrix (`locations.projectionMatrix`), reflection map size (`locations.reflectionMapSize`), block contrast (`locations.contrast`), LOD distance (`locations.lodDistance`), view matrix (`locations.viewMatrix`), ambient light color (`locations.ambientLight`), near and far clipping planes (`locations.zNear`, `locations.zFar`), player position integer part (`locations.playerPositionInteger`), and player position fractional part (`locations.playerPositionFraction`).

The `bindShaderAndUniforms` function binds the main pipeline and sets common uniforms for it. The `bindTransparentShaderAndUniforms` function binds the transparent pipeline, sets additional fog-related uniforms (`fog.color`, `fog.density`, `fog.fogLower`, `fog.fogHigher`), and then calls `bindCommonUniforms` to set other uniforms.

The `drawChunksIndirect` function draws chunks indirectly by iterating over the provided chunk IDs, binding buffers for each LOD level, and calling `drawChunksOfLod`. The `drawChunksOfLod` function handles the detailed drawing process for a specific LOD level. It uploads chunk IDs to the buffer, allocates command buffer space, binds the command pipeline, sets uniforms such as LOD distance (`commandUniforms.lodDistance`), chunk ID index (`commandUniforms.chunkIDIndex`), command index start (`commandUniforms.commandIndexStart`), size (`commandUniforms.size`), and whether it is transparent (`commandUniforms.isTransparent`). It then dispatches compute shaders for non-transparent chunks, performs memory barriers, binds the appropriate shader, and executes draw calls using `glMultiDrawElementsIndirect`. For occlusion tests, it binds the occlusion test pipeline, sets player position uniforms, and draws elements. Finally, it redraws previously invisible chunks if necessary.

## Code Example
```zig
pub fn deinit() void {
	pipeline.deinit();
	transparentPipeline.deinit();
	occlusionTestPipeline.deinit();
	commandPipeline.deinit();
	vao.deinit();
	for (0..settings.highestSupportedLod + 1) |i| {
		faceBuffers[i].deinit();
		lightBuffers[i].deinit();
	}
	chunkBuffer.deinit();
	commandBuffer.deinit();
	chunkIDBuffer.deinit();
}
```

## Related Questions
- What is the purpose of the `deinit` function in this chunk?
- How does the `beginRender` function prepare for rendering?
- What uniforms are set by the `bindCommonUniforms` function?
- How are shaders bound and their uniforms set in this chunk?
- What is the process for drawing chunks indirectly?
- How does occlusion testing work in this chunk?

*Source: unknown | chunk_id: codebase_src_renderer_chunk_meshing.zig_chunk_1*
