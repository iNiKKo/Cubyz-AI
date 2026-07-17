# [hard/codebase_src_graphics.zig] - Chunk 13

**Type:** api
**Keywords:** OpenGL, buffer management, frame buffer, shader storage buffer, memory allocation, resource cleanup
**Symbols:** endRender, rawAlloc, finalFree, free, allocateAndMapRange, unmapRange, uploadData, FrameBuffer, FrameBuffer.frameBuffer, FrameBuffer.texture, FrameBuffer.hasDepthTexture, FrameBuffer.depthTexture, init, deinit
**Concepts:** OpenGL resource management, buffer allocation, frame buffer creation, shader storage buffer

## Summary
This chunk defines functions for managing OpenGL resources such as frame buffers and shader storage buffers.

## Explanation
The chunk contains several functions related to OpenGL resource management. `endRender` deletes a fence sync object and creates a new one. `rawAlloc` allocates memory from a buffer, resizing if necessary. `finalFree` merges freed allocations with adjacent free blocks. `free` adds an allocation to a fenced list for later processing. `allocateAndMapRange` allocates and maps a range of the buffer for writing. `unmapRange` unmaps a previously mapped buffer range. `uploadData` uploads data to a buffer, allocating space if needed. The `FrameBuffer` struct manages OpenGL frame buffers, including initialization and cleanup.

## Code Example
```zig
pub fn endRender(self: *Self) void {
	c.glDeleteSync(self.fences[self.activeFence]);
	self.fences[self.activeFence] = c.glFenceSync(c.GL_SYNC_GPU_COMMANDS_COMPLETE, 0);
}
```

## Related Questions
- How does the `endRender` function work?
- What is the purpose of the `rawAlloc` function?
- Describe the role of the `finalFree` function.
- Explain how the `allocateAndMapRange` function works.
- What steps are involved in initializing a frame buffer?
- How does the `uploadData` function handle data upload to a buffer?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_13*
