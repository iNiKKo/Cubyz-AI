# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, callbacks, settings update, formatter functions, array of options
**Symbols:** window, padding, renderDistances, lodValues, anisotropy, resolutions, leavesQualities, fpsPresetsValue, fpsPresetsText, fpsCapGetIndex, fpsCapCallback, renderDistanceCallback, highestLodCallback, leavesQualityCallback, fovCallback, fovFormatter, lodDistanceFormatter, lodDistanceCallback, contrastFormatter, contrastCallback, nightBrightnessCallback, nightBrightnessFormatter, bloomCallback, vsyncCallback, anisotropicFilteringCallback, resolutionScaleCallback
**Concepts:** GUI settings window, user interface components, settings management, callback functions, text formatting

## Summary
This chunk defines a GUI window for graphics settings with various sliders and checkboxes to adjust rendering parameters.

## Explanation
The code initializes a `GuiWindow` named `window` with specific content size and behavior. It declares several arrays of configuration options such as render distances, LOD values, anisotropy levels, resolutions, leaves qualities, FPS presets, and more. The chunk includes callback functions for each setting to update the corresponding settings in the `settings` module when a user interacts with the GUI components. These callbacks handle saving changes and reloading resources where necessary. Additionally, there are formatter functions that generate display text for certain settings values.

## Code Example
```zig
fn fpsCapGetIndex(fpsOptional: ?u32) u16 {
	const fps: u16 = @truncate(fpsOptional orelse return fpsPresetsValue.len);
	return @intCast(std.sort.lowerBound(u16, &fpsPresetsValue, fps, struct {
		fn order(a: u16, b: u16) std.math.Order {
			return std.math.order(a, b);
		}
	}.order));
}
```

## Related Questions
- What is the purpose of the `fpsCapGetIndex` function?
- How does the `renderDistanceCallback` function update settings?
- What formatter function is used for displaying FOV values?
- How are changes to anisotropic filtering applied in the code?
- What happens when a user adjusts the resolution scale setting?
- How are FPS presets stored and displayed in the GUI?

*Source: unknown | chunk_id: codebase_src_gui_windows_graphics.zig_chunk_0*
