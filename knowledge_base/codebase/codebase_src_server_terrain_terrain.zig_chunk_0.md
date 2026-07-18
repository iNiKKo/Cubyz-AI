# [easy/codebase_src_server_terrain_terrain.zig] - Chunk 0

**Type:** implementation
**Keywords:** terrain gen, biome init, blue noise load, chunk generators, generator state, block generator, generator registry, init and init, global init, deinit
**Symbols:** ZonElement, NeverFailingAllocator, biomes, noise, structures, Biome, ClimateMap, SurfaceMap, LightMap, CaveBiomeMap, CaveMap, cave_layers, StructureMap, sbb, sdf, chunk_generators, GeneratorState, BlockGenerator, generatorRegistry, getAndInitGenerators, TerrainGenerationProfile, init, globalInit, deinit
**Concepts:** terrain generation, biome initialization, blue noise loading

## Summary
Terrain generation and biome initialization logic

## Explanation
This chunk defines the terrain generation profile, initializes various maps and biomes, and loads blue noise. It also includes functions for global initialization and deinitialization.

## Code Example
```zig
pub const GeneratorState = enum { enabled, disabled }
```

## Related Questions
- What is the purpose of the `BlockGenerator` struct?
- How are generators prioritized in the generation process?
- What is the default state for a generator?
- Where can I find the list of all supported block generators?
- How do climate wavelengths affect terrain generation?
- What is the global initialization function for terrain generation?

*Source: unknown | chunk_id: codebase_src_server_terrain_terrain.zig_chunk_0*
