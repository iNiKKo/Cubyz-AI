# [src/server/command/worldedit/set.zig] - PR #1236 review diff

**Type:** review
**Keywords:** seed calculation, position coordinates, unnecessary complexity, copy paste, direct usage
**Symbols:** std, main, User, Pattern, Block, Blueprint, description, usage, execute, args, source, pos1, pos2, seed
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The reviewer suggests removing a complex seed calculation in favor of simpler copying or direct usage.

## Explanation
The reviewer suggests removing a complex seed calculation in favor of simpler copying or direct usage. The specific seed calculation formula used is `var seed: u64 = @as(u64, @intCast(pos1[0])) ^ (@as(u64, @intCast(pos1[1])) << 15) ^ (@as(u64, @intCast(pos1[2])) << 31);`. They recommend either directly copying the structure or using the seed for other specific purposes, implying that the current implementation may be redundant or unclear in its intent. The purpose of the seed calculation is not explicitly stated in the raw content but is part of the execute function. Removing the seed calculation could affect the functionality of the set command by potentially altering how selections are handled or processed. There are no other parts of the code mentioned as relying on this seed calculation. The performance implications of simplifying the seed calculation are not discussed, but it may lead to more efficient execution if the seed is unnecessary. The seed can be used for specific purposes in the worldedit module, although these purposes are not detailed. This change could impact backwards compatibility with existing scripts or plugins that depend on the current implementation.

## Related Questions
- What is the purpose of the seed calculation in the execute function?
- How does removing the seed calculation affect the functionality of the set command?
- Are there any other parts of the code that rely on this seed calculation?
- What are the potential performance implications of simplifying the seed calculation?
- Can the seed be used for any specific purposes in the worldedit module?
- How does this change impact backwards compatibility with existing scripts or plugins?

*Source: unknown | chunk_id: github_pr_1236_comment_2020183493*
