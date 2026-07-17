# [easy/codebase_src_gui_components_Icon.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiComponent, Texture, Vec2f, globalAllocator, deinit, render, updateTexture, position, size, allocation
**Symbols:** Icon, Icon.pos, Icon.size, Icon.texture, Icon.init, Icon.deinit, Icon.toComponent, Icon.updateTexture, Icon.render
**Concepts:** gui component, texture rendering, resource management, allocation lifecycle

## Summary
This chunk defines the Icon GuiComponent struct with initialization, deinitialization, texture update, and rendering methods.

## Explanation
The chunk declares an Icon struct (aliased via @This) containing pos: Vec2f, size: Vec2f, and texture: Texture fields. It provides a public init function that allocates the struct on main.globalAllocator, initializes all fields, and returns the pointer. The deinit function destroys the allocated memory using main.globalAllocator.destroy. A toComponent method converts an Icon into a GuiComponent with an icon field set to self. An updateTexture method allows replacing the texture while keeping position and size unchanged. A render method delegates to the Texture's render function using the stored pos and size.

## Code Example
```zig
pub fn deinit(self: *const Icon) void {
	main.globalAllocator.destroy(self);
}
```

## Related Questions
- How does the Icon component manage its texture resource lifecycle?
- What is the exact signature and behavior of Icon.init?
- Which allocator is used for Icon instances in this chunk?
- How does toComponent wrap an Icon into a GuiComponent?
- Does updateTexture modify position or size fields?
- What arguments does render expect from its caller?

*Source: unknown | chunk_id: codebase_src_gui_components_Icon.zig_chunk_0*
