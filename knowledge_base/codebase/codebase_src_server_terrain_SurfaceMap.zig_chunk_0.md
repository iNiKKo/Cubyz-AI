# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 0

**Type:** implementation
**Keywords:** struct, methods, hash code, distance calculation, priority determination
**Symbols:** MapFragmentPosition, MapFragmentPosition.wx, MapFragmentPosition.wy, MapFragmentPosition.voxelSize, MapFragmentPosition.voxelSizeShift, MapFragmentPosition.init, MapFragmentPosition.equals, MapFragmentPosition.hashCode, MapFragmentPosition.getMinDistanceSquared, MapFragmentPosition.getPriority, map_generators
**Concepts:** chunk meshing, world generation, spatial partitioning

## Summary
Defines the MapFragmentPosition struct and its methods for initialization, equality check, hash code generation, distance calculation, and priority determination.

## Explanation
The chunk defines a `MapFragmentPosition` struct that represents a position in a map fragment. It includes fields for world coordinates (`wx`, `wy`) and voxel size parameters (`voxelSize`, `voxelSizeShift`). The struct provides methods for initialization, equality check, hash code generation, calculation of the minimum squared distance to a player's position, and determination of priority based on proximity and size.

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
