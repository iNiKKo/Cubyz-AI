# [hard/codebase_src_graphics.zig] - Chunk 11

**Type:** implementation
**Keywords:** vulkanTestingMode, VkAttachmentDescription, VK_IMAGE_LAYOUT_PRESENT_SRC_KHR, GL_STATIC_DRAW, glGenVertexArrays, glVertexAttribPointer, comptime switch, shader storage buffer, memory ownership, error handling, conditional initialization, vertex attribute binding, binary serialization, OpenGL API calls, Vulkan device context
**Symbols:** deinitRenderPasses, RenderPass, VertexArray, EmptyVertex, SSBO
**Concepts:** Vulkan render pass creation, OpenGL vertex array storage, shader storage buffers, vertex attribute binding, binary serialization, memory ownership, error handling, conditional initialization

## Summary
This chunk defines Vulkan render pass creation and OpenGL vertex array storage structures.

## Explanation
The deinitRenderPasses function conditionally calls renderToWindow.deinit when vulkanTestingMode is enabled. The RenderPass struct contains init, deinit methods that create/destroy VkRenderPass objects via vkCreateRenderPass/vkDestroyRenderPass with a color attachment configured for VK_IMAGE_LAYOUT_PRESENT_SRC_KHR final layout and VK_ATTACHMENT_STORE_OP_STORE store operation. VertexArray holds vao, vbo, ibo fields; EmptyVertex provides an attributeDescriptions array of zero elements. init(T, data, indices_) allocates VAO/VBO via glGenVertexArrays/glGenBuffers, binds them, uploads vertex data with GL_STATIC_DRAW, conditionally creates IBO if indices_ is provided, then enables vertex attributes by iterating over T.attributeDescriptions (asserting binding==0), mapping VkFormat to GL types and sizes via comptime switches, calling glVertexAttribPointer or glVertexAttribIPointer depending on glType, finally unbinding VAO. deinit deletes VAO/VBO/IBO if present; bind rebinds the VAO. SSBO holds bufferID; init allocates a shader storage buffer with glGenBuffers; initStatic and initStaticSize allocate buffers with GL_SHADER_STORAGE_BUFFER target and call glBufferStorage (with data.ptr or null depending on constructor), returning self; deinit deletes the buffer.

## Code Example
```zig
pub fn deinit(self: RenderPass) void {
	c.vkDestroyRenderPass(vulkan.device, self.renderPass, null);
}
```

## Related Questions
- What Vulkan layout is used for the final image state in RenderPass?
- How does VertexArray handle optional index data during initialization?
- Which OpenGL buffer target is used when creating SSBO via initStatic?
- What assertion is performed on vertex attribute descriptions before enabling them?
- Under what condition does deinitRenderPasses call renderToWindow.deinit?
- Does RenderPass store the VkRenderPass handle in a named field?
- How are GL types derived from VkFormat values in VertexArray.init?
- Is there any cleanup logic for SSBO when bufferID is undefined?
- What happens to ibo if indices_ is null during VertexArray init?
- Are vertex attributes bound with normalized or non-normalized coordinates?
- Which Vulkan structure type constant is used for render pass creation info?
- How does the code ensure VAO is unbound before returning from init?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_11*
