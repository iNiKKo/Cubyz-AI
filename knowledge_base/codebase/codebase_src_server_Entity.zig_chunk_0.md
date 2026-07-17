# [easy/codebase_src_server_Entity.zig] - Chunk 0

**Type:** api
**Keywords:** ZonElement, Base64 encoding, resource allocation, deinitialization, component handling
**Symbols:** Entity, Entity.pos, Entity.vel, Entity.rot, Entity.health, Entity.maxHealth, Entity.energy, Entity.maxEnergy, Entity.name, Entity.id, Entity.loadFrom, Entity.clone, Entity.save, Entity.deinit
**Concepts:** entity ECS, serialization, memory management

## Summary
This chunk defines the Entity struct and its methods for loading, cloning, saving, and deinitializing entities.

## Explanation
The Entity struct contains fields for position, velocity, rotation, health, energy, name, and ID. The `loadFrom` method initializes an entity from a ZonElement, handling optional fields and components. The `clone` method duplicates an entity, ensuring the new instance has its own allocated resources. The `save` method serializes the entity's state into a ZonElement, including components in Base64 format. The `deinit` method frees resources like the name string and removes components based on the side (server or client).

## Code Example
```zig
pub fn clone(self: *@This(), copy: *@This()) void {
	const originalID = copy.id;
	std.debug.assert(copy.name == null);
	copy.* = self.*;
	copy.name = if (self.name) |name| main.globalAllocator.dupe(u8, name) else null;
	copy.id = originalID;
}
```

## Related Questions
- What fields does the Entity struct contain?
- How does the `loadFrom` method initialize an entity?
- What is the purpose of the `clone` method in the Entity struct?
- How does the `save` method serialize the entity's state?
- What resources are freed by the `deinit` method?
- How are components handled during the loading and saving processes?

*Source: unknown | chunk_id: codebase_src_server_Entity.zig_chunk_0*
