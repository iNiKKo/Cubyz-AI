# [src/server/world.zig] - PR #1338 review diff

**Type:** review
**Keywords:** tickBlocksInChunk, tick, ServerWorld, chunk.ServerChunk, random tick, block ticking, thread safety, hashmap iteration, concurrent modification, undefined behavior
**Symbols:** ServerWorld, tickBlocksInChunk, tick, chunk.ServerChunk, main.random.nextInt, main.seed, chunk.chunkShift2, chunk.chunkMask, ch.super.getBlock, block.tickEvents, event.tryRandomTick, ChunkManager.entityChunkHashMap.keyIterator
**Concepts:** thread safety, iteration, hashmap, concurrent modification

## Summary
Added `tickBlocksInChunk` and `tick` functions to handle block ticking in chunks. The review highlights a critical thread safety issue with concurrent modification of the hashmap during iteration.

## Explanation
The changes introduce two new functions, `tickBlocksInChunk` and `tick`, to manage the ticking of blocks within chunks. The `tickBlocksInChunk` function iterates over a specified number of random block indices within a chunk, retrieves the block at each index, and triggers its tick events. The `tick` function then iterates over all chunks managed by the `ChunkManager` entity chunk hashmap to call `tickBlocksInChunk` on each. However, the review points out a significant architectural concern: the iteration over the hashmap is not thread-safe. This means that if another thread modifies the hashmap (e.g., adding or removing chunks) while the iteration is in progress, it could lead to undefined behavior, such as data corruption or crashes.

## Related Questions
- How can the thread safety issue with hashmap iteration be addressed?
- What are the potential consequences of concurrent modification during hashmap iteration?
- How can the `tickBlocksInChunk` function be optimized for performance?
- Is there a need to synchronize access to the hashmap during iteration?
- Can the current implementation lead to data corruption or crashes?
- How should the architecture be modified to ensure thread safety in block ticking?

*Source: unknown | chunk_id: github_pr_1338_comment_2063812403*
