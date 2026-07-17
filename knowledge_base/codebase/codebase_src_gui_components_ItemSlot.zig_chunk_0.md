# [medium/codebase_src_gui_components_ItemSlot.zig] - Chunk 0

**Type:** implementation
**Keywords:** ItemSlot, TextureParamType, globalInit, deinit, refreshText, updateHovered, mainButtonPressed, render, hover callbacks, button press/release
**Symbols:** ItemSlot, Mode, TextureParamType
**Concepts:** GUI component rendering, inventory slot management, texture binding, hover callbacks, button press/release handling, text buffer allocation, global allocator usage, defer cleanup pattern

## Summary
Implements the ItemSlot GUI component for rendering inventory slots with texture support, hover/press callbacks, and stack-size text.

## Explanation
The chunk defines a public struct ItemSlot that encapsulates an inventory slot's position, size, item reference, last-known amount, rendered text buffer, hover/press state flags, render-frame flag, optional texture, and mode (normal/takeOnly/immutable). It declares three global textures (default, immutable, craftingResult) initialized once via globalInit() and cleaned up in globalDeinit(). The init() function allocates an ItemSlot on the global allocator, copies the inventory's amount into self.*, builds a TextBuffer with right-aligned numeric text (or '∞' if allocation fails), computes line breaks for sizing, and resolves the texture via TextureParamType.value(). deinit() removes references from the GUI system, frees the text buffer, and destroys the slot. refreshText() updates the displayed amount only when it changed; it reallocates a new TextBuffer with color red (0xff0000) if empty else white, recomputes line breaks, and stores the last amount to avoid redundant work. toComponent() wraps self into a GuiComponent for the GUI system. updateHovered() sets hovered=true and registers self as gui.hoveredItemSlot; mainButtonPressed() sets pressed=true; mainButtonReleased() clears pressed if it was set. render() refreshes text, binds the texture (if present) and draws the slot background via draw.boundImage(), then renders the item itself using item.render(). It computes whether to show stack-size text based on item.stackSize()>1 and inventory.type!=.creative, positioning the text at the right edge minus border. If mode is not immutable and the slot was hovered, it sets hovered=false and begins a color change (draw.setColor(0x300000ff)) with a defer to restore the previous color.

## Code Example
```zig
pub fn mainButtonReleased(self: *ItemSlot, _: Vec2f) void {
	if (self.pressed) {
		self.pressed = false;
	}
}
```

## Related Questions
- How does ItemSlot handle the case where an item is null in the inventory?
- What happens to the hovered flag when a user moves away from an ItemSlot during render?
- Under what conditions is stack-size text rendered for an ItemSlot?
- Which global textures are initialized and how are they resolved via TextureParamType?
- How does refreshText avoid unnecessary reallocations when the item amount hasn't changed?
- What is the purpose of the defer draw.restoreColor(oldColor) in render?
- Does ItemSlot support any mode that prevents texture rendering entirely?
- Where are references to an ItemSlot removed from the GUI system on deinit?
- How does init compute the correct size for the text buffer given border padding?
- What return value does updateHovered provide and why is it marked handled?
- Can mainButtonReleased be called without first calling mainButtonPressed?
- Is there any logic to handle multiple presses before release in ItemSlot?

*Source: unknown | chunk_id: codebase_src_gui_components_ItemSlot.zig_chunk_0*
