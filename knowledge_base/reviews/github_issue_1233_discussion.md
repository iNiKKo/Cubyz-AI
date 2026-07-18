# [issues/issue_1233.md] - Issue #1233 discussion

**Type:** review
**Keywords:** GPU memory exhaustion, hyperspeed movement, screen blanking, OpenGL SSBO limit, internal mesh buffer resizing
**Symbols:** Cubyz, GPU VRAM, OpenGL, SSBO
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The game exhausts GPU VRAM when moving with hyperspeed, causing screen blanking and requiring a reset. The issue is likely due to OpenGL's limitation on SSBO sizes.

## Explanation
The issue arises when moving with hyperspeed in Cubyz, leading to GPU VRAM exhaustion and causing the screen to blank out. This problem is likely due to OpenGL's limitation on SSBO sizes exceeding 2 GiB, which results in an out-of-memory error. The maintainer suggests checking if the resizing message 'resizing internal mesh buffer from 2048 MiB to 4096 MiB' appears right before the issue occurs to confirm this hypothesis. Additionally, specific settings that contribute to high VRAM usage include render distance set to 11, LOD at 5, leaves quality at 4, opaque leaves distance of 200, FOV of 70, bloom enabled (yes), and VSync also enabled (yes).

## Related Questions
- What is the maximum size of an SSBO in OpenGL?
- How can we optimize memory usage for large buffers in Cubyz?
- Are there any alternative data structures that could be used to avoid SSBO limitations?
- Can we implement a fallback mechanism when GPU memory is exhausted?
- How does the game's LOD (Level of Detail) affect memory consumption?
- What are the implications of increasing the internal mesh buffer size beyond 2 GiB?
- What specific settings contribute to high VRAM usage during hyperspeed movement?

*Source: unknown | chunk_id: github_issue_1233_discussion*
