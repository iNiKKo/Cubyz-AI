# [hard/codebase_src_graphics_Window.zig] - Chunk 3

**Type:** api
**Keywords:** key binding, gamepad state, modifier keys, action callbacks, human-readable names
**Symbols:** Key, Key.name, Key.pressed, Key.isToggling, Key.modsOnPress, Key.value, Key.key, Key.gamepadAxis, Key.gamepadButton, Key.mouseButton, Key.scancode, Key.releaseAction, Key.pressAction, Key.repeatAction, Key.notifyRequirement, Key.grabbedOnPress, Key.requiredModifiers, Key.IsToggling, Key.Modifiers, Key.Modifiers.shift, Key.Modifiers.control, Key.Modifiers.alt, Key.Modifiers.super, Key.Modifiers.capsLock, Key.Modifiers.numLock, Key.Modifiers.toInt, Key.Modifiers.satisfiedBy, Key.Modifiers.isEmpty, Key.Requirement, Key.getGamepadName, Key.getName
**Concepts:** input handling, keyboard mapping, gamepad input

## Summary
Handles gamepad and keyboard input mapping, initialization, and deinitialization.

## Explanation
This chunk defines the `Key` struct which encapsulates various properties of a key or button including its name, state (pressed), modifiers, actions on press, repeat, and release, as well as mappings to gamepad axes and buttons. It also includes nested enums for toggling states (`IsToggling`) and modifier combinations (`Modifiers`). The `init` function initializes the gamepad state using a global allocator, while the `deinit` function cleans up by destroying all allocated values and deinitializing the gamepad state. The `getGamepadName` method returns a human-readable name for a gamepad axis or button based on its configuration.

## Code Example
```zig
pub const Modifiers = packed struct(u6) {
		shift: bool = false,
		control: bool = false,
		alt: bool = false,
		super: bool = false,
		capsLock: bool = false,
		numLock: bool = false,

		fn toInt(self: Modifiers) u6 {
			return @bitCast(self);
		}

		fn satisfiedBy(required: Modifiers, actual: Modifiers) bool {
			return (required.toInt() ^ actual.toInt()) & required.toInt() == 0;
		}

		fn isEmpty(self: Modifiers) bool {
			return self.toInt() == 0;
		}
	}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `Key` struct handle gamepad button mappings?
- What methods are available for retrieving human-readable names from a `Key` instance?
- How are modifier keys represented and checked within the `Modifiers` struct?
- What is the role of the `deinit` function in this chunk?
- How does the `getGamepadName` method determine the name of a gamepad axis or button?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_3*
