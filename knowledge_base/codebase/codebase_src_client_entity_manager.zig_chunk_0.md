# [easy/codebase_src_client_entity_manager.zig] - Chunk 0

**Type:** implementation
**Keywords:** mutex locking, virtual list, thread safety, entity management, client entity manager
**Symbols:** entities, idMapping, mutex
**Concepts:** entity management, thread safety, virtual list

## Summary
Client entity manager for managing entities in the game.

## Explanation
Client entity manager for managing entities in the game. Manages client-side entities with functions to add, get, remove, and update them using a mutex for thread safety and a virtual list to store entities efficiently. The `entities` variable is a `VirtualList` of type `main.client.Entity`, and `idMapping` is a `ListManaged` that maps entity IDs to indices in the `entities` list. Initialization involves setting up these data structures, while deinitialization clears them and releases resources. Mutex locking ensures thread safety during operations such as adding entities, getting entities by ID, removing entities, updating positions based on server data, and handling time differences for updates.

The `addEntity` function initializes an entity from ZonElement data, the `getEntity` function retrieves an entity by its ID, and the `removeEntity` function removes an entity and updates the `idMapping`. The `update` function calculates the current time based on server timestamps and updates each entity's state. The `serverUpdate` function processes incoming entity data from the server to update positions. Specifically, it iterates over `entityData`, which contains position (`pos`) and rotation (`rot`) data for each entity. For each entity, it updates its position and velocity using the provided data.

During entity removal, the `removeEntity` function first checks if the entity ID is within the bounds of `idMapping`. If so, it deinitializes the entity, removes it from the `entities` list, and updates the `idMapping` to reflect the change. The `timeDifference` variable tracks time differences between server timestamps, which are used to adjust the current time for entity updates. The `lastTime` variable stores the last processed time to ensure smooth interpolation of entity positions over time.

## Code Example
```zig
pub fn update() void {
	mutex.lock();
	defer mutex.unlock();

	var time: i16 = @truncate(main.timestamp().toMilliseconds() -% settings.entityLookback);
	time -%= timeDifference.difference.load(.monotonic);
	for (entities.items()) |*ent| {
		ent.update(time, lastTime);
	}
	lastTime = time;
}
```

## Related Questions
- What is the purpose of the mutex in the entity manager?
- How are entities added to the entity manager?
- What happens when an entity is removed from the entity manager?
- How does the entity manager handle updates for server-sent entity data?
- What is the role of the `idMapping` list in the entity manager?
- How is the `entities` virtual list managed?
- What is the difference between update() and serverUpdate() functions?
- What are the steps involved in updating an entity's position based on server data?
- How does the entity manager handle entity deletion when a client disconnects?
- What is the purpose of the timeDifference variable in the entity manager?
- How is the lastTime variable used in the entity manager?

*Source: unknown | chunk_id: codebase_src_client_entity_manager.zig_chunk_0*
