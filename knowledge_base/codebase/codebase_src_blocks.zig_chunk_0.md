# [hard/codebase_src_blocks.zig] - Chunk 0

**Type:** implementation
**Keywords:** arrays, structs, union, functions, conditions, parameters
**Symbols:** maxBlockCount, BlockDrop, Ore, SelectionCapabilities, _transparent, _collide, _id, _blockHealth, _blockResistance, _replaceable, _selectionCapabilities, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, _light, _absorption, _onInteract, _onBreak, _onUpdate, _mode, _modeData, _lodReplacement, _opaqueVariant
**Concepts:** block properties, ore generation, selection capabilities

## Summary
Defines block properties and behaviors in the Cubyz engine, including transparency, collision, health, and interactions.

## Explanation
This chunk defines various arrays that store properties for different blocks in the Cubyz engine. Each array corresponds to a specific property such as transparency, collision, health, and more. The `BlockDrop` struct specifies what items are dropped when a block is broken, including conditions based on the tool used. For example, if an item is not a procedural item, it will drop items only if there are no allowed tool tags specified. If the item is a procedural item, it checks against forbidden and allowed tool tags to determine if the block should drop items.

The `Ore` struct describes ore generation parameters like size, density, and depth. For instance, an ore with a size of 5.0 blocks, a density of 2.0, and a maximum height of 64 will generate veins in chunks according to these parameters. The `SelectionCapabilities` union defines how blocks can be selected by different tools or items. It includes options like always allowing selection, custom tool effectiveness checks, and specific item ID checks.

The chunk also includes functions for loading selection capabilities from Zon elements and checking if a block can be selected with a given item. For example, the `allowsSelectionByItem` function in the `SelectionCapabilities` union checks if an item has a specific tag or matches a block type to determine if it can select the block.

Overall, this chunk provides a comprehensive set of properties and behaviors for blocks in the Cubyz engine, ensuring that each block can have unique interactions and generation characteristics.

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
