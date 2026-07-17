# [hard/codebase_src_graphics_Window.zig] - Chunk 6

**Type:** implementation
**Keywords:** GLFW, OpenGL, Vulkan, window creation, event loop
**Symbols:** vulkanWindow, window, cursorVisible, scrollOffset, scrollOffsetInteger, oldX, oldY, oldWidth, oldHeight, isFullscreen
**Concepts:** window management, input handling, OpenGL context, Vulkan support, fullscreen toggle

## Summary
Handles window creation, initialization, and event processing for Cubyz's graphics module.

## Explanation
This chunk manages the lifecycle of the application window using GLFW. It initializes GLFW, checks Vulkan support, creates a Vulkan-compatible window if enabled, sets up OpenGL context, loads OpenGL functions with GLAD, and configures various callbacks for handling user input and window events. The `deinit` function cleans up resources by destroying windows and terminating GLFW. Additional functionality includes toggling fullscreen mode and updating cursor visibility.

## Code Example
```zig
pub fn deinit() void {
	Gamepad.deinit();
	c.glfwDestroyWindow(window);
	if (settings.launchConfig.vulkanTestingMode) {
		c.glfwDestroyWindow(vulkanWindow);
		vulkan.deinit();
	}
	c.glfwTerminate();
}
```

## Related Questions
- How does the chunk initialize GLFW?
- What checks are performed for Vulkan support?
- How is the OpenGL context created and configured?
- What callbacks are set up for handling user input?
- How does the chunk handle window destruction during deinitialization?
- How is fullscreen mode toggled in this chunk?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_6*
