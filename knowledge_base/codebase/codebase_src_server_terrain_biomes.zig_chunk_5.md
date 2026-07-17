# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 5

**Type:** implementation
**Keywords:** hash map, list manipulation, error handling, data registration, memory allocation
**Symbols:** parentEdgeDistance, UnfinishedSubBiomeData, UnfinishedSubBiomeData.getItem, unfinishedSubBiomes, UnfinishedTransitionBiomeData, TransitionBiome, unfinishedTransitionBiomes, reset, register, finishLoading, hasRegistered, getById, getByIdOptional, getByIndex, getPlaceholderBiome
**Concepts:** biome management, terrain generation, world data initialization

## Summary
This chunk manages biome registration, loading, and retrieval in the Cubyz server terrain system.

## Explanation
The chunk defines structures for unfinished sub-biome and transition data, as well as functions to register biomes, finish loading them, check if a biome is registered, retrieve biomes by ID or index, and get a placeholder biome. It uses `std.StringHashMapUnmanaged` to store unfinished sub-biomes and transitions, and manages lists of surface and cave biomes. The `finishLoading` function processes these lists, initializes data structures, and handles errors such as missing parent biomes or overlapping properties in transition biomes.

## Code Example
```zig
pub fn getItem(self: UnfinishedSubBiomeData) SubBiomeData {
	return .{.biome = getById(self.biomeId), .parentEdgeDistance = self.parentEdgeDistance};
}
```

## Related Questions
- How do you register a new biome?
- What happens if a parent biome is not found during transition processing?
- How are biomes stored and retrieved by ID?
- What does the `reset` function do?
- How are sub-biomes associated with their parent biomes?
- What is the purpose of the `finishLoading` function?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_5*
