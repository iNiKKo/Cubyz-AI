# [hard/codebase_src_blocks.zig] - Chunk 1

**Type:** implementation
**Keywords:** array management, ZonElement parsing, default value setting, global state update, item drop configuration
**Symbols:** _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _onTick, _onTouch, _blockEntity, reverseIndices, size, ores, register, loadBlockDrop, registerBlockDrop, registerLodReplacement
**Concepts:** block properties, block registration, item drops, level-of-detail replacements

## Summary
This chunk manages block registration and properties in the Cubyz voxel engine, including friction, bounciness, density, and other physical attributes.

## Explanation
This chunk manages block registration and properties in the Cubyz voxel engine, including friction, bounciness, density, and other physical attributes. It defines several arrays to store various properties of blocks, such as `_friction`, `_bounciness`, `_density`, and `_terminalVelocity`. Each array has a size of `maxBlockCount` and is initialized with undefined values. The chunk also includes a string hash map called `reverseIndices` for reverse indexing block IDs.

The `register` function handles the registration of new blocks by parsing ZonElement data, setting default values if necessary, and updating the global state with the new block's properties. For example, it sets `_friction` to 20, `_bounciness` to 0.0, `_density` to `main.physics.airDensity`, `_terminalVelocity` to 90, and `_mobility` to 1.0 if these values are not provided in the ZonElement data.

The `loadBlockDrop` function parses drop configurations from ZonElement data, creating a list of possible drops for each block. Each drop configuration includes items that can be dropped, their amounts, and conditions under which they can be dropped (e.g., allowed or forbidden tool tags). The function returns an array of `BlockDrop` structures.

The `registerBlockDrop` function registers the item drops for a specific block type by calling `loadBlockDrop`. The `registerLodReplacement` function registers level-of-detail replacements for a specific block type, either using a specified replacement or defaulting to the original block type if no replacement is provided.

## Code Example
```zig
fn registerBlockDrop(typ: u16, zon: ZonElement) void {
	_blockDrops[typ] = loadBlockDrop(_id[typ], zon);
}
```

## Related Questions
- What is the purpose of the `_friction` array?
- How does the `register` function handle default values for block properties?
- What information does the `loadBlockDrop` function extract from ZonElement data?
- What is the role of the `reverseIndices` hash map in this chunk?
- How are item drops configured and stored for each block?
- What does the `registerLodReplacement` function do?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_1*
