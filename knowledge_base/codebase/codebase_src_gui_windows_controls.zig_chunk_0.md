# [medium/codebase_src_gui_windows_controls.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, Button, ContinuousSlider, CheckBox, settings save, user interaction, layout initialization
**Symbols:** window, padding, selectedKey, editingKeyboard, needsUpdate, keyFunction, keypressListener, gamepadFunction, gamepadListener, updateSensitivity, invertMouseYCallback, sprintIsToggleCallback, updateDeadzone, deadzoneFormatter, sensitivityFormatter, abortBindingProcess, toggleKeyboard, unbindKey, initWindow
**Concepts:** GUI window, game controls configuration, key bindings, sensitivity settings

## Summary
This chunk defines a GUI window for configuring game controls with specific layout dimensions, components like buttons, sliders, checkboxes, and functions to handle user interactions for setting up keyboard and gamepad controls, updating sensitivities, and saving changes to the settings.

## Explanation
This chunk defines a GUI window for configuring game controls with specific layout dimensions, components like buttons, sliders, checkboxes, and functions to handle user interactions for setting up keyboard and gamepad controls, updating sensitivities, and saving changes to the settings.

The code initializes a `GuiWindow` with a content size of `(128, 192)` pixels. It includes padding of `8` f32 units and sets `closeIfMouseIsGrabbed` to true. The window contains components such as buttons, sliders, checkboxes, labels, and horizontal lists for managing key bindings and sensitivity settings.

The `keyFunction`, `keypressListener`, `gamepadFunction`, and `gamepadListener` functions handle the binding process for keyboard keys and gamepad inputs. The `updateSensitivity` function adjusts mouse or controller sensitivity based on user input from a continuous slider, while `invertMouseYCallback` and `sprintIsToggleCallback` manage settings related to inverting mouse Y-axis and toggling sprint mode.

The `initWindow` function sets up the layout of the window with components like buttons for switching between keyboard and gamepad controls, sliders for adjusting sensitivity (with a range from 0 to 5 for mouse and 0 to 1 for controller), checkboxes for setting options, and labels for displaying key names. It also includes a loop that iterates over all keys in `main.KeyBoard.keys`, adding buttons and unbind buttons for each key or gamepad button.

The window layout is initialized with specific dimensions and padding values, ensuring proper placement of components within the window.

## Code Example
```zig
fn abortBindingProcess() void {
	selectedKey = null;
	main.Window.resetNextInputListenters();
	needsUpdate = true;
}
```

## Related Questions
- What are the exact dimensions of the GuiWindow?
- How does the `initWindow` function initialize the vertical list with buttons, sliders, checkboxes, and labels?
- What is the purpose of the `keyFunction`, `keypressListener`, `gamepadFunction`, and `gamepadListener` functions?
- How are sensitivity settings updated using the continuous slider in the GUI window?
- What specific components are added to the vertical list for managing key bindings and gamepad controls?

*Source: unknown | chunk_id: codebase_src_gui_windows_controls.zig_chunk_0*
