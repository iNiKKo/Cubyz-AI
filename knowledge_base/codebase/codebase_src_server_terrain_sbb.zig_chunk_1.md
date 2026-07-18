# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 1

**Type:** implementation
**Keywords:** enum, union, switch, rotation logic, fixed rotation, random rotation, inherit rotation
**Symbols:** isChildBlock, isOriginBlock, RotationMode, Rotation, Rotation.FixedRotation, Rotation.apply, Rotation.getInitialRotation, Rotation.sampleRandom, Rotation.getChildRotation, Rotation.fromZon
**Concepts:** block rotation, child block check, origin block check

## Summary
Defines block rotation logic and checks for child and origin blocks.

## Explanation
This chunk defines functions to check if a block is a child or origin block. It also defines an enum `RotationMode` with three modes: fixed, random, and inherit. A union `Rotation` includes these modes along with methods for applying, getting initial, sampling random, and getting child rotations. The `FixedRotation` nested enum represents four fixed rotation angles: 0 ("@0"), 90 ("@90"), 180 ("@180"), and 270 ("@270") degrees. Methods like `apply`, `getInitialRotation`, `getChildRotation`, and `fromZon` handle different aspects of block rotation logic based on the mode (fixed, random, inherit). The `isChildBlock` function checks if a block is a child by looking up its numeric ID in `childBlockNumericIdMap`. The `isOriginBlock` function checks if a block's type matches the origin block's numeric ID (`originBlockNumericId`). The `fromZon` method parses rotations from Zon elements, supporting string and integer representations of rotation modes. For example, it converts strings like "fixed", "random", or "inherit" to their corresponding enum values.

## Code Example
```zig
pub fn isChildBlock(block: Block) bool {
	return childBlockNumericIdMap.contains(block.typ);
}
```

## Related Questions
- How do you check if a block is a child block?
- What are the different rotation modes defined in this chunk?
- How does the `apply` method work for rotations?
- What is the purpose of the `sampleRandom` function?
- How is a rotation parsed from a Zon element?
- What fixed rotation angles are supported?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_1*
