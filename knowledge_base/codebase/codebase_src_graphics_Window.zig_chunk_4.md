# [hard/codebase_src_graphics_Window.zig] - Chunk 4

**Type:** implementation
**Keywords:** GLFW, key codes, mouse buttons, event handling, modifiers
**Symbols:** Key, Key.setPressed, Key.action
**Concepts:** input handling, keyboard events, mouse events

## Summary
This chunk defines the `Key` struct, which manages key and mouse button states and actions within the Cubyz graphics window.

## Explanation
The `Key` struct handles keyboard and mouse input events. It includes methods to describe the key or mouse button, update its pressed state, and perform actions based on the event type (press, release, repeat). The struct uses GLFW constants for key and mouse codes and manages modifiers and text input requirements.

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
