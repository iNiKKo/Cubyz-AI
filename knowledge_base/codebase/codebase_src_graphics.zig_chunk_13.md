# [hard/codebase_src_graphics.zig] - Chunk 13

**Type:** implementation
**Keywords:** OpenGL, vertex arrays, shader storage buffers, buffer initialization, data binding
**Symbols:** VertexArray, VertexArray.vao, VertexArray.vbo, VertexArray.ibo, VertexArray.EmptyVertex, VertexArray.init, VertexArray.deinit, VertexArray.bind, SSBO, SSBO.bufferID, SSBO.init, SSBO.initStatic, SSBO.initStaticSize, SSBO.deinit, SSBO.bind, SSBO.bufferData, SSBO.bufferSubData, SSBO.createDynamicBuffer, SubAllocation, SubAllocation.start, SubAllocation.len
**Concepts:** OpenGL resource management, Vertex array objects (VAOs), Shader storage buffers (SSBOs)

## Summary
Defines VertexArray and SSBO structures for managing OpenGL vertex arrays and shader storage buffers.

## Explanation
The chunk defines two main structures, VertexArray and SSBO, which are used to manage OpenGL resources such as vertex arrays and shader storage buffers. The VertexArray struct includes methods for initialization (init), cleanup (deinit), and binding (bind). It handles the creation of vertex array objects (VAOs), vertex buffer objects (VBOs), and index buffer objects (IBOs) if indices are provided. The SSBO struct provides similar functionality for shader storage buffers, including static and dynamic buffer initialization, data binding, and sub-data updates. Both structures use OpenGL functions to interact with the graphics API.

The VertexArray.init function generates a VAO and VBO, binds them, and uploads vertex data using glBufferData. If indices are provided, it also generates an IBO and uploads index data. The VertexArray.deinit function deletes the VAO, VBO, and IBO if present. The VertexArray.bind function binds the VAO.

The SSBO.init function generates a buffer ID for shader storage buffers. The SSBO.initStatic function initializes a static buffer with provided data using glBufferStorage. The SSBO.initStaticSize function initializes a static buffer of a specified size without data using glBufferStorage. The SSBO.deinit function deletes the buffer using glDeleteBuffers. The SSBO.bind function binds the buffer to a specific binding point using glBindBufferBase. The SSBO.bufferData function updates the entire buffer with new data using glBufferData. The SSBO.bufferSubData function updates a portion of the buffer with new data using glBufferSubData. The SSBO.createDynamicBuffer function creates a dynamic buffer of a specified size using glBufferData.

## Code Example
```zig
pub fn deinit(self: VertexArray) void {
	c.glDeleteVertexArrays(1, &self.vao);
	c.glDeleteBuffers(1, &self.vbo);
	if (self.ibo != null) {
		c.glDeleteBuffers(1, &self.ibo.?);
	}
}
```

## Related Questions
- How do you initialize a VertexArray with indices?
- What is the purpose of the EmptyVertex struct in VertexArray?
- How does SSBO handle dynamic buffer creation?
- What OpenGL functions are used to manage shader storage buffers in SSBO?
- Can you explain how data is bound to an SSBO?
- What steps are involved in deinitializing a VertexArray?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_13*
