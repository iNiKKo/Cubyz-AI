# [easy/codebase_src_utils_Semaphore.zig] - Chunk 0

**Type:** api
**Keywords:** semaphore, mutex locking, condition wait, signal notify, permissive count, timeout error, defer unlock, static init, kernel thread block, nanosecond duration
**Symbols:** Semaphore, Semaphore.mutex, Semaphore.cond, Semaphore.permits, Semaphore.wait, Semaphore.timedWait, Semaphore.post
**Concepts:** sync primitives, static initialization, condition variable waiting, thread blocking, timeout handling

## Summary
Implements a static-initialized semaphore using mutex and condition variable to block threads when permits reach zero, with wait/timedWait/post operations.

## Explanation
The chunk defines the Semaphore struct (via @This) containing a Mutex field initialized inline, a Condition field initialized inline, and a permits usize field that may be set at static initialization. It exposes three public functions: wait locks the mutex, loops while permits is zero waiting on the condition under the lock, decrements permits, and signals if permits remains positive; timedWait mirrors this but tracks elapsed time from start timestamp using main.timestamp() and returns error.Timeout when the timeout expires before a permit becomes available; post increments permits and signals the condition. All functions use defer to unlock the mutex after acquiring it. The chunk imports Mutex and Condition from main.utils, uses main.timestamp for timing, and includes a TODO comment referencing an upstream Zig issue.

## Related Questions
- What is the initial value of Semaphore.permits and how does it affect blocking behavior?
- How does wait ensure mutual exclusion when checking permits?
- What happens to the condition variable after a permit is consumed in wait?
- When does timedWait return error.Timeout versus proceeding normally?
- How are elapsed nanoseconds computed inside timedWait relative to start timestamp?
- Does post signal the condition even if permits was zero before incrementing?
- Are there any other public methods on Semaphore besides wait, timedWait, and post?
- What imports from main.utils does Semaphore depend on for its synchronization primitives?
- How is the Mutex field initialized when a Semaphore instance is created statically?
- Can the Condition be used directly outside of Semaphore.wait or timedWait in this chunk?

*Source: unknown | chunk_id: codebase_src_utils_Semaphore.zig_chunk_0*
