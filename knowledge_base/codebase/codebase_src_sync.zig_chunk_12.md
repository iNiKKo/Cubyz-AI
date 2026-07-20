# [hard/codebase_src_sync.zig] - Chunk 12

**Type:** api
**Keywords:** serialization, deserialization, inventory operations, crafting recipes, block changes
**Symbols:** CraftFrom, CraftProceduralItem, Clear, UpdateBlock, CraftFrom.destinations, CraftFrom.sources, CraftFrom.recipe, CraftProceduralItem.destinations, CraftProceduralItem.craftingGrid, Clear.inv, UpdateBlock.source, UpdateBlock.pos, UpdateBlock.dropLocation, UpdateBlock.oldBlock, UpdateBlock.newBlock, UpdateBlock.BlockDropLocation, UpdateBlock.BlockDropLocation.normalDir, UpdateBlock.BlockDropLocation.min, UpdateBlock.BlockDropLocation.max
**Concepts:** crafting system, inventory management, serialization, deserialization, block updates

## Summary
This chunk defines several structs related to crafting and inventory management, including serialization and deserialization methods.

## Explanation
This chunk defines several structs related to crafting and inventory management, including detailed serialization and deserialization methods. The `CraftFrom` struct handles crafting items from sources to destinations based on a recipe. It has fields for `destinations`, `sources`, and `recipe`. The `serialize` method writes these fields to a binary writer by calling `self.destinations.toBytes(writer)`, `self.sources.toBytes(writer)`, and `self.recipe.toBytes(writer)`. The `deserialize` method reads them back from a binary reader by creating instances of `Inventory.Inventories` for `destinations` and `sources`, and `main.items.Recipe` for `recipe`. The `CraftProceduralItem` struct manages procedural item crafting, ensuring the crafting grid's contents are used to create new items. It has fields for `destinations` and `craftingGrid`. The `serialize` method writes these fields to a binary writer by calling `self.destinations.toBytes(writer)` and `writer.writeEnum(InventoryId, self.craftingGrid.id)`. The `deserialize` method reads them back from a binary reader by creating an instance of `Inventory.Inventories` for `destinations` and retrieving the `craftingGrid` using `reader.readEnum(InventoryId)`. The `Clear` struct clears all items from an inventory. It has a field for `inv`. The `serialize` method writes this field to a binary writer by calling `writer.writeEnum(InventoryId, self.inv.id)`. The `deserialize` method reads it back from a binary reader by retrieving the inventory using `reader.readEnum(InventoryId)`. The `UpdateBlock` struct updates block states and handles dropping items when blocks change. It has fields for `source`, `pos`, `dropLocation`, `oldBlock`, and `newBlock`. The `serialize` method writes these fields to a binary writer by calling `self.source.toBytes(writer)`, `writer.writeVec3i(self.pos)`, `self.dropLocation.serialize(writer)`, `writer.writeEnum(Block, self.oldBlock)`, and `writer.writeEnum(Block, self.newBlock)`. The `deserialize` method reads them back from a binary reader by creating an instance of `InventoryAndSlot` for `source`, reading `pos` using `reader.readVec3i()`, deserializing `dropLocation` using `BlockDropLocation.deserialize(reader)`, and retrieving `oldBlock` and `newBlock` using `reader.readEnum(Block)`.

## Code Example
```zig
fn run(self: CraftProceduralItem, ctx: Context) error{serverFailure}!void {
			const proceduralItem = Item{.proceduralItem = main.items.ProceduralItem.initFromInventory(self.craftingGrid) orelse return};
			if (self.destinations.canHold(.{.item = proceduralItem, .amount = 1}) != .yes) {
				proceduralItem.deinit();
				return;
			}
			ctx.cmd.removeProceduralItemCraftingIngredients(main.globalAllocator, self.craftingGrid, ctx.side);
			_ = self.destinations.putItemsInto(ctx, 1, .{.create = proceduralItem});
		}
```

## Related Questions
- How does the `CraftFrom` struct handle crafting items?
- What is the purpose of the `serialize` method in `CraftProceduralItem`?
- How does the `Clear` struct clear items from an inventory?
- What are the steps involved in updating a block with the `UpdateBlock` struct?
- How does the `deserialize` method handle errors in `CraftFrom`?
- What is the role of the `BlockDropLocation` struct in item dropping?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_12*
