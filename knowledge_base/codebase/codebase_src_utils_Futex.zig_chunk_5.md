# [hard/codebase_src_utils_Futex.zig] - Chunk 5

**Type:** implementation
**Keywords:** futex, bucket, hashing, pending, mutex, queue, atomic, waiter, Treap, pointer, address
**Symbols:** Address, Bucket, Waiter
**Concepts:** futex synchronization, bucket hashing, atomic pending count, wait queue management, mutex locking, pointer address extraction

## Summary
Implements a futex-based wait mechanism with bucketed waiter queues and atomic pending counts.

## Explanation
The chunk defines the Address struct to extract unique addresses from pointers, Bucket struct containing a mutex, an atomic.Value for pending count, and a Treap field. The Bucket.from function hashes an address using fibonacci multiplication into a power-of-two bucket array. The wait function acquires the bucket's mutex, checks if the pointed value matches expect, inserts a Waiter into the Treap queue, then releases the lock. It uses atomic operations on pending to avoid holding the mutex while waiting for cancellation. The tryRemove function removes a waiter from its queue by updating prev/next links and adjusting head/tail pointers in the Treap entry; it asserts is_queued state before removal. The WaitList struct (partially visible) provides dequeue logic that collects waiters into a returned slice, marking them as not queued after removal.

## Related Questions
- How does the Address.from function extract a unique address from a pointer?
- What is the purpose of the atomic.Value in Bucket and how is it used?
- Describe the steps taken inside the wait function before acquiring the mutex.
- How does tryRemove handle a waiter that has both prev and next links set?
- Why is the pending count decremented outside the critical section when canceled?
- What assertion ensures a waiter can be removed from its queue in tryRemove?
- Explain how Bucket.from uses fibonacci hashing to map addresses into buckets.
- How does the wait function ensure that the announcement of a waiter happens before checking ptr == expect?
- What state changes occur to Waiter.is_queued during removal operations?
- Describe the role of the Treap field in managing waiter queues within Bucket.

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_5*
