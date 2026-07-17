# [src/Inventory.zig] - PR #2469 review diff

**Type:** review
**Keywords:** memory allocation, double free, global allocator, stack allocator, command execution, inventory handling, lifetime management
**Symbols:** Inventory, DepositToAny, run, finalize, globalAllocator, stackAllocator
**Concepts:** memory management, thread safety, allocator usage

## Summary
The change updates the `DepositToAny` struct to handle multiple destination inventories and modifies memory allocation strategies.

## Explanation
The review highlights critical issues with memory management in the `DepositToAny` command. The original code used a stack allocator for potentially long-lived allocations, which is inappropriate as stack allocators are intended for short-lived local allocations. Additionally, freeing memory in the `run` function could lead to double frees if the command runs multiple times on the client side. The reviewer suggests using the global allocator instead and passing it as an argument to avoid hardcoding it. Furthermore, concerns about memory ownership and lifetime management arise, especially when dealing with data that might persist across multiple frames. The developer plans to explore solutions such as duplicating slices to ensure ownership but avoids doing so in certain contexts like `gui.zig`.

## Related Questions
- How does the use of `globalAllocator` instead of `stackAllocator` affect performance?
- What are the implications of passing allocators as arguments in this context?
- How can we ensure that memory ownership is correctly managed across multiple frames?
- What potential issues arise from duplicating slices to guarantee ownership?
- How does changing the allocator impact thread safety in this application?
- Can you explain the benefits and drawbacks of using `globalAllocator` for long-lived allocations?

*Source: unknown | chunk_id: github_pr_2469_comment_2674067299*
