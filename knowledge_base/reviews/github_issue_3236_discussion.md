# [issues/issue_3236.md] - Issue #3236 discussion

**Type:** review
**Keywords:** Panini projection, fisheye, shader, curved triangles, framebuffer, post-processing, base game, future shader support
**Concepts:** shader support, hardware acceleration, framebuffer, post-processing

## Summary
Discussion about implementing non-rectilinear projections like Panini or fisheye in Cubyz, noting potential hardware limitations and future shader support.

## Explanation
Discussion about implementing non-rectilinear projections like Panini or fisheye in Cubyz. The user suggests these effects could be implemented using shaders but notes a lack of resources, providing specific examples such as Panini and fisheye projections along with links to shader examples (https://www.shadertoy.com/view/Wt3fzB, https://www.shadertoy.com/view/X3GcWW) and a video resource (https://www.youtube.com/watch?v=LE9kxUQ-l14). The maintainer points out that current hardware does not support drawing curved triangles directly, necessitating the use of a larger framebuffer and post-processing pass, which is deemed unsuitable for the base game due to performance implications. However, future shader support is anticipated to enable such effects. Additionally, any changes would require a restart.

## Related Questions
- What are the current limitations of hardware in supporting non-rectilinear projections?
- How could future shader support enable the implementation of Panini or fisheye projections?
- What is the impact of using a larger framebuffer and post-processing pass on performance?
- Are there any existing resources or documentation for implementing Panini projection shaders?
- How might user settings be integrated to toggle between different projection types in Cubyz, requiring a restart?
- What are the potential benefits of adding fisheye projection support to Cubyz?

*Source: unknown | chunk_id: github_issue_3236_discussion*
