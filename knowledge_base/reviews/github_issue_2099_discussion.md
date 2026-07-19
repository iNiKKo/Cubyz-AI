# [issues/issue_2099.md] - Issue #2099 discussion

**Type:** review
**Keywords:** Render Distance, LOD Distance, lag, crashes, GPU memory, chunks, LODs, units in blocks, recommended values
**Concepts:** user experience, performance optimization, settings management

## Summary
The issue discusses renaming the 'Render Distance' setting to 'LOD Distance' to avoid confusion and improve accuracy. It also explores potential solutions to prevent crashes and provide better guidance for players based on GPU memory.

## Explanation
The issue discusses renaming the 'Render Distance' setting to 'LOD Distance' to avoid confusion and improve accuracy. The maintainer suggests several measures to mitigate performance issues, including temporarily lowering the default value to 20 until crashes caused by >2GB buffer size are resolved, specifying units in blocks for the render distance setting, counting chunks across multiple LODs, and providing GPU memory-based recommendations. The goal is to improve user understanding and prevent performance problems. Recommended render distance based on GPU VRAM capacity: 1GB or less - 5 chunks, 2GB or less - 10 chunks, 4GB or less - 15 chunks, 8GB or less - 20 chunks.

## Related Questions
- What is the proposed new name for the 'Render Distance' setting?
- Why was the 'Render Distance' setting renamed to 'LOD Distance'?
- What measures are suggested to prevent crashes caused by high render distances?
- How does the proposal aim to improve player understanding of the setting?
- What GPU memory-based recommendations are provided for different VRAM capacities?
- Are there any plans to specify units in blocks for the render distance setting?

*Source: unknown | chunk_id: github_issue_2099_discussion*
