# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, callbacks, settings update, formatter functions, array of options
**Symbols:** window, padding, renderDistances, lodValues, anisotropy, resolutions, leavesQualities, fpsPresetsValue, fpsPresetsText, fpsCapGetIndex, fpsCapCallback, renderDistanceCallback, highestLodCallback, leavesQualityCallback, fovCallback, fovFormatter, lodDistanceFormatter, lodDistanceCallback, contrastFormatter, contrastCallback, nightBrightnessCallback, nightBrightnessFormatter, bloomCallback, vsyncCallback, anisotropicFilteringCallback, resolutionScaleCallback
**Concepts:** GUI settings window, user interface components, settings management, callback functions, text formatting

## Summary
This chunk defines a GUI window for graphics settings with various sliders and checkboxes to adjust rendering parameters.

## Explanation
This chunk defines a GUI window named `window` with content size of (128, 256) and behavior to close if the mouse is grabbed. It declares several arrays for configuration options: render distances (`renderDistances`) ranging from 5 to 24 in increments of 1; LOD values (`lodValues`) as strings representing levels from '0.5' to '9'; anisotropy levels (`anisotropy`) with values [1, 2, 4, 8, 16]; resolutions (`resolutions`) at 25, 50, and 100; leaves qualities (`leavesQualities`) from 0 to 4; FPS presets (`fpsPresetsValue`) ranging from 5 to 360 in increments of 5 with an 'unlimited' option. The chunk includes callback functions for each setting to update the corresponding settings in the `settings` module when a user interacts with GUI components, handling saving changes and reloading resources where necessary. Additionally, there are formatter functions that generate display text for certain settings values.

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
- What are the specific FPS presets stored and displayed in the GUI?

*Source: unknown | chunk_id: codebase_src_gui_windows_graphics.zig_chunk_0*
