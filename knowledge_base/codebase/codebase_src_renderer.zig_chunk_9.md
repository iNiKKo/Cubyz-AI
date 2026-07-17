# [hard/codebase_src_renderer.zig] - Chunk 9

**Type:** implementation
**Keywords:** projection matrix, view matrix, model position uniform, lower bounds uniform, upper bounds uniform, line size uniform, cuboid selection, hide GUI flag, chunk meshing VAO, GL_UNSIGNED_INT indices
**Symbols:** drawCube, render
**Concepts:** cube rendering, selection box drawing, uniform binding, VBO/VAO usage, GL_TRIANGLES draw call

## Summary
This chunk implements the renderer's drawing pipeline: it defines a cube-drawing function that binds null pipelines and sets uniforms, then provides a render entry point that conditionally draws either a single selected block or a cuboid defined by two selection positions.

## Explanation
The chunk declares pub fn drawCube which receives projectionMatrix, viewMatrix, relativePositionToPlayer, min, max. It binds null via pipeline.bind(null), then sets uniforms: projectionMatrix and viewMatrix as 4x4 matrices (GL_TRUE flag), modelPosition as a Vec3f derived from the player-relative position, lowerBounds and upperBounds from the provided min/max vectors, and lineSize to 1/128. It binds main.renderer.chunk_meshing.vao and issues c.glDrawElements with GL_TRIANGLES, count 12*6*6 (432), type GL_UNSIGNED_INT, index null. The chunk also declares pub fn render which first checks main.gui.hideGui; if true it returns early. If selectedBlockPos is set, it computes the relative position by casting _selectedBlockPos to Vec3d and subtracting playerPos, then calls drawCube with selectionMin/selectionMax as bounds. Otherwise, if game.Player.selectionPosition1 and game.Player.selectionPosition2 are both set, it determines bottomLeft via @min(pos1,pos2) and topRight via @max(pos1,pos2). It then calls drawCube with bottomLeft cast to Vec3d minus playerPos for the position, lowerBounds as zero vector, and upperBounds computed from (topRight - bottomLeft + Vec3i{1,1,1}) cast to float. No other functions or public symbols are declared in this chunk.

## Related Questions
- What happens to drawCube when pipeline.bind(null) is called?
- How does render decide which geometry to draw based on selection state?
- What are the exact uniform names set by drawCube and their values?
- Why is lineSize set to 1.0/128.0 in drawCube?
- Which VAO is bound before issuing glDrawElements in this chunk?
- How does render compute the upper bounds when drawing a cuboid selection?
- What condition causes render to return early without drawing anything?
- Does drawCube ever use an index buffer or null indices, and what does that imply for the draw call?
- How are player-relative positions computed before being passed to drawCube?
- What is the purpose of casting selectedBlockPos to Vec3d in render?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_9*
