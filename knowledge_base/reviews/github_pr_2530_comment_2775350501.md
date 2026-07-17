# [src/server/permission.zig] - Chunk 2775350501

**Type:** review
**Keywords:** Permissions, deinit, init, arenaAllocator, whiteList, blackList, std.StringHashMapUnmanaged, NeverFailingArenaAllocator, lifecycle, allocation
**Symbols:** permission.zig, Permissions, ListType, white, black, arenaAllocator, permissionWhiteList, permissionBlackList, deinit
**Concepts:** resource initialization, memory arena allocation, struct lifecycle management, hashmap population, symmetry in API design

## Summary
The file introduces a new `permission.zig` module defining a `Permissions` struct with white/black list hashmaps and allocators, but lacks corresponding initialization logic.

## Explanation
Reviewers flagged that the newly added `deinit` function (and implicitly any future cleanup) requires a matching `init` function to properly construct the arena allocator and populate the permission maps. Without an init counterpart, resource allocation cannot be balanced, leading to potential leaks or undefined state when the struct is instantiated.

## Related Questions
- Where is the init function for Permissions defined?
- What arguments does the missing init require?
- How should arenaAllocator be initialized in init?
- Are permissionWhiteList and permissionBlackList populated in init?
- Does deinit need to check if maps are non-empty before freeing?
- Is there a pattern for init/deinit symmetry elsewhere in the codebase?

*Source: unknown | chunk_id: github_pr_2530_comment_2775350501*
