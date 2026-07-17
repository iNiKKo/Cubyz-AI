# [hard/codebase_src_utils.zig] - Chunk 3

**Type:** implementation
**Keywords:** circular buffer, queue, memory allocation, out-of-memory handling, element insertion, element removal
**Symbols:** CircularBufferQueue, CircularBufferQueue.mem, CircularBufferQueue.mask, CircularBufferQueue.startIndex, CircularBufferQueue.len, CircularBufferQueue.allocator, CircularBufferQueue.init, CircularBufferQueue.deinit, CircularBufferQueue.reset, CircularBufferQueue.increaseCapacity, CircularBufferQueue.pushBack, CircularBufferQueue.forcePushBack, CircularBufferQueue.pushBackAssumeCapacity, CircularBufferQueue.pushFront, CircularBufferQueue.pushFrontAssumeCapacity, CircularBufferQueue.forcePushFront, CircularBufferQueue.pushBackSlice, CircularBufferQueue.insertSliceAtOffset, CircularBufferQueue.popBack, CircularBufferQueue.popFront, CircularBufferQueue.popSliceFront, CircularBufferQueue.discardElementsFront, CircularBufferQueue.getAtOffset
**Concepts:** circular buffer, queue operations, memory management, capacity expansion

## Summary
This chunk defines a circular buffer queue with various operations for adding and removing elements, including handling memory capacity expansion.

## Explanation
The code defines a `CircularBufferQueue` struct that implements a circular buffer using a fixed-size array. It includes methods for pushing and popping elements from both ends of the queue, as well as inserting slices at specific offsets. The `init` method initializes the buffer with a specified capacity, and the `deinit` method frees the allocated memory. The `increaseCapacity` function doubles the buffer's size when it becomes full. The code handles out-of-memory conditions by returning errors where appropriate.

## Code Example
```zig
pub fn pushBack(self: *Self, elem: T) !void {
	if (self.len >= capacity) return error.OutOfMemory;
	self.pushBackAssumeCapacity(elem);
}
```

## Related Questions
- How does the `CircularBufferQueue` handle out-of-memory conditions?
- What is the purpose of the `increaseCapacity` method in the `CircularBufferQueue`?
- How does the `pushBackSlice` method work in the `CircularBufferQueue`?
- What is the role of the `mask` field in the `CircularBufferQueue` struct?
- How do you initialize a `CircularBufferQueue` with a specific capacity?
- What methods are available for adding elements to the front of the `CircularBufferQueue`?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_3*
