# [issues/issue_1161.md] - Issue #1161 discussion

**Type:** review
**Keywords:** lag in caves, 2M faces, frame time, multi-step rendering, occlusion culling, render distance
**Concepts:** performance optimization, occlusion culling, rendering pipeline

## Summary
The issue discusses performance lag in caves due to high face count and proposes a multi-step rendering approach for occlusion culling.

## Explanation
The issue discusses performance lag in caves due to high face count before occlusion culling. The maintainer clarifies that scenes like this should not draw 2 million faces, but notes that the actual frame time is 1.3 ms and does not consider it problematic. A proposed solution involves breaking down the rendering and occlusion culling processes into multiple steps based on render distance (for(0..renderDistance) |i| { do occlusion culling for chunks at distance i; render chunks at distance i }). This approach aims to improve performance by managing the complexity of rendering large numbers of faces more efficiently. The maintainer suggests implementing this change after another feature (#823) is completed.

## Related Questions
- What is the current frame time for cave rendering?
- How does occlusion culling affect the face count before rendering?
- Why is the multi-step rendering approach preferred over a single pass?
- When will feature #823 be completed?
- What are the potential benefits of implementing the multi-step rendering approach?
- How might this change impact memory usage during rendering?

*Source: unknown | chunk_id: github_issue_1161_discussion*
