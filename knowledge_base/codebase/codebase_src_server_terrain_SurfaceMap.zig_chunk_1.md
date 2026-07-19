# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 1

**Type:** documentation
**Keywords:** MapFragment, height map, biome map, terrain data, file loading, file saving, compression, versioning
**Symbols:** MapFragment, MapFragment.biomeShift, MapFragment.biomeSize, MapFragment.mapShift, MapFragment.mapSize, MapFragment.mapMask, MapFragment.heightMap, MapFragment.biomeMap, MapFragment.caveBiomeOffsetMap, MapFragment.minHeight, MapFragment.maxHeight, MapFragment.pos, MapFragment.wasStored, MapFragment.init, MapFragment.privateDeinit, MapFragment.deferredDeinit, MapFragment.getBiome, MapFragment.getHeight, MapFragment.getCaveBiomeOffset, MapFragment.StorageHeader, MapFragment.StorageHeader.minSupportedVersion, MapFragment.StorageHeader.activeVersion, MapFragment.StorageHeader.version, MapFragment.StorageHeader.neighborInfo, MapFragment.NeighborInfo, MapFragment.load, MapFragment.save
**Concepts:** terrain generation, biome mapping, data storage, file I/O, compression, versioning

## Summary
The `MapFragment` struct manages the generation, storage, and retrieval of terrain height and biome maps for a planet.

## Explanation
The `MapFragment` struct manages the generation, storage, and retrieval of terrain height and biome maps for a planet. It includes methods to initialize (`init`), deinitialize (`privateDeinit`, `deferredDeinit`), retrieve biome (`getBiome`), height (`getHeight`), and cave biome offset (`getCaveBiomeOffset`) data. The struct also handles loading (`load`) and saving (`save`) map data from and to disk, including versioning and compression of the data.

### Constants
- `biomeShift`: 5
- `biomeSize`: 1 << biomeShift (32)
- `mapShift`: 8
- `mapSize`: 1 << mapShift (256)
- `mapMask`: mapSize - 1 (255)

### Methods
- **init**: Initializes the `MapFragment` with given coordinates and voxel size. Generates sparse fractal terrain using noise.
- **privateDeinit**: Destroys the `MapFragment` instance using a memory pool.
- **deferredDeinit**: Marks the `MapFragment` for deferred destruction using garbage collection.
- **getBiome**: Retrieves the biome at specified world coordinates.
- **getHeight**: Retrieves the height at specified world coordinates.
- **getCaveBiomeOffset**: Retrieves the cave biome offset at specified world coordinates.

### Loading and Saving
- **load**: Loads map data from a file, handling different versions (0 and 1) and decompressing the data. Reads biome, height, and original height maps.
- **save**: Saves map data to a file, compressing the data using fast compression for performance. Writes biome, height, and original height maps.

### StorageHeader
The `StorageHeader` includes version information and neighbor info, playing a crucial role in versioning and data integrity during loading and saving processes.

## Code Example
```zig
fn privateDeinit(self: *MapFragment) void {
		memoryPool.destroy(self);
	}
```

## Related Questions
-  How does the `MapFragment` struct handle versioning in its data files?
-  What is the purpose of the `deferredDeinit` method in the `MapFragment` struct?
-  Can you explain how the `load` method decompresses and reads the map data from a file?
-  What role does the `StorageHeader` play in the `MapFragment` struct's functionality?
-  How is the terrain height data stored and retrieved within the `MapFragment` struct?
-  What are the benefits of using compression when saving map data in the `MapFragment` struct?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_1*
