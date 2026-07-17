# [easy/codebase_src_gui_tooltip.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture initFromFile, Vec2f arithmetic, bound9SliceImage, setTranslation, restoreClip, calculateLineBreaks, GuiComponent.Label, toComponent
**Symbols:** tooltipTexture, cornerSize, fontSize, offsetFromMouse, globalInit, globalDeinit, render, renderFromText
**Concepts:** GUI rendering, tooltip subsystem, texture loading, window bounds clamping, component composition

## Summary
This chunk defines the tooltip subsystem: it loads a background texture, computes corner offsets, and provides global init/deinit hooks plus rendering functions that adapt to window bounds.

## Explanation
The chunk declares two module-level variables (tooltipTexture, cornerSize) and constants (fontSize, offsetFromMouse). It exposes three public functions. globalInit loads the tooltip background texture from assets/cubyz/ui/tooltip_background.png and derives cornerSize by subtracting a one-pixel border and halving the remaining size. globalDeinit calls deinit on the texture. render takes a GuiComponent pointer and mouse position, computes the final draw rectangle by adding corner offsets to the component size, checks window bounds (main.Window.getWindowSize scaled by gui.scale) and clamps/renderPos accordingly, then draws the background via draw.bound9SliceImage with the computed size and corners, applies an adjustment translation, saves/restore clip region, and finally calls guiComponent.render. renderFromText constructs a GuiComponent.Label from raw text, calculates line breaks using label.text.calculateLineBreaks at fontSize width 300, trims height to zero, expands width to max of all lines, converts the label to a component via label.toComponent, and delegates to render.

## Code Example
```zig
pub fn renderFromText(text: []const u8, pos: Vec2f) void {
	var label = GuiComponent.Label.init(Vec2f{0, 0}, 300, text, .left);
	defer label.deinit();
	var size = label.text.calculateLineBreaks(fontSize, 300);
	size[0] = 0;
	for (label.text.lineBreaks.items) |lineBreak| {
		size[0] = @max(size[0], lineBreak.width);
	}
	label.size = size;

	var component = label.toComponent();
	render(&component, pos);
}
```

## Related Questions
- What assets path is used for the tooltip background texture?
- How does renderFromText compute the final width of a multi-line tooltip?
- Which draw API call renders the tooltip background image with corner offsets?
- Where are translation and clip state saved/restored during render?
- What happens to renderPos when it would exceed window bounds on the right side?
- How is the vertical position adjusted if the tooltip exceeds the bottom of the window?
- Does globalInit perform any validation before loading the texture?
- Is cornerSize derived from the raw texture size or a scaled version?
- What type does render expect for its guiComponent argument?
- Are there any other public functions exposed by this chunk besides the three listed?

*Source: unknown | chunk_id: codebase_src_gui_tooltip.zig_chunk_0*
