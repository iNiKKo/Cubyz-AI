# [medium/codebase_src_utils_Condition.zig] - Chunk 2

**Type:** implementation
**Keywords:** atomic operations, mutex locking, timeout handling, deadlock prevention, futex wait/wake
**Symbols:** FutexImpl, FutexImpl.state, FutexImpl.epoch, FutexImpl.one_waiter, FutexImpl.waiter_mask, FutexImpl.one_signal, FutexImpl.signal_mask, FutexImpl.wait, FutexImpl.wake
**Concepts:** thread synchronization, condition variable, futexes

## Summary
This chunk implements a condition variable mechanism using futexes for synchronization between threads.

## Explanation
The code defines a `FutexImpl` struct that manages state and epoch values to implement a condition variable. It includes two main methods: `wait` and `wake`. The `wait` method allows a thread to wait on a condition, optionally with a timeout, while the `wake` method signals one or all waiting threads. The implementation uses atomic operations to safely manage the state and epoch, ensuring proper synchronization and avoiding deadlocks.

## Code Example
```zig
fn wake(self: *Impl, comptime notify: Notify) void {
	var state = self.state.load(.monotonic);
	while (true) {
		const waiters = (state & waiter_mask) / one_waiter;
		const signals = (state & signal_mask) / one_signal;

		// Reserves which waiters to wake up by incrementing the signals count.
		// Therefore, the signals count is always less than or equal to the waiters count.
		// We don't need to Futex.wake if there's nothing to wake up or if other wake() threads have reserved to wake up the current waiters.
		const wakeable = waiters - signals;
		if (wakeable == 0) {
			return;
		}

		const to_wake = switch (notify) {
			.one => 1,
			.all => wakeable,
		};

		// Reserve the amount of waiters to wake by incrementing the signals count.
		// Release barrier ensures code before the wake() happens before the signal it posted and consumed by the wait() threads.
		const new_state = state + (one_signal * to_wake);
		state = self.state.cmpxchgWeak(state, new_state, .release, .monotonic) orelse {
			// Wake up the waiting threads we reserved above by changing the epoch value.
			// NOTE: a waiting thread could miss a wake up if *exactly* ((1<<32)-1) wake()s happen between it observing the epoch and sleeping on it.
			// This is very unlikely due to how many precise amount of Futex.wake() calls that would be between the waiting thread's potential preemption.
			//
			// Release barrier ensures the signal being added to the state happens before the epoch is changed.
			// If not, the waiting thread could potentially deadlock from missing both the state and epoch change:
			//
			// - T2: UPDATE(&epoch, 1) (reordered before the state change)
			// - T1: e = LOAD(&epoch)
			// - T1: s = LOAD(&state)
			// - T2: UPDATE(&state, signal) + FUTEX_WAKE(&epoch)
			// - T1: s & signals == 0 -> FUTEX_WAIT(&epoch, e) (missed both epoch change and state change)
			_ = self.epoch.fetchAdd(1, .release);
			Futex.wake(&self.epoch, to_wake);
			return;
		};
	}
}
```

## Related Questions
- What is the purpose of the `wait` method in the `FutexImpl` struct?
- How does the `wake` method determine how many threads to wake up?
- What atomic operations are used in the implementation of the condition variable?
- How does the code handle timeouts when a thread is waiting?
- What is the role of the epoch value in this synchronization mechanism?
- How does the implementation prevent deadlocks from occurring?

*Source: unknown | chunk_id: codebase_src_utils_Condition.zig_chunk_2*
