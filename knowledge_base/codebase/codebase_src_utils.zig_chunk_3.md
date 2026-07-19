# [hard/codebase_src_utils.zig] - Chunk 3

**Type:** implementation
**Keywords:** circular buffer, fixed size, bitwise operations, memory allocation, slice manipulation
**Symbols:** FixedSizeCircularBuffer, FixedSizeCircularBuffer.mem, FixedSizeCircularBuffer.startIndex, FixedSizeCircularBuffer.len, FixedSizeCircularBuffer.init, FixedSizeCircularBuffer.deinit, FixedSizeCircularBuffer.peekBack, FixedSizeCircularBuffer.peekFront, FixedSizeCircularBuffer.pushBack, FixedSizeCircularBuffer.forcePushBack, FixedSizeCircularBuffer.pushBackAssumeCapacity, FixedSizeCircularBuffer.pushFront, FixedSizeCircularBuffer.pushFrontAssumeCapacity, FixedSizeCircularBuffer.forcePushFront, FixedSizeCircularBuffer.pushBackSlice, FixedSizeCircularBuffer.insertSliceAtOffset, FixedSizeCircularBuffer.popBack, FixedSizeCircularBuffer.popFront, FixedSizeCircularBuffer.popSliceFront, FixedSizeCircularBuffer.discardElementsFront, FixedSizeCircularBuffer.getAtOffset
**Concepts:** circular buffer, memory management, dynamic array operations

## Summary
Defines a fixed-size circular buffer with methods for initialization, deinitialization, and various operations like push, pop, peek, and slice manipulation.

## Explanation
The chunk defines a generic `FixedSizeCircularBuffer` type that manages a circular buffer of elements of type `T` with a fixed capacity. The capacity must be a power of two, as indicated by the assertion `std.debug.assert(capacity - 1 & capacity == 0 and capacity > 0);`. This allows for efficient index management using bitwise operations. The buffer includes methods for initializing (`init`) and deinitializing (`deinit`) the buffer, as well as operations to add (`pushBack`, `forcePushBack`, `pushFront`, `forcePushFront`) and remove (`popBack`, `popFront`, `popSliceFront`) elements. The buffer supports peeking at front or back elements without removing them (`peekFront`, `peekBack`). It also provides methods for inserting slices of elements at specific offsets (`insertSliceAtOffset`), pushing entire slices to the back (`pushBackSlice`), and accessing elements by offset (`getAtOffset`). Memory management is handled through an allocator, ensuring that the buffer can dynamically allocate and deallocate its storage. The `forcePushBack` method adds an element to the back of the buffer, removing the front element if the buffer is full, and returns the removed element. Similarly, the `forcePushFront` method adds an element to the front of the buffer, removing the back element if the buffer is full, and returns the removed element.

## Code Example
```zig
pub fn peekBack(self: Self) ?T {
	if (self.len == 0) return null;
	return self.mem[self.startIndex + self.len - 1 & mask];
}
```

## Related Questions
- How is the circular buffer initialized?
- What happens if you try to push an element when the buffer is full?
- How does the `peekFront` method work?
- Can elements be inserted at a specific offset in the buffer?
- What is the purpose of the `forcePushBack` method?
- How are elements removed from the front of the buffer?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_3*
