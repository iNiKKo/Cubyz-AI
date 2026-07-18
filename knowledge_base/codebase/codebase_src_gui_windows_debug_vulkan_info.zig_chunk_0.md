# [easy/codebase_src_gui_windows_debug_vulkan_info.zig] - Chunk 0

**Type:** implementation
**Keywords:** Vulkan, Info Window, Extensions, Render Function, Initialization
**Symbols:** graphics, draw, Texture, Vec2f, TaskType, vulkan, GuiWindow, GuiComponent
**Concepts:** Vulkan Info Window, Vulkan Version, Interesting Extensions

## Summary
Vulkan Info Window

## Explanation
This chunk defines a Vulkan info window that displays the Vulkan version and list of interesting extensions present in the engine. It initializes the window's position, size, and properties, and provides a render function to display the information. The Vulkan version is displayed as `{vulkan.version.major}.{vulkan.version.minor}`. The render function iterates over `@TypeOf(vulkan.interestingExtensions)` and prints each extension name if it is present.

## Code Example
```zig
pub fn onOpen() void {
	main.threadPool.performance.clear();
}
```

## Related Questions
- What specific Vulkan version is displayed in the info window?
- Which extensions are listed as interesting in the engine?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_vulkan_info.zig_chunk_0*
