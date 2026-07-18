# [src/chunk.zig] - PR #1338 review diff

**Type:** review
**Keywords:** hashmap, mutex, tickable blocks, random indexing, premature optimization
**Symbols:** Chunk, blockPosToEntityDataMap, blockPosToEntityDataMapMutex, blockPosToTickableBlockMap, blockPosToTickableBlockMutex
**Concepts:** thread safety, data structures, optimization

## Summary
Added block position to tickable block mapping with mutex.

## Explanation
The change introduces a new hashmap `blockPosToTickableBlockMap` and its corresponding mutex `blockPosToTickableBlockMutex` in the `Chunk` struct. The reviewer points out that using a hashmap for random indexing is inefficient and suggests reconsidering the need for a list of tickable blocks, as it may be premature optimization.

## Related Questions
- Why was a hashmap chosen for block position to tickable block mapping?
- What are the potential performance implications of using a hashmap for random access?
- How does the addition of this mutex affect thread safety in the Chunk struct?
- Is there an alternative data structure that would be more suitable for random indexing?
- What is the purpose of the `blockPosToEntityDataMap` and its associated mutex?
- How does this change relate to issue #77 mentioned in the review?

*Source: unknown | chunk_id: github_pr_1338_comment_2056762354*
