# [issues/issue_1137.md] - Issue #1137 discussion

**Type:** review
**Keywords:** swing improvements, durability decrease, block breaking registration, swing cancellation prevention, damage state, auto-healing, explosions, server synchronization
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue discusses improvements to the swinging mechanics in Cubyz, focusing on real-time durability decrease, block breaking registration, and swing cancellation prevention. The maintainer suggests preserving damage states for blocks to support future features like explosions and auto-healing.

## Explanation
The discussion centers around enhancing the tool-swinging system to ensure tools break correctly and provide a more fluid user experience by allowing brief interruptions during block breaking. The maintainer proposes adding a damage state to blocks, which could be used for advanced mechanics such as explosions and auto-healing. This state would not persist between player sessions but would be synchronized across the server and among players.

## Related Questions
- What is the current implementation of tool durability in Cubyz?
- How does the proposed damage state for blocks affect performance?
- Can the auto-healing feature be implemented without introducing bugs?
- How will the new swing mechanics impact multiplayer gameplay?
- What are the potential backward compatibility issues with these changes?
- How will the server handle synchronization of block damage states?

*Source: unknown | chunk_id: github_issue_1137_discussion*
