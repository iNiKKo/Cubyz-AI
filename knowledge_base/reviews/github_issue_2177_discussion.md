# [issues/issue_2177.md] - Issue #2177 discussion

**Type:** review
**Keywords:** structure generation, multiple structure maps, power of two, chunk size, cave maps, storage requirements, computational cost
**Symbols:** structure map, biome, stalagmite, crater
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue proposes creating multiple structure maps based on structure sizes instead of a single fixed-size map.

## Explanation
The current system generates structures within chunks and adjacent chunks, which becomes computationally expensive for larger structures. The proposed change involves creating multiple structure maps of varying sizes to accommodate different structure dimensions. For example, the first biome loads all structures with a max size of less than 32x32x32, creating a 32x32x32 structure map and adding these to the pool. The next biome has a few 32x32x32 structures and one stalagmite that could extend up to 50 blocks tall, so a 64x64x64 structure map is created and the stalagmite is added to the pool. Another biome has a huge crater structure that can generate a maximum diameter of 700, resulting in a 1024x1024x1024 structure map being created and the crater being added to the pool. When generating the world, structure map fragments are generated normally for all of the created structure maps, except chunks are treated like they are as big as the corresponding structure map size.

## Related Questions
-  What sizes are supported by the proposed system?
-  How does the proposed system handle structures larger than 32x32x32?
-  What are the storage requirements for cave maps in the proposed system?

*Source: unknown | chunk_id: github_issue_2177_discussion*
