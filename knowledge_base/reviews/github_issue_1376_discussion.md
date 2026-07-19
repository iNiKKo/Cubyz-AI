# [issues/issue_1376.md] - Issue #1376 discussion

**Type:** review
**Keywords:** vendor-specific compiler errors, Intel's drivers, AMD's drivers, non-opaque uniforms, Vulkan support, #1379
**Concepts:** OpenGL, Vulkan, SPIR-V shaders

## Summary
The discussion revolves around switching to SPIR-V shaders to reduce vendor-specific compiler errors and pave the way for future Vulkan support.

## Explanation
Switching to SPIR-V shaders reduces problems from vendor-specific compiler errors and marks a first step towards future Vulkan support. By using SPIR-V, developers can ensure compatibility across different graphics drivers, avoiding issues related to specific vendors' implementations of OpenGL. This change also paves the way for better performance and more efficient use of resources in the graphics pipeline, ultimately leading to improved overall game stability and user experience.

## Related Questions
- What are the main issues with OpenGL drivers on Intel and AMD hardware?
- How does Vulkan differ from OpenGL in terms of uniform handling?
- Why is #1379 being suggested as a preparatory step for Vulkan support?
- What specific problems are addressed by switching to SPIR-V shaders?
- How does this change impact the overall architecture of the graphics pipeline?
- Are there any potential performance implications from switching to SPIR-V shaders?

*Source: unknown | chunk_id: github_issue_1376_discussion*
