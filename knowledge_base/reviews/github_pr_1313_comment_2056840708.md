# [src/renderer/mesh_storage.zig] - Chunk 2056840708

**Type:** review
**Keywords:** HashMapUnmanaged, list, ChunkMesh, regenerateMesh, lightRefreshList, chunk position, overhead, premature optimization, data structure, batch update
**Symbols:** batchUpdateBlocks, lightRefreshList, main.List, *ChunkMesh, regenerateMesh, std.HashMapUnmanaged, chunk.ChunkPosition
**Concepts:** premature optimization, hash map vs list tradeoff, memory overhead, batch processing, data structure selection

## Summary
The diff introduces a new `batchUpdateBlocks` function that replaces the previous mesh update logic with a HashMap-based approach for regenerating chunk meshes, but the reviewer questions this design choice.

## Explanation
The original code likely updated meshes sequentially or used a list. The change to use `std.HashMapUnmanaged` suggests an attempt to optimize lookups or batch processing of chunks by position. However, the reviewer's concern is valid: HashMaps have higher overhead (allocation, hashing, collision handling) and are unnecessary when the number of entries is small. For a few chunks per frame, a simple list would be faster and use less memory. The architectural reasoning here involves balancing performance gains against premature optimization; using a hash map adds complexity without measurable benefit in this context.

## Related Questions
- What is the maximum number of chunks that `regenerateMesh` can hold?
- How does `lightRefreshList` differ from a standard list in terms of allocation strategy?
- Why was `std.HashMapUnmanaged` chosen over `std.ArrayList` for this use case?
- Is there any scenario where the HashMap approach would outperform a list here?
- What is the hash function used for `chunk.ChunkPosition` and its collision handling?
- Does `batchUpdateBlocks` replace all previous mesh update logic or only part of it?
- How does this change affect memory usage during frame updates?
- Are there any existing benchmarks comparing list vs HashMap performance in the codebase?
- What is the expected lifecycle of entries in `regenerateMesh` (when are they removed)?
- Could a simple array with linear search be sufficient given the small entry count?

*Source: unknown | chunk_id: github_pr_1313_comment_2056840708*
