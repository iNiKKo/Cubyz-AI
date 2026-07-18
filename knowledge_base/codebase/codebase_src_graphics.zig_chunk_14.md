# [hard/codebase_src_graphics.zig] - Chunk 14

**Type:** implementation
**Keywords:** OpenGL, SSBO, memory allocation, fence synchronization, buffer mapping
**Symbols:** LargeBuffer, LargeBuffer.ssbo, LargeBuffer.freeBlocks, LargeBuffer.fences, LargeBuffer.fencedFreeLists, LargeBuffer.activeFence, LargeBuffer.capacity, LargeBuffer.used, LargeBuffer.binding, LargeBuffer.createBuffer, LargeBuffer.init, LargeBuffer.deinit, LargeBuffer.beginRender, LargeBuffer.endRender, LargeBuffer.rawAlloc, LargeBuffer.finalFree, LargeBuffer.free, LargeBuffer.allocateAndMapRange, LargeBuffer.unmapRange, LargeBuffer.uploadData
**Concepts:** shader storage buffer objects (SSBOs), dynamic memory allocation, GPU synchronization, buffer management

## Summary
Defines a LargeBuffer struct for managing shader storage buffer objects (SSBOs) with dynamic allocation and deallocation of sub-regions.

## Explanation
The LargeBuffer struct is designed to handle large SSBOs by allocating and freeing smaller regions within it. It uses OpenGL functions to manage the buffer's lifecycle, including creation, binding, and synchronization with GPU operations. The struct maintains a list of free blocks and fenced lists for managing allocations that are safe to reuse after certain GPU commands have completed. Key methods include `init` for initialization, `deinit` for cleanup, `beginRender` and `endRender` for managing fences, `rawAlloc` for allocating memory, `finalFree` for finalizing deallocation, `free` for queuing deallocations, `allocateAndMapRange` for mapping a region of the buffer for writing, `unmapRange` for unmapping the buffer after use, and `uploadData` for uploading data to the buffer. The struct ensures that memory is efficiently managed and reused while maintaining synchronization with GPU operations.

## Code Example
```zig
fn createBuffer(self: *Self, size: u31) void {
	self.ssbo = .init();
	c.glBindBuffer(c.GL_SHADER_STORAGE_BUFFER, self.ssbo.bufferID);
	const flags = c.GL_MAP_WRITE_BIT | c.GL_DYNAMIC_STORAGE_BIT;
	const bytes = @as(c.GLsizeiptr, size)*@sizeOf(Entry);
	c.glBufferStorage(c.GL_SHADER_STORAGE_BUFFER, bytes, null, flags);
	self.ssbo.bind(self.binding);
	self.capacity = size;
}
```

## Related Questions
- What is the purpose of the `createBuffer` method in the LargeBuffer struct?
- How does the LargeBuffer struct handle buffer resizing when it runs out of space?
- What role do fences play in the LargeBuffer's operation?
- How does the LargeBuffer manage memory allocation and deallocation?
- What is the function of the `allocateAndMapRange` method in the LargeBuffer struct?
- How does the LargeBuffer ensure synchronization with GPU operations?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_14*
