# [issues/issue_1634.md] - Issue #1634 discussion

**Type:** review
**Keywords:** vector, memory layout, extern, GLSL, fixed-width arrays, alignment, uniforms, ptrCast
**Symbols:** QuadInfo, ChunkData, Particle, Vec3f
**Concepts:** memory layout, GLSL compatibility, extern structs

## Summary
The issue discusses the removal of vectors in `extern` structs due to lack of guaranteed memory layout, suggesting replacing them with fixed-width arrays for compatibility with GLSL.

## Explanation
The discussion centers around the requirement to avoid using Zig's vector types (`Vec3f`) in `extern` structs because they do not have a guaranteed memory layout, which is critical for interfacing with languages like GLSL. The maintainers suggest replacing these vectors with fixed-width arrays (e.g., `align(16) [3]f32`) to ensure predictable memory layouts. Users propose optimizing vector usage by only changing those passed into GLSL APIs ending with 'v', but the maintainer clarifies that this is unnecessary for `extern` structs and that casting vectors to array pointers remains safe.

## Related Questions
- What is the impact of using vectors in `extern` structs on GLSL compatibility?
- How can we ensure that vector types maintain a consistent memory layout in Zig?
- Are there any performance implications when replacing vectors with fixed-width arrays?
- Can we safely use `@ptrCast` between vector and array pointers in all contexts?
- What are the potential optimizations for passing vectors into GLSL APIs?
- How does changing vector types affect the overall memory usage of the application?

*Source: unknown | chunk_id: github_issue_1634_discussion*
