# [hard/codebase_src_graphics.zig] - Chunk 14

**Type:** implementation
**Keywords:** OpenGL, SSBO, memory allocation, fence synchronization, buffer mapping
**Symbols:** LargeBuffer, LargeBuffer.ssbo, LargeBuffer.freeBlocks, LargeBuffer.fences, LargeBuffer.fencedFreeLists, LargeBuffer.activeFence, LargeBuffer.capacity, LargeBuffer.used, LargeBuffer.binding, LargeBuffer.createBuffer, LargeBuffer.init, LargeBuffer.deinit, LargeBuffer.beginRender, LargeBuffer.endRender, LargeBuffer.rawAlloc, LargeBuffer.finalFree, LargeBuffer.free, LargeBuffer.allocateAndMapRange, LargeBuffer.unmapRange, LargeBuffer.uploadData
**Concepts:** shader storage buffer objects (SSBOs), dynamic memory allocation, GPU synchronization, buffer management

## Summary
Defines a LargeBuffer struct for managing shader storage buffer objects (SSBOs) with dynamic allocation and deallocation of sub-regions.

## Explanation
The LargeBuffer struct is designed to handle large shader storage buffer objects (SSBOs) by allocating and freeing smaller regions within it. It uses OpenGL functions to manage the buffer's lifecycle, including creation, binding, and synchronization with GPU operations. The struct maintains a list of free blocks and fenced lists for managing allocations that are safe to reuse after certain GPU commands have completed.

Key methods include:
- `init`: Initializes the buffer, setting up fences and free lists. It sets the initial capacity, used space, and binding. Fences are created using `glFenceSync` with the flag `GL_SYNC_GPU_COMMANDS_COMPLETE`.
- `deinit`: Cleans up resources by deleting sync objects and deinitializing lists.
- `beginRender` and `endRender`: Manage fences to ensure that memory is safe to reuse after GPU operations have completed. `beginRender` increments the active fence index, processes fenced free lists, and waits for synchronization using `glClientWaitSync`. `endRender` deletes the current fence and creates a new one.
- `rawAlloc`: Allocates memory for a new allocation, resizing the buffer if necessary. When resizing, it doubles the capacity, copies existing data to the new buffer, and frees the old one. The buffer size is limited by OpenGL's 2 GiB limit.
- `finalFree`: Finalizes deallocation by merging adjacent free blocks.
- `free`: Queues deallocations for later processing.
- `allocateAndMapRange`: Maps a region of the buffer for writing, ensuring synchronization with GPU operations. It uses `glMapBufferRange` with flags `GL_MAP_WRITE_BIT` and `GL_MAP_INVALIDATE_RANGE_BIT` to map the buffer range.
- `unmapRange`: Unmaps the buffer after use using `glUnmapBuffer`.
- `uploadData`: Uploads data to the buffer, handling memory allocation and mapping. It uses `glMapBufferRange` with flags `GL_MAP_WRITE_BIT` and `GL_MAP_INVALIDATE_RANGE_BIT` to map the buffer range and then copies data using `@memcpy`.

The struct ensures that memory is efficiently managed and reused while maintaining synchronization with GPU operations. When the buffer runs out of space, it resizes by doubling its capacity, copying existing data to the new buffer, and freeing the old one. The `createBuffer` method initializes the buffer with specified size and flags, including `GL_MAP_WRITE_BIT` and `GL_DYNAMIC_STORAGE_BIT`, which allow for dynamic storage and writing operations. Fences are used to synchronize buffer access, ensuring that memory is only reused after GPU commands have completed.

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
