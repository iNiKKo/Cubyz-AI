# [hard/codebase_src_utils_heap.zig] - Chunk 2

**Type:** api
**Keywords:** allocator, out of memory, panic, vtable, delegation
**Symbols:** ErrorHandlingAllocator, ErrorHandlingAllocator.backingAllocator, ErrorHandlingAllocator.init, ErrorHandlingAllocator.allocator, ErrorHandlingAllocator.handleError, ErrorHandlingAllocator.alloc, ErrorHandlingAllocator.resize, ErrorHandlingAllocator.remap, ErrorHandlingAllocator.free
**Concepts:** memory management, error handling, allocator wrapper

## Summary
The `ErrorHandlingAllocator` struct provides an allocator that handles OutOfMemory situations by panicking or freeing memory, making it safe to ignore errors.

## Explanation
The `ErrorHandlingAllocator` struct provides an allocator that handles OutOfMemory situations by panicking or freeing memory, making it safe to ignore errors. It wraps another allocator and overrides its allocation methods (`alloc`, `resize`, `remap`, `free`) to handle out-of-memory conditions by panicking. The `alloc` method attempts to allocate a specified number of bytes with a given alignment and returns a pointer to the allocated memory or null if the allocation fails, in which case it calls `handleError`. The `resize` method attempts to expand or shrink memory in place, returning true if successful and false otherwise. The `remap` method attempts to expand or shrink memory, allowing relocation, and returns a non-null pointer to the new memory location if successful or null if the resize would be equivalent to allocating new memory, copying the bytes from the old memory, and then freeing the old memory. The `free` method frees and invalidates a region of memory. It uses a vtable to define the allocator interface and delegates most operations to the backing allocator, only adding error handling in the `alloc` method.

## Code Example
```zig
fn handleError() noreturn {
	@panic("Out Of Memory. Please download more RAM, reduce the render distance, or close some of your 100 browser tabs.");
}
```

## Related Questions
- What is the purpose of the `ErrorHandlingAllocator` struct?
- How does the `ErrorHandlingAllocator` handle out-of-memory situations?
- Which methods are overridden in the `ErrorHandlingAllocator` to add error handling?
- What happens if an allocation fails with the `ErrorHandlingAllocator`?
- How is the `backingAllocator` used within the `ErrorHandlingAllocator`?
- What does the `handleError` function do in the `ErrorHandlingAllocator`?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_2*
