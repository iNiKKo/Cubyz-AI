# [src/server/permission.zig] - Chunk 2775469276

**Type:** review
**Keywords:** HashMapUnmanaged, std.StringHashMap, deprecated, allocator, memory management, permission.zig, unmanaged maps, dedicated allocator, leak prevention, architectural consistency
**Symbols:** std.StringHashMap, HashMapUnmanaged, NeverFailingAllocator, Permissions, PermissionGroup, permissionWhiteList, permissionBlackList, addPermission, removePermission
**Concepts:** memory management, deprecated API usage, unmanaged hash maps, dedicated allocator pattern, architectural consistency, leak prevention, server-side permissions

## Summary
The review critiques the use of `std.StringHashMap` in permission.zig, recommending replacement with `HashMapUnmanaged` paired with a dedicated allocator to align with Cubyz's memory management strategy and avoid deprecated APIs.

## Explanation
The reviewer points out that the current implementation uses `std.StringHashMap`, which is marked as deprecated. The architectural direction for Cubyz favors unmanaged hash maps (`HashMapUnmanaged`) combined with explicit allocators, ensuring better control over memory lifetimes and avoiding reliance on internal allocator management. Additionally, the reviewer suggests that keys should be allocated from this same dedicated allocator rather than relying on default heap behavior. This change improves consistency across the codebase, reduces potential leaks or double-free scenarios, and aligns permission storage with other parts of the server that already use unmanaged maps and arena allocators.

## Related Questions
- What is the current type used for permissionWhiteList and permissionBlackList in permission.zig?
- Why does the reviewer suggest using HashMapUnmanaged instead of std.StringHashMap?
- How should keys be allocated according to the review comment?
- Which allocator is recommended to replace the default heap allocation for permission keys?
- What benefits does switching to unmanaged maps provide in Cubyz's architecture?
- Are there any other parts of the codebase that already use HashMapUnmanaged with a dedicated allocator?
- How would changing from std.StringHashMap affect memory safety guarantees?
- Is there a migration path suggested for existing permission entries when switching map types?
- What implications does this change have on performance or allocation patterns?
- Does the review mention any specific deprecation warnings associated with std.StringHashMap?

*Source: unknown | chunk_id: github_pr_2530_comment_2775469276*
