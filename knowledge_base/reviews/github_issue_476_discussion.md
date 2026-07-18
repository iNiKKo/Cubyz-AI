# [issues/issue_476.md] - Issue #476 discussion

**Type:** review
**Keywords:** f32, f64, fixed point, relative coordinates, precision issues, terrain generation, biome generation, collision detection, integer limit, buggy farlands
**Symbols:** f32, f64, u64, i32
**Concepts:** precision, fixed-point arithmetic, terrain generation, collision detection

## Summary
Discussion on replacing f32 with f64 in terrain generation and exploring alternative fixed-point formats for precision issues.

## Explanation
The issue revolves around the use of f32 floating-point numbers in terrain generation, which causes bugs far out in the world. The maintainers suggest using relative coordinates or fixed-point formats to address this. A u64 fixed point is proposed for high precision, while an i32 fixed point with top 16 bits cut off is considered for other areas. Specifically, for biome generation and collision detection near/at the integer limit, a normal i32 with one block of precision might be sufficient. Relative coordinates are also discussed as a solution that could fix similar issues in collision detection and biome generation.

## Related Questions
- What are the potential benefits and drawbacks of using u64 fixed point in terrain generation?
- How does the i32 fixed point with top 16 bits cut off address precision issues?
- Can relative coordinates solve both terrain generation and collision detection problems?
- What are the implications of not addressing buggy farlands in Cubyz?
- How might using a normal i32 with one block of precision affect biome generation?

*Source: unknown | chunk_id: github_issue_476_discussion*
