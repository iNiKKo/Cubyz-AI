# [src/vec.zig] - PR #1183 review diff

**Type:** review
**Keywords:** rotate2d, vector, rotation, center, optimization, vectorization, Zig, @sin, @cos, position difference
**Symbols:** rotate2d, self, angle, center, @sin, @cos
**Concepts:** vectorization, optimization, performance

## Summary
Added a `rotate2d` function to the `vec.zig` file for rotating 2D vectors around a specified center. The reviewer suggests optimizing the code by pre-calculating the position difference (`self - center`) to ensure vectorization.

## Explanation
The change introduces a new function `rotate2d` that rotates a 2D vector around a given center point. The reviewer is concerned about whether the Zig optimizer will automatically extract and vectorize the subtraction operation (`self[i] - center[i]`). To address this, the reviewer proposes modifying the code to explicitly calculate the position difference (`pos = self - center`) before applying the rotation transformation. This modification aims to ensure that the compiler can optimize the operations for better performance.

## Related Questions
- Does the Zig optimizer automatically vectorize operations like `self[i] - center[i]`?
- How can we ensure that the rotation transformation is optimized for performance in Zig?
- What are the potential benefits of pre-calculating the position difference (`pos = self - center`) before applying the rotation?
- Can you explain the purpose of the `@sin` and `@cos` functions in the `rotate2d` function?
- How does the proposed modification affect the correctness of the `rotate2d` function?
- What are the implications of using vectorized operations for performance in this context?

*Source: unknown | chunk_id: github_pr_1183_comment_1986302969*
