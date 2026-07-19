# [issues/issue_1832.md] - Issue #1832 discussion

**Type:** review
**Keywords:** GPU freezing, item model rendering, out-of-range values, SSBO, texture sampler, OpenGL behavior
**Symbols:** OpenGL, fragment shader, 2x2 quads, SSBO, texture sampler
**Concepts:** GPU debugging, illegal memory access

## Summary
The issue involves GPU freezing due to illegal memory access during item model rendering.

## Explanation
The issue involves GPU freezing due to illegal memory access during item model rendering. Specifically, OpenGL runs fragment shaders on 2x2 quads even if they fall outside the given triangle, resulting in out-of-range values being sampled from an SSBO (Shader Storage Buffer Object). This leads to a graphics driver log message: `amdgpu: amdgpu_cs_query_fence_status failed.` The game freezes for exactly 10 seconds during this issue. For normal textures, the texture sampler automatically guards against out-of-range sampling, but here it is reading values from an SSBO, which does not have such protection. The maintainer notes that this problem is rare and difficult to reproduce, as it occurs randomly during block breaking or at specific angles. The OpenGL behavior of running fragment shaders on 2x2 quads even if they fall outside the given triangle can cause out-of-range values to be sampled from an SSBO, leading to illegal memory access. To debug illegal memory access in GPU shaders, one would typically use tools such as GPU debugging software or logs provided by the graphics driver. There is no known workaround or fix for this OpenGL behavior at the time of writing. The implications of using SSBOs in shader rendering include the need for careful handling to avoid out-of-range sampling and potential illegal memory access. To prevent out-of-range sampling from SSBOs, one could modify the shader code to ensure that all sampled values are within the valid range of the buffer. This might involve adding checks or clamping functions to the shader code.

## Related Questions
- What is the specific condition under which the fragment shader runs on out-of-range quads?
- How does the texture sampler handle out-of-range values for normal textures?
- Can you provide more details on how to debug illegal memory access in GPU shaders?
- Is there a known workaround or fix for this OpenGL behavior?
- What are the implications of using SSBOs in shader rendering?
- How can we modify the shader code to prevent out-of-range sampling from SSBOs?

*Source: unknown | chunk_id: github_issue_1832_discussion*
