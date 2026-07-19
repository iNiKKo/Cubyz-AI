# [hard/codebase_src_renderer.zig] - Chunk 0

**Type:** implementation
**Keywords:** pipeline initialization, framebuffer setup, shader programs, uniforms binding, cubemap generation, rendering lifecycle
**Symbols:** maximumMeshTime, zNear, zFar, deferredRenderPassPipeline, deferredUniforms, fakeReflectionPipeline, fakeReflectionUniforms, activeFrameBuffer, reflectionCubeMapSize, reflectionCubeMap, init, deinit, initReflectionCubeMap, worldFrameBuffer, chunk_meshing, lighting, mesh_storage
**Concepts:** chunk meshing, lighting, mesh storage, deferred rendering, fake reflections, framebuffer management, reflection cube map

## Summary
Handles renderer initialization and deinitialization, manages rendering pipelines, framebuffers, and reflection cube maps.

## Explanation
This chunk defines the renderer's core setup and teardown processes. It initializes various rendering pipelines for deferred rendering and fake reflections using shader programs from specified asset paths (`assets/cubyz/shaders/deferred_render_pass.vert`, `assets/cubyz/shaders/deferred_render_pass.frag`, `assets/cubyz/shaders/fake_reflection.vert`, `assets/cubyz/shaders/fake_reflection.frag`). Framebuffers are set up for world rendering with specific texture formats and filtering options (`GL_RGB16F`), and a reflection cube map is generated to simulate water reflections, initialized by drawing a rectangle across each face of the cube map. The chunk also manages the lifecycle of other renderer components like Bloom, MeshSelection, MenuBackGround, and Skybox.

The `maximumMeshTime` constant is set to 12 milliseconds, allowing the game to run smoother on movement. The near and far clipping planes for the camera are defined as `zNear = 0.1` and `zFar = 65536.0`. The reflection cube map size is set to 64.

The deferred render pass pipeline uses the following uniform variables: `fog.color`, `fog.density`, `fog.fogLower`, `fog.fogHigher`, `tanXY`, `zNear`, `zFar`, `invViewMatrix`, `playerPositionInteger`, and `playerPositionFraction`. The fake reflection pipeline uses the following uniform variables: `normalVector`, `upVector`, `rightVector`, `frequency`, and `reflectionMapSize`.

## Code Example
```zig
pub fn deinit() void {
	deferredRenderPassPipeline.deinit();
	fakeReflectionPipeline.deinit();
	worldFrameBuffer.deinit();
	Bloom.deinit();
	MeshSelection.deinit();
	MenuBackGround.deinit();
	Skybox.deinit();
	mesh_storage.deinit();
	chunk_meshing.deinit();
	reflectionCubeMap.deinit();
}
```

## Related Questions
- What is the maximum time allowed for chunk mesh creation?
- How are deferred rendering and fake reflection pipelines initialized?
- What are the dimensions of the world framebuffer?
- How is the reflection cube map generated?
- What components are deinitialized during the renderer's shutdown process?
- What uniform variables are used in the deferred render pass pipeline?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_0*
