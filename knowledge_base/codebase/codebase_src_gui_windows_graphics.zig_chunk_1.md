# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 1

**Type:** api
**Keywords:** vertical list, sliders, checkboxes, settings initialization, component deinitialization
**Symbols:** onOpen, onClose
**Concepts:** GUI settings management, user interface components, graphical settings adjustment

## Summary
Handles the initialization and cleanup of GUI components for window graphics settings.

## Explanation
The chunk defines two functions, `onOpen` and `onClose`, which manage the setup and teardown of a vertical list containing various sliders and checkboxes for adjusting graphical settings. The `onOpen` function initializes a `VerticalList` and populates it with different types of sliders and checkboxes based on the current settings stored in the `settings` variable. It also sets up callbacks for each component to handle user interactions. The `onClose` function deinitializes the root component if it exists, ensuring proper cleanup.

## Code Example
```zig
pub fn onClose() void {
	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What function initializes the GUI components for window graphics settings?
- How does the chunk handle user interactions with graphical settings?
- What is the purpose of the `onClose` function in this chunk?
- Which components are added to the vertical list in the `onOpen` function?
- How are callbacks set up for each component in the GUI?
- What happens if there is no world loaded when initializing the GUI components?

*Source: unknown | chunk_id: codebase_src_gui_windows_graphics.zig_chunk_1*
