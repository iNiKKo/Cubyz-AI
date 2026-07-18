# [medium/codebase_mods_cubyz_rotations_stairs.zig] - Chunk 0

**Type:** implementation
**Keywords:** rotation table, greedy meshing, stair block, visible faces, resource management
**Symbols:** modelIndex, subBlockMask, hasSubBlock, rotateZ, init, deinit, reset, GreedyFaceInfo, mergeFaces
**Concepts:** block rotation, face merging, render optimization

## Summary
Handles stair block rotations and face merging logic.

## Explanation
This chunk defines functions for rotating stair blocks by a given angle and merging their visible faces. The `rotateZ` function uses a precomputed rotation table to efficiently rotate the stair data based on the specified angle. The `mergeFaces` function combines adjacent visible faces into larger, contiguous areas to optimize rendering. The chunk also includes initialization, deinitialization, and reset functions for managing resources.

## Code Example
```zig
fn subBlockMask(x: u1, y: u1, z: u1) u8 {
	return @as(u8, 1) << ((@as(u3, x)*2 + @as(u3, y))*2 + z);
}
```

## Related Questions
- How is the subBlockMask function used?
- What does the rotateZ function compute?
- How are visible faces merged in this chunk?
- What is the purpose of the GreedyFaceInfo struct?
- How is resource management handled in this module?
- What is the role of the rotation table in the rotateZ function?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_stairs.zig_chunk_0*
