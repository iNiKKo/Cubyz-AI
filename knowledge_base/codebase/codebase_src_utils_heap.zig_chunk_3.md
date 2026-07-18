# [hard/codebase_src_utils_heap.zig] - Chunk 3

**Type:** documentation
**Keywords:** allocator, unreachable, memory management, error-free operations, arena allocator
**Symbols:** NeverFailingAllocator, NeverFailingAllocator.allocator, NeverFailingAllocator.Alignment, NeverFailingAllocator.math, NeverFailingAllocator.rawAlloc, NeverFailingAllocator.rawResize, NeverFailingAllocator.rawRemap, NeverFailingAllocator.rawFree, NeverFailingAllocator.create, NeverFailingAllocator.destroy, NeverFailingAllocator.alloc, NeverFailingAllocator.allocWithOptions, NeverFailingAllocator.allocWithOptionsRetAddr, NeverFailingAllocator.AllocWithOptionsPayload, NeverFailingAllocator.allocSentinel, NeverFailingAllocator.alignedAlloc, NeverFailingAllocator.allocAdvancedWithRetAddr, NeverFailingAllocator.allocWithSizeAndAlignment, NeverFailingAllocator.allocBytesWithAlignment, NeverFailingAllocator.resize, NeverFailingAllocator.remap, NeverFailingAllocator.realloc, NeverFailingAllocator.reallocAdvanced, NeverFailingAllocator.free, NeverFailingAllocator.dupe, NeverFailingAllocator.dupeZ, NeverFailingAllocator.createArena, NeverFailingAllocator.destroyArena
**Concepts:** Memory Allocation, Error Handling, Wrappers, Allocators

## Summary
Defines a wrapper for an allocator that ensures all operations never fail, using `unreachable` to handle any errors.

## Explanation
The `NeverFailingAllocator` struct wraps another allocator and provides methods that call the underlying allocator's functions. If any operation fails (throws an error), it immediately calls `unreachable`, indicating a programming error. The wrapper includes methods for creating, destroying, allocating, resizing, remapping, reallocating, freeing memory, duplicating arrays, and managing arenas. It ensures that all operations are guaranteed to succeed, simplifying the code that uses this allocator by removing the need for error handling.

## Code Example
```zig
fn rawAlloc(a: NeverFailingAllocator, len: usize, alignment: Alignment, ret_addr: usize) ?[*]u8 {
		return a.allocator.vtable.alloc(a.allocator.ptr, len, alignment, ret_addr);
	}
```

## Related Questions
- How does NeverFailingAllocator handle memory allocation errors?
- What methods are provided by NeverFailingAllocator for managing memory?
- Can you explain the purpose of the `createArena` and `destroyArena` methods in NeverFailingAllocator?
- How does NeverFailingAllocator ensure that all operations never fail?
- What is the difference between `resize`, `remap`, and `realloc` in NeverFailingAllocator?
- How does NeverFailingAllocator handle memory duplication with null-termination?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_3*
