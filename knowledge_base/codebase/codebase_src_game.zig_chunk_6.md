# [hard/codebase_src_game.zig] - Chunk 6

**Type:** gameplay
**Keywords:** bounding box, gravity, jump height, wall collision, vertical collision, damage computation, coyote timer, block placement, block breaking, world update, particle system, restart function
**Symbols:** Player, physics, main, world, particles, network, Vec3d, smoothPerc, KeyBoard
**Concepts:** player movement loop, bounding box calculation, gravity and jumping physics, wall collision detection, vertical collision with damage computation, eye position clamping, coyote timer decrement, block placing/breaking timers, world update, particle system update, restart function with error handling

## Summary
This chunk implements the player movement and interaction loop, handling bounding box calculations, gravity/jumping physics, wall collisions, vertical collision with damage computation, block placing/breaking timers, world updates, particle system updates, and a restart function that pauses the world, informs the server, and handles errors.

## Explanation
The chunk begins by setting Player.outerBoundingBox to a symmetric box derived from Player.outerBoundingBoxExtent. It then computes Player.eye.box: min is -Vec3d{extent*0.2, extent*0.2, extent-0.2} and max is Vec3d{extent*0.2, extent*0.2, extent-0.05}. Player.eye.desiredPos interpolates between standing height (1.7 minus standingBoundingBoxExtent[2]) and crouching height (1.3 minus crouchingBoundingBoxExtent[2]), scaled by smoothPerc. Gravity is chosen as 0.0 if Player.isFlying.load(.monotonic) else physics.baseGravity; jumpHeight is Player.jumpHeight when jumping, otherwise 0.0. motion is obtained via physics.calculateMotion with flags .client, deltaTime, friction, volumeProperties, density, super.pos, &super.vel, acc, gravity, and jumpHeight.

Inside a mutex-protected block (Player.mutex.lock(); defer unlock()), stepAmount starts at 0.0; if !Player.isGhost.load(.monotonic), steppingHeightLimit = Player.eye.pos[2] - Player.eye.box.min[2], and stepAmount is set by physics.calculateWallCollision with .client, &motion, &super.pos, &super.vel, &onGround, friction, outerBoundingBox, steppingHeight()[2], steppingHeightLimit, and crouching. Then physics.calculateEyeMovement updates the eye position based on client, deltaTime, super.pos/vel, stepAmount.

didCollide is false initially; wasOnGround = Player.onGround; prevPos = Player.super.pos; prevVel = Player.super.vel. If !Player.isGhost.load(.monotonic), bouncinessMultiplier is 0.0 if flying, else 0.5 if crouching, else 1.0. didCollide becomes the result of physics.calculateVerticalCollision with .client, deltaTime, &super.pos, &super.vel, &jumpCoyote, onGround, outerBoundingBox, motion, and bouncinessMultiplier. If didCollide is true, velocityChange = @abs(@abs(prevVel[2]) - @abs(super.vel[2])); damage = @floatCast(@round(@max((velocityChange*velocityChange)/(2*physics.baseGravity) - 7, 0))/2). When damage > 0.01, main.sync.addHealth(-damage, .fall, .client, Player.id) is called.

After collision handling, physics.calculateVerticalCollisionEyeMovement(deltaTime, &Player.eye, didCollide, onGround, wasOnGround, prevPos, super.pos, prevVel, super.vel, motion, steppingHeight()[2]) runs. Then physics.collision.touchBlocks(.client, &super, outerBoundingBox, deltaTime) is invoked.

If Player.isGhost.load(.monotonic) is true (else branch), Player.super.pos += motion directly.

The eye position is clamped: Player.eye.pos = @max(Player.eye.box.min, @min(Player.eye.pos, Player.eye.box.max)). Coyote timers decrement: Player.eye.coyote -= deltaTime; Player.jumpCoyote -= deltaTime.

Outside the mutex, time = main.timestamp(). If nextBlockPlaceTime exists and placeTime.durationTo(time).nanoseconds >= 0, placeTime is advanced by main.settings.updateRepeatSpeed and Player.placeBlock(main.KeyBoard.key("placeBlock").modsOnPress) runs. Similarly for nextBlockBreakTime: if breakTime.durationTo(time).nanoseconds >= 0 or !Player.isCreative(), breakTime advances and Player.breakBlock(deltaTime) runs.

Finally, world.?.update(deltaTime) is called (world may be null), particles.ParticleSystem.update(@floatCast(deltaTime)) updates the particle system.
The restart() function checks if world exists; if so, it pauses _world, calls network.protocols.reload.informServerOfRestart(_world.conn), then attempts to continue _world. If continuation fails with error err, std.log.err logs "Encountered error while opening world: {s}" using {@errorName(err)}, main.gui.windowlist.notification.raiseNotification raises the same message, world is set to null, main.gui.openWindow("main") opens the main window, and restart returns early. Otherwise main.gui.openHud() is called.

## Related Questions
- How is Player.eye.desiredPos computed and what does smoothPerc represent?
- What happens when Player.isFlying.load(.monotonic) is true versus false for gravity selection?
- Describe the sequence of operations inside the mutex-protected block for non-ghost players.
- How are stepAmount and steppingHeightLimit derived from eye position and box min?
- Explain how bouncinessMultiplier changes based on flying, crouching, or standing states.
- What is the formula used to compute damage from vertical collision velocity change?
- When does Player.eye.pos get clamped and what are its bounds?
- How do nextBlockPlaceTime and nextBlockBreakTime timers control block interactions?
- What occurs if world.?.update(deltaTime) fails or world is null?
- In the restart function, how is the server informed of a world restart?
- What error logging and UI actions are performed when continuing the world throws an error?
- How does Player.isGhost.load(.monotonic) affect collision handling versus direct position updates?

*Source: unknown | chunk_id: codebase_src_game.zig_chunk_6*
