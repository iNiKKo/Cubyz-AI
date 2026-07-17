# [easy/codebase_src_server_terrain_LightMap.zig] - Chunk 0

**Type:** implementation
**Keywords:** cache, deferredDeinit, getHeight, LightMapFragment, mapMask, voxelSize, surfaceMap, lossyCast, findOrCreate, globalAllocator, terrain integration, bit masking, LRU cache, height sampling, garbage collection
**Symbols:** LightMapFragment, LightMapFragment.mapShift, LightMapFragment.mapSize, LightMapFragment.mapMask, LightMapFragment.startHeight, LightMapFragment.pos, LightMapFragment.init, LightMapFragment.privateDeinit, LightMapFragment.deferredDeinit, LightMapFragment.getHeight, cache, cacheInit, deinit, getOrGenerateFragment
**Concepts:** lightmap caching, LRU cache, heightmap sampling, coordinate masking, garbage collection deferral, terrain generation integration, bitwise indexing, global allocator usage

## Summary
This chunk defines the LightMapFragment data structure and a global LRU cache for storing per-block-column light start heights. It provides initialization logic that reads terrain heightmaps to compute base heights with a +16 heuristic, maps coordinates into 2D arrays using bit shifts and masks, and exposes public functions to retrieve or generate fragments via the cache.

## Explanation
The chunk declares LightMapFragment as a pub struct containing mapShift (8), mapSize (256), mapMask (255), startHeight array of i16 sized 256*256, and pos field of type MapFragmentPosition. It defines init(self: *LightMapFragment, wx: i32, wy: i32, voxelSize: u31) which sets self.pos via MapFragmentPosition.init using the passed coordinates and voxel size; privateDeinit frees the fragment through main.globalAllocator.destroy; deferredDeinit registers the fragment for garbage collection by calling main.heap.GarbageCollection.deferredFree with a cast of privateDeinit. getHeight(self, wx, wy) computes xIndex = wx >> self.pos.voxelSizeShift & mapMask and yIndex similarly, then returns startHeight indexed as xIndex << mapShift | yIndex after casting indices to usize. A global cache variable is declared: var cache: Cache(LightMapFragment, 64, 8, LightMapFragment.deferredDeinit) = .{}, using associativity 8 and deferredDeinit for cleanup. The chunk imports terrain.zig and uses terrain.SurfaceMap.getOrGenerateFragment to obtain the heightmap; it asserts that LightMapFragment.mapSize equals terrain.SurfaceMap.MapFragment.mapSize at compile time. cacheInit(pos: MapFragmentPosition) allocates a new LightMapFragment via main.globalAllocator.create, calls init with pos.wx/pos.wy/pos.voxelSize, obtains surfaceMap = terrain.SurfaceMap.getOrGenerateFragment(pos.wx, pos.wy, pos.voxelSize), then iterates over x and y from 0..mapSize to compute baseHeight = std.math.lossyCast(i16, surfaceMap.heightMap[x][y]) and sets startHeight[x << mapShift | y] = @max(0, baseHeight +| 16) as a simple heuristic. deinit() clears the cache via cache.clear(). getOrGenerateFragment(wx, wy, voxelSize) first normalizes wx/wy by masking with ~(@as(i32, LightMapFragment.mapMask*voxelSize | voxelSize - 1)) to align to voxel boundaries, creates compare = MapFragmentPosition.init(normalized wx, normalized wy, voxelSize), then calls cache.findOrCreate(compare, cacheInit, null) and returns the result. All operations are deterministic; no concurrency primitives beyond atomic.Value import (unused here). Memory ownership: fragments allocated on main.globalAllocator, freed via privateDeinit or deferred through GarbageCollection.

## Related Questions
- How does LightMapFragment.getHeight map 3D world coordinates to the startHeight array?
- What is the purpose of the +16 heuristic in cacheInit and why is it marked as a TODO?
- Why does getOrGenerateFragment mask wx/wy with ~(@as(i32, LightMapFragment.mapMask*voxelSize | voxelSize - 1)) before creating MapFragmentPosition?
- Explain how deferredDeinit uses main.heap.GarbageCollection.deferredFree and what happens when the fragment is freed.
- What does cache.findOrCreate do in getOrGenerateFragment and why is null passed as the default value?
- How does the chunk ensure that LightMapFragment.mapSize matches terrain.SurfaceMap.MapFragment.mapSize at compile time?
- Describe the memory lifecycle of a LightMapFragment from creation via main.globalAllocator.create to destruction.
- Why is privateDeinit marked private while deferredDeinit is public and used for garbage collection?
- What role does MapFragmentPosition play in coordinating between this chunk and terrain.SurfaceMap.getOrGenerateFragment?
- How are xIndex and yIndex computed inside getHeight using bitwise shifts and masks?
- Is there any concurrency protection around the global cache variable, or is it assumed single-threaded?
- Where would a developer look to modify the lightmap generation logic if they wanted to replace the +16 heuristic with terrain-aware values?

*Source: unknown | chunk_id: codebase_src_server_terrain_LightMap.zig_chunk_0*
