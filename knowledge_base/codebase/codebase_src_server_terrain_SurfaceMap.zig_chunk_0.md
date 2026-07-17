# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 0

**Type:** implementation
**Keywords:** fractal noise, voxel grid, map fragment, neighbor flags, garbage collection, power of two, bitfield packing, binary reader, atomic bool, deferred free
**Symbols:** map_generators, MapFragmentPosition, MapFragmentPosition.init, MapFragmentPosition.equals, MapFragmentPosition.hashCode, MapFragmentPosition.getMinDistanceSquared, MapFragmentPosition.getPriority, MapFragment, biomeShift, biomeSize, mapShift, mapMask, heightMap, biomeMap, caveBiomeOffsetMap, minHeight, maxHeight, pos, wasStored, privateDeinit, deferredDeinit, getBiome, getHeight, getCaveBiomeOffset, StorageHeader, NeighborInfo
**Concepts:** terrain generation, biome mapping, cave offset computation, binary serialization, atomic state management, deferred deallocation, spatial hashing, coordinate alignment, noise fractal terrain

## Summary
This chunk defines the MapFragment data structure and its associated map generators, handling terrain height maps, biome assignments, cave offsets, neighbor information, serialization via binary files, atomic state tracking, deferred memory deallocation, and coordinate alignment logic.

## Explanation
The chunk declares a public const map_generators imported from an external list file. It defines MapFragmentPosition with fields wx, wy, voxelSize, voxelSizeShift; includes init (asserts power-of-two voxelSize and grid-aligned coordinates), equals, hashCode, getMinDistanceSquared, and getPriority methods for spatial queries. It defines MapFragment with static constants biomeShift, biomeSize, mapShift, mapSize, mapMask; fields heightMap, biomeMap, caveBiomeOffsetMap, minHeight, maxHeight, pos, wasStored (Atomic bool). init allocates a 2D f32 caveBiomeOffsetMap via main.utils.Array2D, calls terrain.noise.FractalNoise.generateSparseFractalTerrain with the world seed XORed by a constant, then floors values into self.caveBiomeOffsetMap. privateDeinit destroys self via memoryPool; deferredDeinit registers self for garbage collection using a cast function to opaque type. getBiome, getHeight, getCaveBiomeOffset compute indices by right-shifting wx/wy by voxelSizeShift and masking with mapMask, then return the corresponding array element. StorageHeader is a packed struct containing version (u8) and NeighborInfo; NeighborInfo is a packed u8 bitfield with flags @

## Related Questions
- What assertions does MapFragmentPosition.init perform on voxelSize and coordinates?
- How is the caveBiomeOffsetMap allocated and populated in MapFragment.init?
- What seed transformation is applied to terrain.noise.FractalNoise.generateSparseFractalTerrain?
- Which methods compute spatial queries for a player position relative to a map fragment?
- How are biome, height, and cave offset indices derived from world coordinates in getBiome/getHeight/getCaveBiomeOffset?
- What is the purpose of privateDeinit versus deferredDeinit on MapFragment?
- Which flags does NeighborInfo expose via its packed bitfield definition?
- How does StorageHeader encode version and neighbor information for binary serialization?
- What role does wasStored play in managing the lifecycle of a map fragment?
- Where is the serialized surface file path constructed from MapFragmentPosition fields?
- How does hashCode combine wx, wy, and voxelSize to produce a u32 hash value?
- What memory pool mechanism is used for destroying MapFragment instances?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_0*
