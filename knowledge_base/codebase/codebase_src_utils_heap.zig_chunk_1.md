# [hard/codebase_src_utils_heap.zig] - Chunk 1

**Type:** api
**Keywords:** allocator, OutOfMemory, panic, memory allocation, error handling
**Symbols:** ErrorHandlingAllocator, ErrorHandlingAllocator.backingAllocator, ErrorHandlingAllocator.init, ErrorHandlingAllocator.allocator, ErrorHandlingAllocator.handleError, alloc, resize, remap, free
**Concepts:** memory management, error handling, allocation

## Summary
This chunk defines an allocator that handles OutOfMemory situations by panicking or freeing memory, making it safe to ignore errors.

## Explanation
The chunk contains the implementation of `ErrorHandlingAllocator`, which wraps another allocator and provides error handling for allocation failures. It includes methods for allocation (`alloc`), resizing (`resize`), remapping (`remap`), and freeing memory (`free`). The `handleError` function is called when an allocation fails, causing a panic with a descriptive message.

## Code Example
```zig
fn handleError() noreturn {
	@panic("Out Of Memory. Please download more RAM, reduce the render distance, or close some of your 100 browser tabs.");
}
```

## Related Questions
- How does the `ErrorHandlingAllocator` handle allocation failures?
- What is the purpose of the `handleError` function in this chunk?
- Which methods are provided by the `ErrorHandlingAllocator` for memory management?
- What happens if an allocation fails when using the `ErrorHandlingAllocator`?
- How does the `resize` method work in the `ErrorHandlingAllocator`?
- Can you explain the role of the `remap` method in this allocator?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_1*
