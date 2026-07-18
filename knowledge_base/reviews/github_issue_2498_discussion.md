# [issues/issue_2498.md] - Issue #2498 discussion

**Type:** review
**Keywords:** torch placement, partial blocks, mesh generation, performance impact, neighbor chunks, bounding boxes, boolean checks
**Symbols:** torches, partial blocks, mesh generation, rotation data, neighbor chunks
**Concepts:** performance optimization, meshing performance, neighbor chunk dependencies

## Summary
Discussion about placing torches on partial blocks, considering performance implications during mesh generation.

## Explanation
The discussion revolves around the feasibility of placing torches on various partial blocks by offsetting their models into neighboring blocks. The main concern is the potential impact on meshing performance if the proposal involves checking entire blocks instead of just a thin slice of faces. The maintainer points out that this could significantly increase the number of faces requiring neighbor chunk checks, potentially slowing down the meshing process. The user suggests optimizing the check to only involve bounding boxes, but the maintainer emphasizes that even a simple boolean check would necessitate moving the block's handling to the part of the code responsible for neighbor-chunk interactions.

## Related Questions
- How does the current meshing code handle neighbor chunk interactions?
- What is the expected performance overhead of checking entire blocks during mesh generation?
- Can bounding box checks be optimized further to reduce their impact on meshing performance?
- What are the architectural implications of moving block handling to the neighbor-chunk interaction section?
- How does the current implementation ensure that only border faces depend on neighbor chunks?
- What is the potential for memory leaks in the proposed changes to mesh generation?
- How can we balance the need for detailed torch placement with performance considerations?
- What are the implications of increasing the rotation data bits for more precise torch placements?
- Can the current optimization strategies be adapted to handle larger areas of dependency on neighbor chunks?
- How does the proposed change affect thread safety in the meshing process?

*Source: unknown | chunk_id: github_issue_2498_discussion*
