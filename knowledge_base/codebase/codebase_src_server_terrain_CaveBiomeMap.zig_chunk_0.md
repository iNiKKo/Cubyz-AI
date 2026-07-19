# [hard/codebase_src_server_terrain_CaveBiomeMap.zig] - Chunk 0

**Type:** world_generation
**Keywords:** 3D array, generator registry, rotation matrix, deferred deinitialization, priority sorting
**Symbols:** CaveBiomeMapFragment, CaveBiomeMapFragment.caveBiomeShift, CaveBiomeMapFragment.caveBiomeSize, CaveBiomeMapFragment.caveBiomeMask, CaveBiomeMapFragment.caveBiomeMapShift, CaveBiomeMapFragment.caveBiomeMapSize, CaveBiomeMapFragment.caveBiomeMapMask, CaveBiomeMapFragment.pos, CaveBiomeMapFragment.biomeMap, CaveBiomeMapFragment.init, CaveBiomeMapFragment.privateDeinit, CaveBiomeMapFragment.deferredDeinit, CaveBiomeMapFragment.rotationMatrixShift, CaveBiomeMapFragment.fac, CaveBiomeMapFragment.rotationMatrix, CaveBiomeMapFragment.transposeRotationMatrix, CaveBiomeMapFragment.rotate, CaveBiomeMapFragment.rotateInverse, CaveBiomeMapFragment.getIndex, CaveBiomeGenerator, CaveBiomeGenerator.init, CaveBiomeGenerator.generate, CaveBiomeGenerator.priority, CaveBiomeGenerator.generatorSeed, CaveBiomeGenerator.defaultState, CaveBiomeGenerator.generatorRegistry, CaveBiomeGenerator.getAndInitGenerators
**Concepts:** chunk meshing, terrain generation, biome data management

## Summary
Defines the CaveBiomeMapFragment and CaveBiomeGenerator structs for managing cave biome data and generation.

## Explanation
The chunk defines two main structures: CaveBiomeMapFragment and CaveBiomeGenerator. CaveBiomeMapFragment represents a fragment of the world's cave biome map, storing positions and biome data. It includes methods for initialization, deferred deinitialization, rotation transformations, and index calculation. The constants defined in CaveBiomeMapFragment are as follows: caveBiomeShift = 7, caveBiomeSize = 1 << caveBiomeShift (128), caveBiomeMask = caveBiomeSize - 1 (127), caveBiomeMapShift = 11, caveBiomeMapSize = 1 << caveBiomeMapShift (2048), and caveBiomeMapMask = caveBiomeMapSize - 1 (2047). The rotation matrix values are: @Vector(3, i64){20*fac, 0*fac, 15*fac}, @Vector(3, i64){9*fac, 20*fac, -12*fac}, and @Vector(3, i64){-12*fac, 15*fac, 16*fac}. CaveBiomeGenerator is responsible for generating cave biomes, with methods for initialization and generation processes. The generator registry compiles all available generators from the 'cavebiomegen/_list.zig' file into a static string map, allowing for dynamic retrieval and prioritization of biome generation algorithms.

## Code Example
```zig
pub fn init(self: *CaveBiomeMapFragment, wx: i32, wy: i32, wz: i32) void {
	self.* = .{
		.pos = main.chunk.ChunkPosition{
			.wx = wx,
			.wy = wy,
			.wz = wz,
			.voxelSize = caveBiomeSize,
		},
	};
}
```

## Related Questions
- What is the purpose of the CaveBiomeMapFragment struct?
- How does the CaveBiomeMapFragment handle initialization and deinitialization?
- What role does the rotation matrix play in the CaveBiomeMapFragment?
- How are cave biome generators registered and retrieved?
- What is the process for initializing cave biome generators with settings?
- How are cave biome generators prioritized during generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_CaveBiomeMap.zig_chunk_0*
