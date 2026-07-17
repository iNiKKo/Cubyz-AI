# [src/rotation.zig] - PR #1216 review diff

**Type:** review
**Keywords:** rotation.zig, TexturePile, std.StringHashMap, std.AutoHashMapUnmanaged, stateful, virtual functions, architecture
**Symbols:** TexturePile, id, rotatedModels, blockToStateCountMap
**Concepts:** statefulness, virtual functions, architectural design

## Summary
Introduces a new struct `TexturePile` with stateful rotation handling in the `rotation.zig` file.

## Explanation
The change introduces a new struct called `TexturePile` within the `RotationModes` namespace. This struct is designed to manage rotated models and block-to-state mappings using Zig's standard library collections like `std.StringHashMap` and `std.AutoHashMapUnmanaged`. The reviewer highlights a critical architectural concern: this addition makes certain rotations stateful, necessitating the passing of a pointer to the state to all virtual functions that might require it. This could have wide-ranging implications for how these functions are implemented and called throughout the codebase.

## Related Questions
- What is the purpose of the `TexturePile` struct in the `rotation.zig` file?
- How does the introduction of stateful rotations affect virtual functions in Cubyz?
- What are the potential implications of passing a pointer to the state to all virtual functions?
- How does the use of `std.StringHashMap` and `std.AutoHashMapUnmanaged` impact memory management in this context?
- Can you explain the architectural decision behind making certain rotations stateful?
- What changes need to be made to ensure thread safety with the new stateful rotation handling?

*Source: unknown | chunk_id: github_pr_1216_comment_2009118382*
