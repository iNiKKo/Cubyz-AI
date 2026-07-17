# [hard/codebase_src_graphics_Window.zig] - Chunk 2

**Type:** implementation
**Keywords:** packed struct, bitCast, switch expression, nullable pointer, function pointer, default value, enum variant, modifier satisfaction, requirement state, gamepad axis, keyboard key code
**Symbols:** IsToggling, Modifiers, Requirement, Key
**Concepts:** input handling, modifier composition, gamepad mapping, keyboard enumeration, enum state machine

## Summary
This chunk defines the Key struct and its associated enums (IsToggling, Modifiers, Requirement) with helper methods for name resolution, modifier satisfaction checks, and requirement state transitions.

## Explanation
The chunk declares pub const IsToggling as an enum with values never, no, yes. It defines pub const Modifiers as a packed struct(u6) containing shift, control, alt, super, capsLock, numLock fields each defaulting to false; includes methods toInt (bitCast), satisfiedBy (checks if required bits are present in actual via XOR and AND), isEmpty (tests zero). Requirement is an enum with always, inGame, inMenu values and a met method that returns true for always, uses isGrabbed for inGame, and negates isGrabbed for inMenu. The Key struct contains fields name ([]const u8), pressed (bool default false), isToggling (?IsToggling default never), modsOnPress (Modifiers default empty), value (f32 default 0.0), key (c_int default GLFW_KEY_UNKNOWN), gamepadAxis (?GamepadAxis default null), gamepadButton (c_int default -1), mouseButton (c_int default -1), scancode (c_int default 0), releaseAction (?*const fn (Modifiers) void default null), pressAction (?*const fn (Modifiers) void default null), repeatAction (?*const fn (Modifiers) void default null), notifyRequirement (Requirement default always), grabbedOnPress (bool default false), requiredModifiers (Modifiers default empty). Key exposes pub const IsToggling and Modifiers as nested enums. It defines getGamepadName(self: Key) []const u8 which first checks if gamepadAxis is non-null; if so, it extracts the positive flag and axis value, then uses a switch on axis to return localized stick names (Left stick right/left, Right stick right/left, Left stick down/up, Right stick down/up, Left trigger/trigger negative, Right trigger/trigger negative) or '(Invalid axis)' for unknown axes; if gamepadAxis is null it falls through to a switch on gamepadButton returning button labels (A/B/X/Y/Back/Down/Left/Right/Up/Guide/Left bumper/Left stick press/Right bumper/Right stick press/Start) or '(Unbound)' for -1 and '(Unrecognized button)' otherwise. The getName(self: Key) []const u8 method begins by checking if mouseButton == -1; if true it enters a switch on self.key returning English names for GLFW_KEY_SPACE, GLFW_KEY_GRAVE_ACCENT, GLFW_KEY_ESCAPE, GLFW_KEY_ENTER, GLFW_KEY_TAB, GLFW_KEY_BACKSPACE, GLFW_KEY_INSERT, GLFW_KEY_DELETE, GLFW_KEY_RIGHT, GLFW_KEY_LEFT, GLFW_KEY_DOWN, GLFW_KEY_UP.

## Related Questions
- How does the Modifiers struct compute whether a required modifier set is satisfied by an actual set?
- What are the default values for each field in the Key struct and how do they affect input state initialization?
- In getGamepadName, what happens when gamepadAxis is null versus when it contains a valid axis value?
- How does Requirement.met determine whether a key should be considered active based on grabbedOnPress?
- What localized names are returned for each GLFW_GAMEPAD_AXIS variant in the switch expression of getGamepadName?
- Which keyboard keys are mapped to English names by getName when mouseButton is -1 and key matches a known GLFW_KEY constant?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_2*
