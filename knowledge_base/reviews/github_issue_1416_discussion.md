# [issues/issue_1416.md] - Issue #1416 discussion

**Type:** review
**Keywords:** high speed flight, large render distance, memory fragmentation, performance hit, chunk freeing, red-black tree, free list allocator, GPU buffer
**Concepts:** memory fragmentation, performance optimization, GPU allocator

## Summary
The game experiences lag when flying at high speeds with large render distances due to significant memory fragmentation and performance issues caused by frequent chunk freeing.

## Explanation
The issue arises from high memory fragmentation of ChunkMesh memory when moving quickly in the game, leading to a performance hit. The maintainer notes that this is expected behavior for any allocator that cannot free pages, resulting in fragmentation when large portions of memory are freed at once. Additionally, the current GPU allocator's performance could be improved by optimizing its allocation and deallocation processes. The maintainer suggests exploring alternative memory allocation strategies, such as using a red-black tree to implement a free list allocator, while ensuring that all allocation data structures reside outside the GPU buffer to avoid reading back from it.

## Related Questions
- What is the current performance of the GPU allocator when dealing with frequent chunk freeing?
- How can the allocation and deallocation processes of the GPU allocator be optimized to improve performance?
- Can using a red-black tree for a free list allocator help reduce memory fragmentation in Cubyz?
- Why must all allocation data structures exist outside the GPU buffer?
- What are the potential benefits of disabling vsync for testing high frame rates in Cubyz?
- How does the game's performance compare with different render distances and movement speeds?

*Source: unknown | chunk_id: github_issue_1416_discussion*
