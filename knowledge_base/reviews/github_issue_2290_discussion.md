# [issues/issue_2290.md] - Issue #2290 discussion

**Type:** review
**Keywords:** game crash, seed value, type mismatch, ZonElement.Int, u64, i64, world creation, conflict resolution
**Symbols:** ZonElement.Int, givin, u64, i64, seed, world.zig.zon, Zon.ParseNumber
**Concepts:** type safety, data type mismatch, bug reproduction

## Summary
The game crashes when creating a world with a specific seed due to type mismatch between expected i64 and provided u64 values.

## Explanation
The game crashes when creating a world with a specific seed due to a type mismatch between expected i64 and provided u64 values. The issue arises because ZonElement.Int expects an i64, but the seed value is treated as a u64. This discrepancy causes the game to crash when processing the seed. Additionally, there's a 50/50 chance you can't open a newly created world more than one time with this bug since Zon.ParseNumber uses an i64 and the seed is a u64. The problem was initially uncovered by #2136 but is not directly caused by it. There may also be a conflict with another issue (#2251) that needs to be addressed.

## Related Questions
- What is the expected data type for seed values in ZonElement.Int?
- How does the game handle u64 values when expecting i64?
- Is there a way to convert u64 to i64 without losing information?
- What other issues might conflict with this fix?
- How can we ensure that the seed value is consistently treated as i64 throughout the codebase?
- Are there any similar type mismatch issues in other parts of the game?
- How does Zon.ParseNumber handle large numbers, and could it be modified to support u64?
- What steps should be taken to prevent future type mismatch bugs?
- Is there a need for additional validation when setting seed values?
- How can we test the fix for this issue without causing regressions in other areas?

*Source: unknown | chunk_id: github_issue_2290_discussion*
