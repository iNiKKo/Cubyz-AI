# [easy/codebase_src_client_Entity.zig] - Chunk 0

**Type:** implementation
**Keywords:** entity, initialization, deinitialization, position update, interpolation, render position, name formatting
**Symbols:** Entity, Entity.interpolatedValues, Entity._interpolationPos, Entity._interpolationVel, Entity.width, Entity.height, Entity.pos, Entity.rot, Entity.id, Entity.name, Entity.init, Entity.deinit, Entity.getRenderPosition, Entity.updatePosition, Entity.update, Entity.format, Entity.formatWithPlayerIndex
**Concepts:** entity ECS, interpolation, rendering, formatting

## Summary
This chunk defines the Entity struct and its methods for initialization, deinitialization, position updates, rendering, and formatting.

## Explanation
The Entity struct represents an entity in the game with properties like position, rotation, dimensions, and components, using a 6-value `GenericInterpolation` (position xyz + rotation xyz) for smooth movement. The `init` method reads `id` (default `std.math.maxInt(u32)` if missing), `width`/`height` (default `1` each), and `name` (default `""`) from a ZonElement, initializes interpolation from the current pos/rot with zero velocity, and loads any `components` (base64-encoded) via `main.entity.loadComponentsFromBase64`. `deinit` removes all of the entity's components and frees its `name`. `updatePosition`/`update` feed new position/velocity samples into the interpolation and copy the interpolated output back into `pos`/`rot`. `format` prints just the entity's name, UNLESS `main.settings.showPlayerIndexWithName` is enabled AND the entity has a `cubyz:player` component, in which case it calls `formatWithPlayerIndex`, which prints `"{name}@{playerIndex}"`.

## Code Example
```zig
pub fn deinit(self: @This(), allocator: NeverFailingAllocator) void {
	main.entity.client.removeAllComponents(self.id);
	allocator.free(self.name);
}
```

## Related Questions
- What is the purpose of the Entity struct?
- How does the init method initialize an Entity from a ZonElement?
- What resources are freed during the deinit method?
- How is the position of an entity updated over time?
- What methods are used to format the name of an entity?
- How does the Entity handle player index formatting if applicable?

*Source: unknown | chunk_id: codebase_src_client_Entity.zig_chunk_0*
