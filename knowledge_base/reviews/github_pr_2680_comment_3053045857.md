# [src/entityModel.zig] - PR #2680 review diff

**Type:** review
**Keywords:** EntityModel, VertexArray, Texture, BinaryReader, NeverFailingAllocator, Mat4f, Vec3d, Vec3f, Vec4f, file paths, resource loading, modularity
**Symbols:** EntityModel, VertexArray, Texture, BinaryReader, NeverFailingAllocator, Mat4f, Vec3d, Vec3f, Vec4f
**Concepts:** memory management, modularity, resource loading, architectural design

## Summary
Refactored `EntityModel` struct to store paths instead of directly loading resources, reducing memory footprint and improving modularity.

## Explanation
The reviewer suggests modifying the `EntityModel` struct to store file paths rather than loading assets immediately. This change aims to optimize memory usage by deferring resource loading until necessary. The review also notes that the `id` field is already present, which can be used to identify and locate assets within a per-world asset folder managed by the assets store. This architectural adjustment enhances modularity and scalability, allowing for more efficient management of resources across different game worlds.

## Related Questions
- How does the change in storing file paths instead of directly loading resources affect memory usage?
- What is the purpose of using the `id` field to identify assets within a per-world asset folder?
- How does this refactoring improve the modularity of the game engine?
- Can you explain the benefits of deferring resource loading until necessary?
- How might this change impact performance in scenarios with limited memory resources?
- What are the potential implications for backwards compatibility with existing code?

*Source: unknown | chunk_id: github_pr_2680_comment_3053045857*
