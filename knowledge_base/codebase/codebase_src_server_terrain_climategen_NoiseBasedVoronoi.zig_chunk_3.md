# [hard/codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig] - Chunk 3

**Type:** implementation
**Keywords:** BiomePoint, ClimateMapFragment, GenerationProperties, stack allocator, influence radius, neighbor mask, transition chance, random seed, lerp, margin padding
**Symbols:** addSubBiomesOf, addTransitionBiomes, fillRecursively, toMap
**Concepts:** recursive subdivision, biome candidate filtering, neighbor mask propagation, transition biome placement, sub-biome generation, random seeded offsetting, map copy with margin padding

## Summary
This chunk implements the core biome generation pipeline for a climate map, including recursive subdivision of candidate biomes, sub-biome placement with random offsets, transition logic between adjacent biomes using neighbor masks, and final copying into the target ClimateMapFragment.

## Explanation
The chunk defines several public functions that orchestrate terrain generation. fillRecursively is a divide-and-conquer routine: it checks if the requested width/height are <=1; if so it fills each cell by calling findClosestBiomeTo (not defined here) with the worldSeed and relative coordinates, then returns. Otherwise it halves both dimensions, creates a new List of BiomePoint candidates for each quadrant, filters them by influence radius (3*ceil(candidate.radius)) against the quadrant bounds, appends qualifying candidates to newCandidates, and recursively calls itself on each quadrant. The recursion builds up a full preMap sized [preMapSize][preMapSize] where preMapSize = ClimateMapFragment.mapEntrysSize + 2*margin; margin is derived from chunkSize shifted by terrain.SurfaceMap.MapFragment.biomeShift. After fillRecursively returns, addTransitionBiomes(&preMap) runs: it allocates a neighborData buffer of shape [16][preMapSize][preMapSize]u15 on the stack allocator, copies each map[x][y].biome.properties into neighborData[0][x][y], then iterates i from 1 to len-1 and x,y from 1 to preMapSize-2. For each (i,x,y) it computes y1=y and y2 based on parity of x, forms xNeighbors as the bitwise OR of four neighbor entries at offset i-1, and sets neighborData[i][x][y] = neighborData[i-1][x][y] | neighborData[i-1][x][y-1] | neighborData[i-1][x][y+1] | xNeighbors. This propagates property bits outward from the border into interior cells. Then it iterates over the inner region (margin..preMapSize-margin) and for each point checks if transitionBiomes.len == 0; if so it asserts the biome is not ocean and continues. Otherwise it seeds a random with point.seed, then loops over point.biome.transitionBiomes. For each transitionBiome it casts its propertyMask to u15 as biomeMask, reads neighborMask from neighborData at index min(len-1, transitionBiome.width) for (x,y), computes result = biomeMask & neighborMask, applies three right shifts and ORs them together, then tests if (result & Biome.GenerationProperties.mask) == Biome.GenerationProperties.mask. If true and random.nextFloat(&seed) < transitionBiome.chance, it generates newHeight by linearly interpolating between minHeight and maxHeight using another random float, then overwrites map[x][y] with a struct containing the transitionBiome.biome, roughness/hills/mountains/height lerped toward original values if keepOriginalTerrain is set, and preserves the seed. The chunk also defines addSubBiomesOf (not shown fully) which appends BiomePoint entries to extraBiomes; it is called for each biome in self.chunks.mem with a random offset determined by radius==.unknown vs .known. After that, while extraBiomes.popOrNull() yields a biomePoint, addSubBiomesOf is invoked again with the same bounds but now using .known as the radius flag. Finally, @memcpy copies preMap entries into map.map[_x] for _x in 0..ClimateMapFragment.mapEntrysSize, offsetting by margin on both axes and truncating to ClimateMapFragment.mapEntrysSize columns.

## Related Questions
- What is the purpose of the margin variable and how is it computed from chunkSize?
- How does fillRecursively decide when to stop subdividing a region?
- In addTransitionBiomes, what condition causes a biome transition to be applied at (x,y)?
- Why are y1 and y2 chosen based on x%2 in the neighborData computation?
- What happens if point.biome.transitionBiomes.len is zero when processing an inner cell?
- How does addSubBiomesOf handle the difference between radius == .unknown and radius == .known?
- Where are BiomePoint candidates collected before being passed to fillRecursively?
- What role does @memcpy play in the final step of toMap?
- Is neighborData allocated on the heap or stack, and how is it cleaned up?
- How is newHeight generated for a transition biome that passes its mask check?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_3*
