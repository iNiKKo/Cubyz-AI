# [issues/issue_2766.md] - Issue #2766 discussion

**Type:** review
**Keywords:** damage, death messages, parkour map, instant teleport, overlap death states
**Concepts:** death state, teleportation, gameplay balance

## Summary
The player dies multiple times when taking large damage due to overlapping death states.

## Explanation
The issue arises because the player's death state is not immediately resolved upon impact, allowing them to continue taking damage and dying repeatedly while still in a 'dead' state. This is caused by the delay between the player being marked as dead and their teleportation to the respawn point. The discussion suggests that this behavior is intentional but may need clarification or adjustment for gameplay balance.

## Related Questions
- How is the player's death state currently managed in the code?
- What is the delay between a player being marked as dead and their teleportation to the respawn point?
- Is there any mechanism to prevent overlapping death states?
- How does the game handle multiple damage sources simultaneously?
- Are there any plans to adjust the death mechanics for better gameplay balance?
- Can the teleportation process be made instantaneous to prevent repeated deaths?
- What are the implications of changing the death state management on multiplayer synchronization?
- Is there a way to detect and log overlapping death states for debugging purposes?
- How does the current implementation handle edge cases like rapid consecutive damage?
- Are there any performance considerations when implementing changes to death mechanics?

*Source: unknown | chunk_id: github_issue_2766_discussion*
