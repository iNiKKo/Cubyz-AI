# [easy/codebase_src_server_terrain_terrain.zig] - Chunk 0

**Type:** implementation
**Keywords:** terrain gen, biome init, blue noise load, chunk generators, generator state, block generator, generator registry, init and init, global init, deinit
**Symbols:** ZonElement, NeverFailingAllocator, biomes, noise, structures, Biome, ClimateMap, SurfaceMap, LightMap, CaveBiomeMap, CaveMap, cave_layers, StructureMap, sbb, sdf, chunk_generators, GeneratorState, BlockGenerator, generatorRegistry, getAndInitGenerators, TerrainGenerationProfile, init, globalInit, deinit
**Concepts:** terrain generation, biome initialization, blue noise loading

## Summary
Terrain generation and biome initialization logic

## Explanation
This chunk defines the terrain generation profile, initializes various maps and biomes, and loads blue noise. It includes detailed information about the `BlockGenerator` struct which contains initialization function (`init`), generation function (`generate`), priority level (`priority`), generator-specific seed (`generatorSeed`), and default state (`defaultState`). The `init` function is a pointer to a function that initializes the generator with parameters of type `ZonElement`. The `generate` function is a pointer to a function that generates blocks in a chunk using a seed, a server chunk, a cave map view, and a biome map view. Generators are prioritized based on their `priority` value with higher values indicating higher priority. The default state for a generator is defined in the `BlockGenerator` struct as either `enabled` or `disabled`. It also includes functions for global initialization and deinitialization, and lists all supported block generators through `generatorRegistry`. Climate wavelengths affect terrain generation by influencing various aspects such as temperature, humidity, vegetation density, and elevation. The specific values for climate wavelengths are `[5]f32 = [2400, 3200, 2400, 2400, 500]` corresponding to hot-cold, land-ocean, wet-dry, vegetation, and mountain respectively.

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

*Source: unknown | chunk_id: codebase_src_server_terrain_terrain.zig_chunk_0*
