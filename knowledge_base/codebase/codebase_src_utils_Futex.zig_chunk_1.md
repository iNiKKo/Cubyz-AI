# [hard/codebase_src_utils_Futex.zig] - Chunk 1

**Type:** implementation
**Keywords:** atomic operations, wait on address, ulock wait, timeout handling, wake up threads
**Symbols:** WindowsImpl, WindowsImpl.wait, WindowsImpl.wake, DarwinImpl, DarwinImpl.wait, DarwinImpl.wake
**Concepts:** futex, thread synchronization, platform-specific implementation

## Summary
This chunk implements platform-specific futex (fast user-space mutex) wait and wake operations for Windows and Darwin.

## Explanation
The code defines two structs, `WindowsImpl` and `DarwinImpl`, each containing methods for waiting on a futex (`wait`) and waking up threads waiting on a futex (`wake`). The `wait` method in both implementations checks if a timeout is provided and adjusts the timeout value accordingly. For Windows, it uses `RtlWaitOnAddress` from NTDLL, converting timeouts to 100-nanosecond units. For Darwin, it uses either `__ulock_wait` or `__ulock_wait2`, depending on the OS version, handling microsecond and nanosecond timeout values respectively. The `wake` method in both implementations wakes up one or all threads waiting on a futex based on the `max_waiters` parameter.

## Code Example
```zig
fn wake(ptr: *const atomic.Value(u32), max_waiters: u32) void {
	const address: ?*const anyopaque = ptr;
	assert(max_waiters != 0);

	switch (max_waiters) {
		1 => windows.ntdll.RtlWakeAddressSingle(address),
		else => windows.ntdll.RtlWakeAddressAll(address),
	}
}
```

## Related Questions
- How does the `wait` method handle timeouts on Windows?
- What is the difference between `__ulock_wait` and `__ulock_wait2` in Darwin's implementation?
- How does the `wake` method determine whether to wake a single or all threads?
- What error handling is implemented for the `wait` method on Darwin?
- How are atomic operations used in this futex implementation?
- What is the role of NTDLL functions in the Windows implementation?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_1*
