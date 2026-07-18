# [easy/codebase_src_callbacks_block_client_edit_sign.zig] - Chunk 0

**Type:** api
**Keywords:** callback initialization, mutex locking, entity type checking, window opening, error handling
**Symbols:** init, run
**Concepts:** block editing, sign interaction, client-side logic

## Summary
Handles client-side editing of sign blocks.

## Explanation
This chunk defines two functions: `init` and `run`. The `init` function initializes a callback for block editing, returning an opaque pointer. The `run` function checks if the target block is a sign, locks a mutex to access sign data, retrieves the sign's text, and opens a sign editor window with this text. If the block is not a sign or the entity type does not match, it logs an error and returns 'ignored'.

## Code Example
```zig
pub fn init(_: ZonElement, _: main.callbacks.Creator) ?*anyopaque {
	return @as(*anyopaque, undefined);
}
```

## Related Questions
- What does the `init` function return?
- How does the `run` function check if a block is a sign?
- What happens if the block entity is not a sign in the `run` function?
- Which mutex is locked in the `run` function and why?
- How is the sign editor window opened with the retrieved text?
- What does the `run` function return after handling the sign editing?

*Source: unknown | chunk_id: codebase_src_callbacks_block_client_edit_sign.zig_chunk_0*
