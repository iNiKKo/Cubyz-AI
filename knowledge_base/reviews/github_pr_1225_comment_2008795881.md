# [src/blueprint.zig] - PR #1225 review diff

**Type:** review
**Keywords:** rotateZ, blueprint rotation, tuple destructuring, switch statement, block mapping
**Symbols:** Blueprint, rotateZ, NeverFailingAllocator, Degrees
**Concepts:** rotation transformation, tuple destructuring

## Summary
Added a `rotateZ` function to the Blueprint struct for rotating blueprints around the Z-axis.

## Explanation
The change introduces a new method `rotateZ` that allows rotating a blueprint by specified angles (0, 90, 180, 270 degrees) around the Z-axis. The function initializes a new Blueprint with dimensions adjusted based on the rotation angle and then maps the original blocks to their new positions in the rotated blueprint. The reviewer suggests using tuple destructuring for more compact code.

## Related Questions
- What is the purpose of the `rotateZ` function in the Blueprint struct?
- How does the `rotateZ` function handle different rotation angles?
- Why was tuple destructuring suggested for improving code compactness?
- What are the dimensions of the new Blueprint after a 90-degree rotation?
- How is block mapping handled during the rotation process?
- Can you explain the logic behind the switch statement in the `rotateZ` function?

*Source: unknown | chunk_id: github_pr_1225_comment_2008795881*
