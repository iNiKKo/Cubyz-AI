# [src/blueprint.zig] - Chunk 3317945686

**Type:** review
**Keywords:** Blueprint, capture, Selection, minPos, maxPos, Vec3i, inclusive, exclusive, convention, rendering
**Symbols:** Blueprint, capture, CaptureResult, Selection, minPos, maxPos, Vec3i
**Concepts:** inclusive/exclusive bounds, architectural convention alignment, code clarity via struct extraction, rendering coordinate math, bounds safety in Array3D.set

## Summary
The diff refactors the Blueprint capture function to introduce a Selection struct that explicitly stores min and max positions, replacing inline calculations with named fields.

## Explanation
The original implementation computed start coordinates on-the-fly using @min of two Vec3i arguments. The reviewer points out that this pattern already follows the project's convention: min is inclusive while max is exclusive (mirroring how size() adds one and avoids bounds failures in Array3D.set). By extracting these into a Selection struct, the code gains clarity and aligns with existing architectural patterns used elsewhere, such as rendering calculations where topRight - bottomLeft + Vec3i{1,1,1} is applied. This refactor does not change semantics but improves readability and consistency.

## Related Questions
- What is the exact definition of Selection in blueprint.zig after this change?
- How does size() handle bounds in Array3D.set and why does it add one?
- Where else in the codebase is topRight - bottomLeft + Vec3i{1,1,1} used for rendering?
- Does capture now return a Selection or still CaptureResult?
- What are the types of minPos and maxPos inside Selection?
- Is there any validation logic added to ensure min <= max in Selection?
- How does this refactor affect callers that previously passed two positions directly?
- Are there any tests that verify the inclusive/exclusive semantics of Selection?
- What is the relationship between CaptureResult and Selection in terms of data flow?
- Does the new Selection struct introduce any memory overhead compared to inline fields?

*Source: unknown | chunk_id: github_pr_3111_comment_3317945686*
