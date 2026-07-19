# [issues/issue_228.md] - Issue #228 discussion

**Type:** review
**Keywords:** OpenGL, GLX, compute shaders, shader storage buffers, Mesa Zink, Vulkan, LLVMpipe, software rasterization
**Concepts:** OpenGL, GPU, Shader, Compatibility

## Summary
The maintainer decides not to support older OpenGL versions due to the need for modern GPU features like compute shaders and shader storage buffers. The user expresses concern about compatibility with older hardware.

## Explanation
The maintainer decides not to support older OpenGL versions due to the need for modern GPU features like compute shaders and shader storage buffers. The user expresses concern about compatibility with older hardware, such as Intel integrated GPUs from around 2012. The maintainer explains that while they understand the desire for broader compatibility, supporting older OpenGL versions would require significant effort and limit their ability to implement advanced features using newer GPU capabilities. They also note that most modern GPUs should support OpenGL 4.6 within the next decade. The user argues that many people still use older hardware, but the maintainer prioritizes developing new game features over maintaining compatibility with outdated systems. Potential solutions such as updating drivers or using API translation layers like Mesa Zink are discussed, but the maintainer admits to limited knowledge about these options and their feasibility. The user points out that software rasterization like LLVMpipe could theoretically offer OpenGL 4.6 support without GPU acceleration, but at a severe performance cost. The maintainer remains committed to using modern GPU features and closes the issue, noting that compatibility with older hardware will naturally improve over time as newer GPUs become more prevalent.

## Related Questions
- What are the specific OpenGL features required by Cubyz that necessitate version 3.4 or higher?
- How does the maintainer plan to address compatibility issues with older GPUs in the future?
- Can Mesa Zink be used as a viable solution for running Cubyz on systems with older OpenGL support?
- What are the potential performance implications of using software rasterization like LLVMpipe for rendering Cubyz?
- Are there any alternative API translation layers that could potentially support older OpenGL versions?
- How does the maintainer justify prioritizing new feature development over maintaining compatibility with older hardware?

*Source: unknown | chunk_id: github_issue_228_discussion*
