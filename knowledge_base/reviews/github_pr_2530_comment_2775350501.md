# [src/server/permission.zig] - PR #2530 review diff

**Type:** review
**Keywords:** permissions, string hash map, zon element, deinit, arena allocator, white list, black list
**Symbols:** mapFromZon, mapToZon, Permissions, ListType, NeverFailingAllocator, NeverFailingArenaAllocator, ZonElement, User
**Concepts:** Resource Management, Memory Allocation, Data Structures, Initialization and Deinitialization

## Summary
Added new file `permission.zig` with functions for mapping between string hash maps and ZonElements, and a Permissions struct with initialization and deinitialization methods.

## Explanation
The added code introduces a new module for handling permissions in the server. It includes two main functions: `mapFromZon` and `mapToZon`, which facilitate converting between string hash maps and ZonElements. The `Permissions` struct manages permission lists using white and black lists, implemented as string hash maps. The reviewer notes that generally, any structure with a deinit function should also have an init function to ensure proper resource management, specifically mentioning the need for initializing the arena allocator.

## Related Questions
- What is the purpose of the `mapFromZon` function?
- How does the `Permissions` struct manage its internal state?
- Why is there a need for both white and black lists in the Permissions struct?
- What is the role of the `NeverFailingAllocator` in this module?
- How does the reviewer suggest improving the initialization process?
- Can you explain the difference between `NeverFailingAllocator` and `NeverFailingArenaAllocator`?

*Source: unknown | chunk_id: github_pr_2530_comment_2775350501*
