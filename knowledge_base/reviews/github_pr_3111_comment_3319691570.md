# [src/blueprint.zig] - PR #3111 review diff

**Type:** review
**Keywords:** capture, allocator, pos1, pos2, startX, startY, startZ, minPos, maxPos, Selection
**Symbols:** Blueprint, CaptureResult, Vec3i, NeverFailingAllocator, Selection
**Concepts:** Coordinate Handling, Struct Initialization, Architectural Review

## Summary
The code introduces a new `Selection` struct with `minPos` and `maxPos` fields, replacing an incorrect capture function.

## Explanation
The reviewer points out that swapping positions between inclusive and exclusive coordinates is architecturally flawed. They recommend removing the existing function to prevent potential bugs related to coordinate handling. The introduction of a new `Selection` struct with explicit field assignments aims to clarify and correct the logic for defining block selections.

## Related Questions
- What is the purpose of the `Selection` struct in the code?
- Why was the original capture function deemed incorrect?
- How does the new `init` method for `Selection` ensure correct coordinate assignment?
- What potential bugs could arise from swapping inclusive and exclusive coordinates?
- Is there any regression testing planned to verify the changes?
- How does this change impact backwards compatibility with existing code?

*Source: unknown | chunk_id: github_pr_3111_comment_3319691570*
