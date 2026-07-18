# [src/blueprint.zig] - PR #1225 review diff

**Type:** review
**Keywords:** rotateZ, blueprint rotation, trigonometry, optimizer, performance optimization, z loop
**Symbols:** Blueprint, rotateZ, NeverFailingAllocator, Degrees, init, get, @round, @sin, @cos
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added a `rotateZ` method to the Blueprint struct for rotating blueprints around the Z-axis.

## Explanation
The change introduces a new method `rotateZ` in the Blueprint struct, which allows rotating a blueprint by specified angles (0, 90, 180, 270 degrees) around the Z-axis. The method initializes a new Blueprint with dimensions adjusted based on the rotation angle and then iterates over each block to compute its new position using trigonometric functions. The reviewer suggests that the optimizer might automatically move certain variables outside the z loop for performance optimization.

## Related Questions
- What is the purpose of the `rotateZ` method in the Blueprint struct?
- How does the method handle different rotation angles (0, 90, 180, 270 degrees)?
- Why are the variables `newX` and `newY` computed inside the z loop?
- What is the role of the optimizer in this code snippet?
- How does the method ensure memory safety during rotation?
- Can you explain the use of trigonometric functions in the rotation calculation?

*Source: unknown | chunk_id: github_pr_1225_comment_2008761929*
