# [medium/codebase_src_gui_windows_controls.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, Button, ContinuousSlider, CheckBox, settings save, user interaction, layout initialization
**Symbols:** window, padding, selectedKey, editingKeyboard, needsUpdate, keyFunction, keypressListener, gamepadFunction, gamepadListener, updateSensitivity, invertMouseYCallback, sprintIsToggleCallback, updateDeadzone, deadzoneFormatter, sensitivityFormatter, abortBindingProcess, toggleKeyboard, unbindKey, initWindow
**Concepts:** GUI window, game controls configuration, key bindings, sensitivity settings

## Summary
This chunk defines the logic for a GUI window that allows users to configure game controls, including key bindings and sensitivity settings.

## Explanation
The code initializes a `GuiWindow` with a vertical list of components such as buttons, sliders, and checkboxes. It handles user interactions for setting up keyboard and gamepad controls, updating sensitivities, and saving changes to the settings. Functions like `keyFunction`, `gamepadFunction`, and `updateSensitivity` manage the binding process and update the settings accordingly. The `initWindow` function sets up the layout of the window with various components, including labels, buttons for key bindings, and sliders for adjusting sensitivities.

## Code Example
```zig
fn abortBindingProcess() void {
	selectedKey = null;
	main.Window.resetNextInputListenters();
	needsUpdate = true;
}
```

## Related Questions
- What is the purpose of the `abortBindingProcess` function?
- How does the `initWindow` function set up the GUI layout?
- What components are added to the vertical list in the `initWindow` function?
- How are key bindings updated when a user selects a new key or gamepad button?
- What is the role of the `updateSensitivity` function in the code?
- How does the code handle saving changes to the settings after updating them?

*Source: unknown | chunk_id: codebase_src_gui_windows_controls.zig_chunk_0*
