# [issues/issue_2707.md] - Issue #2707 discussion

**Type:** review
**Keywords:** crouching, z=-4.1, stuck, hitbox, movement, issue #1831
**Concepts:** bug, player state, hitbox, movement

## Summary
Player gets stuck in crouching state at z=-4.1, affecting hitbox and movement.

## Explanation
The issue describes a bug where the player remains in a crouched state after uncrouching at a specific z-coordinate (-4.1). This causes the player's hitbox to remain that of a crouching player while still being able to move normally. The maintainer suggests this might be related to another issue (#1831), implying a potential shared underlying cause or fix.

## Related Questions
- What is the specific condition that causes the player to get stuck in a crouched state?
- How does the hitbox change when the player gets stuck crouching?
- Are there any known issues with player state transitions at z=-4.1?
- Is there a similar issue reported in #1831?
- What is the intended behavior of the player's hitbox after uncrouching?
- How can we ensure that the player's state transitions correctly at different z-coordinates?

*Source: unknown | chunk_id: github_issue_2707_discussion*
