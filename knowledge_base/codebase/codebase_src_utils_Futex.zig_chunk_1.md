# [hard/codebase_src_utils_Futex.zig] - Chunk 1

**Type:** implementation
**Keywords:** futex, RtlWaitOnAddress, __ulock_wait2, timeout overflow, spurious wakeup, errno mapping, atomic.Value, version detection, COMPARE_AND_WAIT, private futex
**Symbols:** DarwinImpl, LinuxImpl
**Concepts:** futex synchronization, platform-specific backends, timeout handling, spurious wakeup loops, atomic compare-and-wait, errno mapping, version detection, nanosecond to microsecond conversion

## Summary
Implements futex synchronization primitives with separate Windows (RtlWaitOnAddress/RtlWakeAddressSingle/All) and Darwin (__ulock_wait2/__ulock_wake) backends, plus a Linux implementation using futex_4arg.

## Explanation
The chunk defines three platform-specific implementations: DarwinImpl provides wait() which checks for ulock_wait2 support via builtin.target.os.version_range.semver.min.major >= 11, caps timeouts to u32 microseconds when necessary (setting timeout_overflowed), and handles INTR/FAULT/TIMEDOUT with assertions; wake() uses __ulock_wake with flags.op = COMPARE_AND_WAIT, NO_ERRNO, and WAKE_ALL derived from max_waiters > 1, looping on spurious wakes. LinuxImpl provides wait() converting a u64 timeout to linux.timespec (sec/nsec), calling futex_4arg with cmd.WAIT and private=true, then mapping errno codes SUCCESS/INTR/AGAIN/TIMEDOUT/INVAL/FAULT; wake() is not defined here but implied by the switch on rc. Windows backend uses RtlWaitOnAddress with a LARGE_INTEGER timeout converted from nanoseconds (delay/100) negated for relative duration, and RtlWakeAddressSingle/All based on max_waiters.

## Related Questions
- How does DarwinImpl detect support for ulock_wait2?
- What happens when the timeout exceeds u32 microseconds on Darwin?
- Which errno codes are treated as spurious wakeups in LinuxImpl?
- How is a Windows LARGE_INTEGER timeout constructed from nanoseconds?
- Why does DarwinImpl assert that delay != 0 before using ulock_wait2?
- What flag combination is used for __ulock_wake on Darwin?
- Does the chunk define a wake function for LinuxImpl?
- How are INTR and AGAIN distinguished in the Linux errno switch?
- What does timeout_overflowed control in the Darwin wait path?
- Is the futex operation marked private or shared in LinuxImpl?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_1*
