# [issues/issue_700.md] - Issue #700 discussion

**Type:** review
**Keywords:** i32, player coordinates, memory usage, world size, int16, int8, math operators, conversions
**Concepts:** memory usage, fixed-point arithmetic

## Summary
Discussion on using `i32` fixed-point player coordinates for reduced memory usage and potential improvements in world size.

## Explanation
The issue discusses the viability of using `i32` fixed-point integers for player coordinates to reduce memory usage. The user initially suggests considering `int16` with additional precision fields, but later clarifies that `i32` is intended. The maintainer expresses difficulty in performing mathematical operations and conversions without specialized operators, leading to the conclusion that the effort may not be worthwhile.

## Related Questions
- What are the potential memory savings from using `i32` fixed-point coordinates?
- How does the precision of `i32` compare to other integer types for player movement within blocks?
- What specific mathematical operations become challenging with fixed-point arithmetic in this context?
- Are there any existing libraries or tools that simplify fixed-point math in Cubyz?
- How might the world size be affected by using less precise coordinates?
- What are the trade-offs between memory usage and precision for player coordinates?
- Could the use of fixed-point numbers introduce any performance bottlenecks?
- Is there a way to balance memory efficiency with sufficient precision for player movement?
- How does the current implementation handle coordinate conversions between different systems?
- Are there any potential compatibility issues with existing code when changing coordinate types?

*Source: unknown | chunk_id: github_issue_700_discussion*
