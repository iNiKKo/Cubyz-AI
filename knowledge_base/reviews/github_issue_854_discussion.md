# [issues/issue_854.md] - Issue #854 discussion

**Type:** review
**Keywords:** fence collision, teleportation, elevator exploit, block placement, player hitbox
**Concepts:** collision detection, player movement, game physics

## Summary
Fences lack collision checks when connecting, allowing players to be teleported inside them.

## Explanation
The issue arises because the fence placement logic does not account for the player's position relative to neighboring fences. This oversight leads to a situation where placing a fence next to another can cause the player to be inside the fence structure, forcing them upwards. The maintainer notes that this behavior can be exploited to create an elevator-like effect by stacking fences in a column and mentions it only requires a single block column if done correctly. Additionally, the maintainer confirms that the issue is similar to what was demonstrated in the video where a player stood next to a fence underground and placed another next to it.

## Related Questions
-  What specific conditions are required for the elevator exploit with fences?
-  How does the current logic for checking fence collisions fail when placing adjacent fences?

*Source: unknown | chunk_id: github_issue_854_discussion*
