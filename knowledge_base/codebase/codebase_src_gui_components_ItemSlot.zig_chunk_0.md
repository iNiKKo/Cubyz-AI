# [medium/codebase_src_gui_components_ItemSlot.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture management, item quantity display, hover detection, button press handling, global initialization, deinitialization
**Symbols:** ItemSlot, ItemSlot.border, ItemSlot.sizeWithBorder, ItemSlot.Mode, ItemSlot.pos, ItemSlot.size, ItemSlot.inventory, ItemSlot.itemSlot, ItemSlot.lastItemAmount, ItemSlot.text, ItemSlot.textSize, ItemSlot.hovered, ItemSlot.pressed, ItemSlot.renderFrame, ItemSlot.texture, ItemSlot.mode, ItemSlot.defaultTexture, ItemSlot.immutableTexture, ItemSlot.craftingResultTexture, ItemSlot.TextureParamType, ItemSlot.globalInit, ItemSlot.globalDeinit, ItemSlot.init, ItemSlot.deinit, ItemSlot.refreshText, ItemSlot.toComponent, ItemSlot.updateHovered, ItemSlot.mainButtonPressed, ItemSlot.mainButtonReleased
**Concepts:** GUI components, inventory management, user interaction handling, text rendering

## Summary
The ItemSlot component handles the rendering and interaction logic for inventory slots in the GUI.

## Explanation
The ItemSlot component handles the rendering and interaction logic for inventory slots in the GUI. It includes methods for initialization, deinitialization, text refreshment, and handling user interactions such as hovering and button presses. The component uses textures to visually represent different states of the slot: default (`assets/cubyz/ui/inventory/slot.png`), immutable (`assets/cubyz/ui/inventory/immutable_slot.png`), or crafting result (`assets/cubyz/ui/inventory/crafting_result_slot.png`). It also manages text rendering for displaying item quantities within the slot. The `border` variable is set to 2, and the size of an ItemSlot with border is defined as `32 + 2*border`. This ensures that each slot has a consistent appearance and functionality.

The `Mode` enum defines three modes: `normal`, `takeOnly`, and `immutable`. The `init` method initializes an `ItemSlot` instance, setting its position (`pos`), size (`size`), inventory reference (`inventory`), item slot index (`itemSlot`), text buffer (`text`), texture (`texture`), and mode (`mode`). The `deinit` method deinitializes the `ItemSlot` by deleting references, deinitializing the text buffer, and destroying the instance. The `refreshText` method updates the text displayed in an ItemSlot by checking if the item amount has changed. If it has, it deinitializes the current text buffer, creates a new one with the updated amount, and recalculates the text size.

The textures used to represent different states of an ItemSlot are initialized globally using the `globalInit` function, which loads the appropriate images from the assets directory: default (`assets/cubyz/ui/inventory/slot.png`), immutable (`assets/cubyz/ui/inventory/immutable_slot.png`), and crafting result (`assets/cubyz/ui/inventory/crafting_result_slot.png`). Memory for ItemSlot instances is managed through the use of Zig's allocator, where memory is allocated during initialization and deallocated during deinitialization.

The `updateHovered` method sets the `hovered` flag to true and updates the global hovered item slot reference when the mouse hovers over an ItemSlot. The `mainButtonPressed` method sets the `pressed` flag to true when a button is pressed, and the `mainButtonReleased` method resets the `pressed` flag when a button is released.

The `toComponent` method converts an `ItemSlot` instance into a `GuiComponent`, allowing it to be used within the GUI system.

The `TextureParamType` union allows for different types of textures, including default, immutable, crafting result, invisible, and custom. The `value` function returns the appropriate texture based on the type specified.

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
