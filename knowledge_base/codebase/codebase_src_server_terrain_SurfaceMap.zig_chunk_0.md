# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, methods, hash code, distance calculation, priority determination
**Symbols:** MapFragmentPosition, MapFragmentPosition.wx, MapFragmentPosition.wy, MapFragmentPosition.voxelSize, MapFragmentPosition.voxelSizeShift, MapFragmentPosition.init, MapFragmentPosition.equals, MapFragmentPosition.hashCode, MapFragmentPosition.getMinDistanceSquared, MapFragmentPosition.getPriority, map_generators
**Concepts:** chunk meshing, world generation, spatial partitioning

## Summary
Defines the MapFragmentPosition struct and its methods for initialization, equality check, hash code generation, distance calculation, and priority determination.

## Explanation
Defines the `MapFragmentPosition` struct and its methods for initialization, equality check, hash code generation, distance calculation, and priority determination. The struct includes fields for world coordinates (`wx`, `wy`) and voxel size parameters (`voxelSize`, `voxelSizeShift`). The `init` method initializes a `MapFragmentPosition` instance with assertions ensuring `voxelSize` is a power of 2 and coordinates are aligned to the grid. The `equals` method checks equality based on these fields. The `hashCode` method returns a hash code calculated using bitwise operations on the position and size. The `getMinDistanceSquared` method calculates the minimum squared distance from the player's position, considering the fragment's width. The `getPriority` method determines priority based on proximity and size, with additional factors like log2 of voxel size affecting the result.

## Code Example
```zig
pub fn init(wx: i32, wy: i32, voxelSize: u31) MapFragmentPosition {
	std.debug.assert(voxelSize - 1 & voxelSize == 0); // voxelSize must be a power of 2.
	std.debug.assert(wx & voxelSize - 1 == 0 and wy & voxelSize - 1 == 0); // The coordinates are misaligned. They need to be aligned to the voxelSize grid.
	return MapFragmentPosition{
		.wx = wx,
		.wy = wy,
		.voxelSize = voxelSize,
		.voxelSizeShift = @ctz(voxelSize),
	};
}
```

## Related Questions
- What is the purpose of the `init` method in the `MapFragmentPosition` struct?
- How does the `equals` method determine if two `MapFragmentPosition` instances are equal?
- What does the `hashCode` method return and how is it calculated?
- How is the minimum squared distance to a player's position calculated in the `getMinDistanceSquared` method?
- What factors influence the priority calculation in the `getPriority` method?
- What assertion checks are performed during the initialization of a `MapFragmentPosition` instance?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_0*
