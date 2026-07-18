# [hard/codebase_src_graphics_Window.zig] - Chunk 1

**Type:** implementation
**Keywords:** deadzone application, button/axis event handling, thread pool, asynchronous downloading, input processing
**Symbols:** Gamepad, Gamepad.gamepadState, Gamepad.controllerMappingsDownloaded, Gamepad.controllerConnectedPreviously, Gamepad.applyDeadzone, Gamepad.applyDeadzones2D, Gamepad.update, Gamepad.isControllerConnected, Gamepad.wereControllerMappingsDownloaded, ControllerMappingDownloadTask, ControllerMappingDownloadTask.curTimestamp, ControllerMappingDownloadTask.running, ControllerMappingDownloadTask.vtable, ControllerMappingDownloadTask.schedule
**Concepts:** gamepad input processing, controller mapping downloads

## Summary
Handles gamepad input processing and controller mapping downloads.

## Explanation
The `Gamepad` struct manages gamepad state, including deadzone application and button/axis event handling. It updates the gamepad state each frame, checks for connected controllers, and schedules controller mappings downloads if necessary. The `update` method processes input from all connected gamepads, applies deadzones to axes, and triggers callbacks for button presses. The `ControllerMappingDownloadTask` struct handles asynchronous downloading of controller mappings using a thread pool.

## Code Example
```zig
pub fn update(delta: f64) void {
		if (!controllerConnectedPreviously and isControllerConnected()) {
			controllerConnectedPreviously = true;
			downloadControllerMappings();
		}
		var jid: c_int = 0;
		while (jid < c.GLFW_JOYSTICK_LAST) : (jid += 1) {
			// Can't initialize with the state, or it will become a reference.
			var oldState: c.GLFWgamepadstate = std.mem.zeroes(c.GLFWgamepadstate);
			if (gamepadState.get(jid)) |v| {
				oldState = v.*;
			}
			const joystickFound = c.glfwJoystickPresent(jid) != 0 and c.glfwJoystickIsGamepad(jid) != 0;
			if (joystickFound) {
				if (!gamepadState.contains(jid)) {
					gamepadState.put(jid, main.globalAllocator.create(c.GLFWgamepadstate)) catch unreachable;
				}
				_ = c.glfwGetGamepadState(jid, gamepadState.get(jid).?);
			} else {
				if (gamepadState.contains(jid)) {
					main.globalAllocator.destroy(gamepadState.get(jid).?);
					_ = gamepadState.remove(jid);
				}
			}
			const newState: *c.GLFWgamepadstate = gamepadState.get(jid) orelse continue;
			applyDeadzones2D(newState, c.GLFW_GAMEPAD_AXIS_LEFT_X, c.GLFW_GAMEPAD_AXIS_LEFT_Y);
			applyDeadzones2D(newState, c.GLFW_GAMEPAD_AXIS_RIGHT_X, c.GLFW_GAMEPAD_AXIS_RIGHT_Y);
			applyDeadzone(newState, c.GLFW_GAMEPAD_AXIS_LEFT_TRIGGER);
			applyDeadzone(newState, c.GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER);
			if (nextGamepadListener != null) {
				for (0..c.GLFW_GAMEPAD_BUTTON_LAST) |btn| {
					if ((newState.buttons[btn] == 0) and (oldState.buttons[btn] != 0)) {
						nextGamepadListener.?(null, @intCast(btn));
						nextGamepadListener = null;
						return;
					}
				}
			}
			if (nextGamepadListener != null) {
				for (0..c.GLFW_GAMEPAD_AXIS_LAST) |axis| {
					const newAxis = newState.axes[axis];
					const oldAxis = oldState.axes[axis];
					if (newAxis != 0 and oldAxis == 0) {
						nextGamepadListener.?(.{.axis = @intCast(axis), .positive = newState.axes[axis] > 0}, -1);
						nextGamepadListener = null;
						return;
					}
				}
			}
			const isGrabbed = grabbed;
			for (&main.KeyBoard.keys) |*key| {
				if (key.gamepadAxis == null) {
					if (key.gamepadButton >= 0) {
						const oldPressed = oldState.buttons[@intCast(key.gamepadButton)] != 0;
						const newPressed = newState.buttons[@intCast(key.gamepadButton)] != 0;
						if (oldPressed != newPressed) {
							key.setPressed(newPressed, isGrabbed, .{}, false);
						}
					}
				} else {
					const axis = key.gamepadAxis.?.axis;
					const positive = key.gamepadAxis.?.positive;
					var newAxis = newState.axes[@intCast(axis)];
					var oldAxis = oldState.axes[@intCast(axis)];
					if (!positive) {
						newAxis *= -1.0;
						oldAxis *= -1.0;
					}
					newAxis = @max(newAxis, 0.0);
					oldAxis = @max(oldAxis, 0.0);
					const oldPressed = oldAxis > 0.5;
					const newPressed = newAxis > 0.5;
					if (oldPressed != newPressed) {
						key.setPressed(newPressed, isGrabbed, .{}, false);
					}
					if (newAxis != oldAxis) {
						key.value = newAxis;
					}
				}
			}
		}
		if (!grabbed) {
			const x = main.KeyBoard.key("uiRight").value - main.KeyBoard.key("uiLeft").value;
			const y = main.KeyBoard.key("uiDown").value - main.KeyBoard.key("uiUp").value;
			if (x != 0 or y != 0) {
				lastUsedMouse = false;
				GLFWCallbacks.currentPos[0] += @floatCast(x*delta*256);
				GLFWCallbacks.currentPos[1] += @floatCast(y*delta*256);
				const winSize = getWindowSize();
				GLFWCallbacks.currentPos[0] = std.math.clamp(GLFWCallbacks.currentPos[0], 0, winSize[0]);
				GLFWCallbacks.currentPos[1] = std.math.clamp(GLFWCallbacks.currentPos[1], 0, winSize[1]);
			}
			GLFWCallbacks.scroll(undefined, 0, @floatCast((main.KeyBoard.key("scrollUp").value - main.KeyBoard.key("scrollDown").value)*delta*4));
		}
		setCursorVisible(!grabbed and lastUsedMouse);
	}
```

## Related Questions
- How does the `Gamepad` struct handle deadzone application?
- What is the purpose of the `ControllerMappingDownloadTask` struct?
- How does the `update` method process gamepad input?
- What conditions trigger a controller mapping download task?
- How are button presses and axis movements handled in the `update` method?
- What role does the thread pool play in downloading controller mappings?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_1*
