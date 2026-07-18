# [issues/issue_24.md] - Issue #24 discussion

**Type:** review
**Keywords:** 2/3 meter blocks, mesh generation, compute shader, block compression, GPU data, invisible blocks
**Symbols:** ea478e0bd25754c3cae551d2926d13fd3a418091
**Concepts:** mesh generation, block compression, GPU optimization

## Summary
Implemented 2/3 meter-sized blocks, optimizing mesh generation and block compression.

## Explanation
The issue discusses reducing block size to allow for more detailed construction. The maintainer decided on a 2/3 meter size, dividing blocks into 8 smaller parts. Mesh generation optimization was achieved by compressing identical blocks into larger cubes both in memory and GPU data. The ability to place or remove multiple blocks at once is not necessary due to the less significant reduction in block size.

## Related Questions
- What is the commit hash for the implementation of 2/3 meter-sized blocks?
- How does Cubyz optimize mesh generation for smaller block sizes?
- Why was the ability to place/remove multiple blocks at once not implemented?
- What is the impact of block compression on memory usage in Cubyz?
- How does the GPU handle mesh data for compressed blocks in Cubyz?
- What are the benefits of reducing block size to 2/3 meters in Cubyz?

*Source: unknown | chunk_id: github_issue_24_discussion*
