# [hard/codebase_src_utils_Futex.zig] - Chunk 4

**Type:** implementation
**Keywords:** pthread_cond_wait, pthread_mutex_lock, state transition, wait queue, address mapping, Treap.Node, defer unlock, error.Timeout, is_queued flag, linked list
**Symbols:** Event, Waiter, WaitList, WaitQueue
**Concepts:** futex synchronization, condition variable wait, event state machine, wait queue management, Treap-backed address mapping, linked list navigation, thread-safe signaling, timeout handling

## Summary
Implements a futex-based event synchronization mechanism with wait/notify semantics, including a waiter list and address-mapped wait queues backed by a Treap.

## Explanation
The chunk defines an Event struct with state transitions (empty -> waiting -> notified) protected by pthread_mutex_lock/unlock and condition variables. The set() method asserts the mutex is locked, checks that the event hasn't already been notified, updates state to .notified, signals the condition if a thread was waiting, and uses defer to unlock. The wait() method asserts the event is empty before entering, sets state to .waiting, then loops calling pthread_cond_wait or pthread_cond_timedwait depending on timeout; after waking it checks state == .notified to return success, otherwise reasserts .waiting and handles rc values (.SUCCESS, .TIMEDOUT resetting state to .empty with error.Timeout, .INVAL/.PERM unreachable). The chunk also defines a Waiter struct containing a Treap.Node, prev/next/tail pointers for linked-list navigation, is_queued flag, and an Event reference. A WaitList provides push/pop operations on the top of a linked list. A WaitQueue wraps these with insert() which prepares the waiter (clears next, sets is_queued), looks up or creates a Treap entry for the address, links waiters into a doubly-linked tail chain within that entry, and remove() which extracts up to max_waiters from the head of the queue while marking them as not queued. tryRemove() checks is_queued and uses an inner block to handle the case where the waiter is the head (no prev) by calling treap.getEntryForExisting directly.

## Related Questions
- How does the Event.wait() method handle a timeout versus an indefinite wait?
- What assertions are made inside Event.set() to prevent double signaling?
- Why is pthread_cond_timedwait used instead of pthread_cond_wait when a timeout is provided?
- How does WaitQueue.insert() create a new entry in the Treap if none exists for an address?
- What happens to the state of an Event after it times out while waiting?
- In what order are waiters linked within a single WaitQueue entry's doubly-linked list?
- Why is waiter.is_queued set to false when removing from the queue head in WaitQueue.remove()?
- How does tryRemove() avoid a Treap lookup when the waiter has no previous link?
- What role does the defer block play after updating the Treap entry in WaitQueue.insert()?
- Can multiple threads call Event.set() concurrently without race conditions, and how is that ensured?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_4*
