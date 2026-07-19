# [hard/codebase_src_graphics_Window.zig] - Chunk 3

**Type:** api
**Keywords:** key binding, gamepad state, modifier keys, action callbacks, human-readable names
**Symbols:** Key, Key.name, Key.pressed, Key.isToggling, Key.modsOnPress, Key.value, Key.key, Key.gamepadAxis, Key.gamepadButton, Key.mouseButton, Key.scancode, Key.releaseAction, Key.pressAction, Key.repeatAction, Key.notifyRequirement, Key.grabbedOnPress, Key.requiredModifiers, Key.IsToggling, Key.Modifiers, Key.Modifiers.shift, Key.Modifiers.control, Key.Modifiers.alt, Key.Modifiers.super, Key.Modifiers.capsLock, Key.Modifiers.numLock, Key.Modifiers.toInt, Key.Modifiers.satisfiedBy, Key.Modifiers.isEmpty, Key.Requirement, Key.getGamepadName, Key.getName
**Concepts:** input handling, keyboard mapping, gamepad input

## Summary
Handles gamepad and keyboard input mapping, initialization, and deinitialization.

## Explanation
This chunk defines the `Key` struct which encapsulates various properties of a key or button, including its name, state (pressed), modifiers, actions on press, repeat, and release, as well as mappings to gamepad axes and buttons. The `Key` struct includes nested enums for toggling states (`IsToggling`) and modifier combinations (`Modifiers`). The `init` function initializes the gamepad state using a global allocator, while the `deinit` function cleans up by destroying all allocated values and deinitializing the gamepad state.

The `Key` struct has several fields:
- `name`: A string representing the name of the key or button.
- `pressed`: A boolean indicating whether the key is currently pressed.
- `isToggling`: An enum (`IsToggling`) that specifies if the key toggles on press.
- `modsOnPress`: A struct (`Modifiers`) representing the modifiers required to be pressed for the key action.
- `value`: A float representing the value of the key (e.g., axis position).
- `key`: An integer representing the GLFW key code.
- `gamepadAxis`: An optional struct (`GamepadAxis`) representing the gamepad axis mapping.
- `gamepadButton`: An integer representing the GLFW gamepad button code.
- `mouseButton`: An integer representing the GLFW mouse button code.
- `scancode`: An integer representing the scancode of the key.
- `releaseAction`, `pressAction`, `repeatAction`: Optional function pointers for actions on release, press, and repeat.
- `notifyRequirement`: An enum (`Requirement`) specifying when the key should be notified.
- `grabbedOnPress`: A boolean indicating if the key is grabbed on press.
- `requiredModifiers`: A struct (`Modifiers`) representing the required modifiers for the key action.

The `getGamepadName` method returns a human-readable name for a gamepad axis or button based on its configuration. For example, it maps `GLFW_GAMEPAD_AXIS_LEFT_X` to "Left stick right" if positive and "Left stick left" if negative. Similarly, it maps `GLFW_GAMEPAD_BUTTON_A` to "A", `GLFW_GAMEPAD_BUTTON_B` to "B", and so on.

The `Modifiers` struct includes several fields:
- `shift`, `control`, `alt`, `super`, `capsLock`, `numLock`: Boolean flags representing the modifier keys.

The `Modifiers` struct also includes methods:
- `toInt`: Converts the modifiers to an integer representation.
- `satisfiedBy`: Checks if the required modifiers are satisfied by the actual modifiers.
- `isEmpty`: Checks if no modifiers are set.

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
