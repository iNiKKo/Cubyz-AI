# [easy/codebase_src_server_terrain_climategen_SingleBiome.zig] - Chunk 0

**Type:** world_generation
**Keywords:** biome, ClimateMapFragment, ValueNoise, roughness, hills, mountains, seed, parameters, mapSize, mapEntrysSize
**Symbols:** id, biome, init, generateMapFragment
**Concepts:** single biome climate generation, noise sampling, circular heat distribution, height map construction, parameterized biome lookup

## Summary
This chunk defines a single-biome climate map generator that initializes biome data from parameters and produces height/roughness maps using noise sampling within a circular radius.

## Explanation
The chunk declares several imported constants: std, build_options, main (with submodules utils.Array2D, random, ZonElement), server.terrain (ClimateMapFragment, BiomeSample, Biome, TreeNode, noise.ValueNoise), vec (Vec2i, Vec2f), and heap.NeverFailingAllocator. It exposes a public const id = "cubyz:single_biome" identifying the biome type. A global var biome is initialized to undefined; init(parameters: ZonElement) retrieves the Biome by name from parameters.get("biome") or defaults to "missing parameter 'biome'" and assigns it to biome. generateMapFragment(map: *ClimateMapFragment, worldSeed: u64) iterates over map.map (a 2D array of ClimateMapFragment entries), computing wx/wy indices by adding x*y offsets scaled by ClimateMapFragment.mapSize/ClimateMapFragment.mapEntrysSize; it samples terrain.noise.ValueNoise.samplePoint2D with coordinates normalized by biome.radius/2 and worldSeed, then writes a struct literal into map.map[x][y] containing .biome = biome, .height computed as biome.minHeight + (biome.maxHeight - biome.minHeight) * noiseValue, plus biome.roughness, biome.hills, biome.mountains, and seed set to worldSeed ^ 53298562891.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	biome = terrain.biomes.getById(parameters.get([]const u8, "biome") orelse "missing parameter 'biome'");
}
```

## Related Questions
- What biome name is used as the default when parameters does not contain a valid biome entry?
- How are the wx and wy coordinates computed inside generateMapFragment to map local indices to world space?
- Which noise function is called to sample terrain height values, and what arguments does it receive?
- What formula combines biome.minHeight, biome.maxHeight, and the sampled noise value to produce final height?
- How is the seed field of each ClimateMapFragment entry derived from worldSeed in this chunk?
- Does generateMapFragment modify any fields other than map.map entries, or does it only write into the fragment's data array?
- What happens if biome.radius is zero when computing normalized noise coordinates?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_SingleBiome.zig_chunk_0*
