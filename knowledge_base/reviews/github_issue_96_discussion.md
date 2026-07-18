# [issues/issue_96.md] - Issue #96 discussion

**Type:** review
**Keywords:** fps, gpu time, bloom effect, fragment shader, triangle count, vertex shader, optimization, downsampling, chunk rendering, lag spikes
**Symbols:** bloom, fragment shader, opaque geometry, triangle count, vertex shader
**Concepts:** performance optimization, GPU performance, CPU performance

## Summary
The issue discusses and addresses performance bottlenecks in Cubyz, focusing on FPS and GPU time. Bloom effect is optimized by defaulting to off, and further optimizations are suggested for fragment shaders and triangle count.

## Explanation
The issue discusses and addresses performance bottlenecks in Cubyz, focusing on FPS and GPU time. The maintainer notes that a forest scene initially had 43 fps with 20 ms GPU time, indicating poor performance. Specific optimizations were identified: disabling bloom by default due to its high cost (working on multiple full f16 framebuffers), optimizing the fragment shader for opaque geometry, reducing triangle count from 4 million triangles, and improving vertex shader execution frequency. After implementing these changes, the maintainer reported that while bloom passes became faster, downsampling remained slow at around <3 ms post-processing time. Further optimizations are suggested for chunk rendering (reducing triangle count) and CPU-side processing to address lag spikes.

## Related Questions
- What specific changes were made to the bloom effect in commit 72e27e85003ddd8d32852cbae75200f36b6c7e34?
- How does the fragment shader optimization impact the overall performance of Cubyz?
- What are the potential implications of reducing the triangle count from 4 million triangles in Cubyz?
- Can you provide more details on how CPU-side optimizations were implemented to address lag spikes?
- How does downsampling contribute to the current GPU time issues, and what further improvements can be made?
- What is the relationship between the vertex shader execution frequency and overall performance?

*Source: unknown | chunk_id: github_issue_96_discussion*
