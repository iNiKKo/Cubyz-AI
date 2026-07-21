# [hard/codebase_src_renderer.zig] - Chunk 9

**Type:** implementation
**Keywords:** OpenGL, uniforms, VAOs, block breaking, selection rendering
**Symbols:** updateBlockAndSendUpdate, drawCube, render
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
Handles rendering of selected blocks and cubes in the game world.

## Explanation
This chunk contains functions for drawing cubes and handling block breaking animations. The `drawCube` function sets up OpenGL uniforms such as model position, lower bounds, upper bounds, and line size, and draws a cube using vertex array objects (VAOs). The `updateBlockAndSendUpdate` function updates the block at a given position and sends an update to the server, including details about the source inventory, slot, position, old block, and new block. The `render` function checks if the GUI is hidden and then calls `drawCube` to render selected blocks or areas based on player selection positions. Specifically, it calculates the relative position of the cube to be drawn by subtracting the player's position from the selected block position and uses this to set the model position uniform in `drawCube`. The function also handles rendering of selected areas by determining the bottom-left and top-right corners of the area based on the player's selection positions.

## Code Example
```zig
pub fn drawCube(projectionMatrix: Mat4f, viewMatrix: Mat4f, relativePositionToPlayer: Vec3d, min: Vec3f, max: Vec3f) void {
	pipeline.bind(null);

	c.glUniformMatrix4fv(uniforms.projectionMatrix, 1, c.GL_TRUE, @ptrCast(&projectionMatrix));
	c.glUniformMatrix4fv(uniforms.viewMatrix, 1, c.GL_TRUE, @ptrCast(&viewMatrix));

	c.glUniform3f(
		uniforms.modelPosition,
		@floatCast(relativePositionToPlayer[0]),
		@floatCast(relativePositionToPlayer[1]),
		@floatCast(relativePositionToPlayer[2]),
	);
	c.glUniform3f(uniforms.lowerBounds, min[0], min[1], min[2]);
	c.glUniform3f(uniforms.upperBounds, max[0], max[1], max[2]);
	c.glUniform1f(uniforms.lineSize, 1.0/128.0);

	main.renderer.chunk_meshing.vao.bind();
	c.glDrawElements(c.GL_TRIANGLES, 12*6*6, c.GL_UNSIGNED_INT, null);
}
```

## Related Questions
- What specific OpenGL uniforms are set up in the `drawCube` function?
- How does the `render` function determine what blocks or areas to render based on player selection?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_9*
