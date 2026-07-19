# [issues/issue_1634.md] - Issue #1634 discussion

**Type:** review
**Keywords:** vector, memory layout, extern, GLSL, fixed-width arrays, alignment, uniforms, ptrCast
**Symbols:** QuadInfo, ChunkData, Particle, Vec3f
**Concepts:** memory layout, GLSL compatibility, extern structs

## Summary
The issue discusses the removal of vectors (`Vec3f`) from `extern` structs due to lack of guaranteed memory layout. It suggests replacing them with fixed-width arrays (e.g., `align(16) [3]f32`) for compatibility with GLSL and lists specific problematic places in the codebase.

## Explanation
The discussion centers around the requirement to avoid using Zig's vector types (`Vec3f`) in `extern` structs because they do not have a guaranteed memory layout, which is critical for interfacing with languages like GLSL. The maintainers suggest replacing these vectors with fixed-width arrays (e.g., `align(16) [3]f32`) to ensure predictable memory layouts. Problematic places include `QuadInfo` in `models.zig`, `ChunkData` in `chunk_meshing.zig`, and `Particle` in `particles.zig`. Users propose optimizing vector usage by only changing those passed into GLSL APIs ending with 'v', but the maintainer clarifies that this is unnecessary for `extern` structs and that casting vectors to array pointers remains safe. The maintainers also note that using `@ptrCast` from a vector to an array pointer is still safe.

## Related Questions
- What are the specific problematic places in the codebase where vectors need to be replaced?
- How do we ensure consistent memory layout for vectors used in extern structs?
- Can we safely use `@ptrCast` between vector and array pointers in all contexts?

*Source: unknown | chunk_id: github_issue_1634_discussion*
