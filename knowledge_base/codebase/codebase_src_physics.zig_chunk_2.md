# [hard/codebase_src_physics.zig] - Chunk 2

**Type:** implementation
**Keywords:** collision detection, volume properties, friction, motion computation, entity interaction, block collision
**Symbols:** collideOrStep, isBlockIntersecting, touchBlocks, FrictionState, calculateVolumeProperties, calculateFriction, calculateMotion
**Concepts:** collision detection, volume properties calculation, friction management, motion computation

## Summary
This chunk implements physics calculations, including collision detection, volume property calculation, friction state management, and motion computation.

## Explanation
The chunk contains functions for calculating various physical properties such as terminal velocity, density, and mobile friction. It includes methods for detecting collisions and determining whether an entity can step up when colliding with a block. The `touchBlocks` function checks for interactions between blocks and entities within a given bounding box. Additionally, it provides functions to calculate volume properties and friction based on the environment and entity's state.

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
- How does the `isBlockIntersecting` function determine if a block intersects with an entity's bounding box?
- What does the `touchBlocks` function do and how does it interact with blocks?
- How are volume properties calculated in this chunk?
- What is the role of friction state management in the physics calculations?
- How is motion computed for an entity based on its environment and input acceleration?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_2*
