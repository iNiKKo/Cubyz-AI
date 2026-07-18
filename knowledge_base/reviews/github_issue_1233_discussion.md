# [issues/issue_1233.md] - Issue #1233 discussion

**Type:** review
**Keywords:** GPU memory exhaustion, hyperspeed movement, screen blanking, OpenGL SSBO limit, internal mesh buffer resizing
**Symbols:** Cubyz, GPU VRAM, OpenGL, SSBO
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The game exhausts GPU VRAM when moving with hyperspeed, causing screen blanking and requiring a reset. The issue is likely due to OpenGL's limitation on SSBO sizes.

## Explanation
The problem arises when the internal mesh buffer exceeds 2 GiB, which OpenGL does not support for continuous SSBOs. This leads to an out-of-memory error, causing the game to become unresponsive. The maintainer suggests checking if the resizing message is printed right before the issue occurs to confirm this hypothesis.

## Related Questions
- What is the maximum size of an SSBO in OpenGL?
- How can we optimize memory usage for large buffers in Cubyz?
- Are there any alternative data structures that could be used to avoid SSBO limitations?
- Can we implement a fallback mechanism when GPU memory is exhausted?
- How does the game's LOD (Level of Detail) affect memory consumption?
- What are the implications of increasing the internal mesh buffer size beyond 2 GiB?

*Source: unknown | chunk_id: github_issue_1233_discussion*
