# [hard/codebase_src_network.zig] - Chunk 0

**Type:** networking
**Keywords:** import, timestamp, inline, atomic, milliseconds
**Symbols:** Atomic, game, settings, utils, NeverFailingAllocator, authentication, protocols, ms, networkTimestamp
**Concepts:** networking

## Summary
This chunk imports necessary modules and sets up constants for the networking subsystem, including a timestamp function.

## Explanation
The chunk begins by importing standard library modules such as `builtin`, `std`, and custom modules like `main`, `game`, `settings`, `utils`, and `NeverFailingAllocator`. It then re-exports two submodules: `authentication` and `protocols`. The C standard library is also imported. A constant `ms` is defined to represent one thousand milliseconds. An inline function `networkTimestamp` is provided, which calculates the current timestamp in milliseconds by converting nanoseconds to milliseconds.

## Related Questions
- What modules are imported in the networking subsystem?
- How is the timestamp calculated in milliseconds?
- Which submodules are re-exported by this chunk?
- What does the `ms` constant represent?
- Is SSL or similar encoding used for messages?
- Where is the C standard library imported from?

*Source: unknown | chunk_id: codebase_src_network.zig_chunk_0*
