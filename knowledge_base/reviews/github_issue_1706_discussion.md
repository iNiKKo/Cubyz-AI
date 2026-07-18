# [issues/issue_1706.md] - Issue #1706 discussion

**Type:** review
**Keywords:** velocity, eye velocity, climbing, ground friction, swimming in air, resolved
**Concepts:** physics engine, friction, player movement

## Summary
The issue of velocity and eye velocity flutters when climbing up a block is caused by the player attempting to 'swim' in the air due to non-directional ground friction.

## Explanation
The problem arises because the game's physics engine does not correctly handle directional friction, allowing the player to move upward even when grounded. This unintended behavior leads to velocity and eye velocity fluctuations during climbing. The maintainer notes that this issue has been resolved.

## Related Questions
- What is the cause of the player's ability to 'swim' in the air?
- How does the ground friction contribute to this issue?
- Is there a specific part of the code that handles directional friction?
- How was this issue resolved?
- Are there any other areas in the physics engine that might need similar adjustments?
- What tests were conducted to verify the resolution of this issue?

*Source: unknown | chunk_id: github_issue_1706_discussion*
