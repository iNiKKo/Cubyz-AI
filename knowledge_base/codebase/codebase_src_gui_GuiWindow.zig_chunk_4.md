# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 4

**Type:** implementation
**Keywords:** drawing lines, icon rendering, background drawing, translation, scaling
**Symbols:** GuiWindow, drawOrientationLines, drawIcons, render
**Concepts:** GUI rendering, window management, icon display, background textures

## Summary
Handles rendering of GUI windows, including drawing lines, icons, and background textures.

## Explanation
This chunk contains methods for rendering a GUI window. The `drawOrientationLines` method draws orientation lines based on the window's position and size. The `drawIcons` method renders icons such as close, zoom in, and zoom out buttons. The `render` method is the main rendering function that handles background drawing, component rendering, title bar rendering, and border drawing. It also manages translation and scaling for proper positioning.

## Code Example
```zig
pub fn drawIcons(self: *const GuiWindow) void {
	var x = self.size[0]/self.scale;
	if (self.closeable) {
		x -= iconWidth;
		closeTexture.render(.{x, 0}, .{iconWidth, titleBarHeight});
	}
	x -= iconWidth;
	zoomOutTexture.render(.{x, 0}, .{iconWidth, titleBarHeight});
	x -= iconWidth;
	zoomInTexture.render(.{x, 0}, .{iconWidth, titleBarHeight});

	const oldClip = graphics.draw.setClip(.{x, titleBarHeight});
	defer graphics.draw.restoreClip(oldClip);
	if (self.titleBar) |titleBar| titleBar.render(.{0, 0});
}
```

## Related Questions
- How does the `drawOrientationLines` method determine where to draw lines?
- What icons are rendered by the `drawIcons` method?
- What is the purpose of the `render` method in this chunk?
- How does the `render` method handle background drawing?
- What conditions control the rendering of the title bar and border?
- How does the `render` method manage translation and scaling?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_4*
