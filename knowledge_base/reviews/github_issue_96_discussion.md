# [issues/issue_96.md] - Issue #96 discussion

**Type:** review
**Keywords:** fps, gpu time, bloom effect, fragment shader, triangle count, vertex shader, optimization, downsampling, chunk rendering, lag spikes
**Symbols:** bloom, fragment shader, opaque geometry, triangle count, vertex shader
**Concepts:** performance optimization, GPU performance, CPU performance

## Summary
The issue discusses and addresses performance bottlenecks in Cubyz, focusing on FPS and GPU time. Bloom effect is optimized by defaulting to off, and further optimizations are suggested for fragment shaders and triangle count.

## Explanation
The discussion revolves around optimizing the performance of Cubyz, particularly addressing low FPS and high GPU times. The maintainer comments indicate that while some improvements have been made (such as speeding up bloom passes), significant areas like downsampling remain slow. Further optimizations are suggested for chunk rendering and CPU-side processing to address lag spikes.

## Related Questions
- What specific changes were made to the bloom effect in commit 72e27e85003ddd8d32852cbae75200f36b6c7e34?
- How does the fragment shader optimization impact the overall performance of Cubyz?
- What are the potential implications of reducing the triangle count in Cubyz?
- Can you provide more details on how CPU-side optimizations were implemented to address lag spikes?
- How does downsampling contribute to the current GPU time issues, and what further improvements can be made?
- What is the relationship between the vertex shader execution frequency and overall performance?

*Source: unknown | chunk_id: github_issue_96_discussion*
