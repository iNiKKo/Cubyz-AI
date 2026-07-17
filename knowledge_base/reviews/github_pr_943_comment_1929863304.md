# [src/game.zig] - Chunk 1929863304

**Type:** review
**Keywords:** Atomic, bool, ordering, sanitizer, race, connected, World, deinited, thread, memory, guarantees
**Symbols:** World, connected
**Concepts:** atomic operations, memory ordering, data race detection, thread sanitizer, synchronization primitives, struct field initialization order

## Summary
The change adds a `connected: Atomic(bool)` field to the `World` struct, but the reviewer argues that an atomic is insufficient for ordering guarantees and recommends leaving it non-atomic so data races can be detected by the thread sanitizer.

## Explanation
The architectural concern centers on memory ordering semantics. In Zig (and most languages), a simple `Atomic(bool)` provides release/acquire semantics only at the point of load/store, but does not guarantee that other fields in the same struct are observed in a consistent order relative to the connection state. If another thread reads `connected` after it is set, there is no guarantee that the related `conn` handle has been fully initialized or that any side effects tied to establishing the connection have completed. This could lead to subtle bugs where the UI thinks the world is connected while the underlying network layer is still tearing down or hasn't finished setup. By keeping the field non-atomic, any concurrent access will trigger a data race under the thread sanitizer, making such ordering issues visible during testing rather than silently allowing incorrect behavior. The reviewer thus prefers explicit synchronization (e.g., using a mutex or a dedicated event) and letting the sanitizer catch races if the code is written incorrectly.

## Related Questions
- What synchronization primitive should replace the atomic bool for the connected field?
- How does Zig's Atomic type differ from C++ std::atomic regarding memory ordering guarantees?
- Can we use a mutex to protect reads and writes of the connected flag in World?
- What are the performance implications of using a non-atomic bool vs an atomic bool for this use case?
- How would the thread sanitizer report a data race if connected is accessed without proper ordering?
- Is there a way to combine an atomic with a separate event or condition variable for connection state?
- What happens if another thread reads connected before the initialization of related fields completes?
- Could we use Zig's @atomicRmw or similar operations to ensure consistent updates to connected?
- How does the reviewer's suggestion align with best practices in concurrent game loop design?
- What changes are needed in the codebase if we decide to keep connected non-atomic and rely on sanitizer feedback?

*Source: unknown | chunk_id: github_pr_943_comment_1929863304*
