# [src/gui/windows/debug.zig] - PR #161 review diff

**Type:** review
**Keywords:** atomic, load(), memory order, Monotonic, thread safety, data race, debugging, performance, correctness
**Symbols:** draw.print, main.game.world.manager.connections.items.len, Connection.packetsSent.value
**Concepts:** thread safety, atomic operations, memory ordering

## Summary
The code was updated to correctly load atomic values by using `load()` method with appropriate memory ordering.

## Explanation
The reviewer identified that the original code incorrectly accessed an atomic value (`Connection.packetsSent.value`) without using the `load()` method, which is necessary for safely reading atomic variables. The reviewer suggests using `Monotonic` memory order but recommends double-checking to ensure correctness. This change is crucial for maintaining thread safety and preventing potential data races.

## Related Questions
- What is the correct memory order to use with `Connection.packetsSent.value.load()`?
- How does using `load()` on atomic variables affect thread safety in Cubyz?
- Are there any other instances in the code where atomic values are being accessed incorrectly?
- What potential issues could arise from not using `load()` when accessing atomic variables?
- How can we ensure that all atomic variable accesses follow best practices for thread safety?
- Is there a specific reason why `Monotonic` memory order was chosen for these operations?

*Source: unknown | chunk_id: github_pr_161_comment_1375471237*
