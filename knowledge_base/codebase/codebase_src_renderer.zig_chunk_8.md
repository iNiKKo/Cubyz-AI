# [hard/codebase_src_renderer.zig] - Chunk 8

**Type:** implementation
**Keywords:** block placement, block breaking, inventory interaction, damage calculation, health update
**Symbols:** selectedBlockPos, lastSelectedBlockPos, currentSwingProgress, currentSwingTime, currentBlockProgress, updateBlockAndSendUpdate
**Concepts:** block placement, block breaking, player inventory interaction

## Summary
Handles block placement and breaking logic based on player interactions.

## Explanation
The code processes block placement and breaking logic based on player interactions. When placing a block, it checks if the selected item can be added to or replace the existing block, considering rotation modes and neighbor blocks. The `blocks.Block.mode` function determines how the block should be placed or modified. Specifically, it uses the `rotationMode` to adjust the block's orientation and considers neighboring blocks to ensure proper placement. For procedural items, the code calculates damage based on the tool's properties using the `getBlockDamage` method of the item. The damage is then subtracted from the block's resistance to determine how much health is left. If the block is broken completely (health reaches zero), it sends an update to the server. The `updateBlockAndSendUpdate` function handles sending block updates to the server, including the old and new block states. The code also manages animations during the block breaking process by updating the `currentBlockProgress` and removing or adding breaking animations as needed. Additionally, it checks conditions such as whether the player is in creative mode or if the block has fluid or air tags before allowing a block to be placed or broken.

## Code Example
```zig
pub fn breakBlock(inventory: main.items.Inventory.ClientInventory, slot: u32, deltaTime: f64) void {
		if (selectedBlockPos) |selectedPos| {
			const stack = inventory.getStack(slot);
			const isSelectionWand = stack.item == .baseItem and std.mem.eql(u8, stack.item.baseItem.id(), "cubyz:selection_wand");
			if (isSelectionWand) {
				game.Player.selectionPosition1 = selectedPos;
				main.network.protocols.genericUpdate.sendWorldEditPos(main.game.world.?.conn, .selectedPos1, selectedPos);
				return;
			}

			if (@reduce(.Or, lastSelectedBlockPos != selectedPos)) {
				mesh_storage.removeBreakingAnimation(lastSelectedBlockPos);
				currentSwingProgress = 0;
				currentSwingTime = 0;
				lastSelectedBlockPos = selectedPos;
				currentBlockProgress = 0;
			}
			const block = mesh_storage.getBlockFromRenderThread(selectedPos[0], selectedPos[1], selectedPos[2]) orelse return;
			const holdingTargetedBlock = stack.item == .baseItem and stack.item.baseItem.block() == block.typ;
			if ((block.hasTag(.fluid) or block.hasTag(.air)) and !holdingTargetedBlock) return;

			const relPos: Vec3f = @floatCast(lastPos - @as(Vec3d, @floatFromInt(selectedPos)));

			main.sync.client.mutex.lock();
			if (!game.Player.isCreative()) {
				var damage: f32 = main.game.Player.defaultBlockDamage;
				const isProceduralItem = stack.item == .proceduralItem;
				if (isProceduralItem) {
					damage = stack.item.proceduralItem.getBlockDamage(block);
				}
				damage -= block.blockResistance();
				if (damage > 0) {
					const swingTime = if (isProceduralItem and stack.item.proceduralItem.isEffectiveOn(block)) 1.0/stack.item.proceduralItem.getProperty(.swingSpeed) else 0.5;
					if (currentSwingTime > swingTime) {
						currentSwingProgress = 0;
						currentSwingTime = 0;
					}
					if (currentSwingTime == 0) {
						const swings = @ceil(block.blockHealth()/damage);
						const damagePerSwing = block.blockHealth()/swings;
						currentSwingTime = damagePerSwing/damage*swingTime;
					}
					currentSwingProgress += @floatCast(deltaTime);
					while (currentSwingProgress > currentSwingTime) {
						currentSwingProgress -= currentSwingTime;
						currentBlockProgress += damage*currentSwingTime/swingTime/block.blockHealth();
						if (currentBlockProgress > 0.9999) break;
						const swings = @ceil(block.blockHealth()/damage);
						const damagePerSwing = block.blockHealth()/swings;
						currentSwingTime = damagePerSwing/damage*swingTime;
					}
					if (currentBlockProgress < 0.9999) {
						mesh_storage.removeBreakingAnimation(lastSelectedBlockPos);
						if (currentBlockProgress != 0) {
							mesh_storage.addBreakingAnimation(lastSelectedBlockPos, currentBlockProgress);
						}
						main.sync.client.mutex.unlock();

						return;
					} else {
						currentSwingProgress = 0;
						mesh_storage.removeBreakingAnimation(lastSelectedBlockPos);
						currentBlockProgress = 0;
						currentSwingTime = 0;
					}
				} else {
					main.sync.client.mutex.unlock();
					return;
				}
			} else {
				mesh_storage.removeBreakingAnimation(lastSelectedBlockPos);
			}

			var newBlock = block;
			block.mode().onBlockBreaking(inventory.getStack(slot).item, relPos, lastDir, &newBlock);
			main.sync.client.mutex.unlock();

			if (newBlock != block) {
				updateBlockAndSendUpdate(inventory, slot, selectedPos, block, newBlock);
			}
		}
	}
```

## Related Questions
-  How does the code handle block placement when the player selects a block from their inventory?
-  What is the process for breaking blocks in the game engine?
-  How does the code calculate damage to a block based on the tool used?
-  What role does the `updateBlockAndSendUpdate` function play in the block interaction logic?
-  How does the code manage animations during the block breaking process?
-  What conditions are checked before allowing a block to be placed or broken?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_8*
