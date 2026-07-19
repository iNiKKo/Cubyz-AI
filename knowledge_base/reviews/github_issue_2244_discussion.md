# [issues/issue_2244.md] - Issue #2244 discussion

**Type:** review
**Keywords:** random ticks, unloaded chunks, crop progression, Solution A, Solution B, Terraria, block entities, ticking hooks, API
**Concepts:** random ticks, chunk unloading, block progression, memory requirement, performance

## Summary
Proposes solutions for simulating random ticks in unloaded chunks to progress crops and other blocks.

## Explanation
The issue discusses the problem where random ticks do not occur in unloaded chunks, preventing crop progression when players venture far from their base. Solution A suggests storing the last tick time and calculating progress based on the delta. Specifically, this involves using a large grain time (e.g., day counter) to reduce memory usage. Solution B proposes storing the unload time of chunks and ticking blocks upon loading with the duration of unloading. The maintainer prefers Solution B for its lower memory requirement and similarity to Terraria's approach. However, it may negatively impact chunk loading performance due to additional computation during load times. The discussion also mentions that block entities could be used but lack integration between ticking and block entity hooks, as well as an appealing API.

## Related Questions
- What is the exact time storage method proposed in Solution A?
- How does Solution B's chunk unload time storage work in detail?

*Source: unknown | chunk_id: github_issue_2244_discussion*
