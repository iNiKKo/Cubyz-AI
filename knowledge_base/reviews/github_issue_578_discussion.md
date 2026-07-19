# [issues/issue_578.md] - Issue #578 discussion

**Type:** review
**Keywords:** 1-block jump, air strafing, spring system, cylindrical collisions, player movement
**Concepts:** gameplay mechanics, jumping physics, collision detection

## Summary
The issue discusses a player's inability to perform 1-block jumps without initially holding forward due to the spring system pushing them too far from the block. The maintainer suggests fixing this by removing side springs and implementing cylindrical collisions.

## Explanation
The issue discusses a player's inability to perform 1-block jumps without initially holding forward due to the current behavior of the spring system pushing them too far from the block. The maintainer suggests fixing this by removing side springs and implementing cylindrical collisions. Removing side springs reduces the distance the player is pushed away, while adding cylindrical collisions improves the accuracy of player positioning during jumps. These changes would allow for more precise control over the player's position relative to blocks during jumps, thereby resolving the inconsistency in gameplay mechanics related to jumping and movement.

## Related Questions
- What is the current behavior of the spring system when the player stands still?
- How does removing side springs affect the player's ability to jump onto blocks?
- Can cylindrical collisions improve the accuracy of player positioning during jumps?
- Is there a specific reason why the spring system pushes the player away from blocks?
- What other gameplay mechanics might be affected by changes to the jumping physics?
- How can we test the impact of these changes on player movement and jumping?

*Source: unknown | chunk_id: github_issue_578_discussion*
