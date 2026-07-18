# [easy/codebase_src_callbacks_block_server_vine_decay.zig] - Chunk 0

**Type:** implementation
**Keywords:** server-side logic, block rotation, world interaction, conditional replacement, atomic block change
**Symbols:** init, run, decay
**Concepts:** block server callbacks, vine decay, world manipulation

## Summary
Handles vine decay logic on the server side.

## Explanation
This chunk implements the server-side logic for handling vine decay. `run()` first verifies the block's rotation is `cubyz:hanging` (logging an error and returning `.ignored` otherwise), re-fetches the block at that world position to confirm it still matches, then checks the block directly above: if that block is a different type, decay is skipped (`.ignored`) unless the block above is `.replaceable()` (decays immediately) OR its model has no down-facing quads (`neighborFacingQuads[Neighbor.dirDown]` is empty -- decays anyway, since nothing is visually blocking it). `decay()` performs the actual replacement via `cmpxchgBlock`, an atomic compare-and-swap that only replaces the block with `blocks.Block.air` if it still matches the expected `current` value (returns `.handled` on success, `.ignored` if it changed underneath).

## Code Example
```zig
pub fn init(_: ZonElement, _: main.callbacks.Creator) ?*@This() {
	return main.worldArena.create(@This());
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `run` function determine if a block should decay?
- What happens if the block above the vine is not replaceable?
- How is the vine decayed in this code?
- What is the role of the `decay` function in the vine decay process?
- How does the chunk handle errors or invalid states?

*Source: unknown | chunk_id: codebase_src_callbacks_block_server_vine_decay.zig_chunk_0*
