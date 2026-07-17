# [hard/codebase_src_graphics_Window.zig] - Chunk 3

**Type:** api
**Keywords:** GLFW, key events, mouse events, callback functions, state management
**Symbols:** Key, Key.mouseButton, Key.key, Key.scancode, Key.pressed, Key.isToggling, Key.modsOnPress, Key.value, Key.grabbedOnPress, Key.notifyRequirement, Key.requiredModifiers, Key.pressAction, Key.releaseAction, Key.repeatAction, GLFWCallbacks, GLFWCallbacks.errorCallback, GLFWCallbacks.keyCallback
**Concepts:** input handling, event dispatching, key mapping

## Summary
Handles key and mouse input mapping and event dispatching.

## Explanation
This chunk defines a `Key` struct that manages the state of individual keys or mouse buttons, including their pressed status, modifiers, and associated actions. The `getName` method returns the human-readable name of a key or button based on GLFW constants. The `setPressed` method updates the key's pressed state and triggers actions if necessary. The `action` method dispatches events to registered callbacks for press, release, and repeat actions. Additionally, it contains a `GLFWCallbacks` struct with error and key callback functions that interface with GLFW.

## Code Example
```zig
fn getName(self: Key) []const u8 {
		if (self.mouseButton == -1) {
			return switch (self.key) {
				c.GLFW_KEY_SPACE => "Space",
				c.GLFW_KEY_GRAVE_ACCENT => "Grave Accent",
				c.GLFW_KEY_ESCAPE => "Escape",
				c.GLFW_KEY_ENTER => "Enter",
				c.GLFW_KEY_TAB => "Tab",
				c.GLFW_KEY_BACKSPACE => "Backspace",
				c.GLFW_KEY_INSERT => "Insert",
				c.GLFW_KEY_DELETE => "Delete",
				c.GLFW_KEY_RIGHT => "Right",
				c.GLFW_KEY_LEFT => "Left",
				c.GLFW_KEY_DOWN => "Down",
				c.GLFW_KEY_UP => "Up",
				c.GLFW_KEY_PAGE_UP => "Page Up",
				c.GLFW_KEY_PAGE_DOWN => "Page Down",
				c.GLFW_KEY_HOME => "Home",
				c.GLFW_KEY_END => "End",
				c.GLFW_KEY_CAPS_LOCK => "Caps Lock",
				c.GLFW_KEY_SCROLL_LOCK => "Scroll Lock",
				c.GLFW_KEY_NUM_LOCK => "Num Lock",
				c.GLFW_KEY_PRINT_SCREEN => "Print Screen",
				c.GLFW_KEY_PAUSE => "Pause",
				c.GLFW_KEY_F1 => "F1",
				c.GLFW_KEY_F2 => "F2",
				c.GLFW_KEY_F3 => "F3",
				c.GLFW_KEY_F4 => "F4",
				c.GLFW_KEY_F5 => "F5",
				c.GLFW_KEY_F6 => "F6",
				c.GLFW_KEY_F7 => "F7",
				c.GLFW_KEY_F8 => "F8",
				c.GLFW_KEY_F9 => "F9",
				c.GLFW_KEY_F10 => "F10",
				c.GLFW_KEY_F11 => "F11",
				c.GLFW_KEY_F12 => "F12",
				c.GLFW_KEY_F13 => "F13",
				c.GLFW_KEY_F14 => "F14",
				c.GLFW_KEY_F15 => "F15",
				c.GLFW_KEY_F16 => "F16",
				c.GLFW_KEY_F17 => "F17",
				c.GLFW_KEY_F18 => "F18",
				c.GLFW_KEY_F19 => "F19",
				c.GLFW_KEY_F20 => "F20",
				c.GLFW_KEY_F21 => "F21",
				c.GLFW_KEY_F22 => "F22",
				c.GLFW_KEY_F23 => "F23",
				c.GLFW_KEY_F24 => "F24",
				c.GLFW_KEY_F25 => "F25",
				c.GLFW_KEY_KP_0 => "Keypad 0",
				c.GLFW_KEY_KP_1 => "Keypad 1",
				c.GLFW_KEY_KP_2 => "Keypad 2",
				c.GLFW_KEY_KP_3 => "Keypad 3",
				c.GLFW_KEY_KP_4 => "Keypad 4",
				c.GLFW_KEY_KP_5 => "Keypad 5",
				c.GLFW_KEY_KP_6 => "Keypad 6",
				c.GLFW_KEY_KP_7 => "Keypad 7",
				c.GLFW_KEY_KP_8 => "Keypad 8",
				c.GLFW_KEY_KP_9 => "Keypad 9",
				c.GLFW_KEY_KP_DECIMAL => "Keypad Decimal",
				c.GLFW_KEY_KP_DIVIDE => "Keypad Divide",
				c.GLFW_KEY_KP_MULTIPLY => "Keypad Multiply",
				c.GLFW_KEY_KP_SUBTRACT => "Keypad Sutract",
				c.GLFW_KEY_KP_ADD => "Keypad Add",
				c.GLFW_KEY_KP_ENTER => "Keypad Enter",
				c.GLFW_KEY_KP_EQUAL => "Keypad =",
				c.GLFW_KEY_LEFT_SHIFT => "Left Shift",
				c.GLFW_KEY_LEFT_CONTROL => "Left Control",
				c.GLFW_KEY_LEFT_ALT => "Left Alt",
				c.GLFW_KEY_LEFT_SUPER => "Left Super",
				c.GLFW_KEY_RIGHT_SHIFT => "Right Shift",
				c.GLFW_KEY_RIGHT_CONTROL => "Right Control",
				c.GLFW_KEY_RIGHT_ALT => "Right Alt",
				c.GLFW_KEY_RIGHT_SUPER => "Right Super",
				c.GLFW_KEY_MENU => "Menu",
				c.GLFW_KEY_UNKNOWN => "(Unbound)",
				else => {
					const cName = c.glfwGetKeyName(self.key, self.scancode);
					if (cName != null) {
						return std.mem.span(cName);
					} else {
						return "Unknown Key";
					}
				},
			};
		} else {
			return switch (self.mouseButton) {
				c.GLFW_MOUSE_BUTTON_LEFT => "Left Button",
				c.GLFW_MOUSE_BUTTON_MIDDLE => "Middle Button",
				c.GLFW_MOUSE_BUTTON_RIGHT => "Right Button",
				else => "Other Mouse Button",
			};
		}
	}
```

## Related Questions
- What is the purpose of the `getName` method in the `Key` struct?
- How does the `setPressed` method update the key's state?
- What actions are dispatched by the `action` method?
- What does the `GLFWCallbacks.errorCallback` function do?
- How are key events handled in the `keyCallback` function?
- What is the role of the `requiredModifiers` field in the `Key` struct?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_3*
