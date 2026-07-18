# [issues/issue_1831.md] - Issue #1831 discussion

**Type:** review
**Keywords:** bug, teleportation, coordinates, powers of two, boundary check
**Concepts:** coordinate system, teleportation mechanics

## Summary
The issue describes a bug where teleportation fails at specific coordinates, particularly powers of two.

## Explanation
The discussion indicates that the bug occurs when attempting to teleport to or through blocks located at coordinates that are powers of two. The maintainer notes that this happens for both x and y directions, suggesting a potential issue with how coordinate calculations or boundary checks are handled in the teleportation logic.

## Related Questions
- What specific calculations are involved in the teleportation logic?
- Are there any known issues with handling powers of two coordinates in the current implementation?
- How do boundary checks affect teleportation at these problematic coordinates?
- Is there a pattern or common cause for this bug across different parts of the codebase?
- What steps can be taken to ensure that teleportation works correctly for all valid coordinate values?
- Are there any existing tests that cover teleportation scenarios, and if so, how do they handle edge cases like these?

*Source: unknown | chunk_id: github_issue_1831_discussion*
