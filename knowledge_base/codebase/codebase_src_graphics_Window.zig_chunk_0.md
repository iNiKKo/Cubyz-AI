# [hard/codebase_src_graphics_Window.zig] - Chunk 0

**Type:** implementation
**Keywords:** global variables, GLFW window, Vulkan, C interop, settings
**Symbols:** isFullscreen, lastUsedMouse, width, height, window, vulkanWindow, grabbed, scrollOffset, scrollOffsetInteger, scrollOffsetFraction
**Concepts:** window management, global state, imports

## Summary
Declares global variables and imports for window management in the graphics module.

## Explanation
This chunk defines several global variables used to manage window properties such as fullscreen status, dimensions, GLFW window handles, mouse state, scroll offsets, and cursor grabbing. It also imports necessary modules like standard library (`std`), built-in Zig features (`builtin`), main application settings (`main.settings`), file handling utilities (`main.files`), vector math (`main.vec`), Vulkan bindings (`vulkan.zig`), and C interop (`c`). These variables and imports form the foundational setup for window management within the graphics module.

## Related Questions
- What is the initial width of the window?
- How is the fullscreen status managed in this module?
- Which modules are imported for window management?
- What global variables track mouse state and scrolling?
- How does this chunk handle Vulkan integration with GLFW?
- What is the purpose of the `lastUsedMouse` variable?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_0*
