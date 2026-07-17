# [hard/codebase_src_itemdrop.zig] - Chunk 3

**Type:** implementation
**Keywords:** physics calculation, interpolation, rendering pipeline, entity collision, bobbing animation
**Symbols:** ItemDropManager, ItemDropManager.size, ItemDropManager.indices, ItemDropManager.list, ItemDropManager.init, ItemDropManager.deinit, ItemDropManager.processChanges, ItemDropManager.directRemove, ClientItemDropManager, ClientItemDropManager.maxf64Capacity, ClientItemDropManager.super, ClientItemDropManager.lastTime, ClientItemDropManager.timeDifference, ClientItemDropManager.interpolation, ClientItemDropManager.instance, ClientItemDropManager.mutex, ClientItemDropManager.init, ClientItemDropManager.deinit, ClientItemDropManager.readPosition, ClientItemDropManager.updateInterpolationData, ClientItemDropManager.clientSideInternalAdd, ClientItemDropManager.remove, ClientItemDropManager.loadFrom, ClientItemDropManager.addFromZon, ItemDisplayManager, ItemDisplayManager.showItem, ItemDisplayManager.cameraFollow, ItemDisplayManager.cameraFollowVel, ItemDisplayManager.damping, ItemDisplayManager.update, ItemDropRenderer, ItemDropRenderer.itemPipeline, ItemDropRenderer.itemUniforms
**Concepts:** item drop physics, client-side interpolation, item rendering, entity pickup detection

## Summary
Handles item drop physics, client-side interpolation, and rendering.

## Explanation
The chunk defines several structs related to item drops in the game. `ItemDropManager` manages server-side item drops, including calculating motion and checking for entity pickups. `ClientItemDropManager` handles client-side interpolation of item positions and velocities. `ItemDisplayManager` updates the display of items, including bobbing animations. `ItemDropRenderer` is responsible for rendering item drops using a graphics pipeline.

## Code Example
```zig
pub fn checkEntity(self: *ItemDropManager, user: *main.server.User) void {
	var ii: u32 = 0;
	while (ii < self.size) {
		const i = self.indices[ii];
		if (self.list.items(.pickupCooldown)[i] > 0) {
			ii += 1;
			continue;
		}
		const hitbox = main.game.Player.outerBoundingBox;
		const min = user.player().pos + hitbox.min;
		const max = user.player().pos + hitbox.max;
		const itemPos = self.list.items(.pos)[i];
		const dist = @max(min - itemPos, itemPos - max);
		if (@reduce(.Max, dist) < radius + pickupRange) {
			const itemStack = &self.list.items(.itemStack)[i];
			main.items.Inventory.server.tryCollectingToPlayerInventory(user, itemStack);
			if (itemStack.amount == 0) {
				self.directRemove(i);
				continue;
			}
		}
		ii += 1;
	}
}
```

## Related Questions
- What is the purpose of the `checkEntity` function in `ItemDropManager`?
- How does `ClientItemDropManager` handle item position interpolation?
- What role does `ItemDisplayManager` play in the game's rendering pipeline?
- How are item drops managed on the server side according to `ItemDropManager`?
- What is the significance of the `mutex` in `ClientItemDropManager`?
- How does `ItemDropRenderer` initialize its graphics pipeline?

*Source: unknown | chunk_id: codebase_src_itemdrop.zig_chunk_3*
