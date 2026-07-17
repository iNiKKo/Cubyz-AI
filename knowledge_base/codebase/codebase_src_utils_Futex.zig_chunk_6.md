# [hard/codebase_src_utils_Futex.zig] - Chunk 6

**Type:** implementation
**Keywords:** futex, treap wait queue, pending counter, pthread_mutex_lock, release order fetchAdd, deadline timeout, absolute timeout, spurious wakeups, event signaling, atomic.Value, memory ordering, critical section, defer cleanup, error.Timeout, main.timestamp
**Symbols:** Bucket, Bucket.pending, Bucket.mutex, Bucket.treap, sleeper, sleeper.event, sleeper.is_queued, sleep(), wake(), Address.from(), Bucket.from(), WaitQueue.insert(), WaitQueue.tryRemove(), WaitList, Deadline, Deadline.timeout, Deadline.started, Deadline.init(), Futex.wait(), Futex.timedWait()
**Concepts:** futex synchronization, wait queue treap, deadline timeout, atomic memory ordering, pthread mutex locking, event signaling, spurious wakeup handling

## Summary
Implements futex-based synchronization primitives (wait/wake with Treap wait queues and deadline timeouts).

## Explanation
The chunk defines a Bucket struct containing a pthread mutex, an atomic pending counter, and a WaitQueue treap. The sleep() function atomically increments pending under the mutex, checks if the pointer value matches expect, then inserts a waiter into the treap; it defers event initialization and removal from the queue on exit. wake() first performs a release-order fetchAdd(0) to bump pending without acquiring the lock; if no waiters exist it returns early. It maintains a notified list outside the critical section, then acquires the mutex, checks pending again, removes up to max_waiters from the treap, and sets each waiter's event. The Deadline struct wraps Futex.wait() with an absolute timeout derived from std.Io.Timestamp; its wait() method computes elapsed time since init(), subtracts from the configured timeout, and delegates to Futex.timedWait(). All operations use explicit acquire/monotonic/release memory orders via atomic fetchAdd/fetchSub and pthread_mutex_lock/unlock assertions.

## Code Example
```zig
pub fn init(expires_in_ns: ?u64) Deadline {
	var deadline: Deadline = undefined;
	deadline.timeout = expires_in_ns;

	// std.time.Timer is required to be supported for somewhat accurate reportings of error.Timeout.
	if (deadline.timeout != null) {
		deadline.started = main.timestamp();
	}

	return deadline;
}
```

## Related Questions
- Does Bucket.pending use an atomic type and what memory order is used when incrementing it in sleep()?
- How does wake() avoid holding the mutex while iterating over notified waiters, and why is that safe?
- What happens if Futex.timedWait() returns early due to a spurious wakeup before the deadline expires?
- Is there any assertion checking that the pointer value matches expect after waking up in sleep()?
- How does Deadline.wait() compute the remaining timeout when called multiple times with different pointers?
- Does wake() ever call WaitQueue.remove() or tryRemove() without first bumping pending?
- What is the purpose of the defer block that sets waiter.event.set() outside the mutex in wake()?
- If max_waiters is zero, does wake() still attempt to remove any waiters from the treap?
- Are there any cases where sleep() could insert a waiter into an empty treap without checking pending first?
- How does the code ensure that the pointer update happens before the pending counter bump in wake()?
- What error type is returned when Deadline.wait() times out and how is it propagated to the caller?
- Is there any synchronization between multiple calls to sleep() on the same pointer address?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_6*
