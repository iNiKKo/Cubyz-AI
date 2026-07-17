# [hard/codebase_src_main.zig] - Chunk 0

**Type:** implementation
**Keywords:** thread-local variables, global allocators, timestamping, callback functions, GUI visibility
**Symbols:** gui, server, audio, argparse, assets, block_entity, blocks, blueprint, callbacks, chunk, client, entity, entityModel, files, fmt, game, graphics, itemdrop, items, log, meta, migrations, models, network, physics, random, renderer, rotation, settings, sync, particles, Tag, utils, vec, ZonElement, file_monitor, Vec2f, Vec3d, Window, heap, ListManaged, List, MultiArray, stackAllocator, seed, stackAllocatorBase, globalAllocator, globalArena, worldArena, threadPool, threadedIo, io, initThreadLocals, deinitThreadLocals, timestamp, cacheStringImpl, cacheString, std_options, escape, inventory, ungrabMouse, openCreativeInventory, openChat, openCommand, takeBackgroundImageFn, toggleHideGui, toggleHideDisplayItem, toggleDebugOverlay
**Concepts:** thread management, memory allocation, time-stamping, user input handling, GUI management

## Summary
This chunk initializes and deinitializes thread-local variables, sets up global allocators, manages time-stamping, and defines various callback functions for handling user input.

## Explanation
The chunk begins by importing numerous modules essential to the Cubyz engine. It then declares several thread-local variables including `stackAllocator`, `seed`, and `stackAllocatorBase`. Global allocators are also defined, such as `globalAllocator` and `worldArena`. The `initThreadLocals` function initializes these thread-local variables, setting up a stack allocator and adding the current thread to garbage collection. Conversely, `deinitThreadLocals` deinitializes the stack allocator and removes the thread from garbage collection. The `timestamp` function retrieves the current time using the I/O system. Several utility functions like `cacheStringImpl` and `cacheString` are defined for string manipulation. The chunk also configures the standard library's logging options to use a custom log function. A series of callback functions (`escape`, `inventory`, `ungrabMouse`, etc.) handle various user inputs, such as opening inventory windows, toggling GUI visibility, and taking background images.

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
- What are the thread-local variables declared in this chunk?
- How does the `initThreadLocals` function initialize these thread-local variables?
- What is the purpose of the `timestamp` function in this chunk?
- Which callback functions handle user input for opening inventory windows?
- How does the `toggleHideGui` function affect the GUI visibility?
- What global allocators are defined in this chunk and how are they used?
- How does the `deinitThreadLocals` function clean up thread-local resources?
- What is the role of the `cacheStringImpl` and `cacheString` functions?
- How is the standard library's logging configured in this chunk?
- What are the dependencies between different modules imported at the beginning of the chunk?

*Source: unknown | chunk_id: codebase_src_main.zig_chunk_0*
