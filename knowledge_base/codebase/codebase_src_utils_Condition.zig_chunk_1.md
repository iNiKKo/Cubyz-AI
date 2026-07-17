# [medium/codebase_src_utils_Condition.zig] - Chunk 1

**Type:** implementation
**Keywords:** condition variable, mutex, timeout, SRW lock, futex, atomic, barrier, wake all, wait one, deadlock
**Symbols:** SingleThreadedImpl, WindowsImpl, FutexImpl, RtlWakeConditionVariable, RtlWakeAllConditionVariable, SleepConditionVariableSRW
**Concepts:** condition variable synchronization, platform-specific backends, single-threaded stub, Windows SRW locks, Linux futexes, atomic barriers, epoch-based ordering, deadlock detection

## Summary
Implements condition variable synchronization primitives with three platform-specific backends: a single-threaded stub, Windows SRW locks via ntdll exports, and Linux futexes using atomic state/epoch barriers.

## Explanation
The chunk defines an Impl struct containing three impl types. SingleThreadedImpl provides wait that asserts timeout != null (deadlock detection) and wake that does nothing; both ignore self and notify parameters. WindowsImpl exposes a CONDITION_VARIABLE field, imports windows.h via @cImport, declares two extern functions RtlWakeConditionVariable and RtlWakeAllConditionVariable from ntdll with callconv(.winapi), implements wait by rounding nanoseconds to milliseconds (using saturating cast) and handling overflow into INFINITE by decrementing timeout_ms, then calls c.SleepConditionVariableSRW with the SRW lock pointer; on FALSE return it asserts GetLastError == .TIMEOUT and returns error.Timeout if not overflowed. wake switches on notify: one => RtlWakeConditionVariable(&self.condition), all => RtlWakeAllConditionVariable(&self.condition). FutexImpl maintains state (atomic u32) initialized to 0 and epoch (atomic u32) initialized to 0, defines constants one_waiter = 1, waiter_mask = 0xffff, one_signal = 1 << 16, signal_mask = 0xffff << 16. wait loads epoch with .acquire barrier then fetches state with .monotonic (adding one_waiter), asserts state & waiter_mask != waiter_mask, increments state, unlocks mutex via defer lock, creates Futex.Deadline from timeout, loops forever: calls futex_deadline.wait(&self.epoch, epoch) catching error.Timeout; on Timeout it consumes any pending signals by repeatedly cmpxchgWeak subtracting one_waiter and one_signal while state & signal_mask != 0, then decrements waiter count and returns. After the deadline call it reloads epoch (acquire) and state (monotonic), then consumes signals again with cmpxchgWeak before looping. wake loads state monotonically, computes waiters = (state & waiter_mask)/one_waiter and signals = (state & signal_mask)/one_signal, calculates wakeable = waiters - signals, returns early if wakeable == 0, otherwise switches on notify: one => wakes a single waiter.

## Code Example
```zig
fn wait(self: *Impl, mutex: *Mutex, timeout: ?u64) error{Timeout}!void {
	_ = self;
	_ = mutex;
	// There are no other threads to wake us up.
	// So if we wait without a timeout we would never wake up.
	assert(timeout != null); // Deadlock detected.
	return error.Timeout;
}
```

## Related Questions
- What does SingleThreadedImpl.wait assert about the timeout parameter and why?
- How is nanosecond timeout rounded to milliseconds in WindowsImpl.wait, including overflow handling?
- What external functions are declared from ntdll in WindowsImpl and what do they wake?
- In FutexImpl.wait, how are epoch and state loaded with memory ordering guarantees before waiting on futex_deadline?
- Describe the signal consumption loop inside FutexImpl.wait when error.Timeout is caught.
- How does FutexImpl.wake compute waiters and signals from the atomic state value?
- What condition causes FutexImpl.wake to return early without waking any threads?
- Why does SingleThreadedImpl wake ignore its notify argument entirely?
- Which mutex operations are performed in WindowsImpl.wait before calling SleepConditionVariableSRW?
- How is the SRW lock pointer passed to SleepConditionVariableSRW derived from Mutex.super.impl.srwlock?
- What happens if timeout_ms equals c.INFINITE after rounding in WindowsImpl.wait?
- In FutexImpl, what does one_signal represent and how is it used during wake?

*Source: unknown | chunk_id: codebase_src_utils_Condition.zig_chunk_1*
