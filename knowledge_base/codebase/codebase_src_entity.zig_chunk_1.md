# [medium/codebase_src_entity.zig] - Chunk 1

**Type:** api
**Keywords:** entity management, component handling, serialization, network transmission, rendering
**Symbols:** client, client.init, client.deinit, client.clear, client.removeAllComponents, client.render, client.renderHud, server, server.init, server.deinit, server.update, server.componentsToBase64, server.removeAllComponents, server.transmitChange, loadComponentsFromBase64, AudienceInfo, ComponentSaveBehaviour
**Concepts:** entity ECS, networking protocol, binary serialization

## Summary
This chunk defines client and server logic for entity management, including initialization, deinitialization, clearing, rendering, and component handling.

## Explanation
The chunk contains two main structs: `client` and `server`, each with methods for initializing, deinitializing, updating, and managing entities and their components. The client struct handles rendering and HUD updates, while the server struct manages component serialization to Base64, transmitting changes over the network, and loading components from Base64 data. It also defines enums for audience information and component save behavior.

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
