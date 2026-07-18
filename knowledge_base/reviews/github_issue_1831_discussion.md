# [issues/issue_1831.md] - Issue #1831 discussion

**Type:** review
**Keywords:** bug, teleportation, coordinates, powers of two, boundary check
**Concepts:** coordinate system, teleportation mechanics

## Summary
The issue describes a teleportation bug that happens when moving into or through blocks located at specific coordinates, particularly at -1 and other powers of two values.

## Explanation
The discussion indicates that the bug occurs specifically when attempting to move into a block at coordinate -1 in either x or y directions. Moving in the opposite direction from this position causes teleportation into the block. The maintainer notes that similar issues happen for more power-of-two coordinates, suggesting potential problems with how coordinate calculations or boundary checks are handled in the teleportation logic.

## Related Questions
- What specific steps reproduce the bug at coordinate -1?
- How does moving in opposite directions cause teleportation into a block?

*Source: unknown | chunk_id: github_issue_1831_discussion*
