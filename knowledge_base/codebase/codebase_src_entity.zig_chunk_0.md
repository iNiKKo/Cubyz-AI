# [medium/codebase_src_entity.zig] - Chunk 0

**Type:** api
**Keywords:** EntityComponentVTable, components list, systems list, entity enum, noValue sentinel, binary reader errors, client server structs, init deinit clear render
**Symbols:** components, systems, EntityNetworkData, EntityComponentLoadError, Entity, EntityComponentId, EntityComponentVTable, componentList, client, server
**Concepts:** entity component system architecture, vtable dispatch pattern, network replication data structures, error union handling, inline iteration over type declarations

## Summary
This chunk defines the entity system's public API surface: it declares component and system lists, an Entity enum with a sentinel noValue, an EntityNetworkData struct for replication, error sets for loading/unloading components, a vtable type for component callbacks, and client/server structs exposing init/deinit/clear/render methods that iterate over systems and components via inline loops.

## Explanation
The chunk imports std and main, re-exports vec types (Mat4f, Vec3d, Vec3f, Vec4f), then declares pub const components and pub const systems as @import(...) from _list.zig files. It defines EntityNetworkData with fields id, pos, vel, rot for network replication. EntityComponentLoadError is an error union containing DecodingBase64, UnreadableId, UnreadableVersion, UnreadableComponentData, UnknownComponentId, InvalidComponentVersion. Entity is a u32 enum with noValue set to std.math.maxInt(u32) and a trailing underscore variant for valid values. EntityComponentId is an alias for u32. EntityComponentVTable is a struct containing four function pointers: serverLoad, clientLoad (both returning EntityComponentLoadError!void), serverUnload, clientUnload (returning void). A global var componentList holds []?EntityComponentVTable initialized to undefined. initComponents() builds tmpComponentList from @typeInfo(components).@

## Related Questions
- What is the maximum Entity value defined in this chunk and how is it represented?
- Which error variants are included in EntityComponentLoadError for component loading failures?
- How does the vtable type define server-side versus client-side load callbacks?
- Where is the global componentList variable declared and what is its initial state?
- What fields does EntityNetworkData contain for replicating entity state over the network?
- Which pub const imports are used to expose components and systems lists from other files?
- How do initComponents() and deinitComponents() manage the lifecycle of component vtables?
- What inline loop pattern is used to iterate over @typeInfo(components).@

*Source: unknown | chunk_id: codebase_src_entity.zig_chunk_0*
