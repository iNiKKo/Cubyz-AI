# [medium/codebase_mods_cubyz_rotations_stairs.zig] - Chunk 0

**Type:** implementation
**Keywords:** sub-block masks, texture components, normal vectors, visibility arrays, face merging, rotation tables, neighbor iteration, stair data bits, model index caching
**Symbols:** subBlockMask, hasSubBlock, rotateZ, init, deinit, reset, GreedyFaceInfo, mergeFaces, createBlockModel
**Concepts:** rotation logic, face merging, neighbor visibility checks, stair block encoding, compile-time table generation, model index caching

## Summary
This chunk implements rotation logic for stair blocks, face merging utilities, and block model creation with neighbor visibility checks.

## Explanation
The chunk defines helper functions subBlockMask and hasSubBlock to encode/decode stair data bits. It provides pub fn rotateZ which computes a runtime lookup table via compile-time precomputed rotation tables for four angles (0°, 90°, 180°, 270°) around the Z axis, using trigonometric transforms on sub-block masks; it returns the rotated block index or 0 if out of range. It exposes pub fn init and pub fn deinit as no-op stubs, and pub fn reset which clears modelIndex to null. The mergeFaces function takes a [2][2]bool faceVisible array and an output slice mem of GreedyFaceInfo structs; it conditionally writes merged face bounding boxes into mem based on which of the four sub-faces are visible, returning a slice up to faces count. createBlockModel is a pub fn that accepts a Block, a *u16 model index pointer (ignored), and a ZonElement; if modelIndex already exists it returns it, otherwise it iterates over Neighbor.iterable to compute texture components xComponent/yComponent from neighbor.textureX()/textureY(), builds a normal Vec3i from neighbor.relX/relY/relZ, derives zComponent as the max absolute component of that normal, and constructs a zMap array selecting which side faces are front/back based on whether the sum of normal components is positive. It then initializes visibleFront and visibleMiddle [2][2]bool arrays by looping x in 0..2 and y in 0..2, computing posFront and posBack positions using splatted texture components and zMap, calling hasSubBlock for each position to mark which sub-blocks are present on the front face (visibleFront) and marking middle faces as visible only if not already front-visible and a sub-block exists at that back position (visibleMiddle).

## Related Questions
- How does rotateZ compute the rotated block index for a given angle?
- What is the purpose of subBlockMask and how are its results used in hasSubBlock?
- Describe the compile-time precomputation performed inside rotateZ.
- Under what condition does createBlockModel return an existing modelIndex instead of creating a new one?
- How are texture components xComponent and yComponent derived from neighbor.textureX() and neighbor.textureY()?
- What is the role of zMap in determining front versus back face positions inside createBlockModel?
- Explain how visibleMiddle[x][y] is set based on visibleFront and hasSubBlock.
- What does mergeFaces return when all four sub-faces are visible versus when only some are visible?
- How does the chunk handle the case where modelIndex is null at creation time?
- Are init and deinit implemented with any side effects or just as stubs?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_stairs.zig_chunk_0*
