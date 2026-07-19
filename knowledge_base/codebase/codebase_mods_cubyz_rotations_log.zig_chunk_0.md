# [medium/codebase_mods_cubyz_rotations_log.zig] - Chunk 0

**Type:** implementation
**Keywords:** rotation, texture mapping, enum handling, union types, vector operations
**Symbols:** rotateZ, dependsOnNeighbors, modelIndex, LogData, init, deinit, reset, DirectionWithoutSign, fromBranchDirection, Pattern, dot, line, bend, intersection, cross, cut, rotateQuad, originalCorners, corners, angle, offX, offY, corners3d, offset, res
**Concepts:** block texture rotation, pattern-based texturing, neighbor dependency

## Summary
Handles rotation and pattern-based texture mapping for block sides.

## Explanation
This chunk defines logic for rotating block textures based on their orientation and neighboring blocks. It includes functions to initialize (`init`), deinitialize (`deinit`), and reset (`reset`) the module's state, setting `modelIndex` to `null`. The `rotateQuad` function calculates the rotated corners of a quad based on its pattern and relative position using specific angles and offsets. For example, when handling the `.line` pattern, it rotates each corner by an angle calculated as `@as(f32, @floatFromInt(@intFromEnum(dir)))*std.math.pi/2.0`, adjusting for positive or negative sides based on the neighbor's relative position (`side.relZ()`, `side.isPositive()`, and `side.relY()`). For the `.bend` and `.intersection` patterns, it applies a fixed rotation angle of `-@as(f32, @floatFromInt(@intFromEnum(dir)))*std.math.pi/2.0`. The `DirectionWithoutSign` enum simplifies direction handling by removing sign information, mapping directions like `.negYDir`, `.posXDir`, etc., to either `.y` or `.x`. The `Pattern` union defines different texture patterns such as `dot`, `line`, `bend`, `intersection`, `cross`, and `cut`. Each pattern has specific handling in the `rotateQuad` function, including detailed vector operations for calculating rotated corners and offsets. Specifically, the original corners are rotated using `vec.rotate2d(originalCorners[i], angle, @splat(0.5))` to adjust their positions based on the specified angles. The `offX` and `offY` variables are used to calculate the texture offset based on the side's relative position. The `reset` function sets `modelIndex` to `null`, effectively resetting the module's state.

## Code Example
```zig
pub fn reset() void {
	modelIndex = null;
}
```

## Related Questions
- What is the purpose of the `rotateZ` function?
- How does the `rotateQuad` function handle different patterns?
- What does the `DirectionWithoutSign` enum represent?
- How is the `modelIndex` variable used in this module?
- What are the possible values for the `Pattern` union?
- How does the `reset` function affect the module's state?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_log.zig_chunk_0*
