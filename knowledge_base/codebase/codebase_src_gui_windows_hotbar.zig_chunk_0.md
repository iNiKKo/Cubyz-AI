# [easy/codebase_src_gui_windows_hotbar.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, HorizontalList, ItemSlot, player inventory, hotbar texture, mutex lock, HUD positioning, content size update, deinit cleanup
**Symbols:** window, hotbarSlotTexture, itemSlots, init, deinit, onOpen, onClose, update
**Concepts:** GUI window management, horizontal list layout, inventory slot rendering, texture loading, mutex locking for player state

## Summary
This chunk defines the hotbar GUI window, initializing a horizontal list of 12 item slots with custom textures and binding them to player inventory state.

## Explanation
The chunk declares a global GuiWindow instance named 'window' configured as an HUD element positioned at the middle-upper attachment points with content size 64x12 pixels, no title bar or background. It imports ItemStack, Player, Vec2f, and Texture from main modules, plus GuiComponent types (HorizontalList, ItemSlot, Icon) and the parent gui module. A global hotbarSlotTexture variable is initialized in init() by loading 'assets/cubyz/ui/inventory/hotbar_slot.png'. The onOpen() function creates a HorizontalList, iterates 0..12 to instantiate ItemSlot objects with position (0,0), referencing Player.inventory and the current slot index cast to int, using hotbarSlotTexture as custom texture and normal style; each is added to the list. After finishing the list at center anchor, it assigns the resulting component to window.rootComponent and updates contentSize via rootComponent.size(). onClose() safely deinitializes the root component if present. update() acquires Player.mutex (locking before, unlocking in defer), sets hovered=true on the slot corresponding to Player.selectedSlot.

## Related Questions
- What is the default content size of the hotbar window?
- How are item slots initialized in onOpen()?
- Which texture file is loaded for hotbar slots?
- Does the window have a title bar or background by default?
- How does update() handle player selection state?
- What happens to rootComponent when onClose() runs?
- Is itemSlots an array of pointers or values?
- Where is Player.mutex declared and used here?
- Can the hotbar be closed programmatically via this chunk?
- How does HorizontalList.finish anchor its content?

*Source: unknown | chunk_id: codebase_src_gui_windows_hotbar.zig_chunk_0*
