# [medium/codebase_src_entity.zig] - Chunk 1

**Type:** api
**Keywords:** entity management, component handling, serialization, network transmission, rendering
**Symbols:** client, client.init, client.deinit, client.clear, client.removeAllComponents, client.render, client.renderHud, server, server.init, server.deinit, server.update, server.componentsToBase64, server.removeAllComponents, server.transmitChange, loadComponentsFromBase64, AudienceInfo, ComponentSaveBehaviour
**Concepts:** entity ECS, networking protocol, binary serialization

## Summary
This chunk defines client and server logic for entity management, including initialization, deinitialization, clearing, rendering, and component handling. It includes explicit methods for initializing and managing entities' components on both the client and server sides, as well as specific steps for rendering and network transmission of component data.

## Explanation
The chunk contains two main structs: `client` and `server`, each with detailed methods for entity management. The `client.init()` method initializes all systems and components by iterating through their declarations and calling the respective client initialization functions. Similarly, `client.deinit()` deinitializes them in reverse order. The `client.clear()` function clears entities' components and systems by invoking their clear methods. The `client.removeAllComponents(entity: Entity)` removes all components associated with a given entity on the client side. Rendering is handled through `client.render(projMatrix: Mat4f, ambientLight: Vec3f, playerPos: Vec3d, deltaTime: f64)` which updates entities and renders systems based on provided parameters, and `client.renderHud(projMatrix: Mat4f, ambientLight: Vec3f, playerPos: Vec3d)` for rendering HUD elements. On the server side, `server.init()` initializes all components and systems by calling their respective initialization functions. The `server.deinit()` method deinitializes them in reverse order. The `server.update()` function updates all systems on the server. Component data is serialized to Base64 using `server.componentsToBase64(allocator: main.heap.NeverFailingAllocator, entity: Entity, audience: main.entity.AudienceInfo)` which writes component IDs, versions, and binary data into a writer object. The `server.removeAllComponents(entity: Entity)` function removes all components associated with an entity on the server side. Network transmission of changes is managed by `server.transmitChange(EntityComponent: type, entity: Entity)`, which sends updated component data to connected users based on their proximity to the entity. Loading components from Base64 data is handled by `loadComponentsFromBase64(base64Data: []const u8, entity: Entity, comptime side: main.sync.Side)` which decodes and reads serialized data into binary reader objects for further processing.

## Code Example
```zig
pub fn clear() void {
		main.client.entity_manager.clear();
		inline for (@typeInfo(components).@"struct".decls) |decl| {
			@field(components, decl.name).client.clear();
		}
		inline for (@typeInfo(systems).@"struct".decls) |decl| {
			@field(systems, decl.name).client.clear();
		}
	}
```

## Related Questions
- How does the client initialize its entity manager and components?
- What methods are available in the server struct for managing entities?
- How is component data serialized to Base64 on the server side?
- What happens when an entity's components are removed on the server?
- How does the client handle rendering and HUD updates?
- What error handling is implemented when loading components from Base64?

*Source: unknown | chunk_id: codebase_src_entity.zig_chunk_1*
