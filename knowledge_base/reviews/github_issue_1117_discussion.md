# [issues/issue_1117.md] - Issue #1117 discussion

**Type:** review
**Keywords:** panic, out of bounds, PerlinNoise, generateSmoothNoise, map fragment, worldSeed, voxelSize, thread safety, integer overflow, floating-point arithmetic
**Symbols:** generateMapFragment, PerlinNoise.generateSmoothNoise, getOrGenerateFragmentAndIncreaseRefCount, MapFragment.increaseRefCount, run, entryFn
**Concepts:** thread safety, floating-point arithmetic, integer overflow, noise generation

## Summary
A thread panic occurs due to an integer part of a floating-point value being out of bounds in the map generation process.

## Explanation
A thread panic occurs due to an integer part of a floating-point value being out of bounds in the map generation process. The specific error message is 'thread 32856 panic: integer part of floating point value out of bounds'. This issue arises from the function `generateMapFragment` in MapGenV1.zig, specifically at line 76 where PerlinNoise's `generateSmoothNoise` method is called with parameters that cause an overflow or underflow. The maintainer has acknowledged the need for a save file to reproduce and diagnose the issue. The exact error stack trace includes calls to `getOrGenerateFragmentAndIncreaseRefCount`, `run`, and `entryFn`. Additionally, another thread panic occurs at 'thread 5116' with similar symptoms. A save file named Save2.zip is provided to help reproduce this issue.

## Related Questions
- What is the range of values expected for `map.pos.wx` and `map.pos.wy` in `generateSmoothNoise`?
- How does the scaling factor affect the integer part of floating-point values in Perlin noise generation?
- Are there any existing checks or constraints on `worldSeed` that could prevent this overflow?
- What is the purpose of `MapFragment.increaseRefCount` and how might it be related to the error?
- How can we ensure thread safety when generating map fragments concurrently?
- Is there a possibility of integer overflow in other parts of the map generation code?
- What steps should be taken to validate input parameters before calling `generateSmoothNoise`?
- How does the `voxelSize` parameter influence the noise generation and potential out-of-bounds errors?

*Source: unknown | chunk_id: github_issue_1117_discussion*
