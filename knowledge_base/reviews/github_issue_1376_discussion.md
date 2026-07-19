# [issues/issue_1376.md] - Issue #1376 discussion

**Type:** review
**Keywords:** vendor-specific compiler errors, Intel's drivers, AMD's drivers, non-opaque uniforms, Vulkan support, #1379
**Concepts:** OpenGL, Vulkan, SPIR-V shaders

## Summary
The discussion revolves around switching to SPIR-V shaders to reduce vendor-specific compiler errors and pave the way for future Vulkan support.

## Explanation
Switching to SPIR-V shaders reduces problems from vendor-specific compiler errors and marks a first step towards future Vulkan support. By using SPIR-V, developers can ensure compatibility across different graphics drivers, avoiding issues related to specific vendors' implementations of OpenGL. This change also paves the way for better performance and more efficient use of resources in the graphics pipeline, ultimately leading to improved overall game stability and user experience.

The main issues with OpenGL drivers on Intel and AMD hardware are vendor-specific compiler errors. Vulkan doesn't allow non-opaque uniforms (uniforms outside of uniform blocks), which seem to be the main issue for drivers here. Implementing #1379 would make transitioning to Vulkan easier by addressing these specific driver-related problems.

Switching to SPIR-V shaders addresses several specific problems:
- It resolves vendor-specific compiler errors on Intel and AMD hardware.
- It avoids issues related to non-opaque uniforms in OpenGL drivers.
- It paves the way for better performance and more efficient use of resources in the graphics pipeline.

This change impacts the overall architecture of the graphics pipeline by ensuring compatibility across different vendors' implementations, leading to improved game stability and user experience.

## Related Questions
- What are the main issues with OpenGL drivers on Intel and AMD hardware?
- How does Vulkan differ from OpenGL in terms of uniform handling?
- Why is #1379 being suggested as a preparatory step for Vulkan support?
- What specific problems are addressed by switching to SPIR-V shaders?

*Source: unknown | chunk_id: github_issue_1376_discussion*
