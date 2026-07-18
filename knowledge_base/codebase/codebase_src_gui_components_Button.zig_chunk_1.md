# [medium/codebase_src_gui_components_Button.zig] - Chunk 1

**Type:** api
**Keywords:** texture binding, shaded rectangle, 9-slice image, color manipulation, child component rendering
**Symbols:** Button, Button.render, Vec2f, disabledTextures, pressedTextures, hoveredTextures, normalTextures
**Concepts:** GUI rendering, button states, mouse interaction

## Summary
The `Button` component handles rendering based on its state and mouse interactions.

## Explanation
The `render` function of the `Button` struct determines which textures to use based on whether the button is disabled, pressed, or hovered. It binds the appropriate texture and draws a shaded rectangle with rounded corners using custom shaders. The function also updates the position of any child component (like text) relative to the button's position and renders it. The color for drawing is set conditionally based on the button's disabled state, and the original color is restored afterward.

## Code Example
```zig
pub fn render(self: *Button, mousePosition: Vec2f) void {
	const textures = blk: {
		if (self.disabled) break :blk disabledTextures;
		if (self.pressed) break :blk pressedTextures;
		if (GuiComponent.contains(self.pos, self.size, mousePosition) and self.hovered) {
			break :blk hoveredTextures;
		}
		break :blk normalTextures;
	};
	{
		textures.texture.bindTo(0);
		pipeline.bind(draw.getScissor());
		self.hovered = false;
		draw.customShadedRect(buttonUniforms, self.pos + Vec2f{2, 2}, self.size - Vec2f{4, 4});
	}

	const cornerSize = (textures.outlineTextureSize - Vec2f{1, 1})/Vec2f{2, 2};

	textures.outlineTexture.bindTo(0);
	graphics.draw.bound9SliceImage(self.pos, self.size, textures.outlineTextureSize, cornerSize, 2);

	const oldColor = draw.setColor(if (self.disabled) 0xff808080 else 0xffffffff);
	defer draw.restoreColor(oldColor);
	const textPos = self.pos + self.size/@as(Vec2f, @splat(2.0)) - self.child.size()/@as(Vec2f, @splat(2.0));
	self.child.mutPos().* = textPos;
	self.child.render(mousePosition - self.pos);
}
```

## Related Questions
- What textures are used for different button states?
- How is the button's hover state determined?
- What shader is used to draw the shaded rectangle?
- How is the position of child components updated?
- What happens if the button is disabled?
- How are colors manipulated during rendering?

*Source: unknown | chunk_id: codebase_src_gui_components_Button.zig_chunk_1*
