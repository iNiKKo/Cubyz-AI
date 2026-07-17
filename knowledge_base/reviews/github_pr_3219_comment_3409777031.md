# [src/server/server.zig] - Chunk 3409777031

**Type:** review
**Keywords:** leak, dup, free, thread, allocator, defer, syncPoint, globalAllocator, heap, GC, ownership, lifetime
**Symbols:** update, startFromNewThread, main.initThreadLocals, main.deinitThreadLocals, startFromExistingThread, main.globalAllocator.dupe, main.heap.GarbageCollection.syncPoint
**Concepts:** memory leak prevention, string duplication, defer cleanup, thread ownership of data, garbage collection sync point, heap allocation lifetime, backwards compatibility

## Summary
The update() function now duplicates the thread name before passing it to startFromExistingThread, ensuring the original caller's string is not leaked when the new thread exits.

## Explanation
The reviewer pointed out a potential memory leak in the previous implementation where startFromExistingThread was called directly with the caller-provided name slice. Since Zig does not automatically copy strings passed to functions, if the caller's allocation lifetime ended before the newly created thread finished its work, the thread would still hold a dangling reference to that memory. The fix introduces an explicit duplication step: main.globalAllocator.dupe(u8, name) creates a new heap-allocated copy of the name string owned by the server process. This copied string is then passed to startFromExistingThread, guaranteeing that the thread works on data it owns for its entire lifetime. A defer block ensures the duplicated string is freed when the function returns, preventing any leak from the duplication itself. Additionally, main.heap.GarbageCollection.syncPoint() is inserted after starting the thread; this forces a garbage collection checkpoint so that any allocations performed by the new thread are accounted for in the server's heap before the thread potentially exits or blocks on GC. The change preserves backward compatibility because the API signature of startFromExistingThread remains unchanged, only the internal handling of its first argument is altered.

## Related Questions
- What is the exact signature of startFromExistingThread and how does it treat its first argument?
- Does main.globalAllocator.dupe(u8) allocate on the heap or a different pool in this codebase?
- Is there any other place where strings are passed to thread-starting functions without duplication?
- What happens if the caller's name slice is already owned by the server process before calling startFromNewThread?
- How does main.heap.GarbageCollection.syncPoint affect threads that are currently running when it is called?
- Are there any tests that verify the thread name is correctly freed after the thread exits?
- Could the defer block cause double-free if startFromExistingThread internally frees its copy of the name?
- What is the expected behavior if main.globalAllocator fails during dupe? Is error handling added?
- Does the original implementation rely on the caller to keep the name alive for the thread's duration?
- Is there a race condition between calling syncPoint and the newly created thread potentially allocating memory?

*Source: unknown | chunk_id: github_pr_3219_comment_3409777031*
