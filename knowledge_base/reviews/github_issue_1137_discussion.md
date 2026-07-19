# [issues/issue_1137.md] - Issue #1137 discussion

**Type:** review
**Keywords:** swing improvements, durability decrease, block breaking registration, swing cancellation prevention, damage state, auto-healing, explosions, server synchronization
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue discusses improvements to the swinging mechanics in Cubyz, focusing on real-time durability decrease, block breaking registration, and swing cancellation prevention. The maintainer suggests preserving damage states for blocks to support future features like explosions and auto-healing.

## Explanation
The issue discusses improvements to the swinging mechanics in Cubyz, focusing on real-time durability decrease, block breaking registration per swing, and preventing swing cancellation unless hotbar slots are switched. The maintainer suggests preserving a damage state for blocks that were damaged by tools, which can be used for future features like explosions or decaying leaves. This auto-healing mechanism would restore part of the damage (e.g., 10% max health) every N ticks and should not persist between leaving and joining the world. Damage states are to be synced with the server and retained across players.

## Related Questions
- What specific changes will be made to ensure tools break correctly in real-time?
- How will block breaking registration per swing improve the user experience?
- Under what conditions can a swing be cancelled, and how does this affect gameplay?
- Can you explain the maintainer's suggestion for preserving damage states on blocks?
- What are the exact mechanics of auto-healing damaged blocks?

*Source: unknown | chunk_id: github_issue_1137_discussion*
