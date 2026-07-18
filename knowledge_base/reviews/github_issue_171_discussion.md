# [issues/issue_171.md] - Issue #171 discussion

**Type:** review
**Keywords:** lod terrain, CPU cores, render thread, mesh loading, network delay, chunk generation
**Concepts:** networking, thread safety, performance

## Summary
The issue involves players being able to reach low-detail (LOD) terrain when moving too fast on CPUs with many cores, which was not possible on older CPUs.

## Explanation
The root cause of the issue is identified as network delay. Specifically, the time between sending and receiving a chunk can increase significantly (up to 20 seconds) after moving around the terrain for an extended period. This delay affects how meshes are loaded in the render thread, potentially causing chunks close to the player to be generated last instead of first.

## Related Questions
- What is the maximum observed network delay between sending and receiving a chunk?
- How does the number of CPU cores affect the order in which meshes are loaded?
- Is there any mechanism to prioritize generating chunks close to the player?
- Can the network delay be reduced to prevent reaching LOD terrain too easily?
- What is the current architecture for handling mesh loading in the render thread?
- Are there any known optimizations that can improve chunk generation order?
- How does the issue manifest differently on CPUs with varying numbers of cores?
- Is there a way to detect and handle network delays dynamically?
- Can the LOD terrain generation be adjusted based on player movement speed?
- What are the potential implications of increasing network delay on game performance?

*Source: unknown | chunk_id: github_issue_171_discussion*
