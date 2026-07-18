# [easy/codebase_src_entityComponent_player.zig] - Chunk 0

**Type:** implementation
**Keywords:** entity component, player index, binary reader, sparse set, component save behaviour
**Symbols:** entityComponentID, entityComponentVersion, client, server, Entity, game, graphics, c, ZonElement, renderer, settings, utils, vec, Mat4f, Vec3d, Vec3f, Vec4f, NeverFailingAllocator, BinaryReader
**Concepts:** client-only stuff, server-only stuff

## Summary
Player component implementation

## Explanation
This chunk defines the player component for both client and server. It includes initialization, deinitialization, clearing, loading, unloading, getting, and setting methods.

## Code Example
```zig
pub fn load(entity: Entity, reader: *utils.BinaryReader, version: u32) main.entity.EntityComponentLoadError!void {
		if (version != 0) return error.InvalidComponentVersion;
		const playerIndex = reader.readVarInt(u32) catch return error.UnreadableComponentData;

		const ptr = components.get(entity) orelse components.add(main.globalAllocator, entity);
		ptr.* = Component{
			.playerIndex = playerIndex,
		};
	}
```

## Related Questions
- What is the purpose of the `client` and `server` structs in this chunk?
- How are components managed for entities in both client and server contexts?
- What is the role of the `load` function in the `client` struct?
- What is the difference between `save` and `discard` in the `ComponentSaveBehaviour` enum?
- How are components added to the `components` set in the `server` struct?
- What is the purpose of the `put` function in the `server` struct?
- How does the `loadFromData` function differ from the `load` function in the `server` struct?
- What is the role of the `get` function in both client and server structs?
- What is the purpose of the `clear` function in the `client` struct?
- What is the difference between the `init` and `deinit` functions in the `client` and `server` structs?
- How are components removed from the `components` set in the `server` struct?
- What is the purpose of the `entityComponentID` variable?

*Source: unknown | chunk_id: codebase_src_entityComponent_player.zig_chunk_0*
