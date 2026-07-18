# [medium/codebase_src_entitySystem_modelRenderer.zig] - Chunk 1

**Type:** api
**Keywords:** graphics pipeline, node buffer, uniforms, HUD, transformation matrices, OpenGL commands
**Symbols:** client, client.pipeline, client.nodeBuffer, client.uniforms, client.init, client.deinit, client.clear, client.renderHud, client.render, server, server.init, server.deinit, server.update
**Concepts:** entity rendering, HUD rendering, model transformation, OpenGL drawing

## Summary
Handles rendering of entities in the client, including HUD and model rendering.

## Explanation
The `client` struct manages entity rendering on the client side. It initializes a graphics pipeline and a node buffer for storing transformation matrices. The `init` function sets up the shader pipeline and allocates memory for the node buffer. The `deinit` function cleans up resources. The `renderHud` function renders entity names and icons on the HUD, calculating positions based on player position and camera view. The `render` function processes model components, updates transformation matrices, and uploads them to the GPU. It then binds textures and light data before drawing entities using OpenGL commands.

## Code Example
```zig
pub fn deinit() void {
	pipeline.deinit();
	nodeBuffer.deinit();
}
```

## Related Questions
- What is the purpose of the `client.init` function?
- How does the `renderHud` function calculate entity positions on the screen?
- What resources are cleaned up in the `deinit` function?
- How are transformation matrices updated for each entity in the `render` function?
- What OpenGL commands are used to draw entities in the `render` function?
- How is the node buffer managed during rendering?

*Source: unknown | chunk_id: codebase_src_entitySystem_modelRenderer.zig_chunk_1*
