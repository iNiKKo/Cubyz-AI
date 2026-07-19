# [issues/issue_2498.md] - Issue #2498 discussion

**Type:** review
**Keywords:** torch placement, partial blocks, mesh generation, performance impact, neighbor chunks, bounding boxes, boolean checks
**Symbols:** torches, partial blocks, mesh generation, rotation data, neighbor chunks
**Concepts:** performance optimization, meshing performance, neighbor chunk dependencies

## Summary
Discussion about placing torches on partial blocks, considering performance implications during mesh generation.

## Explanation
Discussion about placing torches on various partial blocks by offsetting their models into neighboring blocks. The main concern is the potential impact on meshing performance if the proposal involves checking entire blocks instead of just a thin slice of faces. With 16 bits of rotation data and 5 sides, only 2 bits per side are available for special cases like branches, slabs, fence post sides, wall sides, etc. However, giving up on placing multiple torches in one block would allow for 4 bits per side. The maintainer points out that the current meshing code checks a very thin slice (roughly 1/32th of all faces) and this already takes up significant time; with the proposal, it would need to check an entire plane of blocks (under 6/32th of the faces), potentially slowing down the process. The user suggests optimizing the check to only involve bounding boxes, but the maintainer emphasizes that even a simple boolean check would necessitate moving the block's handling to the part of the code responsible for neighbor-chunk interactions due to potential updates when the neighbor chunk changes.

## Related Questions
- How does the current meshing code handle neighbor chunk interactions?
- What is the expected performance overhead of checking entire blocks during mesh generation?
- Can bounding box checks be optimized further to reduce their impact on meshing performance?
- What are the architectural implications of moving block handling to the neighbor-chunk interaction section?
- How does the current implementation ensure that only border faces depend on neighbor chunks?

*Source: unknown | chunk_id: github_issue_2498_discussion*
