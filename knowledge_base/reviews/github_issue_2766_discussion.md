# [issues/issue_2766.md] - Issue #2766 discussion

**Type:** review
**Keywords:** damage, death messages, parkour map, instant teleport, overlap death states
**Concepts:** death state, teleportation, gameplay balance

## Summary
A player can die multiple times when taking large damage due to a delay between being marked as dead and teleporting to the respawn point, causing overlapping death states. This results in repeated deaths while still on the damaging block.

## Explanation
The issue arises because the player's death state is not immediately resolved upon impact with a high-damage block (999 damage). As a result, players can continue taking damage and dying repeatedly while still in a 'dead' state. This behavior occurs due to the delay between being marked as dead and teleporting to the respawn point. The discussion suggests that this behavior is intentional but may need clarification or adjustment for gameplay balance. Specifically, when touching a block dealing 999 damage, players experience multiple death messages (4-8) in the chat because they remain on the damaging block long enough to die again before respawning.

## Related Questions
- What is the exact damage value of the block that causes repeated deaths?
- How many death messages appear when touching a high-damage block?

*Source: unknown | chunk_id: github_issue_2766_discussion*
