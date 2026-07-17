# [src/rotation.zig] - PR #1216 review diff

**Type:** review
**Keywords:** rotationModelData, generic field, bytes per block, hashmap lookup, top-attached torch, ModelIndex, std.StringHashMap, std.AutoHashMapUnmanaged
**Symbols:** RotationModes, TexturePile, id, rotatedModels, blockToStateCountMap
**Concepts:** performance optimization, data storage, hashmap usage

## Summary
A new `TexturePile` struct is introduced in the `RotationModes` enum, adding fields for managing rotated models and block-to-state counts.

## Explanation
The reviewer suggests incorporating a generic field into the block structure to store additional state information, such as rotation model data. This would eliminate the need for hashmap lookups, potentially improving performance. The reviewer also notes that this change is likely to be beneficial for future features, such as allowing top-attached torch rotations.

## Related Questions
- What is the purpose of the `TexturePile` struct in the `RotationModes` enum?
- How does the introduction of a generic field in the block structure improve performance?
- Why are hashmap lookups being avoided in this change?
- What future features might benefit from the additional state storage introduced here?
- How many bytes per block are being added to store rotation model data?
- What is the expected impact on memory usage with this change?

*Source: unknown | chunk_id: github_pr_1216_comment_2009070657*
