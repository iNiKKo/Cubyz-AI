# [easy/codebase_src_utils_Semaphore.zig] - Chunk 0

**Type:** implementation
**Keywords:** semaphore, mutex, condition variable, thread blocking, permit management
**Symbols:** Semaphore, Semaphore.mutex, Semaphore.cond, Semaphore.permits, Semaphore.wait, Semaphore.timedWait, Semaphore.post
**Concepts:** synchronization, thread management, resource control

## Summary
This chunk implements a semaphore using mutex and condition variable for synchronization.

## Explanation
This chunk implements a semaphore using mutex and condition variable for synchronization. The Semaphore struct uses a Mutex and Condition to manage `permits`, which defaults to `0` (it's explicitly OK to initialize it to any value). It supports static initialization and needs no deinitialization. The `wait` function blocks the calling thread while `permits == 0`, then decrements it by 1 and signals another waiter if permits remain. The `timedWait` function does the same but returns `error.Timeout` if the timeout elapses first, calculated as the difference between the start time and the current timestamp. The `post` function increments `permits` and signals one waiting thread.

## Code Example
```zig
pub fn wait(sem: *Semaphore) void {
	sem.mutex.lock();
	defer sem.mutex.unlock();

	while (sem.permits == 0) {
		sem.cond.wait(&sem.mutex);
	}

	sem.permits -= 1;
	if (sem.permits > 0) {
		sem.cond.signal();
	}
}
```

## Related Questions
- How does the Semaphore struct initialize its fields?
- What is the purpose of the `wait` function in the Semaphore implementation?
- How does the `timedWait` function handle timeouts?
- What role does the Mutex play in the Semaphore's functionality?
- How are permits managed within the Semaphore struct?
- Can multiple threads safely use a single Semaphore instance?

*Source: unknown | chunk_id: codebase_src_utils_Semaphore.zig_chunk_0*
