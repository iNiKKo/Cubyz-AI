# [src/server/world.zig] - PR #1338 review diff

**Type:** review
**Keywords:** tickBlocksInChunk, tick, ServerWorld, chunk, blockIndex, randomTick, thread safety, hashmap, iteration, data corruption
**Symbols:** ServerWorld, tickBlocksInChunk, tick, ChunkManager, entityChunkHashMap
**Concepts:** thread safety, hashmap iteration, block ticking

## Summary
Added `tickBlocksInChunk` and `tick` functions to ServerWorld for block ticking. Reviewer flagged potential thread safety issues with hashmap iteration.

## Explanation
The changes introduce two new functions, `tickBlocksInChunk` and `tick`, within the `ServerWorld` struct to handle block ticking in chunks. The `tickBlocksInChunk` function iterates over a specified number of blocks (`self.tickSpeed`) in a given chunk, selecting random blocks and triggering their tick events. Specifically, it generates a `blockIndex` using `main.random.nextInt(u32, &main.seed)`, then calculates the block's coordinates `(x, y, z)` using bitwise operations with `chunk.chunkShift2`, `chunk.chunkMask`, and `chunk.chunkMask`. The function retrieves the block at these coordinates and iterates over its tick events, attempting a random tick for each event. The `tick` function then iterates over all chunks using an iterator from `ChunkManager.entityChunkHashMap`. However, the reviewer points out that this approach is not thread-safe because another thread could modify the hashmap while it is being iterated, leading to potential data corruption or undefined behavior.

## Related Questions
- How can the iteration over `entityChunkHashMap` be made thread-safe?
- What are the potential consequences of concurrent modifications to `entityChunkHashMap` during iteration?
- Can you suggest a method to ensure that block ticking does not interfere with other operations on chunks?
- Is there a way to implement a read-write lock for `entityChunkHashMap` to prevent concurrent modifications?
- How can we verify the thread safety of the new block ticking functions in a multi-threaded environment?
- What are the implications of using a random number generator (`main.random`) within a loop that could be executed concurrently?

*Source: unknown | chunk_id: github_pr_1338_comment_2063812403*
