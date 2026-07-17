# [src/server/world.zig] - PR #2136 review diff

**Type:** review
**Keywords:** ServerWorld.init, WorldSettings, seed parsing, save_creation, u64, []const u8, architectural review, data handling
**Symbols:** ServerWorld.init, WorldSettings
**Concepts:** architectural refactoring, data consistency

## Summary
Discussion on refactoring `ServerWorld.init` to use `WorldSettings` struct internally for parsing, with confusion about seed storage format.

## Explanation
The reviewer suggests modifying the `ServerWorld.init` function to utilize a new `WorldSettings` struct for internal operations and parsing. This change aims to standardize how world settings are handled within the server. The reviewer expresses confusion regarding why the seed should not be parsed in `save_creation` and stored consistently as a `u64`, rather than sometimes being represented as a `[]const u8` and other times as a `u64`. This inconsistency could lead to potential bugs or complications in handling world data.

## Related Questions
- What is the purpose of refactoring `ServerWorld.init` to use the `WorldSettings` struct?
- Why should the seed be parsed in `save_creation` and stored as a `u64`?
- How does the current implementation of seed storage lead to inconsistencies?
- What are the potential benefits of using the `WorldSettings` struct for parsing?
- Are there any backward compatibility concerns with this refactoring?
- How will this change affect the performance of world initialization?

*Source: unknown | chunk_id: github_pr_2136_comment_2519733282*
