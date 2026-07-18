# [issues/issue_2185.md] - Issue #2185 discussion

**Type:** review
**Keywords:** force-sneak, falling off ledges, collision check, Player.crouching, camera position, ledge
**Symbols:** Player.crouching
**Concepts:** collision detection, camera position adjustment

## Summary
The issue involves a bug where players cannot fall off ledges when force-sneaking due to a gap, as the `Player.crouching` update is conditionally executed based on collision detection.

## Explanation
The root cause of the bug is that the `Player.crouching` state is only updated when the player is not colliding with objects, which affects whether the camera position is adjusted to account for being under a short ceiling. The reviewer suggests moving the `Player.crouching` update outside of the collision check to allow players to fall off ledges while force-sneaking.

## Related Questions
- What is the condition under which `Player.crouching` is updated?
- How does the camera position adjustment depend on `Player.crouching`?
- Why was the `Player.crouching` update originally placed inside the collision check?
- What changes are proposed to fix the bug of not being able to fall off ledges while force-sneaking?
- Could moving the `Player.crouching` update outside the collision check introduce any unintended side effects?
- How does this change impact player behavior when interacting with short ceilings?

*Source: unknown | chunk_id: github_issue_2185_discussion*
