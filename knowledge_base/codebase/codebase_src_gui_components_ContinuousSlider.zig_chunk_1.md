# [medium/codebase_src_gui_components_ContinuousSlider.zig] - Chunk 1

**Type:** implementation
**Keywords:** rendering, texture binding, pipeline usage, color manipulation, translation, mouse interaction, value updating
**Symbols:** ContinuousSlider, ContinuousSlider.render, texture.bindTo, Button.pipeline.bind, draw.getScissor, draw.customShadedRect, Button.buttonUniforms, self.pos, self.size, draw.setColor, draw.restoreColor, draw.rect, self.getBarPos, self.getBarSize, self.label.pos, self.label.render, self.button.pressed, mousePosition, self.mouseAnchor, @min, @max, self.updateValueFromButtonPos, draw.setTranslation, draw.restoreTranslation, self.button.render
**Concepts:** GUI component, slider interaction, mouse input handling

## Summary
The ContinuousSlider component renders a slider with a button that can be moved along a bar, updating its value based on mouse interaction.

## Explanation
This chunk defines the rendering logic for a ContinuousSlider GUI component. It binds a texture and pipeline, draws the slider's background, and then draws the bar and label. If the button is pressed, it updates the button's position based on mouse movement and recalculates the slider's value. The function also handles color and translation settings to ensure proper rendering.

## Code Example
```zig
pub fn render(self: *ContinuousSlider, mousePosition: Vec2f) void {
	texture.bindTo(0);
	Button.pipeline.bind(draw.getScissor());
	draw.customShadedRect(Button.buttonUniforms, self.pos, self.size);

	{
		const oldColor = draw.setColor(0x80000000);
		defer draw.restoreColor(oldColor);
		draw.rect(self.pos + self.getBarPos(), self.getBarSize());
	}

	self.label.pos = self.pos + @as(Vec2f, @splat(1.5*border));
	self.label.render(mousePosition);

	if (self.button.pressed) {
		self.button.pos[0] = mousePosition[0] - self.mouseAnchor;
		self.button.pos[0] = @min(@max(self.button.pos[0], 1.5*border), 1.5*border + self.getBarSize()[0] - 0.001);
		self.updateValueFromButtonPos();
	}
	const oldTranslation = draw.setTranslation(self.pos);
	defer draw.restoreTranslation(oldTranslation);
	self.button.render(mousePosition - self.pos);
}
```

## Related Questions
- How does the ContinuousSlider update its value based on mouse interaction?
- What is the purpose of `draw.setTranslation` and `draw.restoreTranslation` in the render function?
- How does the ContinuousSlider handle rendering the bar and label?
- What role does `self.getBarPos` and `self.getBarSize` play in the rendering process?
- How does the ContinuousSlider ensure that the button stays within the bounds of the bar?
- What is the sequence of operations for rendering the slider's background, bar, and label?

*Source: unknown | chunk_id: codebase_src_gui_components_ContinuousSlider.zig_chunk_1*
