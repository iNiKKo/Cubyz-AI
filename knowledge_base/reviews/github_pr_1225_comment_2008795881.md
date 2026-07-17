# [src/blueprint.zig] - PR #1225 review diff

**Type:** review
**Keywords:** rotateZ, blueprint rotation, Z-axis, tuple destructuring, compact code
**Symbols:** Blueprint, rotateZ, NeverFailingAllocator, Degrees
**Concepts:** rotation transformation, tuple destructuring

## Summary
Added a `rotateZ` function to the Blueprint struct for rotating blueprints around the Z-axis by specified angles.

## Explanation
The change introduces a new method `rotateZ` in the Blueprint struct, which allows for rotating the blueprint around the Z-axis by 0, 90, 180, or 270 degrees. The function initializes a new Blueprint with dimensions adjusted based on the rotation angle and then maps the original blocks to their new positions according to the rotation logic. The reviewer suggests using tuple destructuring for more compact code, which could improve readability and maintainability.

## Related Questions
- What is the purpose of the `rotateZ` function in the Blueprint struct?
- How does the `rotateZ` function handle different rotation angles?
- Why was tuple destructuring suggested for improving the code?
- What are the dimensions of the new Blueprint after a 90-degree rotation?
- How does the function map original blocks to their new positions during rotation?
- Can you explain the logic behind the x and y coordinate calculations in the `rotateZ` function?

*Source: unknown | chunk_id: github_pr_1225_comment_2008795881*
