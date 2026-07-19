# [src/Inventory.zig] - PR #2469 review diff

**Type:** review
**Keywords:** Inventory.zig, DepositToAny, stackAllocator, globalAllocator, double free, memory ownership, thread safety, allocator flexibility, command execution, slice duplication
**Symbols:** Inventory, Command, DepositToAny, Context, main.stackAllocator, globalAllocator
**Concepts:** thread safety, memory management, allocator usage, double free, memory ownership

## Summary
The change updates the `DepositToAny` struct to handle multiple destination inventories and uses the `globalAllocator` instead of `stackAllocator`. The reviewer points out potential issues with double free, allocator usage, and memory ownership.

## Explanation
The update introduces a new field `destinations` in the `DepositToAny` struct to allow depositing items into multiple inventories. The original code used a single destination inventory (`dest`). The reviewer highlights several critical concerns: using `stackAllocator` for persistent allocations across threads, potential double free issues due to repeated command execution on the client side, and unclear memory ownership when passing slices between different parts of the application. The reviewer suggests changing the allocator usage to be more flexible and context-aware, possibly by passing allocators as parameters and duplicating slices to ensure ownership. The developer acknowledges these concerns and plans to revisit the code with a focus on proper memory management and thread safety.

The `DepositToAny` struct now includes a field `destinations: []Inventory`, which is an array of destination inventories. This allows items to be deposited into multiple inventories instead of just one. The original check for specific inventory types (`creative`, `crafting`, `workbench`) has been removed, as the new logic handles multiple destinations.

The reviewer points out that using `stackAllocator` for persistent allocations across threads can lead to double free issues if the allocation is freed more than once. Instead, the developer should use `globalAllocator`, which is designed for longer-lived allocations and is thread-safe. The reviewer also suggests passing allocators as parameters rather than hardcoding them, allowing for greater flexibility in allocator usage.

Memory ownership is a concern when passing slices between different parts of the application. The reviewer recommends duplicating slices to ensure that each part has its own copy and owns the memory. This prevents issues related to double free and ensures that memory is properly managed across different threads.

## Related Questions
- How does the `DepositToAny` struct handle multiple destination inventories?
- What are the potential issues with using `stackAllocator` in this context?
- Why is it important to avoid double free in command execution?
- How should allocators be passed and used in this code?
- What strategies can be employed to ensure memory ownership when passing slices?
- How does changing to `globalAllocator` address the original concerns?

*Source: unknown | chunk_id: github_pr_2469_comment_2674067299*
