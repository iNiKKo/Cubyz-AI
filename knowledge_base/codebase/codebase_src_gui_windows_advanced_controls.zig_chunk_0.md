# [easy/codebase_src_gui_windows_advanced_controls.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, slider controls, callback functions, window lifecycle, setting persistence
**Symbols:** window, padding, delayCallback, delayFormatter, speedCallback, speedFormatter, onOpen, onClose
**Concepts:** GUI window management, user interface controls, settings adjustment

## Summary
Defines a GUI window for advanced controls with sliders for delay and speed settings.

## Explanation
This chunk defines a GUI window named 'window' that contains advanced control components such as ContinuousSliders for adjusting repeat delay and speed. The `onOpen` function initializes these components, sets up their callbacks and formatters, and positions them within the window. The `onClose` function deinitializes the root component when the window is closed. The chunk also imports various GUI components and settings from other modules.

## Code Example
```zig
fn delayCallback(newValue: f32) void {
	settings.updateRepeatDelay.nanoseconds = @trunc(newValue);
	settings.save();
}
```

## Related Questions
- What is the purpose of the `delayCallback` function?
- How does the `onOpen` function initialize the GUI components?
- What happens when the window is closed according to the `onClose` function?
- Which settings are being adjusted in this GUI window?
- How are the slider values formatted and displayed?
- What is the role of the `padding` constant in the layout?

*Source: unknown | chunk_id: codebase_src_gui_windows_advanced_controls.zig_chunk_0*
