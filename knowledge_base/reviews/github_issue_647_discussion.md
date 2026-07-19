# [issues/issue_647.md] - Issue #647 discussion

**Type:** review
**Keywords:** terrain mapping, sphere geometry, fog effect, vertex shaders, chunk wrapping, transparency issues, Earth curvature, spherical world, render optimization, voxel style
**Symbols:** #173, vertex shaders, chunk corners, transparency sorting, Earth's parameters
**Concepts:** vertex shaders, transparency sorting, curvature, render distance, voxel pixel art

## Summary
The discussion revolves around mapping terrain geometry onto a sphere to make far away terrain disappear beneath the horizon instead of fading into fog. Various methods and optimizations are discussed, including vertex shaders, chunk-based wrapping, and maintaining transparency sorting.

## Explanation
The discussion revolves around mapping terrain geometry onto a sphere to make far away terrain disappear beneath the horizon instead of fading into fog. Various methods and optimizations are discussed, including vertex shaders to bend the world geometry, which is suggested to be computationally expensive but potentially optimized by applying effects only at chunk corners with linear interpolation in between chunks. However, they encounter complications due to transparency sorting issues and the lack of noticeable visual difference when using Earth's curvature parameters. Another proposal involves applying wrapping effects only to chunks at the edge of the render distance to avoid unnatural appearances. The maintainers also reject the idea of making the entire world spherical due to the significant effort required and the lack of perceivable benefits in normal gameplay. There is a consensus that while some level of curvature could enhance the game's appearance, it should not disrupt the Euclidean style characteristic of the voxel pixel art. This approach requires issue #173 for proper implementation where there is no terrain and a large enough range.

## Related Questions
- How does the vertex shader approach affect performance?
- What are the potential issues with transparency sorting in this context?
- Why is applying effects only at chunk corners considered an optimization?
- How does the curvature of Earth impact the visual difference observed?
- What are the advantages and disadvantages of wrapping effects on edge chunks?
- Why is making the world spherical not recommended?
- How could a small level of curvature enhance the game's appearance without disrupting its style?

*Source: unknown | chunk_id: github_issue_647_discussion*
