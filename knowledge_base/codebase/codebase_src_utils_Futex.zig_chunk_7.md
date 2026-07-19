# [hard/codebase_src_utils_Futex.zig] - Chunk 7

**Type:** implementation
**Keywords:** Futex, timedWait, deadline, timeout, atomic value
**Symbols:** Deadline, Deadline.timeout, Deadline.started, Deadline.init, Deadline.wait
**Concepts:** Futex, timed waiting, spurious wakeups, timeout handling

## Summary
The Deadline struct manages timeouts for waiting on a pointer's value change using Futex, converting relative durations to absolute ones to handle spurious wakeups and provide accurate error reporting.

## Explanation
The Deadline struct manages timeouts for waiting on a pointer's value change using Futex, converting relative durations to absolute ones to handle spurious wakeups and provide accurate error reporting. The `init` function initializes a deadline with a specified timeout in nanoseconds or sets it to never expire if null is passed. The `wait` method blocks until the pointer's value changes, Futex.wake() is called on the pointer, a spurious wakeup occurs, or the deadline expires, returning an error.Timeout if the deadline is reached. Specifically, in the `wait` method, the timeout duration is calculated by subtracting the elapsed time since the deadline was started from the initial timeout. If the elapsed time exceeds the initial timeout, the result is clamped to zero.

## Code Example
```zig
pub fn init(expires_in_ns: ?u64) Deadline {
		var deadline: Deadline = undefined;
		deadline.timeout = expires_in_ns;

		// std.time.Timer is required to be supported for somewhat accurate reportings of error.Timeout.
		if (deadline.timeout != null) {
			deadline.started = main.timestamp();
		}

		return deadline;
	}
```

## Related Questions
- What is the purpose of the Deadline struct?
- How does the init function initialize a Deadline?
- What does the wait method do in the Deadline struct?
- How does the Deadline handle spurious wakeups?
- What error can be returned by the wait method?
- How is the timeout duration calculated in the wait method?

*Source: unknown | chunk_id: codebase_src_utils_Futex.zig_chunk_7*
