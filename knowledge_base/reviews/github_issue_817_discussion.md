# [issues/issue_817.md] - Issue #817 discussion

**Type:** review
**Keywords:** volumetric fog, ARB_fragment_shader_interlock, Vulkan, performance impact, AMD support, depth buffer copying, transparent rendering, device coverage, visual artifacts, fallback path
**Symbols:** ARB_fragment_shader_interlock, impossible_fog branch
**Concepts:** performance optimization, hardware compatibility, fallback mechanism

## Summary
Discussion on optionally using the `ARB_fragment_shader_interlock` extension for volumetric fog, considering performance and compatibility across different hardware.

## Explanation
The discussion revolves around implementing an optional feature to use the `ARB_fragment_shader_interlock` extension in Vulkan for improved volumetric fog rendering. The maintainer initially implemented a prototype which resolved visual artifacts but found that the performance gains were marginal due to additional depth buffer copying costs. The user pointed out that modern AMD GPUs support this extension, suggesting it might be worth revisiting in the future as more devices gain support. The fallback path for unsupported hardware would remain the current implementation without significant visual changes.

## Related Questions
- What is the performance impact of using `ARB_fragment_shader_interlock` on Intel iGPUs?
- How does the depth buffer copying cost affect the overall performance gain?
- What are the visual improvements expected from using this extension?
- Why was it decided not to implement this feature despite its benefits?
- What is the current fallback mechanism for unsupported hardware?
- How will the implementation ensure compatibility with older GPUs?

*Source: unknown | chunk_id: github_issue_817_discussion*
