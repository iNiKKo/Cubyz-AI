# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, DiscreteSlider, ContinuousSlider, CheckBox, callback functions, settings update, user interaction
**Symbols:** window, padding, renderDistances, lodValues, anisotropy, resolutions, leavesQualities, fpsPresetsValue, fpsPresetsText, fpsCapGetIndex, fpsCapCallback, renderDistanceCallback, highestLodCallback, leavesQualityCallback, fovCallback, fovFormatter, lodDistanceFormatter, lodDistanceCallback, contrastFormatter, contrastCallback, nightBrightnessCallback, nightBrightnessFormatter, bloomCallback, vsyncCallback, anisotropicFilteringCallback, resolutionScaleCallback, onOpen
**Concepts:** GUI settings window, user interface components, configuration management, settings persistence

## Summary
This chunk defines the GUI window for graphics settings, initializing various sliders and checkboxes to adjust rendering parameters.

## Explanation
The code initializes a `GuiWindow` with specific content size and behavior. It defines several arrays of configuration options for different settings like render distance, LOD values, anisotropy levels, resolutions, and FPS presets. Functions handle callbacks for each setting change, updating the global `settings` object and saving them. The `onOpen` function sets up a `VerticalList` containing various UI components such as `DiscreteSlider`, `ContinuousSlider`, and `CheckBox` to allow users to interactively adjust graphics settings.

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
- What components are added to the `VerticalList` in the `onOpen` function?
- How are FPS presets formatted and displayed in the GUI?
- What happens when a user changes the anisotropic filtering setting?
- How is the night brightness setting formatted in the GUI?

*Source: unknown | chunk_id: codebase_src_gui_windows_graphics.zig_chunk_0*
