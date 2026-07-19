# [src/server/terrain/simple_structures/SbbGen.zig] - PR #2195 review diff

**Type:** review
**Keywords:** optional pointer, invalid memory, resize, loop bounds, issue #1932, ugly implementation
**Symbols:** SbbGen, getHash, loadModel, ZonElement, structureList
**Concepts:** memory safety, bounds checking

## Summary
The `loadModel` function in `SbbGen.zig` now returns an optional pointer, and the loop over `structureList` is bounded to prevent accessing invalid memory.

## Explanation
The `loadModel` function in `SbbGen.zig` now returns an optional pointer (`?*SbbGen`) and the loop over `structureList` is bounded to prevent accessing invalid memory. The original implementation could lead to accessing invalid memory due to resizing `structureList` larger than necessary. The fix involves returning an optional pointer and adjusting the loop bounds to only iterate over valid items, addressing issue #1932. Specifically, the slice we loop over is now bounded by how many items made it through registration (`0..stage1Count`). While the current implementation is considered 'ugly,' it will be cleaned up later.

## Related Questions
- What is the purpose of returning an optional pointer in `loadModel`?
- How does the fix prevent accessing invalid memory?
- What was the root cause of issue #1932?
- Why is the current implementation considered 'ugly'?
- When will the ugly implementation be cleaned up?
- What changes were made to the loop over `structureList`?

*Source: unknown | chunk_id: github_pr_2195_comment_2492433648*
