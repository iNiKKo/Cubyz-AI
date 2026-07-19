# [src/blueprint.zig] - PR #3111 review diff

**Type:** review
**Keywords:** Blueprint, capture, Selection, minPos, maxPos, Vec3i, inclusive, exclusive, size(), Array3D.set, rendering
**Symbols:** Blueprint, CaptureResult, Selection, Vec3i
**Concepts:** inclusive-exclusive range, code consistency, off-by-one errors

## Summary
The code introduces a new `Selection` struct within the `Blueprint` struct to encapsulate selection coordinates. The reviewer notes that the convention for min and max positions should be inclusive for min and exclusive for max, similar to other parts of the codebase.

## Explanation
The change involves adding a `Selection` struct with `minPos` and `maxPos` fields to the `Blueprint` struct. The reviewer points out that this follows a common convention where the minimum position is inclusive and the maximum position is exclusive. This consistency is important for avoiding off-by-one errors, especially when calculating sizes or iterating over ranges.

The `size()` method calculates the size of the selection by adding 1 to the difference between `maxPos` and `minPos`. For example, if `minPos` is `(0, 0, 0)` and `maxPos` is `(2, 2, 2)`, the size would be `(3, 3, 3)`. This ensures that the range is inclusive of the minimum position and exclusive of the maximum position.

In rendering, the conversion of selection coordinates to floating-point values involves adding 1 to each component of the vector difference between `topRight` and `bottomLeft`. For example, if `bottomLeft` is `(0, 0, 0)` and `topRight` is `(2, 2, 2)`, the resulting floating-point size would be `(3.0, 3.0, 3.0)`. This ensures that the rendered area includes all selected blocks.

## Related Questions
- What is the purpose of the `Selection` struct in the `Blueprint` struct?
- How does the new `Selection` struct ensure consistency with other parts of the codebase?
- Why is it important to have a clear convention for inclusive and exclusive ranges in this context?
- Can you explain how the `size()` method handles the range between `minPos` and `maxPos`?
- What potential issues could arise from not following the inclusive-exclusive convention consistently?
- How does the rendering code handle the conversion of selection coordinates to floating-point values?

*Source: unknown | chunk_id: github_pr_3111_comment_3317945686*
