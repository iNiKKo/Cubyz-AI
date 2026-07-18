# [issues/issue_579.md] - Issue #579 discussion

**Type:** review
**Keywords:** LOD0.5, transparent leaves, performance, render distance, mesh handling, visual quality, frametime
**Concepts:** Level of Detail (LOD), Performance Optimization, Rendering

## Summary
Discussion about adding a new level of detail (LOD0.5) for opaque leaves to improve performance, especially in areas with transparent leaves.

## Explanation
Discussion about adding a new level of detail (LOD0.5) for opaque leaves to improve performance, particularly in areas with transparent leaves which are significant contributors to lag. The maintainers consider integrating LOD0.5 into the existing system but acknowledge potential difficulties due to current optimizations. They propose rendering leaves as opaque within a fixed radius around the player regardless of render distance, suggesting this approach could be more efficient than introducing a new LOD. Performance tests show that setting leaf quality to 0 can reduce frametime by 4 ms at render distance 12, indicating significant performance gains with minimal visual impact. The maintainers emphasize balancing performance improvements with maintaining acceptable visual quality.

## Related Questions
- What is the primary goal of adding LOD0.5?
- How does reducing leaf transparency impact performance?
- Why is it suggested to use a separate mesh for LOD0.5?
- What are the potential trade-offs between visual quality and performance in this optimization?
- How does changing the FOV affect the comparison of rendering times?
- What is the expected performance gain from implementing LOD0.5?

*Source: unknown | chunk_id: github_issue_579_discussion*
