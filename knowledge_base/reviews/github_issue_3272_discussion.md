# [issues/issue_3272.md] - Issue #3272 discussion

**Type:** review
**Keywords:** texture flickering, OpenGL synchronization, glFinish, depth buffer, transparent rendering, opaque rendering, Vulkan rewrite, bloom effect, resolution scale, render distance
**Symbols:** glTextureBarrier, c.glFinish, WorldFrameBuffer.bindTexture, chunk_meshing.endRender
**Concepts:** synchronization, thread safety, performance costs

## Summary
The issue of violent texture flickering in Cubyz is caused by missing synchronization between opaque and transparent draw calls. The workaround involves adding `c.glFinish();` next to existing synchronization attempts, though it has significant performance costs.

## Explanation
The issue of violent texture flickering in Cubyz is caused by missing synchronization between opaque rendering (which writes to the depth buffer) and transparent rendering (which reads from but does not write to the depth buffer). The initial attempt at using `glTextureBarrier` was ineffective, possibly due to driver interpretation differences. Adding `c.glFinish();` as a brute-force solution temporarily resolves the issue by ensuring proper synchronization between opaque and transparent draw calls. However, this introduces substantial performance overhead. The maintainer suggests exploring cheaper synchronization options or waiting for improvements in Vulkan support (#102) to address the root cause. Specifically, adding `c.glFinish();` next to the existing `glTextureBarrier` call at line 290 did not resolve the issue completely, but placing it before transparent drawing at line 267 fixed the problem temporarily. The maintainer also tried using `c.glMemoryBarrier(c.GL_FRAMEBUFFER_BARRIER_BIT);`, which had similar performance issues and some residual flickering effects.

## Related Questions
-  What is the impact of adding `c.glFinish();` on performance?
-  How does the behavior change with different resolution scales?
-  Can `glMemoryBarrier(c.GL_FRAMEBUFFER_BARRIER_BIT);` be a viable alternative to `c.glFinish();`?
-  What are the potential long-term solutions for this issue after Vulkan support is improved?
-  Are there any other synchronization methods available in OpenGL that could be explored?
-  How does the flickering effect manifest with bloom enabled versus disabled?

*Source: unknown | chunk_id: github_issue_3272_discussion*
