# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 1

**Type:** api
**Keywords:** vertical list, sliders, checkboxes, settings initialization, component deinitialization
**Symbols:** onOpen, onClose
**Concepts:** GUI settings management, user interface components, graphical settings adjustment

## Summary
Handles the initialization and cleanup of GUI components for window graphics settings.

## Explanation
The chunk defines two functions, `onOpen` and `onClose`, which manage the setup and teardown of a vertical list containing various sliders and checkboxes for adjusting graphical settings. The `onOpen` function initializes a `VerticalList` and populates it with different types of sliders and checkboxes based on specific values stored in the `settings` variable. It also sets up callbacks for each component to handle user interactions, including:

- **FPS Limit:** A discrete slider ranging from 0 to 128.
- **LOD1 Distance:** A discrete slider with a value of `@min(@max(settings.renderDistance, renderDistances[0]) - renderDistances[0], renderDistances.len - 1)` in chunks.
- **Highest LOD:** If the world is null, a discrete slider ranging from 0 to settings.highestSupportedLod.
- **Leaves Quality (TODO: requires reload):** A discrete slider with a value of `settings.leavesQuality - leavesQualities[0]`.
- **LOD0.5 Distance:** A continuous slider with no specific range given in the code, but it is initialized with settings.lod0.5Distance and has a callback for handling user interactions.
- **Block Contrast:** A continuous slider ranging from 0.0 to 0.5.
- **Night Brightness:** A continuous slider ranging from 0.0 to 1.0.
- **Field of View (FOV):** A continuous slider ranging from 40.0 to 120.0.
- **Bloom:** A checkbox with a value based on settings.bloom.
- **Vertical Synchronization (VSync):** A checkbox with a value based on settings.vsync.
- **Anisotropic Filtering:** A discrete slider ranging from 1x to 16x, mapped as follows: `switch (settings.anisotropicFiltering) { 1 => 0, 2 => 1, 4 => 2, 8 => 3, 16 => 4, else => 2 }`.
- **Resolution Scale:** A discrete slider with a value of `@as(u16, @trunc(@log2(settings.resolutionScale) + 2.0))`, representing the resolution scale in percentage.

The `onClose` function deinitializes the root component if it exists, ensuring proper cleanup.

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
