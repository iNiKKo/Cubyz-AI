# [hard/codebase_src_physics.zig] - Chunk 3

**Type:** implementation
**Keywords:** collision response, terminal velocity calculation, hitbox intersection, stepping mechanics, block touch events
**Symbols:** terminalVelocity, density, maxDensity, mobileFriction, collideOrStep, side, dir, amount, pos, hitBox, steppingHeight, resultingMovement, checkPos, box, newFloor, heightDifference, isBlockIntersecting, block, posX, posY, posZ, center, extent, model, position, entityBox, relativeBlockCollision, blockBox, touchBlocks, boundingBox, minX, maxX, minY, maxY, minZ, maxZ, extentX, extentY, extentZ, touchX, touchY, touchZ
**Concepts:** collision detection, entity movement, block interaction

## Summary
This chunk implements collision detection and response for entities in the game world.

## Explanation
The chunk contains functions for calculating terminal velocity, handling collisions with blocks, checking if a block intersects with an entity's hitbox, and touching blocks. The `collideOrStep` function determines if an entity can move or step up based on collision checks. The `touchBlocks` function iterates over nearby blocks to detect intersections and trigger touch events.

## Code Example
```zig
pub fn collideOrStep(comptime side: main.sync.Side, comptime dir: Direction, amount: f64, pos: Vec3d, hitBox: Box, steppingHeight: f64) Vec3d {
	const index = @intFromEnum(dir);

	// First argument is amount we end up moving in dir, second argument is how far up we step
	var resultingMovement: Vec3d = .{0, 0, 0};
	resultingMovement[index] = amount;
	var checkPos = pos;
	checkPos[index] += amount;

	if (collision.collides(side, dir, -amount, checkPos, hitBox)) |box| {
		const newFloor = box.max[2] + hitBox.max[2] + epsilon;
		const heightDifference = newFloor - checkPos[2];
		if (heightDifference <= steppingHeight) {
			// If we collide but might be able to step up
			checkPos[2] = newFloor;
			if (collision.collides(side, dir, -amount, checkPos, hitBox) == null) {
				// If there's no new collision then we can execute the step-up
				resultingMovement[2] = heightDifference;
				return resultingMovement;
			}
		}

		// Otherwise move as close to the container as possible
		if (amount < 0) {
			resultingMovement[index] = box.max[index] - hitBox.min[index] - pos[index] + epsilon;
		} else {
			resultingMovement[index] = box.min[index] - hitBox.max[index] - pos[index] - epsilon;
		}
	}

	return resultingMovement;
}
```

## Related Questions
- What is the purpose of the `collideOrStep` function?
- How does the `isBlockIntersecting` function determine if a block intersects with an entity's hitbox?
- What does the `touchBlocks` function do and how does it interact with blocks?
- How is terminal velocity calculated in this chunk?
- What are the parameters of the `collideOrStep` function?
- How does the chunk handle stepping mechanics when colliding with a block?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_3*
