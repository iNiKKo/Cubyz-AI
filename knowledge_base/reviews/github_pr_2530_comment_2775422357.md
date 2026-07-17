# [src/server/permission.zig] - Chunk 2775422357

**Type:** review
**Keywords:** arena, free, leak, NeverFailingArenaAllocator, Permissions, removePermission, slice, hash map, threadContext, assertCorrectContext, do nothing, denial of service, bytes, Zig
**Symbols:** Permissions, addPermission, removePermission, NeverFailingArenaAllocator, sync.threadContext
**Concepts:** arena allocator semantics, memory leak tolerance, thread safety context assertion, hash map key removal, denial of service mitigation

## Summary
The reviewer notes that freeing memory from an arena allocator is impossible; instead of attempting a free on a slice allocated by the arena, the code should simply ignore it since leaking a few bytes here is acceptable and not a security concern.

## Explanation
In Zig, `NeverFailingArenaAllocator` provides memory that cannot be freed individually—only the entire arena can be deallocated at once. Attempting to call `.free(slice)` on a slice obtained from such an allocator will panic or corrupt state because the underlying storage is managed by the arena’s internal bookkeeping. The reviewer correctly identifies this as a logical error: the `removePermission` function tries to free the key slice after removing it from the hash map, but that slice was allocated via the arena (or its backing allocator), not the regular heap allocator used for normal frees. Since the performance impact of leaking these few bytes is negligible and an attacker would need to repeatedly add and remove permissions over hours to cause a denial-of-service by exhausting memory, the pragmatic fix is to drop the free call entirely. This preserves correctness without introducing unnecessary complexity or risking crashes.

## Related Questions
- What is the difference between NeverFailingAllocator and NeverFailingArenaAllocator in this codebase?
- Why does removePermission attempt to free a slice after removing it from the hash map?
- How does sync.threadContext.assertCorrectContext(.server) protect permission modifications?
- Is there any scenario where leaking arena memory would be unacceptable for the server?
- What happens if we try to call .free on a pointer allocated by an arena allocator in Zig?
- Can mapFromZon and mapToZon allocate memory from different allocators safely?
- How does the Permissions struct manage its white and black lists internally?
- Why is unreachable used as the error handling strategy for map operations here?
- What would be a correct way to free memory allocated by an arena in Zig if needed later?
- Does the reviewer’s comment imply that permission removal should not track freed keys at all?
- How does the design of NeverFailingArenaAllocator affect garbage collection or manual deallocation patterns?
- Could adding permissions without removing them be exploited to exhaust server memory?

*Source: unknown | chunk_id: github_pr_2530_comment_2775422357*
