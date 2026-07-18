# [hard/codebase_mods_cubyz_rotations_branch.zig] - Chunk 2

**Type:** implementation
**Keywords:** model creation, rotation logic, collision detection, data manipulation, voxel block
**Symbols:** createBlockModel, model, rotateZ, generateData
**Concepts:** block meshing, branch model generation, neighbor connections

## Summary
This chunk handles the creation and manipulation of block models, including rotation and data generation for branch-like structures.

## Explanation
This chunk handles the creation and manipulation of block models, including rotation and data generation for branch-like structures. The `createBlockModel` function initializes a model based on configuration data from a ZonElement, handling shell models and collision boxes. It sets the radius to 4 if not specified in the ZonElement, calculates `radiusForComparisons`, and uses this value to determine the model index. If a shell model ID is provided, it retrieves the corresponding model and its raw faces for quads and collisions. The function also generates innerBox based on the calculated radius and iterates through 64 possible branch data configurations to create quads and collision boxes accordingly. `model` retrieves the model index for a given block by adding the block's data (masked with 0x3F) to the base model index of the block type. The `rotateZ` function computes a rotated version of branch data based on an angle using precomputed rotation tables. It handles up-down flags and returns the appropriate rotated data value. Finally, `generateData` determines how to connect branches based on neighboring blocks and placement conditions, ensuring proper neighbor connections if applicable.

## Code Example
```zig
pub fn rotateZ(data: u16, angle: Degrees) u16 {
	@setEvalBranchQuota(65_536);

	comptime var rotationTable: [4][16]u8 = undefined;
	comptime for (0..16) |i| {
		rotationTable[0][i] = @intCast(i << 2);
	};
	comptime for (1..4) |a| {
		for (0..16) |i| {
			const old: BranchData = .init(rotationTable[a - 1][i]);
			var new: BranchData = .init(0);

			new.setConnection(Neighbor.dirPosX.rotateZ(), old.isConnected(Neighbor.dirPosX));
			new.setConnection(Neighbor.dirNegX.rotateZ(), old.isConnected(Neighbor.dirNegX));
			new.setConnection(Neighbor.dirPosY.rotateZ(), old.isConnected(Neighbor.dirPosY));
			new.setConnection(Neighbor.dirNegY.rotateZ(), old.isConnected(Neighbor.dirNegY));

			rotationTable[a][i] = new.enabledConnections;
		}
	};
	if (data > 0b111111) return 0;
	const rotationIndex = (data & 0b111100) >> 2;
	const upDownFlags = data & 0b000011;
	const runtimeTable = rotationTable;
	return runtimeTable[@intFromEnum(angle)][rotationIndex] | upDownFlags;
}
```

## Related Questions
- How does the `createBlockModel` function initialize a block model with specific radius and shell model configurations?
- What is the purpose of the `rotateZ` function in this chunk, including how it uses precomputed rotation tables?
- How does the `generateData` function determine neighbor connections based on placement conditions and neighboring blocks?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_branch.zig_chunk_2*
