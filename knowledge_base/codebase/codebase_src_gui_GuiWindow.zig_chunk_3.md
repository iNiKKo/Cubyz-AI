# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 3

**Type:** implementation
**Keywords:** mouse position, window dragging, snapping, relative positioning, title bar, hover detection, minimum size, orientation lines
**Symbols:** update, updateSelected, updateHovered, getMinWindowWidth, updateWindowPosition, drawOrientationLines, drawIcons
**Concepts:** GUI window lifecycle, mouse interaction handling, window dragging and snapping, relative positioning to frame or other windows, title bar hover detection, minimum window width enforcement, orientation line drawing for debugging

## Summary
Chunk defines the GuiWindow struct's update/updateSelected/updateHovered/getMinWindowWidth and drawOrientationLines/drawIcons methods.

## Explanation
The chunk declares pub fn update(self: *GuiWindow) void which calls self.updateFn(); pub fn updateSelected(self: *GuiWindow, mousePosition: Vec2f) void which invokes self.updateSelectedFn(), computes windowSize via main.Window.getWindowSize()/@as(Vec2f,@splat(gui.scale)), handles grabbedWindow/windowMoving with a blk block that sets relativePosition to undefined ratio, resets pos using (mousePosition - _grabPosition) + selfPositionWhenGrabbed, calls self.snapToOtherWindow(), conditionally calls positionRelativeToFrame or positionRelativeToConnectedWindow based on which relativePosition field is .ratio, clamps pos with @max/@min, and updates gui via gui.updateWindowPositions() and gui.save(); it also recursively calls component.updateSelected() if self.rootComponent exists. pub fn updateHovered(self: *GuiWindow, mousePosition: Vec2f) main.callbacks.Result computes scaledMousePos, checks titleBarHeight against showTitleBar or gui.reorderWindows, delegates to titleBar.updateHovered if present and returns .handled; otherwise calls self.updateHoveredFn() and returns its result; then recurses into rootComponent via GuiComponent.contains and component.updateHovered returning .handled; finally returns .ignored if hasBackground is false. pub fn getMinWindowWidth(self: *GuiWindow) f32 returns iconWidth*@as(f32,(if (self.closeable) 4 else 3)). pub fn updateWindowPosition(self: *GuiWindow) void computes minSize via self.getMinWindowWidth(), logs and expands contentSize[0] if below minSize, scales size with gui.scale, iterates over self.relativePosition fields using inline for and switch on .ratio/.attachedToFrame/.attachedToWindow/.relativeToWindow to compute pos[i] based on windowSize or other window positions; after the loop it floors pos to prevent floating point inaccuracies and clamps both axes. fn drawOrientationLines(self: *const GuiWindow) void sets oldColor via draw.setColor(0x80000000), defers restoreColor, computes windowSize, iterates over self.relativePosition with inline for _continue; switch on .ratio/.relativeToWindow breaks the loop; .attachedToFrame draws a line from pos to opposite edge using i ^ 1; .attachedToWindow draws a vertical/horizontal line between self and other based on attachment points. pub fn drawIcons(self: *const GuiWindow) void computes x = self.size[0]/self.scale, subtracts iconWidth if closeable, then renders closeTexture at (x,0).

## Code Example
```zig
pub fn updateHovered(self: *GuiWindow, mousePosition: Vec2f) main.callbacks.Result {
	const scaledMousePos = (mousePosition - self.pos)/@as(Vec2f, @splat(self.scale));
	if (scaledMousePos[1] < titleBarHeight and (self.showTitleBar or gui.reorderWindows)) {
		_ = if (self.titleBar) |titleBar| titleBar.updateHovered(scaledMousePos);
		return .handled;
	}
	if (self.updateHoveredFn() == .handled) return .handled;
	if (self.rootComponent) |component| {
		if (GuiComponent.contains(component.pos(), component.size(), scaledMousePos)) {
			if (component.updateHovered(scaledMousePos) == .handled) return .handled;
		}
	}
	if (self.hasBackground) return .handled;
	return .ignored;
}
```

## Related Questions
- What does updateHovered return when the mouse is over the title bar?
- How are window positions clamped after being computed from relativePosition fields?
- Which function is called to render the close icon texture and where is it positioned?
- Does drawOrientationLines handle both attachedToFrame and attachedToWindow cases?
- What happens if self.rootComponent exists during updateSelected?
- How does getMinWindowWidth decide between 4 or 3 units for the minimum width?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_3*
