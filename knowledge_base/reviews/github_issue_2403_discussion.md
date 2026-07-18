# [issues/issue_2403.md] - Issue #2403 discussion

**Type:** review
**Keywords:** camera rotation, command-line, player direction, minigames, testing, yaw, pitch, Vec3f
**Symbols:** /tp, yaw, pitch, Vec3f
**Concepts:** Command-line Interface (CLI), Player Movement, Game Testing

## Summary
Discussion about adding a camera rotation feature to the `/tp` command in Cubyz.

## Explanation
The discussion revolves around adding functionality to the `/tp` command to allow setting the player's direction of view using yaw and pitch angles. The maintainer suggests integrating this into the existing `/tp` command, citing use cases such as aligning players for minigames and testing. It is noted that Cubyz stores rotation information as a `Vec3f`, implying that the new arguments should be handled similarly.

## Related Questions
- How is the `/tp` command currently implemented in Cubyz?
- What are the potential use cases for adding camera rotation to the `/tp` command?
- Why does Cubyz store rotation as a `Vec3f`?
- How would integrating yaw and pitch into the `/tp` command affect existing functionality?
- Are there any backward compatibility concerns with this change?
- What are the implications of using `Vec3f` for storing camera rotation?

*Source: unknown | chunk_id: github_issue_2403_discussion*
