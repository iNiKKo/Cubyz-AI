# [src/block_entity.zig] - PR #1475 review diff

**Type:** review
**Keywords:** block entity, position, chunk, hashmap, rendering, particles, index management, architectural review, loading functions, unloading functions, parameter modification
**Symbols:** onLoadClient, onUnloadClient, Vec3i, Chunk, BlockEntityIndex
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `onUnloadClient` function's parameter was changed from `Vec3i` and `*Chunk` to just `BlockEntityIndex`. The reviewer emphasizes that loading functions need positional information for rendering or other purposes, and the chunk is necessary for managing block entity indices in a hashmap.

## Explanation
The change modifies the `onUnloadClient` function's signature by removing the position (`Vec3i`) and chunk (`*Chunk`) parameters, replacing them with just `BlockEntityIndex`. The reviewer highlights that loading functions should retain positional information because it is crucial for tasks like rendering or spawning particles. Additionally, the chunk parameter is essential for adding block entity indices to a hashmap, ensuring proper management of block entities within chunks.

## Related Questions
- What is the purpose of retaining positional information in loading functions?
- Why was the chunk parameter necessary for managing block entity indices?
- How does this change affect the overall architecture of block entities?
- Can you explain the implications of removing the position and chunk parameters from `onUnloadClient`?
- What are the potential performance impacts of this architectural decision?
- How does this modification ensure backwards compatibility with existing code?
- Is there a risk of memory leaks associated with this change?
- What are the thread safety considerations for this architectural review?
- How does this change impact the rendering or particle spawning processes?
- Can you provide examples of how block entities might use positional information during loading?
- What is the role of the chunk hashmap in managing block entity indices?

*Source: unknown | chunk_id: github_pr_1475_comment_2100935298*
