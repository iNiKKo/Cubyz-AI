# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** selection capabilities, ZonElement, duplication, allocator, world arena, memory efficiency
**Symbols:** register, zon, SelectionRule, SelectionCapability, loadSelectionCapabilitiesFromZon, main.stackAllocator, main.worldArena
**Concepts:** memory management, allocation strategy

## Summary
The change introduces a new field `_selectionCapabilities` to store block selection capabilities, loaded from a ZonElement. The reviewer suggests passing `main.worldArena` directly for allocation instead of duplicating.

## Explanation
**Explanation**

The code modification introduces a new field `_selectionCapabilities` to store block selection capabilities, which are loaded from a ZonElement. Specifically, the capabilities are loaded using `SelectionCapability.loadSelectionCapabilitiesFromZon(main.stackAllocator, capabilitiesZon)`. The current implementation then duplicates this array using `main.stackAllocator`, which is unnecessary and inefficient. By passing `main.worldArena` directly for allocation, the allocation can be more efficient and aligned with the intended memory management strategy of the application.

The `_selectionCapabilities` field is an optional array (`?[]SelectionCapability`). The code checks if `zon.getChildOrNull("selectionCapabilities")` returns a value before loading capabilities. If it does, the capabilities are loaded using `SelectionCapability.loadSelectionCapabilitiesFromZon(main.stackAllocator, capabilitiesZon)`. The duplicated array is then stored in `main.worldArena.allocator.dupe(SelectionCapability, capabilities) catch unreachable;`. This duplication is unnecessary and inefficient, as suggested by the reviewer.

The reviewer suggests that instead of duplicating the capabilities array, it should be allocated directly using `main.worldArena`. This change would eliminate the need for duplication and improve memory efficiency. The use of `main.worldArena` aligns with the overall memory management strategy in Cubyz, ensuring that allocations are managed consistently across the application.

The `_selectionCapabilities` field is used to store the selection capabilities of blocks, allowing for more flexible and dynamic block interactions based on their properties. By loading these capabilities from a ZonElement, the system can be easily extended or modified without changing the core codebase.

## Related Questions
-  How is `_selectionCapabilities` loaded from a ZonElement?
-  Why is duplicating the capabilities array unnecessary and inefficient?
-  What are the benefits of using `main.worldArena` for allocation instead of duplicating the array?

*Source: unknown | chunk_id: github_pr_2987_comment_3177694224*
