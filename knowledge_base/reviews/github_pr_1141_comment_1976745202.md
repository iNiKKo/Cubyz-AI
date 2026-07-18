# [src/server/command/worldedit/pos1.zig] - PR #1141 review diff

**Type:** review
**Keywords:** worldedit, position storage, user struct, conflict prevention, data association
**Symbols:** pos, Vec3i, User
**Concepts:** data isolation, user session management

## Summary
The reviewer suggests moving worldedit position storage from a command file to the user struct to prevent multiple users from overriding each other's positions.

## Explanation
The current implementation stores worldedit positions in the command file, which can lead to conflicts when multiple users attempt to set their positions simultaneously. The reviewer recommends storing these positions within the user struct instead, using `source.pos1` and `source.pos2`. This change aims to improve data isolation and prevent unintended overrides, ensuring that each user's position is correctly associated with their session.

## Related Questions
- How does the current implementation handle multiple users setting positions simultaneously?
- What are the potential issues with storing worldedit positions in a command file?
- Why is it recommended to store position data within the user struct?
- How can we ensure that each user's position is correctly associated with their session?
- What changes need to be made to prevent unintended overrides of worldedit positions?
- How will moving the position storage affect the overall architecture of the worldedit commands?

*Source: unknown | chunk_id: github_pr_1141_comment_1976745202*
