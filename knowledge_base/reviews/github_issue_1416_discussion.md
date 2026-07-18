# [issues/issue_1416.md] - Issue #1416 discussion

**Type:** review
**Keywords:** high speed flight, large render distance, memory fragmentation, performance hit, chunk freeing, red-black tree, free list allocator, GPU buffer
**Concepts:** memory fragmentation, performance optimization, GPU allocator

## Summary
The game experiences lag when flying at high speeds with large render distances due to significant memory fragmentation and performance issues caused by frequent chunk freeing.

## Explanation
The game experiences lag when flying at high speeds with large render distances due to significant memory fragmentation of ChunkMesh memory and a performance hit caused by frequent chunk freeing. The maintainer notes that this is expected behavior for any allocator that cannot free pages, resulting in fragmentation when large portions of memory are freed at once. Specifically, the reproduction sequence involves joining the world, moving with hyper speed (~30 seconds), waiting for the Queue size to go to 0, and repeating this process. This results in a ~50fps drop on an RTX 3080 and approximately 1GB of fragmentation reported by F3 debug info. The maintainer suggests that it is possible to improve the performance of the GPU allocator by optimizing its allocation and deallocation processes, such as using a red-black tree or another type of tree structure to implement a free list allocator. Additionally, all allocation data structures must exist outside the memory itself to avoid reading back from the GPU buffer.

## Related Questions
- What is the exact frame rate drop observed when flying at high speeds with large render distances?
- How much memory fragmentation occurs during this process and what does it look like in F3 debug info?
- Can using a red-black tree for a free list allocator help reduce memory fragmentation in Cubyz, and how would this be implemented?

*Source: unknown | chunk_id: github_issue_1416_discussion*
