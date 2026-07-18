# [issues/issue_1832.md] - Issue #1832 discussion

**Type:** review
**Keywords:** GPU freezing, item model rendering, out-of-range values, SSBO, texture sampler, OpenGL behavior
**Symbols:** OpenGL, fragment shader, 2x2 quads, SSBO, texture sampler
**Concepts:** GPU debugging, illegal memory access

## Summary
The issue involves GPU freezing due to illegal memory access during item model rendering.

## Explanation
The issue involves GPU freezing due to illegal memory access during item model rendering. Specifically, OpenGL runs fragment shaders on 2x2 quads even if they fall outside the given triangle, resulting in out-of-range values being sampled from an SSBO (Shader Storage Buffer Object). This leads to a graphics driver log message: `amdgpu: amdgpu_cs_query_fence_status failed.` The game freezes for exactly 10 seconds during this issue. The maintainer notes that this problem is rare and difficult to reproduce, as it occurs randomly during block breaking or at specific angles.

## Related Questions
- What is the specific condition under which the fragment shader runs on out-of-range quads?
- How does the texture sampler handle out-of-range values for normal textures?
- Can you provide more details on how to debug illegal memory access in GPU shaders?
- Is there a known workaround or fix for this OpenGL behavior?
- What are the implications of using SSBOs in shader rendering?
- How can we modify the shader code to prevent out-of-range sampling from SSBOs?

*Source: unknown | chunk_id: github_issue_1832_discussion*
