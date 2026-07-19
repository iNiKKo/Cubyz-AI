# [src/game.zig] - PR #665 review diff

**Type:** review
**Keywords:** view bobbing, exponential smoothing, bobVel, bobTime, horizontalMovementSpeed, mutex, thread safety, interpolation, damping factor, Player struct
**Symbols:** update, deltaTime, Player.selectedSlot, main.Window.scrollOffset, fac, targetBobVel, horizontalMovementSpeed, vec.length(vec.xy(Player.getVelBlocking())), Player.bobVel, settings.viewBobStrength, Player.onGround, Player.bobTime, Player.bobMag
**Concepts:** thread safety, smoothing, interpolation, mutex

## Summary
Added view bobbing effect based on player movement speed and ground state.

## Explanation
The change introduces a new feature called 'view bobbing' which simulates the up-and-down motion of a camera when a player is walking. The implementation uses exponential smoothing to interpolate the bobbing velocity (`bobVel`) and time (`bobTime`). It calculates the target bobbing velocity based on the horizontal movement speed of the player, applying a damping factor to ensure smooth transitions.

The `fac` variable is calculated as `1 - std.math.exp(-15 * deltaTime)`, which serves as a damping factor for smoothing the bobbing effect. The code ensures that the view bobbing effect only occurs when the player is on the ground by checking the `Player.onGround` condition. When the player is in the air, `bobTime` is not incremented.

The reviewer points out that since this section modifies variables in the `Player` struct, it should be protected by locking the `Player` mutex to ensure thread safety. The target bobbing velocity (`targetBobVel`) is calculated as `std.math.pow(f64, horizontalMovementSpeed / 4, 0.5)` when the player's horizontal movement speed exceeds 0.01 and they are on the ground. This calculation ensures that the bobbing effect scales with the player's movement speed.

The damping factor (`fac`) plays a crucial role in smoothing the transition between different bobbing velocities by gradually adjusting `bobVel` towards `targetBobVel`. The code prevents excessive bobbing motion when the player is moving quickly by capping `Player.bobMag` at 1.2 times the view bob strength setting.

## Related Questions
- What is the purpose of the `fac` variable in the view bobbing implementation?
- How does the code ensure that the view bobbing effect only occurs when the player is on the ground?
- Why is it important to lock the `Player` mutex when modifying variables in this section?
- Can you explain how the target bobbing velocity (`targetBobVel`) is calculated based on the player's movement speed?
- What role does the damping factor play in the view bobbing effect?
- How does the code prevent excessive bobbing motion when the player is moving quickly?

*Source: unknown | chunk_id: github_pr_665_comment_1755254993*
