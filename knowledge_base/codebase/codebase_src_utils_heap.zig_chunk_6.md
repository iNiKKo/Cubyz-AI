# [hard/codebase_src_utils_heap.zig] - Chunk 6

**Type:** api
**Keywords:** PowerOfTwoPoolAllocator, bucket, mutex, alignment, freeLists, allocNew, NeverFailingArenaAllocator, arena.deinit, alignedAlloc, vtable
**Symbols:** PowerOfTwoPoolAllocator, Node, NodePtr, Bucket, allocNew
**Concepts:** memory pool allocation, power-of-two sizing, thread-safe allocator, mutex locking, arena allocation, aligned memory, bucket management, allocator API surface

## Summary
This chunk defines the PowerOfTwoPoolAllocator type, a thread-safe memory pool allocator that uses power-of-two sized buckets protected by a mutex to allocate and free aligned blocks of memory.

## Explanation
The chunk declares a generic struct named PowerOfTwoPoolAllocator with compile-time parameters minSize, maxSize, and maxAlignment. It asserts that sizes are powers of two and properly ordered, computes the alignment as the maximum of maxAlignment and usize size, derives baseShift via log2_int on minSize, and calculates bucketCount from the range between minSize and maxSize. The returned struct contains a Node inner type with a next pointer field aligned to the computed alignment, a NodePtr alias for *align(alignment) Node, and a Bucket inner struct holding freeLists (a linked list of nodes), freeAllocations count, and totalAllocations count. Bucket defines deinit which checks for leaks by comparing freeAllocations against totalAllocations, logs an error if leaked or info otherwise, then zeroes the bucket. create allocates from either the existing freeLists head or a new allocation via allocNew, decrements freeAllocations, and returns the raw pointer cast to [*]u8. destroy reconstructs a Node with next pointing to the current freeLists head, updates freeLists, and increments freeAllocations. allocNew increments both counters and calls arena.alignedAlloc returning an aligned u8 slice ptr. The outer struct holds an arena of type NeverFailingArenaAllocator, an array of buckets initialized via @splat(.{}), and a mutex from main.utils.Mutex. init returns a Self with the arena initialized. deinit iterates over buckets calling bucket.deinit with sizes computed as minSize shifted left by the index, then calls self.arena.deinit(). allocator returns a NeverFailingAllocator struct containing a vtable of function pointers to alloc, resize, remap, and free, plus an IAssertThatTheProvidedAllocatorCantFail unit type instance. The alloc closure asserts alignment is within maxAlignment, length is a power of two and within bounds, casts ctx to *Self, computes bucket index via @ctz(len) - baseShift, locks the mutex, defers unlock, then calls self.buckets[bucket].create with arena.allocator(). resize and remap are stubs returning false and null respectively. free asserts alignment and power-of-two length, computes bucket similarly, locks mutex, defers unlock, and calls self.buckets[bucket].destroy on the memory ptr.

## Related Questions
- How does PowerOfTwoPoolAllocator compute the bucket index for a given allocation size?
- What assertions are performed in the alloc closure before attempting to retrieve memory from a bucket?
- Describe the deinit behavior of Bucket when freeAllocations differs from totalAllocations.
- Why is @ctz used instead of log2_int in the alloc and free closures for computing the bucket index?
- What happens if an item passed to destroy was not previously created by create on the same pool?
- How does the allocator closure construct its vtable function pointers from the inner functions?
- Explain the role of NeverFailingArenaAllocator in the PowerOfTwoPoolAllocator struct layout.
- Where is the mutex acquired and released within the alloc and free closures?

*Source: unknown | chunk_id: codebase_src_utils_heap.zig_chunk_6*
