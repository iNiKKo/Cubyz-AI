# [easy/codebase_src_entityComponent__template.zig] - Chunk 0

**Type:** api
**Keywords:** EntityComponentId, BinaryReader, BinaryWriter, ComponentSaveBehaviour, stub implementation, public API surface, template component, server struct, client struct, load hook, unload hook, save hook
**Symbols:** entityComponentID, entityComponentVersion, client.load, client.unload, client.init, client.deinit, client.clear, server.ExampleComponent.save, server.init, server.get, server.loadFromData, server.unload
**Concepts:** entity component template, client-only stubs, server-side component management, binary serialization hooks, component save behavior enumeration

## Summary
Defines the public API surface for a template entity component, exposing client-only stubs (load/unload/init/deinit/clear) and server-side functionality including an ExampleComponent struct with save/load/get methods.

## Explanation
The chunk declares several pub imports from main modules: Entity, ServerChunk, game.World, graphics.ZonElement, renderer, settings, utils.BinaryReader/BinaryWriter, vec types (Mat4f, Vec3d, Vec3f, Vec4f, Vec3i), heap.NeverFailingAllocator, blocks, items.ItemStack, random, and c. It then defines two top-level pub constants: entityComponentID (a main.entity.EntityComponentId) initialized to undefined, and entityComponentVersion set to 0. A client struct is declared with five public functions: load(entity, reader, version) returning main.entity.EntityComponentLoadError!void that ignores all arguments; unload(entity) void that also ignores its argument; init() void; deinit() void; and clear() void. A server struct follows with four declarations: a pub const ExampleComponent defined as an anonymous struct containing one public function save(self, writer, audience) returning main.entity.ComponentSaveBehaviour (which currently returns .save while ignoring all arguments); init() void; get(entity) returning ?ExampleComponent (currently returning null); and loadFromData(entity, reader, version) returning main.entity.EntityComponentLoadError!void. The server struct also includes an unload(entity) void function that ignores its argument.

## Related Questions
- What is the default value of entityComponentID in this template component?
- Which functions are declared inside the client struct for a template component?
- How does the server.ExampleComponent.save method indicate whether it wants to be saved?
- What return type does the server.get function use when retrieving an ExampleComponent?
- Are any of the stub implementations in this chunk actually performing operations or are they all no-ops?
- Which module provides the EntityComponentId type used by entityComponentID?
- Does the client.load function accept a version parameter and what does it do with it?
- What is the purpose of the server.ExampleComponent struct in this template component definition?

*Source: unknown | chunk_id: codebase_src_entityComponent__template.zig_chunk_0*
