# [src/vec.zig] - PR #2824 review diff

**Type:** review
**Keywords:** sincos32, quatFromAxisAngle, vector alias, struct, quaternion, axis-angle, minimax polynomial, MIT License
**Symbols:** sincos32, quatFromAxisAngle, Vec3f, Vec4f
**Concepts:** minimax approximation, quaternion representation, type safety

## Summary
Added `sincos32` function and began implementing `quatFromAxisAngle` in `vec.zig`. The reviewer questions whether to use a vector alias or a struct for the quaternion representation.

## Explanation
The change introduces a new function `sincos32`, which computes both sine and cosine of a given angle using minimax polynomial approximations. This function is copied from the zmath library under the MIT License. The reviewer also initiates the implementation of `quatFromAxisAngle`, which converts an axis-angle representation to a quaternion. The architectural concern raised by the reviewer pertains to the choice between using a vector alias or a struct for representing quaternions, suggesting that each option has its own trade-offs in terms of type safety and clarity.

## Related Questions
- What is the purpose of the `sincos32` function in this code?
- How does the minimax approximation work in the `sincos32` function?
- Why was the `quatFromAxisAngle` function being implemented?
- What are the advantages and disadvantages of using a vector alias for quaternions?
- What are the advantages and disadvantages of using a struct for quaternions?
- How does the choice between a vector alias and a struct affect type safety in this context?

*Source: unknown | chunk_id: github_pr_2824_comment_3295193376*
