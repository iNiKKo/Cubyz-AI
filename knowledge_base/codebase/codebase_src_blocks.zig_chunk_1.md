# [hard/codebase_src_blocks.zig] - Chunk 1

**Type:** implementation
**Keywords:** array management, ZonElement parsing, default value setting, global state update, item drop configuration
**Symbols:** _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _onTick, _onTouch, _blockEntity, reverseIndices, size, ores, register, loadBlockDrop, registerBlockDrop, registerLodReplacement
**Concepts:** block properties, block registration, item drops, level-of-detail replacements

## Summary
This chunk manages block registration and properties in the Cubyz voxel engine, including friction, bounciness, density, and other physical attributes.

## Explanation
The chunk defines several arrays to store various properties of blocks, such as friction, bounciness, density, and terminal velocity. It also includes a string hash map for reverse indexing block IDs. The `register` function handles the registration of new blocks by parsing ZonElement data, setting default values if necessary, and updating the global state with the new block's properties. The `loadBlockDrop` function parses drop configurations from ZonElement data, creating a list of possible drops for each block. The `registerBlockDrop` and `registerLodReplacement` functions are helper methods to register block-specific behaviors like item drops and level-of-detail replacements.

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
