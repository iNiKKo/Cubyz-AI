# [src/blueprint.zig] - PR #1225 review diff

**Type:** review
**Keywords:** rotateZ, blueprint rotation, Z-axis, trigonometry, loop optimization, allocator usage
**Symbols:** Blueprint, rotateZ, NeverFailingAllocator, Degrees
**Concepts:** rotation transformation, trigonometric calculations, performance optimization

## Summary
Added a `rotateZ` function to the Blueprint struct for rotating blueprints around the Z-axis.

## Explanation
The change introduces a new method `rotateZ` that allows rotating a blueprint by specified angles (0, 90, 180, 270 degrees) around the Z-axis. The function initializes a new Blueprint with dimensions adjusted based on the rotation angle and then iterates over each block in the original blueprint to compute its new position after rotation using trigonometric functions. The reviewer suggests that the computation of `newX` and `newY` should be moved outside the innermost loop (z-loop) for potential performance optimization, as these variables do not depend on the z index.

## Related Questions
- What is the purpose of the `rotateZ` function in the Blueprint struct?
- How does the function handle different rotation angles (0, 90, 180, 270 degrees)?
- Why are trigonometric functions used to compute new block positions after rotation?
- What potential performance issue is being addressed by moving `newX` and `newY` computations outside the z-loop?
- How does the function ensure that the rotated blueprint maintains its original dimensions?
- Can you explain the role of the allocator in this context?

*Source: unknown | chunk_id: github_pr_1225_comment_2008761929*
