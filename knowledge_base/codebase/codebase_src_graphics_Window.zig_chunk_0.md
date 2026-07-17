# [hard/codebase_src_graphics_Window.zig] - Chunk 0

**Type:** implementation
**Keywords:** gamepad, deadzone, joystick, controller, keyboard mapping, virtual mouse, cursor visibility, GLFW callbacks, memory allocation, state tracking
**Symbols:** Gamepad, Gamepad.gamepadState, Gamepad.controllerMappingsDownloaded, Gamepad.applyDeadzone, Gamepad.applyDeadzones2D, Gamepad.update, Gamepad.isControllerConnected, Gamepad.wereControllerMappingsDownloaded
**Concepts:** gamepad input handling, deadzone normalization, joystick state tracking, keyboard to gamepad mapping, virtual mouse emulation, cursor visibility control, GLFW callbacks integration, memory allocation for controller states

## Summary
Manages GLFW window state, gamepad input handling with deadzone application, and keyboard-to-gamepad mapping updates.

## Explanation
The chunk declares public mutable fields for window dimensions (width, height), fullscreen state, mouse usage tracking, and a map of joystick states keyed by ID. It imports Vulkan and C bindings via main modules. The Gamepad struct contains an AutoHashMap of GLFWgamepadstate pointers and an atomic flag for controller mappings download status. Two helper functions applyDeadzone and applyDeadzones2D normalize analog axes using configurable deadzone values from settings; they compute sign, subtract the deadzone floor, divide by the remaining range, and optionally renormalize to unit length if magnitude exceeds 1. The update function iterates over all joysticks present via GLFW callbacks, storing old state snapshots before reading new states. For each joystick it checks presence and gamepad flag; if a new controller appears it allocates memory for its state struct (using main.globalAllocator) and inserts into the map; if removed it frees the previous allocation and deletes from the map. After populating or removing entries, it applies deadzone corrections to all axes and triggers. It then notifies any registered nextGamepadListener of button releases (transition 0→1 in oldState) and axis activations (non‑zero newAxis with zero oldAxis), passing either a null event for buttons or an AxisEvent struct for axes. Keyboard integration is performed by iterating main.KeyBoard.keys; entries without a gamepadAxis are ignored, while those with a button mapping compare pressed states and call key.setPressed if the state changed. For axis mappings it flips sign according to positive flag, clamps both old and new values to [0,1], compares thresholds (>0.5) for press detection, updates setPressed on change, and writes the analog value into key.value when different. When not grabbed, it computes virtual mouse deltas from UI keys (uiLeft/right/up/down), accumulates position in GLFWCallbacks.currentPos with scaling by delta*256, clamps to window bounds via getWindowSize(), and forwards scroll input through GLFWCallbacks.scroll using scrollUp/down keys scaled by delta*4. Cursor visibility is set based on grabbed state and lastUsedMouse flag.

## Related Questions
- How does the chunk detect a newly connected controller and allocate memory for its state?
- What is the exact sequence of operations inside Gamepad.update when iterating over joysticks?
- How are deadzone values applied to analog axes in applyDeadzones2D, including renormalization logic?
- Under what conditions does nextGamepadListener receive a button release event versus an axis activation event?
- What is the role of main.KeyBoard.keys iteration and how does key.setPressed get invoked for gamepad buttons?
- How are virtual mouse deltas computed from UI keys when grabbed is false, and how are they clamped to window bounds?
- Why does the chunk set cursor visibility based on both grabbed and lastUsedMouse flags?
- What happens to a joystick state entry in Gamepad.gamepadState when the physical controller is removed?
- How does wereControllerMappingsDownloaded use an atomic flag, and what order guarantees are implied?
- In applyDeadzone, how is the sign of the input value preserved after subtracting the deadzone floor?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_0*
