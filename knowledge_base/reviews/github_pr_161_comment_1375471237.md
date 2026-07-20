# [src/gui/windows/debug.zig] - PR #161 review diff

**Type:** review
**Keywords:** atomic, load, memory order, Monotonic, thread safety, race condition, shared state
**Symbols:** draw.print, main.game.world.manager.connections.items.len, Connection.packetsSent.value
**Concepts:** thread safety, atomic operations, memory ordering

## Summary
The code was updated to correctly load an atomic value by using `load()` method with appropriate memory ordering.

## Explanation
The reviewer identified that the original code incorrectly accessed an atomic variable (`Connection.packetsSent.value`) without using the `load()` method, which is necessary for safely reading atomic values. The reviewer suggests using `Monotonic` memory order but advises double-checking to ensure correctness. This change is crucial for maintaining thread safety and preventing potential race conditions when accessing shared state.

The code now includes two new debug prints:
- `Connections number: {}`, which displays the length of `main.game.world.manager.connections.items.len`.
- `PacketsSent number: {}`, which displays the value of `Connection.packetsSent.value.load()` with the correct memory order (`Monotonic`).

The reviewer also noted that the current implementation uses `Monotonic` memory order, but it is recommended to double-check this for correctness.

## Related Questions
- What is the correct memory order to use with `Connection.packetsSent.value.load()`?
- How does using `Monotonic` memory order affect atomic operations in this context?
- Are there any potential performance implications of using `load()` with specific memory orders?
- Can you explain the difference between different memory orders in atomic operations?
- What is the purpose of the `draw.print` function in this code snippet?
- How does the length of `main.game.world.manager.connections.items.len` relate to network diagnostics?

*Source: unknown | chunk_id: github_pr_161_comment_1375471237*
