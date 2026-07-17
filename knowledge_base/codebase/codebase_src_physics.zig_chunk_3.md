# [hard/codebase_src_physics.zig] - Chunk 3

**Type:** implementation
**Keywords:** physics engine, friction, acceleration, velocity, differential equations
**Symbols:** calculateFriction, calculateMotion, calculateEyeMovement
**Concepts:** friction calculation, motion physics, eye movement simulation

## Summary
This chunk implements the physics calculations for friction, motion, and eye movement in the game.

## Explanation
The chunk defines three functions: `calculateFriction`, `calculateMotion`, and `calculateEyeMovement`. Each function is responsible for calculating different aspects of physics related to the player's interaction with the environment. `calculateFriction` computes friction based on the player's position, velocity, and environmental properties. `calculateMotion` calculates the player's movement considering gravity, input acceleration, and friction. `calculateEyeMovement` models the eye's position and velocity changes due to springs and friction.

## Related Questions
- How does the `calculateFriction` function determine the amount of friction?
- What is the role of `deltaTime` in the `calculateMotion` function?
- Can you explain the mathematical model used in `calculateEyeMovement`?
- How does the chunk handle player movement on different axes?
- What are the key parameters that influence eye position calculations in this chunk?
- How does the chunk ensure smooth transitions between movements and states?
- What is the purpose of the `coyote` variable in the eye movement calculations?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_3*
