# [hard/codebase_src_utils_Futex.zig] - Chunk 3

**Type:** implementation
**Keywords:** atomic operations, inline assembly, WebAssembly atomics, timeout handling, synchronization primitives
**Symbols:** WasmImpl, WasmImpl.wait, WasmImpl.wake
**Concepts:** atomic synchronization, WebAssembly, memory wait/wake

## Summary
Provides atomic wait and wake functionality for WebAssembly targets.

## Explanation
The chunk defines a `WasmImpl` struct with two methods: `wait` and `wake`. The `wait` method atomically waits on a memory location until its value changes or a timeout occurs, returning an error if the timeout is reached. The `wake` method wakes up a specified number of waiters waiting on a memory location. Both methods check for the presence of atomic CPU features in WebAssembly targets and use inline assembly to perform atomic operations.

The `wait` method uses the following inline assembly instructions:
```zig
const result = asm volatile (
    \\local.get %[ptr]
    \\local.get %[expected]
    \\local.get %[timeout]
    \\memory.atomic.wait32 0
    \\local.set %[ret]
    : [ret] "=r" (-> u32),
    : [ptr] "r" (&ptr.raw),
        [expected] "r" (@as(i32, @bitCast(expect))),
        [timeout] "r" (to),
);
```
The `wake` method uses the following inline assembly instructions:
```zig
const woken_count = asm volatile (
    \\local.get %[ptr]
    \\local.get %[waiters]
    \\memory.atomic.notify 0
    \\local.set %[ret]
    : [ret] "=r" (-> u32),
    : [ptr] "r" (&ptr.raw),
        [waiters] "r" (max_waiters),
);
```
The `switch` statement in the `wait` method handles different return values as follows:
- `0`: Success
- `1`: Expected value did not match loaded value
- `2`: Timeout occurred, returns an error
- Other: Unreachable state

## Code Example
```zig
fn wake(ptr: *const atomic.Value(u32), max_waiters: u32) void {
		if (!comptime builtin.cpu.has(.wasm, .atomics)) @compileError("WASI target missing cpu feature 'atomics'");

		assert(max_waiters != 0);
		const woken_count = asm volatile (
			\\local.get %[ptr]
			\\local.get %[waiters]
			\\memory.atomic.notify 0
			\\local.set %[ret]
			: [ret] "=r" (-> u32),
			: [ptr] "r" (&ptr.raw),
				[waiters] "r" (max_waiters),
		);
		_ = woken_count; // can be 0 when linker flag 'shared-memory' is not enabled
	}
```

## Related Questions
- What methods does the WasmImpl struct provide?
- How does the wait method handle timeouts?
- What error is returned if a timeout occurs in the wait method?
- What does the wake method do?
- How are atomic operations performed in this code?
- Why is there an assertion that max_waiters should not be zero?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_3*
