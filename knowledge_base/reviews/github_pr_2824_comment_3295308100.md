# [src/vec.zig] - PR #2824 review diff

**Type:** review
**Keywords:** sincos32, minimax approximation, quaternion, axis-angle, performance, math library, struct organization
**Symbols:** sincos32, Vec3f, Vec4f
**Concepts:** performance optimization, trigonometric approximation, quaternions

## Summary
Added `sincos32` function for efficient sine and cosine calculation, copied from zmath library. Also started implementing `quatFromAxisAngle` function.

## Explanation
The change introduces a new function `sincos32` which calculates both sine and cosine of a given angle using minimax polynomial approximations. This is optimized for performance by reducing the number of trigonometric operations. The function is copied from the zmath library, adhering to its MIT license. Additionally, the implementation of `quatFromAxisAngle` begins, which converts an axis-angle representation into a quaternion. The reviewer suggests encapsulating related calculations within a struct to improve organization and potentially enhance performance by reducing redundant computations.

The `sincos32` function uses a 11-degree minimax approximation for sine calculation and a 10-degree minimax approximation for cosine calculation. These approximations are implemented using polynomial expressions that minimize the error over a specified range of angles. The exact polynomial expressions used in the approximations are as follows:

For sine calculation (11-degree minimax approximation):
```zig
var sinv = @mulAdd(f32, @as(f32, -2.3889859e-08), y2, 2.7525562e-06);
sinv = @mulAdd(f32, sinv, y2, -0.00019840874);
sinv = @mulAdd(f32, sinv, y2, 0.0083333310);
sinv = @mulAdd(f32, sinv, y2, -0.16666667);
sinv = y*@mulAdd(f32, sinv, y2, 1.0);
```

For cosine calculation (10-degree minimax approximation):
```zig
var cosv = @mulAdd(f32, @as(f32, -2.6051615e-07), y2, 2.4760495e-05);
cosv = @mulAdd(f32, cosv, y2, -0.0013888378);
cosv = @mulAdd(f32, cosv, y2, 0.041666638);
cosv = @mulAdd(f32, cosv, y2, -0.5);
cosv = sign*@mulAdd(f32, cosv, y2, 1.0);
```

The function handles angles outside the primary range by normalizing them to fall within one period of the trigonometric functions.

The `quatFromAxisAngle` function is being implemented to convert an axis-angle representation into a quaternion, which is a mathematical entity used to represent rotations in 3D space. The implementation details are not fully provided in the diff but involve normalizing the axis vector and using the angle to compute the quaternion components.

The reviewer suggests organizing related calculations within a struct to improve code organization and potentially enhance performance by reducing redundant computations. This could involve grouping functions like `sincos32` and `quatFromAxisAngle` into a single struct, which would allow for more efficient access and manipulation of related data.

## Related Questions
-  What is the purpose of the `sincos32` function?
-  How does the minimax approximation improve performance in trigonometric calculations?
-  Why was the `quatFromAxisAngle` function implementation started?
-  What are the potential benefits of organizing related calculations within a struct?
-  How does the `sincos32` function handle angles outside the primary range?
-  What is the significance of the MIT license in this code addition?
-  How might the `quatFromAxisAngle` function be completed?
-  Are there any potential precision issues with the minimax approximation used in `sincos32`?
-  How does the struct organization suggested by the reviewer impact memory usage?
-  What are the implications of copying functions from external libraries like zmath?

*Source: unknown | chunk_id: github_pr_2824_comment_3295308100*
