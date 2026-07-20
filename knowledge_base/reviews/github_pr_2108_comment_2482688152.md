# [src/server/world.zig] - PR #2108 review diff

**Type:** review
**Keywords:** ServerWorld, entity chunks, ChunkManager, mutex, increaseRefCount, append, deinit, tryRemoveEntityChunk, GarbageCollector, thread safety, memory management, garbage collection
**Symbols:** ServerWorld, main.ListUnmanaged, EntityChunk, ChunkManager.mutex, increaseRefCount, append, deinit, tryRemoveEntityChunk, main.heap.GarbageCollector
**Concepts:** thread safety, memory management, garbage collection

## Summary
The code has been modified to use the `main.heap.GarbageCollector` for freeing entity chunks instead of directly calling `deinit()`, ensuring safe memory management across threads.

## Explanation
The code has been modified to use the `main.heap.GarbageCollector` for freeing entity chunks instead of directly calling `deinit()`, ensuring safe memory management across threads. Additionally, the removal of `increaseRefCount` and `decreaseRefCount` in favor of using `tryRemoveEntityChunk` to check if an entity chunk can be safely removed before calling `deinit()` has been noted. This change ensures that the system only attempts to deinitialize an entity chunk when it is safe to do so, further enhancing thread safety. The critical architectural review comment suggests using the `main.heap.GarbageCollector` to free entity chunks in case another thread still holds a reference. This recommendation aims to prevent potential memory leaks or dangling references by ensuring that entity chunks are only freed when they are no longer in use by any other threads.

## Related Questions
- What was the purpose of removing `increaseRefCount` and `decreaseRefCount` in favor of using `tryRemoveEntityChunk`?

*Source: unknown | chunk_id: github_pr_2108_comment_2482688152*
