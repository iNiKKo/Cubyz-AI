# [src/Inventory.zig] - PR #1251 review diff

**Type:** review
**Keywords:** Inventory.zig, UpdateBlock, dropDirection, Vec3d, f32, normalized coordinates, velocity, performance considerations
**Symbols:** Command, UpdateBlock, source, pos, dropDirection, Vec3i, Vec3d
**Concepts:** architectural review, premature optimization, non-pessimization

## Summary
Added `dropDirection` field to `UpdateBlock` struct with default value `Vec3d{0, 0, 1}`.

## Explanation
The change introduces a new field `dropDirection` in the `UpdateBlock` struct within the `Inventory.zig` file. This field is initialized with a default value of `Vec3d{0, 0, 1}`. The reviewer suggests that adding velocity might be beneficial for future enhancements but considers it premature optimization due to potential code complexity and infrequent usage. The switch to using `f32` instead of normalizing coordinates is described as 'non-pessimization' by Casey Muratori, implying a cautious approach to performance considerations.

## Related Questions
- What is the purpose of adding `dropDirection` to the `UpdateBlock` struct?
- Why was it decided not to normalize the coordinates?
- How might adding velocity in the future affect the codebase?
- What does 'non-pessimization' mean in this context?
- Is there a section about performance considerations in the contributing guidelines?
- How often is the `UpdateBlock` struct likely to be called?

*Source: unknown | chunk_id: github_pr_1251_comment_2023618686*
