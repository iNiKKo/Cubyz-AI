# [issues/issue_1543.md] - Issue #1543 discussion

**Type:** review
**Keywords:** Vulkan, OpenGL, ray tracing, modding, Cubyz, rewrite, memory sharing, cross-platform, performance, integration, screenshot, real-time rendering
**Symbols:** Vulkan, OpenGL, ray tracing, modding, Cubyz
**Concepts:** rendering architecture, moddable interface, GPU memory sharing, cross-platform support, performance optimization

## Summary
Discussion on providing modding support for custom ray tracing renderers in Cubyz, focusing on potential solutions and architectural considerations.

## Explanation
Discussion on providing modding support for custom ray tracing renderers in Cubyz, focusing on potential solutions and architectural considerations. The maintainer suggests that while rewriting the rendering engine to Vulkan is being considered (#102), it's a complex task with significant maintenance overhead. Users propose several options including sharing GPU memory between Vulkan and OpenGL (option 2), blitting Vulkan images into OpenGL textures (option 3), and abstracting the rendering at higher levels (option 6). The maintainer notes that for screenshots, a separate Vulkan renderer could suffice but integration with the existing UI is crucial for real-time rendering. Specifically, users propose disabling OpenGL world rendering while still using it for presentation, obtaining relevant CPU data needed for custom rendering implementations, and implementing GPU->GPU copy as an optional optimization (option 3). The current status of the Vulkan rewrite project in Cubyz is that some setup stuff is already done but significant work remains.

## Related Questions
- What are the potential performance implications of blitting Vulkan images into OpenGL textures?
- How can cross-platform support be achieved when sharing GPU memory between Vulkan and OpenGL?
- What are the advantages and disadvantages of abstracting the rendering at a higher level in Cubyz?
- How can the existing UI be integrated with a separate Vulkan renderer for real-time ray tracing?
- What is the current status of the Vulkan rewrite project in Cubyz?
- How can modders disable OpenGL world rendering while still using it for presentation?
- What are the potential challenges in implementing GPU->CPU->GPU copy for rendering purposes?

*Source: unknown | chunk_id: github_issue_1543_discussion*
