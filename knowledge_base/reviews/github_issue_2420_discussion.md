# [issues/issue_2420.md] - Issue #2420 discussion

**Type:** review
**Keywords:** 2x2x2 chunks, independent passes, player actions, block updates, world edit, inventory ops, server update, frame rate
**Concepts:** parallel processing, thread safety, multi-processor systems

## Summary
The issue discusses parallelizing the server update thread by dividing the world into 2×2×2 chunks for independent processing, while addressing potential drawbacks like player movement and world edit limitations.

## Explanation
The proposal aims to enhance server performance by enabling parallel processing of chunks through 8 independent passes. This approach allows each chunk event to access neighboring chunks without blocking, leveraging multi-processor systems effectively. However, it introduces challenges such as ensuring thread safety during player movement and managing world edit commands to prevent data corruption. The discussion clarifies that all server operations except bookkeeping and terrain generation fall under the update thread, including inventory operations related to block entities like workbenches and chests.

## Related Questions
- How does the parallel processing of chunks affect server performance?
- What are the potential thread safety issues with player movement in this setup?
- How is world edit handled to prevent data corruption during parallel updates?
- Are inventory operations covered by the update thread, and how are they managed?
- Does the server have a concept of frames, or does it operate differently?
- What limitations exist for interacting with block entities like workbenches and chests in this new system?

*Source: unknown | chunk_id: github_issue_2420_discussion*
