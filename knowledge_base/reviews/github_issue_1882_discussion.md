# [issues/issue_1882.md] - Issue #1882 discussion

**Type:** review
**Keywords:** SBBs, non-overlapping structures, bounding box, intersection checks, modular nature, world generation, caching, performance
**Concepts:** bounding box, intersection checks, modular structures, world generation

## Summary
The issue discusses the need for non-overlapping structures in Cubyz, particularly for hollow buildings, due to the modular nature of SBBs (Structure Block Bundles) which lack an easy-to-determine bounding box. The discussion explores efficient methods to handle intersection checks and caching of information to prevent overlapping during world generation.

## Explanation
The issue discusses the need for non-overlapping structures in Cubyz, particularly for hollow buildings, due to the modular nature of SBBs (Structure Block Bundles) which lack an easy-to-determine bounding box. The current method of handling structure positions is noise-based and prioritizes block placement, which is insufficient for preventing overlaps in hollow structures like buildings. The challenge lies in the modular nature of SBBs, making it difficult to determine a bounding box. The maintainer highlights that intersection checks are computationally expensive (O(n²) complexity), necessitating efficient solutions. The user suggests baking or caching information per structure during world generation to reuse and potentially limit the number of variants checked, aiming for an optimal balance between performance and accuracy. Additionally, artifacts like broken branches in trees, which are currently in-game and can be easily spotted, are mentioned as a concern that could be addressed by ensuring non-overlapping structures.

## Related Questions
- How can the bounding box for SBBs be efficiently determined or approximated?
- What are potential methods to cache intersection data during world generation?
- Can limiting the number of SBB variants reduce computational complexity in intersection checks?
- How does the current noise-based positioning system handle overlapping structures?
- What are the trade-offs between a too large and too small bounding box for SBBs?
- Are there existing algorithms that can be adapted for efficient intersection detection in modular structures?

*Source: unknown | chunk_id: github_issue_1882_discussion*
