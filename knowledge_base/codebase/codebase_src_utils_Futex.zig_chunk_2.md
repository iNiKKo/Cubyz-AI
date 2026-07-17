# [hard/codebase_src_utils_Futex.zig] - Chunk 2

**Type:** implementation
**Keywords:** futex, synchronization, wait, wake, timeout, system calls
**Symbols:** LinuxImpl, FreebsdImpl, OpenbsdImpl
**Concepts:** futex synchronization, operating system specific implementations

## Summary
This chunk implements futex-based synchronization primitives for Linux, FreeBSD, and OpenBSD operating systems.

## Explanation
The chunk defines three structs, each implementing the same interface for futex operations but tailored to different operating systems: LinuxImpl, FreebsdImpl, and OpenbsdImpl. Each struct contains two methods: `wait` and `wake`. The `wait` method allows a thread to wait on a futex value until it changes or a timeout occurs, while the `wake` method wakes up waiting threads. The implementations handle system-specific details such as error codes and argument formatting for the respective operating systems' futex syscalls.

## Related Questions
- What are the two methods defined in each futex implementation struct?
- How does the `wait` method handle timeouts on Linux?
- What is the purpose of the `wake` method in the FreeBSD implementation?
- Which operating systems are supported by this chunk?
- How does the OpenBSD implementation handle invalid arguments?
- What error handling is done for spurious wakeups in the Linux implementation?
- How is the timeout value converted to a timespec structure in the FreeBSD implementation?
- What system call is used for futex operations on OpenBSD?
- How are the `wait` and `wake` methods implemented differently across operating systems?
- What does the `assert(timeout != null)` statement indicate in the `wait` method?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_2*
