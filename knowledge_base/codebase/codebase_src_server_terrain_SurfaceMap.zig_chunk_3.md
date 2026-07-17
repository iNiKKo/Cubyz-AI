# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 3

**Type:** implementation
**Keywords:** interpolationDistance, MapFragmentPosition, NeighborInfo, biomePalette, load, deleteTree, openIterableDir, iterate, heightmap, cubic falloff
**Symbols:** MapFragmentPosition, weirdSquareInterpolation
**Concepts:** LOD interpolation, neighbor presence tracking, heightmap blending, directory iteration, stack allocation cleanup

## Summary
Loads stored map fragments from the saves directory and updates their LODs by interpolating height data when neighbor presence changes.

## Explanation
The chunk begins by freeing a previously allocated path string, then constructs a new path under saves/worldName/maps/1. It opens that directory iterably, walks its contents, and for each subdirectory (parsed as wx) and file inside it (parsed from the filename prefix before the dot as wy), appends a MapFragmentPosition entry with voxelSize=1 and voxelSizeShift=0. After collecting all positions, it loads each stored map fragment via main.server.world.?.biomePalette.load, which returns oldNeighborInfo and populates originalHeightMap. It then compares neighborInfo (computed from the current directory layout) against oldNeighborInfo; if they differ, it performs LOD interpolation: for edge cases where a neighbor was absent before but is now present, it copies height values from the newly loaded fragment into originalHeightMap at mirrored coordinates; for corner cases, it computes blending factors using a weirdSquareInterpolation helper that maps two sides of a square to 0 and the other two to 1, applies cubic falloff based on normalized indices, and blends between the new and old heights with @trunc. The chunk uses stack allocation for mapFragment and originalHeightMap, deferring destruction after use.

## Related Questions
- How does the chunk determine which neighbor positions are present in the stored maps?
- What happens when a neighbor was absent before but is now present after loading a map fragment?
- Where is the originalHeightMap populated with data from the loaded map fragments?
- Why does the chunk use stack allocation for mapFragment and originalHeightMap instead of heap allocation?
- How are corner interpolation cases handled differently from edge cases in this chunk?
- What role does weirdSquareInterpolation play in blending height values at corners?
- Does the chunk perform any error handling when parsing directory or file names as integers?
- Is there any synchronization point used between loading multiple map fragments, and if so where?
- How is the interpolationDistance computed from MapFragment.mapSize?
- What does the defer block at the end of the chunk guarantee regarding resource cleanup?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_3*
