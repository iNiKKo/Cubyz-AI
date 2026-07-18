# [medium/codebase_src_utils_Condition.zig] - Chunk 0

**Type:** implementation
**Keywords:** mutex, condition variable, thread blocking, atomic operations, spurious wakeups
**Symbols:** Condition, Condition.impl, Condition.wait, Condition.timedWait, Condition.signal, Condition.broadcast, Impl, Notify, SingleThreadedImpl
**Concepts:** thread synchronization, mutex, condition variable

## Summary
Condition variables for thread synchronization using mutexes.

## Explanation
This chunk defines a `Condition` struct for thread synchronization using mutexes. The `Condition` uses an underlying implementation (`Impl`) that varies based on the build configuration (single-threaded, Windows, or Futex-based). A condition variable is statically initialized and at most `@sizeOf(u64)` large.

The `wait` method atomically releases a mutex, blocks the thread until notified, and re-acquires the mutex. The Mutex must be locked by the caller's thread when this function is called. A blocking call to wait() can be unblocked from spurious wakeups or future calls to `signal()` or `broadcast()` which have acquired the Mutex and are sequenced after this `wait()`. Given wait() can be interrupted spuriously, the blocking condition should be checked continuously irrespective of any notifications.

The `timedWait` method adds a timeout in nanoseconds. A blocking call to timedWait() is unblocked from spurious wakeups or when the caller was blocked for around `timeout_ns` nanoseconds, returning `error.Timeout`. Given `timedWait()` can be interrupted spuriously, the blocking condition should be checked continuously irrespective of any notifications.

The `signal` method unblocks at least one thread blocked in a call to `wait()` or `timedWait()` with a given Mutex. The blocked thread must be sequenced before this call with respect to acquiring the same Mutex in order to be observable for unblocking. `signal()` can be called with or without the relevant Mutex being acquired and have no effect if there's no observable blocked threads.

The `broadcast` method unblocks all threads currently blocked in a call to `wait()` or `timedWait()` with a given Mutex. The blocked threads must be sequenced before this call with respect to acquiring the same Mutex in order to be observable for unblocking. `broadcast()` can be called with or without the relevant Mutex being acquired and have no effect if there's no observable blocked threads.

A condition variable can only reliably unblock threads that are sequenced before them using the same Mutex.

## Code Example
```zig
fn wait(self: *Condition, mutex: *Mutex) void {
	self.impl.wait(mutex, null) catch |err| switch (err) {
		error.Timeout => unreachable, // no timeout provided so we shouldn't have timed-out
	};
}
```

## Related Questions
- What is the size of a Condition struct?
- How does the `timedWait` method handle timeouts?
- Under what conditions will a call to `signal` or `broadcast` successfully unblock waiting threads?

*Source: unknown | chunk_id: codebase_src_utils_Condition.zig_chunk_0*
