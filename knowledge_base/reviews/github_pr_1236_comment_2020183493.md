# [src/server/command/worldedit/set.zig] - PR #1236 review diff

**Type:** review
**Keywords:** seed calculation, position coordinates, unnecessary complexity, copy paste, direct usage
**Symbols:** std, main, User, Pattern, Block, Blueprint, description, usage, execute, args, source, pos1, pos2, seed
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The reviewer suggests removing a complex seed calculation in favor of simpler copying or direct usage.

## Explanation
The reviewer suggests removing a complex seed calculation in favor of simpler copying or direct usage. The specific seed calculation formula used is `var seed: u64 = @as(u64, @intCast(pos1[0])) ^ (@as(u64, @intCast(pos1[1])) << 15) ^ (@as(u64, @intCast(pos1[2])) << 31);`. They recommend either directly copying the structure or using the seed for other specific purposes, implying that the current implementation may be redundant or unclear in its intent.

## Related Questions
- What is the purpose of the seed calculation in the execute function?
- How does removing the seed calculation affect the functionality of the set command?
- Are there any other parts of the code that rely on this seed calculation?
- What are the potential performance implications of simplifying the seed calculation?
- Can the seed be used for any specific purposes in the worldedit module?
- How does this change impact backwards compatibility with existing scripts or plugins?

*Source: unknown | chunk_id: github_pr_1236_comment_2020183493*
