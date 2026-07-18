# [issues/issue_836.md] - Issue #836 discussion

**Type:** review
**Keywords:** light grid, dynamic sizing, static resizing, computational cost, storage difficulty
**Concepts:** lighting, wall blocks, performance, storage

## Summary
Discussion on fixing light passing through wall blocks in Cubyz.

## Explanation
The issue discusses the problem of light being able to pass through wall blocks in the game Cubyz. The maintainer suggests potential solutions such as making the light grid smaller, either dynamically or statically. However, these suggestions come with trade-offs, including increased computational cost and storage difficulty for dynamic adjustments, and a significant increase in resource usage for static resizing.

## Related Questions
- What are the potential performance impacts of making the light grid smaller?
- How would dynamic light grid sizes affect storage requirements?
- Why is increasing the light grid size by a factor of 2 considered 8 times more expensive?
- Can you explain the trade-offs between dynamic and static resizing of the light grid?
- What are the current limitations in Cubyz's lighting system that allow light to pass through walls?
- How might making the light grid smaller impact the visual fidelity of the game?
- Are there any alternative solutions proposed for fixing the light passing through wall blocks issue?
- What is the main concern with implementing dynamic light grid sizes in Cubyz?
- How does the current lighting system in Cubyz handle occlusions like walls?
- What are the potential benefits and drawbacks of adjusting the light grid size statically?

*Source: unknown | chunk_id: github_issue_836_discussion*
