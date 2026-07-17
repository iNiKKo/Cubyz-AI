# [src/game.zig] - PR #2003 review diff

**Type:** review
**Keywords:** inventory management, slot checking, hotbar handling, network traffic optimization, item duplication prevention
**Symbols:** Player, inventory.getItem, isCreative, main.gui.windowlist.inventory.itemSlots.len, main.gui.windowlist.hotbar.itemSlots.len, selectedSlot, Inventory.init, carried.deinit
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The code now checks for item slots in both the inventory and hotbar, updating the selected slot logic accordingly.

## Explanation
The change involves modifying the loop to iterate over all item slots in both the inventory and hotbar. It includes additional logic to handle items being in the hotbar separately from those in the inventory. The reviewer points out a critical architectural concern: creating a copy of an already open inventory, which causes unnecessary network traffic.

## Related Questions
- Why is the loop iterating over both inventory and hotbar slots?
- What is the purpose of the `blk` block in the code?
- How does the code handle cases where no empty slot is found in the hotbar?
- What potential issues could arise from copying an already open inventory?
- How does this change impact performance, especially with larger inventories?
- Is there a risk of memory leaks introduced by the new `Inventory.init` and `deinit` calls?

*Source: unknown | chunk_id: github_pr_2003_comment_2433739215*
