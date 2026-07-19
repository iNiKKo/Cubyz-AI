# [hard/codebase_src_physics.zig] - Chunk 4

**Type:** implementation
**Keywords:** volume properties, friction coefficient, motion integration, gravity effects, input acceleration
**Symbols:** FrictionState, FrictionState.current, FrictionState.mobile, calculateVolumeProperties, calculateFriction, calculateMotion
**Concepts:** physics, friction calculation, motion modeling

## Summary
This chunk defines structures and functions for calculating physical properties, friction, and motion in a voxel engine.

## Explanation
This chunk defines structures and functions for calculating physical properties, friction, and motion in a voxel engine. The `FrictionState` struct contains fields `current: f32` and `mobile: f32`. It includes three main functions: `calculateVolumeProperties`, `calculateFriction`, and `calculateMotion`. 

The `calculateVolumeProperties` function computes volume properties based on block presence, setting density to `airDensity`, terminal velocity to `airTerminalVelocity`, max density to `airDensity`, and mobile friction to `1.0/airTerminalVelocity`. The `calculateFriction` function calculates friction coefficients considering ground contact, where the current friction is calculated as `groundFriction + volumeFrictionCoeffecient` and mobile friction as `groundFriction + mobileFriction`. This function also considers whether the entity is on the ground (`onGround`) to adjust the ground friction accordingly. The `calculateMotion` function models motion over a single frame, applying gravity, input acceleration, and friction effects. It uses effective gravity `(gravity*(density - volumeProperties.density)/density)`, calculates the base friction coefficient (`baseGravity/volumeProperties.terminalVelocity`), and updates velocity based on these parameters.

During jumping, no friction is applied if `jumpHeight > 0.0`. The jump velocity is calculated as `@sqrt(jumpHeight*baseGravity*2)`. The motion model implemented in `calculateMotion` uses the differential equation `dv/dt = a - λ·v` and `dx/dt = v`, where `a` is the acceleration, `λ` is the friction coefficient, `v_0` is the initial velocity, and `c_1` is calculated as `v_0 - a/λ`. The solution to these equations provides the updated velocity and position over time.

## Code Example
```zig
pub const FrictionState = struct {
	current: f32,
	mobile: f32,
};

```

## Related Questions
- What is the purpose of the `FrictionState` struct?
- How does the `calculateVolumeProperties` function determine volume properties?
- What factors influence the calculation in `calculateFriction`?
- Describe the motion model implemented in `calculateMotion`.
- How is friction handled during jumping in the engine?
- What are the key components of the velocity update equation in `calculateMotion`?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_4*
