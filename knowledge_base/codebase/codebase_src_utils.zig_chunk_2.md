# [hard/codebase_src_utils.zig] - Chunk 2

**Type:** implementation
**Keywords:** array initialization, memory allocation, element access, buffer overflow handling, circular data structure
**Symbols:** Array2D, Array2D.init, Array2D.deinit, Array2D.get, Array2D.getRow, Array2D.set, Array2D.ptr, Array3D, Array3D.init, Array3D.deinit, Array3D.get, Array3D.set, Array3D.ptr, Array3D.clone, FixedSizeCircularBuffer, FixedSizeCircularBuffer.init, FixedSizeCircularBuffer.deinit, FixedSizeCircularBuffer.peekBack, FixedSizeCircularBuffer.peekFront, FixedSizeCircularBuffer.pushBack, FixedSizeCircularBuffer.forcePushBack, FixedSizeCircularBuffer.pushBackAssumeCapacity, FixedSizeCircularBuffer.pushFront, FixedSizeCircularBuffer.pushFrontAssumeCapacity, FixedSizeCircularBuffer.forcePushFront
**Concepts:** 2D array management, 3D array management, circular buffer

## Summary
This chunk defines utility types and functions for managing 2D and 3D arrays, as well as a fixed-size circular buffer.

## Explanation
The chunk includes three main components: Array2D, Array3D, and FixedSizeCircularBuffer. Array2D is a struct that represents a two-dimensional array of elements of type T, providing methods for initialization, deinitialization, accessing elements, setting elements, and getting pointers to elements. Array3D extends this concept to three dimensions with similar functionality. FixedSizeCircularBuffer is a circular buffer with a fixed capacity, offering methods for initialization, deinitialization, peeking at the front or back of the buffer, pushing elements to the front or back (with options to handle overflow), and force-pushing elements which may overwrite the oldest element if the buffer is full.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator, width: u32, height: u32) Self {
	return .{
		.mem = allocator.alloc(T, width*height),
		.width = width,
		.height = height,
	};
}
```

## Related Questions
- How do you initialize an Array2D?
- What is the purpose of the `deinit` method in Array3D?
- How does the FixedSizeCircularBuffer handle overflow when pushing elements?
- Can you explain how to access elements in a 3D array using Array3D?
- What is the difference between `pushBack` and `forcePushBack` in FixedSizeCircularBuffer?
- How do you clone an Array3D instance?

*Source: unknown | chunk_id: codebase_src_utils.zig_chunk_2*
