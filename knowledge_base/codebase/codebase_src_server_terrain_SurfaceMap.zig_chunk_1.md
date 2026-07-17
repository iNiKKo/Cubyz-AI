# [hard/codebase_src_server_terrain_SurfaceMap.zig] - Chunk 1

**Type:** serialization
**Keywords:** packed struct, bitCast, BinaryReader, BinaryWriter, deflate, inflateTo, StaticStringMap, monotonic store, paletteId, heightMap
**Symbols:** StorageHeader, NeighborInfo, MapFragment, MapFragment.load, MapFragment.save, MapGenerator, generatorRegistry, getGeneratorById
**Concepts:** surface map serialization, neighbor info encoding, binary reader/writer, compression deflate/inflate, static generator registry, file I/O path creation

## Summary
This chunk defines the MapFragment struct for loading and saving surface maps, including neighbor info encoding, binary serialization with compression, and a static registry of map generators.

## Explanation
The chunk declares StorageHeader (version + NeighborInfo), NeighborInfo packed struct with eight directional flags, and MapFragment containing biomeMap, heightMap, pos, version, wasStored. load() reads compressed .surface files from saves/{world}/maps/{voxelSize}/{wx}/{wy}.surface, parses header.version 0 (inflate to raw bytes, read u32 paletteId + f32 height) or 1 (inflate to raw bytes, read u32 paletteId + i32 height), populates self.biomeMap and self.heightMap via biomePalette.getById, optionally fills originalHeightMap if provided, sets wasStored.store(true,.monotonic). save() writes compressed data: header.version=activeVersion(1), neighborInfo bitcast, then deflate-compressed biomeData (u32 paletteIds), heightData (i32 heights), and optional originalHeightData (i32 heights) into a BinaryWriter, creates parent folder if missing, and writes to the same path. MapGenerator is a const struct with init and generateMapFragment function pointers; generatorRegistry is a std.StaticStringMap populated comptime from map_generators decls, providing getGeneratorById(id) returning !MapGenerator or error.UnknownMapGenerator.

## Related Questions
- What version numbers are supported by the surface map format and how does load() handle each?
- How is NeighborInfo encoded in the binary file and what flags does it contain?
- Describe the exact steps load() takes to read a compressed .surface file into MapFragment fields.
- Explain how save() writes neighbor info, biome data, height data, and optional original height data with compression.
- What error is returned if the stored version in the file does not match activeVersion?
- How does load() populate self.biomeMap using main.server.terrain.biomes.getById and what type does it expect?
- What happens to wasStored after a successful load and why use .monotonic?
- Show how save() creates or updates the parent folder before writing the file.
- How is the generatorRegistry constructed comptime and what fields does MapGenerator expose?
- What error does getGeneratorById return if no matching id is found in the registry?

*Source: unknown | chunk_id: codebase_src_server_terrain_SurfaceMap.zig_chunk_1*
