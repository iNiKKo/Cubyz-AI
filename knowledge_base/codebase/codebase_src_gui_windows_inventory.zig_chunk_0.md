# [easy/codebase_src_gui_windows_inventory.zig] - Chunk 0

**Type:** implementation
**Keywords:** inventory, gui, slots, buttons, hotbar, crafting
**Symbols:** window, padding, craftingIcon, itemSlots
**Concepts:** GUI, Inventory, Hotbar, Crafting, ItemSlot

## Summary
Inventory GUI implementation

## Explanation
This chunk defines the inventory window for a game, including hotbar and crafting slots. It initializes the window size and position, creates item slots for each player's inventory, adds buttons for crafting and bag slots, and updates window positions after opening or closing.

## Code Example
```zig
pub fn init() void {
	craftingIcon = Texture.initFromFile("assets/cubyz/ui/inventory/crafting_icon.png");
}
```

## Related Questions
- What is the purpose of the `window` variable?
- How are item slots initialized and stored?
- Where does the crafting icon come from?
- What components are used to create the inventory window?
- How is the inventory window updated after opening or closing?
- What is the size of the inventory window?
- Where are the hotbar and crafting slots located within the inventory window?
- What buttons are added to the inventory window?
- How is the bag slot displayed in the inventory window?
- What is the default appearance of an item slot?
- What is the normal appearance of an item slot?
- What is the position of the inventory window relative to other components?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory.zig_chunk_0*
