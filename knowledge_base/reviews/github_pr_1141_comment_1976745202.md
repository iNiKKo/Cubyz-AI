# [src/server/command/worldedit/pos1.zig] - PR #1141 review diff

**Type:** review
**Keywords:** worldedit, position storage, user struct, multi-user environment, thread safety, backwards compatibility
**Symbols:** pos, Vec3i, User
**Concepts:** thread safety, backwards compatibility

## Summary
The review suggests moving worldedit position storage from a command file to the user struct to prevent multiple users from overriding each other's positions.

## Explanation
The reviewer points out that storing worldedit positions in the command file is not suitable for a multi-user environment, as it could lead to one user's position being overwritten by another. The proposed solution is to store these positions within the user struct, using `source.pos1` and `source.pos2`, which would ensure that each user has their own set of positions without interference from others.

## Related Questions
- How can we ensure that each user's worldedit positions are stored separately?
- What changes need to be made to the user struct to accommodate worldedit positions?
- How will this change affect the existing command system?
- Are there any potential performance implications of storing positions in the user struct?
- How can we prevent race conditions when multiple users update their positions simultaneously?
- What steps should be taken to ensure backwards compatibility with existing scripts?

*Source: unknown | chunk_id: github_pr_1141_comment_1976745202*
