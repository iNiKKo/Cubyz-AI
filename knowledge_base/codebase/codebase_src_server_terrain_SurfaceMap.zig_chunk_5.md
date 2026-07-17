# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 5

**Type:** algorithm
**Keywords:** LOD, interpolation, noise, biome majority, cache findOrCreate, voxel size doubling, monotonic store
**Symbols:** getOrGenerateFragment, MapFragmentPosition
**Concepts:** LOD generation, neighbor interpolation, polynomial noise blending, majority biome selection, fragment caching, atomic flag stores

## Summary
This chunk implements the LOD generation loop for terrain maps, including neighbor interpolation logic and a multi-scale fragment caching system.

## Explanation
The code begins by checking if all three directional neighbors are present via neighborInfo flags; when true it interpolates height using polynomial noise evaluation scaled by interpolationDistance, blending between mapFragment.heightMap and generatedMap.heightMap with a factor computed as 1 - (1-factorX)*(1-factorY), truncating to i32 after adding 0.5 for rounding, and copies the biome from generatedMap when factor < 0.25. It then calls mapFragment.save(&originalHeightMap, neighborInfo) to persist the interpolated heightmap while leaving biomes unchanged (the save function is not defined here). The LOD generation loop iterates while cur.pos.voxelSizeShift < main.settings.highestSupportedLod, doubling voxel size each iteration and masking wx/wy with nextMask = ~@as(i32, nextPos.voxelSize*MapFragment.mapSize - 1) to align coordinates. It retrieves or generates the next fragment via getOrGenerateFragment(nextPos.wx, nextPos.wy, nextPos.voxelSize). Offsets offSetX and offSetY are computed by subtracting cur.pos from nextPos and shifting right by nextPos.voxelSizeShift. The nested loops over 0..MapFragment.mapSize/2 compute a 4-block neighborhood (dx in 0..2, dy in 0..2) to aggregate height sums and biome counts; biomes are stored in an array of up to four Biome pointers with null terminators, incrementing biomeCounts[i] when a matching biome is found or inserting a new entry. bestBiome is selected by iterating i from 1..4 and picking the highest count (ties keep earlier). next.heightMap[nextX][nextY] = @divFloor(height, 4) averages height over the four blocks; next.biomeMap[nextX][nextY] = bestBiome assigns the majority biome. After filling the map, next.save(null, .{}) discards previous data and writes only the newly computed values (the save function is not defined here). The fragment's wasStored flag is set to true via atomic store with .monotonic ordering. Finally std.log.info(

## Related Questions
- What does the neighborInfo check guard against and why are all three directions required?
- How is the interpolation factor computed from polynomial noise evaluations of x and y offsets?
- Why is biome copying conditional on factor < 0.25 instead of always copying from generatedMap?
- What is the purpose of masking wx/wy with nextMask in each LOD iteration?
- Describe how biomes are aggregated across a 4-block neighborhood before assigning to the next fragment.
- How does getOrGenerateFragment use MapFragmentPosition.init and cache.findOrCreate together?
- Why is wasStored set with .monotonic ordering rather than any other memory order?
- What happens to saved data when calling next.save(null, .{}) during LOD generation?
- Where is originalHeightMap used in mapFragment.save and what does it represent?
- How are offSetX and offSetY derived from cur.pos versus nextPos coordinates?
- Is there any synchronization between multiple threads accessing the same fragment cache here?
- What would happen if main.settings.highestSupportedLod were set to a negative value?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_5*
