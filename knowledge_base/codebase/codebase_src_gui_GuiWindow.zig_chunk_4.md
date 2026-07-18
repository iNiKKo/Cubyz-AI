# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 4

**Type:** implementation
**Keywords:** rendering pipeline, texture binding, shader application, child components, mouse interaction
**Symbols:** GuiWindow, render
**Concepts:** GUI rendering, window management, component rendering

## Summary
Handles rendering of a GUI window, including background, title bar, and child components.

## Explanation
The `render` function manages the drawing process for a GUI window. It checks if the window should be hidden based on mouse grab state. It saves current translation and scale settings, then applies the window's position and scale. If the window has a background or title bar, it binds textures and draws them using custom shaders. The function calls `renderFn` for any additional rendering logic specific to the window. It also renders child components if they exist, adjusting their mouse positions relative to the window. After rendering, it restores the original translation and scale settings. If the window is being moved, it draws orientation lines.

## Code Example
```zig
pub fn render(self: *const GuiWindow, mousePosition: Vec2f) void {
	if (self.hideIfMouseIsGrabbed and main.Window.grabbed) return;
	const oldTranslation = draw.setTranslation(self.pos);
	const oldScale = draw.setScale(self.scale);
	if (self.hasBackground) {
		pipeline.bind(draw.getScissor());
		backgroundTexture.bindTo(0);
		draw.customShadedRect(windowUniforms, .{0, 0}, self.size/@as(Vec2f, @splat(self.scale)));
	}
	self.renderFn();
	if (self.rootComponent) |*component| {
		component.render((mousePosition - self.pos)/@as(Vec2f, @splat(self.scale)));
	}
	if (self.showTitleBar or gui.reorderWindows) {
		pipeline.bind(draw.getScissor());
		titleTexture.bindTo(0);
		draw.customShadedRect(windowUniforms, .{0, 0}, .{self.size[0]/self.scale, titleBarHeight});
		self.drawIcons();
	}
	if (self.hasBackground or (!main.Window.grabbed and gui.reorderWindows)) {
		const oldColor = draw.setColor(0xff2d2d2d);
		defer draw.restoreColor(oldColor);
		draw.rectBorder(.{-2, -2}, self.size/@as(Vec2f, @splat(self.scale)) + Vec2f{4, 4}, 2.0);
	}
	draw.restoreTranslation(oldTranslation);
	draw.restoreScale(oldScale);
	if (self == grabbedWindow and windowMoving and (gui.reorderWindows or self.showTitleBar) and grabPosition != null) {
		self.drawOrientationLines();
	}
}
```

## Related Questions
- What does the `render` function check before rendering the window?
- How does the function handle background and title bar rendering?
- What is the purpose of calling `renderFn` in the `render` function?
- How are child components rendered within the GUI window?
- What steps does the function take to restore the drawing state after rendering?
- When does the function draw orientation lines during rendering?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_4*
