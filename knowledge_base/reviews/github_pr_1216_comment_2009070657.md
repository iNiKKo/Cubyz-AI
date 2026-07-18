# [src/rotation.zig] - PR #1216 review diff

**Type:** review
**Keywords:** rotationModelData, hashmap lookup, generic field, block state, flexibility
**Symbols:** RotationModes, TexturePile, id, rotatedModels, blockToStateCountMap
**Concepts:** performance optimization, architectural design, data structure choice

## Summary
A new `TexturePile` struct is introduced within the `RotationModes` in `rotation.zig`, which includes fields for managing rotated models and block state counts.

## Explanation
The reviewer suggests adding a generic field to each block to store additional rotation model data, rather than using hashmaps. This approach aims to reduce the overhead of hashmap lookups and anticipates potential future needs for other rotation modes with extra states. The introduction of `TexturePile` struct is part of an architectural decision to optimize performance and maintain flexibility for future enhancements.

## Related Questions
- What is the purpose of the `TexturePile` struct in `rotation.zig`?
- How does the introduction of `TexturePile` impact memory usage per block?
- Why was a hashmap lookup considered inefficient in this context?
- What future rotation modes are anticipated to benefit from this change?
- How might the addition of more generic fields affect backwards compatibility?
- Can you explain the reasoning behind choosing `std.StringHashMap` and `std.AutoHashMapUnmanaged` for `rotatedModels` and `blockToStateCountMap` respectively?

*Source: unknown | chunk_id: github_pr_1216_comment_2009070657*
