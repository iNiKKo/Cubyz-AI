# [src/server/command/worldedit/selection.zig] - PR #3313 review diff

**Type:** review
**Keywords:** world edit, selection commands, normalization, cube creation, shrinking, performance, O(n^2) complexity, useless commands, player creativity
**Symbols:** selection, normalize, cube, shrink, Block, command, User, Vec3i
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The code introduces new world edit selection commands in Cubyz, including normalization, cube creation, and shrinking with limits.

## Explanation
The code introduces new world edit selection commands in Cubyz, including normalization, cube creation, and shrinking with limits.

The review discusses the addition of several world edit selection commands to the Cubyz server. The 'normalize' command ensures that the selection's positions are set correctly by setting pos1 to minimal coordinates and pos2 to maximal coordinates from the selection. The 'cube' command creates a cubic selection centered on the player's position with a specified radius (default is 5). The 'shrink' command reduces the selection size by a given limit (default is 32), preventing long iterations and potential performance issues due to O(n^2) complexity of scanning perpendicular plane. The reviewer suggests keeping these commands despite concerns about cluttering the help output, citing specific use cases where they are beneficial.

## Related Questions
- What is the purpose of the 'normalize' command in the selection.zig file?
- How does the 'cube' command determine its center position?
- Why is there a limit on the 'shrink' command, and what potential issues could arise without it?
- Can you explain the performance considerations mentioned for the 'shrink' command?
- What are the specific use cases where the 'shrink' command is beneficial over other methods?
- How does the reviewer justify keeping these commands despite concerns about cluttering the help output?

*Source: unknown | chunk_id: github_pr_3313_comment_3556985210*
