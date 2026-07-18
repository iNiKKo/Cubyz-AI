# [hard/codebase_src_physics.zig] - Chunk 6

**Type:** implementation
**Keywords:** collision response, velocity adjustment, ground detection, eye position, bouncing effect
**Symbols:** calculateVerticalCollision, calculateVerticalCollisionEyeMovement
**Concepts:** player physics, collision detection, vertical movement, camera synchronization

## Summary
Handles vertical collision detection and response for player movement, including eye position adjustments.

## Explanation
The chunk contains two functions: `calculateVerticalCollision` and `calculateVerticalCollisionEyeMovement`. The first function determines if the player collides with the ground or other objects vertically, adjusts their position and velocity accordingly, and updates whether they are on the ground. It also handles bouncing effects based on surface properties. The second function adjusts the eye's position based on collision events, ensuring smooth camera movement during vertical collisions.

## Code Example
```zig
pub fn calculateVerticalCollision(comptime side: main.sync.Side, deltaTime: f64, pos: *Vec3d, vel: *Vec3d, jumpCoyote: ?*f64, onGround: *bool, hitBox: collision.Box, motion: Vec3d, bouncinessMultiplier: f64) bool {
	const wasOnGround = onGround.*;
	onGround.* = false;
	pos[2] += motion[2];

	if (collision.collides(side, .z, -motion[2], pos.*, hitBox)) |box| {
		if (motion[2] < 0) {
			onGround.* = true;
			pos[2] = box.max[2] - hitBox.min[2] + epsilon;
		} else {
			pos[2] = box.min[2] - hitBox.max[2] - epsilon;
		}
		const bounciness = if (bouncinessMultiplier == 0) 0 else collision.calculateSurfaceProperties(side, pos.*, hitBox, 0.0).bounciness*bouncinessMultiplier;

		if (bounciness != 0.0 and vel[2] < -3.0) {
			vel[2] = -vel[2]*bounciness;
			if (jumpCoyote) |coyote| {
				coyote.* = Player.jumpCoyoteTimeConstant + deltaTime;
			}
		} else {
			vel[2] = 0;
		}

		// Always unstuck upwards for now
		while (collision.collides(side, .z, 0, pos.*, hitBox)) |_| {
			pos[2] += 1;
		}
		return true;
	} else {
		if (wasOnGround and motion[2] < 0 and jumpCoyote != null) {
			jumpCoyote.?.* = Player.jumpCoyoteTimeConstant + deltaTime;
		}
		return false;
	}
}
```

## Related Questions
- How does the function `calculateVerticalCollision` determine if a collision occurred?
- What happens to the player's velocity when they collide with a surface in `calculateVerticalCollision`?
- How does `calculateVerticalCollisionEyeMovement` adjust the eye position based on collisions?
- What is the purpose of the `jumpCoyote` parameter in `calculateVerticalCollision`?
- How does the code handle bouncing effects after a collision?
- What conditions trigger the adjustment of the eye's position in `calculateVerticalCollisionEyeMovement`?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_6*
