# [src/game.zig] - PR #2003 review diff

**Type:** review
**Keywords:** inventory management, slot handling, network traffic optimization, item duplication prevention, hotbar inventory, architectural review
**Symbols:** Player, inventory.getItem, isCreative, selectedSlot, main.gui.windowlist.inventory.itemSlots.len, main.gui.windowlist.hotbar.itemSlots.len, Inventory.init, carried.deinit
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The code now checks if the item is in the hotbar or inventory and handles it accordingly, avoiding unnecessary inventory copies.

## Explanation
**Explanation**

The reviewer points out a critical architectural issue where creating a copy of an already open inventory causes unnecessary network traffic. The change iterates through all possible slots (hotbar and inventory) to find the item's location and handle it appropriately without duplicating the inventory.

- **Handling Items in Hotbar**: If the item is found in the hotbar, the `selectedSlot` is directly updated to point to that slot.

- **Handling Items in Inventory**: If the item is found in the inventory, the code first checks if the currently selected slot (`selectedSlot`) is empty. If it is, this slot is used as the target slot for the item. If not, the code iterates through the hotbar slots to find an empty one. If no empty slot is found in the hotbar, the currently selected slot is used.

- **`blk` Block**: The `blk` block is a labeled block that determines the target slot for the item. It checks if the current `selectedSlot` is empty and uses it as the target slot if true. Otherwise, it iterates through the hotbar slots to find an empty one. If no empty slot is found in the hotbar, it defaults back to using the currently selected slot.

- **Network Traffic Minimization**: The code ensures that network traffic is minimized by avoiding unnecessary inventory copies. It checks if there is already a slot with the same item type and handles it accordingly without duplicating the inventory.

**Code Snippet**
```zig
for(0..(main.gui.windowlist.inventory.itemSlots.len + main.gui.windowlist.hotbar.itemSlots.len)) |slotIdx| {
    if(std.meta.eql(inventory.getItem(slotIdx), item)) {
        if(slotIdx < (main.gui.windowlist.hotbar.itemSlots.len)) {
            // when item is in hotbar
            selectedSlot = @intCast(slotIdx);
        } else {
            // when item is in inventory
            const targetSlot = blk: {
                if(inventory.getItem(selectedSlot) == null) break :blk selectedSlot;
                // Look for an empty slot
                for(0..main.gui.windowlist.hotbar.itemSlots.len) |slotId| {
                    if(inventory.getItem(slotId) == null) {
                        break :blk slotId;
                    }
                }
                break :blk selectedSlot;
            };
            var carried: Inventory = undefined;
            carried = Inventory.init(main.globalAllocator, 1, .normal, .{.hand = main.game.Player.id}, .{});
            defer carried.deinit(main.globalAllocator);
        }
    }
}
```

**CRITICAL ARCHITECTURAL REVIEW**: Please don't create a copy of an already open inventory. This just causes needless network traffic.

## Related Questions
- Why is it important to avoid creating a copy of an already open inventory?
- How does the code handle items located in different slots (hotbar and inventory)?
- What is the purpose of the `blk` block in the code?
- How does the code ensure that network traffic is minimized?
- What are the potential implications if the inventory copy logic is not handled correctly?
- How can we verify that this change prevents unnecessary inventory copies?

*Source: unknown | chunk_id: github_pr_2003_comment_2433739215*
