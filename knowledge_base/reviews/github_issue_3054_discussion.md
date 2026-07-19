# [issues/issue_3054.md] - Issue #3054 discussion

**Type:** review
**Keywords:** rotation SDF, offset stacking, symmetric shapes, position offset, trigonometry
**Symbols:** rotation sdfs, offsets, stacking, orbiting_test_biome.zig.zip
**Concepts:** SDF (Signed Distance Function), transformation stacking, memory handling

## Summary
The issue discusses a problem where rotation SDFs do not stack their offsets, causing incorrect positioning. The user suggests fixing this to enable easier creation of rotationally symmetric shapes.

## Explanation
The issue discusses a problem where rotation SDFs do not stack their offsets, causing incorrect positioning. The user suggests fixing this to enable easier creation of rotationally symmetric shapes without manually calculating offsets using trigonometry. Specifically, the current implementation sets the offset by the lowest level rotation sdf object rather than stacking them together. This prevents users from easily creating complex, rotationally symmetric structures. The user provides an example file and image to illustrate the issue. The reviewer notes that while the `rotated` object has a position offset in its memory, it does not utilize this information correctly for stacking offsets.

## Related Questions
- What is the current implementation of rotation SDFs in Cubyz?
- How does the `rotated` object handle position offsets in memory?
- Why are nested transformations not stacking their offsets correctly?
- Can you provide a code snippet showing how to fix the offset stacking issue?
- How would fixing this issue enable easier creation of rotationally symmetric shapes?
- What potential regressions might occur if the offset stacking is changed?

*Source: unknown | chunk_id: github_issue_3054_discussion*
