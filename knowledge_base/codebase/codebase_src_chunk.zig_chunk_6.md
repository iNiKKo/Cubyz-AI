# [hard/codebase_src_chunk.zig] - Chunk 6

**Type:** implementation
**Keywords:** save, wasStored, wasChanged, loadRegionFileAndIncreaseRefCount, storeChunk, updateFromLowerResolution, getOrGenerateChunkAndIncreaseRefCount, region file, compression, LOD
**Symbols:** wasStored, wasChanged, pos, regionSize, regionMask, region, data, nextPos, nextHigherLod
**Concepts:** chunk persistence, LOD hierarchy, reference counting, compression storage, region file management

## Summary
This chunk implements the Chunk struct's save method, handling disk persistence by loading a region file, compressing and storing the chunk data, updating LOD hierarchy for higher resolutions, and managing reference counts.

## Explanation
The code begins by saving an empty map (map.save(null, .{})). It then checks self.wasStored; if false it sets wasStored=true. If self.wasChanged is true, it computes the region coordinates using pos.voxelSize*chunkSize and main.server.storage.RegionFile.regionSize, masking with regionMask to get the base region index. It loads that region file via loadRegionFileAndIncreaseRefCount, deferring a decreaseRefCount on exit. The chunk data is stored by calling ChunkCompression.storeChunk with .toDisk flag and false for some second argument; the returned buffer is freed after use. Then it calls region.storeChunk passing the compressed data and computed region indices (wx, wy, wz divided by voxelSize/chunkSize). After storing, wasChanged is set to false. If the current voxel size is not at the highest supported LOD, it computes a next position by clearing lower bits (masking with ~@as(i32, pos.voxelSize*chunkSize)) and doubling voxelSize. It retrieves or generates that higher-LOD chunk via world.getOrGenerateChunkAndIncreaseRefCount, deferring its refcount decrease, then calls updateFromLowerResolution(self) on it.

## Related Questions
- What is the purpose of map.save(null, .{}) in this chunk?
- How does the code determine which region file to load for a given chunk position?
- What happens when self.wasChanged is true during save?
- Where is the compressed chunk data stored and how is it passed to the region file?
- Under what condition does the code generate or retrieve a higher LOD chunk?
- How are reference counts managed for both the loaded region and the next LOD chunk?
- What role does ChunkCompression.storeChunk play in this save flow?
- Why is wasChanged set to false after storing the chunk data?
- How are the region indices computed from the chunk position and voxel size?
- Does this code handle any error conditions when loading or storing chunks?

*Source: unknown | chunk_id: codebase_src_chunk.zig_chunk_6*
