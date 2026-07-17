# [src/game.zig] - PR #705 review diff

**Type:** review
**Keywords:** sprint, ghost, flying, movement speed, direction, update function, KeyBoard.key, Vec3d, load(.monotonic)
**Symbols:** update, KeyBoard.key, forward, right, movementSpeed, movementDir, Player.isGhost.load, Player.isFlying.load
**Concepts:** code duplication, refactoring, player state management

## Summary
The update function in game.zig has been modified to include sprinting mechanics for different player states (ghost, flying, normal). The reviewer suggests refactoring to avoid code duplication.

## Explanation
The change introduces conditional logic to adjust movement speed and direction based on whether the 'sprint' key is pressed and the player's state (ghost, flying, or normal). This allows for different speeds in each state. The reviewer points out that the current implementation involves duplicating code four times, which could be refactored for better maintainability and elegance.

## Related Questions
- How does the sprinting mechanic affect movement speed in different player states?
- What is the purpose of using `Player.isGhost.load(.monotonic)` and `Player.isFlying.load(.monotonic)`?
- Why was the reviewer concerned about code duplication in this section?
- Can you explain the logic behind setting `movementSpeed` to different values based on player state?
- How might refactoring this code improve maintainability?
- What potential performance impacts could arise from the current implementation?

*Source: unknown | chunk_id: github_pr_705_comment_1750751223*
