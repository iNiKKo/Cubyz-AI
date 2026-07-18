# [hard/codebase_src_physics.zig] - Chunk 0

**Type:** configuration
**Keywords:** constants, imports, gravity, terminal velocity, density
**Symbols:** baseGravity, playerAirTerminalVelocity, airDensity, playerDensity, epsilon
**Concepts:** physics simulation, physical constants

## Summary
Defines constants and imports for physics calculations in the Cubyz engine.

## Explanation
This chunk primarily defines physical constants such as gravity, terminal velocity, air density, and player density. It also imports various modules necessary for handling vectors, items, settings, players, and camera functionalities. The constants are used to simulate realistic physics behavior within the game environment.

Specifically:
- `baseGravity` is set to 30.0.
- `playerAirTerminalVelocity` is set to 90.0.
- `airDensity` is set to 0.001.
- `playerDensity` is set to 1.2.
- `epsilon` is calculated as the last bit when at the integer limit, specifically: `1.0 / (@as(comptime_float, 1 << (std.math.floatMantissaBits(f64) - 31)))`. This value ensures precision in floating-point calculations.

## Related Questions
-  What is the value of baseGravity?
-  Which modules are imported in this chunk?
-  What does playerAirTerminalVelocity represent?
-  How is epsilon calculated?
-  What physical constants are defined in this chunk?
-  Which vector types are imported from vec.zig?

*Source: unknown | chunk_id: codebase_src_physics.zig_chunk_0*
