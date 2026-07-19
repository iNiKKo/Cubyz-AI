# [issues/issue_2177.md] - Issue #2177 discussion

**Type:** review
**Keywords:** structure generation, multiple structure maps, power of two, chunk size, cave maps, storage requirements, computational cost
**Symbols:** structure map, biome, stalagmite, crater
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue proposes creating multiple structure maps based on structure sizes instead of a single fixed-size map.

## Explanation
The issue proposes creating multiple structure maps based on structure sizes instead of a single fixed-size map. The current system generates structures within chunks and adjacent chunks, which becomes computationally expensive for larger structures. The proposed change involves creating multiple structure maps of varying sizes to accommodate different structure dimensions.

For example, the first biome loads all structures with a max size of less than 32x32x32, creating a 32x32x32 structure map and adding these to the pool. The next biome has a few 32x32x32 structures and one stalagmite that could extend up to 50 blocks tall, so a 64x64x64 structure map is created and the stalagmite is added to the pool. Another biome has a huge crater structure that can generate a maximum diameter of 700, resulting in a 1024x1024x1024 structure map being created and the crater being added to the pool.

When generating the world, structure map fragments are generated normally for all of the created structure maps, except chunks are treated like they are as big as the corresponding structure map size. (e.g., a 64x64x64 structure map fragment would contain one list of structures for every 8 chunks.)

The sizes supported by the proposed system include powers of two, such as 32x32x32, 64x64x64, and 1024x1024x1024. The storage requirements for cave maps in the proposed system are significant; generating cave maps in a (1024+margin)³ area would require approximately 1 GiBit of storage.

The maintainer comments indicate that even generating the current 128×128×128 structure maps has a large cost attached to it when it needs to load the cave maps to check where the structure needs to generate. Generating cave maps in a (1024+margin)³ area is going to be a problem. Not only would it take 1 GiBit of storage to generate all these cave maps, but also generating them is quite expensive.

We need another solution.

## Related Questions
-  What sizes are supported by the proposed system?
-  How does the proposed system handle structures larger than 32x32x32?
-  What are the storage requirements for cave maps in the proposed system?

*Source: unknown | chunk_id: github_issue_2177_discussion*
