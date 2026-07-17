# [hard/codebase_src_utils_Futex.zig] - Chunk 3

**Type:** implementation
**Keywords:** pthread_cond_wait, pthread_mutex_lock, CLOCK_REALTIME, timespec, unreachable, static init, error.Timeout, deinit, state enum
**Symbols:** Event, Event.cond, Event.mutex, Event.state, Event.init, Event.deinit, Event.wait
**Concepts:** pthread condition variables, static initialization, mutex locking, timeout handling, state machine

## Summary
Implements userspace wait queues via pthread condition variables on POSIX and atomic memory operations on WASM.

## Explanation
The chunk defines two platform-specific implementations: PosixImpl uses a struct Event with a pthread_cond_t, pthread_mutex_t, and an enum state (empty/waiting/notified). The init() method statically initializes the cond and mutex to zero structs and sets state to empty. deinit() destroys both pthread objects, asserting that rc is SUCCESS or INVAL (EINVAL for static init), then clears self.* with undefined. wait() locks the mutex, returns early if already notified, computes an absolute timespec from a relative timeout using CLOCK.REALTIME (catching failure as unreachable), sets state to waiting, and enters a loop calling pthread_cond_wait or pthread_cond_timedwait depending on whether a timeout is provided; after waking it checks state again—if still empty it loops, otherwise returns. The switch on rc handles SUCCESS (continue), TIMEDOUT (reset state to empty and return error.Timeout), INVAL/PERM (unreachable). wake() is not defined in this chunk.

## Related Questions
- What is the purpose of the Event struct in PosixImpl?
- How does Event.init() initialize pthread condition variables and mutexes?
- Why does Event.deinit() assert that rc == .SUCCESS or rc == .INVAL?
- What happens inside Event.wait() when a timeout is provided versus null?
- How does the code handle the case where pthread_cond_wait returns TIMEDOUT?
- What state transitions occur for Event.state during wait and wake operations?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_3*
