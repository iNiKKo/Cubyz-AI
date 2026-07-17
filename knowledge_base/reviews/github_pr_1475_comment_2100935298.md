# [src/block_entity.zig] - PR #1475 review diff

**Type:** review
**Keywords:** block entity, position, chunk, hashmap, rendering, particles, function signature, loading, unloading
**Symbols:** BlockEntityTypes, onLoadClient, onUnloadClient, Vec3i, Chunk, BlockEntityIndex
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `onUnloadClient` function's parameter was changed from `Vec3i` and `*Chunk` to just `BlockEntityIndex`. The review highlights that loading needs positional information for rendering or other purposes, and the chunk is necessary for adding the index to the chunk hashmap.

## Explanation
The change in the `onUnloadClient` function's parameters from `(Vec3i, *Chunk)` to `BlockEntityIndex` was made to streamline the function signature. The reviewer emphasizes that during loading, knowing the block entity's position is crucial for tasks like rendering or spawning particles. Additionally, the chunk parameter is essential for managing the block entity index within the chunk's hashmap. This modification ensures that the necessary information is retained and utilized effectively.

## Related Questions
- What is the purpose of changing the `onUnloadClient` function's parameters?
- Why is positional information important during loading?
- How does the chunk parameter contribute to managing block entity indices?
- What are the potential implications of removing the chunk parameter from `onUnloadClient`?
- Can you explain the architectural reasoning behind this change?
- How might this modification affect other parts of the codebase?
- Is there a risk of introducing bugs with this change?
- What steps should be taken to ensure backwards compatibility after this change?
- How can we verify that the new function signature meets all necessary requirements?
- Are there any performance considerations associated with this change?

*Source: unknown | chunk_id: github_pr_1475_comment_2100935298*
