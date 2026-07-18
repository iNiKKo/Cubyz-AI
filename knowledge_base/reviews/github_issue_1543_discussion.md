# [issues/issue_1543.md] - Issue #1543 discussion

**Type:** review
**Keywords:** Vulkan, OpenGL, ray tracing, modding, Cubyz, rewrite, memory sharing, cross-platform, performance, integration, screenshot, real-time rendering
**Symbols:** Vulkan, OpenGL, ray tracing, modding, Cubyz
**Concepts:** rendering architecture, moddable interface, GPU memory sharing, cross-platform support, performance optimization

## Summary
Discussion on providing modding support for custom ray tracing renderers in Cubyz, focusing on potential solutions and architectural considerations.

## Explanation
The discussion revolves around the feasibility and methods to allow third-party ray tracing implementations through modding. The maintainer suggests that while rewriting the rendering engine to Vulkan is being considered (#102), it's a complex task with significant maintenance overhead. Users propose several options, including sharing GPU memory between Vulkan and OpenGL, blitting Vulkan images into OpenGL textures, and abstracting the rendering at higher levels. The maintainer notes that for screenshots, a separate Vulkan renderer could suffice, but integration with the existing UI is crucial for real-time rendering.

## Related Questions
- What are the potential performance implications of blitting Vulkan images into OpenGL textures?
- How can cross-platform support be achieved when sharing GPU memory between Vulkan and OpenGL?
- What are the advantages and disadvantages of abstracting the rendering at a higher level in Cubyz?
- How can the existing UI be integrated with a separate Vulkan renderer for real-time ray tracing?
- What is the current status of the Vulkan rewrite project in Cubyz?
- How can modders disable OpenGL world rendering while still using it for presentation?
- What are the potential challenges in implementing GPU->CPU->GPU copy for rendering purposes?
- How can developers contribute to the ongoing Vulkan rewrite project in Cubyz?
- What are the benefits of keeping the current rendering engine in OpenGL but using Vulkan for presentation?
- How can modders obtain relevant CPU data needed for custom rendering implementations?

*Source: unknown | chunk_id: github_issue_1543_discussion*
