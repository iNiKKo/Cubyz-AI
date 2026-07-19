# [hard/codebase_src_utils_heap.zig] - Chunk 0

**Type:** implementation
**Keywords:** allocator, arena allocator, thread safety, memory leak detection, debug allocator
**Symbols:** testingErrorHandlingAllocator, testingAllocator, allocators, allocators.globalGpa, allocators.handledGpa, allocators.globalArenaAllocator, allocators.worldArenaAllocator, allocators.worldArenaOpenCount, allocators.worldArenaMutex, allocators.deinit, allocators.createWorldArena, allocators.destroyWorldArena
**Concepts:** memory management, allocator handling, arena allocation, error handling

## Summary
Manages different types of allocators for memory handling in the Cubyz engine, including global and world-specific arenas with error handling.

## Explanation
This chunk defines various allocator instances and their management functions within the Cubyz engine. It includes a global debug allocator (`globalGpa`), an error-handling wrapper around it (`handledGpa`), and two arena allocators (`globalArenaAllocator` and `worldArenaAllocator`). The `deinit` function clears these allocators, logging any memory leaks. The `createWorldArena` and `destroyWorldArena` functions manage the lifecycle of the world-specific arena allocator, ensuring thread safety with a mutex.

The global arena allocator is initialized when the `allocators.globalArenaAllocator` is first used. The `handledGpa` allocator wraps around `globalGpa` to provide error handling for memory operations. Thread safety for the world arena allocator is ensured by using a mutex (`worldArenaMutex`) to synchronize access during creation and destruction of the world arena. If a memory leak is detected during deinitialization, an error message is logged.

There are six different types of allocators defined in this chunk: `globalGpa`, `handledGpa`, `globalArenaAllocator`, `worldArenaAllocator`, and two instances of `NeverFailingArenaAllocator` (one for global and one for world). The function to create a world arena is `createWorldArena`.

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
- How does the global arena allocator get initialized?
- What is the purpose of the `handledGpa` allocator?
- How is thread safety ensured for the world arena allocator?
- What happens if a memory leak is detected during deinitialization?
- How many different types of allocators are defined in this chunk?
- What function should be called to create a world arena?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_0*
