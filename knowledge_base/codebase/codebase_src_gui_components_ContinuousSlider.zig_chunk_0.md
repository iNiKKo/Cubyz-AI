# [medium/codebase_src_gui_components_ContinuousSlider.zig] - Chunk 0

**Type:** api
**Keywords:** GUI slider, button handling, label management, memory allocation, texture usage, mouse interactions
**Symbols:** ContinuousSlider, ContinuousSlider.border, ContinuousSlider.fontSize, ContinuousSlider.texture, ContinuousSlider.pos, ContinuousSlider.size, ContinuousSlider.minValue, ContinuousSlider.maxValue, ContinuousSlider.callback, ContinuousSlider.formatter, ContinuousSlider.currentValue, ContinuousSlider.currentText, ContinuousSlider.label, ContinuousSlider.button, ContinuousSlider.mouseAnchor, ContinuousSlider.globalInit, ContinuousSlider.globalDeinit, ContinuousSlider.init, ContinuousSlider.deinit, ContinuousSlider.toComponent, ContinuousSlider.setButtonPosFromValue, ContinuousSlider.updateLabel, ContinuousSlider.updateValueFromButtonPos, ContinuousSlider.updateHovered, ContinuousSlider.getBarPos, ContinuousSlider.getBarSize, ContinuousSlider.mainButtonPressed, ContinuousSlider.mainButtonReleased
**Concepts:** GUI component, slider interaction, value updating, callback triggering

## Summary
The ContinuousSlider component manages a slider GUI element with a button and label, handling user interactions to update values and trigger callbacks.

## Explanation
This chunk defines the ContinuousSlider struct, which represents a GUI slider component. It includes methods for initialization (`init`), deinitialization (`deinit`), updating the button position based on value (`setButtonPosFromValue`), updating the label text (`updateLabel`), and handling mouse interactions (`mainButtonPressed`, `mainButtonReleased`). The slider uses a texture for its background, and its value is constrained between a minimum and maximum. The component also manages memory allocation and deallocation using a global allocator.

## Code Example
```zig
pub fn globalInit() void {
	texture = Texture.initFromFile("assets/cubyz/ui/slider.png");
}
```

## Related Questions
- How does the ContinuousSlider initialize its texture?
- What is the purpose of the `setButtonPosFromValue` method?
- How does the ContinuousSlider handle mouse button release events?
- What role does the formatter function play in the ContinuousSlider?
- How is memory managed within the ContinuousSlider component?
- What conditions trigger the callback function in the ContinuousSlider?

*Source: unknown | chunk_id: codebase_src_gui_components_ContinuousSlider.zig_chunk_0*
