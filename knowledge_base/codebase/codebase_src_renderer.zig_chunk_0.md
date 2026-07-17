# [hard/codebase_src_renderer.zig] - Chunk 0

**Type:** implementation
**Keywords:** deferred rendering, framebuffer management, shader initialization, projection matrix update, reflection mapping
**Symbols:** maximumMeshTime, zNear, zFar, deferredRenderPassPipeline, deferredUniforms, fakeReflectionPipeline, fakeReflectionUniforms, activeFrameBuffer, reflectionCubeMapSize, reflectionCubeMap, init, deinit, initReflectionCubeMap, worldFrameBuffer, lastWidth, lastHeight, lastFov, updateFov, updateViewport, chunk_meshing, lighting, mesh_storage
**Concepts:** chunk meshing, lighting, mesh storage, graphics pipelines, framebuffers, reflection cube maps

## Summary
The renderer module initializes and manages graphics pipelines, framebuffers, and reflection cube maps for rendering the game world.

## Explanation
This chunk defines the core rendering logic for the Cubyz engine. It imports various modules related to graphics, blocks, chunks, entities, particles, and settings. The `init` function sets up several graphics pipelines, including deferred render pass and fake reflection pipelines, initializes framebuffers, and prepares a reflection cube map. The `deinit` function cleans up these resources. The `updateFov` and `updateViewport` functions adjust the projection matrix based on field of view and viewport dimensions, respectively. The chunk also includes internal functions like `initReflectionCubeMap` for setting up the reflection cube map texture.

## Code Example
```zig
pub fn init() void {
	deferredRenderPassPipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/deferred_render_pass.vert",
		"assets/cubyz/shaders/deferred_render_pass.frag",
		"",
		&deferredUniforms,
		graphics.draw.SimpleVertex2D,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.noBlending}},
	);
	fakeReflectionPipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/fake_reflection.vert",
		"assets/cubyz/shaders/fake_reflection.frag",
		"",
		&fakeReflectionUniforms,
		graphics.draw.SimpleVertex2D,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.noBlending}},
	);
	worldFrameBuffer.init(true, c.GL_NEAREST, c.GL_CLAMP_TO_EDGE);
	worldFrameBuffer.updateSize(Window.width, Window.height, c.GL_RGB16F);
	Bloom.init();
	MeshSelection.init();
	MenuBackGround.init();
	Skybox.init();
	chunk_meshing.init();
	mesh_storage.init();
	reflectionCubeMap = .init();
	reflectionCubeMap.generate(reflectionCubeMapSize, reflectionCubeMapSize);
	initReflectionCubeMap();
}
```

## Related Questions
- What is the purpose of the `init` function in the renderer module?
- How does the `updateFov` function adjust the projection matrix?
- What are the key components initialized by the `init` function?
- How is the reflection cube map generated and used?
- What resources are cleaned up by the `deinit` function?
- What is the role of the deferred render pass pipeline in rendering?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_0*
