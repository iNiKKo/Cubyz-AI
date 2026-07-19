# [hard/codebase_src_graphics_Window.zig] - Chunk 5

**Type:** api
**Keywords:** GLFW, callback functions, error logging, keyboard input, mouse input, framebuffer resizing, cursor position, smooth mouse movement
**Symbols:** GLFWCallbacks, GLFWCallbacks.errorCallback, GLFWCallbacks.keyCallback, GLFWCallbacks.charCallback, GLFWCallbacks.framebufferSize, GLFWCallbacks.cursorPosition, GLFWCallbacks.applyCursorPositionChanges, GLFWCallbacks.mouseButton, GLFWCallbacks.scroll, GLFWCallbacks.glDebugOutput, nextKeypressListener, setNextKeypressListener, nextGamepadListener, setNextGamepadListener
**Concepts:** input handling, window management, event callbacks, cursor smoothing

## Summary
Handles GLFW callbacks for window events such as key presses, mouse movements, and framebuffer resizing.

## Explanation
This chunk defines a struct `GLFWCallbacks` that encapsulates various callback functions for handling different types of input and window events using GLFW. The primary responsibilities include logging errors, processing keyboard and mouse inputs, updating the viewport and GUI when the framebuffer size changes, and managing cursor position data to smooth out mouse movements. It also provides mechanisms to set listeners for future keypresses and gamepad events, ensuring that only one listener can be active at a time.

The `errorCallback` function logs errors using `std.log.err`. The `keyCallback` function processes key presses and releases by checking the action type (press or release) and updating the corresponding key state in `main.KeyBoard.keys`. If a key press is detected, it also checks if there is an active `nextKeypressListener` to notify.

The `charCallback` function handles character input by passing it to the GUI text callbacks if the window is not grabbed.

The `framebufferSize` callback updates the width and height of the framebuffer, calls `main.renderer.updateViewport`, and refreshes the GUI scale and positions.

Mouse cursor position changes are smoothed out using a circular buffer (`deltas`) that averages mouse movements over multiple frames. The `cursorPosition` function updates the current position and calculates the delta, which is then applied to the camera rotation in `applyCursorPositionChanges`. This function averages the deltas over the last three frames before applying them to the camera.

The `mouseButton` function processes mouse button presses and releases similarly to the `keyCallback`, updating the corresponding key state in `main.KeyBoard.keys`.

The `scroll` function updates the scroll offset, separating it into integer and fractional parts for smooth scrolling.

The `glDebugOutput` function categorizes and logs OpenGL debug messages based on their source, type, and severity.

## Code Example
```zig
fn errorCallback(errorCode: c_int, description: [*c]const u8) callconv(.c) void {
	std.log.err("GLFW Error({}): {s}", .{errorCode, description});
}
```

## Related Questions
- What is the purpose of the `errorCallback` function in the GLFWCallbacks struct?
- How does the `keyCallback` function handle key presses and releases?
- What does the `framebufferSize` callback do when the window size changes?
- How are mouse cursor position changes smoothed out in this code?
- What is the role of the `nextKeypressListener` variable?
- How does the `glDebugOutput` function categorize and log OpenGL debug messages?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_5*
