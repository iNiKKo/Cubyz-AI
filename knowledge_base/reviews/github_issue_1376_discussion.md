# [issues/issue_1376.md] - Issue #1376 discussion

**Type:** review
**Keywords:** vendor-specific compiler errors, Intel's drivers, AMD's drivers, non-opaque uniforms, Vulkan support, #1379
**Concepts:** OpenGL, Vulkan, SPIR-V shaders

## Summary
The discussion revolves around switching to SPIR-V shaders to reduce vendor-specific compiler errors and pave the way for future Vulkan support.

## Explanation
The maintainer comments on the poor support of certain OpenGL features in Intel's and AMD's drivers, highlighting that Vulkan has stricter requirements regarding non-opaque uniforms. The discussion suggests implementing #1379 as a preparatory step to ease the transition towards Vulkan support.

## Related Questions
- What are the main issues with OpenGL drivers on Intel and AMD hardware?
- How does Vulkan differ from OpenGL in terms of uniform handling?
- Why is #1379 being suggested as a preparatory step for Vulkan support?
- What specific problems are addressed by switching to SPIR-V shaders?
- How does this change impact the overall architecture of the graphics pipeline?
- Are there any potential performance implications from switching to SPIR-V shaders?

*Source: unknown | chunk_id: github_issue_1376_discussion*
