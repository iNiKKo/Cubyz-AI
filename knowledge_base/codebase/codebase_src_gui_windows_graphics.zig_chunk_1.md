# [medium/codebase_src_gui_windows_graphics.zig] - Chunk 1

**Type:** api
**Keywords:** VerticalList, DiscreteSlider, ContinuousSlider, resolutionScale, fpsCap, renderDistance, highestLod, leavesQuality, lod0.5Distance, blockContrast, nightBrightness, fov, bloom, vsync, anisotropicFiltering
**Symbols:** resolutionScaleCallback, onOpen, onClose
**Concepts:** GUI configuration panel, graphics settings UI, resolution scaling, FPS limiting, LOD distance sliders, quality toggles, bloom effect, vertical synchronization, anisotropic filtering, field of view adjustment

## Summary
This chunk defines the GUI window initialization and configuration panel for graphics settings, including resolution scale, FPS limit, LOD distances, quality toggles, bloom, vsync, anisotropic filtering, and FOV adjustments.

## Explanation
The chunk declares a public function onOpen that constructs a VerticalList containing multiple DiscreteSlider and ContinuousSlider components bound to various settings fields (resolutionScale, fpsCap, renderDistance, highestLod, leavesQuality, lod0.5Distance, blockContrast, nightBrightness, fov, bloom, vsync, anisotropicFiltering). Each slider is initialized with a label string, the current value derived from settings via helper functions or inline logic, and a callback function (e.g., resolutionScaleCallback, fpsCapCallback) that updates settings and triggers side effects like saving or framebuffer resizing. The onOpen function also conditionally adds the highest LOD slider only if main.game.world is null, finishes the list centered, assigns it to window.rootComponent, computes window.contentSize based on component positions and padding, and calls gui.updateWindowPositions(). A separate public function onClose deinitializes the rootComponent if present. Additionally, a standalone resolutionScaleCallback updates settings.resolutionScale using std.math.pow with @floatFromInt conversion, saves settings, and invokes main.Window.GLFWCallbacks.framebufferSize to resize the framebuffer.

## Related Questions
- What happens when main.game.world is null during onOpen?
- How does resolutionScaleCallback compute the new scale value from an integer input?
- Which settings fields are directly modified by the sliders in onOpen?
- What side effect occurs after updating resolutionScale in resolutionScaleCallback?
- Why is the highest LOD slider conditionally added only when main.game.world is null?
- How does onClose handle cleanup of the GUI window component?
- What is the purpose of gui.updateWindowPositions() called at the end of onOpen?
- Which callback functions are passed to each DiscreteSlider in the configuration list?
- How is the current index for anisotropic filtering determined before passing it to its slider?
- Does any slider in this chunk trigger a texture reload or mesh update?

*Source: unknown | chunk_id: codebase_src_gui_windows_graphics.zig_chunk_1*
