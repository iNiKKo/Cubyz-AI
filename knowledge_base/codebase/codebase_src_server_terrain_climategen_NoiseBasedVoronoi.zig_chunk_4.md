# [hard/codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig] - Chunk 4

**Type:** world_generation
**Keywords:** recursive filling, biome transitions, sub-biomes, map generation, neighbor data
**Symbols:** margin, preMapSize, fillRecursively, toMap
**Concepts:** world generation, biome generation, recursive subdivision

## Summary
This chunk implements the recursive filling of a climate map with biomes, considering transition and sub-biome generation.

## Explanation
This chunk implements the recursive filling of a climate map with biomes, considering transition and sub-biome generation. The code defines methods for recursively filling a climate map with biomes, handling biome transitions, and adding sub-biomes. The `fillRecursively` function subdivides the map until it reaches a minimum size, then fills each segment with the closest biome candidate based on neighbor data. The `addTransitionBiomes` function applies transition rules based on neighbor data to adjust biome properties such as height, roughness, hills, mountains, and seed. The `toMap` method orchestrates the entire process, initializing data structures, calling recursive filling, and copying results into the final map. The `margin` constant defines a border around the map for handling edge cases, while `preMapSize` is the size of the pre-map used in the generation process.

## Code Example
```zig
pub fn toMap(self: GenerationStructure, map: *ClimateMapFragment, worldSeed: u64) void {
		var preMap: [preMapSize][preMapSize]BiomeSample = undefined;
		var allCandidates: main.List(*BiomePoint) = .initCapacity(main.stackAllocator, 1024);
		defer allCandidates.deinit(main.stackAllocator);
		for (self.chunks.mem) |chunk| {
			for (chunk.biomesSortedByX) |*candidate| {
				allCandidates.append(main.stackAllocator, candidate);
			}
		}
		fillRecursively(map.pos.wx, map.pos.wy, &preMap, allCandidates.items, worldSeed, -margin, -margin, preMapSize, preMapSize);
		addTransitionBiomes(&preMap);

		// Add some sub-biomes:
		var extraBiomes: main.ListManaged(BiomePoint) = .init(main.stackAllocator);
		defer extraBiomes.deinit();
		for (self.chunks.mem) |chunk| {
			for (chunk.biomesSortedByX) |biome| {
				addSubBiomesOf(biome, &preMap, &extraBiomes, map.pos.wx -% margin*terrain.SurfaceMap.MapFragment.biomeSize, map.pos.wy -% margin*terrain.SurfaceMap.MapFragment.biomeSize, preMapSize*terrain.SurfaceMap.MapFragment.biomeSize, preMapSize*terrain.SurfaceMap.MapFragment.biomeSize, worldSeed, .unknown);
			}
		}
		// Add some sub-sub(-sub)*-biomes
		while (extraBiomes.popOrNull()) |biomePoint| {
			addSubBiomesOf(biomePoint, &preMap, &extraBiomes, map.pos.wx -% margin*terrain.SurfaceMap.MapFragment.biomeSize, map.pos.wy -% margin*terrain.SurfaceMap.MapFragment.biomeSize, preMapSize*terrain.SurfaceMap.MapFragment.biomeSize, preMapSize*terrain.SurfaceMap.MapFragment.biomeSize, worldSeed, .known);
		}
		for (0..ClimateMapFragment.mapEntrysSize) |_x| {
			@memcpy(&map.map[_x], preMap[_x + margin][margin..][0..ClimateMapFragment.mapEntrysSize]);
		}
	}
```

## Related Questions
- What is the purpose of the `fillRecursively` function?
- How does the code handle biome transitions in the climate map?
- What role does the `margin` constant play in the generation process?
- Describe the functionality of the `toMap` method.
- How are sub-biomes added to the climate map?
- What is the significance of the `preMapSize` variable?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_4*
