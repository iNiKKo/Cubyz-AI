# [hard/codebase_src_server_world.zig] - Chunk 10

**Type:** implementation
**Keywords:** block update, reference counting, mutex locking, user notification, chunk queueing, region file update
**Symbols:** ServerWorld, ServerWorld.updateBlock, ServerWorld.cmpxchgBlock, ServerWorld.triggerNeighborBlockUpdates, ServerWorld.queueChunkUpdateAndDecreaseRefCount, ServerWorld.queueRegionFileUpdateAndDecreaseRefCount
**Concepts:** block updates, neighbor checks, user notifications, chunk management, region file updates

## Summary
Handles block updates in the server world, including neighbor checks and user notifications.

## Explanation
This chunk contains methods for updating blocks in a server world. The `updateBlock` method is the primary entry point, which calls `cmpxchgBlock` to change the block using atomic compare-and-swap operations (`_ = self.cmpxchgBlock(wx, wy, wz, null, newBlock);`). If the new block depends on neighbors or affects neighboring blocks, it updates those as well and notifies connected users of the changes. Specifically, if the neighbor block's mode depends on neighbors, it updates the neighbor block's data (`if (neighborBlock.mode().dependsOnNeighbors and neighborBlock.mode().updateData(&neighborBlock, neighbor.reverse(), newBlock))`) and sends a block update notification to all connected users with the exact position, new block, and block entity data (`main.network.protocols.blockUpdate.send(user.conn, &.{.{.pos = .{wx +% neighbor.relX(), wy +% neighbor.relY(), wz +% neighbor.relZ()}, .newBlock = neighborBlock, .blockEntityData = &.{}}});`). The `cmpxchgBlock` method uses atomic compare-and-swap operations to safely change the block in the chunk. If an error occurs while removing entity data during a block update, it logs the error with details such as the error name, position, and block ID (`std.log.err(

## Code Example
```zig
pub fn triggerNeighborBlockUpdates(self: *ServerWorld, wx: i32, wy: i32, wz: i32) void {
	for (chunk.Neighbor.iterable) |value| {
		const pos = Vec3i{
			wx + value.relX(),
			wy + value.relY(),
			wz + value.relZ(),
		};

		var ch = self.getSimulationChunkAndIncreaseRefCount(pos[0], pos[1], pos[2]) orelse continue;
		defer ch.decreaseRefCount();

		ch.blockUpdateSystem.add(.{
			.x = @truncate(@as(u32, @bitCast(pos[0]))),
			.y = @truncate(@as(u32, @bitCast(pos[1]))),
			.z = @truncate(@as(u32, @bitCast(pos[2]))),
		});
	}
}
```

## Related Questions
- How does the `updateBlock` method handle block updates?
- What is the purpose of the `triggerNeighborBlockUpdates` function?
- How are user notifications managed when a block is updated?
- What role do mutex locks play in this chunk's logic?
- How are chunks and region files queued for updates?
- What happens if an error occurs while removing entity data during a block update?

*Source: unknown | chunk_id: codebase_src_server_world.zig_chunk_10*
