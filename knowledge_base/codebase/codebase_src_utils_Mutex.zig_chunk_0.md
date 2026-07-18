# [easy/codebase_src_utils_Mutex.zig] - Chunk 0

**Type:** implementation
**Keywords:** mutex, locking, SRWLOCK, thread synchronization, Windows API
**Symbols:** Mutex, Mutex.impl, Mutex.init, Mutex.tryLock, Mutex.lock, Mutex.unlock, Impl, WindowsImpl, WindowsImpl.srwlock, WindowsImpl.tryLock, WindowsImpl.lock, WindowsImpl.unlock, windows
**Concepts:** synchronization primitive, critical section, SRWLOCK, thread safety

## Summary
Mutex is a synchronization primitive for enforcing atomic access to shared code regions, implemented using Windows SRWLOCK.

## Explanation
Mutex is a synchronization primitive which enforces atomic access to a shared region of code known as the 'critical section'. It blocks other threads ensuring only one thread can be in the critical section at any given point in time. The Mutex struct provides methods for locking and unlocking this critical section, using the Windows SRWLOCK mechanism internally for efficient synchronization. Specifically, it is statically initialized and has a maximum size of `@sizeOf(u64)`. The `tryLock` method attempts to acquire the mutex without blocking; if the calling thread would have to block to acquire it, `false` is returned. Otherwise, `true` is returned and the caller should call `unlock()` on the Mutex to release it. The `lock` method acquires the mutex, blocking the caller's thread until it can enter the critical section. Once acquired, `unlock()` must be called to release the mutex. It is undefined behavior if a thread tries to unlock or lock from a different thread than it was locked from. The implementation uses the RtlTryAcquireSRWLockExclusive, RtlAcquireSRWLockExclusive, and RtlReleaseSRWLockExclusive functions from the ntdll library.

## Code Example
```zig
pub fn tryLock(self: *Mutex) bool {
	return self.impl.tryLock();
}
```

## Related Questions
- What is the purpose of the Mutex struct?
- How does the Mutex implement locking and unlocking?
- What method should be used to acquire the mutex without blocking?
- What happens if a thread tries to lock an already held mutex?
- Which Windows API functions are used for SRWLOCK operations?
- Can the Mutex be used on non-Windows platforms?
- What is the maximum size of the Mutex struct?

*Source: unknown | chunk_id: codebase_src_utils_Mutex.zig_chunk_0*
