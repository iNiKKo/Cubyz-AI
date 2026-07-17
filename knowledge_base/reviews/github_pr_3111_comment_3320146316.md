# [src/blueprint.zig] - Chunk 3320146316

**Type:** review
**Keywords:** Blueprint, capture, Selection, minPos, maxPos, init, Vec3i, @min, @max, extent constructor, inclusive, exclusive
**Symbols:** Blueprint, CaptureResult, Selection, init
**Concepts:** API refactoring, inclusive/exclusive bounds, dead code elimination, code clarity

## Summary
Refactored the Blueprint struct by replacing the capture function with a new Selection struct and its init method, removing unnecessary min/max logic from the extent constructor.

## Explanation
The original code used a capture function that computed start coordinates via @min on two positions. The reviewer realized this was redundant because the extent constructor already handles ordering correctly without explicit min/max calls. By introducing Selection with minPos (inclusive) and maxPos (exclusive), the API becomes clearer and more consistent with how extents are represented elsewhere in the codebase. This change eliminates dead computation, improves readability, and aligns the selection representation with existing conventions.

## Related Questions
- What is the purpose of the Selection struct in blueprint.zig?
- How does the init method compute minPos and maxPos?
- Why was the capture function replaced with a Selection struct?
- What are the types of pos1Inclusive and pos2Exclusive in Selection.init?
- Does the new Selection API maintain backwards compatibility with existing code?
- Where else in the codebase is an extent represented using inclusive/exclusive bounds?
- How does removing @min/@max from the extent constructor affect performance?
- What constraints apply to Vec3i values passed to Selection.init?
- Is there any documentation explaining the semantics of minPos being inclusive?
- Could a user accidentally pass pos2Exclusive <= pos1Inclusive and what would happen?
- How does this change impact error handling for invalid selections?
- Are there any tests that need updating due to the removal of capture?

*Source: unknown | chunk_id: github_pr_3111_comment_3320146316*
