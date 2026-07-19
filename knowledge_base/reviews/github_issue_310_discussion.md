# [issues/issue_310.md] - Issue #310 discussion

**Type:** review
**Keywords:** player coordinates, fixed point, wraparound, block positions, fragment positions, overflow, integer limit, teleportation, visibility, biome borders
**Symbols:** _getBiome, InterpolatableCaveBiomeMapView, src/server/command
**Concepts:** coordinate wraparound, world position, rotation transform, biome generation

## Summary
Discussion about implementing player coordinate wraparound and understanding fragment positions in Cubyz.

## Explanation
Discussion about implementing player coordinate wraparound at integer limits. The user inquires about modifying the limit for testing purposes within the `/tp` command located in `src/server/command`. There is confusion regarding the correspondence between block and fragment positions, noting that inputs to the `_getBiome()` function overflow around 773000000 instead of the expected integer limit. The maintainer clarifies that these are world positions scaled by one voxel (LOD0). The rotation transform in `InterpolatableCaveBiomeMapView.getRoughBiome()` is applied to rotate input coordinates, using a smallest Pythagorean triple for simplicity without exact angles specified. The user questions whether teleportation at the border will allow visibility of wrapped-around chunks, and the maintainer confirms that it should be possible.

## Related Questions
- Where is the `/tp` command defined in Cubyz?
- What causes the overflow of inputs to `_getBiome()` function?
- How does the rotation transform in `InterpolatableCaveBiomeMapView.getRoughBiome()` affect biome generation?
- Can you explain the significance of using a smallest Pythagorean triple for the rotation transform?
- How does the wraparound implementation impact memory usage or performance?

*Source: unknown | chunk_id: github_issue_310_discussion*
