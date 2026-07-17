# [hard/codebase_src_network_protocols.zig] - Chunk 3

**Type:** networking
**Keywords:** network protocols, mesh generation, player position, entity position, binary serialization, mutex locking
**Symbols:** MeshGenerationTask, MeshGenerationTask.isStillNeeded, MeshGenerationTask.run, MeshGenerationTask.clean, clientReceive, sendChunkOverTheNetwork, sendChunk, playerPosition, playerPosition.id, serverReceive, lastPositionSent, send, entityPosition, entityPosition.id, type_entity, type_item, Type, noVelocityEntity, f16VelocityEntity, f32VelocityEntity, noVelocityItem, f16VelocityItem, f32VelocityItem
**Concepts:** networking, chunk meshing, player position updates, entity position updates

## Summary
This chunk defines network protocols for mesh generation tasks and player/entity position updates.

## Explanation
The chunk contains functions for handling mesh generation tasks, including checking if a task is still needed, running the task to generate lighting data, and cleaning up resources. It also includes functions for sending and receiving chunk data over the network. The `playerPosition` struct handles sending and receiving player position updates, ensuring they are sent no more than once every 50 milliseconds. The `entityPosition` struct manages sending and receiving entity and item position updates, including handling different velocity types.

## Code Example
```zig
pub fn isStillNeeded(self: *MeshGenerationTask) bool {
	if (main.game.world == null or main.game.world.?.paused) return false;
	const distanceSqr = self.pos.getMinDistanceSquared(@trunc(game.Player.getPosBlocking())); // TODO: This is called in loop, find a way to do this without calling the mutex every time.
	var maxRenderDistance = settings.renderDistance*chunk.chunkSize*self.pos.voxelSize;
	maxRenderDistance += 2*self.pos.voxelSize*chunk.chunkSize;
	return distanceSqr < maxRenderDistance*maxRenderDistance;
}
```

## Related Questions
- What is the purpose of the `isStillNeeded` function in the `MeshGenerationTask` struct?
- How does the `run` method handle errors when loading chunk mesh data?
- What steps are taken to clean up resources in the `clean` method of `MeshGenerationTask`?
- How often is player position data sent over the network according to the `playerPosition` struct?
- What types of entity and item velocity data can be handled by the `entityPosition` struct?
- How does the `sendChunkOverTheNetwork` function ensure thread safety when accessing chunk data?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_3*
