# [src/server/command/_command.zig] - PR #2825 review diff

**Type:** review
**Keywords:** selection bounds, struct, vector, minPos, maxPos, explicitness, readability, ambiguity
**Symbols:** getSelectionBounds, User, Vec3i, main.vec.Vec3i
**Concepts:** code clarity, data structure design

## Summary
A new function `getSelectionBounds` is added to return selection bounds as a struct instead of a vector for explicitness.

## Explanation
The reviewer suggests returning a struct with `minPos` and `maxPos` fields instead of using a vector to represent selection bounds. This change aims to make the code more explicit and distinguish between arbitrary positions and normalized min/max positions, potentially improving readability and reducing ambiguity.

## Related Questions
- What is the purpose of the `getSelectionBounds` function?
- Why does the reviewer prefer using a struct instead of a vector for selection bounds?
- How might this change impact existing code that uses selection bounds?
- Can you provide an example of how the new struct would be used in practice?
- What are the potential benefits and drawbacks of using a struct for selection bounds?
- How does this change align with the overall architecture of the Cubyz project?

*Source: unknown | chunk_id: github_pr_2825_comment_3039239737*
