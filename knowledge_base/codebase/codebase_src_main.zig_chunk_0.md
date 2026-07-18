# [hard/codebase_src_main.zig] - Chunk 0

**Type:** implementation
**Keywords:** thread-local storage, allocators, garbage collection, timestamping, string caching, logging options
**Symbols:** gui, server, audio, argparse, assets, block_entity, blocks, blueprint, callbacks, chunk, client, entity, entityModel, files, fmt, game, graphics, itemdrop, items, log, meta, migrations, models, network, physics, random, renderer, rotation, settings, sync, particles, Tag, utils, vec, ZonElement, file_monitor, Vec2f, Vec3d, Window, heap, ListManaged, List, MultiArray, stackAllocator, seed, stackAllocatorBase, globalAllocator, globalArena, worldArena, threadPool, threadedIo, io, initThreadLocals, deinitThreadLocals, timestamp, cacheStringImpl, cacheString, std_options
**Concepts:** thread management, memory allocation, logging configuration

## Summary
This chunk initializes and deinitializes thread-local storage, manages allocators, and sets up global logging options.

## Explanation
This chunk initializes and deinitializes thread-local storage, manages various allocators, sets up global logging options, and defines several utility functions. Specifically, it initializes `stackAllocator`, `seed`, and `stackAllocatorBase` in the `initThreadLocals` function by setting `seed` to a value derived from the current timestamp's nanoseconds, initializing `stackAllocatorBase` with `globalAllocator` and a stack size of 1 << 23 bytes, and setting `stackAllocator` as an allocator for `stackAllocatorBase`. It also adds the current thread to garbage collection. Conversely, in `deinitThreadLocals`, it deinitializes `stackAllocatorBase` and removes the current thread from garbage collection. The chunk defines a global allocator `globalAllocator` using `heap.allocators.handledGpa.allocator()` if not testing, otherwise uses `heap.testingAllocator`. Similarly, `worldArena` is defined as an allocator with `heap.allocators.worldArenaAllocator.allocator()`. Additionally, it sets up logging options in `std_options`, configuring the log level to `.debug` and setting a custom log function `log.logFn`. The chunk also includes functions for generating timestamps and caching strings.

## Code Example
```zig
pub fn initThreadLocals() void {
	seed = @bitCast(@as(i64, @truncate(timestamp().nanoseconds)));
	stackAllocatorBase = heap.StackAllocator.init(globalAllocator, 1 << 23);
	stackAllocator = stackAllocatorBase.allocator();
	heap.GarbageCollection.addThread();
}
```

## Related Questions
- How is the `stackAllocator` initialized in this chunk?
- What does the `deinitThreadLocals` function do?
- Which global allocators are defined and how are they used?
- How is the logging configuration set up in this chunk?
- What is the purpose of the `cacheString` function?
- How is the timestamp generated in this code?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_0*
