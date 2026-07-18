# [issues/issue_1117.md] - Issue #1117 discussion

**Type:** review
**Keywords:** panic, out of bounds, PerlinNoise, generateSmoothNoise, map fragment, worldSeed, voxelSize, thread safety, integer overflow, floating-point arithmetic
**Symbols:** generateMapFragment, PerlinNoise.generateSmoothNoise, getOrGenerateFragmentAndIncreaseRefCount, MapFragment.increaseRefCount, run, entryFn
**Concepts:** thread safety, floating-point arithmetic, integer overflow, noise generation

## Summary
A thread panic occurs due to an integer part of a floating-point value being out of bounds in the map generation process.

## Explanation
The error is triggered during the generation of a map fragment using Perlin noise. The specific line in MapGenV1.zig where the issue arises suggests that the parameters passed to generateSmoothNoise are causing an overflow or underflow, leading to an invalid integer value. This could be due to incorrect scaling or range checks for the floating-point values used in the noise generation process. The maintainer has acknowledged the need for a save file to reproduce and diagnose the issue.

## Related Questions
- What is the range of values expected for `map.pos.wx` and `map.pos.wy` in `generateSmoothNoise`?
- How does the scaling factor affect the integer part of floating-point values in Perlin noise generation?
- Are there any existing checks or constraints on `worldSeed` that could prevent this overflow?
- What is the purpose of `MapFragment.increaseRefCount` and how might it be related to the error?
- How can we ensure thread safety when generating map fragments concurrently?
- Is there a possibility of integer overflow in other parts of the map generation code?
- What steps should be taken to validate input parameters before calling `generateSmoothNoise`?
- How does the `voxelSize` parameter influence the noise generation and potential out-of-bounds errors?
- Are there any known issues with Perlin noise implementations that could lead to this type of error?
- How can we add logging or debugging information to trace the values causing the overflow?

*Source: unknown | chunk_id: github_issue_1117_discussion*
