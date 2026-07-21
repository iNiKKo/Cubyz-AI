# [medium/codebase_src_entitySystem_modelRenderer.zig] - Chunk 1

**Type:** api
**Keywords:** graphics pipeline, node buffer, uniforms, HUD, transformation matrices, OpenGL commands
**Symbols:** client, client.pipeline, client.nodeBuffer, client.uniforms, client.init, client.deinit, client.clear, client.renderHud, client.render, server, server.init, server.deinit, server.update
**Concepts:** entity rendering, HUD rendering, model transformation, OpenGL drawing

## Summary
Handles rendering of entities in the client, including HUD and model rendering.

## Explanation
Handles rendering of entities in the client, including HUD and model rendering.

The `client` struct manages entity rendering on the client side. It initializes a graphics pipeline and a node buffer for storing transformation matrices. The `init` function sets up the shader pipeline using vertex and fragment shaders located at 'assets/cubyz/shaders/entity_vertex.vert' and 'assets/cubyz/shaders/entity_fragment.frag', respectively, and allocates memory for the node buffer with an initial size of 1 MB and a capacity of 15. The `deinit` function cleans up resources by deinitializing the pipeline and the node buffer.

The `renderHud` function renders entity names and icons on the HUD, calculating positions based on player position and camera view. It uses screen units to scale font sizes and projects entity positions onto the screen using the camera's view matrix and the projection matrix from the frame uniforms. The transparency of the text is calculated based on the distance from the player, and the text is rendered centered at the calculated screen coordinates.

The `render` function processes model components, updates transformation matrices, and uploads them to the GPU. It then binds textures and light data before drawing entities using OpenGL commands. Specifically, it sets the ambient light uniform with the provided `ambientLight` vector, sets the contrast uniform to 0.12, and uploads the node buffer data. For each entity, it calculates the model matrix based on the entity's position and rotation, updates the transformation matrices for each node, and binds the entity's texture. It then retrieves light values from the mesh storage and packs them into a single integer value before setting the light uniform. Finally, it sets the model view matrix uniform and draws the entity using `glDrawElements` with the triangle primitive mode.

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
