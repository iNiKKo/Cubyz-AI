# [hard/codebase_src_sync.zig] - Chunk 13

**Type:** implementation
**Keywords:** block change, inventory update, random item drop, binary serialization, server-client synchronization
**Symbols:** UpdateBlock, UpdateBlock.source, UpdateBlock.pos, UpdateBlock.dropLocation, UpdateBlock.oldBlock, UpdateBlock.newBlock, UpdateBlock.run, UpdateBlock.serialize, UpdateBlock.deserialize
**Concepts:** block update, inventory management, item drops

## Summary
The chunk implements block update logic, including inventory changes and item drops.

## Explanation
This chunk defines the `UpdateBlock` struct with methods for running block updates, serializing, and deserializing. The `run` method checks if a block can be changed based on game mode and inventory conditions, then updates the server world and informs clients of changes. It also handles item drops when blocks are broken by calculating the number of drops based on the old and new block types and randomly determining whether each drop occurs based on its chance. The `dropLocation` field is used to determine the position where items should be dropped, including a random offset to simulate natural dispersion. Serialization and deserialization methods ensure that block update data can be written to and read from binary streams.

## Code Example
```zig
fn run(self: UpdateBlock, ctx: Context) error{serverFailure}!void {
			const stack = self.source.ref();

			var shouldDropSourceBlockOnSuccess: bool = true;
			const costOfChange = if (ctx.gamemode != .creative) self.oldBlock.canBeChangedInto(self.newBlock, stack.*, &shouldDropSourceBlockOnSuccess) else .yes;

			// Check if we can change it:
			if (!switch (costOfChange) {
				.no => false,
				.yes => true,
				.yes_costsDurability => stack.item == .proceduralItem,
				.yes_costsItems => |amount| stack.amount >= amount,
			}) {
				if (ctx.side == .server) {
					// Inform the client of the actual block:
					var writer = BinaryWriter.init(main.stackAllocator);
					defer writer.deinit();

					const actualBlock = main.server.world.?.getBlockAndBlockEntityData(self.pos[0], self.pos[1], self.pos[2], &writer) orelse return;
					main.network.protocols.blockUpdate.send(ctx.user.?.conn, &.{.init(self.pos, actualBlock, writer.data.items)});
				}
				return;
			}

			if (ctx.side == .server) {
				if (main.server.world.?.cmpxchgBlock(self.pos[0], self.pos[1], self.pos[2], self.oldBlock, self.newBlock) != null) {
					// Inform the client of the actual block:
					var writer = BinaryWriter.init(main.stackAllocator);
					defer writer.deinit();

					const actualBlock = main.server.world.?.getBlockAndBlockEntityData(self.pos[0], self.pos[1], self.pos[2], &writer) orelse return;
					main.network.protocols.blockUpdate.send(ctx.user.?.conn, &.{.init(self.pos, actualBlock, writer.data.items)});
					return error.serverFailure;
				}
			}

			// Apply inventory changes:
			const handItem = self.source.inv.getItem(self.source.slot); // State should be stored before procedural item breaks
			switch (costOfChange) {
				.no => unreachable,
				.yes => {},
				.yes_costsDurability => |durability| {
					ctx.execute(.{.useDurability = .{
						.source = self.source,
						.durability = durability,
					}});
				},
				.yes_costsItems => |amount| {
					ctx.execute(.{.delete = .{
						.source = self.source,
						.amount = amount,
					}});
				},
			}
			if (ctx.side == .server and ctx.gamemode != .creative and shouldDropSourceBlockOnSuccess) {
				const dropAmount = self.oldBlock.mode().itemDropsOnChange(self.oldBlock, self.newBlock);
				for (0..dropAmount) |_| {
					for (self.oldBlock.blockDrops()) |drop| {
						if (!drop.isDroppedWhenBrokenWithItem(handItem)) continue;

						if (drop.chance == 1 or main.random.nextFloat(&main.seed) < drop.chance) {
							self.dropLocation.drop(self.pos, self.newBlock, drop);
						}
					}
				}
			}
		}
```

## Related Questions
- What is the purpose of the `run` method in the `UpdateBlock` struct?
- How does the `UpdateBlock` struct handle item drops when a block is broken?
- What conditions are checked before updating a block on the server?
- How is the `UpdateBlock` struct serialized and deserialized?
- What role does the `dropLocation` field play in the `UpdateBlock` struct?
- How does the `run` method inform clients of actual block changes?

*Source: unknown | chunk_id: codebase_src_sync.zig_chunk_13*
