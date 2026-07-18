# [easy/codebase_src_callbacks_callbacks.zig] - Chunk 0

**Type:** api
**Keywords:** callback, event handling, vtable, initialization, error handling
**Symbols:** ClientBlockCallback, ServerBlockCallback, BlockTouchCallback, Result, Creator, Callback, SimpleCallback
**Concepts:** callback mechanism, block interactions, vtable pattern

## Summary
Defines callback mechanisms for block interactions in the Cubyz engine, including client and server block callbacks, touch callbacks, and simple callbacks.

## Explanation
This chunk defines various callback structures and functions used to handle block interactions within the Cubyz engine. It includes `ClientBlockCallback`, `ServerBlockCallback`, and `BlockTouchCallback` for different types of block events. The `Callback` function template is used to create these callback types, managing initialization and execution through a vtable mechanism. Additionally, it provides a `SimpleCallback` struct for simpler callback scenarios with optional data. The chunk also includes an `init` function to initialize global callback maps and error handling for missing or unknown event types.

## Code Example
```zig
pub const Result = enum { handled, ignored };
```

## Related Questions
- What are the different types of block callbacks defined in this chunk?
- How does the `Callback` function template work?
- What is the purpose of the `globalInit` method in the `Callback` struct?
- How are simple callbacks initialized and executed?
- What error handling is implemented for missing or unknown event types?
- What is the role of the `noop` callback in this chunk?

*Source: unknown | chunk_id: codebase_src_callbacks_callbacks.zig_chunk_0*
