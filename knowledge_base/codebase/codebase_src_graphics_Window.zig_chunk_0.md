# [hard/codebase_src_graphics_Window.zig] - Chunk 0

**Type:** implementation
**Keywords:** global variables, GLFW window, Vulkan, C interop, settings
**Symbols:** isFullscreen, lastUsedMouse, width, height, window, vulkanWindow, grabbed, scrollOffset, scrollOffsetInteger, scrollOffsetFraction
**Concepts:** window management, global state, imports

## Summary
Declares global variables and imports for window management in the graphics module.

## Explanation
This chunk defines several global variables used to manage window properties such as fullscreen status, dimensions, GLFW window handles, mouse state, scroll offsets, and cursor grabbing. It also imports necessary modules like standard library (`std`), built-in Zig features (`builtin`), main application settings (`main.settings`), file handling utilities (`main.files`), vector math (`main.vec`), Vulkan bindings (`vulkan.zig`), and C interop (`c`). These variables and imports form the foundational setup for window management within the graphics module.

**Global Variables:*
- `isFullscreen`: A boolean indicating whether the window is in fullscreen mode. Initially set to `false`.
- `lastUsedMouse`: A public boolean tracking the last used mouse state. Initially set to `true`.
- `width`: A public unsigned 31-bit integer representing the initial width of the window. Set to `1280` pixels.
- `height`: A public unsigned 31-bit integer representing the initial height of the window. Set to `720` pixels.
- `window`: A pointer to a GLFW window handle. Initially set to `undefined`.
- `vulkanWindow`: A pointer to a Vulkan-specific GLFW window handle. Initially set to `undefined`.
- `grabbed`: A boolean indicating whether the cursor is grabbed. Initially set to `false`.
- `scrollOffset`: A floating-point number representing the scroll offset. Initially set to `0`.
- `scrollOffsetInteger`: An integer representing the scroll offset in whole units. Initially set to `0`.
- `scrollOffsetFraction`: A floating-point number representing the fractional part of the scroll offset. Initially set to `0`.

**Imports:*
- `std`: Standard library for Zig.
- `builtin`: Built-in Zig features.
- `main.settings`: Application settings.
- `main.files`: File handling utilities.
- `vec`: Vector math module, specifically importing `Vec2f`.
- `vulkan.zig`: Vulkan bindings.
- `c`: C interop module.

**Fullscreen Status Management:** The fullscreen status is managed by the `isFullscreen` boolean variable. Initially set to `false`, it can be toggled to switch between windowed and fullscreen modes.

**Mouse State Tracking:** The mouse state is tracked by the `lastUsedMouse` variable, which indicates whether the last interaction was with the mouse. Additionally, cursor grabbing is managed by the `grabbed` boolean variable.

**Vulkan Integration:** Vulkan integration with GLFW is handled through the `vulkanWindow` pointer, which is a specific type of GLFW window handle used for Vulkan contexts.

**Purpose of `lastUsedMouse`:** The `lastUsedMouse` variable is used to track whether the last interaction was with the mouse, which can be useful for input handling and state management within the application.

## Related Questions
- What is the initial width of the window?
- How is the fullscreen status managed in this module?
- Which modules are imported for window management?
- What global variables track mouse state and scrolling?
- How does this chunk handle Vulkan integration with GLFW?
- What is the purpose of the `lastUsedMouse` variable?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_0*
