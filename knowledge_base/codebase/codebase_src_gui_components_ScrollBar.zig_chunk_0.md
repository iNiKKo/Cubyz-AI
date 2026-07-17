# [easy/codebase_src_gui_components_ScrollBar.zig] - Chunk 0

**Type:** implementation
**Keywords:** scrollbar, texture binding, mouse anchor, clamp range, button press release, hover detection, global allocator, scissor rect
**Symbols:** ScrollBar, ScrollBar.globalInit, ScrollBar.globalDeinit, ScrollBar.init, ScrollBar.deinit, ScrollBar.toComponent, ScrollBar.setButtonPosFromValue, ScrollBar.updateValueFromButtonPos, ScrollBar.scroll, ScrollBar.updateHovered, ScrollBar.mainButtonPressed, ScrollBar.mainButtonReleased, ScrollBar.render
**Concepts:** GUI component lifecycle management, texture loading and binding, mouse-driven scrolling interaction, state clamping with min/max, event delegation to embedded Button

## Summary
Implements the ScrollBar GUI component, managing a draggable thumb button over a texture background to scroll content vertically.

## Explanation
The chunk defines the ScrollBar struct with fields for position (pos), size, current scroll state (currentState), an embedded Button pointer, and mouseAnchor. Initialization loads a scrollbar texture from assets/cubyz/ui/scrollbar.png via globalInit() and creates a Button using initText with empty label text; deinit releases both resources. The init function allocates the ScrollBar on main.globalAllocator, sets pos/size/currentState/button fields, adjusts button size to match scrollable range (height minus thumb height), and calls setButtonPosFromValue(). setButtonPosFromValue() computes the range as self.size[1] - self.button.size[1] and positions the button's Y coordinate at range * currentState. updateValueFromButtonPos() reads the button's Y position, divides by range to get a normalized value, and updates currentState only if different (prevents redundant state changes). scroll(offset) clamps the new currentState between 0 and 1 using @min/@max. Hover detection uses GuiComponent.contains on the button rectangle relative to self.pos; if hovered it delegates to button.updateHovered() which returns .handled or .ignored, otherwise returns .ignored. Main button press checks containment again; if handled it records mouseAnchor as mousePosition[1] - button.pos[1] and returns .handled. Release simply forwards to button.mainButtonReleased(). render binds the scrollbar texture to slot 0, sets scissor via Button.pipeline.bind(draw.getScissor()), draws a custom shaded rectangle using draw.customShadedRect with Button.buttonUniforms and self.pos/self.size, then calls setButtonPosFromValue() to sync thumb position. If button.pressed is true it updates button.pos[1] based on mouseAnchor (mousePosition[1] - mouseAnchor), clamps the result within [0, range - 0.001], re-syncs via updateValueFromButtonPos(), and finally renders the button with draw.setTranslation(self.pos) restored via defer.

## Code Example
```zig
pub fn scroll(self: *ScrollBar, offset: f32) void {
	self.currentState += offset;
	self.currentState = @min(1, @max(0, self.currentState));
}
```

## Related Questions
- How does ScrollBar clamp the current state value when scrolling?
- What happens to the button position when it is pressed during rendering?
- Which function is responsible for loading the scrollbar texture file?
- How is the normalized scroll value computed from the button's Y position?
- Does updateValueFromButtonPos modify currentState on every call or only when needed?
- What does setButtonPosFromValue compute as its range variable?
- How does ScrollBar delegate hover handling to its embedded Button?

*Source: unknown | chunk_id: codebase_src_gui_components_ScrollBar.zig_chunk_0*
