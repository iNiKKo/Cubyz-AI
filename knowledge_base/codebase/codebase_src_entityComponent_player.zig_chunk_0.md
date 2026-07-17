# [easy/codebase_src_entityComponent_player.zig] - Chunk 0

**Type:** api
**Keywords:** SparseSet, BinaryReader, BinaryWriter, EntityComponentId, init, deinit, load, unload, get, put, version check, allocator
**Symbols:** entityComponentID, entityComponentVersion, client, server, client.Component, client.components, client.init, client.deinit, client.clear, client.load, client.unload, client.get, server.Component, server.save, server.components, server.init, server.deinit, server.loadFromData, server.load, server.unload, server.put, server.get
**Concepts:** sparse set storage, client server split, binary serialization, component lifecycle, entity component system, versioned loading, allocator management, public API surface

## Summary
Defines client-only and server-only sparse-set-backed component storage for player entities, exposing init/deinit/clear/load/unload/get/put operations with binary serialization via BinaryReader/BinaryWriter.

## Explanation
The chunk declares a top-level pub var entityComponentID (EntityComponentId) and a const entityComponentVersion = 0. It then defines two separate structs: client and server, each containing a Component struct and methods operating on a SparseSet(Component, Entity). The client struct has a private components field of type main.utils.SparseSet(Component, Entity), initialized to an empty set via .{}. Its init() is an empty void function; deinit() calls components.deinit(main.globalAllocator); clear() calls components.clear(). load(entity: Entity, reader: *utils.BinaryReader, version: u32) checks that version == 0 else returns error.InvalidComponentVersion; it reads a varInt u32 from the reader (catching UnreadableComponentData), then retrieves or adds an entry in components via get orelse add(main.globalAllocator, entity), and assigns Component{.playerIndex = playerIndex}. unload(entity: Entity) calls components.remove(entity) with catch {} to suppress errors. get(entity: Entity) returns components.get(entity). The server struct has a pub const Component with fields playerIndex: u32 and a save(self: Component, writer: *utils.BinaryWriter, audience: main.entity.AudienceInfo) method that writes the varInt and returns .discard for disk audiences else .save. Its components field is declared as undefined (var). init() sets components = .{}; deinit() calls components.deinit(main.globalAllocator); loadFromData(entity: Entity, reader: *utils.BinaryReader, version: u32) validates version == 0, reads playerIndex, then delegates to load(entity, playerIndex). load(entity: Entity, playerIndex: u32) uses put(entity, Component{.playerIndex = playerIndex}). unload(entity: Entity) calls components.remove(entity) catch {}. put(entity: Entity, renderComponent: Component) retrieves or adds an entry via get orelse add(main.globalAllocator, entity) and assigns ptr.* = renderComponent. get(entity: Entity) returns components.get(entity). Both client and server rely on main.utils.SparseSet for storage; the chunk does not define SparseSet itself but uses it as a type parameter. All functions are pub (or pub const where appropriate), making them part of the public API surface.

## Related Questions
- What is the default version for player components in this chunk?
- How does client.load handle an invalid component version?
- Which allocator is used when adding a new component entry to the sparse set?
- Does server.save write data differently depending on the audience parameter?
- What error is returned if reading a varInt from the binary reader fails in loadFromData?
- How does client.clear differ from client.deinit in terms of side effects?
- Can server.put be called with an arbitrary Component value or must it match the stored type?
- Is there any synchronization mechanism mentioned for concurrent access to components?
- What happens if get is called on a non-existent entity in either client or server?
- Does this chunk define its own SparseSet implementation or import it from another module?

*Source: unknown | chunk_id: codebase_src_entityComponent_player.zig_chunk_0*
