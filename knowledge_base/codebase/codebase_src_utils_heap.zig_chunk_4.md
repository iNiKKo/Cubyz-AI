# [hard/codebase_src_utils_heap.zig] - Chunk 4

**Type:** implementation
**Keywords:** arena allocation, thread-safe, memory diagnostics, free list, mutex locking
**Symbols:** NeverFailingArenaAllocator, NeverFailingArenaAllocator.init, NeverFailingArenaAllocator.deinit, NeverFailingArenaAllocator.allocator, NeverFailingArenaAllocator.reset, NeverFailingArenaAllocator.shrinkAndFree, MemoryPool, MemoryPool.item_size, MemoryPool.item_alignment, MemoryPool.Node, MemoryPool.NodePtr, MemoryPool.ItemPtr, MemoryPool.init, MemoryPool.deinit, MemoryPool.create, MemoryPool.destroy, MemoryPool.allocNew
**Concepts:** memory management, arena allocator, thread safety, memory pool

## Summary
Defines a thread-safe memory pool with diagnostics and an arena allocator that never fails.

## Explanation
The chunk defines two main structures: `NeverFailingArenaAllocator` and `MemoryPool`. The `NeverFailingArenaAllocator` is an arena allocator that ensures allocations never fail. It provides methods for initialization (`init`), deinitialization (`deinit`), resetting the allocator (`reset`), and shrinking memory (`shrinkAndFree`). The `MemoryPool` is a thread-safe memory pool that manages items of a specified type, using an internal free list to reuse allocated memory. It includes methods for creating (`create`) and destroying (`destroy`) items, as well as initializing (`init`) and deinitializing (`deinit`) the pool itself. The pool uses a mutex to ensure thread safety during operations.

The `NeverFailingArenaAllocator` struct has the following fields:
- `arena`: A standard heap arena allocator.

The `MemoryPool` struct has the following fields:
- `arena`: An instance of `NeverFailingArenaAllocator`.
- `free_list`: A pointer to the head of the free list, which contains nodes that can be reused for new allocations.
- `freeAllocations`: The number of currently available items in the free list.
- `totalAllocations`: The total number of items allocated by the pool.
- `mutex`: A mutex used to ensure thread safety during operations on the pool.

The `MemoryPool` struct also defines a nested `Node` struct, which represents each node in the free list. Each node has a pointer to the next node in the list (`next`).

The methods available for managing items in a `MemoryPool` include:
- `create`: Creates a new item and adds it to the memory pool.
- `destroy`: Destroys a previously created item, returning it to the free list.

The `NeverFailingArenaAllocator` struct provides the following methods:
- `init(childAllocator: NeverFailingAllocator) NeverFailingArenaAllocator`: Initializes the arena allocator with a child allocator.
- `deinit(self: NeverFailingArenaAllocator) void`: Deinitializes the arena allocator and frees all allocated memory.
- `allocator(self: *NeverFailingArenaAllocator) NeverFailingAllocator`: Returns an allocator that ensures allocations never fail.
- `reset(self: *NeverFailingArenaAllocator, mode: std.heap.ArenaAllocator.ResetMode) bool`: Resets the arena allocator and frees all allocated memory. It returns whether the reset operation was successful or not.
- `shrinkAndFree(self: *NeverFailingArenaAllocator) void`: Shrinks the arena allocator and frees unused memory.

The `MemoryPool` struct provides the following methods:
- `init(arena: NeverFailingAllocator) Pool`: Creates a new memory pool with the given arena allocator.
- `deinit(pool: *Pool) void`: Destroys the memory pool and frees all allocated memory. It logs an error if there are leaked elements or prints information about the total allocations.
- `create(pool: *Pool) ItemPtr`: Creates a new item and adds it to the memory pool. It locks the mutex, checks the free list, allocates new memory if necessary, and returns a pointer to the created item.
- `destroy(pool: *Pool, ptr: ItemPtr) void`: Destroys a previously created item by returning it to the free list. It locks the mutex, sets the item to undefined, updates the free list, and increments the count of free allocations.

The `MemoryPool` struct also defines constants for the item size (`item_size`) and alignment (`item_alignment`). The item size is the maximum of the size of a node and the size of the specified item type. The item alignment is the maximum of the alignment of a pointer to any opaque type and the alignment of the specified item type.

## Code Example
```zig
pub fn deinit(self: NeverFailingArenaAllocator) void {
	self.arena.deinit();
}
```

## Related Questions
- How does the `NeverFailingArenaAllocator` ensure allocations never fail?
- What is the purpose of the `MemoryPool` structure in this code?
- How does the `MemoryPool` handle thread safety?
- What methods are available for managing items in a `MemoryPool`?
- How does the `NeverFailingArenaAllocator` reset its state?
- What happens if an allocation fails when using the `NeverFailingArenaAllocator`?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_4*
