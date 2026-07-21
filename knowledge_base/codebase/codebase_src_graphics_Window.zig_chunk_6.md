# [hard/codebase_src_graphics_Window.zig] - Chunk 6

**Type:** implementation
**Keywords:** GLFW, OpenGL, Vulkan, cursor control, event callbacks, window initialization, resource loading
**Symbols:** resetNextInputListenters, updateCursor, releaseButtonsOnGrabChange, setMouseGrabbed, getMousePosition, getWindowSize, reloadSettings, getClipboardString, setClipboardString, init
**Concepts:** window management, input handling, settings configuration, clipboard operations

## Summary
Handles window initialization, input management, and settings reloading for the Cubyz graphics engine.

## Explanation
This chunk manages the lifecycle of a GLFW window in the Cubyz graphics engine. It initializes the window with OpenGL context, sets up various callbacks for handling keyboard, mouse, and framebuffer events, and manages input modes such as cursor visibility and raw mouse motion. The `init` function is responsible for setting up GLFW, creating windows, loading resources like icons, and initializing Vulkan if enabled. Other functions handle resetting input listeners, updating the cursor state based on window grab status, releasing buttons when the grab state changes, getting mouse position and window size, reloading settings like vsync, and managing clipboard operations.

The `init` function specifically sets up GLFW with error callbacks and initializes a window with OpenGL context. It also checks if Vulkan is supported and creates a Vulkan window if enabled. On macOS, it sets the Vulkan loader directly due to static linking issues. The chunk handles cursor visibility by setting the GLFW cursor mode based on whether the window is grabbed or not. Clipboard operations are managed through functions that get and set clipboard strings.

The `releaseButtonsOnGrabChange` function releases buttons when the grab state changes, ensuring that key states are reset appropriately. The chunk reloads settings like vsync using the `reloadSettings` function, which sets the GLFW swap interval based on the current settings.

Callbacks for handling input events include key callbacks, character callbacks, framebuffer size callbacks, cursor position callbacks, mouse button callbacks, and scroll callbacks.

Specifically, the Vulkan initialization process includes checking if Vulkan is supported (`c.glfwVulkanSupported() == c.GLFW_TRUE`) and creating a Vulkan window with specific hints (`c.GLFW_CLIENT_API`, `c.GLFW_VISIBLE`). On macOS, it sets the Vulkan loader directly using `glfwInitVulkanLoader`. The OpenGL context is initialized with specific version requirements (OpenGL 4.6) and debug settings (`c.GLFW_OPENGL_DEBUG_CONTEXT`, `c.GLFW_CONTEXT_VERSION_MAJOR`, `c.GLFW_CONTEXT_VERSION_MINOR`). If Vulkan testing mode is not enabled, the Vulkan window is destroyed after initialization.

## Code Example
```zig
pub fn resetNextInputListenters() void {
	nextGamepadListener = null;
	nextKeypressListener = null;
}
```

## Related Questions
- What function initializes the GLFW window and sets up OpenGL context?
- How does the chunk handle cursor visibility based on the grab status?
- Which functions manage clipboard operations in this chunk?
- What is the purpose of the `releaseButtonsOnGrabChange` function?
- How does the chunk reload settings like vsync?
- What callbacks are set up for handling input events in the GLFW window?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_6*
