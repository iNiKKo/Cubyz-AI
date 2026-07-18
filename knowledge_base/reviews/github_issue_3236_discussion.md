# [issues/issue_3236.md] - Issue #3236 discussion

**Type:** review
**Keywords:** Panini projection, fisheye, shader, curved triangles, framebuffer, post-processing, base game, future shader support
**Concepts:** shader support, hardware acceleration, framebuffer, post-processing

## Summary
Discussion about implementing non-rectilinear projections like Panini or fisheye in Cubyz, noting potential hardware limitations and future shader support.

## Explanation
The issue discusses the desire to add projection types such as Panini or fisheye to Cubyz. The user mentions that these effects could be implemented using shaders but highlights a lack of resources. The maintainer points out that current hardware does not support drawing curved triangles directly, making it necessary to use a larger framebuffer and post-processing pass, which is deemed unsuitable for the base game. However, future shader support is anticipated to enable such effects.

## Related Questions
- What are the current limitations of hardware in supporting non-rectilinear projections?
- How could future shader support enable the implementation of Panini or fisheye projections?
- What is the impact of using a larger framebuffer and post-processing pass on performance?
- Are there any existing resources or documentation for implementing Panini projection shaders?
- How might user settings be integrated to toggle between different projection types in Cubyz?
- What are the potential benefits of adding fisheye projection support to Cubyz?

*Source: unknown | chunk_id: github_issue_3236_discussion*
