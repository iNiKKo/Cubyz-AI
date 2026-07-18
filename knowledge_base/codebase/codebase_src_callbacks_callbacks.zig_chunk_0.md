# [easy/codebase_src_callbacks_callbacks.zig] - Chunk 0

**Type:** api
**Keywords:** callback, event handling, vtable, initialization, error handling
**Symbols:** ClientBlockCallback, ServerBlockCallback, BlockTouchCallback, Result, Creator, Callback, SimpleCallback
**Concepts:** callback mechanism, block interactions, vtable pattern

## Summary
Defines callback mechanisms for block interactions in the Cubyz engine, including client and server block callbacks, touch callbacks, and simple callbacks.

## Explanation
This chunk defines various callback structures and functions used to handle block interactions within the Cubyz engine. It includes `ClientBlockCallback`, `ServerBlockCallback`, and `BlockTouchCallback` for different types of block events. The `Callback` function template is used to create these callback types, managing initialization and execution through a vtable mechanism. Each callback type has specific parameters and return types as follows:

- **ClientBlockCallback**: Takes a struct with fields `block: Block`, `chunk: *main.chunk.Chunk`, and `blockPos: Vec3i`. The function returns an enum value of `Result` (`handled` or `ignored`).
- **ServerBlockCallback**: Takes a struct with fields `block: Block`, `chunk: *main.chunk.ServerChunk`, and `blockPos: main.chunk.BlockPos`. The function also returns an enum value of `Result`.
- **BlockTouchCallback**: Takes a struct with fields `entity: *main.server.Entity`, `source: Block`, `blockPos: Vec3i`, and `deltaTime: f64`. This callback also returns an enum value of `Result`.

The `init` function initializes global callback maps for each type, ensuring that the necessary vtables are set up. It checks for a required `

## Code Example
```zig
pub const Result = enum { handled, ignored };
```

## Related Questions
- What are the specific parameters and return types for each block callback?
- How does the `globalInit` method handle missing or unknown event types?

*Source: unknown | chunk_id: codebase_src_callbacks_callbacks.zig_chunk_0*
