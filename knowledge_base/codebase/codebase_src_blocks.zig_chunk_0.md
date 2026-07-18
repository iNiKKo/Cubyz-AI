# [hard/codebase_src_blocks.zig] - Chunk 0

**Type:** implementation
**Keywords:** arrays, structs, union, functions, conditions, parameters
**Symbols:** maxBlockCount, BlockDrop, Ore, SelectionCapabilities, _transparent, _collide, _id, _blockHealth, _blockResistance, _replaceable, _selectionCapabilities, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, _light, _absorption, _onInteract, _onBreak, _onUpdate, _mode, _modeData, _lodReplacement, _opaqueVariant
**Concepts:** block properties, ore generation, selection capabilities

## Summary
Defines block properties and behaviors in the Cubyz engine, including transparency, collision, health, and interactions.

## Explanation
This chunk defines various arrays that store properties for different blocks in the Cubyz engine. Each array corresponds to a specific property such as transparency, collision, health, and more. The `BlockDrop` struct specifies what items are dropped when a block is broken, including conditions based on the tool used. The `Ore` struct describes ore generation parameters like size, density, and depth. The `SelectionCapabilities` union defines how blocks can be selected by different tools or items. The chunk also includes functions for loading selection capabilities from Zon elements and checking if a block can be selected with a given item.

## Code Example
```zig
pub fn isDroppedWhenBrokenWithItem(self: BlockDrop, item: Item) bool {
	if (item != .proceduralItem) return self.allowedToolTags == null;

	const proceduralItem = item.proceduralItem;
	for (self.forbiddenToolTags) |tag| if (proceduralItem.hasTag(tag)) return false;
	if (self.allowedToolTags) |tags| {
		for (tags) |tag| if (proceduralItem.hasTag(tag)) return true;
		return false;
	}

	return true;
}
```

## Related Questions
- What is the maximum number of blocks defined in the Cubyz engine?
- How does the `BlockDrop` struct determine if a block should drop items when broken?
- What parameters define ore generation in the Cubyz engine?
- How are selection capabilities loaded from Zon elements?
- What conditions must be met for a block to be selected by a specific item?
- What properties are stored in the `_transparent` array?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_0*
