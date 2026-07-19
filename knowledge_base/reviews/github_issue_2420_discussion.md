# [issues/issue_2420.md] - Issue #2420 discussion

**Type:** review
**Keywords:** 2x2x2 chunks, independent passes, player actions, block updates, world edit, inventory ops, server update, frame rate
**Concepts:** parallel processing, thread safety, multi-processor systems

## Summary
The issue discusses parallelizing the server update thread by dividing the world into 2×2×2 chunks for independent processing, while addressing potential drawbacks like player movement and world edit limitations.

## Explanation
The proposal aims to enhance server performance by enabling parallel processing of chunks through dividing them into units of 2×2×2. This allows for 8 independent passes, ensuring each chunk event can access its surrounding chunks without blocking. The approach introduces challenges such as preventing further actions until the next tick when a player moves far enough out of a chunk to avoid accessing data currently used by another thread. Additionally, world edit commands need to be split into chunks and recombined at the end to store undo operations, with a limit of 1 command per player per tick to prevent data corruption. All server operations except bookkeeping and terrain generation fall under the update thread, including inventory operations related to block entities like workbenches and chests. Inventory updates are limited to a radius of 32 blocks around the player who performs the interaction.

## Related Questions
- How does the parallel processing of chunks affect server performance?
- What are the potential thread safety issues with player movement in this setup?
- How is world edit handled to prevent data corruption during parallel updates?
- Are inventory operations covered by the update thread, and how are they managed?
- Does the server have a concept of frames, or does it operate differently?

*Source: unknown | chunk_id: github_issue_2420_discussion*
