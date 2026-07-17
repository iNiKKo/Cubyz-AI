# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 2

**Type:** implementation
**Keywords:** deleteTree, openIterableDir, parseInt, Array2D, NeverFailingAllocator, defer, comptime registry, voxelSizeShift, biomePalette, FractalNoise
**Symbols:** MapGenerator, cacheInit, InterpolationPolynomial, TiledNoise, regenerateLOD
**Concepts:** LOD regeneration, terrain generation, file system traversal, noise interpolation, static registry, deferred cleanup, memory pool allocation, biome palette loading, fractal noise synthesis, path construction

## Summary
Chunk implements LOD regeneration by deleting old map directories and scanning the saves/maps/1 folder to collect MapFragmentPosition entries for rebuilding terrain.

## Explanation
The chunk declares a public function regenerateLOD(worldName) that logs, allocates a TiledNoise instance with size 8*MapFragment.mapSize (deferred deinit), then iterates LOD levels from 1 up to main.settings.highestSupportedLod+1. For each level it builds a path string 'saves/{worldName}/maps/{lod}' and calls main.files.cubyzDir().deleteTree(path) on error, logging only if the error is not FileNotFound. After clearing old LODs, it opens the directory at saves/maps/1 using main.files.cubyzDir().openIterableDir, then iterates over entries: directories are skipped; for each entry it parses the wx coordinate from the name (parseInt), opens that subdirectory, and iterates its contents to find files. For each file it extracts the wy coordinate by locating the first '.' in the filename and parsing the prefix as i32. Valid entries are appended into a main.List(MapFragmentPosition) with voxelSize=1 and voxelSizeShift=0. The chunk also defines MapGenerator (init, generateMapFragment fields plus a comptime registry), cacheInit(pos) which creates a MapFragment from memoryPool, loads biomePalette, and if that fails calls profile.mapFragmentGenerator.generateMapFragment; InterpolationPolynomial struct with init(noise) solving for coefficients a,b,c and eval(x) clamping result to [0,0.99999]; TiledNoise struct holding noisePolynomials (Array2D of InterpolationPolynomial) and sizeMask, with init(allocator,size) that asserts power-of-two, generates sparse fractal terrain into rawNoise, then maps each cell to an InterpolationPolynomial via polynomial.* = .init(noise); deinit releases the polynomials; get(wx,wy) masks indices and retrieves from noisePolynomials. The chunk uses main.heap.MemoryPool(MapFragment), main.server.world.?.biomePalette, profile (TerrainGenerationProfile), terrain.noise.FractalNoise.generateSparseFractalTerrain, main.files.cubyzDir() for file system operations, std.fmt.allocPrint for path construction, and main.io for iteration.

## Related Questions
- How does regenerateLOD handle errors when deleting old LOD directories?
- What is the purpose of the sizeMask field in TiledNoise and how is it computed?
- Why are only files with a '.' character considered valid map entries during regeneration?
- How does cacheInit decide whether to load biomePalette or call generateMapFragment?
- Which allocator is used for rawNoise in TiledNoise.init and why is that choice made?
- What happens if main.server.world.?.biomePalette fails to load inside cacheInit?
- Is the MapGenerator registry populated at compile time or runtime, and how are entries added?
- How does InterpolationPolynomial.init solve for coefficients a,b,c given noise input?
- Does regenerateLOD preserve any LODs beyond highestSupportedLod after deletion loop?
- What is the exact path pattern used to locate stored maps during regeneration?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_2*
