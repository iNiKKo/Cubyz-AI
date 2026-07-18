# [src/server/world.zig] - PR #2136 review diff

**Type:** review
**Keywords:** ServerWorld.init, WorldSettings, seed parsing, data storage, u64, []const u8, architectural decision
**Symbols:** ServerWorld.init, WorldSettings
**Concepts:** architectural review, data consistency

## Summary
Discussion about adjusting `ServerWorld.init` to use `WorldSettings` struct internally and for parsing, with confusion over seed storage format.

## Explanation
The reviewer is questioning the architectural decision to modify `ServerWorld.init` to utilize the new `WorldSettings` struct. They express confusion regarding why it wouldn't be more logical to parse the seed during save creation and store it consistently as a `u64` instead of sometimes as a `[]const u8` and other times as a `u64`. The reviewer is seeking clarification on the rationale behind these changes.

## Related Questions
- Why was the decision made to adjust `ServerWorld.init` to use the `WorldSettings` struct?
- What are the benefits of parsing the seed during save creation and storing it as a `u64`?
- How does using the `WorldSettings` struct internally in `ServerWorld.init` improve the architecture?
- Are there any potential drawbacks to changing the seed storage format to always be a `u64`?
- What is the purpose of the `WorldSettings` struct in this context?
- How does the current implementation of seed parsing and storage impact performance or correctness?

*Source: unknown | chunk_id: github_pr_2136_comment_2519733282*
