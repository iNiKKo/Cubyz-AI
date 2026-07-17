# [src/Inventory.zig] - Chunk 2677575375

**Type:** review
**Keywords:** DepositToAny, destinations, owned, allocator, free, defer, Inventory, dupe, slice, type check, memory leak, ownership
**Symbols:** DepositToAny, destinations, owned, source, amount, run, Context, Inventory, InventoryAndSlot
**Concepts:** memory ownership, allocator semantics, defer cleanup, slice allocation, dupe prevention, type checking, resource management

## Summary
The DepositToAny command was refactored to accept multiple destination inventories via a slice instead of a single target, and introduced an 'owned' flag that tracks whether the allocated destinations were already provided by the caller; this change also ensures the command always operates on owned data to prevent dupe bugs.

## Explanation
Previously, DepositToAny stored a single Inventory pointer in 'dest', with type checks rejecting creative, crafting, and workbench inventories. The reviewer flagged that switching to an allocator for destinations (now a []Inventory) required careful ownership semantics: if the caller supplies the slice, we must not free it; if we allocate internally, we must free on exit. The diff adds a 'defer' block that frees self.destinations only when owned is true, indicating the command allocated them. Additionally, the reviewer noted an earlier dupe bug where the command sometimes operated on non-owned data; by always ensuring ownership (via the allocator path), the code now guarantees correct behavior and prevents memory leaks or double-free errors.

## Related Questions
- What is the type of 'destinations' in DepositToAny after the change?
- How does the defer block ensure proper cleanup when owned is true?
- Why was a single Inventory replaced with []Inventory in this command?
- What prior bug related to dupe prevention prompted this ownership fix?
- Does the new implementation still reject creative, crafting, and workbench inventories?
- Where is the allocation of 'destinations' performed if owned is false initially?
- Is there any path where self.destinations could be freed twice after this change?
- What happens to the original 'dest' field when switching to a slice-based destination?
- How does the reviewer’s comment about ‘always be owned’ affect error handling in run()?
- Are there any other commands that need similar ownership adjustments for slices?
- Does this change impact performance due to extra allocation overhead on every deposit?
- What is the expected behavior if a caller passes an empty []Inventory slice?

*Source: unknown | chunk_id: github_pr_2469_comment_2677575375*
