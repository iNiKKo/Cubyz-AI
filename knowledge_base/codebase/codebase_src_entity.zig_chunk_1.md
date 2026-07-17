# [medium/codebase_src_entity.zig] - Chunk 1

**Type:** api
**Keywords:** entity management, component lifecycle, network transmission, serialization, deserialization
**Symbols:** client, server, clear, removeAllComponents, render, renderHud, init, deinit, update, componentsToBase64, transmitChange, loadComponentsFromBase64, AudienceInfo, ComponentSaveBehaviour
**Concepts:** entity ECS, networking protocol, binary serialization

## Summary
This chunk defines client and server entity management functions, including clearing entities, rendering, initializing, deinitializing systems and components, converting components to Base64, removing components, transmitting changes over the network, and loading components from Base64.

## Explanation
The chunk contains two main sections: one for client-side operations and another for server-side operations. The client section includes functions like `clear`, which resets entity managers and components; `removeAllComponents`, which unloads all components of an entity; and `render` and `renderHud`, which update and render entities and their HUDs respectively. The server section manages initialization (`init`) and deinitialization (`deinit`) of systems and components, updates systems, converts components to Base64 for transmission, removes components from an entity, and transmits changes in entity components over the network using a binary protocol. Additionally, there are utility functions like `loadComponentsFromBase64` for decoding Base64 data into components and enums defining audience information and component save behavior.

## Code Example
```zig
pub fn removeAllComponents(entity: Entity) void {
		const list = main.entity.components;
		inline for (@typeInfo(list).@"struct".decls) |decl| {
			@field(list, decl.name).client.unload(entity);
		}
	}
```

## Related Questions
- How does the client clear entities and components?
- What is the purpose of the `renderHud` function in the client section?
- How are systems initialized on the server side?
- How do components get converted to Base64 for transmission?
- What happens when a component needs to be transmitted over the network?
- How are components loaded from Base64 data?

*Source: unknown | chunk_id: codebase_src_entity.zig_chunk_1*
