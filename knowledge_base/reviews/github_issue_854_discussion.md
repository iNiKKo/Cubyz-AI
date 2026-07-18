# [issues/issue_854.md] - Issue #854 discussion

**Type:** review
**Keywords:** fence collision, teleportation, elevator exploit, block placement, player hitbox
**Concepts:** collision detection, player movement, game physics

## Summary
Fences lack collision checks when connecting, allowing players to be teleported inside them.

## Explanation
The issue arises because the fence placement logic does not account for the player's position relative to neighboring fences. This oversight leads to a situation where placing a fence next to another can cause the player to be inside the fence structure, forcing them upwards. The maintainer notes that this behavior can be exploited to create an elevator-like effect by stacking fences in a column.

## Related Questions
- What is the current logic for checking fence collisions?
- How can we modify the fence placement logic to prevent players from being inside fences?
- Are there any other game elements that might have similar collision issues?
- Can we implement a check to ensure that no player can be trapped inside a fence structure?
- What are the potential performance implications of adding additional collision checks for fences?
- How does this issue affect multiplayer gameplay and synchronization?

*Source: unknown | chunk_id: github_issue_854_discussion*
