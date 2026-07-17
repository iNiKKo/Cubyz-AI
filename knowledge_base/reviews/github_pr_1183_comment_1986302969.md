# [src/vec.zig] - Chunk 1986302969

**Type:** review
**Keywords:** rotate2d, center, angle, sin, cos, vector, len, compileError, pos, translation, optimizer
**Symbols:** rotate2d, sin, cos, pos
**Concepts:** vector rotation, compile-time type checking, optimizer friendliness, common subexpression elimination, generic functions

## Summary
Added a new `rotate2d` function to rotate 2D vectors around an arbitrary center point, with a compiler error for non-2D types. The reviewer suggested extracting the translation (`self - center`) into a local variable `pos` to improve optimizer friendliness and readability.

## Explanation
The change introduces a generic rotation function that works on any vector type but is restricted to length-2 vectors via a compile-time check. By computing `const pos = self - center;` before the return, we avoid repeating the subtraction in each component expression, which should help Zig's optimizer recognize common subexpressions and potentially emit more efficient SIMD or scalar code. The reviewer’s concern was whether the optimizer would automatically extract the translation; making it explicit guarantees clarity and gives the compiler a clear opportunity to optimize without relying on heuristics that might miss the pattern in complex expressions.

## Related Questions
- What happens if rotate2d is called with a vector of length other than 2?
- How does the function handle negative angles for rotation direction?
- Is there any performance difference between using pos = self - center vs inline subtraction?
- Could this implementation be extended to support 3D rotations around an arbitrary point?
- What are the implications of returning @TypeOf(self) instead of a fixed type?
- Does the function preserve the vector's element type when rotating?
- How does the compiler optimize the multiplication by sin and cos in this context?
- Is there any risk of overflow or precision loss with large rotation angles?
- Can rotate2d be used inside a comptime block for compile-time geometry?
- What is the expected behavior when center equals self (zero rotation offset)?
- How does this function interact with existing vector arithmetic operations in Zig?
- Is there any documentation or comment explaining why pos is extracted separately?

*Source: unknown | chunk_id: github_pr_1183_comment_1986302969*
