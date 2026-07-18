# [issues/issue_579.md] - Issue #579 discussion

**Type:** review
**Keywords:** LOD0.5, transparent leaves, performance, render distance, mesh handling, visual quality, frametime
**Concepts:** Level of Detail (LOD), Performance Optimization, Rendering

## Summary
Discussion about adding a new level of detail (LOD0.5) for opaque leaves to improve performance, especially in areas with transparent leaves.

## Explanation
The discussion revolves around the need to optimize leaf rendering to enhance runtime performance, particularly focusing on transparent leaves which are a significant contributor to lag. The maintainers consider adding a new LOD or adjusting the render distance radius around the player to draw leaves as opaque instead of transparent. They explore various approaches, including different mesh handling and quality settings, while emphasizing the importance of balancing performance improvements with visual quality. The maintainers also highlight that reducing leaf transparency can lead to substantial performance gains, as demonstrated by a 4 ms reduction in frametime.

## Related Questions
- What is the primary goal of adding LOD0.5?
- How does reducing leaf transparency impact performance?
- Why is it suggested to use a separate mesh for LOD0.5?
- What are the potential trade-offs between visual quality and performance in this optimization?
- How does changing the FOV affect the comparison of rendering times?
- What is the expected performance gain from implementing LOD0.5?

*Source: unknown | chunk_id: github_issue_579_discussion*
