# [easy/codebase_src_server_terrain_simple_structures_SbbGen.zig] - Chunk 0

**Type:** world_generation
**Keywords:** reference counting, binary serialization, mutex locking, structure placement, blueprint loading, recursive generation
**Symbols:** id, generationMode, SbbGen, structureRef, placeMode, rotation, getHash, loadModel, generate, placeSbb, alignDirections
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
The `SbbGen` struct handles the generation of structures using SBB (Structure Building Block) models, including loading parameters and placing structures in chunks.

## Explanation
`id = "cubyz:sbb"`, `generationMode = .floor`. The `SbbGen` struct is responsible for generating structures based on SBB (Structure Building Block) models. `loadModel` requires a `structure` field (errors and returns `null` if missing, or if no matching blueprint is found by that ID); `placeMode` defaults to `"degradable"` if omitted or unrecognized; `rotation` defaults to `.random` if the field is missing or invalid (logging an error either way). `generate` places the main structure and recursively handles child structures via `placeSbb`, which pastes the rotated blueprint into the chunk using `self.placeMode`, then recurses into each of the blueprint's `childBlocks`. `alignDirections` computes (via a comptime-built lookup table) the rotation needed to align an input direction with a desired one. `getHash` combines `placeMode` and the structure's ID via `std.hash.Wyhash`.

## Code Example
```zig
pub fn getHash(self: SbbGen) u64 {
	return std.hash.Wyhash.hash(@intFromEnum(self.placeMode), self.structureRef.id);
}
```

## Related Questions
- How does the `SbbGen` struct load its configuration?
- What is the purpose of the `getHash` method in `SbbGen`?
- How does the `generate` method place structures in a chunk?
- What error handling is implemented in the `loadModel` function?
- How are child structures handled during generation?
- What role does the `alignDirections` function play in structure placement?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_SbbGen.zig_chunk_0*
