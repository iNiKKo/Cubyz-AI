# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 4

**Type:** algorithm
**Keywords:** interpolation distance, neighbor flags, weird square interpolation, biome map copy, level of detail, voxel size shift, noise polynomial evaluation, heightmap truncation
**Symbols:** weirdSquareInterpolation, noise
**Concepts:** terrain interpolation, biome blending, LOD generation, edge handling, corner handling, heightmap merging

## Summary
Interpolates terrain heightmaps between generated fragments and existing maps, applies biome blending based on interpolation distance, and generates Level-of-Detail (LOD) pyramid entries by computing offsets and fetching or generating next-level fragments.

## Explanation
The chunk performs edge interpolation first: for each neighbor direction (+o, -o, o+, o-), it checks old vs new neighborInfo flags to decide whether to use weirdSquareInterpolation (when only one side changed) or linear blending (factor = 0 or 1). It then interpolates heightMap values using @trunc(0.5 + floatFromInt(mapFragment.heightMap[x][y])*factor + floatFromInt(originalHeightMap[x][y])*(1-factor)). If the resulting factor is < 0.25, it copies biomeMap from generatedMap to mapFragment. After edges, it handles corners: for each corner combination (e.g., ++ with +o and o+), it computes two factors along X and Y using noise.get evaluated at normalized distance a/interpolationDistance and b/interpolationDistance, then combines them as factor = 1 - (1-factorX)*(1-factorY) before applying the same height/biome blending logic. Finally, it calls mapFragment.save(&originalHeightMap, neighborInfo) to persist the interpolated result.

## Related Questions
- How does the chunk decide when to use weirdSquareInterpolation versus linear blending for edge neighbors?
- What condition triggers copying biomeMap from generatedMap to mapFragment during interpolation?
- How are corner interpolations computed using two separate factors along X and Y axes?
- Why is noise.get evaluated at a normalized distance (a/interpolationDistance) rather than raw coordinates?
- What does the chunk do after finishing edge and corner interpolation before saving the result?
- How does the chunk compute offsets for LOD generation using cur.pos and nextPos.voxelSizeShift?
- What is the purpose of applying ~@as(i32, nextPos.voxelSize*MapFragment.mapSize - 1) to nextPos.wx/wy?
- Does the chunk modify originalHeightMap directly or only mapFragment.heightMap during interpolation?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_4*
