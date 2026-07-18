# [issues/issue_2185.md] - Issue #2185 discussion

**Type:** review
**Keywords:** force-sneak, falling off ledges, collision check, Player.crouching, camera position, ledge
**Symbols:** Player.crouching
**Concepts:** collision detection, camera position adjustment

## Summary
The issue involves a bug where players cannot fall off ledges when force-sneaking due to a gap, as the `Player.crouching` update is conditionally executed based on collision detection.

## Explanation
The issue involves a bug where players cannot fall off ledges when force-sneaking due to a 1.5 block-high gap, as the `Player.crouching` state is only updated when not colliding with objects. The root cause of this behavior is that the `Player.crouching` update is conditionally executed based on collision detection and does not depend on whether the sneak key is pressed or not. This results in players being unable to fall off ledges while under a short ceiling, as the camera position adjustment for crouching is not properly handled when force-sneaking. The reviewer suggests moving the `Player.crouching` update outside of the collision check so that it can be updated regardless of whether the player is colliding with objects, allowing players to fall off ledges while force-sneaking.

## Related Questions
- What is the condition under which `Player.crouching` is updated?
- How does the camera position adjustment depend on `Player.crouching`?
- Why was the `Player.crouching` update originally placed inside the collision check?
- What changes are proposed to fix the bug of not being able to fall off ledges while force-sneaking?
- Could moving the `Player.crouching` update outside the collision check introduce any unintended side effects?
- How does this change impact player behavior when interacting with short ceilings?

*Source: unknown | chunk_id: github_issue_2185_discussion*
