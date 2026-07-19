# [hard/codebase_src_graphics_Window.zig] - Chunk 7

**Type:** implementation
**Keywords:** deinitialization, cursor visibility, event processing, fullscreen mode, GLFW functions
**Symbols:** deinit, cursorVisible, setCursorVisible, handleEvents, scrollOffset, scrollOffsetInteger, toggleFullscreen, oldX, oldY, oldWidth, oldHeight, isFullscreen
**Concepts:** window management, cursor control, event handling, fullscreen toggle

## Summary
Handles window deinitialization, cursor visibility, event processing, and fullscreen toggling.

## Explanation
This chunk manages the lifecycle of a graphics window, including its destruction, cursor management, event handling, and switching between windowed and fullscreen modes. The `deinit` function cleans up resources like gamepads and GLFW windows. The `setCursorVisible` method updates the visibility state of the cursor. The `handleEvents` function processes input events and updates the gamepad state. The `toggleFullscreen` method toggles the window between fullscreen and windowed modes, saving and restoring the previous window position and size by storing the old position (`oldX`, `oldY`) and dimensions (`oldWidth`, `oldHeight`) before entering fullscreen mode and restoring them when exiting.

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
- How does the `deinit` function clean up resources?
- What is the purpose of the `setCursorVisible` method?
- How are input events processed in this chunk?
- What steps are involved in toggling fullscreen mode?
- How does the chunk handle cursor visibility changes?
- What GLFW functions are used for window management?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_7*
