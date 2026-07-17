# [easy/codebase_mods_cubyz_rotations_ore.zig] - Chunk 0

**Type:** implementation
**Keywords:** rotation mode, cube model, transparent block, view through, neighbor occluded, model cache, quad list duplication, texture slot offset, opaque in lod, block data swap
**Symbols:** modelCache, init, deinit, reset, createBlockModel, generateData, modifyBlock, canBeChangedInto, onBlockBreaking, formatBlockData
**Concepts:** ore rotation, model caching, block modification, neighbor occlusion check, texture slot offset, serialization format

## Summary
This chunk defines the ore rotation system for Cubyz, providing functions to create and cache block models (specifically for cube-based ores), modify blocks in place, determine if a block can be changed into another type during rotation, handle breaking of rotated blocks, and format block data for serialization.

## Explanation
The chunk imports the main module's blocks, models, vec, ZonElement, and rotation types. It declares a global modelCache variable to hold a cached ModelIndex for cube-based ores. The init() and deinit() functions are empty stubs; reset() clears the cache by setting modelCache to null. createBlockModel(block, _, zon) extracts the model ID from the ZonElement (falling back to 'cubyz:cube' if parsing fails), validates that it is exactly 'cubyz:cube', and returns early with the cached index if available. If not cached, it retrieves the base cube model, copies its quad list into a managed ListManaged<QuadInfo>, appends each original quad again (doubling the face count) while incrementing textureSlot by 16 for the duplicated faces and setting opaqueInLod to 2 on originals, then initializes a new ModelIndex from the modified quads and caches it. generateData is an empty stub returning false. modifyBlock(block, newBlockType) checks that the block is not transparent or view-through, that all neighbors are occluded (via model().allNeighborsOccluded), and that data != 0; if any check fails it returns false; otherwise it sets block.data = block.typ and block.typ = newBlockType. canBeChangedInto(oldBlock, newBlock, _, shouldDropSourceBlockOnSuccess) verifies oldBlock != newBlock, non-transparent/non-view-through, occluded neighbors, data != 0, and that newBlock.data == oldBlock.typ; if all pass it sets shouldDropSourceBlockOnSuccess.* = false and returns .{.yes_costsItems = 1}. onBlockBreaking(item, _, _, currentData) swaps the block's typ and data fields (setting data to 0). formatBlockData(block, _list) appends a serialized representation of the block with its original data moved into typ and data cleared.

## Related Questions
- What happens if createBlockModel receives a ZonElement that does not parse to a string?
- Under what conditions will modifyBlock return false without modifying the block?
- How is textureSlot adjusted when duplicating quads in createBlockModel?
- Why does canBeChangedInto set shouldDropSourceBlockOnSuccess to false on success?
- What value does generateData always return and why might that be intentional?
- Does reset() affect any other global state besides modelCache?
- How is the base cube model obtained inside createBlockModel?
- What fields are swapped in onBlockBreaking and what do they represent?
- Can a block with data == 0 ever pass modifyBlock's checks?
- Is there any caching of ModelIndex for non-cube models in this chunk?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_ore.zig_chunk_0*
