# [easy/codebase_src_gui_windows_advanced_controls.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, slider controls, callback functions, window lifecycle, setting persistence
**Symbols:** window, padding, delayCallback, delayFormatter, speedCallback, speedFormatter, onOpen, onClose
**Concepts:** GUI window management, user interface controls, settings adjustment

## Summary
Defines a GUI window named 'window' with ContinuousSliders for adjusting repeat delay and speed settings. The window has a fixed content size of (128, 256) and contains sliders that adjust settings.updateRepeatDelay.nanoseconds and settings.updateRepeatSpeed.nanoseconds within specified ranges.

## Explanation
This chunk defines a GUI window named 'window' with a fixed content size of Vec2f{128, 256}. The `onOpen` function initializes two ContinuousSliders for adjusting repeat delay and speed. The first slider adjusts the settings.updateRepeatDelay.nanoseconds value within the range of 1.0e6 to 1.0e9 nanoseconds (1ms to 1s). The second slider adjusts the settings.updateRepeatSpeed.nanoseconds value within the range of 1.0e6 to 0.5e9 nanoseconds (1ms to 500ms). Each slider has a callback function (`delayCallback` and `speedCallback`) that updates the corresponding setting and saves it, as well as a formatter function (`delayFormatter` and `speedFormatter`) that formats the displayed value in milliseconds. The padding constant is set to 8 for layout purposes. The `onClose` function deinitializes the root component when the window is closed.

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
