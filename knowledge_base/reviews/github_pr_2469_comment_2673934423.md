# [src/Inventory.zig] - PR #2469 review diff

**Type:** review
**Keywords:** double free, stackAllocator, memory leak, thread safety, allocator passing, ownership tracking
**Symbols:** DepositToAny, destinations, owned, Inventory, main.stackAllocator
**Concepts:** memory management, thread safety, allocator usage

## Summary
The code modifies the `DepositToAny` struct to accept multiple destination inventories and adds a flag for ownership. The reviewer points out potential issues with memory management, suggesting changes to prevent double frees and improve allocator usage.

## Explanation
The change introduces a new field `destinations`, which is an array of `Inventory` objects instead of a single `Inventory`. This allows the command to deposit items into multiple destinations. The `owned` flag indicates whether the struct should manage the memory of the `destinations` array. However, the reviewer highlights several critical issues: using `defer` with `main.stackAllocator.free(self.destinations)` can lead to double frees if the command runs multiple times on the client side. Additionally, the use of `stackAllocator` for non-local allocations is discouraged as it may cause memory corruption across different threads. The reviewer suggests that the allocator should be passed by the caller instead of being hardcoded. Furthermore, there are concerns about who owns the memory when the struct is used over multiple frames, and how to track such ownership correctly.

## Related Questions
- How can we ensure that the `DepositToAny` command does not cause double frees when run multiple times?
- What are the implications of using `stackAllocator` for non-local allocations in a multi-threaded environment?
- How should the allocator be passed to avoid hardcoding it within the struct?
- What strategies can be employed to track memory ownership correctly over multiple frames?
- Can you provide an example of how to refactor the code to prevent double frees and improve allocator usage?
- How does the introduction of multiple destinations affect the performance of the `DepositToAny` command?

*Source: unknown | chunk_id: github_pr_2469_comment_2673934423*
