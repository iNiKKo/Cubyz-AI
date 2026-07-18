# [issues/issue_310.md] - Issue #310 discussion

**Type:** review
**Keywords:** player coordinates, fixed point, wraparound, block positions, fragment positions, overflow, integer limit, teleportation, visibility, biome borders
**Symbols:** _getBiome, InterpolatableCaveBiomeMapView, src/server/command
**Concepts:** coordinate wraparound, world position, rotation transform, biome generation

## Summary
Discussion about implementing player coordinate wraparound and understanding fragment positions in Cubyz.

## Explanation
The discussion revolves around the implementation of player coordinate wraparound at integer limits. The user inquires about modifying the limit for testing purposes, specifically within the `/tp` command located in `src/server/command`. There is confusion regarding the correspondence between block and fragment positions, particularly noting that inputs to the `_getBiome()` function overflow around 773000000 instead of the expected integer limit. The maintainer clarifies that these are world positions scaled by one voxel (LOD0) and explains the rotation transform applied in `InterpolatableCaveBiomeMapView.getRoughBiome()`, although the exact angles are unknown. The user also questions whether teleportation at the border will allow visibility of wrapped-around chunks, to which the maintainer confirms that it should be possible.

## Related Questions
- Where is the `/tp` command defined in Cubyz?
- What causes the overflow of inputs to `_getBiome()` function?
- How does the rotation transform in `InterpolatableCaveBiomeMapView.getRoughBiome()` affect biome generation?
- Can you explain the significance of the smallest pythagorean triple used in the rotation transform?
- How does the wraparound implementation impact memory usage or performance?
- What are the potential side effects of modifying the integer limit for testing purposes?

*Source: unknown | chunk_id: github_issue_310_discussion*
