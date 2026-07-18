# [easy/codebase_src_gui_tooltip.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture initialization, position calculation, 9-slice rendering, text rendering, screen bounds checking
**Symbols:** tooltipTexture, cornerSize, fontSize, offsetFromMouse, globalInit, globalDeinit, render, renderFromText
**Concepts:** GUI rendering, 9-slice image technique, tooltip management

## Summary
Handles tooltip rendering in the GUI system.

## Explanation
This chunk manages the initialization and deinitialization of a tooltip texture, as well as rendering tooltips based on either a pre-existing GUI component or text input. The `fontSize` is set to 16 pixels, and the `offsetFromMouse` is set to 4 pixels from the mouse position. It calculates positions to ensure tooltips do not go off-screen by adjusting their placement relative to the window size using screen bounds checking logic within the `render` function. Specifically, if the tooltip's calculated position would cause it to exceed the window dimensions, its position is adjusted accordingly. The `cornerSize` is calculated as half of the difference between the texture's dimensions minus one pixel in each direction divided by two, ensuring smooth corners for the tooltip background. The exact calculation for `cornerSize` is given by: `(@as(Vec2f, @floatFromInt(tooltipTexture.size())) - Vec2f{1, 1})/Vec2f{2, 2}`.

## Code Example
```zig
pub fn globalInit() void {
	tooltipTexture = Texture.initFromFile("assets/cubyz/ui/tooltip_background.png");
	cornerSize = (@as(Vec2f, @floatFromInt(tooltipTexture.size())) - Vec2f{1, 1})/Vec2f{2, 2};
}
```

## Related Questions
- How is the tooltip texture initialized?
- What does the `render` function do with the position of the tooltip?
- How is text rendered into a tooltip using `renderFromText`?
- What happens during the global deinitialization of tooltips?
- How is the 9-slice image technique applied in rendering?
- What adjustments are made to ensure tooltips stay on-screen?

*Source: unknown | chunk_id: codebase_src_gui_tooltip.zig_chunk_0*
