# [hard/codebase_src_utils_heap.zig] - Chunk 3

**Type:** api
**Keywords:** allocator, sentinel, arena, resize, remap, realloc, free, dupe, alignment, never failing
**Symbols:** NeverFailingAllocator, NeverFailingAllocator.allocSentinel, NeverFailingAllocator.alignedAlloc, NeverFailingAllocator.allocAdvancedWithRetAddr, NeverFailingAllocator.resize, NeverFailingAllocator.remap, NeverFailingAllocator.realloc, NeverFailingAllocator.reallocAdvanced, NeverFailingAllocator.free, NeverFailingAllocator.dupe, NeverFailingAllocator.dupeZ, NeverFailingAllocator.createArena, NeverFailingAllocator.destroyArena, NeverFailingArenaAllocator, NeverFailingArenaAllocator.init
**Concepts:** sentinel allocation, arena allocator, memory resizing, allocation reallocation, resource leak prevention

## Summary
This chunk defines the `NeverFailingAllocator` struct, which wraps a standard allocator with sentinel-based allocation and arena management to prevent resource leaks.

## Explanation
The chunk declares `pub const NeverFailingAllocator = struct { ... }`. It exposes public methods: `allocSentinel`, `alignedAlloc`, `allocAdvancedWithRetAddr`, `resize`, `remap`, `realloc`, `reallocAdvanced`, `free`, `dupe`, `dupeZ`, and arena helpers `createArena`/`destroyArena`. All these delegate to an internal field `self.allocator` (a standard allocator). The struct also contains a private helper function `allocWithSizeAndAlignment` and another private helper `allocBytesWithAlignment`; both are not exported and are used internally by the public API. The chunk further defines `pub const NeverFailingArenaAllocator = struct { arena: std.heap.ArenaAllocator }`, with an `init` method that constructs a new arena allocator from a child allocator. No other types or functions are declared in this chunk.

## Related Questions
- What is the purpose of `allocSentinel` and how does it differ from regular allocation?
- How does `NeverFailingAllocator` guarantee that allocations never fail at runtime?
- When should a developer call `free` versus using `destroyArena` to release memory?
- What happens if `resize` returns false—does the original allocation remain valid?
- Does `remap` ever relocate the pointer, and how does it signal success or failure?
- How are alignment requirements handled in `alignedAlloc` when no explicit alignment is provided?
- Can `dupeZ` be used for any type, or only null-terminated strings?
- What is the relationship between `NeverFailingArenaAllocator.arena` and the parent allocator?
- Is it safe to call `createArena` multiple times on the same `NeverFailingAllocator` instance?
- How does this chunk interact with Zig's standard heap allocator (`std.heap.ArenaAllocator`)?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_3*
