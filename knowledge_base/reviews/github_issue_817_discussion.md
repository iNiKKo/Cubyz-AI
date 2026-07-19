# [issues/issue_817.md] - Issue #817 discussion

**Type:** review
**Keywords:** volumetric fog, ARB_fragment_shader_interlock, Vulkan, performance impact, AMD support, depth buffer copying, transparent rendering, device coverage, visual artifacts, fallback path
**Symbols:** ARB_fragment_shader_interlock, impossible_fog branch
**Concepts:** performance optimization, hardware compatibility, fallback mechanism

## Summary
Discussion on optionally using the `ARB_fragment_shader_interlock` extension for volumetric fog, considering performance and compatibility across different hardware.

## Explanation
Discussion on optionally using the `ARB_fragment_shader_interlock` extension for volumetric fog, considering performance and compatibility across different hardware. The maintainer implemented a prototype which resolved visual artifacts such as blooming pixel errors when looking at the fog backface and issues with large fog strength or distance. Performance testing showed an increase of ~600 µs in transparent rendering on Intel iGPUs but was offset by a depth buffer copying cost of ~500 µs, resulting in only a marginal overall performance improvement (~5-10%). Due to the small difference and additional code complexity, it was decided not to implement this feature for now. Modern AMD GPUs support this extension on Windows (and Linux), particularly Vulkan #102 on Polaris and later GPUs. However, since device coverage is around 40%, a fallback path remains necessary for older hardware, which would be the current implementation without significant visual changes.

## Related Questions
- What specific performance improvements were observed with `ARB_fragment_shader_interlock`?
- How does the depth buffer copying affect overall performance?
- What are the exact visual improvements from using this extension?
- Why was it decided not to implement this feature despite its benefits?
- What is the current fallback mechanism for unsupported hardware?

*Source: unknown | chunk_id: github_issue_817_discussion*
