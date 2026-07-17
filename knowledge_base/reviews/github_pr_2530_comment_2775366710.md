# [src/server/permission.zig] - Chunk 2775366710

**Type:** review
**Keywords:** Permissions, whiteList, blackList, arenaAllocator, deinit, thread safety, assertion, NeverFailingArenaAllocator, StringHashMapUnmanaged, ZonElement
**Symbols:** Permissions, ListType, white, black, arenaAllocator, permissionWhiteList, permissionBlackList, deinit, mapFromZon, mapToZon, NeverFailingArenaAllocator, NeverFailingAllocator, std.StringHashMapUnmanaged
**Concepts:** thread safety, arena allocator, memory leak prevention, deterministic deallocation, hash map management, Zon serialization, assertion-based verification, resource ownership

## Summary
The change introduces a new `Permissions` struct with white/black list hashmaps and an arena allocator, along with helper functions to convert between Zon elements and these maps; the reviewer specifically requests adding an assertion in `deinit` to ensure the arena is not freed on the wrong thread.

## Explanation
The diff adds a fresh permission management module (`permission.zig`) that encapsulates user permissions using two unmanaged string hashmaps (white list and black list) backed by a never-failing arena allocator. The `mapFromZon` function populates these maps from a Zon array, skipping duplicates, while `mapToZon` serializes the map keys back into a Zon array. The reviewer’s concern centers on thread safety: since the arena allocator is used for dynamic allocations within this struct, freeing it in `deinit` without an assertion could lead to double-free or use-after-free bugs if the same instance is deinitialized from multiple threads or if the arena is reused incorrectly elsewhere. Adding an assertion (e.g., checking that no pending allocations remain or that a thread-local flag indicates exclusive ownership) would provide compile-time and runtime guarantees against accidental concurrent deallocation, aligning with Cubyz’s emphasis on deterministic memory safety.

## Related Questions
- What is the purpose of `mapFromZon` and how does it handle duplicate strings?
- How does `Permissions.deinit` currently manage the arena allocator, and what could go wrong without an assertion?
- Why are `permissionWhiteList` and `permissionBlackList` declared as unmanaged hashmaps instead of using a regular allocator?
- What constraints does `NeverFailingAllocator` impose on allocations in this module?
- How would adding an assertion to `deinit` prevent double-free or use-after-free bugs in a multi-threaded context?
- Is there any existing synchronization mechanism (e.g., mutexes) around the permission maps, and why might it be unnecessary here?
- What happens if `mapFromZon` is called with an empty Zon array—does it leave the maps unchanged or does it allocate anything?
- Could `mapToZon` produce a different ordering of keys than the original insertion order, and does that matter for permission checks?
- If the arena allocator fails to deinit cleanly, what fallback behavior is expected in Cubyz’s error model?
- How would you test that the assertion added to `deinit` actually catches concurrent deallocation attempts?

*Source: unknown | chunk_id: github_pr_2530_comment_2775366710*
