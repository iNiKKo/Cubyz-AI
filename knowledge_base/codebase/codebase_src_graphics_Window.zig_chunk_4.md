# [hard/codebase_src_graphics_Window.zig] - Chunk 4

**Type:** implementation
**Keywords:** GLFW, key codes, mouse buttons, event handling, modifiers
**Symbols:** Key, Key.setPressed, Key.action
**Concepts:** input handling, keyboard events, mouse events

## Summary
This chunk defines the `Key` struct, which manages key and mouse button states and actions within the Cubyz graphics window.

## Explanation
This chunk defines the `Key` struct, which manages key and mouse button states and actions within the Cubyz graphics window. The struct uses GLFW constants for key and mouse codes, including specific mappings such as `c.GLFW_KEY_INSERT => "Insert"`, `c.GLFW_KEY_DELETE => "Delete"`, `c.GLFW_KEY_RIGHT => "Right"`, `c.GLFW_KEY_LEFT => "Left"`, `c.GLFW_KEY_DOWN => "Down"`, `c.GLFW_KEY_UP => "Up"`, `c.GLFW_KEY_PAGE_UP => "Page Up"`, `c.GLFW_KEY_PAGE_DOWN => "Page Down"`, `c.GLFW_KEY_HOME => "Home"`, `c.GLFW_KEY_END => "End"`, `c.GLFW_KEY_CAPS_LOCK => "Caps Lock"`, `c.GLFW_KEY_SCROLL_LOCK => "Scroll Lock"`, `c.GLFW_KEY_NUM_LOCK => "Num Lock"`, `c.GLFW_KEY_PRINT_SCREEN => "Print Screen"`, `c.GLFW_KEY_PAUSE => "Pause"`, `c.GLFW_KEY_F1 => "F1"` through `c.GLFW_KEY_F25 => "F25"`, `c.GLFW_KEY_KP_0 => "Keypad 0"` through `c.GLFW_KEY_KP_EQUAL => "Keypad ="`, `c.GLFW_KEY_LEFT_SHIFT => "Left Shift"`, `c.GLFW_KEY_LEFT_CONTROL => "Left Control"`, `c.GLFW_KEY_LEFT_ALT => "Left Alt"`, `c.GLFW_KEY_LEFT_SUPER => "Left Super"`, `c.GLFW_KEY_RIGHT_SHIFT => "Right Shift"`, `c.GLFW_KEY_RIGHT_CONTROL => "Right Control"`, `c.GLFW_KEY_RIGHT_ALT => "Right Alt"`, `c.GLFW_KEY_RIGHT_SUPER => "Right Super"`, and `c.GLFW_KEY_MENU => "Menu"`. Additionally, it handles mouse buttons with constants like `c.GLFW_MOUSE_BUTTON_LEFT => "Left Button"`, `c.GLFW_MOUSE_BUTTON_MIDDLE => "Middle Button"`, and `c.GLFW_MOUSE_BUTTON_RIGHT => "Right Button"`. The struct includes methods to describe the key or mouse button, update its pressed state (`setPressed`), and perform actions based on the event type (press, release, repeat) (`action`). It manages modifiers and text input requirements within these methods.

## Code Example
```zig
fn setPressed(self: *Key, newPressed: bool, isGrabbed: bool, mods: Modifiers, textKeyPressedInTextField: bool) void {
	if (self.isToggling == .yes) {
		if (newPressed) {
			self.pressed = !self.pressed;
		}
		return;
	}
	if (newPressed != self.pressed) {
		self.pressed = newPressed;
		self.modsOnPress = mods;
		self.value = @floatFromInt(@intFromBool(newPressed));
		if (newPressed) {
			self.action(.press, isGrabbed, mods, textKeyPressedInTextField);
			self.action(.repeat, isGrabbed, mods, textKeyPressedInTextField);
		} else {
			self.action(.release, isGrabbed, mods, textKeyPressedInTextField);
		}
	}
}
```

## Related Questions
- What does the `Key` struct manage in Cubyz?
- How does the `setPressed` method update the key state?
- What actions are performed based on event types (press, release, repeat)?
- How does the `action` method handle different event types?
- What are the GLFW constants used for key and mouse codes?
- How are modifiers and text input requirements managed in the `Key` struct?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_4*
