# [hard/codebase_src_server_world.zig] - Chunk 0

**Type:** api
**Keywords:** settings serialization, directory creation, file writing, cache management, reference counting, mutex locking
**Symbols:** Settings, Settings.defaultGamemode, Settings.allowCheats, Settings.testingMode, Settings.seed, Settings.defaults, Settings.fromZon, Settings.toZon, findValidFolderName, tryCreateWorld, ChunkManager, ChunkManager.world, ChunkManager.terrainGenerationProfile, ChunkManager.reducedChunkCacheMask, ChunkManager.chunkCache, ChunkManager.HashContext, ChunkManager.simulationChunkHashMap, ChunkManager.mutex, ChunkManager.getSimulationChunkAndIncreaseRefCount
**Concepts:** world settings, folder name validation, world creation, chunk management

## Summary
Defines world settings, folder name validation, world creation logic, and chunk management for the server.

## Explanation
This chunk contains definitions for world settings, including default gamemode, cheat permissions, testing mode, and seed. It includes a function to validate and create unique folder names for worlds. The `tryCreateWorld` function handles the creation of a new world by setting up directories, writing configuration files, and initializing assets. The `ChunkManager` struct manages chunks within the server world, including caching and reference counting mechanisms.

## Code Example
```zig
pub fn hash(_: HashContext, a: chunk.ChunkPosition) u64 {
			return a.hashCode();
		}
```

## Related Questions
- How does the `Settings` struct handle default values?
- What is the purpose of the `findValidFolderName` function?
- How are chunks managed within the `ChunkManager` struct?
- What error handling is implemented in the `tryCreateWorld` function?
- How are world settings serialized and deserialized?
- What is the role of the `simulationChunkHashMap` in chunk management?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_0*
