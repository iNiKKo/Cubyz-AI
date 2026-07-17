# [hard/codebase_src_utils_Futex.zig] - Chunk 0

**Type:** implementation
**Keywords:** wait, wake, futex, thread synchronization, atomic.Value, platform detection, deadlock avoidance, timeout handling, single-threaded fallback, NtDll RtlWaitOnAddress
**Symbols:** Futex, wait, timedWait, wake, UnsupportedImpl, SingleThreadedImpl, WindowsImpl
**Concepts:** thread synchronization, futex wait wake, platform detection, atomic value comparison, deadlock avoidance, timeout handling, single-threaded fallback, NtDll RtlWaitOnAddress

## Summary
Implements futex-based thread synchronization primitives (wait/wake) with per-platform backends and a single-threaded fallback.

## Explanation
The chunk defines the Futex struct containing public wait, timedWait, and wake methods that delegate to an Impl type selected via a compile-time switch over builtin.single_threaded, OS tag, CPU arch, pthread availability, etc. UnsupportedImpl provides stub implementations that call unsupported() which asserts on unused arguments and then @compileError with the target OS name. SingleThreadedImpl implements wait by checking ptr.raw against expect; if they differ it returns immediately, otherwise it treats a missing timeout as unreachable (deadlock) and always returns error.Timeout. wake in SingleThreadedImpl discards both arguments. WindowsImpl uses NtDll.RtlWaitOnAddress with a LARGE_INTEGER timeout converted to 100‑ns units (negative for relative), returning on .SUCCESS or .TIMEOUT; its wake stub begins by casting ptr to ?*const anyopaque but the body is truncated in this chunk. The Impl switch also includes DarwinImpl, LinuxImpl, FreebsdImpl, OpenbsdImpl, WasmImpl, and PosixImpl as alternatives depending on platform detection.

## Related Questions
- What does the Futex struct provide for thread synchronization?
- How is the Impl type selected at compile time in this chunk?
- What happens when a wait call finds ptr.raw != expect in SingleThreadedImpl?
- Why does SingleThreadedImpl treat a missing timeout as unreachable?
- Which platforms are covered by the Impl switch statement here?
- How is the WindowsImpl wait method implemented using NtDll?
- What error does UnsupportedImpl return when its stub is invoked?
- Does timedWait ever call the OS directly for zero timeouts in this chunk?
- What arguments are discarded in SingleThreadedImpl.wake?
- Is there any public API surface beyond wait, timedWait, and wake defined here?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_0*
