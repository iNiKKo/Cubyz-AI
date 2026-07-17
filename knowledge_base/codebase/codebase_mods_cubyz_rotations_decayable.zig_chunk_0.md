# [easy/codebase_mods_cubyz_rotations_decayable.zig] - Chunk 0

**Type:** api
**Keywords:** World, Neighbor, RotationMode, RayIntersectionResult, Mat4f, Vec3f, Vec3i, blockPlacing, data field
**Symbols:** init, deinit, reset, generateData
**Concepts:** decayable blocks, rotation support, block state management, placement flag handling

## Summary
This chunk defines a public API for handling decayable blocks with rotation support, providing initialization, reset, and data generation functions that set internal block state based on placement flags.

## Explanation
The chunk declares several imported types from the main module: World, Neighbor, ModelIndex, RotationMode, Degrees, RayIntersectionResult, Mat4f, Vec3f, Vec3i, ZonElement. It defines three public functions init(), deinit(), and reset() with empty bodies (void return). The generateData function takes a world pointer, several coordinate/value parameters, an optional Neighbor, two Block pointers, and a blockPlacing bool; if blockPlacing is true it sets the first block's data field to 1 and returns that boolean. No struct or enum definitions are present in this chunk.

## Related Questions
- What does the generateData function return when blockPlacing is false?
- Which imported types are used as parameters in generateData?
- Does this chunk define any struct or enum types?
- How many public functions are declared at top level?
- What value is assigned to block.data inside generateData?
- Are init, deinit, and reset implemented with bodies?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_decayable.zig_chunk_0*
