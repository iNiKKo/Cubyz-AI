# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 6

**Type:** api
**Keywords:** finishedLoading, biomesById, caveBiomes, getCheckSum, XOR accumulation, placeholder biome, index access, slice return, assert precondition
**Symbols:** getById, getByIdOptional, getByIndex, getPlaceholderBiome, getCaveBiomes, getBiomeCheckSum
**Concepts:** biome lookup, fallback handling, checksum computation, slice access, assert precondition

## Summary
This chunk defines public accessor functions for the Biome collection, including lookup by ID (with fallback), index access, placeholder retrieval, cave biome enumeration, and a checksum computation over all biomes.

## Explanation
The chunk declares several pub fn entries that operate on global state (biomesById, biomes.items, caveBiomes.items) under the precondition finishedLoading. getById performs an assert then uses biomesById.get(id); if missing it logs an error and returns &biomes.items[0]. getByIdOptional mirrors this but returns null instead of a fallback. getByIndex asserts then directly indexes biomesByIndex.items[index]. getPlaceholderBiome simply returns &biomes.items[0]. getCaveBiomes returns caveBiomes.items as a slice. getBiomeCheckSum takes a seed u64, initializes result to the seed, XORs each biome's checksum from both biomes.items and caveBiomes.items, then returns the accumulated value.

## Related Questions
- What precondition must be satisfied before calling getById?
- How does getById handle a missing biome ID?
- What does getByIdOptional return when the biome is not found?
- Which global collection does getByIndex read from directly?
- What slice does getCaveBiomes expose to callers?
- How is the checksum seed incorporated into getBiomeCheckSum's result?
- Does getBiomeCheckSum iterate over cave biomes as well as regular biomes?
- Which accessor returns a reference to the first biome in the collection?
- What assertion is common across all getById variants?
- How does the chunk ensure consistent access patterns for biomes?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_6*
