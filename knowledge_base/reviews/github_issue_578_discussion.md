# [issues/issue_578.md] - Issue #578 discussion

**Type:** review
**Keywords:** 1-block jump, air strafing, spring system, cylindrical collisions, player movement
**Concepts:** gameplay mechanics, jumping physics, collision detection

## Summary
The issue discusses a player's inability to perform 1-block jumps without initially holding forward due to the spring system pushing them too far from the block. The maintainer suggests fixing this by removing side springs and implementing cylindrical collisions.

## Explanation
The problem arises because the current spring system in Cubyz pushes the player character too far away from a block when standing still, making it impossible to jump onto it without moving forward first. This inconsistency affects gameplay mechanics related to jumping and movement. The maintainer proposes a solution by eliminating side springs and introducing cylindrical collisions, which would allow for more precise control over the player's position relative to blocks during jumps.

## Related Questions
- What is the current behavior of the spring system when the player stands still?
- How does removing side springs affect the player's ability to jump onto blocks?
- Can cylindrical collisions improve the accuracy of player positioning during jumps?
- Is there a specific reason why the spring system pushes the player away from blocks?
- What other gameplay mechanics might be affected by changes to the jumping physics?
- How can we test the impact of these changes on player movement and jumping?

*Source: unknown | chunk_id: github_issue_578_discussion*
