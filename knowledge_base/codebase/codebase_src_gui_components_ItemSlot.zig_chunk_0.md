# [medium/codebase_src_gui_components_ItemSlot.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture management, item quantity display, hover detection, button press handling, global initialization, deinitialization
**Symbols:** ItemSlot, ItemSlot.border, ItemSlot.sizeWithBorder, ItemSlot.Mode, ItemSlot.pos, ItemSlot.size, ItemSlot.inventory, ItemSlot.itemSlot, ItemSlot.lastItemAmount, ItemSlot.text, ItemSlot.textSize, ItemSlot.hovered, ItemSlot.pressed, ItemSlot.renderFrame, ItemSlot.texture, ItemSlot.mode, ItemSlot.defaultTexture, ItemSlot.immutableTexture, ItemSlot.craftingResultTexture, ItemSlot.TextureParamType, ItemSlot.globalInit, ItemSlot.globalDeinit, ItemSlot.init, ItemSlot.deinit, ItemSlot.refreshText, ItemSlot.toComponent, ItemSlot.updateHovered, ItemSlot.mainButtonPressed, ItemSlot.mainButtonReleased
**Concepts:** GUI components, inventory management, user interaction handling, text rendering

## Summary
The ItemSlot component handles the rendering and interaction logic for inventory slots in the GUI.

## Explanation
This chunk defines the `ItemSlot` struct, which represents an individual slot in a graphical user interface (GUI) inventory. It includes methods for initialization, deinitialization, text refreshment, and handling user interactions such as hovering and button presses. The component uses textures to visually represent different states of the slot, such as default, immutable, or crafting result slots. It also manages text rendering for displaying item quantities within the slot.

## Code Example
```zig
pub fn globalInit() void {
	defaultTexture = Texture.initFromFile("assets/cubyz/ui/inventory/slot.png");
	immutableTexture = Texture.initFromFile("assets/cubyz/ui/inventory/immutable_slot.png");
	craftingResultTexture = Texture.initFromFile("assets/cubyz/ui/inventory/crafting_result_slot.png");
}
```

## Related Questions
- What is the purpose of the `globalInit` function in the ItemSlot component?
- How does the `refreshText` method update the text displayed in an ItemSlot?
- What textures are used to represent different states of an ItemSlot?
- How does the ItemSlot handle user interactions like hovering and button presses?
- What is the role of the `toComponent` method in the ItemSlot struct?
- How is memory managed for ItemSlot instances, particularly during initialization and deinitialization?

*Source: unknown | chunk_id: codebase_src_gui_components_ItemSlot.zig_chunk_0*
