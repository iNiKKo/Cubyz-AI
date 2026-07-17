# [hard/codebase_src_utils_heap.zig] - Chunk 0

**Type:** implementation
**Keywords:** arena allocation, error handling allocator, stack-like buffer, thread-safe mutex locking, defer cleanup, aligned memory, allocation trailers, reference counting, NeverFailingAllocator, DebugAllocator
**Symbols:** testingErrorHandlingAllocator, testingAllocator, allocators, globalGpa, handledGpa, globalArenaAllocator, worldArenaAllocator, worldArenaOpenCount, worldArenaMutex, StackAllocator, AllocationTrailer, deinit, createWorldArena, destroyWorldArena, allocator, isInsideBuffer, indexInBuffer, getTrueAllocationEnd, getTrailerBefore, alloc, resize, remap, free
**Concepts:** arena allocation, error handling allocator, stack-like buffer, thread-safe mutex locking, defer cleanup, aligned memory, allocation trailers, reference counting via previousAllocationTrailer

## Summary
Defines global arena allocators with error handling and a stack-like StackAllocator providing fast, safe allocations via an internal buffer backed by NeverFailingAllocator.

## Explanation
The chunk declares pub const build_options imported from another module (not declared here), pub const main imported from another module (not declared here). It defines var testingErrorHandlingAllocator as a local variable inside the file scope, then exposes pub const testingAllocator derived from it. The allocators struct contains pub var globalGpa (DebugAllocator with thread_safe=true), pub var handledGpa (ErrorHandlingAllocator wrapping globalGpa), pub var globalArenaAllocator (NeverFailingArenaAllocator initialized from handledGpa), and a pub var worldArenaAllocator (NeverFailingArenaAllocator) that is undefined until created. It also defines local vars worldArenaOpenCount and worldArenaMutex inside allocators. The deinit function logs capacity of globalArenaAllocator, calls its deinit, sets it to undefined, checks if globalGpa.deinit returns .leak and logs an error, then sets globalGpa to undefined. createWorldArena locks worldArenaMutex via defer unlock, increments worldArenaOpenCount, and if count was zero initializes worldArenaAllocator from handledGpa. destroyWorldArena locks mutex, decrements count, and when count reaches zero logs capacity of worldArenaAllocator, calls its deinit, sets it to undefined. StackAllocator is a struct with fields backingAllocator (NeverFailingAllocator), buffer ([]align(4096) u8), index (usize). Its init function allocates the buffer via backingAllocator.alignedAlloc and returns an initialized instance. deinit checks if index != 0 and logs an error, then frees the buffer. allocator method constructs a NeverFailingAllocator vtable with pointers to alloc, resize, remap, free functions defined later; it sets ptr to self and includes an IAssertThatTheProvidedAllocatorCantFail empty struct. isInsideBuffer computes start/end of the backing buffer using @intFromPtr and compares pointer addresses. indexInBuffer similarly computes offset within the buffer. getTrueAllocationEnd aligns forward to the size of AllocationTrailer (packed struct with wasFreed bool and previousAllocationTrailer u31) and adds that size. getTrailerBefore subtracts AllocationTrailer size from end to obtain a casted pointer into the buffer. alloc casts ctx to StackAllocator, computes start aligned to given alignment using std.mem.alignForward, computes end via getTrueAllocationEnd; if end >= self.buffer.len it delegates to self.backingAllocator.rawAlloc, otherwise it writes an AllocationTrailer with wasFreed=false and previousAllocationTrailer set to current index, updates self.index to end, and returns the aligned start pointer. resize casts ctx, checks isInsideBuffer; if true it computes start via indexInBuffer, end via getTrueAllocationEnd, verifies end equals self.index (returns false otherwise), computes newEnd for new_len, verifies newEnd < buffer.len (returns false otherwise), reads trailer at old end, asserts !trailer.wasFreed, writes a new trailer preserving previousAllocationTrailer from the old one, updates self.index to newEnd, and returns true; else delegates to backingAllocator.rawResize. remap calls resize and if successful returns memory.ptr else null. free casts ctx, checks isInsideBuffer (body truncated in source).

## Code Example
```zig
pub fn deinit() void {
	std.log.info("Clearing global arena with {} MiB", .{globalArenaAllocator.arena.queryCapacity() >> 20});
	globalArenaAllocator.deinit();
	globalArenaAllocator = undefined;
	if (globalGpa.deinit() == .leak) {
		std.log.err("Memory leak", .{});
	}
	globalGpa = undefined;
}
```

## Related Questions
- What happens when globalGpa.deinit returns .leak?
- How does createWorldArena ensure only one world arena is created at a time?
- Why is worldArenaAllocator initialized with handledGpa.allocator() instead of directly from globalGpa?
- What role does the AllocationTrailer play in StackAllocator's memory management?
- How does StackAllocator handle requests that exceed its internal buffer capacity?
- What guarantees does the allocator method provide for NeverFailingAllocator usage?
- Why is worldArenaMutex used with defer unlock in both createWorldArena and destroyWorldArena?
- How does getTrueAllocationEnd compute the end of an allocation including the trailer?
- What happens to previousAllocationTrailer when a new allocation overwrites it?
- Is StackAllocator safe for concurrent use without additional locking?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_0*
