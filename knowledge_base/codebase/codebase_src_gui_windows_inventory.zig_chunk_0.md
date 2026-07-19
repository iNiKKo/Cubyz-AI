# [easy/codebase_src_gui_windows_inventory.zig] - Chunk 0

**Type:** implementation
**Keywords:** inventory, hotbar, slots, buttons, init, deinit
**Symbols:** window, padding, craftingIcon, itemSlots
**Concepts:** inventory window, layout management, item slots, buttons

## Summary
Inventory window initialization and management

## Explanation
This chunk initializes the inventory window, including its layout with a hotbar reference, content size, scale, and HUD status. It also manages item slots and buttons for crafting and other items. The `window` variable is defined with relative position attached to the hotbar window's middle point, content size of 640x192 pixels (64*10 by 64*3), scale of 0.75, and it is marked as a HUD element that cannot be closed. The inventory window initializes item slots using a vertical list structure with padding of 8 units. It includes a bag slot and a crafting icon button linked to the 'inventory_crafting' window. The `init` function loads the crafting icon texture from 'assets/cubyz/ui/inventory/crafting_icon.png'. The `deinit` function deinitializes the crafting icon texture. The inventory window is composed of 20 item slots arranged in a vertical list with 3 rows and 10 columns, starting from index 12. Each slot is initialized with a specific position, player inventory reference, index, default settings, and normal mode.

## Code Example
```zig
pub fn init() void {
	craftingIcon = Texture.initFromFile("assets/cubyz/ui/inventory/crafting_icon.png");
}
```

## Related Questions
- What is the purpose of the `window` variable in this chunk?
- How does the inventory window manage its content size and scale?
- What are the initial contents of the inventory slots?
- What is the function responsible for initializing the crafting icon?
- What is the function responsible for deinitializing the crafting icon?
- What is the purpose of the `itemSlots` array in this chunk?
- How does the inventory window handle bag slots and crafting buttons?

*Source: unknown | chunk_id: codebase_src_gui_windows_inventory.zig_chunk_0*
