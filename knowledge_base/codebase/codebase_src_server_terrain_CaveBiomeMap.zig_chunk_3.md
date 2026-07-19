# [hard/codebase_src_server_terrain_CaveBiomeMap.zig] - Chunk 3

**Type:** api
**Keywords:** world coordinates, grid points, bitwise operations, seed generation, coordinate bounds checking
**Symbols:** getCaveBiomeOffset, _getBiome, getGridPointFromPrerotated, getGridPoint, getGridPointAndHeight, getRoughBiome, getRoughBiomeAndHeight, getBiome, getBiomeAndSeed, getBiomeColumnAndSeed
**Concepts:** cave biome mapping, terrain generation, biome retrieval

## Summary
Handles cave biome mapping and retrieval for the server terrain.

## Explanation
This chunk defines methods for retrieving cave biomes based on world coordinates. The `getCaveBiomeOffset` function calculates the offset for a given position, using bitwise operations to determine the index in the surface fragments array. The `_getBiome` function retrieves the biome at a specific grid point, using assertions for coordinate bounds checking. The `getGridPointFromPrerotated` and `getGridPoint` functions calculate the grid point from a rotated position, while `getGridPointAndHeight` also determines the height of the grid point. The `getRoughBiome` and `getRoughBiomeAndHeight` methods return a rough biome based on the world coordinates, with optional seed generation. The `getBiome` function retrieves the exact biome at a given position, while `getBiomeAndSeed` also returns a unique seed for each biome position. The `getBiomeColumnAndSeed` method is similar to `getBiomeAndSeed`, but it also determines the height of the biome column. The code uses bitwise operations and assertions for efficient calculations and interacts with other components like `MapFragment` and `Biome`. It also generates unique seeds using a custom hash function that combines the grid point coordinates and the world seed.

## Code Example
```zig
pub fn getBiome(self: CaveBiomeMapView, relX: i32, relY: i32, relZ: i32) *const Biome {
		return self.getBiomeAndSeed(relX, relY, relZ, false, undefined);
	}
```

## Related Questions
- How does the code handle coordinate out of bounds?
- What is the purpose of the `getSeed` parameter in the functions?
- Can you explain the rotation matrix used in the code?
- How does the code ensure unique seed generation for each biome position?
- What are the differences between `getRoughBiome` and `getRoughBiomeAndHeight` methods?
- chunk_type_description: This chunk is part of the server terrain module, specifically dealing with cave biomes. It provides a set of functions to map and retrieve biomes based on world coordinates, including handling surface biomes and generating unique seeds for each biome position.
- related_chunks: ["MapFragment", "Biome", "TerrainGeneration"]
- chunk_dependencies: ["std.debug.assert", "vec.dot", "main.server.world.settings.seed"]

*Source: unknown | chunk_id: codebase_src_server_terrain_CaveBiomeMap.zig_chunk_3*
