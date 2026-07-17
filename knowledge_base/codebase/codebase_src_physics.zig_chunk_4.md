# [hard/codebase_src_physics.zig] - Chunk 4

**Type:** implementation
**Keywords:** collision detection, velocity calculation, position update, friction coefficient, gravity, bounciness factor, crouching state, jumping mechanics
**Symbols:** calculateWallCollision, calculateVerticalCollision, calculateVerticalCollisionEyeMovement
**Concepts:** collision detection, player movement, friction, gravity, bounciness, crouching, jumping coyote time

## Summary
This chunk implements physics calculations for player movement, including collision detection and response.

## Explanation
The chunk contains functions for calculating wall collisions, vertical collisions, and eye movement based on collision events. It uses complex mathematical formulas to determine velocities and positions after collisions, taking into account factors like friction, gravity, and bounciness. The code also handles special cases such as crouching and jumping coyote time.

## Code Example
```zig
pub fn calculateWallCollision(comptime side: main.sync.Side, motion: *Vec3d, pos: *Vec3d, vel: *Vec3d, onGround: *bool, frictionState: FrictionState, hitBox: collision.Box, steppingHeight: f64, steppingHeightLimit: ?f64, crouching: bool) f64 {
    var adjustedSteppingHeight = steppingHeight;
    if (vel[2] > 0) {
        adjustedSteppingHeight = vel[2]*vel[2]/baseGravity/2;
    }
    if (steppingHeightLimit) |limit| {
        adjustedSteppingHeight = @min(adjustedSteppingHeight, limit);
    }
    const slipLimit = 0.25*frictionState.current;

    const xMovement = collision.collideOrStep(side, .x, motion[0], pos.*, hitBox, adjustedSteppingHeight);
    pos.* += xMovement;
    if (crouching and onGround.* and @abs(vel[0]) < slipLimit) {
        if (collision.collides(side, .x, 0, pos.* - Vec3d{0, 0, 1}, hitBox) == null) {
            pos.* -= xMovement;
            vel[0] = 0;
        }
    }

    const yMovement = collision.collideOrStep(side, .y, motion[1], pos.*, hitBox, adjustedSteppingHeight);
    pos.* += yMovement;
    if (crouching and onGround.* and @abs(vel[1]) < slipLimit) {
        if (collision.collides(side, .y, 0, pos.* - Vec3d{0, 0, 1}, hitBox) == null) {
            pos.* -= yMovement;
            vel[1] = 0;
        }
    }

    if (xMovement[0] != motion[0]) {
        vel[0] = 0;
    }
    if (yMovement[1] != motion[1]) {
        vel[1] = 0;
    }

    const stepAmount = xMovement[2] + yMovement[2];
    if (stepAmount > 0) {
        motion[2] = -0.01;
        onGround.* = true;
    }
    return stepAmount;
}
```

## Related Questions
- How does the `calculateWallCollision` function adjust the stepping height based on velocity?
- What is the purpose of the `slipLimit` variable in the `calculateWallCollision` function?
- How does the `calculateVerticalCollision` function handle bounciness when a collision occurs?
- What conditions trigger the eye movement adjustments in the `calculateVerticalCollisionEyeMovement` function?
- How is the player's vertical velocity adjusted after a collision in the `calculateVerticalCollision` function?
- What role does the `jumpCoyoteTimeConstant` play in the jumping mechanics of the player?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_4*
