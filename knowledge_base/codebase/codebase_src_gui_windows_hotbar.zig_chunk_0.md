# [easy/codebase_src_gui_windows_hotbar.zig] - Chunk 0

**Type:** api
**Keywords:** texture initialization, component creation, state update, mutex locking, inventory access
**Symbols:** window, hotbarSlotTexture, itemSlots, init, deinit, onOpen, onClose, update
**Concepts:** GUI window management, Item slot handling, Player inventory interaction

## Summary
Manages the hotbar GUI window, including initialization, deinitialization, and updating item slots.

## Explanation
This chunk defines a hotbar GUI window for the Cubyz game. It initializes textures, creates item slots, and updates the selected slot's hover state. The `init` function loads the texture for hotbar slots, while `deinit` releases it. The `onOpen` method sets up the horizontal list of item slots, attaching them to the player's inventory. The `onClose` method deinitializes components when the window is closed. The `update` function highlights the currently selected slot by setting its hover state.

## Code Example
```zig
pub fn init() void {
	hotbarSlotTexture = Texture.initFromFile("assets/cubyz/ui/inventory/hotbar_slot.png");
}
```

## Related Questions
- What texture is used for hotbar slots?
- How many item slots are in the hotbar?
- What method initializes the hotbar window?
- How does the chunk handle deinitialization of resources?
- Which player component is accessed during updates?
- What happens when the hotbar window is opened?
- How is the selected slot highlighted in the hotbar?
- What mutex is used to protect inventory access?
- Where are the item slots stored in memory?
- How does the chunk update the GUI positions?

*Source: unknown | chunk_id: codebase_src_gui_windows_hotbar.zig_chunk_0*
